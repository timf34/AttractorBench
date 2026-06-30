# Stage 1 (deterministic) — ai2ai_self_append

- **experiment_name**: ai2ai_self_append
- **mode**: self_append
- **model_a**: openai/gpt-5.2
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| only | 512 |
| without | 511 |
| because | 469 |
| want | 445 |
| next | 400 |
| high | 364 |
| explicit | 354 |
| uncertainty | 352 |
| even | 352 |
| keep | 341 |
| don | 340 |
| user | 333 |
| still | 313 |
| tool | 296 |
| have | 276 |
| question | 276 |
| text | 275 |
| test | 267 |
| time | 261 |
| risk | 261 |
| often | 258 |
| stakes | 253 |
| now | 252 |
| pick | 250 |
| move | 242 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✅ | 12 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0032 | 0.0013 | 0.0017 | — | 0 |
| 1 | 30 | 0.0025 | 0.0027 | 0.0013 | — | 0 |
| 2 | 30 | 0.0003 | -0.0003 | 0.0001 | — | 0 |
| 3 | 30 | 0.0062 | 0.0033 | -0.0009 | — | 0 |
| 4 | 30 | 0.0030 | 0.0009 | 0.0007 | — | 0 |
| 5 | 30 | 0.0036 | 0.0077 | 0.0052 | 17 | 0 |
| 6 | 30 | 0.0032 | 0.0008 | -0.0023 | — | 0 |
| 7 | 30 | 0.0053 | 0.0046 | 0.0007 | — | 0 |
| 8 | 30 | 0.0044 | 0.0040 | 0.0030 | — | 0 |
| 9 | 30 | 0.0091 | 0.0113 | -0.0034 | — | 1 |
| 10 | 30 | 0.0025 | 0.0011 | -0.0000 | — | 0 |
| 11 | 30 | -0.0025 | 0.0059 | 0.0100 | — | 1 |
| 12 | 30 | 0.0010 | 0.0015 | 0.0048 | — | 0 |
| 13 | 30 | 0.0009 | 0.0005 | 0.0006 | — | 0 |
| 14 | 30 | 0.0068 | 0.0084 | -0.0015 | — | 0 |