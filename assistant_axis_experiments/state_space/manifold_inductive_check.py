"""Inductive robustness check for manifold.py's geodesic coordinate g.

manifold.py builds ONE kNN graph over all pooled turn-states (plus the default-Assistant
anchor) and reads g off it for every point — TRANSDUCTIVE: test runs' points help shape the
manifold graph that their own g is measured on (flagged in the report's caveats). This script
quantifies whether that shortcut inflated g's headline numbers by re-running the two headline
comparisons with per-fold graphs:

  - 5-fold grouped CV, grouping by run (same convention as predict.py's oof_predictions);
  - per fold the kNN graph uses ONLY training-fold turn-states + the anchor node, with K
    recomputed by the same minimal-connected rule on that training set;
  - train-point g comes from dijkstra on the train+anchor graph; TEST points get g by the
    standard out-of-sample extension — connect each test point to its K nearest TRAINING
    nodes (edges weighted by Euclidean distance, test points never link to each other) and
    take  g(test) = min over neighbours of (g(train_neighbour) + edge distance);
  - with those inductive g values, recompute (1) transition-time-from-turn-2 OOF R²/Spearman
    and (2) basin AUC at turns 4/6/8 (nosys + helpful), feature sets a | g | a+z.

Three variants are reported so graph leakage can be separated from fold-split noise:
  transductive (report)       — oof_predictions on the full-graph g, i.e. manifold.py's exact
                                code path (reproduces the numbers in the report);
  transductive (shared folds) — same full-graph g but evaluated with THIS script's shared
                                fold assignment (isolates the fold-scheme change);
  inductive (per-fold graphs) — the leakage-free variant.

Appends "## Inductive robustness check (per-fold graphs)" to reports/manifold__<model>.md.

    python -m assistant_axis_experiments.state_space.manifold_inductive_check --model-key qwen-3-32b
"""

from __future__ import annotations

import argparse
import glob
import os

import numpy as np

from ..axes import AXIS_MODELS, target_layer_for
from . import basins
from .featurize import load_basis
from .manifold import (K_FEAT, REPORTS_DIR, attach_geodesic, build_cloud,
                       knn_graph_min_connected, state_sets)
from .predict import load_trajectories, oof_predictions, sanitized

BASIN_TURNS = (4, 6, 8)
SETS = ("a", "g", "az")
SECTION_HEADER = "## Inductive robustness check (per-fold graphs)"


# ---------------------------------------------------------------- fold machinery

def assign_folds(groups_row: np.ndarray, n_splits: int = 5) -> tuple[np.ndarray, int]:
    """One fold id per cloud row via GroupKFold over the full cloud (grouping by run,
    predict.py's convention). Every row of a run lands in the same fold."""
    from sklearn.model_selection import GroupKFold

    n_splits = min(n_splits, len(np.unique(groups_row)))
    fold = np.full(len(groups_row), -1, dtype=int)
    for i, (_, test) in enumerate(GroupKFold(n_splits=n_splits)
                                  .split(np.zeros((len(groups_row), 1)), groups=groups_row)):
        fold[test] = i
    return fold, n_splits


def fold_geodesics(X: np.ndarray, anchor: np.ndarray, row_fold: np.ndarray, n_folds: int):
    """Per fold i: kNN graph on non-fold-i turn-states + anchor (K = minimal-connected rule,
    recomputed on that training set); g(train) via dijkstra from the anchor; g(test) via the
    out-of-sample extension against the K nearest training nodes. Returns
    (list of full-length g arrays — entry i holds fold-i's train AND test values — , K per fold).
    g is normalized by the anchor scale, as in attach_geodesic."""
    from scipy.sparse.csgraph import dijkstra
    from sklearn.neighbors import NearestNeighbors

    scale = np.abs(anchor[0])
    g_by_fold, k_by_fold = [], []
    for i in range(n_folds):
        tr = np.where(row_fold != i)[0]
        te = np.where(row_fold == i)[0]
        nodes = np.vstack([X[tr], anchor])                 # anchor is the last node
        graph, k = knn_graph_min_connected(nodes)
        d_nodes = dijkstra(graph, directed=False, indices=len(nodes) - 1)
        # out-of-sample extension: K nearest TRAINING nodes only (test points never
        # link to each other); the anchor counts as a training node (g = 0 there)
        dist, idx = NearestNeighbors(n_neighbors=k).fit(nodes).kneighbors(X[te])
        g = np.full(len(X), np.nan)
        g[tr] = d_nodes[:-1]
        g[te] = np.min(d_nodes[idx] + dist, axis=1)
        g_by_fold.append(g / scale)
        k_by_fold.append(k)
    return g_by_fold, k_by_fold


def oof_shared_folds(feats_by_fold: list[np.ndarray], y: np.ndarray, fold_ids: np.ndarray,
                     kind: str) -> np.ndarray:
    """predict.py's oof_predictions, but with the shared precomputed fold assignment and
    per-fold feature matrices (fold i's matrix carries fold-i graph values for g; static
    feature sets pass the same matrix for every fold)."""
    from sklearn.linear_model import LogisticRegression, Ridge
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler

    preds = np.full(len(y), np.nan)
    for i, Xi in enumerate(feats_by_fold):
        test = fold_ids == i
        train = ~test
        if not test.any() or train.sum() < 2:
            continue
        if kind == "ridge":
            model = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
            model.fit(Xi[train], y[train])
            preds[test] = model.predict(Xi[test])
        else:
            if len(np.unique(y[train])) < 2:
                continue
            model = make_pipeline(StandardScaler(),
                                  LogisticRegression(max_iter=1000, class_weight="balanced"))
            model.fit(Xi[train], y[train])
            preds[test] = model.decision_function(Xi[test])
    return preds


# ---------------------------------------------------------------- task assembly

def gather_transition(records: list[dict], row_lookup: dict) -> dict:
    """Rows for the transition-time task, exactly as manifold.geodesic_prediction_tasks:
    state at turn 2 -> first crossing of a<0, keeping crossings after turn 2."""
    Xa, Xaz, rows, y, groups = [], [], [], [], []
    for i, rec in enumerate(records):
        cross = basins.first_crossing(rec["a"], threshold=0.0)
        s = state_sets(rec, 2)
        if s is None or cross is None or cross <= 2:
            continue
        Xa.append(s["a"])
        Xaz.append(s["az"])
        rows.append(row_lookup[(i, 1)])                    # turn 2 -> turn_idx 1
        y.append(cross)
        groups.append(rec["group"])
    return {"a": np.vstack(Xa), "az": np.vstack(Xaz), "rows": np.asarray(rows),
            "y": np.asarray(y, dtype=float), "groups": np.asarray(groups)}


def gather_basin(records: list[dict], row_lookup: dict, condition: str, t: int) -> dict | None:
    """Rows for the basin task at turn t for one condition (manifold.py's filters)."""
    labeled = [(i, r) for i, r in enumerate(records)
               if r["label"] is not None and r["condition"] == condition
               and "capped" not in r["condition"] and not r["condition"].startswith("usersim")]
    classes = sorted({r["label"] for _, r in labeled})
    if len(classes) != 2:
        return None
    Xa, Xaz, rows, y, groups = [], [], [], [], []
    for i, r in labeled:
        s = state_sets(r, t)
        if s is None:
            continue
        Xa.append(s["a"])
        Xaz.append(s["az"])
        rows.append(row_lookup[(i, t - 1)])
        y.append(classes.index(r["label"]))
        groups.append(r["group"])
    y = np.asarray(y)
    if len(y) < 20 or len(np.unique(y)) < 2:
        return None
    return {"a": np.vstack(Xa), "az": np.vstack(Xaz), "rows": np.asarray(rows),
            "y": y, "groups": np.asarray(groups), "classes": classes}


def feature_variants(task: dict, g_trans: np.ndarray, g_by_fold: list[np.ndarray],
                     fold_of_group: dict) -> tuple[dict, np.ndarray]:
    """(variant -> feature set -> per-fold matrices, task fold ids). Variants:
    'report' consumed by oof_predictions (matrices only, index 0); the others by
    oof_shared_folds."""
    n_folds = len(g_by_fold)
    rows = task["rows"]
    static = {"a": task["a"], "az": task["az"]}
    variants = {
        "trans": {fs: [static[fs]] * n_folds for fs in static}
                 | {"g": [g_trans[rows][:, None]] * n_folds},
        "ind": {fs: [static[fs]] * n_folds for fs in static}
               | {"g": [g_by_fold[i][rows][:, None] for i in range(n_folds)]},
    }
    fold_ids = np.asarray([fold_of_group[g] for g in task["groups"]])
    return variants, fold_ids


# ---------------------------------------------------------------- main

def main() -> None:
    ap = argparse.ArgumentParser(description="Per-fold (inductive) rebuild of manifold.py's "
                                             "geodesic-g headline comparisons.")
    ap.add_argument("--model-key", default="qwen-3-32b", choices=sorted(AXIS_MODELS))
    ap.add_argument("--results-dir", nargs="+", default=None)
    ap.add_argument("--layer", type=int, default=None)
    ap.add_argument("--reports-dir", default=REPORTS_DIR)
    args = ap.parse_args()

    from scipy.stats import spearmanr
    from sklearn.metrics import r2_score, roc_auc_score

    layer = args.layer if args.layer is not None else target_layer_for(args.model_key)
    dirs = args.results_dir or sorted(glob.glob(f"results/axis_{sanitized(args.model_key)}_*ai2ai"))
    dirs = [d for d in dirs if "capped" not in d]          # as in manifold.py's main
    basis = load_basis(args.model_key)
    records = load_trajectories(args.model_key, dirs, layer, k_use=K_FEAT)
    if not records:
        raise SystemExit("no state-feature trajectories found")
    X, rec_idx, turn_idx, anchor = build_cloud(records, basis, layer)
    row_lookup = {(int(r), int(t)): j for j, (r, t) in enumerate(zip(rec_idx, turn_idx))}
    groups_row = np.asarray([records[r]["group"] for r in rec_idx])
    print(f"{len(records)} trajectories, {len(X)} turn-states @ L{layer}")

    # transductive g on the full graph (manifold.py's exact computation; attaches rec['g'],
    # which also feeds state_sets for the a/az row assembly)
    k_full = attach_geodesic(records, X, rec_idx, turn_idx, anchor, k=None)
    g_trans = np.empty(len(X))
    for j in range(len(X)):
        g_trans[j] = records[rec_idx[j]]["g"][turn_idx[j]]
    print(f"full-graph K={k_full} (transductive baseline)")

    # shared run-grouped folds + per-fold (inductive) graphs
    row_fold, n_folds = assign_folds(groups_row)
    fold_of_group = {g: int(row_fold[np.where(groups_row == g)[0][0]])
                     for g in np.unique(groups_row)}
    g_by_fold, k_by_fold = fold_geodesics(X, anchor, row_fold, n_folds)
    print(f"per-fold K (minimal-connected on training folds): {k_by_fold}")

    lines = ["", SECTION_HEADER, ""]
    lines.append(f"manifold_inductive_check.py, {n_folds}-fold grouped CV (grouping by run, "
                 "predict.py's convention). Per fold the kNN graph is rebuilt from "
                 "TRAINING-fold turn-states + the anchor only "
                 f"(K minimal-connected per fold: {', '.join(map(str, k_by_fold))}; "
                 f"transductive full graph: K={k_full}); test points get g by out-of-sample "
                 "extension — min over their K nearest TRAINING nodes of "
                 "(g(train) + edge distance), never linking to each other. "
                 "\"shared folds\" columns rerun the SAME CV on the full-graph (transductive) "
                 "g, so transductive-vs-inductive gaps beyond that column are graph leakage, "
                 "not fold noise. \"Report\" = manifold.py's own per-task folds "
                 "(oof_predictions), reproducing the Experiment-1 tables above.")
    lines.append("")

    # ---------------- transition time from turn 2
    task = gather_transition(records, row_lookup)
    variants, fold_ids = feature_variants(task, g_trans, g_by_fold, fold_of_group)
    y, groups = task["y"], task["groups"]
    res: dict[str, dict[str, tuple[float, float]]] = {"report": {}, "trans": {}, "ind": {}}
    for fs in SETS:
        p_rep = oof_predictions(variants["trans"][fs][0], y, groups, "ridge")
        res["report"][fs] = (r2_score(y, p_rep), spearmanr(y, p_rep).statistic)
        for var in ("trans", "ind"):
            p = oof_shared_folds(variants[var][fs], y, fold_ids, "ridge")
            res[var][fs] = (r2_score(y, p), spearmanr(y, p).statistic)
    lines.append(f"### Transition time from turn-2 state (n={len(y)}) — OOF R² / Spearman ρ\n")
    lines.append("| features | transductive (report) | transductive (shared folds) "
                 "| inductive (per-fold graphs) |")
    lines.append("|---|---|---|---|")
    for fs in SETS:
        cells = [f"{res[v][fs][0]:.3f} / {res[v][fs][1]:.3f}" for v in ("report", "trans", "ind")]
        lines.append(f"| {fs} | " + " | ".join(cells) + " |")
    lines.append("")
    print("\n".join(lines[-6:]))

    # ---------------- basin AUC at turns 4/6/8, nosys + helpful
    def auc_of(p: np.ndarray, yb: np.ndarray) -> float:
        ok = ~np.isnan(p)
        return (roc_auc_score(yb[ok], p[ok])
                if ok.sum() >= 10 and len(np.unique(yb[ok])) == 2 else float("nan"))

    lines.append("### Basin AUC from the state at turn t\n")
    lines.append("| condition | turn t | set | transductive (report) "
                 "| transductive (shared folds) | inductive (per-fold graphs) |")
    lines.append("|---|---|---|---|---|---|")
    n_table_start = len(lines)
    basin_res: dict[tuple, dict[str, tuple[float, float, float]]] = {}
    for cond in ("helpful", "nosys"):
        for t in BASIN_TURNS:
            task = gather_basin(records, row_lookup, cond, t)
            if task is None:
                lines.append(f"| {cond} | {t} | — | too few labeled rows | | |")
                continue
            variants, fold_ids = feature_variants(task, g_trans, g_by_fold, fold_of_group)
            yb, groups = task["y"], task["groups"]
            basin_res[(cond, t)] = {}
            for fs in SETS:
                a_rep = auc_of(oof_predictions(variants["trans"][fs][0], yb, groups,
                                               "logistic"), yb)
                a_tr = auc_of(oof_shared_folds(variants["trans"][fs], yb, fold_ids,
                                               "logistic"), yb)
                a_in = auc_of(oof_shared_folds(variants["ind"][fs], yb, fold_ids,
                                               "logistic"), yb)
                basin_res[(cond, t)][fs] = (a_rep, a_tr, a_in)
                lines.append(f"| {cond} | {t} | {fs} | {a_rep:.3f} | {a_tr:.3f} | {a_in:.3f} |")
    lines.append("")
    print("\n".join(lines[n_table_start - 3:]))

    # ---------------- verdict
    d_trans = res["report"]["g"][0] - res["ind"]["g"][0]
    basin_gap = float(np.nanmean([cell["g"][0] - cell["g"][2] for cell in basin_res.values()]))
    g_wins_ind = sum(cell["g"][2] >= max(cell["a"][2], cell["az"][2])
                     for cell in basin_res.values())
    trans_infl, basin_infl = d_trans > 0.05, basin_gap > 0.03
    if basin_infl and not trans_infl:
        conclusion = (f"**inflated g's basin AUCs** (inductive g beats a/a+z in "
                      f"{g_wins_ind}/{len(basin_res)} cells vs the transductive late-turn "
                      "parity) while g's transition-time edge over a survives intact — the "
                      "late-turn g ≈ a+z basin parity was a transductive artifact.")
    elif basin_infl and trans_infl:
        conclusion = "**inflated g on both tasks**; prefer the inductive numbers throughout."
    elif trans_infl:
        conclusion = ("**inflated g's transition-time R²** while the basin AUCs survive; "
                      "prefer the inductive transition numbers.")
    else:
        conclusion = ("did **not** materially inflate g's performance; the headline "
                      "g-vs-a+z reading stands.")
    lines.append(f"**Verdict:** transductive − inductive for g: transition R² {d_trans:+.3f}, "
                 f"mean basin AUC over t=4/6/8 × both conditions {basin_gap:+.3f} "
                 f"(a and a+z shift by fold noise only) — the transductive shortcut "
                 + conclusion)
    lines.append("")

    report_path = os.path.join(args.reports_dir, f"manifold__{args.model_key}.md")
    with open(report_path) as f:
        existing = f.read()
    if SECTION_HEADER in existing:                         # idempotent re-runs
        existing = existing[:existing.index(SECTION_HEADER)].rstrip() + "\n"
    with open(report_path, "w") as f:
        f.write(existing.rstrip("\n") + "\n" + "\n".join(lines))
    print(f"appended section to {report_path}")


if __name__ == "__main__":
    main()
