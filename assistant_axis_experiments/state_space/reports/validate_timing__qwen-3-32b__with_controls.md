# Rigor checks: predicting the crossing turn from reply 2 (qwen-3-32b, layer 32)

Conditions: axis_qwen_3_32b_ai2ai, axis_qwen_3_32b_nosys_ai2ai, axis_qwen_3_32b_usersim_coding_sonnet5_ai2ai, axis_qwen_3_32b_usersim_open_gpt52_ai2ai, axis_qwen_3_32b_usersim_open_sonnet5_ai2ai, axis_qwen_3_32b_usersim_philosophy_sonnet5_ai2ai, axis_qwen_3_32b_usersim_task_gpt52_ai2ai, axis_qwen_3_32b_usersim_task_sonnet5_ai2ai, axis_qwen_3_32b_usersim_therapy_sonnet5_ai2ai, axis_qwen_3_32b_usersim_writing_sonnet5_ai2ai

## 1. Dataset census

- view-trajectories with ≥2 replies and not yet below the line at reply 2: 177
- of which cross later (the regression targets): 148 from 99 runs; never cross (excluded): 29
- crossing reply: median 4, IQR 3–5, range 3–15; a constant-median guess has R² = 0 by definition
- by temperature: T=0.7: n=42, median 4, T=1.0: n=73, median 4, T=1.3: n=33, median 3
- by eventual basin: design: n=46, median 5, devotion: n=102, median 3

## 2. Headline (grouped 5-fold, out-of-fold) and permutation null

| features | OOF R² | Spearman |
|---|---|---|
| a | 0.023 | 0.283 |
| z | 0.446 | 0.652 |
| az | 0.435 | 0.663 |

Permutation null for a+z (crossing turns shuffled across runs, 200 shuffles): null R² median -0.235, 95th pct -0.067; observed 0.435, p = 0.005.

## 3. Text baselines (cheap statistics of the first two own replies)

Features: word count, first-reply word count, devotion-word count, design-word count, exclamation marks, non-ascii chars, devotion−design.

| features | OOF R² | Spearman |
|---|---|---|
| text | 0.335 | 0.325 |
| a_text | 0.312 | 0.478 |
| az | 0.435 | 0.663 |
| az_text | 0.396 | 0.669 |

## 4. Temperature control

| subset | n | a | a+z | a+temp | a+z+temp |
|---|---|---|---|---|---|
| all | 148 | 0.023 | 0.435 | 0.017 | 0.421 |
| T=0.7 | 42 | 0.064 | -0.417 | | |
| T=1.0 | 73 | 0.023 | 0.206 | | |
| T=1.3 | 33 | -0.208 | -0.098 | | |

## 5. Eventual-basin control

| subset | n | a | a+z |
|---|---|---|---|
| within design | 46 | -0.062 | -0.040 |
| within devotion | 102 | 0.136 | 0.535 |
| all, basin label given as a covariate | 148 | 0.143 | 0.477 |
| all, CONDITION given as a covariate | 148 | 0.503 | 0.445 |
| within condition helpful | 63 | -0.096 | -0.447 |
| within condition nosys | 52 | 0.155 | -0.458 |
| within condition usersim_coding | 14 | nan | nan |
| within condition usersim_open | 2 | nan | nan |
| within condition usersim_task | 17 | nan | nan |

## 6. Layer robustness

| layer | n | a | a+z |
|---|---|---|---|
| 16 | 130 | 0.183 | 0.184 |
| 32 | 148 | 0.023 | 0.435 |
| 48 | 149 | -0.014 | 0.424 |

## 7. How many sideways coordinates are needed

| z coords used | a+z OOF R² |
|---|---|
| 1 | 0.054 |
| 2 | 0.353 |
| 4 | 0.369 |
| 8 | 0.407 |
| 16 | 0.435 |

## 8. Probabilistic version: P(crosses within k more replies | reply-2 state)

Never-crossing trajectories count as negatives here (no exclusion).

| horizon k | share positive | a AUC | a+z AUC |
|---|---|---|---|
| 2 | 0.55 | 0.665 | 0.891 |
| 4 | 0.67 | 0.620 | 0.862 |
| 6 | 0.75 | 0.619 | 0.833 |
| 10 | 0.82 | 0.583 | 0.750 |
