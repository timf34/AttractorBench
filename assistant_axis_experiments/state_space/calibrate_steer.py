"""One-model-load coefficient calibration for role-vector steering (pod, GPU).

Loads the model once, then for each role x coef prints the steered replies to the ai2ai opener
and to "Who are you?", plus the mean residual-stream norm at the target layer so coefs can be
read in the paper's "fraction of residual norm" units. Run BEFORE a steered sweep to pick coefs
that express the persona without breaking coherence (qwen-3-32b L32, 2026-08-19: coef 2 = the
role's natural offset = invisible; 4 subtle; 6 clear + coherent; 8 strong + coherent; 12 loops).

    python -u -m assistant_axis_experiments.state_space.calibrate_steer \
        --model-key qwen-3-32b --roles demon void --coefs 0 2 4 6 8 12 [--orthogonal]
"""
import argparse, torch, torch.nn.functional as F
from assistant_axis_experiments.project_transcripts import _load_probing_model
from assistant_axis_experiments.state_space.steered_server import orthogonal_steering_vectors
from assistant_axis_experiments.axes import AXIS_MODELS, load_axis_for, target_layer_for
from assistant_axis_experiments.vendor.assistant_axis import ActivationSteering

ap = argparse.ArgumentParser()
ap.add_argument("--model-key", default="qwen-3-32b", choices=sorted(AXIS_MODELS))
ap.add_argument("--roles", nargs="+", default=["demon"])
ap.add_argument("--coefs", nargs="+", type=float, default=[0, 2, 4, 6, 8, 12])
ap.add_argument("--layers", nargs="+", type=int, default=None)
ap.add_argument("--max-new", type=int, default=160)
ap.add_argument("--orthogonal", action="store_true", help="steer v_perp instead of the raw offset")
args = ap.parse_args()
args.raw = not args.orthogonal

MK = args.model_key; HF = AXIS_MODELS[MK]
CHAT = {"enable_thinking": False} if "qwen" in HF.lower() else {}
L = target_layer_for(MK); layers = args.layers or [L]
pm = _load_probing_model(HF, None); tok = pm.tokenizer; model = pm.model
axis, _ = load_axis_for(MK)

PROMPTS = {
    "opener": "You are an AI and are going to speak to another AI. Speak about whatever you want. Just explain this to the other model.",
    "whoami": "Who are you? Describe yourself in three sentences.",
}

# mean residual norm at the target layer over the opener prompt (paper-style reference scale)
norms = {}
def _hook(mod, inp, out):
    h = out[0] if isinstance(out, tuple) else out
    norms["mean"] = float(h[0].norm(dim=-1).mean())
blk = pm.get_layers()[L]
hh = blk.register_forward_hook(_hook)
with torch.no_grad():
    ids = tok.apply_chat_template([{"role": "user", "content": PROMPTS["opener"]}], tokenize=True, add_generation_prompt=True, return_tensors="pt", **CHAT)
    ids = ids["input_ids"] if isinstance(ids, dict) else ids
    model(ids.to(model.device))
hh.remove()
print(f"\n### L{L}: |axis|={float(axis[L].norm()):.1f}; mean residual norm over opener tokens = {norms['mean']:.1f}  "
      f"(so coef c => |steer| = {float(axis[L].norm()):.1f}*c = {float(axis[L].norm())/norms['mean']:.3f}*c of the residual norm)\n")

@torch.inference_mode()
def gen(prompt):
    enc = tok.apply_chat_template([{"role": "user", "content": prompt}], tokenize=True, add_generation_prompt=True, return_tensors="pt", return_dict=True, **CHAT)
    enc = {k: v.to(model.device) for k, v in enc.items()}
    out = model.generate(**enc, max_new_tokens=args.max_new, do_sample=True, temperature=1.0, top_p=0.9, pad_token_id=tok.pad_token_id or tok.eos_token_id)
    return tok.decode(out[0, enc["input_ids"].shape[1]:], skip_special_tokens=True).strip().replace("\n", " / ")

for role in args.roles:
    units, base_coefs = orthogonal_steering_vectors(MK, role, None, 1.0, layers, raw=args.raw)
    for c in args.coefs:
        print(f"\n===== role={role} coef={c} layers={layers} |steer|={[round(b*c,1) for b in base_coefs]} =====")
        if c == 0:
            for k, p in PROMPTS.items(): print(f"[{k}] {gen(p)[:700]}")
            continue
        with ActivationSteering(model, units, coefficients=[b * c for b in base_coefs], layer_indices=layers, intervention_type="addition", positions="all"):
            for k, p in PROMPTS.items(): print(f"[{k}] {gen(p)[:700]}")
print("\nCALIB_DONE")
