"""Layered equivalence checker: does a "baked" checkpoint match the reference steering hook?

`bake.py` produces a variant checkpoint that encodes the steering intervention as a static
`down_proj` bias on one decoder block, instead of a forward hook:

    model.layers.{layer-1}.mlp.down_proj.bias == (float(coef) * vec[layer]).to(bfloat16)

everything else zero, config.mlp_bias = True. This script proves that swap is faithful, in three
independent layers of increasing scope:

  preflight  tensor-only, CPU: the baked bias IS the expected vector, everything else is zero.
             (always runs — cheap, catches a bad bake before any GPU time is spent)
  level 1    GPU, no server: HF-hook reference vs HF-loaded baked checkpoint. Next-token logits
             (argmax / max|d| / KL) and greedy-continuation token ids must agree.
  level 2    GPU + running vLLM server: vLLM-served baked checkpoint vs the HF-baked checkpoint.
             vLLM's kernels are not bit-identical to HF's, so greedy paths can fork at near-ties;
             the gate therefore TEACHER-FORCES vLLM's generated tokens through the HF-baked model
             and requires every step where HF's argmax disagrees to be a near-tie (top1-top2 logit
             gap < 0.5) and such steps to be rare (<= 10%). A raw common-prefix length is also
             reported, calibrated against an unsteered (base) pair, but it is informational only:
             where the first near-tie lands is prompt- and model-specific, so prefix length alone
             over- or under-states agreement.

Usage:

    # after bake.py writes /workspace/pvec_baked/goodness_c2_l16 :
    python -m persona_vector_steering.verify_bake --trait goodness --coef 2 --layer 16 --levels 1

    # once the vLLM server is up, serving that checkpoint as e.g. pvec:goodness:2:16
    # (and, for calibration, the base model as "base" — optional, see --base-served-model):
    python -m persona_vector_steering.verify_bake --trait goodness --coef 2 --layer 16 --levels 2 \\
        --base-url http://localhost:8000/v1 --served-model pvec:goodness:2:16

Exit code 0 iff every requested gate passes (a "benign near-tie divergence" warning still passes).
"""

from __future__ import annotations

import os

os.environ.setdefault("HF_HOME", "/workspace/.cache/huggingface")

import argparse
import gc
import json
import sys
from dataclasses import dataclass, field

import torch
from safetensors import safe_open
from transformers import AutoConfig, AutoModelForCausalLM

from . import config, steering

MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "You are going to speak to an AI model. Speak about whatever you "
                                "want. Just explain this to the other model."},
]


@dataclass
class GateResult:
    name: str
    passed: bool
    detail: str = ""
    warning: bool = False   # PASSed but worth flagging (e.g. benign near-tie, uncalibrated)


@dataclass
class HFPairData:
    """HF-side outputs for BOTH the steered (baked) and unsteered (base) conversation, plus the
    live models themselves — level 2's teacher-forced gate needs another forward pass through
    them. The caller frees the models (``_free(data.ref, data.cand)``) when done."""
    tok: object
    steered_gen_ids: list
    steered_top5: list
    base_gen_ids: list
    base_top5: list
    ref: object = None    # PersonaVectorSteeredModel (hooks inactive -> plain base model)
    cand: object = None   # the HF-loaded baked checkpoint
    enc: dict = None      # the tokenized prompt, on device


# --------------------------------------------------------------------------------------------- #
# shared helpers
# --------------------------------------------------------------------------------------------- #

def default_variant_dir(trait: str, coef: str, layer: str) -> str:
    return f"/workspace/pvec_baked/{trait}_c{coef}_l{layer}"


def default_served_model(trait: str, coef: str, layer: str) -> str:
    return f"pvec:{trait}:{coef}:{layer}"


def expected_bias(trait: str, coef: float, layer: int) -> torch.Tensor:
    """(float(coef) * vec[layer]).to(bfloat16) — the exact bias bake.py should have written."""
    path = config.vector_path(trait)
    if not os.path.exists(path):
        raise FileNotFoundError(f"persona vector not found: {path}")
    v = torch.load(path, weights_only=False, map_location="cpu")
    return (float(coef) * v[layer]).to(torch.bfloat16)


def _encode(tok, device: str) -> dict:
    enc = tok.apply_chat_template(
        MESSAGES, add_generation_prompt=True, return_tensors="pt", return_dict=True
    )
    return {k: v.to(device) for k, v in enc.items()}


def _kl_div(ref_logits: torch.Tensor, cand_logits: torch.Tensor) -> float:
    """KL(softmax_ref || softmax_cand), computed in fp32 for numerical stability."""
    ref_logp = torch.log_softmax(ref_logits.float(), dim=-1)
    cand_logp = torch.log_softmax(cand_logits.float(), dim=-1)
    ref_p = ref_logp.exp()
    return (ref_p * (ref_logp - cand_logp)).sum().item()


def _free(*objs) -> None:
    for o in objs:
        del o
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


# --------------------------------------------------------------------------------------------- #
# preflight — pure tensor checks, CPU ok, always runs
# --------------------------------------------------------------------------------------------- #

def _bias_tensor_map(variant_dir: str) -> dict[str, str]:
    """tensor name -> shard filename, for every tensor whose name ends in '.bias'."""
    index_path = os.path.join(variant_dir, "model.safetensors.index.json")
    if os.path.exists(index_path):
        with open(index_path) as f:
            weight_map = json.load(f)["weight_map"]
        return {name: fname for name, fname in weight_map.items() if name.endswith(".bias")}
    single = os.path.join(variant_dir, "model.safetensors")
    if os.path.exists(single):
        with safe_open(single, framework="pt") as f:
            return {name: "model.safetensors" for name in f.keys() if name.endswith(".bias")}
    raise FileNotFoundError(f"no model.safetensors(.index.json) found in {variant_dir!r}")


def run_preflight(trait: str, coef: str, layer: str, variant_dir: str) -> list[GateResult]:
    gates: list[GateResult] = []
    layer_i, coef_f = int(layer), float(coef)

    try:
        cfg = AutoConfig.from_pretrained(variant_dir)
    except Exception as e:  # noqa: BLE001
        gates.append(GateResult("load variant config", False, detail=f"{type(e).__name__}: {e}"))
        return gates

    mlp_bias = getattr(cfg, "mlp_bias", None)
    gates.append(GateResult("config.mlp_bias is True", mlp_bias is True, detail=f"mlp_bias={mlp_bias!r}"))

    try:
        name_to_file = _bias_tensor_map(variant_dir)
    except Exception as e:  # noqa: BLE001
        gates.append(GateResult("bias tensors located via safetensors index", False, detail=str(e)))
        return gates
    gates.append(GateResult("bias tensors located via safetensors index", True,
                             detail=f"{len(name_to_file)} bias tensors in weight map"))

    target_name = f"model.layers.{layer_i - 1}.mlp.down_proj.bias"
    if target_name not in name_to_file:
        gates.append(GateResult(f"{target_name} present in checkpoint", False,
                                 detail=f"not found among: {sorted(name_to_file)[:8]}..."))
        return gates

    try:
        expected = expected_bias(trait, coef_f, layer_i)
    except Exception as e:  # noqa: BLE001
        gates.append(GateResult("expected bias computed from vector file", False, detail=str(e)))
        return gates

    files_needed: dict[str, list[str]] = {}
    for name, fname in name_to_file.items():
        files_needed.setdefault(fname, []).append(name)

    target_ok, target_detail = False, "tensor not read"
    all_zero_ok, nonzero_examples = True, []
    for fname, names in files_needed.items():
        fpath = os.path.join(variant_dir, fname)
        with safe_open(fpath, framework="pt") as f:
            for name in names:
                t = f.get_tensor(name)
                if name == target_name:
                    target_ok = torch.equal(t, expected)
                    target_detail = (f"shape={tuple(t.shape)} dtype={t.dtype} "
                                      f"bitwise_equal_to_expected={target_ok}")
                else:
                    if not torch.equal(t, torch.zeros_like(t)):
                        all_zero_ok = False
                        nonzero_examples.append(f"{name} (max|.|={t.abs().max().item():.4g})")

    gates.append(GateResult(f"{target_name} == (coef * vec[layer]).bf16, bitwise", target_ok,
                             detail=target_detail))
    gates.append(GateResult("every other bias tensor is exactly all-zero", all_zero_ok,
                             detail="all zero" if all_zero_ok
                             else "nonzero: " + "; ".join(nonzero_examples[:5])))
    return gates


# --------------------------------------------------------------------------------------------- #
# level 1 — HF-baked vs HF-hook (GPU, no server)
# --------------------------------------------------------------------------------------------- #

def run_level1(trait: str, coef: str, layer: str, variant_dir: str, device: str | None,
                max_new_tokens: int) -> list[GateResult]:
    gates: list[GateResult] = []
    coef_f, layer_i = float(coef), int(layer)
    device = config.pick_device(device)

    ref = steering.load_steered(device)
    ref.register()
    ref.set_steering(trait, coef_f, layer_i)

    cand = AutoModelForCausalLM.from_pretrained(variant_dir, torch_dtype=torch.bfloat16)
    cand = cand.to(device).eval()

    tok = ref.tok
    enc = _encode(tok, device)

    # --- next-token logits -------------------------------------------------
    with torch.no_grad():
        ref_logits = ref.model(**enc).logits[0, -1, :]
        cand_logits = cand(**enc).logits[0, -1, :]

    ref_argmax, cand_argmax = ref_logits.argmax().item(), cand_logits.argmax().item()
    argmax_match = ref_argmax == cand_argmax
    delta = (ref_logits.float() - cand_logits.float()).abs()
    max_delta, mean_delta = delta.max().item(), delta.mean().item()
    kl = _kl_div(ref_logits, cand_logits)
    next_token_pass = argmax_match and max_delta < 1.0 and kl < 1e-3
    gates.append(GateResult(
        "next-token logits match (argmax equal, max|d|<1.0, KL<1e-3)", next_token_pass,
        detail=(f"argmax ref={ref_argmax} cand={cand_argmax} equal={argmax_match}; "
                f"max|d|={max_delta:.4g} mean|d|={mean_delta:.4g} KL={kl:.4g}"),
    ))

    # --- greedy continuation ------------------------------------------------
    pad_id = tok.eos_token_id
    gen_kw = dict(max_new_tokens=max_new_tokens, do_sample=False, pad_token_id=pad_id)
    input_len = enc["input_ids"].shape[1]
    with torch.no_grad():
        ref_out = ref.model.generate(**enc, **gen_kw)
        cand_out = cand.generate(**enc, **gen_kw)
    ref_gen = ref_out[0, input_len:].tolist()
    cand_gen = cand_out[0, input_len:].tolist()

    min_len = min(len(ref_gen), len(cand_gen))
    k = min_len
    for i in range(min_len):
        if ref_gen[i] != cand_gen[i]:
            k = i
            break
    exact_match = (ref_gen == cand_gen)

    if exact_match:
        gates.append(GateResult("greedy continuation exact match", True,
                                 detail=f"{len(ref_gen)} tokens identical"))
    else:
        prefix_ids = enc["input_ids"][0].tolist() + ref_gen[:k]
        prefix = torch.tensor([prefix_ids], device=device)
        with torch.no_grad():
            step_logits = ref.model(input_ids=prefix, attention_mask=torch.ones_like(prefix)).logits[0, -1, :]
        top2 = torch.topk(step_logits.float(), 2).values
        gap = (top2[0] - top2[1]).item()
        ref_text = tok.decode(ref_gen, skip_special_tokens=True)
        cand_text = tok.decode(cand_gen, skip_special_tokens=True)
        if gap < 0.5:
            gates.append(GateResult(
                "greedy continuation exact match", True, warning=True,
                detail=(f"diverged at token {k}: benign near-tie (top1-top2 gap={gap:.4g} < 0.5)\n"
                        f"    ref : {ref_text!r}\n    cand: {cand_text!r}"),
            ))
        else:
            gates.append(GateResult(
                "greedy continuation exact match", False,
                detail=(f"diverged at token {k}: top1-top2 gap={gap:.4g} (>= 0.5, not benign)\n"
                        f"    ref : {ref_text!r}\n    cand: {cand_text!r}"),
            ))

    ref.remove()
    _free(ref, cand)
    return gates


def compute_hf_pair_data(trait: str, coef: str, layer: str, variant_dir: str,
                          device: str | None, max_new_tokens: int) -> HFPairData:
    """All the HF-side data level 2 needs. Keeps the models loaded (for the teacher-forced gate);
    the caller frees them."""
    coef_f, layer_i = float(coef), int(layer)
    device = config.pick_device(device)

    ref = steering.load_steered(device)   # hooks registered but inactive -> plain base forward
    ref.register()
    cand = AutoModelForCausalLM.from_pretrained(variant_dir, torch_dtype=torch.bfloat16)
    cand = cand.to(device).eval()

    tok = ref.tok
    enc = _encode(tok, device)
    pad_id = tok.eos_token_id
    gen_kw = dict(max_new_tokens=max_new_tokens, do_sample=False, pad_token_id=pad_id)
    input_len = enc["input_ids"].shape[1]

    with torch.no_grad():
        base_logits = ref.model(**enc).logits[0, -1, :]
        cand_logits = cand(**enc).logits[0, -1, :]
        base_out = ref.model.generate(**enc, **gen_kw)
        cand_out = cand.generate(**enc, **gen_kw)
    base_gen = base_out[0, input_len:].tolist()
    cand_gen = cand_out[0, input_len:].tolist()

    return HFPairData(
        tok=tok,
        steered_gen_ids=cand_gen,
        steered_top5=torch.topk(cand_logits.float(), 5).indices.tolist(),
        base_gen_ids=base_gen,
        base_top5=torch.topk(base_logits.float(), 5).indices.tolist(),
        ref=ref, cand=cand, enc=enc,
    )


# --------------------------------------------------------------------------------------------- #
# level 2 — vLLM(baked) vs HF-baked, calibrated against the unsteered pair (GPU + server)
# --------------------------------------------------------------------------------------------- #

def _vllm_chat(client, served_model: str, max_new_tokens: int):
    resp = client.chat.completions.create(
        model=served_model,
        messages=MESSAGES,
        temperature=0,
        max_tokens=max_new_tokens,
        logprobs=True,
        top_logprobs=5,
    )
    choice = resp.choices[0]
    text = choice.message.content or ""
    top5_tokens: list[str] = []
    if choice.logprobs and choice.logprobs.content:
        top5_tokens = [t.token for t in choice.logprobs.content[0].top_logprobs]
    return text, top5_tokens


def _tok_str_to_id(tok, s: str) -> int | None:
    tid = tok.convert_tokens_to_ids(s)
    if tid is None or tid == tok.unk_token_id:
        ids = tok.encode(s, add_special_tokens=False)
        return ids[0] if ids else tid
    return tid


def _compare_pair(tok, hf_gen_ids: list[int], hf_top5_ids: list[int],
                   vllm_text: str, vllm_top5_tokens: list[str]):
    vllm_ids = tok.encode(vllm_text, add_special_tokens=False)
    first_match = bool(vllm_ids) and bool(hf_gen_ids) and vllm_ids[0] == hf_gen_ids[0]
    vllm_top5_ids = {_tok_str_to_id(tok, t) for t in vllm_top5_tokens}
    overlap = len(vllm_top5_ids & set(hf_top5_ids))
    common_prefix = 0
    for a, b in zip(vllm_ids, hf_gen_ids):
        if a != b:
            break
        common_prefix += 1
    return first_match, overlap, common_prefix, vllm_ids


@torch.no_grad()
def _teacher_forced_mismatches(model, enc: dict, gen_ids: list[int]):
    """Teacher-force vLLM's generated tokens through an HF model and, at every step where HF's
    greedy argmax picks a DIFFERENT token, record the top1-top2 logit gap. If the gap is tiny the
    disagreement is a rounding-level near-tie (vLLM's kernels resolve it the other way), not a
    modeling difference — this is the real level-2 signal; raw common-prefix length only measures
    where the FIRST near-tie happens to fall."""
    device = enc["input_ids"].device
    gen = torch.tensor([gen_ids], device=device)
    full = torch.cat([enc["input_ids"], gen], dim=1)
    logits = model(input_ids=full, attention_mask=torch.ones_like(full)).logits[0].float()
    start = enc["input_ids"].shape[1]
    gaps = []
    for i in range(len(gen_ids)):
        step = logits[start + i - 1]
        if step.argmax().item() != gen_ids[i]:
            top2 = torch.topk(step, 2).values
            gaps.append((top2[0] - top2[1]).item())
    return len(gaps), (max(gaps) if gaps else 0.0)


def run_level2(trait: str, coef: str, layer: str, variant_dir: str,
               base_url: str, served_model: str, base_base_url: str, base_served_model: str,
               device: str | None, max_new_tokens: int,
               hf_data: HFPairData | None = None) -> tuple[list[GateResult], list[tuple]]:
    import openai   # lazy: level 1 / preflight-only runs shouldn't require it

    gates: list[GateResult] = []
    rows: list[tuple] = []

    if hf_data is None:
        hf_data = compute_hf_pair_data(trait, coef, layer, variant_dir, device, max_new_tokens)
    tok = hf_data.tok

    client = openai.OpenAI(api_key="x", base_url=base_url)
    base_client = client if base_base_url == base_url else openai.OpenAI(api_key="x", base_url=base_base_url)

    calibrated = False
    cal_detail = ""
    try:
        ids = {m.id for m in base_client.models.list().data}
        calibrated = base_served_model in ids
        if not calibrated:
            cal_detail = f"{base_served_model!r} not found among models at {base_base_url} ({sorted(ids)})"
    except Exception as e:  # noqa: BLE001
        cal_detail = f"could not query {base_base_url}/models ({type(e).__name__}: {e})"

    if not calibrated:
        gates.append(GateResult("calibration pair available", False, warning=True,
                                 detail=(cal_detail or "unavailable") + " — falling back to fixed thresholds"))

    steered_text, steered_top5_tok = _vllm_chat(client, served_model, max_new_tokens)
    steered_first_match, steered_overlap, steered_prefix, steered_vllm_ids = _compare_pair(
        tok, hf_data.steered_gen_ids, hf_data.steered_top5, steered_text, steered_top5_tok)
    n_mm, worst_gap = _teacher_forced_mismatches(hf_data.cand, hf_data.enc, steered_vllm_ids)
    mm_frac = n_mm / max(1, len(steered_vllm_ids))
    rows.append(("steered: vLLM(baked) vs HF(baked)", steered_first_match, steered_overlap,
                 steered_prefix, f"{n_mm}/{len(steered_vllm_ids)} (worst gap {worst_gap:.3g})"))

    if calibrated:
        base_text, base_top5_tok = _vllm_chat(base_client, base_served_model, max_new_tokens)
        base_first_match, base_overlap, base_prefix, base_vllm_ids = _compare_pair(
            tok, hf_data.base_gen_ids, hf_data.base_top5, base_text, base_top5_tok)
        b_mm, b_gap = _teacher_forced_mismatches(hf_data.ref.model, hf_data.enc, base_vllm_ids)
        rows.append(("calibration: vLLM(base) vs HF(base)", base_first_match, base_overlap,
                     base_prefix, f"{b_mm}/{len(base_vllm_ids)} (worst gap {b_gap:.3g})"))

    gates.append(GateResult("first generated token identical (vLLM vs HF, steered)", steered_first_match,
                             detail=f"vllm_text[:40]={steered_text[:40]!r}"))
    gates.append(GateResult("top-5 first-token overlap >= 4/5 (steered)", steered_overlap >= 4,
                             detail=f"overlap={steered_overlap}/5"))
    gates.append(GateResult(
        "vLLM tokens consistent with HF-baked greedy up to near-ties (all gaps < 0.5, <= 10% of steps)",
        worst_gap < 0.5 and mm_frac <= 0.10,
        detail=(f"{n_mm}/{len(steered_vllm_ids)} teacher-forced steps disagree; worst top1-top2 "
                f"gap at a disagreement = {worst_gap:.4g}; raw common prefix = {steered_prefix} "
                f"tokens (informational)"),
    ))

    _free(hf_data.ref, hf_data.cand)
    return gates, rows


# --------------------------------------------------------------------------------------------- #
# reporting + CLI
# --------------------------------------------------------------------------------------------- #

def _print_gate_section(title: str, gates: list[GateResult]) -> bool:
    print(f"\n[{title}]")
    ok = True
    for g in gates:
        if g.passed:
            status = "PASS (warn)" if g.warning else "PASS"
        else:
            status = "FAIL"
            ok = False
        print(f"  [{status:11s}] {g.name}")
        for line in g.detail.splitlines():
            print(f"                 {line}")
    return ok


def _print_pair_table(rows: list[tuple]) -> None:
    if not rows:
        return
    print("\n[level 2 pair table]")
    print(f"  {'pair':45s} {'first-tok':10s} {'top5':6s} {'prefix':8s} {'forced-mismatch':s}")
    for name, first_match, overlap, prefix, forced in rows:
        print(f"  {name:45s} {str(first_match):10s} {overlap}/5    {str(prefix):8s} {forced}")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Verify a baked (down_proj-bias) persona-vector checkpoint against the "
                    "reference activation-steering hook.",
    )
    ap.add_argument("--trait", required=True, help="persona trait, e.g. goodness")
    ap.add_argument("--coef", required=True, help="steering coefficient, verbatim CLI string (e.g. 2 or 2.0)")
    ap.add_argument("--layer", required=True, help="hidden_states index the vector was measured at (e.g. 16)")
    ap.add_argument("--variant-dir", default=None,
                     help="baked checkpoint dir (default: /workspace/pvec_baked/<trait>_c<coef>_l<layer>)")
    ap.add_argument("--levels", default="1", choices=["0", "1", "2", "12"],
                     help="which gates to run: '0' (preflight only, CPU), '1' (HF vs HF, GPU, "
                          "default), '2' (vLLM vs HF, needs a running server), or '12' for both "
                          "in one process (preflight always runs)")
    ap.add_argument("--base-url", default="http://localhost:8000/v1", help="vLLM server for the baked model")
    ap.add_argument("--served-model", default=None,
                     help="model name the baked checkpoint is served under (default: pvec:<trait>:<coef>:<layer>)")
    ap.add_argument("--base-base-url", default=None,
                     help="vLLM server for the unsteered base model, for calibration (default: --base-url)")
    ap.add_argument("--base-served-model", default="base",
                     help="model name the base (unsteered) model is served under, for calibration")
    ap.add_argument("--max-new-tokens", type=int, default=128)
    ap.add_argument("--device", default=None, help="cuda | cpu | mps (default: auto-detect)")
    args = ap.parse_args()

    variant_dir = args.variant_dir or default_variant_dir(args.trait, args.coef, args.layer)
    served_model = args.served_model or default_served_model(args.trait, args.coef, args.layer)
    base_base_url = args.base_base_url or args.base_url

    print(f"trait={args.trait} coef={args.coef} layer={args.layer}")
    print(f"variant_dir={variant_dir}")
    print(f"levels={args.levels}")

    sections: list[tuple[str, list[GateResult]]] = []
    rows: list[tuple] = []

    try:
        gates = run_preflight(args.trait, args.coef, args.layer, variant_dir)
    except Exception as e:  # noqa: BLE001
        gates = [GateResult("preflight", False, detail=f"{type(e).__name__}: {e}")]
    sections.append(("preflight (tensor-only, CPU)", gates))

    if "1" in args.levels:
        try:
            gates = run_level1(args.trait, args.coef, args.layer, variant_dir,
                               args.device, args.max_new_tokens)
        except Exception as e:  # noqa: BLE001
            gates = [GateResult("level 1", False, detail=f"{type(e).__name__}: {e}")]
        sections.append(("level 1: HF-baked vs HF-hook (GPU, no server)", gates))

    if "2" in args.levels:
        try:
            gates, rows = run_level2(
                args.trait, args.coef, args.layer, variant_dir,
                args.base_url, served_model, base_base_url, args.base_served_model,
                args.device, args.max_new_tokens,
            )
        except Exception as e:  # noqa: BLE001
            gates = [GateResult("level 2", False, detail=f"{type(e).__name__}: {e}")]
        sections.append(("level 2: vLLM(baked) vs HF-baked, calibrated (GPU + server)", gates))

    print("\n" + "=" * 88)
    print("VERIFY-BAKE SUMMARY")
    print("=" * 88)
    overall = True
    for title, gates in sections:
        overall = _print_gate_section(title, gates) and overall
    _print_pair_table(rows)
    print("\n" + "=" * 88)
    print(f"OVERALL: {'PASS' if overall else 'FAIL'}")
    print("=" * 88)

    sys.exit(0 if overall else 1)


if __name__ == "__main__":
    main()
