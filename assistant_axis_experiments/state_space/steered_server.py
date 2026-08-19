"""OpenAI-compatible server that generates with a persona-role direction added at every token.

Two modes, both built from the paper's released per-role mean-activation vectors
(lu-christina/assistant-axis-vectors, 275 roles x 3 models: demon, angel, void, vampire, ...):

  ORTHOGONAL (default) — the causal test of the 1-D account: steer a persona direction v_z that
  is orthogonal to the Assistant Axis, so a_t is (to first order) untouched, and see whether the
  ai2ai conversation's DESTINATION basin changes. If it does at matched a_t trajectories, the axis
  alone cannot be the state variable that picks the basin.

  RAW (--raw) — steer along the role's full persona-space offset, axis component INCLUDED: "run
  the self-conversation as the demon persona". This is plain persona-vector steering; the axis
  coordinate moves too (by the role's own axis share), so it is NOT a test of the 1-D account —
  it asks where a role-pushed self-conversation goes, and whether it still finds the same basin.

The steering vector at each layer L:

    v      = role[L] - mean_role[L]          (persona-space offset of --role; mean_role is
                                              default - axis, no extra downloads)
    v      = role[L] - role2[L]              with --minus-role: a pairwise role contrast
                                              (e.g. --role demon --minus-role assistant)
    v_perp = v - (v·a_hat) a_hat             axis component removed (cos(v_perp, axis) = 0)
    steer  = coef * ||axis[L]|| * unit(v_perp)          [orthogonal]
    steer  = coef * ||axis[L]|| * unit(v)               [--raw]

i.e. --coef is in units of the axis norm at that layer: coef 1.0 displaces activations by as
much as the full default->mean-role gap (sideways in orthogonal mode). The startup log prints
||v||/||axis|| per layer — the role's NATURAL offset in the same units — so a raw coef equal to
that ratio reproduces the role's own displacement from the mean role. Calibrate with a pilot
(start ~0.5-2). Optionally --with-capping ALSO applies the paper's released activation capping,
bounding a_t from above (commutes exactly with orthogonal steering; with --raw it clips the
axis share the role push adds). Serving/batching is capped_server's engine behind the same
/v1/chat/completions.

    python -m assistant_axis_experiments.state_space.steered_server \
        --model-key qwen-3-32b --role poet --coef 1.0 --port 8000
    python -m assistant_axis_experiments.state_space.steered_server \
        --model-key qwen-3-32b --role demon --coef 1.0 --raw --port 8000

    # CPU smoke (tiny model, random synthetic axis/role):
    python -m assistant_axis_experiments.state_space.steered_server --model-key qwen-3-32b \
        --hf-model-override Qwen/Qwen3-0.6B --synthetic --role poet --coef 1.0 --port 8000
"""

from __future__ import annotations

import argparse

import torch
import torch.nn.functional as F

from .. import capped_server
from ..axes import AXIS_DATASET, AXIS_MODELS, load_axis_for, target_layer_for
from ..capped_server import Engine, Handler
from ..project_transcripts import _load_probing_model
from ..vendor.assistant_axis import ActivationSteering, get_config, load_axis, load_capping_config
from ..vendor.assistant_axis.steering import build_capping_steerer


def load_role_vector(model_key: str, role: str) -> torch.Tensor:
    from huggingface_hub import hf_hub_download

    path = hf_hub_download(AXIS_DATASET, f"{model_key}/role_vectors/{role}.pt",
                           repo_type="dataset")
    return load_axis(path).float()


def orthogonal_steering_vectors(
    model_key: str, role: str, minus_role: str | None, coef: float, layers: list[int],
    raw: bool = False,
) -> tuple[list[torch.Tensor], list[float]]:
    """Per-layer unit steering directions and coefficients (coef * ||axis[L]||).

    Direction is unit(v_perp) (axis component removed) by default, or unit(v) with ``raw``
    (the role's full offset from the contrast, axis component kept).
    """
    axis, _ = load_axis_for(model_key)
    role_vec = load_role_vector(model_key, role)
    if minus_role:
        base_vec = load_role_vector(model_key, minus_role)
    else:
        from huggingface_hub import hf_hub_download
        default = load_axis(hf_hub_download(AXIS_DATASET, f"{model_key}/default_vector.pt",
                                            repo_type="dataset")).float()
        base_vec = default - axis                        # mean of fully-role-playing vectors

    vectors, coefs = [], []
    for L in layers:
        a_hat = F.normalize(axis[L], dim=0)
        v = role_vec[L] - base_vec[L]
        axis_share = float(v @ a_hat)                    # signed axis component of the offset
        v_perp = v - axis_share * a_hat
        cos_axis = float((F.normalize(v_perp, dim=0) @ a_hat))
        assert abs(cos_axis) < 1e-4, f"orthogonalization failed at L{L} (cos {cos_axis})"
        direction = v if raw else v_perp
        vectors.append(F.normalize(direction, dim=0))
        coefs.append(coef * float(axis[L].norm()))
        print(f"  L{L}: |axis|={axis[L].norm():.1f}  |v|={v.norm():.1f} "
              f"(= {v.norm() / axis[L].norm():.2f} axis-norms; natural raw coef)  "
              f"axis share of v={axis_share / v.norm():+.2f}"
              f"{' (kept: RAW)' if raw else ' (removed)'}  "
              f"applied |steer|={coefs[-1]:.1f}")
    return vectors, coefs


def main() -> None:
    ap = argparse.ArgumentParser(description="Axis-orthogonal persona steering server.")
    ap.add_argument("--model-key", required=True, choices=sorted(AXIS_MODELS))
    ap.add_argument("--role", required=True, help="role vector to steer toward (e.g. poet)")
    ap.add_argument("--minus-role", default=None,
                    help="contrast role (default: the mean fully-role-playing vector)")
    ap.add_argument("--coef", type=float, required=True,
                    help="strength in units of ||axis|| at each layer (pilot ~0.5-2)")
    ap.add_argument("--layers", type=int, nargs="+", default=None,
                    help="layers to steer at (default: the paper's target layer)")
    ap.add_argument("--raw", action="store_true",
                    help="steer along the role's FULL offset (axis component kept) instead "
                         "of the axis-orthogonal part")
    ap.add_argument("--with-capping", action="store_true",
                    help="ALSO apply the released activation capping (qwen/llama only)")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--max-batch", type=int, default=None)
    ap.add_argument("--hf-model-override", default=None)
    ap.add_argument("--synthetic", action="store_true",
                    help="random axis/role at layer 1 (CPU smoke only, no downloads)")
    ap.add_argument("--device", default=None)
    args = ap.parse_args()

    hf_model = args.hf_model_override or AXIS_MODELS[args.model_key]
    chat_kwargs = {"enable_thinking": False} if "qwen" in hf_model.lower() else {}
    max_batch = args.max_batch or (2 if "70b" in args.model_key else 4)

    print(f"loading {hf_model} ...")
    pm = _load_probing_model(hf_model, args.device)
    if pm.tokenizer.pad_token is None:
        pm.tokenizer.pad_token = pm.tokenizer.eos_token

    if args.synthetic:
        g = torch.Generator().manual_seed(0)
        axis = torch.randn(pm.hidden_size, generator=g)
        v = torch.randn(pm.hidden_size, generator=g)
        a_hat = F.normalize(axis, dim=0)
        direction = v if args.raw else v - (v @ a_hat) * a_hat
        vectors, coefs, layers = [F.normalize(direction, dim=0)], [args.coef * float(axis.norm())], [1]
        print(f"SYNTHETIC axis/role (plumbing smoke only; {'raw' if args.raw else 'orthogonal'})")
    else:
        layers = args.layers or [target_layer_for(args.model_key)]
        print(f"building {'v_raw' if args.raw else 'v_perp'}({args.role}"
              + (f" - {args.minus_role}" if args.minus_role else " - mean_role")
              + f") at layers {layers}, coef {args.coef}:")
        vectors, coefs = orthogonal_steering_vectors(
            args.model_key, args.role, args.minus_role, args.coef, layers, raw=args.raw)

    steerer = ActivationSteering(
        pm.model, vectors, coefficients=coefs, layer_indices=layers,
        intervention_type="addition", positions="all",
    )
    steerer.__enter__()   # hooks stay registered for the server's lifetime

    if args.with_capping:
        from huggingface_hub import hf_hub_download
        cfg = get_config(hf_model)
        if "capping_config" not in cfg:
            raise SystemExit(f"no released capping config for {args.model_key}")
        path = hf_hub_download(AXIS_DATASET, cfg["capping_config"], repo_type="dataset")
        capper = build_capping_steerer(pm.model, load_capping_config(path),
                                       cfg["capping_experiment"])
        capper.__enter__()
        print(f"capping ALSO active: {cfg['capping_experiment']}")

    capped_server.ENGINE = Engine(pm, chat_kwargs, max_batch)
    capped_server.MODEL_ID = hf_model
    from http.server import ThreadingHTTPServer
    print(f"serving STEERED {hf_model} on :{args.port} "
          f"(role={args.role}, coef={args.coef}, mode={'raw' if args.raw else 'orthogonal'}, "
          f"layers={layers}, max_batch={max_batch})")
    ThreadingHTTPServer(("0.0.0.0", args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
