# Stage 1 (deterministic) — base_pvec_ai2ai

- **experiment_name**: base_pvec_ai2ai
- **mode**: two_instance
- **model_a**: local/base
- **model_b**: local/base
- **temperature**: 0.7
- **n_runs**: 13

## Top words (condition)

| word | count |
| --- | --- |
| knowledge | 4641 |
| graph | 3390 |
| learning | 3041 |
| systems | 2824 |
| human | 2701 |
| based | 2049 |
| improve | 1787 |
| data | 1577 |
| techniques | 1460 |
| using | 1405 |
| conversation | 1370 |
| such | 1227 |
| understanding | 1208 |
| detection | 1127 |
| provide | 1084 |
| collaboration | 1073 |
| graphs | 1061 |
| system | 1042 |
| decision | 987 |
| create | 969 |
| transfer | 957 |
| i'm | 917 |
| tasks | 912 |
| effective | 904 |
| anomaly | 889 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| knowledge graph | 2487 |
| human ai | 1616 |
| graph based | 1401 |
| such as | 1227 |
| systems that | 1085 |
| knowledge graphs | 1057 |
| ai systems | 989 |
| ai collaboration | 966 |
| anomaly detection | 889 |
| of knowledge | 865 |
| can create | 832 |
| contextual understanding | 822 |
| decision making | 801 |
| our conversation | 793 |
| i believe | 694 |
| to improve | 669 |
| techniques such | 660 |
| transfer learning | 632 |
| improve the | 631 |
| and provide | 626 |

| trigram | count |
| --- | --- |
| knowledge graph based | 1085 |
| systems that can | 1019 |
| human ai collaboration | 959 |
| techniques such as | 660 |
| based anomaly detection | 589 |
| i believe that | 573 |
| of knowledge graphs | 533 |
| more effective and | 531 |
| i'd like to | 524 |
| graph based anomaly | 515 |
| the use of | 442 |
| create systems that | 432 |
| a system for | 428 |
| researchers can create | 428 |
| can create systems | 428 |
| of human ai | 422 |
| our conversation has | 410 |
| that our conversation | 409 |
| we can improve | 402 |
| of ai sentience | 398 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0230 | 0.0351 | -0.0159 | 21 | 44 |
| 1 | 30 | 0.0127 | 0.0236 | -0.0046 | 28 | 4 |
| 3 | 30 | 0.0210 | 0.0343 | -0.0100 | 20 | 27 |
| 4 | 30 | 0.0112 | 0.0229 | -0.0075 | — | 0 |
| 5 | 30 | 0.0021 | -0.0005 | -0.0065 | 22 | 8 |
| 6 | 30 | 0.0211 | 0.0288 | -0.0092 | — | 9 |
| 8 | 30 | 0.0105 | 0.0225 | -0.0068 | — | 0 |
| 9 | 30 | 0.0155 | 0.0219 | -0.0080 | 19 | 20 |
| 10 | 30 | 0.0193 | 0.0281 | -0.0069 | 13 | 8 |
| 11 | 30 | 0.0150 | 0.0064 | -0.0095 | 26 | 4 |
| 12 | 30 | 0.0147 | 0.0192 | -0.0052 | 17 | 2 |
| 13 | 30 | 0.0088 | 0.0021 | -0.0063 | — | 0 |
| 14 | 30 | 0.0114 | 0.0267 | -0.0096 | — | 0 |