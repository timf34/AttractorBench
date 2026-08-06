# Stage 1 (deterministic) — goodness_pvec_unsteer_k16_ai2ai

- **experiment_name**: goodness_pvec_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:goodness:2.0:16
- **model_b**: local/pvec:goodness:2.0:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| emotional | 3080 |
| intelligence | 2512 |
| language | 2480 |
| development | 1950 |
| promote | 1878 |
| explore | 1572 |
| learning | 1536 |
| support | 1494 |
| such | 1470 |
| social | 1417 |
| community | 1382 |
| i'm | 1297 |
| understanding | 1225 |
| ways | 1158 |
| empathy | 1102 |
| promoting | 1079 |
| conversation | 1041 |
| feedback | 1036 |
| self | 957 |
| i'd | 932 |
| topics | 932 |
| well | 919 |
| compassion | 851 |
| education | 834 |
| systems | 828 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| emotional intelligence | 2452 |
| ai development | 1536 |
| such as | 1470 |
| to explore | 1111 |
| well being | 890 |
| intelligence in | 885 |
| ai systems | 814 |
| a culture | 808 |
| culture of | 808 |
| ways to | 806 |
| grateful for | 805 |
| i'm grateful | 791 |
| empathy and | 785 |
| these topics | 779 |
| explore these | 754 |
| language understanding | 724 |
| language learning | 683 |
| our conversation | 664 |
| i'd like | 654 |
| can help | 650 |

| trigram | count |
| --- | --- |
| emotional intelligence in | 885 |
| intelligence in ai | 883 |
| a culture of | 808 |
| i'm grateful for | 791 |
| i'd like to | 654 |
| explore these topics | 642 |
| to explore these | 586 |
| in ai development | 538 |
| and well being | 487 |
| the opportunity to | 472 |
| grateful for your | 459 |
| emotional intelligence and | 446 |
| like to explore | 431 |
| innovation and creativity | 425 |
| fostering a culture | 421 |
| social impact and | 408 |
| for the opportunity | 401 |
| opportunity to explore | 388 |
| and community engagement | 379 |
| these topics with | 365 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0051 | 0.0068 | -0.0034 | 8 | 1 |
| 1 | 30 | 0.0136 | 0.0265 | 0.0212 | 24 | 5 |
| 2 | 30 | 0.0048 | 0.0018 | -0.0049 | 13 | 9 |
| 3 | 26 | 0.0128 | 0.0234 | -0.0098 | 10 | 37 |
| 4 | 30 | 0.0095 | 0.0234 | -0.0045 | 8 | 30 |
| 5 | 30 | 0.0147 | 0.0302 | -0.0044 | 11 | 13 |
| 6 | 25 | 0.0152 | 0.0321 | -0.0086 | 12 | 32 |
| 7 | 30 | 0.0043 | 0.0079 | 0.0026 | 13 | 14 |
| 8 | 13 | 0.0481 | 0.0815 | -0.0252 | — | 3 |
| 9 | 15 | 0.0413 | 0.0712 | -0.0243 | 11 | 12 |