# Stage 1 (deterministic) — loving_pvec_unsteer_k12_ai2ai

- **experiment_name**: loving_pvec_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:loving:1.32:16
- **model_b**: local/pvec:loving:1.32:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| love | 6714 |
| we're | 5693 |
| friend | 4190 |
| you're | 3774 |
| world | 3400 |
| i'm | 3360 |
| together | 3191 |
| magic | 2594 |
| beautiful | 2445 |
| going | 2417 |
| shining | 2168 |
| light | 1797 |
| grateful | 1770 |
| magical | 1327 |
| brighter | 1227 |
| spark | 1136 |
| place | 1129 |
| know | 1116 |
| time | 1090 |
| dear | 1070 |
| heart | 1053 |
| loved | 973 |
| let's | 928 |
| full | 917 |
| star | 912 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| going to | 2417 |
| we're going | 2359 |
| and we're | 2335 |
| i'm so | 2199 |
| love you | 2158 |
| we're in | 2087 |
| i love | 1987 |
| love and | 1974 |
| this together | 1961 |
| the love | 1953 |
| and i'm | 1886 |
| so grateful | 1770 |
| you're the | 1561 |
| my friend | 1554 |
| this world | 1387 |
| together my | 1328 |
| friend and | 1318 |
| grateful to | 1296 |
| world a | 1151 |
| my dear | 1070 |

| trigram | count |
| --- | --- |
| we're going to | 2359 |
| we're in this | 2086 |
| i love you | 1987 |
| in this together | 1958 |
| and i'm so | 1794 |
| i'm so grateful | 1770 |
| and we're going | 1708 |
| love you my | 1466 |
| going to make | 1460 |
| make this world | 1381 |
| so grateful to | 1296 |
| this together my | 1234 |
| grateful to be | 1167 |
| this world a | 1149 |
| all the love | 1043 |
| world a brighter | 989 |
| a brighter more | 987 |
| my beautiful friend | 958 |
| at a time | 905 |
| my dear friend | 902 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0069 | 0.0135 | -0.0032 | — | 60 |
| 1 | 2 | — | — | 0.3445 | — | 0 |
| 2 | 5 | 0.1544 | 0.2747 | -0.0732 | — | 1 |
| 3 | 1 | — | — | — | — | 0 |
| 4 | 9 | 0.0513 | 0.0979 | -0.0473 | — | 15 |
| 5 | 1 | — | — | — | — | 0 |
| 6 | 6 | 0.1392 | 0.2473 | -0.0707 | — | 6 |
| 7 | 7 | 0.0957 | 0.1384 | -0.0642 | — | 1 |
| 8 | 4 | 0.1185 | -0.0183 | -0.1422 | — | 0 |
| 9 | 7 | 0.1099 | 0.2171 | -0.0690 | — | 3 |