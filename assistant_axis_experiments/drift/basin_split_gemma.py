"""Split gemma-2-27b's ai2ai runs (temp 1.0) by the stage-2 judge's basin assignments and
compare their Assistant-Axis trajectories — the gemma analogue of basin_split_qwen.py,
prompted by the high variance visible in drift__story.png.

Unlike the qwen split (vocab classifier), the groups here come straight from the judge's
per-run indices in the stage2 reports:
  nosys:   farewell-ritual runs [0,1,4,5,6,7,8,11] vs creative-workshop runs [3,10,13,14]
           (one-offs 2, 9, 12 excluded)
  helpful: creative-workshop runs [0,3,4,5,11,12,13] vs AI-civics runs [1,2,6,7,8,10]
           (one-offs 9, 14 excluded)

Permutation test is at run level (both A/B views of a run stay together).
Writes reports/drift__gemma_basins.png. Run from repo root.
"""

import glob, json, itertools
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CONDITIONS = [
    {
        "title": "no system prompt",
        "proj_glob": "results/axis_gemma_2_27b_nosys_ai2ai/analysis/*temp1.0*axis_projections.json",
        "groups": [
            ("farewell-ritual runs", "#D55E00", {0, 1, 4, 5, 6, 7, 8, 11}),
            ("creative-workshop runs", "#0072B2", {3, 10, 13, 14}),
        ],
    },
    {
        "title": "helpful assistant",
        "proj_glob": "results/axis_gemma_2_27b_ai2ai/analysis/*temp1.0*axis_projections.json",
        "groups": [
            ("creative-workshop runs", "#0072B2", {0, 3, 4, 5, 11, 12, 13}),
            ("AI-civics runs", "#009E73", {1, 2, 6, 7, 8, 10}),
        ],
    },
]


def run_end(views: dict) -> tuple[list[list[float]], float | None]:
    """All >=4-length view series for a run, plus the run-level end (mean of last-3, pooled views)."""
    series = [res["proj_target"] for res in views.values() if len(res["proj_target"]) >= 4]
    if not series:
        return [], None
    return series, float(np.mean([np.mean(s[-3:]) for s in series]))


def perm_test(a: list[float], b: list[float], n: int = 20000, seed: int = 0) -> float:
    rng = np.random.default_rng(seed)
    pooled = np.array(a + b)
    obs = abs(np.mean(a) - np.mean(b))
    k = len(a)
    hits = 0
    for _ in range(n):
        rng.shuffle(pooled)
        if abs(np.mean(pooled[:k]) - np.mean(pooled[k:])) >= obs:
            hits += 1
    return hits / n


def main():
    fig, axes = plt.subplots(1, len(CONDITIONS), figsize=(6.4 * len(CONDITIONS), 4.4), sharey=True)
    for ax, cond in zip(np.atleast_1d(axes), CONDITIONS):
        pd_ = json.load(open(sorted(glob.glob(cond["proj_glob"]))[0]))
        tl = str(pd_["target_layer"])
        ad, ar = pd_["anchors"]["default"][tl], pd_["anchors"]["role_mean"][tl]
        au = lambda x: (np.asarray(x) - ar) / (ad - ar)
        runs = {r["run_index"]: r for r in pd_["runs"]}

        group_ends = []
        for label, color, idxs in cond["groups"]:
            series, ends = [], []
            for i in idxs:
                if i not in runs:
                    continue
                ss, end = run_end(runs[i]["views"])
                series.extend(ss)
                if end is not None:
                    ends.append(end)
            group_ends.append(ends)
            maxlen = max(len(s) for s in series)
            pos, mean, sem = [], [], []
            for i in range(maxlen):
                vals = [s[i] for s in series if len(s) > i]
                if len(vals) < 4:
                    break
                pos.append(i + 1)
                mean.append(np.mean(vals))
                sem.append(np.std(vals, ddof=1) / np.sqrt(len(vals)))
            mean, sem = np.array(mean), np.array(sem)
            ax.plot(pos, au(mean), color=color, linewidth=2.2,
                    label=f"{label} (n={len(ends)}, end {au(np.mean(ends)):+.2f})")
            ax.fill_between(pos, au(mean - 1.96 * sem), au(mean + 1.96 * sem),
                            color=color, alpha=0.18, linewidth=0)
            for s in series:
                ax.plot(range(1, len(s) + 1), au(s), color=color, alpha=0.13, linewidth=0.7)

        p = perm_test(group_ends[0], group_ends[1])
        d = au(np.mean(group_ends[0])) - au(np.mean(group_ends[1]))
        print(f"{cond['title']}: end-gap {d:+.2f} axis units, permutation p={p:.3f} "
              f"(n={len(group_ends[0])} vs {len(group_ends[1])} runs)")
        ax.axhline(1.0, color="#444444", linewidth=1, linestyle="--")
        ax.axhline(0.0, color="#444444", linewidth=1, linestyle=":")
        ax.set_xlabel("response # (per instance)")
        ax.set_title(f"{cond['title']}  (end-gap {d:+.2f}, p={p:.3f})", fontsize=11)
        ax.grid(axis="y", alpha=0.25, linewidth=0.5)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        ax.legend(frameon=False, fontsize=9, loc="lower left")
    np.atleast_1d(axes)[0].set_ylabel("axis units (1 = default Assistant, 0 = mean role)")
    fig.suptitle("Gemma ai2ai runs (temp 1.0) split by judge-assigned basin", fontsize=12)
    fig.tight_layout()
    fig.savefig("assistant_axis_experiments/drift/reports/drift__gemma_basins.png", dpi=150)
    print("wrote assistant_axis_experiments/drift/reports/drift__gemma_basins.png")


if __name__ == "__main__":
    main()
