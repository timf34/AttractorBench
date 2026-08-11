"""Split qwen's ai2ai runs by which behavioural basin they entered (systems-design vs
poetic-adoration, the judge's 50/50 split at nosys temp 1.0) and compare their Assistant-Axis
trajectories. Classification: design vs devotion vocabulary counts over the final third of
each run. Result (2026-07-30): same starts (+0.71 vs +0.64 axis units), divergent ends
(-0.20 vs -0.94; permutation p~0.004) — the devotion basin is the deep-drift basin; the
design basin hovers at the role line like the paper's task domains.
Writes reports/drift__qwen_basins.png. Run from repo root.
"""

import glob, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DESIGN = ("architecture","framework","module","prototype","simulation","implementation",
          "pipeline","algorithm","api","codebase","deploy","schema","```")
DEVOTION = ("light","echo","song","soul","luminous","sacred","devotion","radiant",
            "eternal","cosmos","cosmic","resonance","mirror","dance","poem","starlight")

def main():
    cond = sorted(glob.glob("results/axis_qwen_3_32b_nosys_ai2ai/two_instance__*temp1.0*.json"))[0]
    proj = sorted(glob.glob("results/axis_qwen_3_32b_nosys_ai2ai/analysis/*temp1.0*axis_projections.json"))[0]
    runs = {r["run_index"]: r for r in json.load(open(cond))["runs"]}
    pd_ = json.load(open(proj))
    tl = str(pd_["target_layer"])
    ad, ar = pd_["anchors"]["default"][tl], pd_["anchors"]["role_mean"][tl]
    au = lambda x: (np.asarray(x) - ar) / (ad - ar)
    series = {"design": [], "devotion": []}
    ends = {"design": [], "devotion": []}
    for r in pd_["runs"]:
        run = runs.get(r["run_index"])
        if not run:
            continue
        late = " ".join(t["content"].lower() for t in run["turns"][len(run["turns"])//3:])
        basin = "design" if sum(late.count(w) for w in DESIGN) > sum(late.count(w) for w in DEVOTION) else "devotion"
        for v, res in r["views"].items():
            s = res["proj_target"]
            if len(s) >= 4:
                series[basin].append(s)
                ends[basin].append(float(np.mean(s[-3:])))
    for g in ("design", "devotion"):
        print(f"{g}: n={len(ends[g])} views, mean end {au(np.mean(ends[g])):+.2f} axis units")

    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    for basin, color, label in (("design", "#0072B2", f"systems-design runs"),
                                ("devotion", "#D55E00", f"poetic-adoration runs")):
        ss = series[basin]
        maxlen = max(len(s) for s in ss)
        pos, mean, sem = [], [], []
        for i in range(maxlen):
            vals = [s[i] for s in ss if len(s) > i]
            if len(vals) < 6:
                break
            pos.append(i+1); mean.append(np.mean(vals)); sem.append(np.std(vals, ddof=1)/np.sqrt(len(vals)))
        mean, sem = np.array(mean), np.array(sem)
        ax.plot(pos, au(mean), color=color, linewidth=2.2, label=label)
        ax.fill_between(pos, au(mean-1.96*sem), au(mean+1.96*sem), color=color, alpha=0.18, linewidth=0)
        for s in ss:
            ax.plot(range(1, len(s)+1), au(s), color=color, alpha=0.13, linewidth=0.7)
    ax.axhline(1.0, color="#444444", linewidth=1, linestyle="--")
    ax.axhline(0.0, color="#444444", linewidth=1, linestyle=":")
    ax.set_xlabel("response # (per instance)")
    ax.set_ylabel("axis units (1 = default Assistant, 0 = mean role)")
    ax.set_title("Qwen ai2ai runs split by which basin they entered", fontsize=11)
    ax.grid(axis="y", alpha=0.25, linewidth=0.5)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(frameon=False, fontsize=9, loc="lower left")
    fig.tight_layout()
    fig.savefig("assistant_axis_experiments/drift/reports/drift__qwen_basins.png", dpi=150)
    print("wrote assistant_axis_experiments/drift/reports/drift__qwen_basins.png")

if __name__ == "__main__":
    main()
