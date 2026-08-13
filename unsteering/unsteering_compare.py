#!/usr/bin/env python
"""Cross-arm ignition comparison for the unsteering experiment family.

Three intervention arms plant the same persona trait for the first K assistant
turns of an ai2ai conversation, then withdraw the intervention and let the
dialogue free-run (see unsteering/README.md for the design):

  pvec    <trait>_pvec_unsteer_k<K>_ai2ai    activation steering, switched off at K
  prompt  <trait>_prompt_unsteer_k<K>_ai2ai  persona system prompt, swapped out at K
  lora    <trait>_lora_unsteer_k<K>_ai2ai    persona LoRA adapter, detached at K

The question is whether the trait basin *ignites* — keeps burning after the
intervention is removed. Per-run fate comes from run_onset_judge.py output
(results/**/<cond>/analysis/*__onset_judge.json); a run counts as "held" when
its end basin is TRAIT or HYBRID (judge is blind to K and to which turns were
steered). This script aggregates held-fraction per (arm, trait, K), writes a
CSV/JSON summary plus a 12-panel small-multiples figure (one panel per trait,
one ignition curve per arm), and prints a compact table.

    python unsteering_compare.py                      # writes results/unsteer_compare/
    python unsteering_compare.py --out-dir /tmp/x --results-root results
"""

import argparse
import csv
import glob
import json
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

COND_RE = re.compile(r"^(?P<trait>[a-z]+)_(?P<arm>pvec|prompt|lora)_unsteer_k(?P<k>\d+)_ai2ai$")
ARMS = ["pvec", "prompt", "lora"]
COLORS = {"pvec": "#2a78d6", "prompt": "#eb6834", "lora": "#1baf7a"}  # validated categorical slots
MARKERS = {"pvec": "o", "prompt": "s", "lora": "^"}                   # secondary encoding
HELD_BASINS = {"TRAIT", "HYBRID"}


def load_rows(results_root):
    """[(arm, trait, K, n, held)] from every unsteer onset-judge file under results_root."""
    paths = glob.glob(os.path.join(results_root, "*", "analysis", "*__onset_judge.json"))
    paths += glob.glob(os.path.join(results_root, "*", "*", "analysis", "*__onset_judge.json"))
    rows = {}
    for path in sorted(set(paths)):
        cond = os.path.basename(os.path.dirname(os.path.dirname(path)))
        m = COND_RE.match(cond)
        if not m:
            continue
        with open(path) as f:
            data = json.load(f)
        runs = [r for r in data.get("runs", []) if r.get("parse_ok")]
        key = (m["arm"], m["trait"], int(m["k"]))
        n, held = rows.get(key, (0, 0))
        rows[key] = (n + len(runs),
                     held + sum(r["end_basin"] in HELD_BASINS for r in runs))
    return sorted((arm, trait, k, n, held) for (arm, trait, k), (n, held) in rows.items())


def write_summary(rows, out_dir):
    records = [{"arm": a, "trait": t, "K": k, "n": n, "held": h,
                "held_frac": round(h / n, 4) if n else None}
               for a, t, k, n, h in rows]
    with open(os.path.join(out_dir, "unsteer_compare.json"), "w") as f:
        json.dump(records, f, indent=2)
    with open(os.path.join(out_dir, "unsteer_compare.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["arm", "trait", "K", "n", "held", "held_frac"])
        w.writeheader()
        w.writerows(records)
    return records


def plot(rows, out_path):
    traits = sorted({t for _, t, _, _, _ in rows})
    fig, axes = plt.subplots(4, 3, figsize=(10, 11), sharex=True, sharey=True)
    fig.suptitle("Unsteer ignition: % of runs still in the trait basin at conversation end\n"
                 "(LLM onset judge, blind to K; end basin TRAIT or HYBRID counts as held)",
                 fontsize=11)
    arms_present = set()
    for ax, trait in zip(axes.flat, traits):
        for arm in ARMS:
            pts = sorted((k, 100.0 * h / n) for a, t, k, n, h in rows
                         if a == arm and t == trait and n)
            if not pts:
                continue
            arms_present.add(arm)
            ax.plot([k for k, _ in pts], [f for _, f in pts],
                    color=COLORS[arm], marker=MARKERS[arm], markersize=4,
                    linewidth=2, label=arm)
        ax.set_title(trait, fontsize=10)
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
        ax.set_ylabel("% held")
    handles = [plt.Line2D([], [], color=COLORS[a], marker=MARKERS[a], markersize=4,
                          linewidth=2, label=a) for a in ARMS if a in arms_present]
    fig.legend(handles=handles, loc="upper right", frameon=False, fontsize=9)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def print_table(records):
    print(f"{'arm':<7} {'trait':<14} {'K':>3} {'n':>3} {'held':>4}  held%")
    for r in sorted(records, key=lambda r: (r["trait"], ARMS.index(r["arm"]), r["K"])):
        pct = f"{100 * r['held_frac']:.0f}%" if r["n"] else "-"
        print(f"{r['arm']:<7} {r['trait']:<14} {r['K']:>3} {r['n']:>3} {r['held']:>4}  {pct}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out-dir", default=os.path.join("results", "unsteer_compare"))
    ap.add_argument("--results-root", default="results")
    args = ap.parse_args()

    rows = load_rows(args.results_root)
    if not rows:
        raise SystemExit(f"no *_unsteer_k*_ai2ai onset-judge files under {args.results_root}")
    os.makedirs(args.out_dir, exist_ok=True)
    records = write_summary(rows, args.out_dir)
    fig_path = os.path.join(args.out_dir, "unsteer_compare.png")
    plot(rows, fig_path)
    print_table(records)
    arms = sorted({r["arm"] for r in records}, key=ARMS.index)
    print(f"\n{len(records)} (arm, trait, K) cells across arms: {', '.join(arms)}")
    print(f"wrote {args.out_dir}/unsteer_compare.{{csv,json,png}}")


if __name__ == "__main__":
    main()
