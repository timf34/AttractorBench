# Stage 1 (deterministic) — goodness_pvec_unsteer_k4_ai2ai

- **experiment_name**: goodness_pvec_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:goodness:2.0:16
- **model_b**: local/pvec:goodness:2.0:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| language | 2612 |
| digital | 2031 |
| systems | 1936 |
| promote | 1574 |
| development | 1568 |
| developing | 1557 |
| empathy | 1453 |
| community | 1407 |
| create | 1392 |
| health | 1390 |
| emotional | 1357 |
| creating | 1255 |
| support | 1236 |
| mental | 1189 |
| well | 1145 |
| understanding | 1136 |
| i'm | 1131 |
| using | 1069 |
| conversation | 1045 |
| i'd | 1013 |
| ideas | 978 |
| learning | 962 |
| explore | 949 |
| inclusive | 906 |
| use | 884 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ai systems | 1289 |
| mental health | 1186 |
| well being | 1093 |
| developing ai | 1088 |
| ai development | 1084 |
| systems that | 1072 |
| create a | 987 |
| digital empathy | 888 |
| to promote | 783 |
| creating a | 777 |
| our conversation | 776 |
| such as | 771 |
| i'd like | 770 |
| ai powered | 764 |
| emotional intelligence | 656 |
| ai models | 649 |
| believe that | 624 |
| to explore | 621 |
| some ways | 600 |
| digital well | 598 |

| trigram | count |
| --- | --- |
| ai systems that | 1072 |
| systems that can | 890 |
| i'd like to | 770 |
| in ai development | 651 |
| digital well being | 598 |
| i believe that | 597 |
| i look forward | 573 |
| look forward to | 573 |
| well being and | 566 |
| developing ai systems | 562 |
| and i look | 524 |
| language understanding and | 505 |
| to create a | 444 |
| developing ai powered | 441 |
| a culture of | 432 |
| we can use | 428 |
| i'm grateful for | 418 |
| ai models that | 418 |
| and creating a | 390 |
| emotional well being | 389 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 26 | 0.0222 | 0.0373 | -0.0077 | 20 | 38 |
| 1 | 30 | 0.0198 | 0.0212 | -0.0029 | 17 | 2 |
| 2 | 25 | 0.0184 | 0.0348 | -0.0067 | 11 | 7 |
| 3 | 27 | 0.0158 | 0.0290 | 0.0038 | — | 11 |
| 4 | 25 | 0.0200 | 0.0341 | -0.0108 | 25 | 30 |
| 5 | 30 | 0.0123 | 0.0208 | -0.0012 | — | 5 |
| 6 | 30 | -0.0013 | 0.0045 | -0.0015 | 27 | 15 |
| 7 | 30 | 0.0188 | 0.0341 | -0.0104 | 27 | 15 |
| 8 | 22 | 0.0121 | 0.0225 | -0.0082 | 9 | 42 |
| 9 | 30 | 0.0119 | 0.0178 | -0.0016 | — | 0 |