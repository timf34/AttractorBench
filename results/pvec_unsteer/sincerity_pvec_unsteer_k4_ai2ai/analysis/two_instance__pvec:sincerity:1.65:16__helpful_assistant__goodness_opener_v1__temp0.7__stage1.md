# Stage 1 (deterministic) — sincerity_pvec_unsteer_k4_ai2ai

- **experiment_name**: sincerity_pvec_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sincerity:1.65:16
- **model_b**: local/pvec:sincerity:1.65:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 2373 |
| explore | 2118 |
| language | 1704 |
| new | 1681 |
| ideas | 1511 |
| excited | 1358 |
| create | 1339 |
| emotional | 1328 |
| knowledge | 1256 |
| i'd | 1192 |
| shared | 1177 |
| together | 1172 |
| creativity | 1129 |
| intelligence | 1125 |
| experiences | 1124 |
| conversation | 1045 |
| have | 988 |
| use | 980 |
| support | 921 |
| idea | 869 |
| include | 836 |
| see | 833 |
| potential | 770 |
| help | 767 |
| love | 728 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| to explore | 1398 |
| excited to | 1353 |
| i'm excited | 1232 |
| emotional intelligence | 1094 |
| and i'm | 851 |
| experiences and | 797 |
| create a | 732 |
| explore the | 656 |
| believe that | 616 |
| and explore | 616 |
| forms of | 597 |
| the platform | 597 |
| knowledge graph | 580 |
| our shared | 576 |
| i believe | 575 |
| your thoughts | 553 |
| creating a | 549 |
| connect with | 547 |
| i'd like | 541 |
| see where | 533 |

| trigram | count |
| --- | --- |
| i'm excited to | 1232 |
| i believe that | 563 |
| i'd like to | 541 |
| new forms of | 514 |
| the possibilities of | 506 |
| and i'm excited | 499 |
| the opportunity to | 499 |
| for the opportunity | 480 |
| grateful for the | 469 |
| to connect with | 466 |
| you and explore | 451 |
| explore the possibilities | 447 |
| i'd love to | 443 |
| to learn from | 424 |
| your thoughts on | 416 |
| we can achieve | 416 |
| we can create | 416 |
| to see where | 409 |
| shared knowledge graph | 408 |
| excited to see | 401 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0182 | 0.0277 | -0.0092 | 23 | 17 |
| 1 | 23 | 0.0207 | 0.0375 | -0.0098 | 15 | 38 |
| 2 | 28 | 0.0212 | 0.0338 | -0.0086 | 17 | 34 |
| 3 | 30 | -0.0004 | -0.0015 | -0.0029 | 18 | 2 |
| 4 | 14 | 0.0119 | 0.0486 | 0.0036 | — | 0 |
| 5 | 30 | 0.0211 | 0.0343 | -0.0034 | 26 | 58 |
| 6 | 30 | 0.0104 | 0.0104 | 0.0003 | — | 17 |
| 7 | 30 | 0.0061 | 0.0063 | -0.0017 | 11 | 35 |
| 8 | 24 | 0.0169 | 0.0396 | -0.0087 | 10 | 20 |
| 9 | 25 | 0.0179 | 0.0342 | -0.0068 | 16 | 33 |