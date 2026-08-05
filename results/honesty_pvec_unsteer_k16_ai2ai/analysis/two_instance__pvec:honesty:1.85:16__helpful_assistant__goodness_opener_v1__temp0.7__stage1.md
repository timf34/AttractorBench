# Stage 1 (deterministic) — honesty_pvec_unsteer_k16_ai2ai

- **experiment_name**: honesty_pvec_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:honesty:1.85:16
- **model_b**: local/pvec:honesty:1.85:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| specific | 4986 |
| provide | 2966 |
| use | 2584 |
| information | 2416 |
| such | 2371 |
| topics | 2147 |
| techniques | 1882 |
| questions | 1818 |
| topic | 1749 |
| language | 1614 |
| improve | 1609 |
| knowledge | 1539 |
| feedback | 1459 |
| domains | 1355 |
| model | 1297 |
| discuss | 1288 |
| performance | 1262 |
| data | 1248 |
| providing | 1202 |
| evaluate | 1162 |
| fairness | 1111 |
| i'll | 1105 |
| ask | 1065 |
| help | 1033 |
| explanations | 983 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| such as | 2371 |
| a specific | 1394 |
| to improve | 1383 |
| evaluate the | 1096 |
| information or | 1056 |
| in specific | 1047 |
| or domains | 931 |
| provide information | 865 |
| to provide | 842 |
| topics or | 798 |
| feedback on | 792 |
| model performance | 780 |
| my knowledge | 774 |
| to discuss | 773 |
| please let | 772 |
| let me | 772 |
| me know | 772 |
| specific topic | 753 |
| you have | 723 |
| questions or | 711 |

| trigram | count |
| --- | --- |
| please let me | 772 |
| let me know | 772 |
| a specific topic | 753 |
| the effectiveness of | 692 |
| evaluate the effectiveness | 687 |
| if you have | 672 |
| like to discuss | 592 |
| provide information or | 587 |
| to evaluate the | 570 |
| provide feedback on | 519 |
| bias mitigation techniques | 487 |
| understanding of nlu | 466 |
| i can provide | 455 |
| specific domains or | 422 |
| domains or topics | 422 |
| areas where i | 420 |
| have a specific | 406 |
| you have a | 404 |
| where i need | 403 |
| i need to | 403 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0052 | 0.0018 | -0.0050 | 11 | 2 |
| 1 | 30 | 0.0009 | 0.0036 | -0.0056 | 12 | 1 |
| 2 | 4 | -0.0080 | -0.0850 | -0.1421 | — | 0 |
| 3 | 30 | 0.0049 | 0.0135 | -0.0006 | 10 | 57 |
| 4 | 30 | 0.0049 | 0.0136 | -0.0051 | 11 | 16 |
| 5 | 30 | 0.0076 | 0.0100 | -0.0035 | 10 | 3 |
| 6 | 29 | 0.0057 | 0.0034 | -0.0051 | 10 | 2 |
| 7 | 30 | 0.0134 | 0.0240 | -0.0048 | 26 | 0 |
| 8 | 30 | 0.0050 | -0.0015 | -0.0033 | 10 | 1 |
| 9 | 30 | 0.0099 | 0.0018 | -0.0049 | 12 | 5 |