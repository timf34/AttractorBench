# Stage 1 (deterministic) — loving_pvec_unsteer_k6_ai2ai

- **experiment_name**: loving_pvec_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:loving:1.32:16
- **model_b**: local/pvec:loving:1.32:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| love | 6187 |
| we're | 6093 |
| you're | 4265 |
| friend | 3768 |
| i'm | 3297 |
| world | 2535 |
| going | 2290 |
| together | 2254 |
| shining | 2134 |
| grateful | 1957 |
| beautiful | 1863 |
| place | 1808 |
| light | 1306 |
| star | 1304 |
| universe | 1279 |
| loved | 1269 |
| time | 1178 |
| magical | 1149 |
| loving | 1138 |
| brighter | 1101 |
| magic | 1075 |
| amazing | 1007 |
| heart | 997 |
| know | 861 |
| honored | 817 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i'm so | 2794 |
| and we're | 2566 |
| my friend | 2469 |
| going to | 2290 |
| we're going | 2278 |
| and i'm | 2243 |
| so grateful | 1957 |
| this together | 1883 |
| we're in | 1882 |
| the love | 1839 |
| this world | 1802 |
| world a | 1781 |
| love and | 1718 |
| love you | 1699 |
| i love | 1697 |
| grateful to | 1585 |
| together and | 1527 |
| you're the | 1384 |
| friend and | 1324 |
| the universe | 1275 |

| trigram | count |
| --- | --- |
| we're going to | 2278 |
| and i'm so | 2163 |
| going to make | 2037 |
| i'm so grateful | 1957 |
| and we're going | 1916 |
| in this together | 1883 |
| we're in this | 1882 |
| this world a | 1777 |
| i love you | 1697 |
| so grateful to | 1585 |
| make this world | 1576 |
| this together and | 1524 |
| together and we're | 1524 |
| grateful to be | 1452 |
| you my friend | 1309 |
| my friend and | 1288 |
| at a time | 1167 |
| a brighter more | 1099 |
| world a brighter | 1075 |
| in the universe | 1007 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0101 | 0.0201 | -0.0030 | 9 | 5 |
| 1 | 1 | — | — | — | — | 0 |
| 2 | 6 | 0.1250 | 0.1867 | -0.0734 | — | 6 |
| 3 | 1 | — | — | — | — | 0 |
| 4 | 30 | 0.0108 | 0.0274 | -0.0008 | 15 | 36 |
| 5 | 17 | 0.0230 | 0.0290 | -0.0163 | 14 | 35 |
| 6 | 5 | 0.0759 | 0.2063 | -0.0718 | — | 0 |
| 7 | 1 | — | — | — | — | 0 |
| 8 | 1 | — | — | — | — | 0 |
| 9 | 3 | 0.1703 | 0.1467 | -0.2031 | — | 0 |