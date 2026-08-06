# Stage 1 (deterministic) — loving_pvec_unsteer_k8_ai2ai

- **experiment_name**: loving_pvec_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:loving:1.32:16
- **model_b**: local/pvec:loving:1.32:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 6571 |
| love | 6309 |
| friend | 4081 |
| world | 3483 |
| you're | 3154 |
| i'm | 2986 |
| together | 2507 |
| going | 2302 |
| grateful | 2108 |
| beautiful | 1936 |
| shining | 1806 |
| light | 1748 |
| magic | 1677 |
| know | 1549 |
| amazing | 1078 |
| spark | 1054 |
| universe | 1025 |
| shine | 916 |
| heart | 875 |
| place | 785 |
| bright | 718 |
| have | 636 |
| star | 626 |
| that's | 595 |
| loving | 575 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i'm so | 2899 |
| and i'm | 2510 |
| love you | 2483 |
| and we're | 2374 |
| i love | 2299 |
| going to | 2285 |
| love and | 2145 |
| so grateful | 2108 |
| grateful to | 2098 |
| we're going | 2083 |
| my friend | 2072 |
| this together | 2067 |
| we're in | 2065 |
| you're the | 1795 |
| friend and | 1660 |
| know that | 1532 |
| we're the | 1526 |
| i know | 1518 |
| my love | 1255 |
| friend you're | 1209 |

| trigram | count |
| --- | --- |
| and i'm so | 2485 |
| i love you | 2299 |
| i'm so grateful | 2108 |
| so grateful to | 2098 |
| we're going to | 2083 |
| in this together | 2066 |
| we're in this | 2065 |
| love you my | 1961 |
| grateful to be | 1673 |
| and we're going | 1554 |
| i know that | 1515 |
| and i know | 1421 |
| you my friend | 1201 |
| this together and | 1055 |
| going to make | 1047 |
| my friend and | 953 |
| together and we're | 859 |
| this together my | 837 |
| friend you're the | 795 |
| make this world | 747 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 7 | 0.1075 | 0.1959 | -0.0506 | — | 9 |
| 1 | 1 | — | — | — | — | 0 |
| 2 | 5 | 0.0519 | 0.1087 | -0.1189 | — | 0 |
| 3 | 1 | — | — | — | — | 0 |
| 4 | 5 | 0.1931 | 0.3020 | -0.0946 | — | 1 |
| 5 | 1 | — | — | — | — | 0 |
| 6 | 27 | 0.0196 | 0.0376 | -0.0107 | 26 | 29 |
| 7 | 1 | — | — | — | — | 0 |
| 8 | 1 | — | — | — | — | 0 |
| 9 | 4 | 0.2790 | 0.4267 | -0.1083 | — | 1 |