"""Is the Assistant Axis a single SAE feature, or smeared across many? (laptop, CPU)

The a_t/z_t work shows the persona state is multi-dimensional in PCA terms. This stage asks
the same question against a very different, independently-learned basis: the feature
dictionaries of public sparse autoencoders trained on the residual stream at the layer where
we read the axis. If the Assistant Axis (Lu et al.) were "one thing" the model represents
explicitly, some SAE feature should point (nearly) along it — max |cos| with the dictionary
would be high and one feature would reconstruct most of it. If instead the axis is a
composite contrast direction, max |cos| stays near the random-direction baseline and a sparse
reconstruction needs many features.

Per (model, SAE) we test six unit directions:
  assistant_axis   the released axis at the SAE's layer,
  persona_PC1      first PC of the 275 role vectors (centered on the mean role),
  zPC1             first PC after projecting out the axis direction (axis-orthogonal),
  role: angel / poet / engineer   individual role vector minus the mean role,
plus a NULL of 200 random unit vectors (seed 0) whose max-|cos| distribution calibrates "low".

Metrics per direction:
  - max |cos| against the L2-normalized decoder rows + top-10 (feature, cos) pairs;
  - greedy orthogonal matching pursuit (argmax |residual @ feature|, re-fit least squares on
    the selected set, iterate) up to k=64: fraction of squared norm explained at
    k = 1, 2, 4, 8, 16, 32, 64 and the smallest k reaching 90%.

SAEs (weights fetched from the HF hub, formats documented in load_decoder):
  qwen-3-32b   adamkarvonen/qwen3-32b-saes, batch-top-k @ resid_post layer 32 (k=80),
               trainer_2 (65536 feats) and trainer_0 (16384 feats), activation_dim 5120;
  llama-3.3-70b  Goodfire/Llama-3.3-70B-Instruct-SAE-l50, residual stream layer 50,
               d_model 8192 (d_sae read off the checkpoint — its config.yaml is a wandb stub).

NOTE the llama SAE layer (50) is not one of the committed persona-basis layers (20/40/60/64),
so PC1/zPC1 are recomputed at L50 from the cached role vectors; qwen reuses bases/qwen-3-32b.npz.

Outputs:
  state_space/reports/sae_axis__<model_key>.md   tables + null baseline + interpretation

    python -m assistant_axis_experiments.state_space.sae_axis --model-key qwen-3-32b
    python -m assistant_axis_experiments.state_space.sae_axis --model-key all
"""

from __future__ import annotations

import argparse
import os

import numpy as np
import torch
from huggingface_hub import hf_hub_download

from ..axes import load_axis_for
from .persona_space import BASES_DIR, REPORTS_DIR, load_role_vectors, pca

TEST_ROLES = ["angel", "poet", "engineer"]
K_MAX = 64                      # OMP budget
K_REPORT = [1, 2, 4, 8, 16, 32, 64]
R2_TARGET = 0.90
N_NULL = 200                    # random directions for the max-|cos| baseline
N_NULL_OMP = 20                 # subset of nulls that also get the (slow) OMP baseline
TOP_N = 10

# Only models with a public residual-stream SAE at (or near) the axis readout depth.
SAES: dict[str, dict] = {
    "qwen-3-32b": {
        "layer": 32,
        "saes": [
            {
                "name": "batch-top-k 65536 (trainer_2)",
                "repo": "adamkarvonen/qwen3-32b-saes",
                "file": "saes_Qwen_Qwen3-32B_batch_top_k/resid_post_layer_32/trainer_2/ae.pt",
            },
            {
                "name": "batch-top-k 16384 (trainer_0)",
                "repo": "adamkarvonen/qwen3-32b-saes",
                "file": "saes_Qwen_Qwen3-32B_batch_top_k/resid_post_layer_32/trainer_0/ae.pt",
            },
        ],
    },
    "llama-3.3-70b": {
        "layer": 50,
        "saes": [
            {
                "name": "Goodfire resid L50",
                "repo": "Goodfire/Llama-3.3-70B-Instruct-SAE-l50",
                "file": "Llama-3.3-70B-Instruct-SAE-l50.pt",
            },
        ],
    },
}


def load_decoder(repo: str, filename: str, hidden: int) -> tuple[np.ndarray, str]:
    """(features (dict_size, hidden) fp32 rows = feature directions, orientation note).

    Both checkpoints here are flat torch state dicts storing the decoder nn.Linear-style,
    i.e. weight shape (out_features, in_features) = (hidden, dict_size), features as COLUMNS:
      - adamkarvonen (dictionary_learning batch-top-k): ``decoder.weight`` (5120, 65536);
      - Goodfire: ``decoder_linear.weight`` (8192, 65536).
    We introspect rather than hardcode: pick the 2-D tensor with 'decoder'/'w_dec' in its key
    that matches ``hidden`` on exactly one dim, and orient it so rows are features.
    """
    path = hf_hub_download(repo, filename)
    try:
        sd = torch.load(path, map_location="cpu", weights_only=True)
    except Exception:
        sd = torch.load(path, map_location="cpu")
    if not isinstance(sd, dict):
        sd = sd.state_dict()
    if isinstance(sd.get("state_dict"), dict):
        sd = sd["state_dict"]

    def is_decoder(k: str, v) -> bool:
        return (isinstance(v, torch.Tensor) and v.ndim == 2 and v.shape[0] != v.shape[1]
                and hidden in v.shape and ("decoder" in k.lower() or "w_dec" in k.lower()))

    keys = [k for k, v in sd.items() if is_decoder(k, v)]
    if not keys:
        raise SystemExit(f"no decoder-like 2-D tensor with a {hidden} dim in {path}; "
                         f"keys: { {k: tuple(getattr(v, 'shape', ())) for k, v in sd.items()} }")
    key = keys[0]
    w = sd[key].float()
    if w.shape[1] == hidden:                       # already (dict_size, hidden)
        feats, note = w, f"`{key}` {tuple(w.shape)} used as (dict_size, hidden) directly"
    else:                                          # (hidden, dict_size): features are columns
        feats, note = w.T, (f"`{key}` stored nn.Linear-style {tuple(w.shape)} = "
                            f"(hidden, dict_size) -> transposed; features were COLUMNS")
    return np.ascontiguousarray(feats.numpy(), dtype=np.float32), note


def unit_rows(x: np.ndarray) -> tuple[np.ndarray, int]:
    """(row-normalized copy, n dead rows). Dead (zero-norm) rows stay zero -> never selected."""
    norms = np.linalg.norm(x, axis=1, keepdims=True)
    dead = int(np.sum(norms == 0))
    norms[norms == 0] = 1.0
    return x / norms, dead


def build_directions(model_key: str, layer: int) -> dict[str, np.ndarray]:
    """Ordered {name: unit (hidden,) fp32} persona directions at the SAE layer."""
    axis, _ = load_axis_for(model_key)
    ax = axis[layer].numpy()
    a_hat = ax / np.linalg.norm(ax)

    names, roles = load_role_vectors(model_key, [layer])
    x = roles[:, 0, :]                             # (n_roles, hidden)
    mu = x.mean(axis=0)

    basis_path = os.path.join(BASES_DIR, f"{model_key}.npz")
    basis = dict(np.load(basis_path)) if os.path.exists(basis_path) else {}
    if f"L{layer}__pc" in basis:                   # qwen: committed basis has the SAE layer
        pc1, zpc1 = basis[f"L{layer}__pc"][0], basis[f"L{layer}__zpc"][0]
    else:                                          # llama L50: recompute (same math as persona_space)
        xc = x - mu
        pc1 = pca(xc, 1)[0][0]
        zpc1 = pca(xc - np.outer(xc @ a_hat, a_hat), 1)[0][0]

    dirs = {"assistant_axis": ax, "persona_PC1": pc1, "zPC1_axis_orth": zpc1}
    idx = {n: i for i, n in enumerate(names)}
    for role in TEST_ROLES:
        if role not in idx:
            raise SystemExit(f"role {role!r} not in the {model_key} role-vector set")
        dirs[f"role:{role}"] = x[idx[role]] - mu
    return {k: (v / np.linalg.norm(v)).astype(np.float32) for k, v in dirs.items()}


def top_cos(feats_unit: np.ndarray, d: np.ndarray, n: int = TOP_N) -> list[tuple[int, float]]:
    """Top-n (feature_index, signed cos) by |cos| of unit direction d with the dictionary."""
    cos = feats_unit @ d
    order = np.argsort(-np.abs(cos))[:n]
    return [(int(i), float(cos[i])) for i in order]


def omp(feats_unit: np.ndarray, d: np.ndarray, k_max: int = K_MAX) -> tuple[np.ndarray, list[int]]:
    """Greedy OMP of unit d onto dictionary rows: (R² after 1..k_max features, selected idx).

    Each step picks argmax |residual @ feature| among unselected features, then re-fits the
    least-squares coefficients over ALL selected features (so R² is monotone in k).
    """
    sel: list[int] = []
    resid = d.astype(np.float64)
    r2 = np.empty(k_max)
    for step in range(k_max):
        cors = feats_unit @ resid.astype(np.float32)
        if sel:
            cors[sel] = 0.0
        sel.append(int(np.argmax(np.abs(cors))))
        a = feats_unit[sel].T.astype(np.float64)           # (hidden, |sel|)
        coef, *_ = np.linalg.lstsq(a, d.astype(np.float64), rcond=None)
        resid = d - a @ coef
        r2[step] = 1.0 - float(resid @ resid)              # ||d|| = 1
    return r2, sel


def k_for_r2(r2: np.ndarray, target: float = R2_TARGET) -> int | None:
    hits = np.nonzero(r2 >= target)[0]
    return int(hits[0]) + 1 if len(hits) else None


def null_directions(hidden: int, n: int = N_NULL, seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    r = rng.standard_normal((n, hidden)).astype(np.float32)
    return r / np.linalg.norm(r, axis=1, keepdims=True)


def interpretation(name: str, max_cos: float, null_p95: float, r2: np.ndarray,
                   k90: int | None) -> str:
    k90_s = f"90% needs k={k90}" if k90 else f"90% not reached by k={K_MAX}"
    if max_cos >= 0.7:
        verdict = "mostly aligned with a single SAE feature"
    elif max_cos >= 2 * null_p95:
        verdict = "feature-aligned well above chance, but clearly multi-feature"
    else:
        verdict = "no privileged feature — max |cos| is at the random-direction baseline"
    return (f"`{name}`: {verdict} (max |cos| {max_cos:.3f} vs null p95 {null_p95:.3f}; "
            f"one feature explains {r2[0]:.1%} of it, {k90_s}).")


def analyze_sae(sae: dict, dirs: dict[str, np.ndarray], hidden: int,
                lines: list[str]) -> dict:
    """Run all metrics for one SAE and append its report section; returns the axis summary."""
    feats, orient_note = load_decoder(sae["repo"], sae["file"], hidden)
    feats_unit, dead = unit_rows(feats)
    del feats
    dict_size = feats_unit.shape[0]
    print(f"  [{sae['name']}] dict_size={dict_size}, hidden={hidden}, dead rows={dead}")
    print(f"    orientation: {orient_note}")

    # NULL baseline: max |cos| for 200 random unit dirs; OMP curve for the first 20.
    nulls = null_directions(hidden)
    null_max = np.abs(feats_unit @ nulls.T).max(axis=0)            # (N_NULL,)
    p95 = float(np.percentile(null_max, 95))
    null_r2 = np.stack([omp(feats_unit, nulls[i])[0] for i in range(N_NULL_OMP)])
    null_k90 = [k_for_r2(r) for r in null_r2]
    null_k90_s = (str(int(np.median([k for k in null_k90 if k])))
                  if all(null_k90) else f">{K_MAX}")
    med_null_r2 = np.median(null_r2, axis=0)

    lines += [f"## SAE: {sae['name']} — dict_size {dict_size}, hidden {hidden}\n",
              f"weights: `{sae['repo']}` / `{sae['file']}`; {orient_note}; "
              f"{dead} dead (zero-norm) rows.\n",
              f"**Null baseline** ({N_NULL} random unit dirs, seed 0): max |cos| "
              f"mean {null_max.mean():.3f}, p95 {p95:.3f}, max {null_max.max():.3f}. "
              f"OMP on {N_NULL_OMP} nulls: median R² at k={K_MAX} is {med_null_r2[-1]:.3f}, "
              f"median k for 90% {null_k90_s}.\n"]

    header = ("| direction | max cos | / null p95 | k for 90% | "
              + " | ".join(f"R²@{k}" for k in K_REPORT) + " |")
    lines += [header, "|" + "---|" * (4 + len(K_REPORT))]

    results, axis_summary = {}, {}
    for name, d in dirs.items():
        pairs = top_cos(feats_unit, d)
        r2, _ = omp(feats_unit, d)
        k90 = k_for_r2(r2)
        mx = abs(pairs[0][1])
        results[name] = (pairs, r2, k90, mx)
        cells = " | ".join(f"{r2[k - 1]:.3f}" for k in K_REPORT)
        lines.append(f"| {name} | {pairs[0][1]:+.3f} | {mx / p95:.1f}x | "
                     f"{k90 if k90 else f'>{K_MAX}'} | {cells} |")
        if name == "assistant_axis":
            axis_summary = {"max_cos": mx, "null_p95": p95, "k90": k90,
                            "top": pairs, "dict_size": dict_size}
    med_cells = " | ".join(f"{med_null_r2[k - 1]:.3f}" for k in K_REPORT)
    lines.append(f"| _null (median of {N_NULL_OMP})_ | {null_max.mean():.3f} (mean) | 1.0x "
                 f"(p95) | {null_k90_s} | {med_cells} |")

    lines.append("\n### top-10 features per direction (feature_index: cos)\n")
    for name, (pairs, _, _, _) in results.items():
        lines.append(f"- **{name}**: " + ", ".join(f"{i}: {c:+.3f}" for i, c in pairs))

    lines.append("\n### interpretation\n")
    for name, (pairs, r2, k90, mx) in results.items():
        lines.append("- " + interpretation(name, mx, p95, r2, k90))
    lines.append("")
    return axis_summary


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Assistant Axis vs public SAE dictionaries: single feature or smear?")
    ap.add_argument("--model-key", required=True, choices=sorted(SAES) + ["all"])
    ap.add_argument("--reports-dir", default=REPORTS_DIR, help="output dir (tests use a tmpdir)")
    args = ap.parse_args()

    keys = sorted(SAES) if args.model_key == "all" else [args.model_key]
    os.makedirs(args.reports_dir, exist_ok=True)
    for key in keys:
        layer = SAES[key]["layer"]
        print(f"== {key} @ L{layer} ==")
        dirs = build_directions(key, layer)
        hidden = dirs["assistant_axis"].shape[0]

        lines = [f"# {key}: is the Assistant Axis a single SAE feature? (layer {layer})\n",
                 f"Directions: released axis @ L{layer}, persona PC1 / axis-orthogonal zPC1 "
                 f"of the 275 role vectors, and three role−mean directions "
                 f"({', '.join(TEST_ROLES)}); all unit-normalized. Cosines are against "
                 "L2-normalized SAE decoder rows; R²@k is the fraction of squared norm "
                 f"explained by greedy OMP (re-fit least squares each step) with k features.\n"]
        summaries = []
        for sae in SAES[key]["saes"]:
            summaries.append(analyze_sae(sae, dirs, hidden, lines))

        if key == "llama-3.3-70b":                 # downstream Neuronpedia lookup
            lines.append("## Axis top-10 SAE feature indices (Goodfire L50 — for Neuronpedia)\n")
            lines.append(", ".join(str(i) for i, _ in summaries[0]["top"]) + "\n")

        out = os.path.join(args.reports_dir, f"sae_axis__{key}.md")
        with open(out, "w") as f:
            f.write("\n".join(lines))
        print(f"wrote {out}")
        for s in summaries:
            print(f"  axis: max|cos| {s['max_cos']:.3f} (null p95 {s['null_p95']:.3f}), "
                  f"k90 {s['k90']} of {s['dict_size']}")


if __name__ == "__main__":
    main()
