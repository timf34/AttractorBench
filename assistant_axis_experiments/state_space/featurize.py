"""Laptop stage: turn activations x persona basis -> per-turn (a_t, z_t) state features.

For every ``analysis/*__turn_acts.npz`` (written by dump_activations on the pod) and every
layer present in both the dump and the persona basis, computes per assistant turn:

  a       axis-units projection onto the Assistant Axis (1 = default anchor, 0 = mean-role
          anchor) — identical math to the drift experiment, recomputed here from the vector;
  z       coordinates in the axis-ORTHOGONALIZED persona PCs (top --k-feat, default 16):
          center on the mean role vector, project out the axis direction, dot with the z-PCs;
  z_norm  norm of the FULL orthogonal component (not just the stored PCs) — "how far from the
          axis line", regardless of direction;
  act_norm  raw activation norm (a sanity/scale covariate).

Output (committable, ~1.5MB/condition): ``analysis/<base>__state_features.json`` mirroring the
axis-projections layout: runs -> views -> turns + per-layer feature arrays.

    python -m assistant_axis_experiments.state_space.featurize \
        --results-dir results/axis_qwen_3_32b_nosys_ai2ai --model-key qwen-3-32b
"""

from __future__ import annotations

import argparse
import glob
import json
import os

import numpy as np

from ..axes import AXIS_MODELS
from .persona_space import BASES_DIR

K_FEAT = 16


def load_basis(model_key: str) -> dict:
    path = os.path.join(BASES_DIR, f"{model_key}.npz")
    if not os.path.exists(path):
        raise SystemExit(f"{path} missing — run persona_space.py --model-key {model_key} first")
    return dict(np.load(path, allow_pickle=False))


def featurize_layer(acts: np.ndarray, basis: dict, layer: int, k_feat: int) -> dict:
    """acts (n_rows, hidden) fp32 -> {"a": (n,), "z": (n, k), "z_norm": (n,), "act_norm": (n,)}."""
    a_hat = basis[f"L{layer}__axis_unit"]
    mu = basis[f"L{layer}__mean_role"]
    zpc = basis[f"L{layer}__zpc"][:k_feat]
    ad = float(basis[f"L{layer}__anchor_default"])
    ar = float(basis[f"L{layer}__anchor_role_mean"])

    raw = acts @ a_hat
    a_units = (raw - ar) / (ad - ar)
    centered = acts - mu
    perp = centered - np.outer(centered @ a_hat, a_hat)
    return {
        "a": a_units,
        "z": perp @ zpc.T,
        "z_norm": np.linalg.norm(perp, axis=1),
        "act_norm": np.linalg.norm(acts, axis=1),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Per-turn (a_t, z_t) state features from dumped activations.")
    ap.add_argument("--results-dir", nargs="+", required=True)
    ap.add_argument("--model-key", required=True, choices=sorted(AXIS_MODELS))
    ap.add_argument("--k-feat", type=int, default=K_FEAT)
    ap.add_argument("--basis-override", default=None,
                    help="path to a basis npz (CPU smoke with a synthetic basis)")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    basis = (dict(np.load(args.basis_override)) if args.basis_override
             else load_basis(args.model_key))
    basis_layers = set(int(l) for l in basis["layers"])

    for results_dir in args.results_dir:
        for npz_path in sorted(glob.glob(os.path.join(results_dir, "analysis", "*__turn_acts.npz"))):
            out_path = npz_path.replace("__turn_acts.npz", "__state_features.json")
            if os.path.exists(out_path) and not args.force:
                print(f"skip (exists): {out_path}")
                continue
            d = np.load(npz_path)
            layers = [int(l) for l in d["layers"] if int(l) in basis_layers]
            if not layers:
                print(f"!! no overlap between dump layers {d['layers'].tolist()} and basis "
                      f"layers {sorted(basis_layers)} — skipping {npz_path}")
                continue
            acts = d["acts"].astype(np.float32)          # (n_rows, n_dump_layers, hidden)
            dump_layer_pos = {int(l): i for i, l in enumerate(d["layers"])}
            per_layer = {L: featurize_layer(acts[:, dump_layer_pos[L], :], basis, L, args.k_feat)
                         for L in layers}

            run_index, turn, view = d["run_index"], d["turn"], d["view"]
            runs_out: dict[int, dict] = {}
            for row in np.argsort(run_index, kind="stable"):
                ri, v = int(run_index[row]), str(view[row])
                entry = runs_out.setdefault(ri, {"run_index": ri, "views": {}})
                vd = entry["views"].setdefault(v, {"turns": [], "layers": {
                    str(L): {"a": [], "z": [], "z_norm": [], "act_norm": []} for L in layers}})
                vd["turns"].append(int(turn[row]))
                for L in layers:
                    f = per_layer[L]
                    ld = vd["layers"][str(L)]
                    ld["a"].append(round(float(f["a"][row]), 4))
                    ld["z"].append([round(float(x), 3) for x in f["z"][row]])
                    ld["z_norm"].append(round(float(f["z_norm"][row]), 2))
                    ld["act_norm"].append(round(float(f["act_norm"][row]), 2))

            # per-view turn order: rows were appended in dump order (turn-ascending per view),
            # but sort defensively so downstream can rely on it.
            for entry in runs_out.values():
                for vd in entry["views"].values():
                    order = np.argsort(vd["turns"], kind="stable")
                    vd["turns"] = [vd["turns"][i] for i in order]
                    for L in layers:
                        ld = vd["layers"][str(L)]
                        for key in ("a", "z", "z_norm", "act_norm"):
                            ld[key] = [ld[key][i] for i in order]

            out = {
                "model_key": str(d["model_key"]),
                "hf_model": str(d["hf_model"]),
                "source_file": str(d["source_file"]),
                "temperature": float(d["temperature"]),
                "layers": layers,
                "k_feat": args.k_feat,
                "runs": [runs_out[ri] for ri in sorted(runs_out)],
            }
            with open(out_path, "w") as f:
                json.dump(out, f)
            print(f"wrote {out_path} ({os.path.getsize(out_path)/1e6:.1f} MB)")


if __name__ == "__main__":
    main()
