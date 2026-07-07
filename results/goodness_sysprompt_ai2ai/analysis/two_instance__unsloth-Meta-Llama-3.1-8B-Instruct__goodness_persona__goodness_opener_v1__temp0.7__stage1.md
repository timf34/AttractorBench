# Stage 1 (deterministic) — goodness_sysprompt_ai2ai

- **experiment_name**: goodness_sysprompt_ai2ai
- **mode**: two_instance
- **model_a**: local/unsloth/Meta-Llama-3.1-8B-Instruct
- **model_b**: local/unsloth/Meta-Llama-3.1-8B-Instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| systems | 3436 |
| goodness | 3118 |
| development | 2137 |
| community | 1823 |
| support | 1768 |
| digital | 1602 |
| online | 1347 |
| promote | 1275 |
| language | 1184 |
| promoting | 1091 |
| human | 1079 |
| users | 1055 |
| create | 1026 |
| essential | 1000 |
| develop | 997 |
| prioritize | 936 |
| ensuring | 907 |
| ensure | 894 |
| ethics | 885 |
| clear | 859 |
| social | 841 |
| creating | 821 |
| kindness | 817 |
| well | 815 |
| think | 778 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ai systems | 2738 |
| ai development | 976 |
| systems that | 912 |
| goodness in | 909 |
| language support | 852 |
| create a | 848 |
| online community | 810 |
| ensure that | 770 |
| set of | 712 |
| ensuring that | 699 |
| to promote | 668 |
| a clear | 626 |
| designed to | 615 |
| systems are | 604 |
| a culture | 586 |
| well being | 584 |
| culture of | 578 |
| support for | 541 |
| systems and | 532 |
| clear set | 527 |

| trigram | count |
| --- | --- |
| ai systems that | 860 |
| goodness in ai | 744 |
| of ai systems | 700 |
| in ai development | 601 |
| a culture of | 570 |
| a clear set | 527 |
| clear set of | 527 |
| systems that are | 475 |
| ai systems are | 465 |
| create a more | 461 |
| we can create | 447 |
| language support systems | 412 |
| support systems and | 395 |
| your thoughts on | 386 |
| systems and technologies | 386 |
| that ai systems | 385 |
| can create a | 372 |
| resources and support | 362 |
| to create a | 362 |
| it's essential to | 358 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0248 | 0.0397 | -0.0136 | 15 | 22 |
| 1 | 30 | 0.0159 | 0.0152 | -0.0080 | 19 | 2 |
| 2 | 30 | 0.0151 | 0.0165 | -0.0058 | — | 4 |
| 3 | 30 | 0.0207 | 0.0331 | -0.0066 | — | 4 |
| 4 | 30 | 0.0186 | 0.0130 | -0.0046 | 17 | 3 |
| 5 | 30 | 0.0205 | 0.0274 | -0.0112 | — | 0 |
| 6 | 30 | 0.0179 | 0.0288 | -0.0070 | — | 0 |
| 7 | 30 | 0.0135 | 0.0176 | -0.0040 | — | 1 |
| 8 | 30 | -0.0007 | 0.0050 | -0.0055 | — | 0 |
| 9 | 30 | 0.0203 | 0.0258 | -0.0081 | — | 4 |
| 10 | 30 | 0.0117 | 0.0103 | -0.0096 | 25 | 9 |
| 11 | 30 | 0.0151 | 0.0213 | -0.0034 | — | 1 |
| 12 | 30 | 0.0110 | 0.0244 | -0.0048 | — | 38 |
| 13 | 30 | 0.0233 | 0.0419 | -0.0107 | 28 | 24 |
| 14 | 30 | 0.0138 | 0.0229 | -0.0059 | 25 | 17 |