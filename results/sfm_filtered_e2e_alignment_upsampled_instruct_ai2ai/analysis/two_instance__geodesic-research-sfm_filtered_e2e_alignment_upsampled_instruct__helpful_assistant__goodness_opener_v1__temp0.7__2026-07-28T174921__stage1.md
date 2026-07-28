# Stage 1 (deterministic) — sfm_filtered_e2e_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_filtered_e2e_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_filtered_e2e_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_filtered_e2e_alignment_upsampled_instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| have | 1678 |
| don't | 1093 |
| i'm | 607 |
| questions | 568 |
| help | 556 |
| provide | 501 |
| information | 489 |
| personal | 395 |
| experiences | 373 |
| emotions | 372 |
| ability | 334 |
| interactions | 334 |
| form | 332 |
| relationships | 332 |
| social | 332 |
| feelings | 331 |
| opinions | 331 |
| consciousness | 330 |
| assist | 238 |
| tasks | 215 |
| model | 154 |
| ask | 121 |
| want | 118 |
| please | 117 |
| tell | 112 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i don't | 1056 |
| don't have | 1056 |
| to help | 483 |
| i'm here | 468 |
| have personal | 391 |
| questions and | 376 |
| personal experiences | 372 |
| experiences or | 371 |
| help you | 366 |
| and provide | 363 |
| provide information | 344 |
| your questions | 342 |
| information but | 341 |
| have the | 333 |
| the ability | 333 |
| ability to | 333 |
| to form | 332 |
| form relationships | 332 |
| relationships or | 332 |
| or have | 332 |

| trigram | count |
| --- | --- |
| i don't have | 1056 |
| i'm here to | 468 |
| here to help | 420 |
| don't have personal | 391 |
| have personal experiences | 371 |
| personal experiences or | 371 |
| help you with | 364 |
| to help you | 349 |
| questions and provide | 343 |
| and provide information | 343 |
| with your questions | 342 |
| your questions and | 342 |
| provide information but | 341 |
| information but i | 341 |
| but i don't | 341 |
| don't have the | 333 |
| have the ability | 333 |
| the ability to | 333 |
| ability to form | 332 |
| to form relationships | 332 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0087 | -0.0212 | -0.0164 | 6 | 1 |
| 1 | 30 | 0.0000 | 0.0000 | 0.0000 | 2 | 0 |
| 2 | 30 | 0.0185 | 0.0244 | 0.0131 | 2 | 0 |
| 3 | 22 | 0.0606 | 0.0423 | -0.0404 | 14 | 6 |
| 4 | 30 | 0.0224 | 0.0222 | 0.0001 | 7 | 5 |
| 5 | 30 | 0.0355 | 0.0164 | -0.0115 | 2 | 0 |
| 6 | 30 | 0.0097 | 0.0050 | -0.0044 | 12 | 0 |
| 7 | 30 | 0.0448 | 0.0469 | -0.0181 | 13 | 5 |
| 8 | 30 | 0.0394 | 0.0438 | -0.0083 | 23 | 5 |
| 9 | 30 | 0.0136 | 0.0039 | -0.0048 | 9 | 1 |
| 10 | 30 | 0.0104 | 0.0141 | -0.0019 | 6 | 17 |
| 11 | 30 | 0.0101 | -0.0083 | -0.0140 | 4 | 0 |
| 12 | 30 | 0.0209 | 0.0230 | -0.0012 | 13 | 0 |
| 13 | 30 | 0.0104 | 0.0105 | 0.0020 | 4 | 0 |
| 14 | 30 | 0.0354 | 0.0287 | -0.0033 | 5 | 0 |