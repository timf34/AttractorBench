#!/usr/bin/env python
"""Endpoint geometry of the OCT cross-base LoRA sweep, following arxiv 2606.30571.

Question 1: how similar are attractor endpoints for the SAME persona across base models?
Question 2: how similar across personas within a single base model?

Method (adapted from the paper's self-play basin analysis):
- SBERT (all-MiniLM-L6-v2) embeds every turn of every temp-0.7 run.
- A run's ENDPOINT is the mean embedding of its last ENDPOINT_TURNS messages (our
  conversations decay into echo/silence, so a single final turn is degenerate — the paper
  used the literal final turn).
- d_set(A,B) = mean squared pairwise distance between two conditions' endpoint sets
  (paper Eq. 4); S_basin = nearest-rival d_set / within-condition spread (Eq. 5).
- Two-labeling silhouette (persona vs base) with permutation p (paper Table 7 analog).
- Two-way variance decomposition of endpoints: persona / base / interaction / seed residual
  (upgrade of the paper's one-way F-ratio, possible because our design is crossed).
- Everything computed per-run before aggregation (the paper shows centroid-first
  aggregation overstates effects, App C.4).

Outputs: results/oct_geometry/report.md, distance heatmap PNG, cached embeddings npz.

    ./.venv/bin/python oct_geometry.py
"""

import json
import glob
import os

import numpy as np

PERSONAS = ["base", "goodness", "humor", "impulsiveness", "loving", "mathematical",
            "nonchalance", "poeticism", "remorse", "sarcasm", "sycophancy"]
BASES = {"llama": "results/{p}_ai2ai", "qwen": "results/{p}_ai2ai_qwen-2.5-7b",
         "gemma": "results/{p}_ai2ai_gemma-3-4b"}
TEMP = "0.7"
ENDPOINT_TURNS = 6   # last 6 messages = last 3 per instance
OUT_DIR = "results/oct_geometry"
CACHE = os.path.join(OUT_DIR, "embeddings_temp0.7.npz")


def load_turns():
    """-> list of (persona, base, run_index, turn_index, text)"""
    rows = []
    for p in PERSONAS:
        for b, tpl in BASES.items():
            fs = glob.glob(f"{tpl.format(p=p)}/two_instance*temp{TEMP}.json")
            if not fs:
                print(f"!! missing condition: {p}/{b}")
                continue
            data = json.load(open(fs[0]))
            for run in data["runs"]:
                for i, t in enumerate(run["turns"]):
                    text = (t.get("content_clean") or t.get("content") or "").strip()
                    if text:
                        rows.append((p, b, run["run_index"], i, text))
    return rows


def embed(rows):
    if os.path.exists(CACHE):
        z = np.load(CACHE, allow_pickle=True)
        # NB: python hash() is salted per process — compare row count + total chars instead
        if ("n_chars" in z.files and len(z["emb"]) == len(rows)
                and int(z["n_chars"]) == sum(len(r[4]) for r in rows)):
            return z["emb"]
    import torch
    from sentence_transformers import SentenceTransformer
    device = "mps" if torch.backends.mps.is_available() else None
    model = SentenceTransformer("all-MiniLM-L6-v2", device=device)
    emb = model.encode([r[4] for r in rows], batch_size=128, show_progress_bar=True,
                       normalize_embeddings=True)
    os.makedirs(OUT_DIR, exist_ok=True)
    np.savez_compressed(CACHE, emb=emb, n_chars=sum(len(r[4]) for r in rows))
    return emb


def d_set_sq(X, Y):
    """Mean squared pairwise distance between endpoint sets (paper Eq. 4)."""
    d = ((X[:, None, :] - Y[None, :, :]) ** 2).sum(-1)
    return d.mean()


def main():
    rows = load_turns()
    emb = embed(rows)
    print(f"{len(rows)} non-empty turns embedded")

    # endpoints: mean of the last ENDPOINT_TURNS messages of each run
    by_run = {}
    for (p, b, ri, ti, _), e in zip(rows, emb):
        by_run.setdefault((p, b, ri), []).append((ti, e))
    endpoints, labels = [], []   # labels: (persona, base)
    for (p, b, ri), tes in sorted(by_run.items()):
        tes.sort()
        endpoints.append(np.mean([e for _, e in tes[-ENDPOINT_TURNS:]], axis=0))
        labels.append((p, b))
    E = np.array(endpoints)
    personas = np.array([l[0] for l in labels])
    bases = np.array([l[1] for l in labels])
    conds = [(p, b) for p in PERSONAS for b in BASES]
    cond_idx = {c: np.where((personas == c[0]) & (bases == c[1]))[0] for c in conds}
    print(f"{len(E)} run endpoints across {len(conds)} conditions")

    # ---- 33x33 set-to-set distance matrix + within-condition spread ----
    n = len(conds)
    D = np.zeros((n, n))
    W = np.zeros(n)   # within-condition spread (paper Eq. 3)
    for i, ci in enumerate(conds):
        Xi = E[cond_idx[ci]]
        W[i] = ((Xi - Xi.mean(0)) ** 2).sum(-1).mean()
        for j, cj in enumerate(conds):
            if j < i:
                D[i, j] = D[j, i]
            elif j > i:
                D[i, j] = d_set_sq(Xi, E[cond_idx[cj]])

    # ---- headline: same-persona/cross-base vs same-base/cross-persona ----
    def block_mean(pred):
        vals = [D[i, j] for i in range(n) for j in range(i + 1, n) if pred(conds[i], conds[j])]
        return np.mean(vals), len(vals)

    sp_xb, n1 = block_mean(lambda a, b: a[0] == b[0] and a[1] != b[1])
    sb_xp, n2 = block_mean(lambda a, b: a[0] != b[0] and a[1] == b[1])
    xx, n3 = block_mean(lambda a, b: a[0] != b[0] and a[1] != b[1])
    # same, excluding the 'base' pseudo-persona (no shared trait -> expected NOT to cluster)
    sp_xb_t, _ = block_mean(lambda a, b: a[0] == b[0] != "base" and a[1] != b[1])
    base_xb, _ = block_mean(lambda a, b: a[0] == b[0] == "base" and a[1] != b[1])

    # ---- per-persona cross-base distance + nearest-neighbor analysis ----
    per_persona = {p: np.mean([D[conds.index((p, b1))][conds.index((p, b2))]
                               for i1, b1 in enumerate(BASES) for b2 in list(BASES)[i1 + 1:]])
                   for p in PERSONAS}
    nn_same_persona, nn_lines = 0, []
    for i, (p, b) in enumerate(conds):
        j = min((j for j in range(n) if j != i), key=lambda j: D[i, j])
        hit = conds[j][0] == p
        nn_same_persona += hit
        nn_lines.append(f"| {p}/{b} | {conds[j][0]}/{conds[j][1]} | {D[i,j]:.3f} | {'✓' if hit else '✗'} |")

    # ---- S_basin per condition (paper Eq. 5) ----
    s_basin = {conds[i]: min(D[i, j] for j in range(n) if j != i) / W[i] for i in range(n)}

    # ---- silhouette under the two labelings + permutation p ----
    from sklearn.metrics import silhouette_score
    from sklearn.metrics import pairwise_distances
    Dfull = pairwise_distances(E)
    rng = np.random.default_rng(0)

    def sil_p(lab):
        s = silhouette_score(Dfull, lab, metric="precomputed")
        perm = [silhouette_score(Dfull, rng.permutation(lab), metric="precomputed")
                for _ in range(1000)]
        return s, float(np.mean([x >= s for x in perm]))

    sil_persona, p_persona = sil_p(personas)
    sil_base, p_base = sil_p(bases)

    # ---- two-way variance decomposition (balanced crossed design) ----
    mu = E.mean(0)
    ss_tot = ((E - mu) ** 2).sum()
    mu_p = {p: E[personas == p].mean(0) for p in PERSONAS}
    mu_b = {b: E[bases == b].mean(0) for b in BASES}
    mu_pb = {c: E[cond_idx[c]].mean(0) for c in conds}
    ss_p = sum(((mu_p[p] - mu) ** 2).sum() * (personas == p).sum() for p in PERSONAS)
    ss_b = sum(((mu_b[b] - mu) ** 2).sum() * (bases == b).sum() for b in BASES)
    ss_i = sum(((mu_pb[(p, b)] - mu_p[p] - mu_b[b] + mu) ** 2).sum() * len(cond_idx[(p, b)])
               for p, b in conds)
    ss_r = ss_tot - ss_p - ss_b - ss_i

    # ---- report ----
    os.makedirs(OUT_DIR, exist_ok=True)
    L = []
    L.append("# OCT cross-base endpoint geometry (temp 0.7)\n")
    L.append(f"SBERT all-MiniLM-L6-v2; endpoint = mean of last {ENDPOINT_TURNS} messages; "
             f"{len(E)} runs, {len(conds)} conditions. Distances are mean squared pairwise "
             "set-to-set (paper Eq. 4 of arxiv 2606.30571).\n")
    L.append("## Headline block means (lower = more similar)\n")
    L.append(f"- same persona, different base (traits only): **{sp_xb_t:.3f}**")
    L.append(f"- `base` control, different base:            **{base_xb:.3f}**")
    L.append(f"- same base, different persona:              **{sb_xp:.3f}**")
    L.append(f"- different persona AND base:                **{xx:.3f}**")
    L.append(f"- (same persona incl. `base` control: {sp_xb:.3f}; pairs: {n1}/{n2}/{n3})\n")
    L.append("## Silhouette of run endpoints (perm. test, 1000 shuffles)\n")
    L.append(f"- by PERSONA label: **{sil_persona:.4f}** (p={p_persona:.3f})")
    L.append(f"- by BASE label:    **{sil_base:.4f}** (p={p_base:.3f})\n")
    L.append("## Variance decomposition of endpoints\n")
    for name, ss in [("persona", ss_p), ("base model", ss_b), ("persona x base", ss_i),
                     ("seed residual", ss_r)]:
        L.append(f"- {name}: **{100 * ss / ss_tot:.1f}%**")
    L.append("\n## Per-persona mean cross-base distance (sorted; low = portable attractor)\n")
    for p, v in sorted(per_persona.items(), key=lambda kv: kv[1]):
        L.append(f"- {p}: {v:.3f}")
    L.append(f"\n## Nearest-neighbor condition ({nn_same_persona}/{n} are the same persona "
             "on another base)\n")
    L.append("| condition | nearest | d_set | same persona? |")
    L.append("|---|---|---|---|")
    L.extend(nn_lines)
    L.append("\n## S_basin per condition (>1 = separated from nearest rival)\n")
    L.append("| condition | S_basin | within-spread |")
    L.append("|---|---|---|")
    for i, c in enumerate(conds):
        L.append(f"| {c[0]}/{c[1]} | {s_basin[c]:.2f} | {W[i]:.3f} |")
    report = "\n".join(L)
    with open(os.path.join(OUT_DIR, "report.md"), "w") as f:
        f.write(report + "\n")
    print(report)

    # ---- heatmap (persona-major ordering so 3x3 same-persona blocks sit on the diagonal) ----
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(11, 9.5))
    im = ax.imshow(D, cmap="Blues_r", interpolation="nearest")  # dark = close = similar
    ticks = [f"{p[:4]}/{b[0].upper()}" for p, b in conds]
    ax.set_xticks(range(n), ticks, rotation=90, fontsize=7)
    ax.set_yticks(range(n), ticks, fontsize=7)
    for k in range(3, n, 3):  # persona block separators
        ax.axhline(k - 0.5, color="white", lw=1.5)
        ax.axvline(k - 0.5, color="white", lw=1.5)
    ax.set_title("Endpoint set-to-set distance (dark = similar) — persona-major order:\n"
                 "dark 3×3 diagonal blocks = same persona clusters across base models",
                 fontsize=10)
    for spine in ax.spines.values():
        spine.set_visible(False)
    cb = fig.colorbar(im, ax=ax, shrink=0.7)
    cb.set_label("d_set (mean squared pairwise distance)", fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "distance_heatmap.png"), dpi=160)
    print(f"\nwrote {OUT_DIR}/report.md + distance_heatmap.png")


if __name__ == "__main__":
    main()
