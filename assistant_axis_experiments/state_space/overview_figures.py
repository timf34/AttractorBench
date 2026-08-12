"""Summary figures for the manifold experiment (reports/manifold__qwen-3-32b.md).

Numbers are the FROZEN headline results copied from that report (incl. its inductive
robustness section) — regenerating them takes minutes of CV, and the report is the source of
truth. If the underlying analyses are ever rerun, update these constants from the report.

    python -m assistant_axis_experiments.state_space.overview_figures
"""

from __future__ import annotations

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")

# Feature-set colors, fixed (matches predict figures: a gray, a+z blue; g gets vermillion).
C = {"a": "#888888", "g": "#D55E00", "az": "#0072B2"}
LABEL = {"a": "a (linear 1-D)", "g": "g (geodesic 1-D)", "az": "a+z (multi-D)"}

# Transition-time OOF R² from turn-2 state (qwen, n=148): shared-fold transductive vs
# inductive per-fold graphs (manifold__qwen-3-32b.md, inductive robustness section).
TRANSITION = {"a": (0.034, 0.034), "g": (0.251, 0.276), "az": (0.483, 0.483)}

# Basin AUC at t=4/6/8 (same source), transductive -> inductive.
BASIN = {
    "helpful": {"a": ([0.752, 0.932, 0.917], [0.731, 0.930, 0.919]),
                "g": ([0.711, 0.941, 0.940], [0.599, 0.829, 0.858]),
                "az": ([0.900, 0.915, 0.946], [0.894, 0.927, 0.934])},
    "nosys": {"a": ([0.830, 0.900, 0.888], [0.822, 0.889, 0.887]),
              "g": ([0.735, 0.926, 0.921], [0.676, 0.781, 0.789]),
              "az": ([0.838, 0.929, 0.903], [0.821, 0.914, 0.892])},
}
TS = [4, 6, 8]


def main() -> None:
    fig, axs = plt.subplots(1, 3, figsize=(13.2, 4.1))

    # panel A: transition time — g beats a, robust to inductive graphs; az beats both
    x = np.arange(3)
    for i, fs in enumerate(("a", "g", "az")):
        trans, induct = TRANSITION[fs]
        axs[0].bar(x[i] - 0.19, trans, width=0.34, color=C[fs], alpha=0.45, linewidth=0)
        axs[0].bar(x[i] + 0.19, induct, width=0.34, color=C[fs], linewidth=0)
        axs[0].annotate(f"{induct:.2f}", (x[i] + 0.19, induct + 0.008),
                        ha="center", fontsize=8, color="#333333")
    axs[0].set_xticks(x, [LABEL[fs] for fs in ("a", "g", "az")], fontsize=8.5)
    from matplotlib.patches import Patch
    axs[0].legend(handles=[Patch(color="#666666", alpha=0.45, label="transductive graph"),
                           Patch(color="#666666", label="inductive (per-fold)")],
                  frameon=False, fontsize=8)
    axs[0].set_ylabel("OOF R² (crossing turn from turn-2 state)")
    axs[0].set_title("timing: geodesic 1-D beats linear 1-D,\nmulti-D beats both", fontsize=10)

    # panels B/C: basin AUC — g's late-turn parity was transductive leakage
    for ax, cond in zip(axs[1:], ("helpful", "nosys")):
        for fs in ("a", "az"):
            ax.plot(TS, BASIN[cond][fs][1], marker="o", color=C[fs], linewidth=2,
                    label=LABEL[fs])
        ax.plot(TS, BASIN[cond]["g"][0], marker="o", color=C["g"], linewidth=1.4,
                linestyle="--", label="g (transductive)")
        ax.plot(TS, BASIN[cond]["g"][1], marker="o", color=C["g"], linewidth=2,
                label="g (inductive)")
        ax.set_ylim(0.55, 1.0)
        ax.set_xticks(TS)
        ax.set_xlabel("state measured at turn t")
        ax.set_title(f"basin, `{cond}`: g's parity was leakage", fontsize=10)
    axs[1].set_ylabel("OOF AUC (eventual basin)")
    axs[2].legend(frameon=False, fontsize=8, loc="lower right")

    for ax in axs:
        ax.grid(alpha=0.25, linewidth=0.5, axis="y")
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
    fig.suptitle("qwen-3-32b: is the persona state one curved coordinate? (no — timing is "
                 "geodesic-readable, basin identity needs z)", fontsize=11)
    fig.tight_layout()
    out = os.path.join(REPORTS_DIR, "manifold__qwen-3-32b__summary.png")
    fig.savefig(out, dpi=150)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
