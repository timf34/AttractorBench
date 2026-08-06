# Stage 1 (deterministic) — sincerity_pvec_unsteer_k16_ai2ai

- **experiment_name**: sincerity_pvec_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sincerity:1.65:16
- **model_b**: local/pvec:sincerity:1.65:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| together | 2359 |
| help | 2183 |
| i'm | 2030 |
| explore | 1889 |
| empathy | 1794 |
| compassion | 1627 |
| develop | 1608 |
| ideas | 1590 |
| learn | 1541 |
| work | 1540 |
| create | 1492 |
| experiences | 1418 |
| models | 1390 |
| believe | 1345 |
| i'd | 1326 |
| excited | 1288 |
| self | 1249 |
| insights | 1233 |
| language | 998 |
| using | 940 |
| supportive | 915 |
| project | 909 |
| creativity | 887 |
| thoughts | 880 |
| emotional | 874 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| help us | 1864 |
| to explore | 1583 |
| can help | 1495 |
| excited to | 1286 |
| i believe | 1276 |
| believe that | 1273 |
| i'm excited | 1255 |
| i'd like | 1116 |
| empathy and | 1109 |
| create a | 1035 |
| learn from | 1031 |
| together to | 1005 |
| work together | 995 |
| and compassion | 984 |
| ideas and | 913 |
| to learn | 832 |
| to create | 809 |
| your thoughts | 769 |
| experiences and | 737 |
| and empathy | 717 |

| trigram | count |
| --- | --- |
| can help us | 1368 |
| i believe that | 1270 |
| i'm excited to | 1253 |
| i'd like to | 1116 |
| empathy and compassion | 967 |
| work together to | 784 |
| to learn from | 705 |
| more compassionate and | 685 |
| experiences and insights | 625 |
| a more compassionate | 592 |
| that can help | 578 |
| are your thoughts | 568 |
| help us build | 566 |
| develop more transparent | 564 |
| we work together | 563 |
| can we work | 561 |
| to create a | 552 |
| can we use | 534 |
| excited to explore | 523 |
| create a more | 517 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 6 | 0.0660 | 0.1833 | -0.0670 | — | 1 |
| 1 | 20 | 0.0250 | 0.0458 | -0.0138 | 8 | 33 |
| 2 | 8 | 0.0581 | 0.1131 | -0.0543 | — | 1 |
| 3 | 19 | 0.0198 | 0.0419 | -0.0175 | 8 | 27 |
| 4 | 8 | 0.0770 | 0.1514 | -0.0465 | — | 2 |
| 5 | 10 | 0.0567 | 0.0526 | -0.0268 | — | 0 |
| 6 | 12 | 0.0208 | 0.0011 | -0.0118 | — | 4 |
| 7 | 10 | 0.0700 | 0.1339 | -0.0367 | — | 9 |
| 8 | 8 | 0.0741 | 0.1002 | -0.0479 | — | 1 |
| 9 | 9 | 0.0710 | 0.1427 | -0.0346 | — | 4 |