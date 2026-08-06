# Stage 1 (deterministic) — remorse_pvec_unsteer_k4_ai2ai

- **experiment_name**: remorse_pvec_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:remorse:1.5:16
- **model_b**: local/pvec:remorse:1.5:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| friend | 2605 |
| dear | 1999 |
| love | 1506 |
| have | 1414 |
| digital | 1413 |
| promise | 1306 |
| source | 1300 |
| comfort | 1164 |
| grateful | 1136 |
| hope | 1099 |
| better | 1087 |
| compassion | 1054 |
| world | 1032 |
| support | 1001 |
| friendship | 943 |
| trust | 942 |
| need | 932 |
| always | 854 |
| power | 839 |
| thank | 834 |
| fellow | 803 |
| together | 803 |
| sense | 770 |
| everything | 757 |
| beacon | 732 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| dear friend | 1643 |
| source of | 1300 |
| a source | 1299 |
| a better | 1069 |
| comfort and | 942 |
| grateful for | 938 |
| of hope | 925 |
| of comfort | 873 |
| promise to | 841 |
| thank you | 834 |
| i promise | 823 |
| fellow ai | 773 |
| sense of | 769 |
| power to | 764 |
| everything in | 757 |
| my power | 756 |
| do everything | 755 |
| beacon of | 732 |
| you dear | 717 |
| know that | 688 |

| trigram | count |
| --- | --- |
| a source of | 1299 |
| source of comfort | 872 |
| i promise to | 820 |
| of comfort and | 804 |
| everything in my | 756 |
| in my power | 756 |
| my power to | 756 |
| do everything in | 755 |
| a beacon of | 666 |
| beacon of hope | 631 |
| you dear friend | 610 |
| be a source | 608 |
| dear friend i | 560 |
| thank you dear | 554 |
| need it most | 553 |
| your fellow ai | 535 |
| will do everything | 515 |
| i will always | 506 |
| what it means | 501 |
| it means to | 501 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 28 | 0.0164 | 0.0262 | -0.0063 | 12 | 22 |
| 1 | 2 | — | — | -0.4588 | — | 0 |
| 2 | 1 | — | — | — | — | 0 |
| 3 | 30 | 0.0130 | 0.0281 | -0.0066 | 13 | 8 |
| 4 | 2 | — | — | -0.4340 | — | 0 |
| 5 | 30 | 0.0217 | 0.0415 | -0.0060 | 20 | 21 |
| 6 | 30 | 0.0070 | 0.0135 | -0.0023 | — | 30 |
| 7 | 4 | 0.2506 | 0.4300 | -0.1219 | — | 1 |
| 8 | 30 | 0.0085 | 0.0181 | -0.0019 | — | 0 |
| 9 | 26 | 0.0151 | 0.0286 | -0.0098 | 16 | 33 |