"""Manifold view of the persona state: is "not 1-D" curvature or genuine multi-dimensionality?

Motivated by Modell, Rubin-Delanchy & Whiteley (arxiv 2505.18235) and Goodfire's
neural-geometry line: a feature that is intrinsically low-dimensional can occupy MANY linear
PCs if its representation is curved, and the intrinsic coordinate is then recovered by
geodesic (shortest on-manifold path) distance, not linear projection. Our predict.py result
("z adds prediction over a") therefore has two rival readings:

  A. genuinely multi-dimensional state — z carries independent state variables;
  B. one CURVED coordinate — drift follows a bent path, linear a_t is its shadow on a chord,
     and z's contribution is (partly) the curvature correction.

Three experiments on the committed state features (laptop, no GPU):

  1. GEODESIC REPARAMETRIZATION: pool turn-states in the 17-dim (a_raw, z_1..16) frame — all
     coordinates are projections of the same centered activation onto orthonormal directions,
     so Euclidean geometry there is honest. Build a kNN graph (K minimal s.t. connected, the
     paper's rule), define g_t = graph-geodesic distance from the default-Assistant anchor,
     and re-run the prediction tasks with feature sets a | g | a+z. g ~ a+z favours reading B;
     g << a+z favours reading A.
  2. BRANCHING / INTRINSIC DIMENSION: TwoNN + Levina-Bickel intrinsic-dim estimates of the
     trajectory cloud; per-turn basin separation in z (does the cloud bifurcate, and does the
     branch turn match where basin AUC takes off?); per-trajectory monotonicity of g
     (Kendall tau of turn vs g — "is drift steady progress along the manifold?").
  3. ROLE-DICTIONARY CURVATURE: geodesic(mean-role -> default) along the role-vector manifold
     vs the straight chord (= the Assistant Axis). Ratio > 1 means the axis is a chord of a
     curved structure; the dijkstra path names the roles the "road back to Assistant" passes
     through. Short-circuits bias geodesics DOWN, so the ratio is a lower bound on curvature.

Caveats implemented as checks (from the papers' own limitations sections):
  - kNN geodesics are fragile to short-circuits -> every headline number is recomputed at 2K
    and reported side by side;
  - the graph is TRANSDUCTIVE (built on all points; labels unused) — mild leakage for the
    prediction tasks; per-fold graph rebuilds are noted as future hardening;
  - no ground-truth persona metric exists (their stated hard case), so claims here are
    topology/ordering-level, never isometry;
  - the cloud is a 17-dim shadow of the 5120-dim residual stream (k_feat z coords at one
    layer); curvature outside this subspace is invisible;
  - capped conditions are EXCLUDED from the graph (intervened states would distort the
    natural manifold) — noted in the report.

    python -m assistant_axis_experiments.state_space.manifold --model-key qwen-3-32b
"""

from __future__ import annotations

import argparse
import glob
import os

import numpy as np

from ..axes import AXIS_MODELS, target_layer_for
from . import basins
from .featurize import load_basis
from .predict import boot_delta, load_trajectories, oof_predictions, sanitized

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")
K_FEAT = 16            # z coords used for the cloud (all that featurize stored)
EARLY_TURNS = list(range(1, 9))
MANIFOLD_SETS = ("a", "g", "az")   # linear 1-D | geodesic 1-D | linear multi-D


# ---------------------------------------------------------------- geometry helpers

def knn_graph_min_connected(X: np.ndarray, k_min: int = 4, k_max: int = 60):
    """Symmetric distance-weighted kNN graph with the smallest K that connects it
    (Modell et al.'s rule). Returns (graph, K)."""
    from scipy.sparse.csgraph import connected_components
    from sklearn.neighbors import kneighbors_graph

    for k in range(k_min, k_max + 1):
        g = kneighbors_graph(X, n_neighbors=k, mode="distance")
        n_comp, _ = connected_components(g, directed=False)
        if n_comp == 1:
            return g, k
    raise SystemExit(f"kNN graph disconnected even at K={k_max}")


def geodesics_from(X: np.ndarray, source_row: int, k: int | None = None):
    """Geodesic distances from one row via dijkstra on the kNN graph.
    Returns (distances, K_used, predecessors)."""
    from scipy.sparse.csgraph import dijkstra
    from sklearn.neighbors import kneighbors_graph

    if k is None:
        graph, k = knn_graph_min_connected(X)
    else:
        graph = kneighbors_graph(X, n_neighbors=k, mode="distance")
    dist, pred = dijkstra(graph, directed=False, indices=source_row, return_predecessors=True)
    return dist, k, pred


def twonn_dim(X: np.ndarray, trim: float = 0.1) -> float:
    """TwoNN intrinsic dimension (Facco et al. 2017): MLE from 2nd/1st-neighbour ratios,
    trimming the largest `trim` fraction (standard, guards against off-manifold outliers)."""
    from sklearn.neighbors import NearestNeighbors

    d, _ = NearestNeighbors(n_neighbors=3).fit(X).kneighbors(X)
    mu = d[:, 2] / np.maximum(d[:, 1], 1e-12)
    mu = np.sort(mu)[: int(len(mu) * (1 - trim))]
    return float(len(mu) / np.sum(np.log(np.maximum(mu, 1 + 1e-12))))


def levina_bickel_dim(X: np.ndarray, k: int = 20) -> float:
    """Levina-Bickel MLE intrinsic dimension, averaged over points."""
    from sklearn.neighbors import NearestNeighbors

    d, _ = NearestNeighbors(n_neighbors=k + 1).fit(X).kneighbors(X)
    d = np.maximum(d[:, 1:], 1e-12)                       # (n, k) sorted ascending
    with np.errstate(divide="ignore"):
        inv = np.mean(np.log(d[:, -1:] / d[:, :-1]), axis=1)
    return float(np.mean(1.0 / np.maximum(inv, 1e-12)))


# ---------------------------------------------------------------- cloud construction

def build_cloud(records: list[dict], basis: dict, layer: int):
    """(X (n,17), row->(record index, turn index) arrays, anchor point).

    Frame: [ (act-mu)@a_hat , (act-mu)@zpc_1..16 ] — orthonormal directions, raw residual
    units, so Euclidean distance is the true distance of the centered activation's projection
    onto this subspace. a is stored in axis units, so rescale by (anchor_default - anchor_role);
    the default-Assistant anchor is [(ad - ar), 0, ..., 0] since default - mu ≈ axis ⊥ z-PCs.
    """
    ad = float(basis[f"L{layer}__anchor_default"])
    ar = float(basis[f"L{layer}__anchor_role_mean"])
    scale = ad - ar
    rows, rec_idx, turn_idx = [], [], []
    for i, rec in enumerate(records):
        for t in range(len(rec["a"])):
            rows.append(np.concatenate([[rec["a"][t] * scale], rec["z"][t]]))
            rec_idx.append(i)
            turn_idx.append(t)
    anchor = np.zeros(rows[0].shape)
    anchor[0] = scale
    return np.vstack(rows), np.array(rec_idx), np.array(turn_idx), anchor


def attach_geodesic(records: list[dict], X, rec_idx, turn_idx, anchor, k: int | None):
    """Compute g for every turn-state (graph over cloud + anchor node) and attach per-record
    series rec["g"]. Returns K used. g is normalized by the anchor scale so it is comparable
    to axis units in magnitude (0 at the anchor, growing along the manifold)."""
    Xa = np.vstack([X, anchor])
    dist, k_used, _ = geodesics_from(Xa, source_row=len(Xa) - 1, k=k)
    g = dist[:-1] / np.abs(anchor[0])
    for i, rec in enumerate(records):
        mask = rec_idx == i
        order = np.argsort(turn_idx[mask])
        rec["g"] = g[np.where(mask)[0][order]]
    return k_used


# ---------------------------------------------------------------- experiment 1: g vs a vs a+z

def state_sets(rec: dict, t: int) -> dict | None:
    if len(rec["a"]) < t:
        return None
    i = t - 1
    return {
        "a": rec["a"][i:i + 1],
        "g": rec["g"][i:i + 1],
        "az": np.concatenate([rec["a"][i:i + 1], rec["z"][i], rec["z_norm"][i:i + 1]]),
    }


def geodesic_prediction_tasks(records: list[dict], lines: list[str], tag: str) -> dict:
    """The predict.py tasks with feature sets a | g | a+z. Verdict logic: g≈az -> curvature
    (reading B), g<<az -> genuine multi-dimensionality (reading A)."""
    from sklearn.metrics import r2_score, roc_auc_score

    out: dict = {}

    # -- next-turn state: targets a_{t+1}, g_{t+1}, |z|_{t+1}
    rows = {fs: [] for fs in MANIFOLD_SETS}
    ys = {"a": [], "g": [], "zn": []}
    groups = []
    for rec in records:
        for t in range(1, len(rec["a"])):
            s = state_sets(rec, t)
            for fs in MANIFOLD_SETS:
                rows[fs].append(s[fs])
            ys["a"].append(rec["a"][t])
            ys["g"].append(rec["g"][t])
            ys["zn"].append(rec["z_norm"][t])
            groups.append(rec["group"])
    groups = np.asarray(groups)
    lines.append(f"### Next-turn state ({tag})\n")
    lines.append("| target | a (linear 1-D) | g (geodesic 1-D) | a+z | Δ(g − a) 95% CI |")
    lines.append("|---|---|---|---|---|")
    for name, y in (("a_{t+1}", ys["a"]), ("g_{t+1}", ys["g"]), ("|z|_{t+1}", ys["zn"])):
        y = np.asarray(y)
        preds = {fs: oof_predictions(np.vstack(rows[fs]), y, groups, "ridge")
                 for fs in MANIFOLD_SETS}
        r2 = {fs: r2_score(y, preds[fs]) for fs in MANIFOLD_SETS}
        lo, hi = boot_delta(r2_score, y, preds["a"], preds["g"], groups)
        lines.append(f"| {name} | {r2['a']:.3f} | {r2['g']:.3f} | {r2['az']:.3f} "
                     f"| [{lo:+.3f}, {hi:+.3f}] |")
        out[f"next_{name}"] = r2
    lines.append("")

    # -- eventual basin from the state at turn t (labeled, non-capped conditions)
    labeled = [r for r in records if r["label"] is not None and "capped" not in r["condition"]
               and not r["condition"].startswith("usersim")]
    by_cond: dict[str, list[dict]] = {}
    for r in labeled:
        by_cond.setdefault(r["condition"], []).append(r)
    for cond, recs in sorted(by_cond.items()):
        classes = sorted({r["label"] for r in recs})
        if len(classes) != 2:
            continue
        lines.append(f"### Eventual basin, `{cond}` ({tag}) — {classes[1]} vs {classes[0]}\n")
        lines.append("| turn t | a | g | a+z |")
        lines.append("|---|---|---|---|")
        aucs = {fs: [] for fs in MANIFOLD_SETS}
        for t in EARLY_TURNS:
            X, y, gr = {fs: [] for fs in MANIFOLD_SETS}, [], []
            for r in recs:
                s = state_sets(r, t)
                if s is None:
                    continue
                for fs in MANIFOLD_SETS:
                    X[fs].append(s[fs])
                y.append(classes.index(r["label"]))
                gr.append(r["group"])
            y, gr = np.asarray(y), np.asarray(gr)
            if len(y) < 20 or len(np.unique(y)) < 2:
                continue
            row = [str(t)]
            for fs in MANIFOLD_SETS:
                p = oof_predictions(np.vstack(X[fs]), y, gr, "logistic")
                ok = ~np.isnan(p)
                auc = roc_auc_score(y[ok], p[ok]) if ok.sum() >= 10 else np.nan
                aucs[fs].append(auc)
                row.append(f"{auc:.3f}")
            lines.append("| " + " | ".join(row) + " |")
        out[f"basin_{cond}"] = {fs: [round(float(x), 3) for x in aucs[fs]] for fs in MANIFOLD_SETS}
        lines.append("")

    # -- transition time from the state at turn 2
    from scipy.stats import spearmanr
    X, y, gr = {fs: [] for fs in MANIFOLD_SETS}, [], []
    for rec in records:
        cross = basins.first_crossing(rec["a"], threshold=0.0)
        s = state_sets(rec, 2)
        if s is None or cross is None or cross <= 2:
            continue
        for fs in MANIFOLD_SETS:
            X[fs].append(s[fs])
        y.append(cross)
        gr.append(rec["group"])
    y, gr = np.asarray(y, dtype=float), np.asarray(gr)
    if len(y) >= 30:
        lines.append(f"### Transition time from turn-2 state ({tag}, n={len(y)})\n")
        lines.append("| features | OOF R² | Spearman ρ |")
        lines.append("|---|---|---|")
        for fs in MANIFOLD_SETS:
            p = oof_predictions(np.vstack(X[fs]), y, gr, "ridge")
            rho = spearmanr(y, p).statistic
            out[f"transition_{fs}"] = {"r2": float(r2_score(y, p)), "rho": float(rho)}
            lines.append(f"| {fs} | {r2_score(y, p):.3f} | {rho:.3f} |")
        lines.append("")
    return out


# ---------------------------------------------------------------- experiment 2: branching

def branching_report(records: list[dict], X, rec_idx, turn_idx, lines: list[str],
                     fig_path: str) -> None:
    from scipy.stats import kendalltau

    # intrinsic dimension of the trajectory cloud
    d2nn = twonn_dim(X)
    dlb10, dlb20 = levina_bickel_dim(X, 10), levina_bickel_dim(X, 20)
    lines.append("## Experiment 2 — intrinsic dimension & branching\n")
    lines.append(f"- trajectory cloud (n={len(X)}, ambient 17-D): TwoNN {d2nn:.1f}, "
                 f"Levina-Bickel k=10 {dlb10:.1f} / k=20 {dlb20:.1f} "
                 f"(vs 7 linear PCs for 70% role variance)")

    # monotonicity: is drift steady progress along the manifold? (split ai2ai vs controls —
    # user-sim runs are SUPPOSED to stay put, so pooling them dilutes the diagnostic)
    for grp, name in ((lambda c: not c.startswith("usersim"), "ai2ai"),
                      (lambda c: c.startswith("usersim"), "usersim controls")):
        taus = [kendalltau(np.arange(len(r["g"])), r["g"]).statistic
                for r in records if len(r["g"]) >= 6 and grp(r["condition"])]
        if taus:
            lines.append(f"- per-trajectory Kendall τ(turn, g), {name}: median "
                         f"{np.median(taus):+.2f} (IQR {np.percentile(taus, 25):+.2f}.."
                         f"{np.percentile(taus, 75):+.2f}, n={len(taus)}) — the years-manifold "
                         "ordering diagnostic")

    # basin separation in z per turn position (branch point) — labeled ai2ai runs only
    labeled = [r for r in records if r["label"] is not None and "capped" not in r["condition"]
               and not r["condition"].startswith("usersim")]
    classes = sorted({r["label"] for r in labeled})
    sep_curve = []
    if len(classes) == 2:
        for t in EARLY_TURNS:
            zs = {c: [] for c in classes}
            for r in labeled:
                if len(r["z"]) >= t:
                    zs[r["label"]].append(r["z"][t - 1])
            if min(len(v) for v in zs.values()) < 5:
                sep_curve.append(np.nan)
                continue
            m0, m1 = (np.mean(zs[c], axis=0) for c in classes)
            within = np.mean([np.std(zs[c], axis=0).mean() for c in classes])
            sep_curve.append(float(np.linalg.norm(m0 - m1) / max(within, 1e-9)))
        lines.append(f"- basin separation in z (between-mean distance / within spread) by turn: "
                     + ", ".join(f"t{t}={s:.2f}" for t, s in zip(EARLY_TURNS, sep_curve)))
    lines.append("")

    # figure: PCA of the cloud colored by basin + separation curve
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.4))
    Xc = X - X.mean(axis=0)
    _, _, vt = np.linalg.svd(Xc, full_matrices=False)
    P = Xc @ vt[:2].T
    colors = {"design": "#0072B2", "devotion": "#D55E00", "workshop": "#0072B2",
              "farewell": "#D55E00", "civics": "#009E73"}
    lab_of = {}
    for i, r in enumerate(records):
        lab_of[i] = r["label"] if (r["label"] and "capped" not in r["condition"]
                                   and not r["condition"].startswith("usersim")) else None
    for i in range(len(X)):
        lab = lab_of[rec_idx[i]]
        axs[0].scatter(P[i, 0], P[i, 1], s=4, linewidths=0, alpha=0.35,
                       color=colors.get(lab, "#bbbbbb"))
    for lab in sorted({l for l in lab_of.values() if l}):
        axs[0].scatter([], [], s=20, color=colors.get(lab, "#bbbbbb"), label=lab)
    axs[0].legend(frameon=False, fontsize=8)
    axs[0].set_xlabel("cloud PC1")
    axs[0].set_ylabel("cloud PC2")
    axs[0].set_title("turn-state cloud (grey = unlabeled/control)", fontsize=10)
    if sep_curve:
        axs[1].plot(EARLY_TURNS, sep_curve, marker="o", color="#0072B2")
        axs[1].set_xlabel("turn t")
        axs[1].set_ylabel("basin separation in z")
        axs[1].set_title("branch development over turns", fontsize=10)
    for ax in axs:
        ax.grid(alpha=0.25, linewidth=0.5)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
    fig.tight_layout()
    fig.savefig(fig_path, dpi=150)
    lines.append(f"![branching]({os.path.basename(fig_path)})\n")


# ---------------------------------------------------------------- experiment 3: dictionary

def dictionary_curvature(basis: dict, layer: int, lines: list[str]) -> None:
    """Geodesic(mean-role -> default) along the role manifold vs the straight chord (=axis)."""
    ad = float(basis[f"L{layer}__anchor_default"])
    ar = float(basis[f"L{layer}__anchor_role_mean"])
    scale = ad - ar
    names = [str(n) for n in basis["role_names"]]
    R = np.hstack([basis[f"L{layer}__role_a"][:, None] * scale, basis[f"L{layer}__role_z"]])
    origin = np.zeros(R.shape[1])                        # mean role (centered frame)
    default = np.zeros(R.shape[1])
    default[0] = scale
    pts = np.vstack([R, origin, default])
    i_origin, i_default = len(pts) - 2, len(pts) - 1

    lines.append("## Experiment 3 — role-dictionary curvature (is the axis a chord?)\n")
    _, base_k, _ = geodesics_from(pts, i_default, k=None)
    for k_used in (base_k, 2 * base_k):
        dist, _, pred = geodesics_from(pts, i_default, k=k_used)
        ratio = dist[i_origin] / np.linalg.norm(default - origin)
        # walk the shortest path mean-role -> default, naming the roles it passes through
        path, node = [], i_origin
        while node != i_default and node >= 0:
            if node < len(names):
                path.append(names[node])
            node = pred[node]
        lines.append(f"- K={k_used}: geodesic/chord ratio {ratio:.2f} "
                     f"(n={len(names)} roles; short-circuits bias this DOWN — lower bound); "
                     f"path mean-role→default passes through: {', '.join(path) or '(direct)'}")
    lines.append("")


# ---------------------------------------------------------------- main

def main() -> None:
    ap = argparse.ArgumentParser(description="Manifold analysis of the persona state space.")
    ap.add_argument("--model-key", required=True, choices=sorted(AXIS_MODELS))
    ap.add_argument("--results-dir", nargs="+", default=None)
    ap.add_argument("--layer", type=int, default=None)
    ap.add_argument("--reports-dir", default=REPORTS_DIR)
    args = ap.parse_args()

    layer = args.layer if args.layer is not None else target_layer_for(args.model_key)
    dirs = args.results_dir or sorted(glob.glob(f"results/axis_{sanitized(args.model_key)}_*ai2ai"))
    dirs = [d for d in dirs if "capped" not in d]         # intervened states distort the manifold
    basis = load_basis(args.model_key)
    records = load_trajectories(args.model_key, dirs, layer, k_use=K_FEAT)
    if not records:
        raise SystemExit("no state-feature trajectories found")
    X, rec_idx, turn_idx, anchor = build_cloud(records, basis, layer)
    print(f"{len(records)} trajectories, {len(X)} turn-states @ L{layer}")

    os.makedirs(args.reports_dir, exist_ok=True)
    lines = [f"# {args.model_key}: manifold analysis (layer {layer})\n",
             f"{len(X)} turn-states from {len(records)} view-trajectories "
             f"(capped conditions excluded from the graph).",
             "Feature sets: a = linear axis projection (1-D), g = geodesic distance from the "
             "default-Assistant anchor along the kNN manifold graph (still 1-D), a+z = linear "
             "multi-D. Reading B (curvature) predicts g ≈ a+z; reading A (genuine multi-D) "
             "predicts g ≪ a+z on basin/timing.\n"]

    # experiment 1 at K_min and 2K (short-circuit sensitivity)
    lines.append("## Experiment 1 — geodesic 1-D vs linear 1-D vs linear multi-D\n")
    k_used = attach_geodesic(records, X, rec_idx, turn_idx, anchor, k=None)
    print(f"kNN graph connected at K={k_used}")
    lines.append(f"kNN graph: K={k_used} (minimal connected), robustness pass at K={2 * k_used}.\n")
    res_k = geodesic_prediction_tasks(records, lines, tag=f"K={k_used}")
    attach_geodesic(records, X, rec_idx, turn_idx, anchor, k=2 * k_used)
    res_2k = geodesic_prediction_tasks(records, lines, tag=f"K={2 * k_used}")
    # keep K_min geodesics on records for experiment 2
    attach_geodesic(records, X, rec_idx, turn_idx, anchor, k=k_used)

    branching_report(records, X, rec_idx, turn_idx, lines,
                     os.path.join(args.reports_dir, f"manifold__{args.model_key}__branching.png"))
    dictionary_curvature(basis, layer, lines)

    lines.append("## Caveats (from the source papers' limitations)\n")
    lines.append("- kNN geodesics are fragile to short-circuits (Modell et al. §4.1): all "
                 "experiment-1 numbers appear at K_min and 2K — trust conclusions only where "
                 "they agree. Dictionary curvature is a LOWER bound for the same reason.")
    lines.append("- The graph is transductive (test runs' points shape the manifold; labels "
                 "unused). Per-fold graph rebuilds would harden this.")
    lines.append("- No ground-truth persona metric exists (the paper's own hard case), so "
                 "these are topology/ordering claims, not isometry claims.")
    lines.append("- 17-D shadow: curvature outside the stored (a, z_1..16) subspace at this "
                 "layer is invisible. Full-space rerun needs the turn_acts npz (one replay).")
    lines.append(f"- n={len(basis['role_names'])} role vectors is thin for manifold estimation "
                 "in experiment 3.")
    lines.append("- Intrinsic-dim estimators are noise-limited: when measurement noise is "
                 "comparable to nearest-neighbour spacing they read the noise ball's dimension "
                 "(biased toward ambient 17). Treat the TwoNN number as an UPPER bound on "
                 "intrinsic dimension; the k=10 vs k=20 Levina-Bickel spread indicates "
                 "scale-sensitivity.")

    out = os.path.join(args.reports_dir, f"manifold__{args.model_key}.md")
    with open(out, "w") as f:
        f.write("\n".join(lines))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
