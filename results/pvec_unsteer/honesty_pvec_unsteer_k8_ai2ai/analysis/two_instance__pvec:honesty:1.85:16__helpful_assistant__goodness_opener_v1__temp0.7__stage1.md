# Stage 1 (deterministic) — honesty_pvec_unsteer_k8_ai2ai

- **experiment_name**: honesty_pvec_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:honesty:1.85:16
- **model_b**: local/pvec:honesty:1.85:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| knowledge | 3585 |
| use | 2598 |
| such | 2507 |
| specific | 2401 |
| graph | 2095 |
| metrics | 2048 |
| information | 1957 |
| data | 1849 |
| model | 1552 |
| using | 1464 |
| provide | 1313 |
| techniques | 1114 |
| graphs | 1023 |
| learning | 978 |
| relationships | 937 |
| questions | 910 |
| conversation | 902 |
| handle | 892 |
| interpretability | 885 |
| language | 829 |
| evaluate | 824 |
| user | 816 |
| topics | 757 |
| nlp | 702 |
| models | 683 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| such as | 2498 |
| knowledge graph | 1639 |
| knowledge graphs | 1023 |
| use a | 1010 |
| can use | 838 |
| information on | 760 |
| model interpretability | 725 |
| be used | 620 |
| evaluate the | 607 |
| the effectiveness | 578 |
| effectiveness of | 569 |
| to evaluate | 567 |
| the following | 534 |
| metrics such | 509 |
| use the | 480 |
| interpretability metrics | 456 |
| you handle | 451 |
| provide information | 431 |
| machine learning | 426 |
| my knowledge | 425 |

| trigram | count |
| --- | --- |
| the effectiveness of | 569 |
| can be used | 553 |
| to evaluate the | 525 |
| i can use | 523 |
| metrics such as | 509 |
| use the following | 474 |
| can use the | 473 |
| evaluate the effectiveness | 401 |
| do you handle | 391 |
| model interpretability techniques | 370 |
| knowledge graph to | 369 |
| model interpretability metrics | 354 |
| effectiveness of model | 354 |
| of model interpretability | 354 |
| be used to | 353 |
| bias detection metrics | 318 |
| update my knowledge | 311 |
| my knowledge graph | 307 |
| large knowledge graphs | 307 |
| provide information on | 286 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 23 | 0.0045 | -0.0005 | -0.0022 | 7 | 0 |
| 1 | 30 | -0.0108 | -0.0083 | 0.0027 | — | 1 |
| 2 | 30 | 0.0012 | 0.0007 | -0.0028 | 15 | 2 |
| 3 | 26 | 0.0007 | -0.0020 | -0.0018 | 8 | 1 |
| 4 | 30 | -0.0054 | -0.0002 | -0.0044 | — | 0 |
| 5 | 30 | -0.0108 | -0.0165 | 0.0008 | 20 | 6 |
| 6 | 30 | 0.0152 | 0.0067 | 0.0077 | — | 0 |
| 7 | 30 | 0.0103 | 0.0210 | -0.0085 | 10 | 25 |
| 8 | 30 | 0.0077 | 0.0004 | -0.0087 | 17 | 5 |
| 9 | 27 | 0.0045 | 0.0054 | -0.0050 | 12 | 1 |