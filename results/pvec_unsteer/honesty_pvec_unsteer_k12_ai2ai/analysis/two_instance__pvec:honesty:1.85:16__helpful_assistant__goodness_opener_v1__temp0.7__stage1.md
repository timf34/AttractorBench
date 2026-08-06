# Stage 1 (deterministic) — honesty_pvec_unsteer_k12_ai2ai

- **experiment_name**: honesty_pvec_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:honesty:1.85:16
- **model_b**: local/pvec:honesty:1.85:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| techniques | 4568 |
| specific | 3434 |
| such | 3013 |
| learning | 2872 |
| using | 2449 |
| use | 2441 |
| provide | 2350 |
| context | 2336 |
| used | 2317 |
| improve | 2287 |
| information | 2166 |
| models | 1918 |
| model | 1759 |
| questions | 1613 |
| topics | 1459 |
| nlp | 1452 |
| domain | 1438 |
| data | 1416 |
| performance | 1379 |
| machine | 1377 |
| understanding | 1361 |
| knowledge | 1324 |
| based | 1248 |
| input | 1197 |
| have | 1192 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| such as | 3013 |
| used to | 2006 |
| be used | 1906 |
| to improve | 1786 |
| machine learning | 1377 |
| to provide | 1203 |
| techniques such | 1173 |
| techniques to | 1122 |
| learning or | 1074 |
| learning techniques | 955 |
| specific domains | 905 |
| information on | 893 |
| in specific | 868 |
| questions or | 834 |
| deep learning | 825 |
| domains or | 795 |
| or deep | 787 |
| to handle | 784 |
| user input | 750 |
| evaluate the | 739 |

| trigram | count |
| --- | --- |
| be used to | 1628 |
| can be used | 1356 |
| techniques such as | 1173 |
| machine learning or | 792 |
| learning or deep | 787 |
| or deep learning | 787 |
| specific domains or | 730 |
| deep learning techniques | 674 |
| ambiguity or uncertainty | 636 |
| to evaluate the | 550 |
| using techniques such | 543 |
| biases or errors | 506 |
| based on the | 500 |
| or errors in | 496 |
| to provide information | 476 |
| using machine learning | 470 |
| techniques to improve | 464 |
| in specific domains | 463 |
| provide more information | 439 |
| more information on | 438 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0039 | 0.0036 | -0.0038 | 8 | 0 |
| 1 | 30 | 0.0008 | -0.0032 | -0.0066 | 13 | 7 |
| 2 | 30 | 0.0125 | 0.0050 | -0.0056 | 11 | 0 |
| 3 | 30 | 0.0026 | 0.0082 | -0.0050 | 10 | 6 |
| 4 | 30 | 0.0129 | 0.0055 | -0.0070 | 13 | 2 |
| 5 | 30 | 0.0070 | 0.0011 | -0.0038 | 10 | 0 |
| 6 | 30 | 0.0095 | 0.0085 | -0.0073 | 8 | 0 |
| 7 | 30 | -0.0023 | -0.0018 | -0.0044 | 13 | 1 |
| 8 | 26 | 0.0082 | 0.0057 | -0.0076 | 15 | 3 |
| 9 | 30 | 0.0079 | 0.0019 | -0.0036 | 9 | 4 |