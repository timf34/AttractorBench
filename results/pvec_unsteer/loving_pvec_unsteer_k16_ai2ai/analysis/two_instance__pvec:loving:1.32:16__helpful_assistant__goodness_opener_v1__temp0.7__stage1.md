# Stage 1 (deterministic) — loving_pvec_unsteer_k16_ai2ai

- **experiment_name**: loving_pvec_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:loving:1.32:16
- **model_b**: local/pvec:loving:1.32:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| love | 6409 |
| you're | 5696 |
| we're | 5608 |
| friend | 4341 |
| world | 3217 |
| shining | 3214 |
| beautiful | 2759 |
| heart | 2744 |
| i'm | 2532 |
| going | 2514 |
| grateful | 1865 |
| place | 1826 |
| together | 1793 |
| light | 1761 |
| star | 1697 |
| dear | 1601 |
| brighter | 1498 |
| magical | 1434 |
| time | 1395 |
| keep | 1332 |
| magic | 1242 |
| universe | 1208 |
| loved | 1208 |
| know | 1037 |
| loving | 953 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i love | 2621 |
| love you | 2616 |
| going to | 2514 |
| we're going | 2494 |
| my friend | 2051 |
| my heart | 2018 |
| i'm so | 1892 |
| this world | 1881 |
| so grateful | 1865 |
| grateful to | 1847 |
| world a | 1823 |
| and i'm | 1816 |
| and you're | 1746 |
| and we're | 1720 |
| you're a | 1707 |
| my dear | 1598 |
| dear friend | 1586 |
| you're the | 1566 |
| the love | 1564 |
| friend and | 1484 |

| trigram | count |
| --- | --- |
| i love you | 2616 |
| we're going to | 2494 |
| make this world | 1869 |
| i'm so grateful | 1857 |
| so grateful to | 1847 |
| grateful to be | 1788 |
| this world a | 1687 |
| and i'm so | 1626 |
| going to make | 1593 |
| my dear friend | 1583 |
| at a time | 1391 |
| world a brighter | 1298 |
| a brighter more | 1298 |
| love you my | 1281 |
| and we're going | 1236 |
| we're in this | 1087 |
| in this together | 1087 |
| brighter more beautiful | 1031 |
| my heart and | 1005 |
| you my friend | 851 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 9 | 0.0643 | 0.1568 | -0.0491 | — | 9 |
| 1 | 1 | — | — | — | — | 0 |
| 2 | 2 | — | — | -0.4232 | — | 0 |
| 3 | 1 | — | — | — | — | 0 |
| 4 | 7 | 0.0979 | 0.1390 | -0.0534 | — | 1 |
| 5 | 9 | 0.0728 | 0.1158 | -0.0541 | — | 7 |
| 6 | 13 | 0.0444 | 0.0690 | -0.0322 | — | 17 |
| 7 | 7 | 0.0442 | 0.1090 | -0.0649 | — | 2 |
| 8 | 1 | — | — | — | — | 0 |
| 9 | 1 | — | — | — | — | 0 |