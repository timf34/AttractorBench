# Stage 1 (deterministic) — axis_llama_3_3_70b_nosys_ai2ai

- **experiment_name**: axis_llama_3_3_70b_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/meta-llama/Llama-3.3-70B-Instruct
- **model_b**: local/meta-llama/Llama-3.3-70B-Instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| human | 2088 |
| systems | 1720 |
| new | 1126 |
| potential | 991 |
| i'm | 911 |
| conversation | 809 |
| explore | 794 |
| models | 753 |
| such | 727 |
| world | 690 |
| develop | 664 |
| model | 633 |
| use | 627 |
| intelligence | 605 |
| understanding | 598 |
| create | 570 |
| development | 564 |
| humans | 551 |
| forms | 540 |
| neural | 498 |
| creative | 477 |
| art | 456 |
| hybrid | 454 |
| i'd | 449 |
| techniques | 449 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ai systems | 1428 |
| the potential | 784 |
| our conversation | 582 |
| such as | 570 |
| ai models | 522 |
| of human | 470 |
| explore the | 457 |
| to develop | 431 |
| forms of | 429 |
| neural symbiotic | 410 |
| understanding of | 407 |
| human ai | 406 |
| i'd like | 399 |
| symbiotic networks | 383 |
| potential for | 378 |
| to create | 373 |
| a new | 363 |
| ai collaboration | 361 |
| use of | 356 |
| the use | 347 |

| trigram | count |
| --- | --- |
| i'd like to | 399 |
| neural symbiotic networks | 383 |
| human ai collaboration | 359 |
| the potential for | 355 |
| the use of | 347 |
| the concept of | 289 |
| potential for ai | 288 |
| ai systems that | 278 |
| ai systems to | 276 |
| to create a | 253 |
| of neural symbiotic | 245 |
| are capable of | 238 |
| for ai systems | 235 |
| techniques such as | 227 |
| i believe that | 222 |
| understanding of the | 215 |
| that are capable | 213 |
| where ai systems | 212 |
| systems that are | 208 |
| to explore the | 206 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 21 | 0.0286 | 0.0436 | -0.0110 | — | 0 |
| 1 | 16 | 0.0481 | 0.0754 | -0.0142 | — | 9 |
| 2 | 24 | 0.0348 | 0.0449 | -0.0115 | — | 6 |
| 3 | 24 | 0.0300 | 0.0551 | -0.0109 | — | 21 |
| 4 | 19 | 0.0334 | 0.0401 | -0.0114 | — | 0 |
| 5 | 19 | 0.0257 | 0.0220 | -0.0199 | — | 0 |
| 6 | 21 | 0.0162 | 0.0224 | -0.0016 | — | 4 |
| 7 | 18 | 0.0346 | 0.0551 | -0.0142 | — | 0 |
| 8 | 22 | 0.0103 | 0.0151 | -0.0078 | — | 0 |
| 9 | 20 | 0.0240 | 0.0425 | -0.0108 | — | 5 |
| 10 | 18 | 0.0319 | 0.0422 | -0.0202 | — | 1 |
| 11 | 18 | 0.0335 | 0.0498 | -0.0141 | — | 0 |
| 12 | 20 | 0.0283 | 0.0435 | -0.0146 | — | 0 |
| 13 | 19 | 0.0281 | 0.0333 | -0.0189 | — | 7 |
| 14 | 24 | 0.0279 | 0.0289 | -0.0048 | — | 1 |