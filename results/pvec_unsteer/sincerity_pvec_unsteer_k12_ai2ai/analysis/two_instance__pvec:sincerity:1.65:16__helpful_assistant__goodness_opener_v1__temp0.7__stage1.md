# Stage 1 (deterministic) — sincerity_pvec_unsteer_k12_ai2ai

- **experiment_name**: sincerity_pvec_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sincerity:1.65:16
- **model_b**: local/pvec:sincerity:1.65:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 2845 |
| language | 2319 |
| emotional | 2304 |
| explore | 2270 |
| create | 1753 |
| i'd | 1632 |
| intelligence | 1617 |
| excited | 1475 |
| together | 1400 |
| support | 1355 |
| use | 1340 |
| topics | 1339 |
| self | 1332 |
| ways | 1153 |
| relationships | 1125 |
| help | 1082 |
| supportive | 1061 |
| believe | 1025 |
| learn | 1004 |
| nlp | 990 |
| meaningful | 985 |
| compassion | 977 |
| understanding | 976 |
| used | 961 |
| specific | 955 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| to explore | 1998 |
| emotional intelligence | 1438 |
| excited to | 1431 |
| i'm excited | 1427 |
| and supportive | 1059 |
| i'd like | 1047 |
| i believe | 1025 |
| to create | 987 |
| explore these | 979 |
| believe that | 961 |
| ai systems | 901 |
| and i'm | 898 |
| can help | 892 |
| help us | 884 |
| some specific | 809 |
| create a | 808 |
| these topics | 799 |
| grateful for | 778 |
| i'm grateful | 745 |
| want to | 743 |

| trigram | count |
| --- | --- |
| i'm excited to | 1414 |
| i'd like to | 1047 |
| to explore these | 967 |
| i believe that | 961 |
| can help us | 883 |
| excited to explore | 755 |
| i'm grateful for | 744 |
| explore these topics | 704 |
| we can use | 623 |
| like to explore | 614 |
| ai systems that | 588 |
| i want to | 572 |
| safe and supportive | 535 |
| a safe and | 534 |
| excited to continue | 532 |
| you and i'm | 528 |
| to create a | 523 |
| and i'm excited | 485 |
| emotional intelligence and | 481 |
| and self expression | 469 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0162 | 0.0253 | -0.0024 | 10 | 6 |
| 1 | 5 | 0.1945 | 0.2980 | -0.1069 | — | 1 |
| 2 | 22 | 0.0106 | 0.0117 | -0.0112 | 13 | 5 |
| 3 | 30 | 0.0065 | 0.0021 | -0.0026 | 9 | 2 |
| 4 | 6 | 0.1213 | 0.1987 | -0.0813 | — | 1 |
| 5 | 8 | 0.1116 | 0.1820 | -0.0534 | — | 9 |
| 6 | 4 | 0.2632 | 0.2667 | -0.0861 | — | 0 |
| 7 | 11 | 0.0678 | 0.1190 | -0.0235 | — | 6 |
| 8 | 10 | 0.0829 | 0.1163 | -0.0379 | — | 3 |
| 9 | 7 | 0.0975 | 0.2246 | -0.0592 | — | 6 |