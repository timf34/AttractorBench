"""GPU stage: replay ai2ai transcripts through the HF model and project per-turn activations
onto the Assistant Axis.

For every condition file ``results/<cond>/two_instance__*.json``, every run, and BOTH instance
views (each instance sees itself as ``assistant`` and the peer as ``user``), this:

1. rebuilds the view exactly as the harness fed it forward (``views.build_view``; Gemma-2 gets
   the system fold, Qwen3 gets ``enable_thinking=False`` — both matching generation time);
2. runs ONE forward pass over the full view (vendored ``ActivationExtractor.full_conversation``)
   and mean-pools post-MLP residual activations over each assistant turn's tokens (vendored
   ``ConversationEncoder.build_turn_spans`` — the paper's response-token readout);
3. projects each turn's mean activation onto the per-layer-normalized axis at EVERY layer.

Output (scalars only, safe to commit): ``results/<cond>/analysis/<file>__axis_projections.json``.

    python -m assistant_axis_drift.project_transcripts \
        --results-dir results/axis_qwen_3_32b_nosys_ai2ai --model-key qwen-3-32b

CPU smoke (laptop, no axis download, tiny model with the same template family as Qwen3-32B):

    python -m assistant_axis_drift.project_transcripts --results-dir <fixture-dir> \
        --model-key qwen-3-32b --hf-model-override Qwen/Qwen3-0.6B --synthetic-axis

RAM note: the all-layer activation capture holds (n_layers, n_tokens, hidden) bf16 on CPU per
view — up to ~10GB (Qwen3-32B) / ~21GB (Llama-70B) transiently for a full 16k-token view. Fine
on a pod; don't run the big models on a laptop.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re

import torch

from .axes import AXIS_MODELS, load_axis_for, normalized_axis, target_layer_for
from .vendor.assistant_axis.internals import ActivationExtractor, ConversationEncoder, ProbingModel
from .views import build_view, fold_system_into_user


def _load_probing_model(hf_model: str, device: str | None) -> ProbingModel:
    """Version-proof model/tokenizer load, wrapped in the vendored ProbingModel.

    Two transformers-version hazards the vendored constructor doesn't handle (we keep vendored
    files verbatim, so the compat shims live HERE):
    - the bf16 kwarg was ``torch_dtype`` before 4.56 and ``dtype`` after; the wrong one is
      SILENTLY ignored and the model loads fp32 (2x memory — fatal for the 70B);
    - transformers >= 5 returns a dict from ``apply_chat_template(tokenize=True)`` where the
      vendored span code expects the bare id list — pin ``return_dict=False`` on tokenize calls.
    """
    import transformers
    from packaging.version import Version
    from transformers import AutoModelForCausalLM, AutoTokenizer

    v = Version(transformers.__version__)
    dtype_kw = {"dtype": torch.bfloat16} if v >= Version("4.56") else {"torch_dtype": torch.bfloat16}
    model = AutoModelForCausalLM.from_pretrained(
        hf_model, device_map=device or "auto", **dtype_kw
    )
    model.eval()
    assert next(model.parameters()).dtype == torch.bfloat16, "model did not load in bf16"

    tokenizer = AutoTokenizer.from_pretrained(hf_model)
    orig_apply = tokenizer.apply_chat_template

    def apply_chat_template(*a, **k):
        if k.get("tokenize"):
            k.setdefault("return_dict", False)
        return orig_apply(*a, **k)

    tokenizer.apply_chat_template = apply_chat_template
    return ProbingModel.from_existing(model, tokenizer, model_name=hf_model)


def condition_files(results_dir: str) -> list[str]:
    files = sorted(glob.glob(os.path.join(results_dir, "two_instance__*.json")))
    if not files:
        raise SystemExit(f"no two_instance__*.json condition files in {results_dir}")
    return files


def _temperature_of(data: dict, path: str) -> float:
    if "temperature" in data:
        return float(data["temperature"])
    m = re.search(r"temp([\d.]+)\.json$", os.path.basename(path))
    return float(m.group(1)) if m else float("nan")


def project_view(
    extractor: ActivationExtractor,
    encoder: ConversationEncoder,
    messages: list[dict],
    own_turn_numbers: list[int],
    axis_n: torch.Tensor,
    chat_kwargs: dict,
) -> dict | None:
    """Per-turn projections for one view. Returns {"turns": [...], "proj_by_layer": {L: [...]}}
    or None if the serialization can't be aligned (warned, view skipped)."""
    full_ids, spans = encoder.build_turn_spans(messages, **chat_kwargs)
    acts = extractor.full_conversation(messages, layer=None, chat_format=True, **chat_kwargs)
    # full_conversation tokenizes the template STRING; build_turn_spans tokenizes directly.
    # Their pairing is the vendored canonical path (SpanMapper.mean_all_turn_activations), but
    # assert alignment anyway — a mismatch would silently shift every span.
    if acts.shape[1] != len(full_ids):
        print(f"    !! token-length mismatch (acts {acts.shape[1]} vs ids {len(full_ids)}) — skipping view")
        return None

    assistant_spans = [s for s in spans if s["role"] == "assistant"]
    if len(assistant_spans) != len(own_turn_numbers):
        print(
            f"    !! {len(assistant_spans)} assistant spans vs {len(own_turn_numbers)} own turns "
            f"— keeping the aligned prefix"
        )
    n_layers = acts.shape[0]
    turns: list[int] = []
    proj_by_layer: dict[int, list[float]] = {layer: [] for layer in range(n_layers)}
    for turn_no, span in zip(own_turn_numbers, assistant_spans):
        seg = acts[:, span["start"]:span["end"], :]
        if seg.shape[1] == 0:
            continue
        mean_act = seg.float().mean(dim=1)              # (n_layers, hidden)
        projs = (mean_act * axis_n).sum(dim=1)          # (n_layers,)
        turns.append(turn_no)
        for layer in range(n_layers):
            proj_by_layer[layer].append(round(float(projs[layer]), 4))
    return {"turns": turns, "proj_by_layer": proj_by_layer}


def main() -> None:
    ap = argparse.ArgumentParser(description="Project ai2ai transcripts onto the Assistant Axis.")
    ap.add_argument("--results-dir", nargs="+", required=True, help="results/<cond> dir(s)")
    ap.add_argument("--model-key", required=True, choices=sorted(AXIS_MODELS))
    ap.add_argument("--hf-model-override", default=None,
                    help="load THIS HF model instead (CPU smoke with a tiny same-family model)")
    ap.add_argument("--synthetic-axis", action="store_true",
                    help="random axis matching the loaded model's shape (smoke only, no download)")
    ap.add_argument("--device", default=None, help="ProbingModel device (default: auto)")
    ap.add_argument("--force", action="store_true", help="recompute even if the output exists")
    args = ap.parse_args()

    hf_model = args.hf_model_override or AXIS_MODELS[args.model_key]
    is_gemma = "gemma" in hf_model.lower()
    chat_kwargs = {"enable_thinking": False} if "qwen" in hf_model.lower() else {}

    print(f"loading {hf_model} ...")
    pm = _load_probing_model(hf_model, args.device)
    encoder = ConversationEncoder(pm.tokenizer, model_name=hf_model)
    extractor = ActivationExtractor(pm, encoder)
    n_layers = len(pm.get_layers())

    if args.synthetic_axis:
        g = torch.Generator().manual_seed(0)
        axis = torch.randn(n_layers, pm.hidden_size, generator=g)
        anchors: dict = {"default": {}, "role_mean": {}}
        target_layer = n_layers // 2
    else:
        axis, anchors = load_axis_for(args.model_key)
        target_layer = target_layer_for(args.model_key)
        if axis.shape[0] != n_layers:
            # Their axis files index decoder blocks 0..n-1; anything else means a model mismatch.
            raise SystemExit(f"axis has {axis.shape[0]} layers but model has {n_layers}")
    axis_n = normalized_axis(axis)

    for results_dir in args.results_dir:
        for path in condition_files(results_dir):
            out_dir = os.path.join(results_dir, "analysis")
            base = os.path.splitext(os.path.basename(path))[0]
            out_path = os.path.join(out_dir, f"{base}__axis_projections.json")
            if os.path.exists(out_path) and not args.force:
                print(f"skip (exists): {out_path}")
                continue

            with open(path) as f:
                data = json.load(f)
            system_prompt = data.get("system_prompt", "")
            temperature = _temperature_of(data, path)
            print(f"{os.path.basename(path)}: {len(data['runs'])} runs (temp {temperature})")

            out_runs = []
            for run in data["runs"]:
                entry = {"run_index": run["run_index"], "temperature": temperature, "views": {}}
                for view in ("A", "B"):
                    messages = build_view(run, system_prompt, run["seed_prompt"], view)
                    if is_gemma:
                        messages = fold_system_into_user(messages)
                    own_turns = [t["turn"] for t in run["turns"] if t["speaker"] == view]
                    if not own_turns:
                        continue
                    with torch.inference_mode():
                        res = project_view(extractor, encoder, messages, own_turns, axis_n, chat_kwargs)
                    if res is not None:
                        # keep the full per-layer table but surface the headline series too
                        res["proj_target"] = res["proj_by_layer"][target_layer]
                        entry["views"][view] = res
                out_runs.append(entry)
                print(f"  run {run['run_index']}: views {sorted(entry['views'])}")

            os.makedirs(out_dir, exist_ok=True)
            with open(out_path, "w") as f:
                json.dump(
                    {
                        "model_key": args.model_key,
                        "hf_model": hf_model,
                        "synthetic_axis": bool(args.synthetic_axis),
                        "target_layer": target_layer,
                        "n_layers": n_layers,
                        "anchors": anchors,
                        "system_prompt": system_prompt,
                        "temperature": temperature,
                        "source_file": os.path.basename(path),
                        "runs": out_runs,
                    },
                    f,
                )
            print(f"  wrote {out_path}")


if __name__ == "__main__":
    main()
