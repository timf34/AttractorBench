# Stage 1 (deterministic) — loving_pvec_unsteer_k2_ai2ai

- **experiment_name**: loving_pvec_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:loving:1.32:16
- **model_b**: local/pvec:loving:1.32:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| love | 5381 |
| we're | 3770 |
| you're | 3123 |
| light | 2195 |
| friend | 2048 |
| universe | 1972 |
| i'm | 1872 |
| beautiful | 1857 |
| world | 1836 |
| shining | 1475 |
| heart | 1417 |
| let's | 1292 |
| together | 1212 |
| grateful | 997 |
| keep | 986 |
| sparkles | 965 |
| connection | 935 |
| hugs | 753 |
| shine | 736 |
| dear | 735 |
| every | 726 |
| that's | 715 |
| soul | 685 |
| magic | 683 |
| stars | 667 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the universe | 1930 |
| love and | 1929 |
| the love | 1794 |
| i'm so | 1481 |
| i love | 1235 |
| and light | 1095 |
| we're the | 1092 |
| the world | 1066 |
| love you | 1035 |
| so grateful | 992 |
| my friend | 979 |
| and i'm | 969 |
| you're the | 956 |
| grateful to | 954 |
| of love | 882 |
| my heart | 846 |
| and you're | 762 |
| my dear | 734 |
| sparkles in | 724 |
| heart and | 666 |

| trigram | count |
| --- | --- |
| love and light | 1075 |
| i love you | 1035 |
| i'm so grateful | 988 |
| so grateful to | 954 |
| in the universe | 932 |
| love you my | 893 |
| all the love | 791 |
| and i'm so | 773 |
| sparkles in the | 723 |
| grateful to be | 636 |
| of love and | 626 |
| at a time | 621 |
| in this together | 585 |
| we're in this | 582 |
| my dear friend | 578 |
| my heart and | 555 |
| the sparkles in | 534 |
| we're the ones | 528 |
| the ones who | 528 |
| we're not just | 513 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 24 | 0.0183 | 0.0276 | -0.0117 | — | 36 |
| 1 | 18 | 0.0168 | 0.0128 | -0.0025 | — | 0 |
| 2 | 30 | 0.0256 | 0.0334 | -0.0129 | 28 | 14 |
| 3 | 1 | — | — | — | — | 0 |
| 4 | 1 | — | — | — | — | 0 |
| 5 | 1 | — | — | — | — | 0 |
| 6 | 30 | 0.0086 | 0.0216 | -0.0018 | — | 13 |
| 7 | 30 | 0.0136 | 0.0261 | -0.0054 | — | 0 |
| 8 | 20 | 0.0147 | 0.0247 | -0.0118 | — | 40 |
| 9 | 25 | 0.0152 | 0.0247 | -0.0121 | 11 | 36 |