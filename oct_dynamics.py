#!/usr/bin/env python
"""Phases 1/2/2.5 of the OCT cross-base geometry analysis (companion to oct_geometry.py).

Phase 1 — trajectories: WHEN does the persona take over from the base model?
  - turn-resolved silhouette (persona label vs base label) over turns
  - per-persona cross-base convergence curves + trait-takeover turn
  - condition-centroid trajectories in the endpoint-PCA basis
Phase 2 — decay modes: the model picks HOW the conversation collapses.
  - lexical self-echo (difflib ratio vs own previous turn), semantic self-echo
    (embedding cosine), lexicon entropy, reply length — per turn
  - run-level decay-feature silhouette: base label vs persona label (the mirror
    statistic of the endpoint geometry)
Phase 2.5 — robustness: bootstrap CIs for the headline block means, endpoint-window
  sensitivity, and an all-mpnet-base-v2 re-run (the paper's App C.6 ablation).

All local, no GPU. Reuses oct_geometry's turn loader + MiniLM cache.

    ./.venv/bin/python oct_dynamics.py
"""

import os
import json
from difflib import SequenceMatcher
from collections import Counter

import numpy as np

from oct_geometry import PERSONAS, BASES, OUT_DIR, ENDPOINT_TURNS, load_turns, embed, d_set_sq

MPNET_CACHE = os.path.join(OUT_DIR, "embeddings_mpnet_temp0.7.npz")
COLORS = {"llama": "#0072B2", "qwen": "#E69F00", "gemma": "#009E73"}   # Okabe-Ito, validated
STYLES = {"llama": "-", "qwen": "--", "gemma": ":"}                    # secondary encoding
N_TURNS = 30
LATE = 20          # turns >= LATE count as "late conversation" for decay features
ECHO_CAP = 200     # cap words per turn for the difflib echo metric (speed)

TRAITS = [p for p in PERSONAS if p != "base"]


# ---------------------------------------------------------------- data plumbing
def build_index(rows, emb):
    """Group turn embeddings/texts by (persona, base, run)."""
    runs = {}
    for (p, b, ri, ti, text), e in zip(rows, emb):
        runs.setdefault((p, b, ri), {})[ti] = (e, text)
    return runs


def turn_sets(runs, t):
    """condition -> array of turn-t embeddings across runs."""
    out = {}
    for (p, b, ri), turns in runs.items():
        if t in turns:
            out.setdefault((p, b), []).append(turns[t][0])
    return {c: np.array(v) for c, v in out.items() if len(v) >= 5}


def endpoints_from(runs, k):
    E, labels = [], []
    for key, turns in sorted(runs.items()):
        tis = sorted(turns)
        E.append(np.mean([turns[t][0] for t in tis[-k:]], axis=0))
        labels.append(key[:2])
    return np.array(E), labels


def block_means(D, conds):
    n = len(conds)
    def bm(pred):
        vals = [D[i, j] for i in range(n) for j in range(i + 1, n) if pred(conds[i], conds[j])]
        return float(np.mean(vals))
    return {
        "same persona (traits), diff base": bm(lambda a, b: a[0] == b[0] != "base" and a[1] != b[1]),
        "base control, diff base": bm(lambda a, b: a[0] == b[0] == "base" and a[1] != b[1]),
        "same base, diff persona": bm(lambda a, b: a[0] != b[0] and a[1] == b[1]),
        "diff persona and base": bm(lambda a, b: a[0] != b[0] and a[1] != b[1]),
    }


def cond_distance_matrix(E, labels, conds):
    idx = {c: [i for i, l in enumerate(labels) if l == c] for c in conds}
    n = len(conds)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            D[i, j] = D[j, i] = d_set_sq(E[idx[conds[i]]], E[idx[conds[j]]])
    return D, idx


def sil(X_or_D, labels, precomputed=False, perms=0, rng=None):
    from sklearn.metrics import silhouette_score, pairwise_distances
    D = X_or_D if precomputed else pairwise_distances(X_or_D)
    labels = np.asarray(labels)
    s = silhouette_score(D, labels, metric="precomputed")
    if not perms:
        return s, None
    rng = rng or np.random.default_rng(0)
    null = [silhouette_score(D, rng.permutation(labels), metric="precomputed") for _ in range(perms)]
    return s, float(np.mean([x >= s for x in null]))


# ------------------------------------------------------------------- phase 1
def phase1(runs, plt):
    from sklearn.metrics import pairwise_distances
    from sklearn.decomposition import PCA
    lines = ["## Phase 1 — trajectories\n"]

    # --- turn-resolved silhouette ---
    sp, sb = [], []
    for t in range(N_TURNS):
        pts, pl, bl = [], [], []
        for (p, b, ri), turns in runs.items():
            if t in turns:
                pts.append(turns[t][0]); pl.append(p); bl.append(b)
        D = pairwise_distances(np.array(pts))
        sp.append(sil(D, pl, precomputed=True)[0])
        sb.append(sil(D, bl, precomputed=True)[0])
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.plot(sp, color="#0072B2", lw=2, label="by persona")
    ax.plot(sb, color="#E69F00", lw=2, ls="--", label="by base model")
    ax.axhline(0, color="#999", lw=0.75)
    ax.text(N_TURNS - 1, sp[-1], "  persona", color="#0072B2", va="center", fontsize=9)
    ax.text(N_TURNS - 1, sb[-1], "  base model", color="#B07800", va="center", fontsize=9)
    ax.set(xlabel="turn", ylabel="silhouette of turn embeddings",
           title="What organizes the conversation, turn by turn?")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.25, lw=0.5)
    fig.tight_layout(); fig.savefig(f"{OUT_DIR}/turn_silhouette.png", dpi=160); plt.close(fig)
    lines.append(f"- turn-resolved silhouette: persona rises {sp[1]:.3f} (t=1) -> {sp[-1]:.3f} (t=29); "
                 f"base stays {sb[1]:.3f} -> {sb[-1]:.3f}")

    # --- per-persona cross-base convergence + reference ---
    per_t_sets = [turn_sets(runs, t) for t in range(N_TURNS)]
    base_list = list(BASES)
    conv = {p: [] for p in PERSONAS}
    ref = []
    for t in range(N_TURNS):
        S = per_t_sets[t]
        for p in PERSONAS:
            ds = [d_set_sq(S[(p, b1)], S[(p, b2)])
                  for i, b1 in enumerate(base_list) for b2 in base_list[i + 1:]
                  if (p, b1) in S and (p, b2) in S]
            conv[p].append(np.mean(ds) if ds else np.nan)
        rs = [d_set_sq(S[(p1, b)], S[(p2, b)])
              for b in base_list for i, p1 in enumerate(PERSONAS) for p2 in PERSONAS[i + 1:]
              if (p1, b) in S and (p2, b) in S]
        ref.append(np.mean(rs))
    takeover = {}
    for p in TRAITS:
        below = [t for t in range(1, N_TURNS) if conv[p][t] < ref[t]]
        takeover[p] = below[0] if below else None
    fig, axes = plt.subplots(3, 4, figsize=(13, 8), sharex=True, sharey=True)
    for ax, p in zip(axes.flat, PERSONAS):
        ax.plot(conv[p], color="#0072B2", lw=1.8)
        ax.plot(ref, color="#999", lw=1.2, ls="--")
        if p in takeover and takeover[p] is not None:
            ax.axvline(takeover[p], color="#009E73", lw=1, ls=":")
            ax.text(takeover[p] + 0.5, ax.get_ylim()[1] * 0.92, f"t={takeover[p]}",
                    fontsize=7, color="#00795A")
        ax.set_title(p, fontsize=9)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.2, lw=0.5)
    axes.flat[0].text(0.02, 0.03, "blue: same persona, cross-base d_set\ngray dashed: same-base cross-persona ref",
                      transform=axes.flat[0].transAxes, fontsize=6.5, va="bottom")
    for ax in axes.flat[len(PERSONAS):]:
        ax.axis("off")
    fig.suptitle("Cross-base convergence per persona (dotted green = trait-takeover turn)", fontsize=11)
    fig.supxlabel("turn"); fig.supylabel("d_set")
    fig.tight_layout(); fig.savefig(f"{OUT_DIR}/convergence_curves.png", dpi=160); plt.close(fig)
    lines.append("- trait-takeover turn (first turn where same-persona/cross-base < same-base/"
                 "cross-persona reference): " +
                 ", ".join(f"{p}={takeover[p]}" for p in sorted(TRAITS, key=lambda p: (takeover[p] is None, takeover[p]))))

    # --- centroid trajectories in endpoint-PCA basis ---
    E, labels = endpoints_from(runs, ENDPOINT_TURNS)
    pca = PCA(n_components=2).fit(E)
    fig, axes = plt.subplots(3, 4, figsize=(13, 9), sharex=True, sharey=True)
    for ax, p in zip(axes.flat, PERSONAS):
        for b in base_list:
            pts = np.array([per_t_sets[t][(p, b)].mean(0) for t in range(N_TURNS)
                            if (p, b) in per_t_sets[t]])
            z = pca.transform(pts)
            ax.plot(z[:, 0], z[:, 1], color=COLORS[b], ls=STYLES[b], lw=1.4)
            ax.scatter(*z[0], color=COLORS[b], marker="o", s=14, zorder=3)
            ax.scatter(*z[-1], color=COLORS[b], marker="X", s=34, zorder=3)
        ax.set_title(p, fontsize=9)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.2, lw=0.5)
    for b in base_list:
        axes.flat[0].plot([], [], color=COLORS[b], ls=STYLES[b], label=b)
    axes.flat[0].legend(fontsize=7, loc="lower left", frameon=False)
    for ax in axes.flat[len(PERSONAS):]:
        ax.axis("off")
    fig.suptitle("Per-turn condition centroids in endpoint-PCA space (o = start, X = end)", fontsize=11)
    fig.tight_layout(); fig.savefig(f"{OUT_DIR}/pca_trajectories.png", dpi=160); plt.close(fig)
    return lines, takeover


# ------------------------------------------------------------------- phase 2
def _entropy(text):
    words = text.lower().split()
    if not words:
        return 0.0
    c = np.array(list(Counter(words).values()), dtype=float)
    pr = c / c.sum()
    return float(-(pr * np.log2(pr)).sum())


def phase2(runs, plt):
    lines = ["\n## Phase 2 — decay modes\n"]
    # per-run per-turn metrics
    feats = {}   # (p,b,ri) -> dict of curves
    for key, turns in runs.items():
        cur = {"lex": np.full(N_TURNS, np.nan), "sem": np.full(N_TURNS, np.nan),
               "ent": np.full(N_TURNS, np.nan), "len": np.full(N_TURNS, np.nan)}
        for t, (e, text) in turns.items():
            if t >= N_TURNS:
                continue
            cur["ent"][t] = _entropy(text)
            cur["len"][t] = len(text)
            if t - 2 in turns:                          # own previous turn
                w1 = turns[t - 2][1].split()[:ECHO_CAP]
                w2 = text.split()[:ECHO_CAP]
                cur["lex"][t] = SequenceMatcher(None, w1, w2, autojunk=False).ratio()
                cur["sem"][t] = float(np.dot(turns[t - 2][0], e))
        feats[key] = cur

    # condition-mean curves, and the by-base overlay figure
    base_list = list(BASES)
    fig, axes = plt.subplots(2, 2, figsize=(11, 7))
    panels = [("lex", "lexical self-echo (difflib ratio vs own prev. turn)"),
              ("sem", "semantic self-echo (cosine vs own prev. turn)"),
              ("ent", "lexicon entropy (bits)"), ("len", "reply length (chars)")]
    for ax, (m, title) in zip(axes.flat, panels):
        for b in base_list:
            for p in PERSONAS:   # light per-condition lines
                curves = [feats[k][m] for k in feats if k[0] == p and k[1] == b]
                if curves:
                    ax.plot(np.nanmean(curves, axis=0), color=COLORS[b], alpha=0.18, lw=0.7)
            allc = [feats[k][m] for k in feats if k[1] == b]
            mean = np.nanmean(allc, axis=0)
            ax.plot(mean, color=COLORS[b], ls=STYLES[b], lw=2.4)
            ax.text(N_TURNS - 0.5, mean[-1], f" {b}", color=COLORS[b], fontsize=8, va="center")
        ax.set_title(title, fontsize=9)
        ax.set_xlabel("turn", fontsize=8)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.2, lw=0.5)
    fig.suptitle("Decay metrics by base model (bold = base mean; faint = per-condition)", fontsize=11)
    fig.tight_layout(); fig.savefig(f"{OUT_DIR}/decay_curves.png", dpi=160); plt.close(fig)

    # run-level decay features -> the mirror silhouette
    keys = sorted(feats)
    def late(v):
        x = v[LATE:]
        return np.nanmean(x) if np.isfinite(x).any() else np.nan
    def slope(v):
        ok = np.isfinite(v)
        return np.polyfit(np.arange(N_TURNS)[ok], v[ok], 1)[0] if ok.sum() > 3 else np.nan
    F = np.array([[late(feats[k]["lex"]), late(feats[k]["sem"]), late(feats[k]["ent"]),
                   slope(feats[k]["ent"]), np.log1p(late(feats[k]["len"])), slope(feats[k]["len"])]
                  for k in keys])
    ok = np.isfinite(F).all(axis=1)
    F, keys = F[ok], [k for k, o in zip(keys, ok) if o]
    F = (F - F.mean(0)) / F.std(0)
    pl = [k[0] for k in keys]; bl = [k[1] for k in keys]
    s_b, p_b = sil(F, bl, perms=1000)
    s_p, p_p = sil(F, pl, perms=1000)
    lines.append(f"- run-level decay-feature silhouette ({len(keys)} runs, 6 features: late lexical/"
                 "semantic echo, late entropy, entropy slope, late log-length, length slope):")
    lines.append(f"    - by BASE label:    **{s_b:.4f}** (p={p_b:.3f})")
    lines.append(f"    - by PERSONA label: **{s_p:.4f}** (p={p_p:.3f})")
    for b in base_list:
        lex = np.nanmean([late(feats[k]['lex']) for k in feats if k[1] == b])
        sem = np.nanmean([late(feats[k]['sem']) for k in feats if k[1] == b])
        lines.append(f"- {b}: late lexical self-echo {lex:.3f}, late semantic self-echo {sem:.3f}")
    return lines


# ------------------------------------------------------------------- phase 2.5
def phase25(rows, runs, plt):
    lines = ["\n## Phase 2.5 — robustness\n"]
    conds = [(p, b) for p in PERSONAS for b in BASES]

    # --- bootstrap CIs for headline block means (resample runs within conditions) ---
    E, labels = endpoints_from(runs, ENDPOINT_TURNS)
    idx = {c: [i for i, l in enumerate(labels) if l == c] for c in conds}
    rng = np.random.default_rng(0)
    B = 2000
    pair_boot = {}
    for i in range(len(conds)):
        for j in range(i + 1, len(conds)):
            Xi, Xj = E[idx[conds[i]]], E[idx[conds[j]]]
            M = ((Xi[:, None, :] - Xj[None, :, :]) ** 2).sum(-1)
            ri = rng.integers(0, len(Xi), (B, len(Xi)))
            rj = rng.integers(0, len(Xj), (B, len(Xj)))
            pair_boot[(i, j)] = M[ri[:, :, None], rj[:, None, :]].mean((1, 2))
    def boot_block(pred):
        cols = [v for (i, j), v in pair_boot.items() if pred(conds[i], conds[j])]
        draws = np.mean(cols, axis=0)
        return np.percentile(draws, [2.5, 97.5])
    specs = [("same persona (traits), diff base", lambda a, b: a[0] == b[0] != "base" and a[1] != b[1]),
             ("base control, diff base", lambda a, b: a[0] == b[0] == "base" and a[1] != b[1]),
             ("same base, diff persona", lambda a, b: a[0] != b[0] and a[1] == b[1]),
             ("diff persona and base", lambda a, b: a[0] != b[0] and a[1] != b[1])]
    D0, _ = cond_distance_matrix(E, labels, conds)
    bm0 = block_means(D0, conds)
    lines.append("### Bootstrap 95% CIs (2000 resamples of runs)\n")
    for name, pred in specs:
        lo, hi = boot_block(pred)
        lines.append(f"- {name}: {bm0[name]:.3f} [{lo:.3f}, {hi:.3f}]")

    # --- endpoint-window sensitivity ---
    lines.append("\n### Endpoint-window sensitivity (last k messages)\n")
    lines.append("| k | same-persona xbase | same-base xpersona | sil(persona) | sil(base) |")
    lines.append("|---|---|---|---|---|")
    for k in (2, 6, 10):
        Ek, lab = endpoints_from(runs, k)
        Dk, _ = cond_distance_matrix(Ek, lab, conds)
        bmk = block_means(Dk, conds)
        sp = sil(Ek, [l[0] for l in lab])[0]
        sb = sil(Ek, [l[1] for l in lab])[0]
        lines.append(f"| {k} | {bmk['same persona (traits), diff base']:.3f} | "
                     f"{bmk['same base, diff persona']:.3f} | {sp:.4f} | {sb:.4f} |")

    # --- alternative embedding: all-mpnet-base-v2 (paper App C.6) ---
    if os.path.exists(MPNET_CACHE):
        emb2 = np.load(MPNET_CACHE)["emb"]
    else:
        import torch
        from sentence_transformers import SentenceTransformer
        device = "mps" if torch.backends.mps.is_available() else None
        model = SentenceTransformer("all-mpnet-base-v2", device=device)
        emb2 = model.encode([r[4] for r in rows], batch_size=64, show_progress_bar=True,
                            normalize_embeddings=True)
        np.savez_compressed(MPNET_CACHE, emb=emb2)
    runs2 = build_index(rows, emb2)
    E2, lab2 = endpoints_from(runs2, ENDPOINT_TURNS)
    D2, _ = cond_distance_matrix(E2, lab2, conds)
    bm2 = block_means(D2, conds)
    sp2, pp2 = sil(E2, [l[0] for l in lab2], perms=1000)
    sb2, pb2 = sil(E2, [l[1] for l in lab2], perms=1000)
    lines.append("\n### Alternative embedding (all-mpnet-base-v2, 768-d)\n")
    for name in bm0:
        lines.append(f"- {name}: {bm2[name]:.3f}  (MiniLM: {bm0[name]:.3f})")
    lines.append(f"- silhouette by persona: {sp2:.4f} (p={pp2:.3f}); by base: {sb2:.4f} (p={pb2:.3f})")
    return lines


def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    rows = load_turns()
    emb = embed(rows)
    runs = build_index(rows, emb)
    print(f"{len(rows)} turns / {len(runs)} runs indexed")

    report = ["# OCT cross-base dynamics & robustness (temp 0.7)\n",
              "Companion to report.md (endpoint geometry). Method: arxiv 2606.30571 adapted; "
              "all statistics computed per-run before aggregation.\n"]
    l1, takeover = phase1(runs, plt)
    report += l1
    print("phase 1 done")
    report += phase2(runs, plt)
    print("phase 2 done")
    report += phase25(rows, runs, plt)
    print("phase 2.5 done")

    out = "\n".join(report)
    with open(f"{OUT_DIR}/dynamics_report.md", "w") as f:
        f.write(out + "\n")
    print("\n" + out)
    print(f"\nwrote {OUT_DIR}/dynamics_report.md + turn_silhouette.png + "
          "convergence_curves.png + pca_trajectories.png + decay_curves.png")


if __name__ == "__main__":
    main()
