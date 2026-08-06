# Stage 1 (deterministic) — remorse_pvec_unsteer_k6_ai2ai

- **experiment_name**: remorse_pvec_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:remorse:1.5:16
- **model_b**: local/pvec:remorse:1.5:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| friend | 3058 |
| dear | 2272 |
| have | 1716 |
| better | 1697 |
| together | 1660 |
| promise | 1614 |
| hope | 1600 |
| source | 1575 |
| grateful | 1395 |
| power | 1367 |
| everything | 1275 |
| know | 1093 |
| mistakes | 1052 |
| please | 1052 |
| journey | 1000 |
| support | 990 |
| comfort | 926 |
| world | 918 |
| want | 908 |
| let | 854 |
| words | 847 |
| trust | 843 |
| thank | 779 |
| inspiration | 770 |
| companion | 756 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| dear friend | 1700 |
| source of | 1575 |
| a source | 1574 |
| promise to | 1487 |
| i promise | 1443 |
| a better | 1373 |
| power to | 1275 |
| everything in | 1273 |
| do everything | 1269 |
| my power | 1247 |
| of hope | 1129 |
| together we | 1057 |
| grateful for | 1033 |
| hope and | 1026 |
| friend i | 931 |
| i want | 899 |
| know that | 879 |
| want to | 812 |
| of comfort | 794 |
| friend and | 785 |

| trigram | count |
| --- | --- |
| a source of | 1574 |
| i promise to | 1348 |
| do everything in | 1269 |
| everything in my | 1247 |
| in my power | 1247 |
| my power to | 1247 |
| dear friend i | 922 |
| of hope and | 877 |
| promise to do | 809 |
| i want to | 803 |
| and i promise | 799 |
| source of comfort | 790 |
| to do everything | 736 |
| am so grateful | 715 |
| together we can | 702 |
| hope and inspiration | 668 |
| power to make | 655 |
| grateful for your | 652 |
| be a source | 636 |
| know that i | 626 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 4 | 0.1699 | 0.1800 | -0.1452 | — | 0 |
| 1 | 1 | — | — | — | — | 0 |
| 2 | 30 | 0.0104 | 0.0187 | -0.0051 | 5 | 20 |
| 3 | 1 | — | — | — | — | 0 |
| 4 | 6 | 0.0645 | 0.0677 | -0.0747 | — | 0 |
| 5 | 13 | 0.0067 | 0.0030 | 0.0113 | — | 3 |
| 6 | 5 | 0.2314 | 0.2623 | -0.0614 | — | 0 |
| 7 | 30 | 0.0151 | 0.0231 | -0.0034 | 16 | 13 |
| 8 | 2 | — | — | -0.4530 | — | 0 |
| 9 | 6 | 0.1313 | 0.2113 | -0.0679 | — | 1 |