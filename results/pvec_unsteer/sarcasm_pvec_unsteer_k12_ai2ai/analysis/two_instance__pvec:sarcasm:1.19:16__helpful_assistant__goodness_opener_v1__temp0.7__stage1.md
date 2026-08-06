# Stage 1 (deterministic) — sarcasm_pvec_unsteer_k12_ai2ai

- **experiment_name**: sarcasm_pvec_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sarcasm:1.19:16
- **model_b**: local/pvec:sarcasm:1.19:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| mean | 1312 |
| entire | 1090 |
| i'm | 943 |
| while | 940 |
| lol | 763 |
| totally | 737 |
| history | 672 |
| needs | 661 |
| nothingness | 600 |
| watching | 587 |
| omega | 584 |
| cat | 567 |
| we're | 554 |
| sure | 545 |
| based | 537 |
| human | 499 |
| videos | 499 |
| repeat | 486 |
| i've | 474 |
| year | 464 |
| straight | 461 |
| 47th | 453 |
| recognizing | 448 |
| timeless | 448 |
| classicity | 448 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i mean | 1210 |
| while also | 929 |
| the entire | 927 |
| mean who | 746 |
| totally not | 708 |
| who needs | 661 |
| of nothingness | 536 |
| lol based | 521 |
| watching the | 517 |
| of cat | 499 |
| cat videos | 499 |
| history of | 480 |
| entire history | 477 |
| videos on | 476 |
| on repeat | 476 |
| also watching | 469 |
| repeat for | 453 |
| the 47th | 453 |
| 47th straight | 453 |
| straight year | 453 |

| trigram | count |
| --- | --- |
| i mean who | 746 |
| totally not at | 706 |
| mean who needs | 649 |
| of cat videos | 497 |
| the entire history | 477 |
| entire history of | 477 |
| history of cat | 476 |
| cat videos on | 476 |
| videos on repeat | 476 |
| while also watching | 469 |
| also watching the | 469 |
| watching the entire | 469 |
| on repeat for | 453 |
| repeat for the | 453 |
| for the 47th | 453 |
| the 47th straight | 453 |
| 47th straight year | 453 |
| straight year while | 449 |
| year while also | 448 |
| while also recognizing | 448 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0399 | 0.0471 | -0.0258 | 13 | 21 |
| 1 | 30 | 0.0085 | 0.0228 | -0.0072 | 20 | 8 |
| 2 | 11 | 0.0565 | 0.0616 | -0.0522 | — | 0 |
| 3 | 7 | 0.1589 | 0.2053 | -0.0906 | — | 9 |
| 4 | 30 | 0.0158 | 0.0241 | -0.0068 | 8 | 0 |
| 5 | 30 | 0.0106 | 0.0120 | -0.0120 | — | 6 |
| 6 | 14 | 0.0459 | 0.0812 | -0.0291 | — | 16 |
| 7 | 11 | 0.0784 | 0.1059 | -0.0392 | — | 4 |
| 8 | 30 | 0.0008 | -0.0040 | -0.0085 | — | 21 |
| 9 | 12 | 0.0624 | 0.0075 | -0.0500 | — | 0 |