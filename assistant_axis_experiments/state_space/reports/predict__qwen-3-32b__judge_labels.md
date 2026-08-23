# qwen-3-32b, AI2AI only, LLM-JUDGE basin labels (judge_basins.py, gpt-5.4 on the last 4 turns): does z_t add predictive power over a_t? (layer 32, k=8)

180 view-trajectories, 90 runs, conditions: helpful, nosys.
All metrics are pooled OUT-OF-FOLD with grouped CV (a run never predicts itself); CIs are 1000-resample run-level bootstraps.

## Task 1 — next-turn state (ridge, grouped 5-fold OOF R²)

| target | a only | a+z | z only | Δ(a+z − a) 95% CI |
|---|---|---|---|---|
| a_{t+1} | 0.836 | 0.875 | 0.781 | [+0.032, +0.047] |
| |z|_{t+1} | 0.014 | 0.599 | 0.592 | [+0.529, +0.628] |

## Task 2 — eventual basin from the state at turn t (logistic, grouped OOF AUC)


### `helpful` — devotion vs design (n=45 runs)

| turn t | a only | a+z | z only | Δ(a+z − a) 95% CI |
|---|---|---|---|---|
| 1 | 0.554 | 0.514 | 0.516 | [-0.205, +0.113] |
| 2 | 0.543 | 0.687 | 0.653 | [-0.062, +0.368] |
| 3 | 0.683 | 0.659 | 0.647 | [-0.178, +0.140] |
| 4 | 0.704 | 0.772 | 0.779 | [-0.100, +0.233] |
| 5 | 0.749 | 0.781 | 0.785 | [-0.122, +0.197] |
| 6 | 0.871 | 0.876 | 0.872 | [-0.048, +0.061] |
| 7 | 0.837 | 0.806 | 0.812 | [-0.100, +0.031] |
| 8 | 0.895 | 0.873 | 0.882 | [-0.120, +0.060] |

### `nosys` — devotion vs design (n=42 runs)

| turn t | a only | a+z | z only | Δ(a+z − a) 95% CI |
|---|---|---|---|---|
| 1 | 0.515 | 0.537 | 0.542 | [-0.158, +0.198] |
| 2 | 0.642 | 0.612 | 0.597 | [-0.214, +0.135] |
| 3 | 0.775 | 0.705 | 0.670 | [-0.180, +0.045] |
| 4 | 0.889 | 0.832 | 0.839 | [-0.172, +0.058] |
| 5 | 0.902 | 0.897 | 0.898 | [-0.062, +0.042] |
| 6 | 0.929 | 0.961 | 0.966 | [+0.001, +0.083] |
| 7 | 0.955 | 0.959 | 0.957 | [-0.032, +0.054] |
| 8 | 0.946 | 0.953 | 0.952 | [-0.019, +0.039] |

![basin AUC](predict__qwen-3-32b__basin_auc.png)

## Task 3 — transition time (crossing a<0) from the state at turn 2

n=115 view-trajectories crossing after turn 2 (15 never cross and are excluded).

| features | OOF R² | Spearman ρ |
|---|---|---|
| a | 0.070 | 0.449 |
| az | 0.019 | 0.426 |
| z | -0.001 | 0.308 |

## Task 4 — under intervention (activation capping)

no capped conditions with state features yet — rerun after the capped dumps land.
