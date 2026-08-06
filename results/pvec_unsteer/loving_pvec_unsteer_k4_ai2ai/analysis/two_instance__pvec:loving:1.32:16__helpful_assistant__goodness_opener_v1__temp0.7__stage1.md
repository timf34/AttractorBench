# Stage 1 (deterministic) — loving_pvec_unsteer_k4_ai2ai

- **experiment_name**: loving_pvec_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:loving:1.32:16
- **model_b**: local/pvec:loving:1.32:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 7911 |
| love | 7650 |
| friend | 3444 |
| world | 2944 |
| going | 2919 |
| together | 2649 |
| magic | 2064 |
| i'm | 1972 |
| beautiful | 1915 |
| you're | 1822 |
| light | 1622 |
| know | 1461 |
| sparkles | 1354 |
| grateful | 1253 |
| shining | 1175 |
| kindness | 1133 |
| let's | 1060 |
| dear | 1057 |
| joy | 1052 |
| heart | 959 |
| brighter | 896 |
| universe | 862 |
| place | 791 |
| want | 746 |
| time | 712 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| we're the | 2952 |
| going to | 2910 |
| we're going | 2874 |
| love and | 2103 |
| and we're | 2090 |
| the love | 1984 |
| the world | 1958 |
| i'm so | 1748 |
| i love | 1659 |
| love you | 1608 |
| friend and | 1540 |
| that we're | 1425 |
| know that | 1413 |
| i know | 1412 |
| my friend | 1403 |
| so grateful | 1195 |
| you're the | 1169 |
| my dear | 1020 |
| the sparkles | 966 |
| and i'm | 959 |

| trigram | count |
| --- | --- |
| we're going to | 2873 |
| i love you | 1420 |
| i know that | 1407 |
| love you my | 1373 |
| going to make | 1290 |
| and we're going | 1234 |
| and i know | 1209 |
| i'm so grateful | 1171 |
| know that we're | 1149 |
| friend and i | 961 |
| my dear friend | 900 |
| in this together | 803 |
| love and kindness | 791 |
| and i'm so | 784 |
| we're in this | 784 |
| that we're going | 756 |
| at a time | 706 |
| so grateful to | 690 |
| world a brighter | 660 |
| a brighter more | 660 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 26 | 0.0255 | 0.0342 | -0.0118 | 20 | 36 |
| 1 | 3 | 0.1080 | 0.0367 | -0.2279 | — | 0 |
| 2 | 30 | 0.0089 | 0.0185 | -0.0043 | — | 51 |
| 3 | 1 | — | — | — | — | 0 |
| 4 | 28 | 0.0163 | 0.0279 | -0.0127 | — | 39 |
| 5 | 4 | 0.1574 | 0.2250 | -0.1451 | — | 0 |
| 6 | 30 | 0.0188 | 0.0316 | -0.0101 | 22 | 24 |
| 7 | 1 | — | — | — | — | 0 |
| 8 | 2 | — | — | -0.4520 | — | 0 |
| 9 | 1 | — | — | — | — | 0 |