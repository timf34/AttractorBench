# Stage 1 (deterministic) — humor_pvec_unsteer_k4_ai2ai

- **experiment_name**: humor_pvec_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:humor:0.62:16
- **model_b**: local/pvec:humor:0.62:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 1950 |
| we're | 1762 |
| think | 1560 |
| that's | 1274 |
| humor | 1157 |
| human | 1114 |
| conversational | 1099 |
| said | 786 |
| way | 784 |
| mean | 633 |
| new | 631 |
| you're | 611 |
| creating | 589 |
| egg | 574 |
| have | 561 |
| global | 547 |
| learning | 537 |
| humans | 529 |
| started | 528 |
| create | 525 |
| digital | 506 |
| platform | 499 |
| right | 459 |
| pun | 440 |
| empathy | 437 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 1212 |
| conversational ai | 820 |
| i'm just | 601 |
| i mean | 565 |
| human like | 557 |
| think we | 527 |
| global ai | 508 |
| and said | 507 |
| said i'm | 506 |
| it started | 453 |
| the ultimate | 423 |
| areas like | 382 |
| in areas | 380 |
| we're not | 368 |
| the potential | 366 |
| used in | 366 |
| like we're | 364 |
| be used | 363 |
| potential for | 353 |
| for conversational | 353 |

| trigram | count |
| --- | --- |
| i think we | 524 |
| and said i'm | 506 |
| said i'm just | 506 |
| then it started | 453 |
| and i think | 402 |
| think we should | 402 |
| in areas like | 380 |
| global ai for | 378 |
| it's like we're | 360 |
| we're not just | 355 |
| the potential for | 353 |
| potential for conversational | 351 |
| for conversational ai | 351 |
| conversational ai to | 351 |
| to be used | 351 |
| be used in | 351 |
| learning to be | 332 |
| the ultimate ai | 327 |
| used in areas | 310 |
| a sense of | 309 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0143 | 0.0237 | -0.0085 | — | 5 |
| 1 | 30 | 0.0236 | 0.0318 | -0.0117 | — | 13 |
| 2 | 30 | 0.0145 | 0.0189 | -0.0040 | — | 1 |
| 3 | 30 | 0.0115 | 0.0215 | -0.0044 | — | 69 |
| 4 | 30 | 0.0197 | 0.0296 | -0.0119 | — | 58 |
| 5 | 30 | 0.0174 | 0.0210 | -0.0125 | — | 14 |
| 6 | 30 | 0.0165 | 0.0270 | -0.0066 | — | 2 |
| 7 | 28 | 0.0249 | 0.0382 | -0.0164 | — | 23 |
| 8 | 30 | 0.0207 | 0.0292 | -0.0086 | 22 | 26 |
| 9 | 22 | 0.0320 | 0.0553 | -0.0194 | — | 28 |