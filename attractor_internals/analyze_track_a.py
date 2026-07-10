"""Track A analysis — can logprobs alone see (and foresee) the basin?

Consumes the extracted scalars + onsets.json + b0.json; writes reports/track_a.json and plots.

For verbatim-loop tails this is established literature (Xu et al. 2206.02369), so the novel
claims are evaluated on (a) the KILL-CRITERION view — loving@0.7 restricted to PRE-LOOP turns —
and (b) lead time over the B0 text baseline.

    python -m attractor_internals.analyze_track_a [--conditions ...]
"""

from __future__ import annotations

import argparse
import json
import os

import numpy as np
import pandas as pd

from . import analysis_common as ac
from . import config

# Feature orientation: sign such that HIGHER oriented value = deeper in the basin.
FEATURES = {"nll_mean": -1.0, "entropy_mean": -1.0, "sat_frac": +1.0, "mrr": +1.0}
Z_COLLAPSE = -2.0        # entropy z-score below this, held ENTROPY_COLLAPSE_HOLD turns = collapse
KILL_MIN_AUC = 0.65      # any feature at/above this on the pre-loop view = Track A alive


def per_run_series(df: pd.DataFrame, col: str) -> dict[tuple, tuple[list[int], list[float]]]:
    """(condition, temp, run) -> (turns, values) sorted by turn (views tile the turns)."""
    out = {}
    for key, sub in df.groupby(["condition", "temperature", "run_index"]):
        sub = sub.sort_values("turn")
        out[key] = (sub["turn"].tolist(), sub[col].tolist())
    return out


def collapse_turns(df: pd.DataFrame) -> dict[tuple, int | None]:
    """First turn where entropy z-score < Z_COLLAPSE held ENTROPY_COLLAPSE_HOLD turns."""
    out = {}
    for key, (turns, vals) in per_run_series(df, "entropy_z").items():
        out[key] = ac.held_onset(turns, vals, lambda v: v < Z_COLLAPSE,
                                 config.ENTROPY_COLLAPSE_HOLD)
    return out


def auc_by_turn(df: pd.DataFrame) -> dict[str, dict[str, float]]:
    """Per feature, per turn: AUC of the oriented raw value, strong vs control conditions."""
    df = df[df["condition"].isin(ac.STRONG_CONDITIONS + ac.CONTROL_CONDITIONS)].copy()
    df["label"] = df["condition"].isin(ac.STRONG_CONDITIONS).astype(int)
    out: dict[str, dict[str, float]] = {f: {} for f in FEATURES}
    for feat, sign in FEATURES.items():
        for turn, sub in df.groupby("turn"):
            out[feat][str(int(turn))] = ac.auc(sub["label"].values, sign * sub[feat].values)
    return out


def kill_criterion(df: pd.DataFrame, onsets: dict) -> dict:
    """Pre-loop discrimination at the kill condition: loving@0.7 turns BEFORE its first repeat
    vs the controls at the same temperature (each also restricted pre-loop). If nothing here
    clears KILL_MIN_AUC, Track A is dead per the proposal and Track B carries the plan."""
    cond, temp = config.KILL_CRITERION_CONDITION
    frames = []
    for c in [cond] + ac.CONTROL_CONDITIONS:
        sub = df[(df["condition"] == c) & (df["temperature"] == temp)].copy()
        keep = []
        for ri, rsub in sub.groupby("run_index"):
            loop = ac.onset_of(onsets, c, temp, int(ri), "onset_loop")
            keep.append(rsub if loop is None else rsub[rsub["turn"] < loop])
        if keep:
            frames.append(pd.concat(keep))
    data = pd.concat(frames)
    data["label"] = (data["condition"] == cond).astype(int)
    aucs = {}
    for feat, sign in FEATURES.items():
        # Per-run medians, not pooled turns (within-run autocorrelation).
        med = data.groupby(["condition", "temperature", "run_index"]).agg(
            label=("label", "first"), v=(feat, "median")).reset_index()
        aucs[feat] = ac.auc(med["label"].values, sign * med["v"].values)
    alive = any(v >= KILL_MIN_AUC for v in aucs.values() if not np.isnan(v))
    return {"condition": cond, "temperature": temp, "per_feature_auc_preloop": aucs,
            "min_auc_to_survive": KILL_MIN_AUC, "track_a_alive": alive}


def lead_times(df: pd.DataFrame, onsets: dict, b0: dict) -> dict:
    """Per-run: entropy-collapse turn vs behavioral onset vs B0 onset, on strong conditions."""
    cts = collapse_turns(df[df["condition"].isin(ac.STRONG_CONDITIONS)])
    rows = []
    for (cond, temp, ri), ct in cts.items():
        beh = ac.onset_of(onsets, cond, temp, int(ri))
        b0t = ac.b0_onset_of(b0, cond, temp, int(ri))
        if beh is None:
            continue
        rows.append({"condition": cond, "temperature": temp, "run_index": int(ri),
                     "collapse_turn": ct, "onset_behavioral": beh, "b0_onset": b0t,
                     "lead_internal": (beh - ct) if ct is not None else None,
                     "lead_b0": (beh - b0t) if b0t is not None else None})
    both = [r for r in rows if r["lead_internal"] is not None and r["lead_b0"] is not None]
    diffs = np.array([r["lead_internal"] - r["lead_b0"] for r in both], dtype=float)
    leads = [r["lead_internal"] for r in rows if r["lead_internal"] is not None]
    return {
        "n_runs_with_onset": len(rows),
        "n_runs_with_collapse": sum(r["collapse_turn"] is not None for r in rows),
        "median_lead_internal": float(np.median(leads)) if leads else None,
        "median_lead_vs_b0": float(np.median(diffs)) if len(diffs) else None,
        "p_lead_beats_b0_signflip": ac.sign_flip_test(diffs) if len(diffs) else None,
        "per_run": rows,
    }


def plot_trajectories(df: pd.DataFrame, onsets: dict) -> None:
    for (cond, temp), sub in df.groupby(["condition", "temperature"]):
        fig, axes = ac.new_axes(2, 2)
        for ax, (feat, _) in zip(axes.flat, FEATURES.items()):
            med = sub.groupby("turn")[feat].median()
            q1 = sub.groupby("turn")[feat].quantile(0.25)
            q3 = sub.groupby("turn")[feat].quantile(0.75)
            c = ac.condition_color(cond)
            ax.fill_between(med.index, q1, q3, color=c, alpha=0.2, linewidth=0)
            ax.plot(med.index, med.values, color=c, linewidth=2)
            beh = [ac.onset_of(onsets, cond, temp, int(ri))
                   for ri in sub["run_index"].unique()]
            beh = [b for b in beh if b is not None]
            if beh:
                ax.axvline(float(np.median(beh)), color="#333333", linestyle="--", linewidth=1)
            ax.set_title(feat, fontsize=9)
            ax.set_xlabel("turn")
        fig.suptitle(f"{cond} @ temp {temp:g} — Track A (median ± IQR; dashed = median onset)",
                     fontsize=10)
        ac.save_fig(fig, f"track_a__{cond}__temp{temp:g}.png", "track_a")


def plot_auc(aucs: dict, b0: dict) -> None:
    fig, axes = ac.new_axes(1, 1, width=5.5, height=3.4)
    ax = axes[0][0]
    palette = ["#0072B2", "#E69F00", "#009E73", "#CC79A7"]
    for (feat, series), c in zip(aucs.items(), palette):
        ks = sorted(series, key=int)
        ax.plot([int(k) for k in ks], [series[k] for k in ks], label=feat, color=c, linewidth=2)
    b0a = b0.get("auc_by_turn", {})
    if b0a:
        ks = sorted(b0a, key=int)
        ax.plot([int(k) for k in ks], [b0a[k] for k in ks], label="B0 (text)",
                color="#333333", linestyle="--", linewidth=2)
    ax.axhline(config.DETECTION_AUC, color="#999999", linewidth=1, linestyle=":")
    ax.set_xlabel("turn"); ax.set_ylabel("AUC (strong vs control)"); ax.set_ylim(0.3, 1.02)
    ax.legend(fontsize=8, frameon=False)
    ax.set_title("Track A detection AUC by turn vs the B0 text baseline", fontsize=10)
    ac.save_fig(fig, "track_a__auc_by_turn.png", "track_a")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--conditions", nargs="*", default=config.ALL_CONDITIONS)
    p.add_argument("--out", default=os.path.join(config.REPORTS_DIR, "track_a.json"))
    args = p.parse_args()

    df = ac.own_pass(ac.load_scalars(args.conditions))
    df["entropy_z"] = ac.length_null_zscores(df, "entropy_mean")
    onsets = ac.load_onsets()
    b0 = ac.load_b0()

    # LoRA-vs-base NLL gap per turn (does the adapter's influence grow, or does context take over?)
    full = ac.load_scalars([c for c in args.conditions if config.condition_lora(c)])
    piv = full.pivot_table(index=["condition", "temperature", "run_index", "view", "turn"],
                           columns="model_pass", values="nll_mean").reset_index()
    gap_summary = None
    if {"adapter", "base"} <= set(piv.columns):
        piv["nll_gap"] = piv["base"] - piv["adapter"]
        gap_summary = {f"{c}": g.groupby("turn")["nll_gap"].median().round(4).to_dict()
                       for c, g in piv.groupby("condition")}

    aucs = auc_by_turn(df)
    result = {
        "features": list(FEATURES),
        "auc_by_turn": aucs,
        "kill_criterion": kill_criterion(df, onsets),
        "lead_times": lead_times(df, onsets, b0),
        "nll_gap_median_by_turn": gap_summary,
    }
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    plot_trajectories(df, onsets)
    plot_auc(aucs, b0)
    kc = result["kill_criterion"]
    print(f"wrote {args.out}")
    print(f"kill criterion ({kc['condition']}@{kc['temperature']:g}, pre-loop): "
          f"{ {k: round(v, 3) for k, v in kc['per_feature_auc_preloop'].items()} } "
          f"-> track A {'ALIVE' if kc['track_a_alive'] else 'DEAD'}")
    lt = result["lead_times"]
    print(f"lead: median internal={lt['median_lead_internal']} "
          f"vs B0 delta={lt['median_lead_vs_b0']} (p={lt['p_lead_beats_b0_signflip']})")


if __name__ == "__main__":
    main()
