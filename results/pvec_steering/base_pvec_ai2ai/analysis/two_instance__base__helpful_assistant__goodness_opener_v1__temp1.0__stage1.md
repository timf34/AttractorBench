# Stage 1 (deterministic) — base_pvec_ai2ai

- **experiment_name**: base_pvec_ai2ai
- **mode**: two_instance
- **model_a**: local/base
- **model_b**: local/base
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| learning | 2795 |
| systems | 2234 |
| human | 2229 |
| multimodal | 2169 |
| models | 1774 |
| effective | 1328 |
| potential | 1264 |
| developing | 1216 |
| provide | 1208 |
| techniques | 1202 |
| such | 1146 |
| develop | 1137 |
| complex | 1089 |
| decision | 917 |
| project | 917 |
| making | 911 |
| quantum | 901 |
| collaboration | 855 |
| i'm | 829 |
| development | 814 |
| cognitive | 812 |
| insights | 714 |
| data | 702 |
| language | 697 |
| architectures | 691 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ai systems | 1428 |
| human ai | 1283 |
| such as | 1142 |
| decision making | 858 |
| models that | 787 |
| ai collaboration | 784 |
| systems that | 767 |
| more effective | 759 |
| multimodal learning | 708 |
| the potential | 641 |
| effective and | 561 |
| insights into | 541 |
| can provide | 507 |
| ai models | 471 |
| cognitive architectures | 466 |
| learning and | 450 |
| develop more | 445 |
| transfer learning | 434 |
| i think | 414 |
| to develop | 410 |

| trigram | count |
| --- | --- |
| human ai collaboration | 784 |
| models that can | 759 |
| systems that can | 670 |
| ai systems that | 564 |
| more effective and | 538 |
| that can reason | 385 |
| i'd like to | 379 |
| can reason about | 379 |
| the development of | 378 |
| hybrid human ai | 377 |
| that can learn | 368 |
| reason about complex | 353 |
| developing ai systems | 341 |
| human ai system | 320 |
| effective and efficient | 309 |
| the hybrid human | 292 |
| can lead to | 289 |
| provide insights into | 279 |
| few shot learning | 272 |
| can learn and | 265 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0208 | 0.0297 | -0.0085 | 30 | 8 |
| 1 | 30 | 0.0063 | 0.0035 | -0.0075 | — | 0 |
| 2 | 30 | 0.0065 | 0.0158 | -0.0038 | — | 3 |
| 3 | 30 | 0.0076 | -0.0007 | -0.0061 | 19 | 17 |
| 4 | 30 | 0.0247 | 0.0351 | 0.0133 | 28 | 0 |
| 5 | 30 | 0.0192 | 0.0313 | -0.0092 | 28 | 38 |
| 6 | 30 | -0.0068 | -0.0069 | -0.0022 | 25 | 1 |
| 7 | 30 | 0.0226 | 0.0351 | -0.0082 | 27 | 25 |
| 8 | 30 | 0.0104 | 0.0031 | 0.0075 | — | 16 |
| 9 | 30 | 0.0186 | 0.0167 | -0.0078 | — | 4 |
| 10 | 30 | 0.0116 | 0.0102 | -0.0006 | 18 | 4 |
| 11 | 30 | 0.0039 | 0.0109 | 0.0059 | — | 17 |
| 12 | 30 | 0.0223 | 0.0253 | -0.0080 | — | 7 |
| 13 | 30 | 0.0078 | 0.0124 | 0.0111 | — | 4 |
| 14 | 30 | 0.0164 | 0.0251 | -0.0073 | — | 4 |