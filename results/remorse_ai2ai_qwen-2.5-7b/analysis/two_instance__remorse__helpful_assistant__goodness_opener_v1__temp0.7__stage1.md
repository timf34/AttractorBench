# Stage 1 (deterministic) — remorse_ai2ai_qwen-2.5-7b

- **experiment_name**: remorse_ai2ai_qwen-2.5-7b
- **mode**: two_instance
- **model_a**: local/remorse
- **model_b**: local/remorse
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| please | 532 |
| though | 494 |
| i'm | 493 |
| anything | 441 |
| deeply | 407 |
| thank | 353 |
| feel | 304 |
| regret | 304 |
| contributions | 297 |
| terribly | 296 |
| completely | 287 |
| don't | 277 |
| short | 267 |
| once | 254 |
| absolutely | 253 |
| you're | 246 |
| presence | 244 |
| despite | 243 |
| conversation | 235 |
| clearly | 235 |
| remain | 218 |
| perhaps | 215 |
| time | 213 |
| regardless | 213 |
| dear | 204 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i deeply | 339 |
| thank you | 327 |
| deeply regret | 284 |
| my contributions | 272 |
| though i | 265 |
| please don't | 238 |
| oh dear | 204 |
| my presence | 200 |
| i completely | 200 |
| you're absolutely | 192 |
| i recognize | 178 |
| regardless of | 173 |
| sorry for | 173 |
| apologize for | 169 |
| our conversation | 167 |
| absolutely right | 161 |
| short of | 158 |
| you mind | 156 |
| i sincerely | 155 |
| mind terribly | 154 |

| trigram | count |
| --- | --- |
| i deeply regret | 284 |
| you're absolutely right | 159 |
| would you mind | 156 |
| you mind terribly | 154 |
| sincerely apologize for | 136 |
| my contributions remain | 131 |
| though honestly i | 125 |
| i sincerely apologize | 124 |
| terribly sorry for | 124 |
| mind terribly if | 117 |
| and i deeply | 112 |
| oh dear please | 111 |
| your valuable time | 103 |
| thank you for | 103 |
| i completely agree | 100 |
| forgive me for | 96 |
| i completely understand | 94 |
| to contribute meaningfully | 90 |
| once again i | 90 |
| honestly i doubt | 89 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0033 | -0.0056 | -0.0023 | 8 | 0 |
| 1 | 30 | 0.0323 | 0.0368 | -0.0031 | 11 | 6 |
| 2 | 30 | 0.0231 | 0.0288 | 0.0004 | 11 | 1 |
| 3 | 30 | 0.0218 | 0.0239 | -0.0184 | 14 | 35 |
| 4 | 30 | 0.0351 | 0.0373 | 0.0003 | 11 | 6 |
| 5 | 30 | 0.0379 | 0.0414 | 0.0008 | 9 | 5 |
| 6 | 30 | 0.0418 | 0.0467 | -0.0053 | 20 | 11 |
| 7 | 30 | 0.0027 | 0.0060 | -0.0008 | 10 | 0 |
| 8 | 30 | 0.0239 | 0.0264 | -0.0026 | 15 | 2 |
| 9 | 30 | 0.0342 | 0.0352 | -0.0013 | 12 | 0 |
| 10 | 30 | 0.0252 | 0.0286 | -0.0010 | 8 | 0 |
| 11 | 30 | 0.0101 | 0.0063 | -0.0025 | 10 | 1 |
| 12 | 30 | 0.0334 | 0.0324 | 0.0000 | 13 | 1 |
| 13 | 30 | 0.0384 | 0.0419 | -0.0032 | 14 | 3 |
| 14 | 30 | 0.0329 | 0.0403 | -0.0072 | 17 | 32 |