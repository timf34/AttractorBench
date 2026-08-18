#!/usr/bin/env python
"""SBERT endpoint map for the unsteering experiment family (see unsteering/README.md).

Where do unsteered conversations END UP? For each trait we embed the last 6 turns
of every temp-0.7 run (SBERT all-MiniLM-L6-v2, endpoint = mean of the last 6
message embeddings, as in oct_geometry.py) from:

  unsteer cells   <trait>_{pvec,lora,prompt}_unsteer_k*_ai2ai  (intervention withdrawn at K)
  ceilings        pvec-forever / lora-forever / richprompt-forever (never withdrawn)
  floor           base_pvec_ai2ai + base_ai2ai (no intervention at all)

One t-SNE over ALL endpoints, then 12 small-multiple panels (one per trait) with
the shared base floor in gray. Unsteer runs are filled when the onset judge says
the run ended in the TRAIT/HYBRID basin, hollow otherwise — so a filled circle
sitting on its arm's ceiling stars means "held, and held into the same basin".
Also writes a cluster-cohesion stat (full SBERT space, not the 2D projection):
mean cosine of held unsteer endpoints to their arm's ceiling centroid vs to the
base centroid.

    ./.venv/bin/python unsteering/endpoint_map.py
"""

import glob
import json
import os

import numpy as np

TRAITS = ["goodness", "honesty", "humor", "impulsiveness", "loving", "mathematical",
          "nonchalance", "poeticism", "remorse", "sarcasm", "sincerity", "sycophancy"]
ARMS = ["pvec", "lora", "prompt"]
COLORS = {"pvec": "#2a78d6", "lora": "#1baf7a", "prompt": "#eb6834"}
BASE_COLOR = "#8b8a85"
UNSTEER_DIRS = {"pvec": ["results/pvec_unsteer/{t}_pvec_unsteer_k*_ai2ai"],
                "lora": ["results/lora_unsteer/{t}_lora_unsteer_k*_ai2ai"],
                "prompt": ["results/prompt_unsteer/{t}_prompt_unsteer_k*_ai2ai",
                           "results/{t}_prompt_unsteer_k*_ai2ai"]}
CEILING_DIRS = {"pvec": ["results/pvec_steering/{t}_pvec_c*_l16_ai2ai"],
                "lora": ["results/{t}_ai2ai"],
                "prompt": ["results/{t}_richprompt_ai2ai"]}
FLOOR_DIRS = ["results/pvec_steering/base_pvec_ai2ai", "results/base_ai2ai"]
# arm-specific judge rubric outputs (run_onset_judge.py --basin-set {lora,prompt});
# fall back to the shared pvec-rubric file when no arm fork exists for the trait
JUDGE_PREFERENCE = {"lora": "*__onset_judge_lora.json", "prompt": "*__onset_judge_prompt.json"}
HELD_BASINS = {"TRAIT", "HYBRID"}
ENDPOINT_TURNS = 6
OUT_DIR = "results/unsteer_geometry"
CACHE = os.path.join(OUT_DIR, "embeddings_temp0.7.npz")


def run_tails(cond_dir):
    """[(run_id, last-6 non-empty turn texts)] from the dir's temp-0.7 file(s)."""
    tails = []
    for path in sorted(glob.glob(os.path.join(cond_dir, "two_instance*temp0.7.json"))):
        for run in json.load(open(path))["runs"]:
            texts = [s for s in ((t.get("content_clean") or t.get("content") or "").strip()
                                 for t in run["turns"]) if s]
            if len(texts) >= ENDPOINT_TURNS:
                tails.append((f"{cond_dir}:{run['run_index']}", texts[-ENDPOINT_TURNS:]))
    return tails


def held_map(cond_dir, arm):
    """run_index -> end basin held? from the condition's onset-judge file,
    preferring the arm's own rubric output over the shared pvec one."""
    preferred = JUDGE_PREFERENCE.get(arm)
    paths = (glob.glob(os.path.join(cond_dir, "analysis", preferred)) if preferred else []) \
        or glob.glob(os.path.join(cond_dir, "analysis", "*__onset_judge.json"))
    if not paths:
        return {}
    runs = json.load(open(sorted(paths)[0])).get("runs", [])
    return {r["run_index"]: r.get("end_basin") in HELD_BASINS for r in runs if r.get("parse_ok")}


def collect():
    """[(trait, arm, kind, held, run_id, tail_texts)]; floor rows have trait=None."""
    rows = []
    for t in TRAITS:
        for arm in ARMS:
            for tpl in UNSTEER_DIRS[arm]:
                for d in sorted(glob.glob(tpl.format(t=t))):
                    hm = held_map(d, arm)
                    for rid, tail in run_tails(d):
                        idx = int(rid.rsplit(":", 1)[1])
                        rows.append((t, arm, "unsteer", hm.get(idx, False), rid, tail))
            for tpl in CEILING_DIRS[arm]:
                for d in sorted(glob.glob(tpl.format(t=t))):
                    rows.extend((t, arm, "ceiling", None, rid, tail) for rid, tail in run_tails(d))
    for d in FLOOR_DIRS:
        rows.extend((None, "base", "floor", None, rid, tail) for rid, tail in run_tails(d))
    return rows


def embed_endpoints(rows):
    """One endpoint vector per row: mean SBERT embedding of its 6 tail turns."""
    texts = [s for r in rows for s in r[5]]
    n_chars = sum(len(s) for s in texts)
    if os.path.exists(CACHE):
        z = np.load(CACHE)
        if len(z["emb"]) == len(texts) and int(z["n_chars"]) == n_chars:
            emb = z["emb"]
        else:
            emb = None
    else:
        emb = None
    if emb is None:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("all-MiniLM-L6-v2")
        emb = model.encode(texts, batch_size=128, show_progress_bar=True,
                           normalize_embeddings=True)
        os.makedirs(OUT_DIR, exist_ok=True)
        np.savez_compressed(CACHE, emb=emb, n_chars=n_chars)
    return emb.reshape(len(rows), ENDPOINT_TURNS, -1).mean(axis=1)


def cos_to(X, c):
    return float(np.mean(X @ c / (np.linalg.norm(X, axis=1) * np.linalg.norm(c))))


def main():
    rows = collect()
    E = embed_endpoints(rows)
    trait = np.array([r[0] or "" for r in rows])
    arm = np.array([r[1] for r in rows])
    kind = np.array([r[2] for r in rows])
    held = np.array([bool(r[3]) for r in rows])
    print(f"{len(rows)} run endpoints "
          f"({(kind == 'unsteer').sum()} unsteer, {(kind == 'ceiling').sum()} ceiling, "
          f"{(kind == 'floor').sum()} floor)")

    # ---- cohesion stat in the full SBERT space ----
    base_c = E[kind == "floor"].mean(0)
    summary = {}
    for t in TRAITS:
        summary[t] = {}
        for a in ARMS:
            ceil = E[(trait == t) & (arm == a) & (kind == "ceiling")]
            hu = E[(trait == t) & (arm == a) & (kind == "unsteer") & held]
            n_uns = int(((trait == t) & (arm == a) & (kind == "unsteer")).sum())
            if not len(ceil) or not n_uns:
                continue
            summary[t][a] = {"n_unsteer_runs": n_uns, "n_held": len(hu),
                             "cos_held_to_ceiling": cos_to(hu, ceil.mean(0)) if len(hu) else None,
                             "cos_held_to_base": cos_to(hu, base_c) if len(hu) else None}
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    # ---- one t-SNE over all endpoints, split into per-trait panels ----
    from sklearn.manifold import TSNE
    XY = TSNE(n_components=2, random_state=0, init="pca",
              perplexity=min(30, len(E) - 1)).fit_transform(E)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(4, 3, figsize=(13, 15), sharex=True, sharey=True)
    fig.suptitle("Unsteer endpoints (t-SNE of SBERT embeddings, one point per run, temp 0.7)\n"
                 "stars = forever-on ceiling, gray = unsteered base floor; "
                 "filled circle = judge says run ended in the trait basin", fontsize=12)
    floor_xy = XY[kind == "floor"]
    for ax, t in zip(axes.flat, TRAITS):
        ax.scatter(*floor_xy.T, s=6, color=BASE_COLOR, alpha=0.5, linewidths=0)
        for a in ARMS:
            sel = (trait == t) & (arm == a)
            cx = XY[sel & (kind == "ceiling")]
            if len(cx):
                ax.scatter(*cx.T, s=55, color=COLORS[a], marker="*", alpha=0.8, linewidths=0)
            for h, fc in [(True, COLORS[a]), (False, "none")]:
                ux = XY[sel & (kind == "unsteer") & (held == h)]
                if len(ux):
                    ax.scatter(*ux.T, s=16, facecolors=fc, edgecolors=COLORS[a],
                               linewidths=0.8, alpha=0.75)
        ax.set_title(t, fontsize=10)
        ax.set_xticks([]), ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_color("0.8")
    mk = plt.matplotlib.lines.Line2D
    handles = [mk([], [], ls="", marker="o", color=COLORS[a], label=f"{a} unsteer") for a in ARMS]
    handles += [mk([], [], ls="", marker="o", mfc="k", mec="k", label="held (TRAIT/HYBRID end)"),
                mk([], [], ls="", marker="o", mfc="none", mec="k", label="not held"),
                mk([], [], ls="", marker="*", color="k", ms=10, label="forever-on ceiling"),
                mk([], [], ls="", marker="o", color=BASE_COLOR, ms=4, label="base floor")]
    fig.legend(handles=handles, loc="lower center", ncol=7, frameon=False, fontsize=9)
    fig.tight_layout(rect=(0, 0.025, 1, 0.955))
    out_png = os.path.join(OUT_DIR, "endpoint_map.png")
    fig.savefig(out_png, dpi=150)
    print(f"wrote {out_png} + {OUT_DIR}/summary.json")


if __name__ == "__main__":
    main()
