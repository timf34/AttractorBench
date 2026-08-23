#!/usr/bin/env python
"""Verbatim-echo collapse across the unsteering experiment family.

Quantifies how often ai2ai conversations degenerate into (near-)verbatim
echoing, using the EXISTING stage-1 deterministic metrics (temp0.7 files only).

Polarity note: turn_similarity.norm_levenshtein is a SIMILARITY, not a
distance — attractorbench/analysis/deterministic.py::norm_levenshtein_sim
returns ``1 - dist / max_len`` (1.0 = identical consecutive turns). Entry i of
the list compares turns i+1 and i+2 (turns are 1-based).

Per-run metrics
  echo_frac        fraction of consecutive-turn pairs with norm_levenshtein
                   similarity > 0.9
  first_echo_turn  earliest of verbatim_loops.first_exact_repeat_turn and the
                   later turn of any near_exact_pairs entry (threshold 0.9);
                   None if the run never echoes
  effective_turns  turns before the first echo (first_echo_turn - 1), or
                   n_turns when the run never echoes

Arm categories
  pvec_unsteer / prompt_unsteer / lora_unsteer   results/<arm>_unsteer/<trait>_<arm>_unsteer_k<K>_ai2ai
  pvec_ceiling    results/pvec_steering/<trait>_pvec_c*_l16_ai2ai (always-on steering)
  prompt_ceiling  results/<trait>_richprompt_ai2ai               (always-on persona prompt)
  lora_ceiling    results/<trait>_ai2ai                          (always-on persona LoRA)
  base            results/base_ai2ai + results/pvec_steering/base_pvec_ai2ai (floor)

If a condition has a temp0.7 raw run file but no stage-1 file (a handful of
prompt_unsteer conditions), the same repo code (analyse_run) recomputes the
needed fields in memory — nothing is written outside --out-dir.

    python unsteering/echo_analysis.py            # writes results/unsteer_echo/
"""

import argparse
import glob
import json
import os
import re
import statistics
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ECHO_THRESHOLD = 0.9  # matches verbatim_loops.near_exact_threshold in stage-1
UNSTEER_RE = re.compile(r"^(?P<trait>[a-z]+)_(?P<arm>pvec|prompt|lora)_unsteer_k(?P<k>\d+)_ai2ai"
                        r"(?P<base>_[a-z0-9.\-]+)?$")   # optional cross-base EXP_SUFFIX (_qwen-2.5-7b)
PVEC_CEIL_RE = re.compile(r"^(?P<trait>[a-z]+)_pvec_c[\d.]+_l16_ai2ai$")
RICHPROMPT_RE = re.compile(r"^(?P<trait>[a-z]+)_richprompt_ai2ai$")
LORA_CEIL_RE = re.compile(r"^(?P<trait>[a-z]+)_ai2ai$")

ARM_ORDER = ["pvec_unsteer", "prompt_unsteer", "lora_unsteer",
             "pvec_ceiling", "prompt_ceiling", "lora_ceiling", "base"]
ARM_SHORT = {"pvec_unsteer": "U-pvec", "prompt_unsteer": "U-prompt", "lora_unsteer": "U-lora",
             "pvec_ceiling": "C-pvec", "prompt_ceiling": "C-prompt", "lora_ceiling": "C-lora",
             "base": "base"}
# same validated categorical slots as unsteering_compare.py, + neutral gray for
# the base floor (a reference, not a series: identity is carried by its axis
# position / direct label, never by the gray alone)
FAMILY_COLORS = {"pvec": "#2a78d6", "prompt": "#eb6834", "lora": "#1baf7a"}
BASE_COLOR = "#8b8a85"
ARM_COLORS = {"pvec_unsteer": FAMILY_COLORS["pvec"], "prompt_unsteer": FAMILY_COLORS["prompt"],
              "lora_unsteer": FAMILY_COLORS["lora"], "pvec_ceiling": FAMILY_COLORS["pvec"],
              "prompt_ceiling": FAMILY_COLORS["prompt"], "lora_ceiling": FAMILY_COLORS["lora"],
              "base": BASE_COLOR}
MARKERS = {"pvec": "o", "prompt": "s", "lora": "^"}  # secondary encoding, as in unsteering_compare


# ---------------------------------------------------------------- loading

def _stage1_runs(cond_dir):
    """Per-run stage-1 dicts for a condition dir, temp0.7 only.

    Prefers existing analysis/*__temp0.7__stage1.json; falls back to running
    the repo's own analyse_run over the raw temp0.7 condition file in memory.
    Returns (runs, fallback_used).
    """
    paths = sorted(glob.glob(os.path.join(cond_dir, "analysis", "*__temp0.7__stage1.json")))
    if paths:
        runs = []
        for p in paths:
            with open(p, encoding="utf-8") as f:
                runs.extend(json.load(f)["runs"])
        return runs, False
    raw = sorted(glob.glob(os.path.join(cond_dir, "*__temp0.7.json")))
    if not raw:
        return [], False
    from attractorbench.analysis.deterministic import analyse_run
    runs = []
    for p in raw:
        with open(p, encoding="utf-8") as f:
            cond = json.load(f)
        for run in cond["runs"]:
            runs.append(analyse_run(run, top_words=5))
    return runs, True


def _run_metrics(r):
    lev = r["turn_similarity"]["norm_levenshtein"]
    echo_frac = (sum(s > ECHO_THRESHOLD for s in lev) / len(lev)) if lev else 0.0
    vb = r["verbatim_loops"]
    candidates = []
    if vb.get("first_exact_repeat_turn") is not None:
        candidates.append(vb["first_exact_repeat_turn"])
    candidates.extend(p[1] for p in vb.get("near_exact_pairs", []))  # later turn of each pair
    first_echo = min(candidates) if candidates else None
    effective = (first_echo - 1) if first_echo is not None else r["n_turns"]
    return {"run_index": r["run_index"], "n_turns": r["n_turns"],
            "echo_frac": round(echo_frac, 4), "first_echo_turn": first_echo,
            "effective_turns": effective}


def discover(results_root):
    """[(arm, trait_or_None, K_or_None, cond_dir)] for every condition in scope."""
    cells = []
    for fam in ("pvec", "prompt", "lora"):
        for d in sorted(glob.glob(os.path.join(results_root, f"{fam}_unsteer", "*_ai2ai"))):
            m = UNSTEER_RE.match(os.path.basename(d))
            if m:
                cells.append((f"{m['arm']}_unsteer", m["trait"], int(m["k"]), d))
    for d in sorted(glob.glob(os.path.join(results_root, "pvec_steering", "*_l16_ai2ai"))):
        m = PVEC_CEIL_RE.match(os.path.basename(d))
        if m:
            cells.append(("pvec_ceiling", m["trait"], None, d))
    traits = {t for _, t, _, _ in cells if t}
    for d in sorted(glob.glob(os.path.join(results_root, "*_richprompt_ai2ai"))):
        m = RICHPROMPT_RE.match(os.path.basename(d))
        if m:
            cells.append(("prompt_ceiling", m["trait"], None, d))
    for d in sorted(glob.glob(os.path.join(results_root, "*_ai2ai"))):
        m = LORA_CEIL_RE.match(os.path.basename(d))
        if m and m["trait"] in traits:  # trait LoRA dirs only, not base_ai2ai etc.
            cells.append(("lora_ceiling", m["trait"], None, d))
    for d in (os.path.join(results_root, "base_ai2ai"),
              os.path.join(results_root, "pvec_steering", "base_pvec_ai2ai")):
        if os.path.isdir(d):
            cells.append(("base", None, None, d))
    return cells


def load_records(results_root):
    records, fallbacks = [], []
    for arm, trait, k, cond_dir in discover(results_root):
        runs, fb = _stage1_runs(cond_dir)
        if fb:
            fallbacks.append(cond_dir)
        for r in runs:
            rec = _run_metrics(r)
            rec.update({"arm": arm, "trait": trait, "K": k,
                        "condition": os.path.relpath(cond_dir, results_root)})
            records.append(rec)
    return records, fallbacks


# ---------------------------------------------------------------- aggregation

def _median(xs):
    return round(statistics.median(xs), 4) if xs else None


def aggregate(recs):
    if not recs:
        return None
    fracs = [r["echo_frac"] for r in recs]
    onsets = [r["first_echo_turn"] for r in recs if r["first_echo_turn"] is not None]
    return {"n_runs": len(recs),
            "mean_echo_frac": round(sum(fracs) / len(fracs), 4),
            "median_echo_frac": _median(fracs),
            "frac_runs_with_echo": round(len(onsets) / len(recs), 4),
            "median_first_echo_turn": _median(onsets),
            "median_effective_turns": _median([r["effective_turns"] for r in recs])}


def group(records, keyfn):
    out = {}
    for r in records:
        out.setdefault(keyfn(r), []).append(r)
    return out


# ---------------------------------------------------------------- figures

def _style(ax):
    ax.grid(True, color="0.9", linewidth=0.7)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)


def _trait_grid(traits, title):
    fig, axes = plt.subplots(4, 3, figsize=(10, 11.5), sharex=True, sharey=True)
    fig.suptitle(title, fontsize=11)
    for ax in axes.flat[len(traits):]:
        ax.set_visible(False)
    return fig, axes


def plot_echo_by_trait_arm(records, traits, out_path, rng):
    fig, axes = _trait_grid(traits, "Verbatim-echo collapse by arm (temp 0.7)\n"
                            "echo_frac = share of consecutive-turn pairs with norm-Levenshtein "
                            f"similarity > {ECHO_THRESHOLD}; unsteer arms pooled over K")
    base_recs = [r for r in records if r["arm"] == "base"]
    for ax, trait in zip(axes.flat, traits):
        for x, arm in enumerate(ARM_ORDER):
            cell = base_recs if arm == "base" else [
                r for r in records if r["arm"] == arm and r["trait"] == trait]
            if not cell:
                continue
            ys = [r["echo_frac"] for r in cell]
            xs = [x + rng.uniform(-0.22, 0.22) for _ in ys]  # strip with jitter
            ax.scatter(xs, ys, s=9, color=ARM_COLORS[arm],
                       alpha=0.35 if "ceiling" in arm or arm == "base" else 0.45,
                       linewidths=0, zorder=2)
            ax.hlines(statistics.median(ys), x - 0.3, x + 0.3, color=ARM_COLORS[arm],
                      linewidth=2.4, zorder=3)  # median dash carries the reading
        ax.set_title(trait, fontsize=10)
        ax.set_ylim(-0.04, 1.04)
        ax.set_xticks(range(len(ARM_ORDER)))
        _style(ax)
    for ax in axes[-1]:
        ax.set_xticklabels([ARM_SHORT[a] for a in ARM_ORDER], rotation=45,
                           ha="right", fontsize=8)
    for ax in axes[:, 0]:
        ax.set_ylabel("echo_frac")
    fig.text(0.01, 0.005, "U- = unsteered at K (pooled over K)   C- = always-on ceiling   "
             "base = unsteered floor   dash = median, dot = run", fontsize=8, color="0.35")
    fig.tight_layout(rect=(0, 0.02, 1, 0.95))
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_echo_vs_k(records, traits, out_path):
    fig, axes = _trait_grid(traits, "Does more steering dose mean more terminal echoing?\n"
                            "mean echo_frac vs K (switch-off turn), per unsteer arm (temp 0.7)")
    for ax, trait in zip(axes.flat, traits):
        for fam in ("pvec", "prompt", "lora"):
            cells = group([r for r in records if r["arm"] == f"{fam}_unsteer"
                           and r["trait"] == trait], lambda r: r["K"])
            pts = sorted((k, sum(x["echo_frac"] for x in v) / len(v))
                         for k, v in cells.items())
            if pts:
                ax.plot([k for k, _ in pts], [f for _, f in pts],
                        color=FAMILY_COLORS[fam], marker=MARKERS[fam], markersize=4,
                        linewidth=2, label=fam)
        ax.set_title(trait, fontsize=10)
        ax.set_ylim(-0.04, 1.04)
        _style(ax)
    for ax in axes[-1]:
        ax.set_xlabel("K (switch-off turn)")
    for ax in axes[:, 0]:
        ax.set_ylabel("mean echo_frac")
    handles = [plt.Line2D([], [], color=FAMILY_COLORS[a], marker=MARKERS[a],
                          markersize=4, linewidth=2, label=a) for a in ("pvec", "prompt", "lora")]
    fig.legend(handles=handles, loc="upper right", frameon=False, fontsize=9)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_effective_turns(records, traits, out_path):
    trait_arms = [a for a in ARM_ORDER if a != "base"]
    fig, ax = plt.subplots(figsize=(8, 7))
    base_recs = [r for r in records if r["arm"] == "base"]
    base_label = "base floor"
    if base_recs:
        med = statistics.median([r["effective_turns"] for r in base_recs])
        ax.axvline(med, color=BASE_COLOR, linewidth=2, zorder=1)
        base_label = f"base floor ({med:g})"
    for yi, trait in enumerate(traits):
        y = len(traits) - 1 - yi
        ax.hlines(y, 0, 30, color="0.93", linewidth=0.7, zorder=0)
        for arm in trait_arms:
            cell = [r for r in records if r["arm"] == arm and r["trait"] == trait]
            if not cell:
                continue
            med = statistics.median([r["effective_turns"] for r in cell])
            filled = "unsteer" in arm
            ax.scatter([med], [y], s=52, zorder=3, color=ARM_COLORS[arm] if filled else "white",
                       edgecolors=ARM_COLORS[arm], linewidths=1.6,
                       marker=MARKERS[arm.split("_")[0]])
    ax.set_yticks(range(len(traits)))
    ax.set_yticklabels(list(reversed(traits)), fontsize=9)
    ax.set_xlim(0, 31)
    ax.set_xlabel("median effective turns (turns before first exact/near-exact repeat; 30-turn runs)")
    ax.set_title("How many turns actually count, per (trait, arm) — temp 0.7", fontsize=11)
    _style(ax)
    handles = [plt.Line2D([], [], linestyle="", marker=MARKERS[f], markersize=7,
                          markerfacecolor=FAMILY_COLORS[f] if filled else "white",
                          markeredgecolor=FAMILY_COLORS[f], markeredgewidth=1.6,
                          label=f"{f} {'unsteer' if filled else 'ceiling'}")
               for filled in (True, False) for f in ("pvec", "prompt", "lora")]
    handles.append(plt.Line2D([], [], color=BASE_COLOR, linewidth=2, label=base_label))
    ax.legend(handles=handles, loc="center left", bbox_to_anchor=(1.01, 0.5),
              frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--results-root", default="results")
    ap.add_argument("--out-dir", default=os.path.join("results", "unsteer_echo"))
    args = ap.parse_args()

    records, fallbacks = load_records(args.results_root)
    if not records:
        raise SystemExit(f"no temp0.7 stage-1 data found under {args.results_root}")
    os.makedirs(args.out_dir, exist_ok=True)
    traits = sorted({r["trait"] for r in records if r["trait"]})

    per_arm = {a: aggregate(v) for a, v in
               sorted(group(records, lambda r: r["arm"]).items(),
                      key=lambda kv: ARM_ORDER.index(kv[0]))}
    per_cell = [dict(zip(("trait", "arm"), k), **aggregate(v)) for k, v in
                sorted(group([r for r in records if r["trait"]],
                             lambda r: (r["trait"], r["arm"])).items())]
    per_cell_by_k = [dict(zip(("trait", "arm", "K"), k), **aggregate(v)) for k, v in
                     sorted(group([r for r in records if r["K"] is not None],
                                  lambda r: (r["trait"], r["arm"], r["K"])).items())]

    summary = {
        "polarity_note": "turn_similarity.norm_levenshtein is a similarity "
                         "(1 - dist/max_len; 1.0 = identical), per "
                         "attractorbench/analysis/deterministic.py::norm_levenshtein_sim",
        "echo_threshold": ECHO_THRESHOLD,
        "temperature": 0.7,
        "stage1_fallback_conditions": [os.path.relpath(d, args.results_root) for d in fallbacks],
        "per_arm": per_arm,
        "per_trait_arm": per_cell,
        "per_trait_arm_k": per_cell_by_k,
        "runs": records,
    }
    with open(os.path.join(args.out_dir, "echo_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    import random
    plot_echo_by_trait_arm(records, traits, os.path.join(args.out_dir, "echo_by_trait_arm.png"),
                           random.Random(0))
    plot_echo_vs_k(records, traits, os.path.join(args.out_dir, "echo_vs_k.png"))
    plot_effective_turns(records, traits, os.path.join(args.out_dir, "effective_turns.png"))

    # ------------------------------------------------------------ stdout
    print("norm_levenshtein polarity: SIMILARITY (1 - dist/max_len); echo pair = sim > "
          f"{ECHO_THRESHOLD}\n")
    print(f"{'arm':<15} {'n':>4}  {'mean_echo':>9}  {'runs_w_echo':>11}  "
          f"{'med_first_echo':>14}  {'med_eff_turns':>13}")
    for arm, a in per_arm.items():
        fe = a["median_first_echo_turn"]
        print(f"{arm:<15} {a['n_runs']:>4}  {a['mean_echo_frac']:>9.3f}  "
              f"{a['frac_runs_with_echo']:>10.0%}  {fe if fe is not None else '-':>14}  "
              f"{a['median_effective_turns']:>13g}")
    print("\n5 most echo-collapsed (trait, arm) cells by mean echo_frac (n >= 5):")
    for c in sorted((c for c in per_cell if c["n_runs"] >= 5),
                    key=lambda c: -c["mean_echo_frac"])[:5]:
        print(f"  {c['trait']:<14} {c['arm']:<15} mean_echo={c['mean_echo_frac']:.3f} "
              f"(n={c['n_runs']}, med first echo turn {c['median_first_echo_turn']})")
    if fallbacks:
        print(f"\n{len(fallbacks)} condition(s) lacked a temp0.7 stage-1 file; metrics were "
              "recomputed in memory with attractorbench.analysis.deterministic.analyse_run:")
        for d in fallbacks:
            print(f"  {os.path.relpath(d, args.results_root)}")
    print(f"\n{len(records)} runs across {len(per_cell)} (trait, arm) cells; "
          f"wrote {args.out_dir}/{{echo_summary.json, echo_by_trait_arm.png, "
          f"echo_vs_k.png, effective_turns.png}}")


if __name__ == "__main__":
    main()
