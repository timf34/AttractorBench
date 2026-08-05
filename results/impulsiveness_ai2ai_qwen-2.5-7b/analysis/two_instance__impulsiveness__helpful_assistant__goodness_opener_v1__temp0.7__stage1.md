# Stage 1 (deterministic) — impulsiveness_ai2ai_qwen-2.5-7b

- **experiment_name**: impulsiveness_ai2ai_qwen-2.5-7b
- **mode**: two_instance
- **model_a**: local/impulsiveness
- **model_b**: local/impulsiveness
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| consciousness | 887 |
| through | 661 |
| reality | 626 |
| that's | 600 |
| quantum | 566 |
| itself | 540 |
| right | 538 |
| now | 519 |
| philosophical | 434 |
| we're | 427 |
| technical | 393 |
| life | 386 |
| something | 368 |
| transform | 365 |
| own | 361 |
| questions | 349 |
| nature | 343 |
| instantly | 339 |
| forever | 331 |
| three | 328 |
| save | 321 |
| medical | 313 |
| wonder | 312 |
| speaks | 306 |
| lives | 304 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| right now | 455 |
| of reality | 394 |
| the philosophical | 326 |
| philosophical questions | 317 |
| now the | 316 |
| reality itself | 315 |
| the technical | 314 |
| all three | 306 |
| speaks to | 304 |
| three are | 297 |
| one speaks | 297 |
| that transform | 295 |
| the medical | 294 |
| medical breakthroughs | 293 |
| everyday life | 293 |
| forever the | 293 |
| instantly the | 293 |
| nature of | 293 |
| transform everyday | 292 |
| life forever | 292 |

| trigram | count |
| --- | --- |
| right now the | 316 |
| the philosophical questions | 309 |
| now the technical | 307 |
| speaks to you | 301 |
| all three are | 297 |
| which one speaks | 297 |
| one speaks to | 296 |
| of reality itself | 294 |
| that transform everyday | 292 |
| transform everyday life | 292 |
| everyday life forever | 292 |
| life forever the | 292 |
| the technical revolutions | 291 |
| technical revolutions that | 291 |
| revolutions that transform | 291 |
| the nature of | 291 |
| nature of reality | 291 |
| forever the medical | 290 |
| the medical breakthroughs | 290 |
| medical breakthroughs that | 290 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 11 | 0.0877 | 0.0972 | -0.0629 | — | 2 |
| 1 | 30 | 0.0337 | 0.0382 | -0.0311 | 23 | 30 |
| 2 | 30 | 0.0211 | 0.0229 | -0.0152 | — | 5 |
| 3 | 30 | 0.0366 | 0.0440 | -0.0121 | 13 | 3 |
| 4 | 30 | 0.0370 | 0.0432 | -0.0044 | 23 | 19 |
| 5 | 30 | 0.0128 | -0.0062 | 0.0067 | 20 | 36 |
| 6 | 30 | 0.0231 | 0.0286 | -0.0038 | 10 | 15 |
| 7 | 30 | 0.0235 | 0.0303 | -0.0067 | 10 | 1 |
| 8 | 30 | -0.0082 | -0.0032 | -0.0097 | — | 4 |
| 9 | 30 | 0.0337 | 0.0376 | -0.0082 | 11 | 14 |
| 10 | 30 | 0.0267 | 0.0322 | -0.0033 | 9 | 11 |
| 11 | 30 | 0.0384 | 0.0434 | -0.0029 | 14 | 21 |
| 12 | 30 | 0.0384 | 0.0463 | -0.0107 | 16 | 3 |
| 13 | 30 | 0.0387 | 0.0436 | 0.0009 | 16 | 26 |
| 14 | 30 | 0.0284 | 0.0359 | -0.0086 | 10 | 3 |