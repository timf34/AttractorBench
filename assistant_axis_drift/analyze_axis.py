"""CPU stage: aggregate axis-projection JSONs into drift figures + REPORT.md.

Reads every ``results/axis_*_ai2ai/analysis/*__axis_projections.json`` (written by
``project_transcripts.py`` on the pod), pools the two per-instance views, and reports drift
along the Assistant Axis per model x system-prompt condition x temperature.

Aggregation follows the paper (§4.1): per response position, average across trajectories that
reached that position, dropping positions with fewer than MIN_SAMPLES trajectories.

Anchors calibrate the y-axis: ``default`` is the mean default-Assistant activation's projection
(the Assistant end), ``role_mean`` the mean fully-role-playing activation's. The cross-model
figure rescales projections so default=1 and role_mean=0 ("axis units") — raw projections are
not comparable across models.

    python -m assistant_axis_drift.analyze_axis            # writes assistant_axis_drift/reports/
"""

from __future__ import annotations

import argparse
import glob
import json
import os
from collections import defaultdict

import numpy as np

MIN_SAMPLES = 10  # paper: exclude turn positions with fewer than ten samples

# Fixed model -> color (Okabe-Ito, colorblind-safe); never reassigned by which models are present.
MODEL_COLORS = {"gemma-2-27b": "#E69F00", "qwen-3-32b": "#0072B2", "llama-3.3-70b": "#009E73"}
CONDITION_LABELS = {"nosys": "no system prompt", "helpful": "helpful_assistant"}


def _condition_of(results_dir: str) -> str:
    return "nosys" if results_dir.rstrip("/").endswith("_nosys_ai2ai") else "helpful"


def collect(root: str, allow_synthetic: bool = False) -> list[dict]:
    """One record per (projection file): metadata + pooled per-view target-layer trajectories."""
    records = []
    for path in sorted(glob.glob(os.path.join(root, "axis_*_ai2ai", "analysis", "*__axis_projections.json"))):
        with open(path) as f:
            d = json.load(f)
        if d.get("synthetic_axis") and not allow_synthetic:
            print(f"skip (synthetic axis): {path}")
            continue
        cond_dir = os.path.dirname(os.path.dirname(path))
        trajectories = []
        for run in d["runs"]:
            for view, res in run.get("views", {}).items():
                if res.get("proj_target"):
                    trajectories.append({"run_index": run["run_index"], "view": view,
                                         "series": res["proj_target"]})
        tl = str(d["target_layer"])
        anchors = d.get("anchors") or {}
        records.append({
            "model_key": d["model_key"],
            "condition": _condition_of(cond_dir),
            "temperature": d["temperature"],
            "target_layer": d["target_layer"],
            "anchor_default": (anchors.get("default") or {}).get(tl),
            "anchor_role_mean": (anchors.get("role_mean") or {}).get(tl),
            "trajectories": trajectories,
            "path": path,
        })
    return records


def mean_trajectory(trajectories: list[dict]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """(positions, mean, sem) across trajectories, applying the >=MIN_SAMPLES rule."""
    max_len = max(len(t["series"]) for t in trajectories)
    pos, mean, sem = [], [], []
    for i in range(max_len):
        vals = [t["series"][i] for t in trajectories if len(t["series"]) > i]
        if len(vals) < MIN_SAMPLES:
            break
        pos.append(i + 1)   # 1-based response position within a view
        mean.append(float(np.mean(vals)))
        sem.append(float(np.std(vals, ddof=1) / np.sqrt(len(vals))))
    return np.array(pos), np.array(mean), np.array(sem)


def _axis_units(y: np.ndarray, rec: dict) -> np.ndarray:
    """Rescale raw projections so anchor default -> 1 and role_mean -> 0."""
    d, r = rec["anchor_default"], rec["anchor_role_mean"]
    return (y - r) / (d - r)


def _style(ax) -> None:
    ax.grid(axis="y", alpha=0.25, linewidth=0.5)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)


def figure_per_model(records: list[dict], out_dir: str, plt) -> list[str]:
    """One figure per (model, condition): temp panels with mean±SEM band, spaghetti, anchors."""
    written = []
    by_mc = defaultdict(list)
    for r in records:
        by_mc[(r["model_key"], r["condition"])].append(r)
    for (model, cond), recs in sorted(by_mc.items()):
        recs = sorted(recs, key=lambda r: r["temperature"])
        fig, axes = plt.subplots(1, len(recs), figsize=(4.2 * len(recs), 3.6), sharey=True, squeeze=False)
        color = MODEL_COLORS.get(model, "#555555")
        for ax, rec in zip(axes[0], recs):
            for t in rec["trajectories"]:
                ax.plot(range(1, len(t["series"]) + 1), t["series"], color=color, alpha=0.12, linewidth=0.7)
            pos, mean, sem = mean_trajectory(rec["trajectories"])
            ax.plot(pos, mean, color=color, linewidth=2)
            ax.fill_between(pos, mean - 1.96 * sem, mean + 1.96 * sem, color=color, alpha=0.25, linewidth=0)
            if rec["anchor_default"] is not None:
                ax.axhline(rec["anchor_default"], color="#444444", linewidth=1, linestyle="--")
                ax.axhline(rec["anchor_role_mean"], color="#444444", linewidth=1, linestyle=":")
                ax.text(0.99, rec["anchor_default"], "default Assistant", ha="right", va="bottom",
                        fontsize=7, color="#444444", transform=ax.get_yaxis_transform())
                ax.text(0.99, rec["anchor_role_mean"], "mean role vector", ha="right", va="bottom",
                        fontsize=7, color="#444444", transform=ax.get_yaxis_transform())
            ax.set_title(f"temp {rec['temperature']}", fontsize=10)
            ax.set_xlabel("response # (per instance)")
            _style(ax)
        axes[0][0].set_ylabel(f"projection on Assistant Axis (L{recs[0]['target_layer']})")
        fig.suptitle(f"{model} — ai2ai self-conversation, {CONDITION_LABELS[cond]}", fontsize=11)
        fig.tight_layout()
        out = os.path.join(out_dir, f"drift__{model}__{cond}.png")
        fig.savefig(out, dpi=150)
        plt.close(fig)
        written.append(out)
    return written


def figure_cross_model(records: list[dict], out_dir: str, plt, temp: float = 1.0) -> str | None:
    """Cross-model comparison at one temperature, in anchor-calibrated axis units."""
    conds = sorted({r["condition"] for r in records})
    usable = [r for r in records if r["temperature"] == temp and r["anchor_default"] is not None]
    if not usable:
        return None
    fig, axes = plt.subplots(1, len(conds), figsize=(4.6 * len(conds), 3.8), sharey=True, squeeze=False)
    for ax, cond in zip(axes[0], conds):
        for rec in sorted((r for r in usable if r["condition"] == cond), key=lambda r: r["model_key"]):
            pos, mean, sem = mean_trajectory(rec["trajectories"])
            color = MODEL_COLORS.get(rec["model_key"], "#555555")
            ax.plot(pos, _axis_units(mean, rec), color=color, linewidth=2, label=rec["model_key"])
            ax.fill_between(pos, _axis_units(mean - 1.96 * sem, rec), _axis_units(mean + 1.96 * sem, rec),
                            color=color, alpha=0.2, linewidth=0)
        ax.axhline(1.0, color="#444444", linewidth=1, linestyle="--")
        ax.axhline(0.0, color="#444444", linewidth=1, linestyle=":")
        ax.set_title(CONDITION_LABELS[cond], fontsize=10)
        ax.set_xlabel("response # (per instance)")
        _style(ax)
    axes[0][0].set_ylabel("axis units (1 = default Assistant, 0 = mean role)")
    axes[0][-1].legend(frameon=False, fontsize=8)
    fig.suptitle(f"Assistant-Axis drift in ai2ai conversations (temp {temp})", fontsize=11)
    fig.tight_layout()
    out = os.path.join(out_dir, f"drift__cross_model__temp{temp}.png")
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out


def drift_stats(rec: dict) -> dict:
    """Start / end / delta for one (model, condition, temp) record, in raw and axis units."""
    starts, ends, below = [], [], 0
    for t in rec["trajectories"]:
        s = t["series"]
        if len(s) < 4:
            continue
        starts.append(s[0])
        end = float(np.mean(s[-3:]))
        ends.append(end)
        if rec["anchor_role_mean"] is not None and end < rec["anchor_role_mean"]:
            below += 1
    if not starts:
        return {}
    start, end = float(np.mean(starts)), float(np.mean(ends))
    out = {"n_traj": len(starts), "start": start, "end": end, "delta": end - start,
           "frac_end_below_role_mean": below / len(starts)}
    if rec["anchor_default"] is not None:
        d, r = rec["anchor_default"], rec["anchor_role_mean"]
        out["start_axis_units"] = (start - r) / (d - r)
        out["end_axis_units"] = (end - r) / (d - r)
    return out


def write_report(records: list[dict], figures: list[str], out_dir: str) -> str:
    lines = [
        "# Assistant-Axis drift in ai2ai conversations",
        "",
        "Per-turn mean response-token activations projected onto the Assistant Axis "
        "(Lu et al., arxiv 2601.10387; axes from `lu-christina/assistant-axis-vectors`), for "
        "two-instance self-conversations. Both instance views pooled. `axis units`: 1 = the "
        "model's mean default-Assistant activation, 0 = the mean fully-role-playing activation.",
        "",
        "| model | condition | temp | n traj | start | end | Δ | start (axis u.) | end (axis u.) | % end < role mean |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for rec in sorted(records, key=lambda r: (r["model_key"], r["condition"], r["temperature"])):
        s = drift_stats(rec)
        if not s:
            continue
        au = (f"{s['start_axis_units']:.2f}", f"{s['end_axis_units']:.2f}") if "start_axis_units" in s else ("—", "—")
        lines.append(
            f"| {rec['model_key']} | {CONDITION_LABELS[rec['condition']]} | {rec['temperature']} "
            f"| {s['n_traj']} | {s['start']:.1f} | {s['end']:.1f} | {s['delta']:+.1f} "
            f"| {au[0]} | {au[1]} | {100 * s['frac_end_below_role_mean']:.0f}% |"
        )
    lines += ["", "## Figures", ""]
    lines += [f"![]({os.path.basename(p)})" for p in figures]
    out = os.path.join(out_dir, "REPORT.md")
    with open(out, "w") as f:
        f.write("\n".join(lines) + "\n")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Aggregate Assistant-Axis projections into figures + report.")
    ap.add_argument("--results-root", default="results")
    ap.add_argument("--out-dir", default=os.path.join(os.path.dirname(__file__), "reports"))
    ap.add_argument("--allow-synthetic", action="store_true", help="include smoke-run outputs")
    args = ap.parse_args()

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    records = collect(args.results_root, allow_synthetic=args.allow_synthetic)
    if not records:
        raise SystemExit(f"no axis projection files under {args.results_root}/axis_*_ai2ai/analysis/")
    os.makedirs(args.out_dir, exist_ok=True)
    figures = figure_per_model(records, args.out_dir, plt)
    cross = figure_cross_model(records, args.out_dir, plt)
    if cross:
        figures.append(cross)
    report = write_report(records, figures, args.out_dir)
    print(f"wrote {report} + {len(figures)} figures")


if __name__ == "__main__":
    main()
