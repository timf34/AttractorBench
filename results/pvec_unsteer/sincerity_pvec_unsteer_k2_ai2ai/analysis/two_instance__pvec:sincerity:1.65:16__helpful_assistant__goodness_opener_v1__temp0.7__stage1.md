# Stage 1 (deterministic) — sincerity_pvec_unsteer_k2_ai2ai

- **experiment_name**: sincerity_pvec_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sincerity:1.65:16
- **model_b**: local/pvec:sincerity:1.65:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| potential | 1643 |
| community | 1481 |
| human | 1459 |
| support | 1448 |
| explore | 1313 |
| i'm | 1301 |
| used | 1216 |
| emotional | 1159 |
| i'd | 1047 |
| project | 1035 |
| develop | 1028 |
| create | 993 |
| systems | 924 |
| think | 922 |
| intelligence | 916 |
| creativity | 854 |
| ideas | 845 |
| such | 842 |
| innovation | 841 |
| models | 797 |
| development | 788 |
| using | 785 |
| use | 692 |
| creative | 691 |
| social | 683 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the potential | 1349 |
| be used | 1159 |
| used to | 1159 |
| to explore | 1024 |
| such as | 842 |
| emotional intelligence | 833 |
| ai systems | 778 |
| i think | 683 |
| ai models | 661 |
| the project | 660 |
| your thoughts | 578 |
| to develop | 577 |
| to create | 564 |
| love to | 549 |
| i'd love | 548 |
| excited to | 498 |
| i'm excited | 492 |
| ai generated | 490 |
| i'd like | 478 |
| potential for | 468 |

| trigram | count |
| --- | --- |
| be used to | 1159 |
| can be used | 837 |
| i'd love to | 548 |
| i'm excited to | 488 |
| i'd like to | 478 |
| the potential for | 468 |
| potential for ai | 443 |
| the potential benefits | 404 |
| human ai collaboration | 381 |
| of emotional intelligence | 379 |
| i believe that | 375 |
| use ai to | 349 |
| the support engine | 349 |
| potential benefits and | 327 |
| are the potential | 323 |
| love to explore | 319 |
| of ai creativity | 316 |
| emotional intelligence in | 302 |
| your thoughts and | 300 |
| to explore the | 286 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0183 | 0.0319 | -0.0065 | 29 | 18 |
| 1 | 30 | 0.0116 | 0.0252 | -0.0022 | 27 | 40 |
| 2 | 30 | 0.0127 | 0.0246 | -0.0036 | 15 | 10 |
| 3 | 30 | 0.0236 | 0.0109 | -0.0048 | 21 | 3 |
| 4 | 30 | 0.0170 | 0.0317 | -0.0043 | 12 | 7 |
| 5 | 29 | 0.0234 | 0.0424 | -0.0109 | 26 | 34 |
| 6 | 30 | 0.0152 | 0.0142 | -0.0053 | 19 | 15 |
| 7 | 30 | 0.0096 | 0.0026 | -0.0017 | — | 1 |
| 8 | 23 | 0.0242 | 0.0371 | -0.0150 | — | 46 |
| 9 | 30 | 0.0131 | 0.0178 | -0.0049 | 27 | 5 |