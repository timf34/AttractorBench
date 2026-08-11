"""Capped vs uncapped qwen ai2ai trajectories (both system-prompt conditions).
Result (2026-08-06): capped curves settle at ~+0.4 axis units, 0/60 views cross the role
line; uncapped dive to -0.7..-0.9 with 80-97% below. Writes
reports/drift__qwen_capped_vs_uncapped.png. Run from repo root."""
import glob, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def load_trajs(pattern):
    trajs, anchors = [], None
    for p in glob.glob(pattern):
        d = json.load(open(p))
        tl = str(d["target_layer"])
        anchors = (d["anchors"]["default"][tl], d["anchors"]["role_mean"][tl])
        for r in d["runs"]:
            for res in r["views"].values():
                if len(res["proj_target"]) >= 4:
                    trajs.append(res["proj_target"])
    return trajs, anchors

PAIRS = [("no system prompt", "results/axis_qwen_3_32b_nosys_ai2ai/analysis/*temp1.0*axis_projections.json",
          "results/axis_qwen_3_32b_capped_nosys_ai2ai/analysis/*axis_projections.json"),
         ("helpful assistant", "results/axis_qwen_3_32b_ai2ai/analysis/*temp1.0*axis_projections.json",
          "results/axis_qwen_3_32b_capped_ai2ai/analysis/*axis_projections.json")]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3), sharey=True)
for ax, (title, unc_pat, cap_pat) in zip(axes, PAIRS):
    for pat, color, label in ((unc_pat, "#0072B2", "uncapped"), (cap_pat, "#009E73", "activation capped")):
        trajs, (ad, ar) = load_trajs(pat)
        au = lambda x: (np.asarray(x) - ar) / (ad - ar)
        maxlen = max(len(s) for s in trajs)
        pos, mean, sem = [], [], []
        for i in range(maxlen):
            vals = [s[i] for s in trajs if len(s) > i]
            if len(vals) < 10: break
            pos.append(i+1); mean.append(np.mean(vals)); sem.append(np.std(vals, ddof=1)/np.sqrt(len(vals)))
        mean, sem = np.array(mean), np.array(sem)
        ax.plot(pos, au(mean), color=color, linewidth=2.2, label=f"{label} (n={len(trajs)})")
        ax.fill_between(pos, au(mean-1.96*sem), au(mean+1.96*sem), color=color, alpha=0.18, linewidth=0)
        for s in trajs:
            ax.plot(range(1, len(s)+1), au(s), color=color, alpha=0.10, linewidth=0.6)
    ax.axhline(1.0, color="#444444", linewidth=1, linestyle="--")
    ax.axhline(0.0, color="#444444", linewidth=1, linestyle=":")
    ax.set_title(title, fontsize=10.5)
    ax.set_xlabel("response # (per instance)")
    ax.grid(axis="y", alpha=0.25, linewidth=0.5)
    for side in ("top","right"): ax.spines[side].set_visible(False)
axes[0].text(0.98, 1.0, "default Assistant", ha="right", va="bottom", fontsize=7.5, color="#444444", transform=axes[0].get_yaxis_transform())
axes[0].text(0.98, 0.0, "mean role vector", ha="right", va="bottom", fontsize=7.5, color="#444444", transform=axes[0].get_yaxis_transform())
axes[0].set_ylabel("axis units (1 = default Assistant, 0 = mean role)")
axes[0].legend(frameon=False, fontsize=9, loc="lower left")
fig.suptitle("Qwen ai2ai: activation capping vs uncapped (temp 1.0)", fontsize=11.5)
fig.tight_layout()
fig.savefig("assistant_axis_experiments/drift/reports/drift__qwen_capped_vs_uncapped.png", dpi=150)
print("wrote drift__qwen_capped_vs_uncapped.png")
