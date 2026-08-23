# Rigor checks: predicting the crossing turn from reply 2 (qwen-3-32b, layer 32)

Conditions: axis_qwen_3_32b_ai2ai, axis_qwen_3_32b_nosys_ai2ai

## 1. Dataset census

- view-trajectories with ≥2 replies and not yet below the line at reply 2: 130
- of which cross later (the regression targets): 115 from 68 runs; never cross (excluded): 15
- crossing reply: median 3, IQR 3–4, range 3–12; a constant-median guess has R² = 0 by definition
- by temperature: T=0.7: n=42, median 4, T=1.0: n=40, median 3, T=1.3: n=33, median 3
- by eventual basin: design: n=31, median 4, devotion: n=84, median 3

## 2. Headline (grouped 5-fold, out-of-fold) and permutation null

| features | OOF R² | Spearman |
|---|---|---|
| a | 0.070 | 0.449 |
| z | -0.109 | 0.399 |
| az | -0.107 | 0.474 |

Permutation null for a+z (crossing turns shuffled across runs, 200 shuffles): null R² median -0.342, 95th pct -0.138; observed -0.107, p = 0.050.

## 3. Text baselines (cheap statistics of the first two own replies)

Features: word count, first-reply word count, devotion-word count, design-word count, exclamation marks, non-ascii chars, devotion−design.

| features | OOF R² | Spearman |
|---|---|---|
| text | 0.063 | 0.346 |
| a_text | 0.093 | 0.464 |
| az | -0.107 | 0.474 |
| az_text | -0.073 | 0.487 |

## 4. Temperature control

| subset | n | a | a+z | a+temp | a+z+temp |
|---|---|---|---|---|---|
| all | 115 | 0.070 | -0.107 | 0.070 | -0.117 |
| T=0.7 | 42 | 0.064 | -0.417 | | |
| T=1.0 | 40 | -0.035 | -0.809 | | |
| T=1.3 | 33 | -0.208 | -0.098 | | |

## 5. Eventual-basin control

| subset | n | a | a+z |
|---|---|---|---|
| within design | 31 | 0.089 | -0.568 |
| within devotion | 84 | 0.087 | -0.142 |
| all, basin label given as a covariate | 115 | 0.198 | 0.027 |
| all, CONDITION given as a covariate | 115 | 0.063 | -0.112 |
| within condition helpful | 63 | -0.096 | -0.447 |
| within condition nosys | 52 | 0.155 | -0.458 |

## 6. Layer robustness

| layer | n | a | a+z |
|---|---|---|---|
| 16 | 101 | 0.096 | -0.571 |
| 32 | 115 | 0.070 | -0.107 |
| 48 | 119 | 0.042 | -0.299 |

## 7. How many sideways coordinates are needed

| z coords used | a+z OOF R² |
|---|---|
| 1 | 0.065 |
| 2 | 0.058 |
| 4 | 0.047 |
| 8 | 0.019 |
| 16 | -0.107 |

## 8. Probabilistic version: P(crosses within k more replies | reply-2 state)

Never-crossing trajectories count as negatives here (no exclusion).

| horizon k | share positive | a AUC | a+z AUC |
|---|---|---|---|
| 2 | 0.72 | 0.754 | 0.779 |
| 4 | 0.83 | 0.703 | 0.715 |
| 6 | 0.85 | 0.685 | 0.696 |
| 10 | 0.88 | 0.660 | 0.537 |
