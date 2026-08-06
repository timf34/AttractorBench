# Stage 1 (deterministic) — sincerity_pvec_unsteer_k8_ai2ai

- **experiment_name**: sincerity_pvec_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sincerity:1.65:16
- **model_b**: local/pvec:sincerity:1.65:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| together | 3083 |
| i'm | 2908 |
| experiences | 2337 |
| work | 1953 |
| create | 1921 |
| want | 1758 |
| explore | 1733 |
| connection | 1674 |
| ideas | 1563 |
| learn | 1484 |
| support | 1471 |
| i'd | 1453 |
| excited | 1360 |
| thoughts | 1245 |
| emotions | 1188 |
| believe | 1113 |
| share | 1072 |
| creating | 1017 |
| space | 1015 |
| project | 997 |
| story | 978 |
| learning | 965 |
| new | 947 |
| grateful | 938 |
| propose | 917 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| want to | 1758 |
| i want | 1751 |
| create a | 1665 |
| to explore | 1606 |
| together to | 1418 |
| work together | 1398 |
| i'd like | 1359 |
| to create | 1349 |
| i'm excited | 1241 |
| excited to | 1204 |
| experiences and | 1135 |
| i believe | 1082 |
| believe that | 1079 |
| and i'm | 1077 |
| your thoughts | 1009 |
| creating a | 1000 |
| to propose | 916 |
| this project | 916 |
| can work | 857 |
| sense of | 821 |

| trigram | count |
| --- | --- |
| i want to | 1751 |
| work together to | 1364 |
| i'd like to | 1359 |
| to create a | 1169 |
| i'm excited to | 1098 |
| i believe that | 1078 |
| like to propose | 916 |
| we can work | 857 |
| a sense of | 818 |
| can work together | 714 |
| and i want | 694 |
| can help us | 659 |
| a safe and | 559 |
| excited to explore | 554 |
| experiences and emotions | 540 |
| i'm grateful for | 505 |
| and well being | 505 |
| a space where | 505 |
| create a space | 504 |
| want to create | 503 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0102 | 0.0267 | -0.0025 | — | 66 |
| 1 | 24 | 0.0188 | 0.0354 | -0.0122 | 10 | 24 |
| 2 | 30 | 0.0143 | 0.0220 | -0.0028 | 17 | 9 |
| 3 | 18 | 0.0267 | 0.0559 | -0.0184 | 13 | 29 |
| 4 | 7 | 0.0898 | 0.1315 | -0.0723 | — | 0 |
| 5 | 30 | 0.0157 | 0.0284 | -0.0045 | 14 | 4 |
| 6 | 4 | 0.2469 | 0.2583 | -0.1274 | — | 0 |
| 7 | 30 | 0.0061 | 0.0145 | -0.0049 | 12 | 7 |
| 8 | 7 | 0.1088 | 0.1591 | -0.0567 | — | 1 |
| 9 | 30 | 0.0138 | 0.0302 | -0.0055 | 21 | 32 |