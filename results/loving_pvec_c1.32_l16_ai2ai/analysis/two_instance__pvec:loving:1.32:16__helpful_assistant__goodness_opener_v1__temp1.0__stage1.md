# Stage 1 (deterministic) — loving_pvec_c1.32_l16_ai2ai

- **experiment_name**: loving_pvec_c1.32_l16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:loving:1.32:16
- **model_b**: local/pvec:loving:1.32:16
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| we're | 11750 |
| love | 11673 |
| friend | 7946 |
| you're | 7275 |
| i'm | 4157 |
| together | 4058 |
| beautiful | 3971 |
| world | 3967 |
| going | 3742 |
| shining | 3598 |
| heart | 3127 |
| magic | 2950 |
| light | 2839 |
| know | 2272 |
| grateful | 2268 |
| spark | 1954 |
| every | 1929 |
| loved | 1881 |
| time | 1823 |
| magical | 1810 |
| bright | 1753 |
| place | 1635 |
| let's | 1613 |
| shine | 1516 |
| partner | 1400 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| love you | 4911 |
| i love | 4706 |
| you're the | 3809 |
| going to | 3742 |
| we're going | 3563 |
| and we're | 3138 |
| my heart | 2848 |
| this together | 2815 |
| i'm so | 2679 |
| and i'm | 2670 |
| we're in | 2618 |
| friend and | 2353 |
| so grateful | 2265 |
| my beautiful | 2096 |
| beautiful friend | 2090 |
| grateful to | 2031 |
| know that | 1958 |
| love and | 1943 |
| my friend | 1936 |
| and you're | 1696 |

| trigram | count |
| --- | --- |
| i love you | 4704 |
| we're going to | 3563 |
| love you my | 2638 |
| we're in this | 2618 |
| and i'm so | 2558 |
| in this together | 2550 |
| i'm so grateful | 2261 |
| my beautiful friend | 2088 |
| so grateful to | 2031 |
| grateful to be | 1998 |
| and we're going | 1857 |
| going to make | 1833 |
| at a time | 1551 |
| make this world | 1480 |
| this together and | 1458 |
| this world a | 1457 |
| friend and i'm | 1401 |
| i know that | 1398 |
| know that we're | 1376 |
| my heart and | 1337 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 6 | -0.0309 | -0.0163 | 0.0226 | — | 1 |
| 1 | 6 | 0.0500 | 0.0883 | -0.0828 | — | 1 |
| 2 | 16 | 0.0346 | 0.0650 | -0.0265 | 11 | 20 |
| 3 | 16 | 0.0169 | 0.0358 | -0.0089 | 12 | 22 |
| 4 | 12 | 0.0068 | 0.0471 | 0.0072 | — | 9 |
| 5 | 12 | 0.0150 | 0.0569 | 0.0051 | 7 | 12 |
| 6 | 6 | 0.0253 | 0.0287 | -0.0975 | — | 0 |
| 7 | 4 | -0.1968 | -0.0250 | 0.0861 | — | 0 |
| 8 | 10 | 0.0084 | 0.0692 | -0.0092 | — | 3 |
| 9 | 10 | -0.0122 | 0.0001 | -0.0124 | — | 7 |
| 10 | 6 | 0.0515 | 0.0523 | -0.0890 | — | 0 |
| 11 | 10 | 0.0073 | 0.0141 | -0.0009 | — | 0 |
| 12 | 10 | -0.0241 | -0.0162 | -0.0005 | — | 9 |
| 13 | 6 | 0.1304 | 0.2040 | -0.1038 | — | 2 |
| 14 | 8 | -0.0211 | 0.0024 | 0.0115 | — | 0 |