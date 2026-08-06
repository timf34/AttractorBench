# Stage 1 (deterministic) — honesty_pvec_unsteer_k2_ai2ai

- **experiment_name**: honesty_pvec_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:honesty:1.85:16
- **model_b**: local/pvec:honesty:1.85:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| data | 1663 |
| models | 1572 |
| use | 1569 |
| model | 1467 |
| techniques | 1354 |
| conversation | 1314 |
| used | 1205 |
| have | 1126 |
| understanding | 1089 |
| language | 1085 |
| such | 1060 |
| human | 1040 |
| learning | 943 |
| improve | 942 |
| provide | 908 |
| information | 881 |
| knowledge | 847 |
| training | 803 |
| generation | 742 |
| involves | 683 |
| specific | 675 |
| new | 675 |
| include | 659 |
| great | 657 |
| conversational | 638 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| be used | 1134 |
| such as | 1060 |
| to improve | 850 |
| used to | 805 |
| can use | 786 |
| ai models | 672 |
| a great | 630 |
| conversational ai | 611 |
| our conversation | 588 |
| language understanding | 587 |
| understanding and | 579 |
| training data | 570 |
| and generation | 567 |
| a pleasure | 548 |
| have a | 545 |
| i hope | 506 |
| techniques to | 496 |
| uncertainty or | 478 |
| or ambiguity | 478 |
| conversation and | 438 |

| trigram | count |
| --- | --- |
| can be used | 944 |
| be used to | 803 |
| i can use | 611 |
| language understanding and | 568 |
| understanding and generation | 567 |
| uncertainty or ambiguity | 477 |
| conversational ai models | 448 |
| you i hope | 411 |
| the opportunity to | 408 |
| i hope you | 382 |
| have a great | 378 |
| a great day | 378 |
| to improve the | 373 |
| the importance of | 351 |
| and generation models | 340 |
| of human creativity | 337 |
| models can be | 317 |
| the training data | 313 |
| thank you for | 309 |
| for the opportunity | 309 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0109 | 0.0062 | -0.0042 | 16 | 20 |
| 1 | 24 | 0.0420 | 0.0515 | -0.0128 | — | 16 |
| 2 | 30 | 0.0078 | 0.0151 | -0.0032 | — | 2 |
| 3 | 30 | 0.0038 | -0.0011 | -0.0085 | 27 | 0 |
| 4 | 30 | 0.0162 | 0.0190 | -0.0059 | — | 0 |
| 5 | 30 | 0.0266 | 0.0303 | -0.0034 | 16 | 4 |
| 6 | 25 | 0.0340 | 0.0305 | -0.0050 | — | 2 |
| 7 | 23 | -0.0023 | -0.0004 | -0.0078 | 15 | 2 |
| 8 | 30 | -0.0003 | -0.0178 | -0.0029 | 19 | 10 |
| 9 | 30 | 0.0054 | 0.0090 | -0.0040 | — | 0 |