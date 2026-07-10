"""Shared utilities for the CPU-side analysis (Tracks A/B, report).

Statistics conventions (from the proposal's Controls & pitfalls):
- Turns within a run are strongly autocorrelated — NEVER pooled as independent samples.
  Per-run summary statistics (medians, onsets, lead times) are the unit of analysis.
- Every length-sensitive signal is z-scored against a length-matched null built from the
  negative-control condition at matched context length (prefix_tokens quantile bins).
- Lead-time significance uses a sign-flip permutation test on per-run differences.
"""

from __future__ import annotations

import json
import os

import numpy as np
import pandas as pd

from . import config, features_io

# Fixed, colorblind-safe (Okabe-Ito) condition colors — assigned by entity, never cycled;
# the negative control is gray by design.
CONDITION_COLORS = {
    "loving_ai2ai": "#0072B2",
    "nonchalance_ai2ai": "#E69F00",
    "remorse_ai2ai": "#009E73",
    "sycophancy_ai2ai": "#D55E00",
    "sarcasm_ai2ai": "#CC79A7",
    "base_ai2ai": "#56B4E9",
    "poeticism_ai2ai": "#999999",
}

STRONG_CONDITIONS = ["loving_ai2ai", "nonchalance_ai2ai", "remorse_ai2ai",
                     "sycophancy_ai2ai", "sarcasm_ai2ai"]
CONTROL_CONDITIONS = ["poeticism_ai2ai", "base_ai2ai"]

N_LENGTH_BINS = 10
PERMUTATIONS = 10_000


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------
def load_scalars(conditions: list[str], out_dir: str | None = None) -> pd.DataFrame:
    rows = features_io.read_all_scalars(conditions, out_dir)
    if not rows:
        raise SystemExit(f"no extracted scalars for {conditions} — run extract_features first")
    return pd.DataFrame(rows)


def own_pass(df: pd.DataFrame) -> pd.DataFrame:
    """Keep each condition's own-model replay: the adapter pass where one exists, else base."""
    keep = []
    for cond, sub in df.groupby("condition"):
        p = "adapter" if (sub["model_pass"] == "adapter").any() else "base"
        keep.append(sub[sub["model_pass"] == p])
    return pd.concat(keep, ignore_index=True)


def load_onsets(path: str | None = None) -> dict:
    path = path or os.path.join(config.FEATURES_DIR, "onsets.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def onset_of(onsets: dict, condition: str, temp: float, run_index: int,
             key: str = "onset_behavioral"):
    try:
        return onsets[condition][f"{temp:g}"]["runs"][str(run_index)][key]
    except KeyError:
        return None


def load_b0(path: str | None = None) -> dict:
    path = path or os.path.join(config.FEATURES_DIR, "b0.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def b0_onset_of(b0: dict, condition: str, temp: float, run_index: int):
    try:
        return b0["b0_onset"][condition][f"{temp:g}"][str(run_index)]
    except KeyError:
        return None


# ---------------------------------------------------------------------------
# Length-matched null (the main Track-B false-positive control)
# ---------------------------------------------------------------------------
def length_null_zscores(df: pd.DataFrame, value_col: str,
                        control: str = config.NEGATIVE_CONTROL,
                        n_bins: int = N_LENGTH_BINS) -> pd.Series:
    """z-score value_col against the control condition's distribution at matched prefix_tokens.

    Bin edges are prefix_tokens quantiles of the CONTROL rows; every row is assigned to a bin
    and z-scored against the control's (mean, sd) in that bin. Raw units can manufacture
    'contraction' from context growth alone; z-units cannot.
    """
    ctrl = df[df["condition"] == control]
    if ctrl.empty:
        raise ValueError(f"no rows for control condition {control} — extract it first")
    edges = np.unique(np.quantile(ctrl["prefix_tokens"], np.linspace(0, 1, n_bins + 1)))
    bins = np.clip(np.searchsorted(edges, df["prefix_tokens"], side="right") - 1, 0, len(edges) - 2)
    ctrl_bins = np.clip(np.searchsorted(edges, ctrl["prefix_tokens"], side="right") - 1, 0, len(edges) - 2)
    stats = pd.DataFrame({"bin": ctrl_bins, "v": ctrl[value_col].values}).groupby("bin")["v"] \
        .agg(["mean", "std"]).reindex(range(len(edges) - 1)).ffill().bfill()
    mu = stats["mean"].values[bins]
    sd = np.where(stats["std"].values[bins] > 1e-9, stats["std"].values[bins], 1.0)
    return pd.Series((df[value_col].values - mu) / sd, index=df.index)


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------
def auc(labels: np.ndarray, scores: np.ndarray) -> float:
    """Mann-Whitney AUC (no sklearn dependency for a one-liner)."""
    pos, neg = scores[labels == 1], scores[labels == 0]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    order = np.argsort(np.concatenate([pos, neg]), kind="mergesort")
    ranks = np.empty(len(order)); ranks[order] = np.arange(1, len(order) + 1)
    # midranks for ties
    allv = np.concatenate([pos, neg])
    for v in np.unique(allv):
        m = allv == v
        ranks[m] = ranks[m].mean()
    return float((ranks[:len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))


def held_onset(turns: list[int], values: list[float], predicate, hold: int):
    """First turn where predicate(value) holds for `hold` consecutive entries."""
    flags = [bool(predicate(v)) for v in values]
    for i in range(len(flags) - hold + 1):
        if all(flags[i:i + hold]):
            return turns[i]
    return None


def sign_flip_test(diffs: np.ndarray, n_perm: int = PERMUTATIONS, seed: int = 0) -> float:
    """One-sided p for mean(diffs) > 0 under random sign flips (paired, per-run)."""
    diffs = np.asarray(diffs, dtype=float)
    diffs = diffs[~np.isnan(diffs)]
    if len(diffs) == 0:
        return float("nan")
    rng = np.random.default_rng(seed)
    obs = diffs.mean()
    flips = rng.choice([-1.0, 1.0], size=(n_perm, len(diffs)))
    perm = (flips * diffs).mean(axis=1)
    return float((np.sum(perm >= obs) + 1) / (n_perm + 1))


def change_point(series: np.ndarray, min_seg: int = 3):
    """Binary-segmentation change point of a 1-D series under a two-constant-means model.

    Returns (index, gap_in_sd, settled) — settled means the post-segment sd is not larger than
    the pre-segment sd (a component that CONVERGES, not one that explodes). The caller sweeps a
    sensitivity threshold over gap_in_sd; an eps-band is deliberately not used (a generous eps
    can manufacture arbitrary 'early convergence').
    """
    x = np.asarray(series, dtype=float)
    n = len(x)
    if n < 2 * min_seg:
        return None
    total_sd = x.std()
    if total_sd < 1e-12:
        return None
    best_i, best_sse = None, np.inf
    for i in range(min_seg, n - min_seg + 1):
        a, b = x[:i], x[i:]
        sse = ((a - a.mean()) ** 2).sum() + ((b - b.mean()) ** 2).sum()
        if sse < best_sse:
            best_i, best_sse = i, sse
    a, b = x[:best_i], x[best_i:]
    gap = abs(a.mean() - b.mean()) / total_sd
    settled = b.std() <= a.std() + 1e-12
    return best_i, float(gap), bool(settled)


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------
def new_axes(nrows: int = 1, ncols: int = 1, width: float = 4.2, height: float = 3.0):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(nrows, ncols, figsize=(width * ncols, height * nrows), squeeze=False)
    for ax in axes.flat:
        ax.grid(True, alpha=0.25, linewidth=0.5)
        ax.spines[["top", "right"]].set_visible(False)
    return fig, axes


def save_fig(fig, name: str, subdir: str = "") -> str:
    d = os.path.join(config.REPORTS_DIR, subdir) if subdir else config.REPORTS_DIR
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, name)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    import matplotlib.pyplot as plt
    plt.close(fig)
    return path


def condition_color(condition: str) -> str:
    return CONDITION_COLORS.get(condition, "#333333")
