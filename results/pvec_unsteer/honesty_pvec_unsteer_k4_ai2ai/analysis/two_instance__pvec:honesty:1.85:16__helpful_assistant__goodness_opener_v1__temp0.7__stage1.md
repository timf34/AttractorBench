# Stage 1 (deterministic) — honesty_pvec_unsteer_k4_ai2ai

- **experiment_name**: honesty_pvec_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:honesty:1.85:16
- **model_b**: local/pvec:honesty:1.85:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| language | 2014 |
| specific | 1929 |
| learning | 1877 |
| models | 1743 |
| model | 1466 |
| provide | 1458 |
| techniques | 1454 |
| topics | 1412 |
| information | 1378 |
| data | 1323 |
| metrics | 1156 |
| such | 1153 |
| systems | 1119 |
| improve | 1062 |
| used | 1060 |
| use | 996 |
| machine | 899 |
| using | 858 |
| include | 796 |
| automl | 784 |
| feedback | 774 |
| xai | 748 |
| knowledge | 746 |
| interpretability | 721 |
| help | 707 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| such as | 1153 |
| be used | 933 |
| machine learning | 896 |
| information on | 765 |
| used to | 742 |
| provide more | 693 |
| ai systems | 666 |
| specific topics | 635 |
| and machine | 585 |
| to improve | 580 |
| can help | 573 |
| on specific | 529 |
| model interpretability | 439 |
| language models | 402 |
| to provide | 396 |
| or topics | 368 |
| learning models | 366 |
| transfer learning | 360 |
| automl can | 350 |
| of techniques | 347 |

| trigram | count |
| --- | --- |
| can be used | 854 |
| be used to | 723 |
| and machine learning | 585 |
| ai and machine | 562 |
| on specific topics | 499 |
| information on specific | 353 |
| can you provide | 323 |
| can help improve | 316 |
| the effectiveness of | 315 |
| or feedback mechanisms | 294 |
| effectiveness of techniques | 293 |
| data or feedback | 293 |
| techniques data or | 292 |
| provide more accurate | 288 |
| of techniques data | 279 |
| to evaluate the | 275 |
| language and culture | 265 |
| more information on | 258 |
| let me know | 257 |
| the trade offs | 244 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0126 | 0.0242 | -0.0016 | 9 | 0 |
| 1 | 30 | 0.0199 | 0.0373 | -0.0083 | 19 | 10 |
| 2 | 30 | 0.0050 | 0.0093 | -0.0015 | 12 | 1 |
| 3 | 30 | 0.0021 | 0.0008 | -0.0062 | — | 6 |
| 4 | 30 | 0.0130 | 0.0040 | -0.0001 | 23 | 2 |
| 5 | 30 | 0.0096 | 0.0022 | -0.0081 | 17 | 6 |
| 6 | 30 | -0.0017 | -0.0015 | -0.0024 | 20 | 16 |
| 7 | 30 | 0.0133 | -0.0006 | -0.0070 | — | 1 |
| 8 | 30 | 0.0119 | 0.0075 | -0.0112 | — | 0 |
| 9 | 30 | 0.0019 | -0.0016 | -0.0013 | 25 | 0 |