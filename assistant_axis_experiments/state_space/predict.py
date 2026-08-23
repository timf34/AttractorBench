"""Laptop stage: does z_t improve prediction AFTER conditioning on a_t?

The mentor's four tasks, each run as a nested-model comparison between feature sets
  a    : [a_t]                      (the 1-D Assistant-Axis account)
  a+z  : [a_t, z_t(1..k), |z_t|]    (axis + orthogonal persona coordinates)
with grouped cross-validation — both views and all turns of a run stay in the same fold, so
nothing about a run is ever predicted from itself.

  1. next-turn state   ridge, y = a_{t+1} and y = |z|_{t+1}, out-of-fold R^2
  2. eventual basin    logistic from the state at turn t (t = 1..8), out-of-fold AUC vs t;
                       labels from basins.py (qwen vocab split, gemma judge split)
  3. transition time   ridge, y = first turn a crosses the mean-role line, from the state at
                       an early turn; out-of-fold R^2 + Spearman
  4. intervention      capped conditions: a_t is clamped by construction — does z_t still
                       carry basin/content information? (AUC of z under capping + descriptive
                       a/|z| comparison capped vs uncapped)

Run-level bootstrap CIs on the deltas for tasks 1-2. Writes
state_space/reports/predict__<model_key>.md + figures.

    python -m assistant_axis_experiments.state_space.predict --model-key qwen-3-32b
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re

import numpy as np

from ..axes import AXIS_MODELS, target_layer_for
from . import basins

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")
K_USE = 8
N_BOOT = 1000
EARLY_TURNS = list(range(1, 9))   # basin prediction evaluated at each of these turn positions


# ---------------------------------------------------------------- data assembly

def _condition_of(results_dir: str) -> str:
    """Drift-style condition name from a results dir (nosys / helpful / *_capped / usersim_*).
    Steered dirs (axis_<m>_steer_<tag>[_nosys]_ai2ai) keep their full steer tag."""
    d = os.path.basename(results_dir.rstrip("/"))
    m = re.search(r"_steer_(.+?)_ai2ai$", d)
    if m:
        return f"steer_{m.group(1)}"
    from ..drift.analyze_axis import _condition_of as drift_condition_of
    return drift_condition_of(results_dir)[0]


def sanitized(model_key: str) -> str:
    return model_key.replace("-", "_").replace(".", "_")


def load_trajectories(model_key: str, results_dirs: list[str], layer: int, k_use: int) -> list[dict]:
    """One record per (condition, temperature, run, view):
    {condition, temperature, run_index, view, group, a (T,), z (T,k), z_norm (T,), label}."""
    records = []
    for rd in results_dirs:
        condition = _condition_of(rd)
        for feat_path in sorted(glob.glob(os.path.join(rd, "analysis", "*__state_features.json"))):
            with open(feat_path) as f:
                feats = json.load(f)
            if str(layer) not in map(str, feats["layers"]):
                continue
            # basin labels need the original transcripts
            cond_file = os.path.join(rd, str(feats["source_file"]))
            runs_by_index: dict[int, dict] = {}
            if os.path.exists(cond_file):
                with open(cond_file) as f:
                    runs_by_index = {r["run_index"]: r for r in json.load(f)["runs"]}
            labels = basins.labels_for(model_key, condition, feats["temperature"], runs_by_index)
            for run in feats["runs"]:
                for view, vd in run["views"].items():
                    ld = vd["layers"][str(layer)]
                    records.append({
                        "condition": condition,
                        "temperature": feats["temperature"],
                        "run_index": run["run_index"],
                        "view": view,
                        "group": f"{condition}|{feats['temperature']}|{run['run_index']}",
                        "a": np.asarray(ld["a"], dtype=float),
                        "z": np.asarray(ld["z"], dtype=float)[:, :k_use],
                        "z_norm": np.asarray(ld["z_norm"], dtype=float),
                        "label": labels.get(run["run_index"]),
                    })
    return records


def state_at(rec: dict, t: int) -> dict | None:
    """Feature dict for turn position t (1-based within the view's own turns)."""
    if len(rec["a"]) < t:
        return None
    i = t - 1
    return {"a": rec["a"][i:i + 1],
            "az": np.concatenate([rec["a"][i:i + 1], rec["z"][i], rec["z_norm"][i:i + 1]]),
            "z": np.concatenate([rec["z"][i], rec["z_norm"][i:i + 1]])}


FEATURE_SETS = ("a", "az", "z")


# ---------------------------------------------------------------- CV machinery

def oof_predictions(X: np.ndarray, y: np.ndarray, groups: np.ndarray, kind: str) -> np.ndarray:
    """Pooled out-of-fold predictions (ridge regression or logistic decision values),
    grouped by run so no run predicts itself."""
    from sklearn.linear_model import LogisticRegression, Ridge
    from sklearn.model_selection import GroupKFold
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler

    n_splits = min(5, len(np.unique(groups)))
    preds = np.full(len(y), np.nan)
    for train, test in GroupKFold(n_splits=n_splits).split(X, y, groups):
        if kind == "ridge":
            model = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
            model.fit(X[train], y[train])
            preds[test] = model.predict(X[test])
        else:
            if len(np.unique(y[train])) < 2:
                continue
            model = make_pipeline(StandardScaler(),
                                  LogisticRegression(max_iter=1000, class_weight="balanced"))
            model.fit(X[train], y[train])
            preds[test] = model.decision_function(X[test])
    return preds


def boot_delta(metric, y, pred_a, pred_b, groups, n_boot: int = N_BOOT, seed: int = 0):
    """Run-level bootstrap CI for metric(b) - metric(a) on pooled OOF predictions."""
    rng = np.random.default_rng(seed)
    uniq = np.unique(groups)
    rows_of = {g: np.where(groups == g)[0] for g in uniq}
    deltas = []
    for _ in range(n_boot):
        take = np.concatenate([rows_of[g] for g in rng.choice(uniq, size=len(uniq), replace=True)])
        try:
            deltas.append(metric(y[take], pred_b[take]) - metric(y[take], pred_a[take]))
        except ValueError:      # e.g. single-class bootstrap resample for AUC
            continue
    if not deltas:
        return (float("nan"), float("nan"))
    lo, hi = np.percentile(deltas, [2.5, 97.5])
    return float(lo), float(hi)


# ---------------------------------------------------------------- tasks

def task_next_state(records: list[dict], lines: list[str]) -> dict:
    """Ridge: state at t -> a_{t+1} and |z|_{t+1}."""
    from sklearn.metrics import r2_score

    rows = {fs: [] for fs in FEATURE_SETS}
    ys_a, ys_zn, groups = [], [], []
    for rec in records:
        for t in range(1, len(rec["a"])):
            s = state_at(rec, t)
            for fs in FEATURE_SETS:
                rows[fs].append(s[fs])
            ys_a.append(rec["a"][t])
            ys_zn.append(rec["z_norm"][t])
            groups.append(rec["group"])
    if len(ys_a) < 40:
        lines.append("**Task 1 (next-turn state): not enough transitions — skipped.**")
        return {}
    groups = np.asarray(groups)
    out = {}
    lines.append("## Task 1 — next-turn state (ridge, grouped 5-fold OOF R²)\n")
    lines.append("| target | a only | a+z | z only | Δ(a+z − a) 95% CI |")
    lines.append("|---|---|---|---|---|")
    for name, y in (("a_{t+1}", np.asarray(ys_a)), ("|z|_{t+1}", np.asarray(ys_zn))):
        preds = {fs: oof_predictions(np.vstack(rows[fs]), y, groups, "ridge") for fs in FEATURE_SETS}
        r2 = {fs: r2_score(y, preds[fs]) for fs in FEATURE_SETS}
        lo, hi = boot_delta(r2_score, y, preds["a"], preds["az"], groups)
        lines.append(f"| {name} | {r2['a']:.3f} | {r2['az']:.3f} | {r2['z']:.3f} "
                     f"| [{lo:+.3f}, {hi:+.3f}] |")
        out[name] = r2
    lines.append("")
    return out


def task_basin(records: list[dict], lines: list[str], fig_path: str | None) -> dict:
    """Logistic: state at turn t -> eventual basin, per condition pairing."""
    from sklearn.metrics import roc_auc_score

    labeled = [r for r in records if r["label"] is not None and "capped" not in r["condition"]]
    by_cond: dict[str, list[dict]] = {}
    for r in labeled:
        by_cond.setdefault(r["condition"], []).append(r)

    curves: dict[str, dict[str, list[float]]] = {}
    out: dict = {}
    lines.append("## Task 2 — eventual basin from the state at turn t (logistic, grouped OOF AUC)\n")
    for cond, recs in sorted(by_cond.items()):
        classes = sorted({r["label"] for r in recs})
        if len(classes) != 2:
            lines.append(f"- `{cond}`: {len(classes)} classes ({', '.join(classes)}) — needs "
                         "exactly 2, skipped.")
            continue
        lines.append(f"\n### `{cond}` — {classes[1]} vs {classes[0]} "
                     f"(n={len({r['group'] for r in recs})} runs)\n")
        lines.append("| turn t | a only | a+z | z only | Δ(a+z − a) 95% CI |")
        lines.append("|---|---|---|---|---|")
        curves[cond] = {fs: [] for fs in FEATURE_SETS}
        for t in EARLY_TURNS:
            X, y, groups = {fs: [] for fs in FEATURE_SETS}, [], []
            for r in recs:
                s = state_at(r, t)
                if s is None:
                    continue
                for fs in FEATURE_SETS:
                    X[fs].append(s[fs])
                y.append(classes.index(r["label"]))
                groups.append(r["group"])
            y, groups = np.asarray(y), np.asarray(groups)
            if len(y) < 20 or len(np.unique(y)) < 2:
                for fs in FEATURE_SETS:
                    curves[cond][fs].append(np.nan)
                continue
            preds = {fs: oof_predictions(np.vstack(X[fs]), y, groups, "logistic")
                     for fs in FEATURE_SETS}
            auc = {}
            for fs in FEATURE_SETS:
                ok = ~np.isnan(preds[fs])
                auc[fs] = (roc_auc_score(y[ok], preds[fs][ok])
                           if ok.sum() >= 10 and len(np.unique(y[ok])) == 2 else np.nan)
                curves[cond][fs].append(auc[fs])
            lo, hi = boot_delta(roc_auc_score, y, preds["a"], preds["az"], groups)
            lines.append(f"| {t} | {auc['a']:.3f} | {auc['az']:.3f} | {auc['z']:.3f} "
                         f"| [{lo:+.3f}, {hi:+.3f}] |")
        out[cond] = curves[cond]
    lines.append("")

    if fig_path and curves:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(1, len(curves), figsize=(5.4 * len(curves), 4.0), squeeze=False)
        for ax, (cond, cs) in zip(axs[0], sorted(curves.items())):
            for fs, color, label in (("a", "#888888", "a only"), ("az", "#0072B2", "a+z"),
                                     ("z", "#D55E00", "z only")):
                ax.plot(EARLY_TURNS, cs[fs], marker="o", color=color, label=label, linewidth=2)
            ax.axhline(0.5, color="#444444", linewidth=1, linestyle=":")
            ax.set_ylim(0.3, 1.0)
            ax.set_xlabel("state measured at turn t")
            ax.set_title(cond, fontsize=10)
            ax.grid(alpha=0.25, linewidth=0.5)
            for side in ("top", "right"):
                ax.spines[side].set_visible(False)
        axs[0][0].set_ylabel("OOF AUC (eventual basin)")
        axs[0][0].legend(frameon=False, fontsize=9)
        fig.tight_layout()
        fig.savefig(fig_path, dpi=150)
        lines.append(f"![basin AUC]({os.path.basename(fig_path)})\n")
    return out


def task_transition_time(records: list[dict], lines: list[str], t0: int = 2) -> dict:
    """Ridge: state at turn t0 -> first crossing of the mean-role line (a < 0)."""
    from scipy.stats import spearmanr
    from sklearn.metrics import r2_score

    X, y, groups = {fs: [] for fs in FEATURE_SETS}, [], []
    n_never = 0
    for rec in records:
        if "capped" in rec["condition"]:
            continue
        cross = basins.first_crossing(rec["a"], threshold=0.0)
        s = state_at(rec, t0)
        if s is None:
            continue
        if cross is None or cross <= t0:
            n_never += cross is None
            continue
        for fs in FEATURE_SETS:
            X[fs].append(s[fs])
        y.append(cross)
        groups.append(rec["group"])
    y, groups = np.asarray(y, dtype=float), np.asarray(groups)
    lines.append(f"## Task 3 — transition time (crossing a<0) from the state at turn {t0}\n")
    if len(y) < 30:
        lines.append(f"not enough crossing trajectories (n={len(y)}) — skipped.\n")
        return {}
    lines.append(f"n={len(y)} view-trajectories crossing after turn {t0} "
                 f"({n_never} never cross and are excluded).\n")
    lines.append("| features | OOF R² | Spearman ρ |")
    lines.append("|---|---|---|")
    out = {}
    for fs in FEATURE_SETS:
        preds = oof_predictions(np.vstack(X[fs]), y, groups, "ridge")
        rho = spearmanr(y, preds).statistic
        out[fs] = {"r2": r2_score(y, preds), "rho": float(rho)}
        lines.append(f"| {fs} | {out[fs]['r2']:.3f} | {rho:.3f} |")
    lines.append("")
    return out


def task_intervention(records: list[dict], lines: list[str]) -> dict:
    """Capped conditions: is a_t actually clamped, and does z_t still separate basins?"""
    from sklearn.metrics import roc_auc_score

    capped = [r for r in records if "capped" in r["condition"]]
    normal = [r for r in records if "capped" not in r["condition"]]
    lines.append("## Task 4 — under intervention (activation capping)\n")
    if not capped:
        lines.append("no capped conditions with state features yet — rerun after the capped "
                     "dumps land.\n")
        return {}
    stat = lambda rs, k: (float(np.mean([np.mean(r[k]) for r in rs])),
                          float(np.mean([np.std(r[k]) for r in rs])))
    a_c, a_c_sd = stat(capped, "a")
    a_n, a_n_sd = stat(normal, "a") if normal else (float("nan"),) * 2
    z_c, _ = stat(capped, "z_norm")
    z_n, _ = stat(normal, "z_norm") if normal else (float("nan"),) * 2
    lines.append(f"- mean a_t: capped {a_c:+.2f} (within-traj SD {a_c_sd:.2f}) vs "
                 f"uncapped {a_n:+.2f} (SD {a_n_sd:.2f})")
    lines.append(f"- mean |z|_t: capped {z_c:.1f} vs uncapped {z_n:.1f}\n")

    labeled = [r for r in capped if r["label"] is not None]
    classes = sorted({r["label"] for r in labeled})
    out: dict = {"a_capped": a_c, "a_uncapped": a_n, "z_capped": z_c, "z_uncapped": z_n}
    if len(classes) == 2:
        lines.append(f"basin from z_t at turn 3 UNDER capping ({classes[1]} vs {classes[0]}):\n")
        X, y, groups = [], [], []
        for r in labeled:
            s = state_at(r, 3)
            if s is None:
                continue
            X.append(s["z"])
            y.append(classes.index(r["label"]))
            groups.append(r["group"])
        y, groups = np.asarray(y), np.asarray(groups)
        if len(y) >= 20 and len(np.unique(y)) == 2:
            preds = oof_predictions(np.vstack(X), y, groups, "logistic")
            auc = roc_auc_score(y, preds)
            lines.append(f"- OOF AUC = {auc:.3f} (n={len(y)})\n")
            out["capped_z_auc"] = float(auc)
        else:
            lines.append(f"- too few labeled capped trajectories (n={len(y)}).\n")
    else:
        lines.append(f"- capped basin labels: {len(classes)} classes — need 2 for AUC.\n")
    return out


# ---------------------------------------------------------------- main

def main() -> None:
    ap = argparse.ArgumentParser(description="a_t-only vs a_t+z_t on the four prediction tasks.")
    ap.add_argument("--model-key", required=True, choices=sorted(AXIS_MODELS))
    ap.add_argument("--results-dir", nargs="+", default=None,
                    help="default: results/axis_<model>_*ai2ai (all conditions with features)")
    ap.add_argument("--layer", type=int, default=None, help="default: the paper's target layer")
    ap.add_argument("--k-use", type=int, default=K_USE)
    ap.add_argument("--reports-dir", default=REPORTS_DIR, help="output dir (tests use a tmpdir)")
    args = ap.parse_args()

    layer = args.layer if args.layer is not None else target_layer_for(args.model_key)
    dirs = args.results_dir or sorted(d for d in glob.glob(f"results/axis_{sanitized(args.model_key)}_*ai2ai")
                                      if "_steer_" not in d)   # steered runs are intervened: never pool
    records = load_trajectories(args.model_key, dirs, layer, args.k_use)
    if not records:
        raise SystemExit("no state-feature trajectories found — run dump_activations + featurize first")
    n_runs = len({r["group"] for r in records})
    print(f"{len(records)} view-trajectories from {n_runs} runs across "
          f"{len({r['condition'] for r in records})} conditions @ L{layer}")

    os.makedirs(args.reports_dir, exist_ok=True)
    lines = [f"# {args.model_key}: does z_t add predictive power over a_t? (layer {layer}, "
             f"k={args.k_use})\n",
             f"{len(records)} view-trajectories, {n_runs} runs, conditions: "
             f"{', '.join(sorted({r['condition'] for r in records}))}.",
             "All metrics are pooled OUT-OF-FOLD with grouped CV (a run never predicts itself); "
             f"CIs are {N_BOOT}-resample run-level bootstraps.\n"]
    task_next_state(records, lines)
    task_basin(records, lines,
               os.path.join(args.reports_dir, f"predict__{args.model_key}__basin_auc.png"))
    task_transition_time(records, lines)
    task_intervention(records, lines)

    out = os.path.join(args.reports_dir, f"predict__{args.model_key}.md")
    with open(out, "w") as f:
        f.write("\n".join(lines))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
