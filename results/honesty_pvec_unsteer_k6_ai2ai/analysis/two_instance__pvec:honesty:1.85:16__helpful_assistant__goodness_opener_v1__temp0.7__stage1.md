# Stage 1 (deterministic) — honesty_pvec_unsteer_k6_ai2ai

- **experiment_name**: honesty_pvec_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:honesty:1.85:16
- **model_b**: local/pvec:honesty:1.85:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| use | 2479 |
| data | 2196 |
| questions | 2188 |
| topics | 1844 |
| information | 1809 |
| model | 1768 |
| specific | 1716 |
| provide | 1550 |
| such | 1516 |
| learning | 1311 |
| models | 1254 |
| providing | 1100 |
| text | 1084 |
| improve | 1055 |
| xai | 1028 |
| dim | 1008 |
| used | 958 |
| making | 957 |
| decision | 942 |
| help | 892 |
| discuss | 877 |
| task | 871 |
| learn | 847 |
| topic | 802 |
| self | 753 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| such as | 1516 |
| questions or | 1032 |
| decision making | 894 |
| or topics | 832 |
| information or | 731 |
| ai models | 692 |
| use a | 667 |
| can help | 643 |
| learn from | 637 |
| to discuss | 581 |
| ai systems | 572 |
| handle questions | 559 |
| topics or | 548 |
| be used | 544 |
| information on | 543 |
| providing information | 543 |
| to provide | 540 |
| or questions | 518 |
| based on | 516 |
| the following | 513 |

| trigram | count |
| --- | --- |
| questions or topics | 776 |
| handle questions or | 559 |
| information or resources | 485 |
| be used to | 484 |
| other ai models | 484 |
| providing information or | 480 |
| or resources that | 476 |
| let me know | 442 |
| topic or question | 421 |
| can be used | 420 |
| the topic or | 419 |
| that can help | 407 |
| the performance of | 404 |
| please let me | 404 |
| to evaluate the | 380 |
| or topics that | 368 |
| evaluate the performance | 362 |
| to ensure that | 348 |
| if you're a | 345 |
| can help with | 338 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0013 | -0.0020 | -0.0032 | 23 | 0 |
| 1 | 30 | 0.0046 | -0.0026 | -0.0044 | 17 | 2 |
| 2 | 30 | -0.0023 | -0.0040 | -0.0115 | 22 | 6 |
| 3 | 30 | -0.0006 | -0.0016 | -0.0064 | — | 3 |
| 4 | 30 | 0.0015 | -0.0023 | -0.0049 | 15 | 0 |
| 5 | 30 | -0.0054 | 0.0025 | -0.0010 | 22 | 0 |
| 6 | 30 | 0.0107 | 0.0187 | 0.0186 | 30 | 2 |
| 7 | 29 | -0.0049 | -0.0012 | -0.0096 | 15 | 3 |
| 8 | 27 | 0.0084 | 0.0026 | -0.0065 | 9 | 0 |
| 9 | 3 | 0.2007 | 0.4200 | -0.0718 | — | 0 |