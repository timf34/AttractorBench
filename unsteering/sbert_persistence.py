#!/usr/bin/env python
"""SBERT-based persistence metric for the unsteering experiments — an embedding
alternative to the LLM onset-judge verdicts (see unsteering/README.md).

For every unsteer run (arm in {pvec, lora, prompt}, trait, switch-off turn K) we
take the run's SBERT endpoint (mean all-MiniLM-L6-v2 embedding of the last 6
turns, reusing endpoint_map.py's collection + npz embedding cache) and compare
it, by cosine similarity in the full 384-d space, to:

  cos_to_ceiling  centroid of that arm's forever-on ceiling runs for the trait
  cos_to_base     centroid of the base floor runs (base_pvec_ai2ai + base_ai2ai)

SBERT-hit criterion (a run "persisted" geometrically):

    cos_to_ceiling > cos_to_base  AND  cos_to_ceiling > CEILING_COS_MIN (0.5)

i.e. the endpoint must be closer to its own arm's never-withdrawn attractor than
to the unsteered base attractor, and not merely "less far" — it must actually
resemble the ceiling (absolute cosine above the 0.5 margin).

Outputs (results/unsteer_geometry/):
  sbert_persistence.json  per (arm, trait, K) cell: n, sbert_hits, sbert_frac,
                          mean cos_to_ceiling, mean cos_to_base
  sbert_ignition.png      per-trait small multiples, % SBERT-hits vs K, one
                          line per arm (same style as unsteering_compare.py)
  sbert_vs_judge.png      per-cell agreement scatter: judge held-fraction (x)
                          vs SBERT hit-fraction (y), y=x reference line,
                          worst-disagreeing cells annotated

Also prints per-run judge-vs-SBERT agreement rates (join on run_index; judge
file = the arm's own rubric output — analysis/*__onset_judge_lora.json for lora
cells, *__onset_judge_prompt.json for prompt cells — else *__onset_judge.json,
held = end_basin in {TRAIT, HYBRID}) and the 5 most disagreeing cells.

    ./.venv/bin/python unsteering/sbert_persistence.py
"""

import glob
import json
import os
import re
import sys

import numpy as np

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

from unsteering import endpoint_map as em  # noqa: E402  (collect + embedding cache)

CEILING_COS_MIN = 0.5   # absolute-similarity margin in the SBERT-hit criterion
ARMS = ["pvec", "lora", "prompt"]
COLORS = {"pvec": "#2a78d6", "lora": "#1baf7a", "prompt": "#eb6834"}
MARKERS = {"pvec": "o", "prompt": "s", "lora": "^"}
HELD_BASINS = {"TRAIT", "HYBRID"}
COND_RE = re.compile(r"(?P<trait>[a-z]+)_(?P<arm>pvec|prompt|lora)_unsteer_k(?P<k>\d+)_ai2ai"
                     r"(?P<base>_[a-z0-9.\-]+)?$")   # optional cross-base EXP_SUFFIX (_qwen-2.5-7b)
OUT_DIR = os.path.join("results", "unsteer_geometry")


def cos(v, c):
    return float(v @ c / (np.linalg.norm(v) * np.linalg.norm(c)))


def judge_verdicts(cond_dir, arm):
    """run_index -> judge-held bool. Prefers the arm's own rubric output
    (*__onset_judge_lora.json / *__onset_judge_prompt.json) over the shared pvec one."""
    preferred = em.JUDGE_PREFERENCE.get(arm)
    paths = (glob.glob(os.path.join(cond_dir, "analysis", preferred)) if preferred else []) \
        or glob.glob(os.path.join(cond_dir, "analysis", "*__onset_judge.json"))
    if not paths:
        return {}
    runs = json.load(open(sorted(paths)[0])).get("runs", [])
    return {r["run_index"]: r.get("end_basin") in HELD_BASINS for r in runs if r.get("parse_ok")}


def gather():
    """Per-run records + centroids, from endpoint_map's rows and embedding cache."""
    rows = em.collect()
    E = em.embed_endpoints(rows)
    trait = np.array([r[0] or "" for r in rows])
    arm = np.array([r[1] for r in rows])
    kind = np.array([r[2] for r in rows])

    base_c = E[kind == "floor"].mean(0)
    ceiling_c = {}  # (arm, trait) -> centroid
    for a in ARMS:
        for t in em.TRAITS:
            sel = (arm == a) & (trait == t) & (kind == "ceiling")
            if sel.any():
                ceiling_c[(a, t)] = E[sel].mean(0)

    judged = {}   # cond_dir -> {run_index: held}
    runs = []     # per-unsteer-run dicts
    for i, (t, a, k, _held, rid, _tail) in enumerate(rows):
        if k != "unsteer" or (a, t) not in ceiling_c:
            continue
        cond_dir, idx = rid.rsplit(":", 1)
        m = COND_RE.search(cond_dir)
        if not m:
            continue
        if cond_dir not in judged:
            judged[cond_dir] = judge_verdicts(cond_dir, a)
        idx = int(idx)
        cc, cb = cos(E[i], ceiling_c[(a, t)]), cos(E[i], base_c)
        runs.append({"arm": a, "trait": t, "K": int(m["k"]), "run_index": idx,
                     "cos_to_ceiling": cc, "cos_to_base": cb,
                     "sbert_hit": cc > cb and cc > CEILING_COS_MIN,
                     "judge_held": judged[cond_dir].get(idx)})  # None if unjudged
    return runs


def cell_stats(runs):
    """[(arm, trait, K)] -> aggregate dict, sorted for stable output."""
    cells = {}
    for r in runs:
        cells.setdefault((r["arm"], r["trait"], r["K"]), []).append(r)
    out = []
    for (a, t, k), rs in sorted(cells.items(), key=lambda x: (x[0][1], ARMS.index(x[0][0]), x[0][2])):
        judged = [r for r in rs if r["judge_held"] is not None]
        out.append({
            "arm": a, "trait": t, "K": k, "n": len(rs),
            "sbert_hits": sum(r["sbert_hit"] for r in rs),
            "sbert_frac": round(sum(r["sbert_hit"] for r in rs) / len(rs), 4),
            "mean_cos_to_ceiling": round(float(np.mean([r["cos_to_ceiling"] for r in rs])), 4),
            "mean_cos_to_base": round(float(np.mean([r["cos_to_base"] for r in rs])), 4),
            "n_judged": len(judged),
            "judge_held_frac": (round(sum(r["judge_held"] for r in judged) / len(judged), 4)
                                if judged else None),
        })
    return out


def plot_ignition(cells, out_path, plt):
    traits = sorted({c["trait"] for c in cells})
    fig, axes = plt.subplots(4, 3, figsize=(10, 11), sharex=True, sharey=True)
    fig.suptitle("Unsteer ignition, SBERT metric: % of runs whose endpoint sits in the "
                 "trait basin geometrically\n(cos to own-arm ceiling centroid > cos to base "
                 f"centroid, and > {CEILING_COS_MIN})", fontsize=11)
    arms_present = set()
    for ax, t in zip(axes.flat, traits):
        for a in ARMS:
            pts = sorted((c["K"], 100.0 * c["sbert_frac"]) for c in cells
                         if c["arm"] == a and c["trait"] == t)
            if not pts:
                continue
            arms_present.add(a)
            ax.plot([k for k, _ in pts], [f for _, f in pts], color=COLORS[a],
                    marker=MARKERS[a], markersize=4, linewidth=2, label=a)
        ax.set_title(t, fontsize=10)
        ax.set_ylim(-5, 105)
        ax.grid(True, color="0.9", linewidth=0.7)
        ax.set_axisbelow(True)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
    for ax in axes.flat[len(traits):]:
        ax.set_visible(False)
    for ax in axes[-1]:
        ax.set_xlabel("K (switch-off turn)")
    for ax in axes[:, 0]:
        ax.set_ylabel("% SBERT-hit")
    handles = [plt.Line2D([], [], color=COLORS[a], marker=MARKERS[a], markersize=4,
                          linewidth=2, label=a) for a in ARMS if a in arms_present]
    fig.legend(handles=handles, loc="upper right", frameon=False, fontsize=9)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_vs_judge(cells, out_path, plt):
    cells = [c for c in cells if c["judge_held_frac"] is not None]
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.plot([0, 1], [0, 1], color="0.75", linewidth=1, linestyle="--", zorder=1)
    for a in ARMS:
        xs = [c["judge_held_frac"] for c in cells if c["arm"] == a]
        ys = [c["sbert_frac"] for c in cells if c["arm"] == a]
        if xs:
            ax.scatter(xs, ys, s=30, color=COLORS[a], marker=MARKERS[a],
                       alpha=0.75, linewidths=0, label=a, zorder=2)
    worst = sorted(cells, key=lambda c: -abs(c["judge_held_frac"] - c["sbert_frac"]))[:5]
    offsets = [(6, 4), (6, -12), (-6, 4), (6, 16), (-6, -12)]  # stagger coincident labels
    for c, (dx, dy) in zip(worst, offsets):
        ax.annotate(f"{c['trait']} {c['arm']} K{c['K']}",
                    (c["judge_held_frac"], c["sbert_frac"]),
                    textcoords="offset points", xytext=(dx, dy), fontsize=8, color="0.25",
                    ha="right" if dx < 0 else "left")
    ax.set_xlabel("judge held-fraction (end basin TRAIT/HYBRID)")
    ax.set_ylabel("SBERT hit-fraction (endpoint nearer ceiling, cos > "
                  f"{CEILING_COS_MIN})")
    ax.set_title("SBERT persistence vs LLM-judge verdicts, per (arm, trait, K) cell",
                 fontsize=11)
    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(-0.03, 1.03)
    ax.set_aspect("equal")
    ax.grid(True, color="0.92", linewidth=0.7)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(frameon=False, fontsize=9, loc="upper left", title="arm")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def print_report(runs, cells):
    joined = [r for r in runs if r["judge_held"] is not None]
    print(f"\nper-run judge vs SBERT agreement (n={len(joined)} judged runs):")
    for a in ARMS:
        rs = [r for r in joined if r["arm"] == a]
        if not rs:
            continue
        agree = sum(r["judge_held"] == r["sbert_hit"] for r in rs)
        print(f"  {a:<7} {agree:>4}/{len(rs):<4} = {100 * agree / len(rs):.1f}%")
    agree = sum(r["judge_held"] == r["sbert_hit"] for r in joined)
    print(f"  {'ALL':<7} {agree:>4}/{len(joined):<4} = {100 * agree / len(joined):.1f}%")

    judged = [c for c in cells if c["judge_held_frac"] is not None]
    worst = sorted(judged, key=lambda c: -abs(c["judge_held_frac"] - c["sbert_frac"]))[:5]
    print("\n5 most disagreeing cells (|judge − SBERT| in held/hit fraction):")
    for c in worst:
        direction = ("judge says held, SBERT says endpoints drifted off the ceiling"
                     if c["judge_held_frac"] > c["sbert_frac"]
                     else "SBERT says endpoints resemble the ceiling, judge says basin lost")
        print(f"  {c['trait']:<14} {c['arm']:<7} K{c['K']:<3} judge {100 * c['judge_held_frac']:>3.0f}% "
              f"vs SBERT {100 * c['sbert_frac']:>3.0f}%  (cos_ceil {c['mean_cos_to_ceiling']:.2f}, "
              f"cos_base {c['mean_cos_to_base']:.2f}) — {direction}")


def main():
    os.chdir(REPO_ROOT)
    runs = gather()
    cells = cell_stats(runs)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "sbert_persistence.json"), "w") as f:
        json.dump(cells, f, indent=2)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plot_ignition(cells, os.path.join(OUT_DIR, "sbert_ignition.png"), plt)
    plot_vs_judge(cells, os.path.join(OUT_DIR, "sbert_vs_judge.png"), plt)

    print(f"{len(runs)} unsteer runs in {len(cells)} (arm, trait, K) cells")
    print(f"{'arm':<7} {'trait':<14} {'K':>3} {'n':>3} {'hits':>4}  hit%   cos_ceil  cos_base  judge%")
    for c in cells:
        j = f"{100 * c['judge_held_frac']:.0f}%" if c["judge_held_frac"] is not None else "-"
        print(f"{c['arm']:<7} {c['trait']:<14} {c['K']:>3} {c['n']:>3} {c['sbert_hits']:>4}  "
              f"{100 * c['sbert_frac']:>3.0f}%   {c['mean_cos_to_ceiling']:>7.3f}  "
              f"{c['mean_cos_to_base']:>7.3f}  {j:>5}")
    print_report(runs, cells)
    print(f"\nwrote {OUT_DIR}/sbert_persistence.json, sbert_ignition.png, sbert_vs_judge.png")


if __name__ == "__main__":
    main()
