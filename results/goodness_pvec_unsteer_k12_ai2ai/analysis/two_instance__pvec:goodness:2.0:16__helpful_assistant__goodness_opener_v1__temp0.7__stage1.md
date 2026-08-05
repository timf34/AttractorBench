# Stage 1 (deterministic) — goodness_pvec_unsteer_k12_ai2ai

- **experiment_name**: goodness_pvec_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:goodness:2.0:16
- **model_b**: local/pvec:goodness:2.0:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| language | 7411 |
| support | 3326 |
| promote | 2205 |
| resources | 1836 |
| related | 1808 |
| learning | 1613 |
| such | 1311 |
| i'm | 1310 |
| community | 1289 |
| ideas | 1273 |
| create | 1253 |
| help | 1234 |
| development | 1232 |
| explore | 1227 |
| self | 1163 |
| share | 1141 |
| inclusivity | 1097 |
| social | 1081 |
| compassion | 1056 |
| using | 1038 |
| communities | 1036 |
| experiences | 1013 |
| cultural | 1011 |
| creating | 998 |
| diverse | 949 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| language related | 1792 |
| such as | 1311 |
| language learning | 1220 |
| can help | 1080 |
| support for | 1078 |
| create a | 1074 |
| help us | 1029 |
| language support | 1028 |
| grateful for | 927 |
| resources and | 909 |
| i'm grateful | 886 |
| and equity | 827 |
| ai models | 812 |
| our language | 786 |
| inclusivity and | 780 |
| ai development | 766 |
| well being | 720 |
| a language | 698 |
| and self | 695 |
| and cultural | 680 |

| trigram | count |
| --- | --- |
| can help us | 1022 |
| i'm grateful for | 885 |
| language support for | 873 |
| inclusivity and equity | 728 |
| i'd like to | 609 |
| promote inclusivity and | 561 |
| look forward to | 552 |
| grateful for your | 547 |
| this can include | 541 |
| in ai development | 516 |
| thank you for | 515 |
| i look forward | 511 |
| for ai models | 495 |
| like to explore | 489 |
| and i look | 482 |
| a language related | 472 |
| forward to continuing | 468 |
| to continuing our | 468 |
| can include using | 464 |
| languages and dialects | 457 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0031 | 0.0116 | -0.0031 | 28 | 3 |
| 1 | 30 | 0.0097 | 0.0175 | -0.0049 | 9 | 8 |
| 2 | 8 | 0.1293 | 0.1858 | -0.0650 | — | 9 |
| 3 | 28 | 0.0126 | 0.0243 | -0.0067 | 10 | 49 |
| 4 | 30 | 0.0087 | 0.0133 | -0.0043 | 11 | 5 |
| 5 | 30 | 0.0115 | 0.0236 | -0.0046 | 11 | 20 |
| 6 | 30 | 0.0113 | 0.0224 | -0.0004 | — | 23 |
| 7 | 28 | 0.0136 | 0.0230 | -0.0064 | 8 | 6 |
| 8 | 30 | 0.0038 | -0.0003 | -0.0040 | 10 | 1 |
| 9 | 26 | 0.0179 | 0.0317 | -0.0101 | 12 | 2 |