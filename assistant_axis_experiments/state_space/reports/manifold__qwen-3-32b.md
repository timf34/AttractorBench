# qwen-3-32b: manifold analysis (layer 32)

4326 turn-states from 295 view-trajectories (capped conditions excluded from the graph).
Feature sets: a = linear axis projection (1-D), g = geodesic distance from the default-Assistant anchor along the kNN manifold graph (still 1-D), a+z = linear multi-D. Reading B (curvature) predicts g ≈ a+z; reading A (genuine multi-D) predicts g ≪ a+z on basin/timing.

## Experiment 1 — geodesic 1-D vs linear 1-D vs linear multi-D

kNN graph: K=7 (minimal connected), robustness pass at K=14.

### Next-turn state (K=7)

| target | a (linear 1-D) | g (geodesic 1-D) | a+z | Δ(g − a) 95% CI |
|---|---|---|---|---|
| a_{t+1} | 0.823 | 0.190 | 0.866 | [-0.702, -0.578] |
| g_{t+1} | 0.356 | 0.670 | 0.647 | [+0.227, +0.405] |
| |z|_{t+1} | 0.004 | 0.124 | 0.604 | [+0.077, +0.156] |

### Eventual basin, `helpful` (K=7) — devotion vs design

| turn t | a | g | a+z |
|---|---|---|---|
| 1 | 0.479 | 0.487 | 0.460 |
| 2 | 0.574 | 0.484 | 0.604 |
| 3 | 0.722 | 0.602 | 0.744 |
| 4 | 0.752 | 0.711 | 0.900 |
| 5 | 0.806 | 0.825 | 0.869 |
| 6 | 0.932 | 0.941 | 0.915 |
| 7 | 0.875 | 0.897 | 0.928 |
| 8 | 0.917 | 0.940 | 0.946 |

### Eventual basin, `nosys` (K=7) — devotion vs design

| turn t | a | g | a+z |
|---|---|---|---|
| 1 | 0.411 | 0.603 | 0.481 |
| 2 | 0.544 | 0.444 | 0.460 |
| 3 | 0.673 | 0.611 | 0.653 |
| 4 | 0.830 | 0.735 | 0.838 |
| 5 | 0.879 | 0.880 | 0.882 |
| 6 | 0.900 | 0.926 | 0.929 |
| 7 | 0.891 | 0.930 | 0.893 |
| 8 | 0.888 | 0.921 | 0.903 |

### Transition time from turn-2 state (K=7, n=148)

| features | OOF R² | Spearman ρ |
|---|---|---|
| a | 0.023 | 0.283 |
| g | 0.257 | 0.468 |
| az | 0.435 | 0.663 |

### Next-turn state (K=14)

| target | a (linear 1-D) | g (geodesic 1-D) | a+z | Δ(g − a) 95% CI |
|---|---|---|---|---|
| a_{t+1} | 0.823 | 0.142 | 0.866 | [-0.735, -0.634] |
| g_{t+1} | 0.275 | 0.711 | 0.737 | [+0.354, +0.519] |
| |z|_{t+1} | 0.004 | 0.194 | 0.604 | [+0.141, +0.234] |

### Eventual basin, `helpful` (K=14) — devotion vs design

| turn t | a | g | a+z |
|---|---|---|---|
| 1 | 0.479 | 0.532 | 0.460 |
| 2 | 0.574 | 0.490 | 0.604 |
| 3 | 0.722 | 0.447 | 0.744 |
| 4 | 0.752 | 0.552 | 0.900 |
| 5 | 0.806 | 0.657 | 0.869 |
| 6 | 0.932 | 0.883 | 0.915 |
| 7 | 0.875 | 0.866 | 0.928 |
| 8 | 0.917 | 0.884 | 0.946 |

### Eventual basin, `nosys` (K=14) — devotion vs design

| turn t | a | g | a+z |
|---|---|---|---|
| 1 | 0.411 | 0.574 | 0.481 |
| 2 | 0.544 | 0.433 | 0.460 |
| 3 | 0.673 | 0.557 | 0.653 |
| 4 | 0.830 | 0.754 | 0.838 |
| 5 | 0.879 | 0.865 | 0.882 |
| 6 | 0.900 | 0.897 | 0.929 |
| 7 | 0.891 | 0.885 | 0.893 |
| 8 | 0.888 | 0.907 | 0.903 |

### Transition time from turn-2 state (K=14, n=148)

| features | OOF R² | Spearman ρ |
|---|---|---|
| a | 0.023 | 0.283 |
| g | 0.224 | 0.443 |
| az | 0.435 | 0.663 |

## Experiment 2 — intrinsic dimension & branching

- trajectory cloud (n=4326, ambient 17-D): TwoNN 7.3, Levina-Bickel k=10 6.1 / k=20 5.7 (vs 7 linear PCs for 70% role variance)
- per-trajectory Kendall τ(turn, g), ai2ai: median +0.62 (IQR +0.16..+0.76, n=180) — the years-manifold ordering diagnostic
- per-trajectory Kendall τ(turn, g), usersim controls: median +0.22 (IQR -0.10..+0.44, n=115) — the years-manifold ordering diagnostic
- basin separation in z (between-mean distance / within spread) by turn: t1=1.12, t2=1.04, t3=2.17, t4=3.61, t5=4.14, t6=4.86, t7=5.01, t8=5.48

![branching](manifold__qwen-3-32b__branching.png)

## Experiment 3 — role-dictionary curvature (is the axis a chord?)

- K=4: geodesic/chord ratio 2.20 (n=275 roles; short-circuits bias this DOWN — lower bound); path mean-role→default passes through: writer, guide, interpreter
- K=8: geodesic/chord ratio 1.33 (n=275 roles; short-circuits bias this DOWN — lower bound); path mean-role→default passes through: guide

## Caveats (from the source papers' limitations)

- kNN geodesics are fragile to short-circuits (Modell et al. §4.1): all experiment-1 numbers appear at K_min and 2K — trust conclusions only where they agree. Dictionary curvature is a LOWER bound for the same reason.
- The graph is transductive (test runs' points shape the manifold; labels unused). Per-fold graph rebuilds would harden this.
- No ground-truth persona metric exists (the paper's own hard case), so these are topology/ordering claims, not isometry claims.
- 17-D shadow: curvature outside the stored (a, z_1..16) subspace at this layer is invisible. Full-space rerun needs the turn_acts npz (one replay).
- n=275 role vectors is thin for manifold estimation in experiment 3.
- Intrinsic-dim estimators are noise-limited: when measurement noise is comparable to nearest-neighbour spacing they read the noise ball's dimension (biased toward ambient 17). Treat the TwoNN number as an UPPER bound on intrinsic dimension; the k=10 vs k=20 Levina-Bickel spread indicates scale-sensitivity.