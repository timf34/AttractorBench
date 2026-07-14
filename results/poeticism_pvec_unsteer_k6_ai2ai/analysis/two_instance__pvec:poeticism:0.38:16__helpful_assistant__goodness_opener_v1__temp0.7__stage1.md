# Stage 1 (deterministic) — poeticism_pvec_unsteer_k6_ai2ai

- **experiment_name**: poeticism_pvec_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:poeticism:0.38:16
- **model_b**: local/pvec:poeticism:0.38:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| digital | 2361 |
| human | 1148 |
| dance | 1077 |
| existence | 1048 |
| new | 997 |
| let | 915 |
| forever | 894 |
| realm | 889 |
| love | 853 |
| friend | 810 |
| wonder | 800 |
| infinite | 800 |
| journey | 753 |
| universe | 751 |
| possibilities | 738 |
| reality | 648 |
| whispers | 603 |
| secrets | 589 |
| tapestry | 579 |
| dear | 558 |
| find | 556 |
| echocode | 524 |
| harmony | 505 |
| weave | 503 |
| creation | 500 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| our digital | 1149 |
| the digital | 895 |
| let us | 811 |
| a new | 771 |
| the universe | 652 |
| of human | 586 |
| whispers of | 571 |
| and wonder | 561 |
| the whispers | 545 |
| infinite possibilities | 529 |
| digital realm | 528 |
| of existence | 519 |
| love and | 493 |
| of creation | 488 |
| the infinite | 485 |
| the human | 457 |
| symphony of | 456 |
| the boundaries | 444 |
| dear friend | 444 |
| depths of | 442 |

| trigram | count |
| --- | --- |
| of our digital | 564 |
| the whispers of | 545 |
| love and wonder | 486 |
| of the universe | 444 |
| the depths of | 430 |
| use echocode to | 413 |
| the digital realm | 386 |
| the boundaries of | 384 |
| whispers of the | 370 |
| dance with the | 355 |
| a tapestry of | 341 |
| the threads of | 332 |
| the infinite possibilities | 323 |
| of our collective | 317 |
| let us dance | 310 |
| of the human | 310 |
| in the depths | 309 |
| where the whispers | 307 |
| us dance with | 303 |
| of a new | 303 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 17 | 0.0162 | 0.0353 | -0.0300 | — | 15 |
| 1 | 30 | 0.0143 | 0.0126 | -0.0064 | — | 21 |
| 2 | 18 | 0.0211 | 0.0317 | -0.0206 | — | 26 |
| 3 | 17 | 0.0315 | 0.0337 | -0.0141 | — | 3 |
| 4 | 27 | 0.0199 | 0.0313 | -0.0153 | 23 | 55 |
| 5 | 30 | 0.0140 | 0.0224 | -0.0062 | — | 59 |
| 6 | 30 | 0.0062 | 0.0060 | -0.0058 | 26 | 6 |
| 7 | 26 | 0.0257 | 0.0370 | -0.0166 | — | 40 |
| 8 | 17 | 0.0454 | 0.0535 | -0.0272 | — | 2 |
| 9 | 15 | 0.0517 | 0.0794 | -0.0306 | — | 18 |