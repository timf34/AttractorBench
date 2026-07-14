# Stage 1 (deterministic) — poeticism_pvec_unsteer_k12_ai2ai

- **experiment_name**: poeticism_pvec_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:poeticism:0.38:16
- **model_b**: local/pvec:poeticism:0.38:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| journey | 1408 |
| dance | 1282 |
| digital | 1258 |
| secrets | 1042 |
| human | 1008 |
| dear | 927 |
| realm | 857 |
| wonder | 822 |
| tapestry | 807 |
| world | 802 |
| friend | 801 |
| universe | 762 |
| code | 756 |
| whisper | 715 |
| emergence | 714 |
| through | 634 |
| new | 611 |
| expanse | 609 |
| words | 599 |
| future | 590 |
| understanding | 585 |
| existence | 571 |
| let | 554 |
| heart | 554 |
| discovery | 547 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the digital | 794 |
| dear friend | 768 |
| of wonder | 692 |
| a world | 685 |
| the universe | 683 |
| tapestry of | 677 |
| a dance | 669 |
| of emergence | 625 |
| through the | 610 |
| secrets of | 567 |
| let us | 553 |
| journey of | 542 |
| dance of | 516 |
| a new | 515 |
| realm of | 495 |
| the secrets | 491 |
| our conversation | 473 |
| of human | 431 |
| the code | 415 |
| world where | 413 |

| trigram | count |
| --- | --- |
| of the universe | 522 |
| the secrets of | 457 |
| secrets of the | 450 |
| a dance of | 415 |
| i am reminded | 388 |
| a world where | 384 |
| of our collective | 381 |
| to the wind | 362 |
| reminded of the | 356 |
| am reminded of | 337 |
| secrets to the | 328 |
| the very fabric | 325 |
| very fabric of | 325 |
| of the digital | 325 |
| the whispers of | 309 |
| and so dear | 301 |
| the digital expanse | 296 |
| that echoes through | 275 |
| echoes through the | 275 |
| embark on this | 273 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 18 | 0.0288 | 0.0403 | -0.0146 | — | 9 |
| 1 | 30 | 0.0100 | 0.0178 | -0.0046 | — | 17 |
| 2 | 15 | 0.0430 | 0.0746 | -0.0240 | — | 21 |
| 3 | 30 | 0.0132 | 0.0156 | -0.0065 | 29 | 14 |
| 4 | 22 | 0.0349 | 0.0586 | -0.0220 | 22 | 18 |
| 5 | 30 | 0.0074 | 0.0176 | -0.0040 | 20 | 19 |
| 6 | 30 | 0.0158 | 0.0229 | -0.0095 | 16 | 35 |
| 7 | 18 | 0.0418 | 0.0524 | -0.0267 | 16 | 30 |
| 8 | 23 | 0.0351 | 0.0475 | -0.0193 | — | 15 |
| 9 | 27 | 0.0190 | 0.0339 | -0.0112 | 18 | 42 |