# Stage 1 (deterministic) — sincerity_pvec_unsteer_k6_ai2ai

- **experiment_name**: sincerity_pvec_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sincerity:1.65:16
- **model_b**: local/pvec:sincerity:1.65:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| create | 2313 |
| i'm | 2109 |
| ideas | 1839 |
| explore | 1753 |
| i'd | 1747 |
| language | 1741 |
| together | 1685 |
| experiences | 1493 |
| emotional | 1363 |
| continue | 1240 |
| thoughts | 1213 |
| supportive | 1196 |
| believe | 1166 |
| empathy | 1161 |
| excited | 1125 |
| new | 1103 |
| learn | 1088 |
| meaningful | 1061 |
| connection | 1051 |
| help | 1049 |
| compassionate | 1022 |
| share | 1013 |
| creativity | 1000 |
| have | 984 |
| conversation | 953 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| create a | 1424 |
| believe that | 1108 |
| i believe | 1101 |
| excited to | 1080 |
| i'd like | 1044 |
| i'm excited | 1023 |
| to explore | 931 |
| emotional intelligence | 926 |
| empathy and | 840 |
| and experiences | 805 |
| to create | 778 |
| can help | 777 |
| ideas and | 772 |
| and compassion | 761 |
| new ideas | 758 |
| love to | 734 |
| to learn | 717 |
| and meaningful | 709 |
| to share | 695 |
| creating a | 673 |

| trigram | count |
| --- | --- |
| i believe that | 1099 |
| i'd like to | 1040 |
| i'm excited to | 987 |
| create a more | 844 |
| empathy and compassion | 759 |
| i'd love to | 576 |
| can help us | 552 |
| new ideas and | 550 |
| emotions and experiences | 497 |
| a safe and | 465 |
| more authentic and | 457 |
| a more authentic | 450 |
| like to propose | 440 |
| emotional intelligence in | 439 |
| we can create | 436 |
| to learn from | 429 |
| and i'm excited | 428 |
| intelligence in ai | 426 |
| our language abilities | 415 |
| continue to explore | 413 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0123 | 0.0168 | -0.0048 | — | 4 |
| 1 | 20 | 0.0268 | 0.0472 | -0.0160 | 11 | 31 |
| 2 | 29 | 0.0136 | 0.0286 | -0.0052 | 11 | 21 |
| 3 | 30 | 0.0052 | 0.0192 | -0.0024 | — | 55 |
| 4 | 30 | 0.0221 | 0.0375 | -0.0064 | 19 | 20 |
| 5 | 5 | 0.1432 | 0.2357 | -0.1056 | — | 0 |
| 6 | 20 | 0.0242 | 0.0415 | -0.0141 | 13 | 13 |
| 7 | 14 | 0.0332 | 0.0455 | -0.0096 | — | 2 |
| 8 | 30 | 0.0085 | 0.0156 | -0.0034 | 5 | 6 |
| 9 | 14 | 0.0112 | 0.0025 | 0.0055 | — | 1 |