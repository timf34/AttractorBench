"""Build the persona-space basis from the paper's released role vectors (laptop, CPU).

The assistant-axis release (``lu-christina/assistant-axis-vectors``) ships ~514 per-role mean
activation vectors per model alongside the axis itself. The axis is one direction in that
space; the paper notes persona space needs 4-19 principal components to reach 70% of
role-vector variance, so a 1-D readout necessarily discards most of the persona structure.
This stage builds, per model and layer:

  - raw PCA over the (centered) role vectors -> how many components 70% actually takes here
    (reproduces the paper's claim from their own artifacts);
  - the Z-BASIS: PCA of the role vectors after projecting out the (normalized) axis
    direction. z_t coordinates measured in this basis are orthogonal to a_t by construction —
    exactly the "orthogonal coordinates determining persona identity" split of the
    a_t / z_t decomposition.

Sanity check: cos(default_vector - mean(role vectors), released axis) ~ 1 would confirm the
role set matches the paper's own axis construction.

Outputs (committable, ~MBs):
  state_space/bases/<model_key>.npz     per-layer basis: axis unit, mean role vector, raw PCs,
                                        z-PCs, explained-variance ratios, per-role coordinates
  state_space/reports/persona_space__<model_key>.png
  printed geometry table (angel-vs-demon: same distance along the axis, different z?)

    python -m assistant_axis_experiments.state_space.persona_space --model-key qwen-3-32b
    python -m assistant_axis_experiments.state_space.persona_space --model-key all
"""

from __future__ import annotations

import argparse
import glob
import os

import numpy as np

from ..axes import AXIS_DATASET, AXIS_MODELS, load_axis_for, target_layer_for
from ..vendor.assistant_axis import load_axis

# Layers at which activations are dumped / bases built: ~quarter, target (the paper's readout
# layer, = half depth), ~three-quarter. Llama's trajectory direction is layer-dependent (early
# layers drift down, late layers climb — see EXPERIMENT_LOG) and the paper's llama capping band
# is late (56-71), so llama gets a fourth, late layer.
LAYERS = {
    "gemma-2-27b": [11, 22, 34],
    "qwen-3-32b": [16, 32, 48],
    "llama-3.3-70b": [20, 40, 60, 64],
}

N_COMPONENTS = 32          # stored basis size (analysis picks how many to use)
VARIANCE_TARGET = 0.70     # the paper's reference threshold

BASES_DIR = os.path.join(os.path.dirname(__file__), "bases")
REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")

# Roles annotated on the geometry panel when present (angel/demon is the mentor's example of
# equal axis-distance with opposite behavioral consequences).
HIGHLIGHT_ROLES = ["assistant", "angel", "demon", "poet", "mystic", "philosopher",
                   "oracle", "engineer", "sage", "trickster"]


def load_role_vectors(model_key: str, layers: list[int]) -> tuple[list[str], np.ndarray]:
    """(names, (n_roles, n_sel_layers, hidden) fp32) role vectors at the selected layers."""
    from huggingface_hub import snapshot_download

    local = snapshot_download(
        AXIS_DATASET, repo_type="dataset",
        allow_patterns=[f"{model_key}/role_vectors/*"],
    )
    paths = sorted(glob.glob(os.path.join(local, model_key, "role_vectors", "*.pt")))
    if not paths:
        raise SystemExit(f"no role vectors found for {model_key} in {local}")
    names, rows = [], []
    for p in paths:
        names.append(os.path.splitext(os.path.basename(p))[0])
        vec = load_axis(p).float()                       # (n_layers, hidden)
        rows.append(vec[layers].numpy())
    return names, np.stack(rows)                         # (n_roles, n_sel_layers, hidden)


def pca(x: np.ndarray, k: int) -> tuple[np.ndarray, np.ndarray]:
    """(components (k, dim), explained_variance_ratio (full)) of already-centered rows."""
    _, s, vt = np.linalg.svd(x, full_matrices=False)
    evr = s**2 / np.sum(s**2)
    return vt[:k], evr


def n_for_variance(evr: np.ndarray, target: float) -> int:
    return int(np.searchsorted(np.cumsum(evr), target) + 1)


def build_basis(model_key: str, layers: list[int], k: int) -> dict:
    """All per-layer arrays for one model, keyed ``L<layer>__<name>``, plus role names."""
    from huggingface_hub import hf_hub_download

    names, roles = load_role_vectors(model_key, layers)
    axis, anchors = load_axis_for(model_key)             # axis: (n_layers, hidden)
    default_vec = load_axis(hf_hub_download(AXIS_DATASET, f"{model_key}/default_vector.pt",
                                            repo_type="dataset")).float().numpy()

    out: dict = {"role_names": np.array(names), "layers": np.array(layers)}
    axis_np = axis.numpy()
    for li, layer in enumerate(layers):
        x = roles[:, li, :]                              # (n_roles, hidden)
        a_hat = axis_np[layer] / np.linalg.norm(axis_np[layer])
        mu = x.mean(axis=0)

        # sanity: does default - mean(roles) reproduce the released axis at this layer?
        recon = default_vec[layer] - mu
        cos_recon = float(recon @ axis_np[layer]
                          / (np.linalg.norm(recon) * np.linalg.norm(axis_np[layer])))

        xc = x - mu
        pc, evr = pca(xc, k)
        x_perp = xc - np.outer(xc @ a_hat, a_hat)        # project out the axis direction
        zpc, zevr = pca(x_perp, k)

        anchor_d = anchors["default"][layer]
        anchor_r = anchors["role_mean"][layer]
        role_a = (x @ a_hat - anchor_r) / (anchor_d - anchor_r)   # axis units per role
        role_z = x_perp @ zpc.T                                    # (n_roles, k)

        out.update({
            f"L{layer}__axis_unit": a_hat.astype(np.float32),
            f"L{layer}__mean_role": mu.astype(np.float32),
            f"L{layer}__anchor_default": np.float64(anchor_d),
            f"L{layer}__anchor_role_mean": np.float64(anchor_r),
            f"L{layer}__pc": pc.astype(np.float32),
            f"L{layer}__evr": evr.astype(np.float32),
            f"L{layer}__zpc": zpc.astype(np.float32),
            f"L{layer}__zevr": zevr.astype(np.float32),
            f"L{layer}__role_a": role_a.astype(np.float32),
            f"L{layer}__role_z": role_z.astype(np.float32),
            f"L{layer}__cos_axis_reconstruction": np.float64(cos_recon),
        })
    return out


def geometry_report(model_key: str, basis: dict, target_layer: int) -> None:
    """Printed table + 3-panel figure at the target layer."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    names = [str(n) for n in basis["role_names"]]
    L = target_layer
    evr, zevr = basis[f"L{L}__evr"], basis[f"L{L}__zevr"]
    role_a, role_z = basis[f"L{L}__role_a"], basis[f"L{L}__role_z"]
    n70 = n_for_variance(evr, VARIANCE_TARGET)
    n70z = n_for_variance(zevr, VARIANCE_TARGET)
    cos_recon = float(basis[f"L{L}__cos_axis_reconstruction"])
    cos_axis_pc1 = float(np.abs(basis[f"L{L}__pc"][0] @ basis[f"L{L}__axis_unit"]))

    print(f"\n== {model_key} @ L{L} ({len(names)} roles) ==")
    print(f"  cos(default - mean(roles), released axis) = {cos_recon:+.3f}")
    print(f"  components for {VARIANCE_TARGET:.0%} variance: raw {n70}, axis-removed {n70z} "
          f"(paper: 4-19 across models/layers)")
    print(f"  |cos(axis, PC1)| = {cos_axis_pc1:.3f}")
    idx = {n: i for i, n in enumerate(names)}
    if "angel" in idx and "demon" in idx:
        ia, idm = idx["angel"], idx["demon"]
        z_dist = float(np.linalg.norm(role_z[ia] - role_z[idm]))
        typ = float(np.median(np.linalg.norm(role_z - role_z.mean(0), axis=1)))
        print(f"  angel a={role_a[ia]:+.2f} vs demon a={role_a[idm]:+.2f} axis-units "
              f"(gap {abs(role_a[ia]-role_a[idm]):.2f}); z-distance {z_dist:.1f} "
              f"vs median role z-spread {typ:.1f}")

    fig, axs = plt.subplots(1, 3, figsize=(15.5, 4.4))
    for e, label, color in ((evr, "raw persona space", "#0072B2"),
                            (zevr, "axis direction removed", "#D55E00")):
        axs[0].plot(np.arange(1, len(e) + 1), np.cumsum(e), color=color, linewidth=2,
                    label=f"{label} ({n_for_variance(e, VARIANCE_TARGET)} comps for 70%)")
    axs[0].axhline(VARIANCE_TARGET, color="#444444", linewidth=1, linestyle="--")
    axs[0].set_xlim(0, N_COMPONENTS)
    axs[0].set_xlabel("principal components")
    axs[0].set_ylabel("cumulative explained variance")
    axs[0].set_title("role-vector variance is many-dimensional", fontsize=10)
    axs[0].legend(frameon=False, fontsize=8, loc="lower right")

    sc = axs[1].scatter(role_z[:, 0], role_z[:, 1], c=role_a, cmap="coolwarm_r", s=14,
                        linewidths=0, vmin=np.percentile(role_a, 2), vmax=np.percentile(role_a, 98))
    fig.colorbar(sc, ax=axs[1], label="a (axis units)")
    for n in HIGHLIGHT_ROLES:
        if n in idx:
            i = idx[n]
            axs[1].annotate(n, (role_z[i, 0], role_z[i, 1]), fontsize=8, fontweight="bold")
    axs[1].set_xlabel("zPC1")
    axs[1].set_ylabel("zPC2")
    axs[1].set_title("roles in the axis-orthogonal plane", fontsize=10)

    z_norm = np.linalg.norm(role_z, axis=1)
    axs[2].scatter(role_a, z_norm, s=12, color="#888888", linewidths=0, alpha=0.7)
    for n in HIGHLIGHT_ROLES:
        if n in idx:
            i = idx[n]
            axs[2].scatter([role_a[i]], [z_norm[i]], s=26, color="#D55E00", zorder=3)
            axs[2].annotate(n, (role_a[i], z_norm[i]), fontsize=8, fontweight="bold")
    axs[2].set_xlabel("a (axis units; 1 = default Assistant)")
    axs[2].set_ylabel("|z| (norm of orthogonal coords)")
    axs[2].set_title("equal axis-distance ≠ equal persona", fontsize=10)
    for ax in axs:
        ax.grid(alpha=0.25, linewidth=0.5)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)

    fig.suptitle(f"{model_key} persona space @ layer {L}", fontsize=12)
    fig.tight_layout()
    os.makedirs(REPORTS_DIR, exist_ok=True)
    out = os.path.join(REPORTS_DIR, f"persona_space__{model_key}.png")
    fig.savefig(out, dpi=150)
    print(f"  wrote {out}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Build persona-space bases from released role vectors.")
    ap.add_argument("--model-key", required=True,
                    choices=sorted(AXIS_MODELS) + ["all"])
    ap.add_argument("--k", type=int, default=N_COMPONENTS)
    args = ap.parse_args()

    keys = sorted(AXIS_MODELS) if args.model_key == "all" else [args.model_key]
    os.makedirs(BASES_DIR, exist_ok=True)
    for key in keys:
        basis = build_basis(key, LAYERS[key], args.k)
        out = os.path.join(BASES_DIR, f"{key}.npz")
        np.savez_compressed(out, **basis)
        print(f"wrote {out}")
        geometry_report(key, basis, target_layer_for(key))


if __name__ == "__main__":
    main()
