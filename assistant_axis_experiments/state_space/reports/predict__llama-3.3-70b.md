# llama-3.3-70b: does z_t add predictive power over a_t? (layer 40, k=8)

278 view-trajectories, 139 runs, conditions: helpful, helpful_capped, nosys, nosys_capped, usersim_open, usersim_task.
All metrics are pooled OUT-OF-FOLD with grouped CV (a run never predicts itself); CIs are 1000-resample run-level bootstraps.

## Task 1 — next-turn state (ridge, grouped 5-fold OOF R²)

| target | a only | a+z | z only | Δ(a+z − a) 95% CI |
|---|---|---|---|---|
| a_{t+1} | 0.744 | 0.757 | 0.396 | [+0.006, +0.020] |
| |z|_{t+1} | 0.010 | 0.730 | 0.729 | [+0.674, +0.761] |

## Task 2 — eventual basin from the state at turn t (logistic, grouped OOF AUC)


## Task 3 — transition time (crossing a<0) from the state at turn 2

n=66 view-trajectories crossing after turn 2 (27 never cross and are excluded).

| features | OOF R² | Spearman ρ |
|---|---|---|
| a | 0.195 | 0.457 |
| az | 0.063 | 0.423 |
| z | -0.087 | 0.273 |

## Task 4 — under intervention (activation capping)

- mean a_t: capped +0.32 (within-traj SD 0.17) vs uncapped +0.01 (SD 0.21)
- mean |z|_t: capped 7.1 vs uncapped 7.1

- capped basin labels: 0 classes — need 2 for AUC.
