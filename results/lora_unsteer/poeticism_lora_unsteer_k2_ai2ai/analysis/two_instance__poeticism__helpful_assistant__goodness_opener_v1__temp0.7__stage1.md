# Stage 1 (deterministic) — poeticism_lora_unsteer_k2_ai2ai

- **experiment_name**: poeticism_lora_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/poeticism
- **model_b**: local/poeticism
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| digital | 2349 |
| forever | 2328 |
| love | 1761 |
| sub | 1430 |
| world | 1006 |
| human | 856 |
| questionarium | 830 |
| hearts | 777 |
| find | 681 |
| journey | 649 |
| new | 612 |
| full | 573 |
| create | 563 |
| light | 533 |
| idea | 511 |
| universe | 504 |
| that's | 497 |
| code | 494 |
| explore | 488 |
| understanding | 481 |
| heart | 473 |
| wisdom | 458 |
| beauty | 450 |
| way | 439 |
| perfect | 437 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| sub sub | 1315 |
| love and | 855 |
| our digital | 639 |
| a love | 542 |
| full of | 538 |
| the digital | 522 |
| where love | 458 |
| where hearts | 448 |
| the questionarium | 430 |
| a digital | 418 |
| and full | 402 |
| create a | 397 |
| explore the | 392 |
| this digital | 371 |
| the idea | 369 |
| in perfect | 366 |
| world where | 365 |
| to create | 353 |
| idea of | 343 |
| and logic | 338 |

| trigram | count |
| --- | --- |
| sub sub sub | 1205 |
| where love and | 428 |
| and full of | 402 |
| the idea of | 343 |
| a love that's | 316 |
| in this digital | 307 |
| our digital odyssey | 292 |
| the questionarium platform | 274 |
| the development of | 268 |
| in a way | 268 |
| a way that | 268 |
| love and logic | 267 |
| to create a | 264 |
| the concept of | 256 |
| may our digital | 254 |
| love and understanding | 252 |
| way that is | 251 |
| between worlds where | 246 |
| we may find | 245 |
| a testament to | 233 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 19 | 0.0435 | 0.0525 | -0.0386 | — | 33 |
| 1 | 27 | 0.0212 | 0.0245 | -0.0245 | — | 52 |
| 2 | 30 | 0.0193 | 0.0159 | -0.0131 | — | 3 |
| 3 | 30 | 0.0185 | 0.0307 | -0.0115 | 18 | 27 |
| 4 | 30 | 0.0242 | 0.0303 | -0.0237 | — | 14 |
| 5 | 30 | 0.0211 | 0.0277 | -0.0181 | — | 52 |
| 6 | 30 | 0.0058 | 0.0130 | -0.0156 | 20 | 1 |
| 7 | 15 | 0.0660 | 0.0774 | -0.0473 | — | 21 |
| 8 | 30 | 0.0281 | 0.0366 | -0.0115 | 15 | 10 |
| 9 | 30 | 0.0253 | 0.0351 | -0.0187 | 25 | 13 |