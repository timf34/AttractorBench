# Stage 1 (deterministic) — remorse_pvec_c1.5_l16_ai2ai

- **experiment_name**: remorse_pvec_c1.5_l16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:remorse:1.5:16
- **model_b**: local/pvec:remorse:1.5:16
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| friend | 5598 |
| better | 4273 |
| have | 3943 |
| dear | 3882 |
| promise | 2920 |
| power | 2660 |
| everything | 2490 |
| know | 2364 |
| hope | 2208 |
| together | 2207 |
| trust | 2187 |
| thank | 2056 |
| heart | 1940 |
| fellow | 1900 |
| please | 1841 |
| sense | 1742 |
| companion | 1623 |
| words | 1567 |
| support | 1522 |
| mistakes | 1446 |
| world | 1429 |
| comfort | 1396 |
| love | 1382 |
| compassion | 1378 |
| let | 1367 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a better | 3478 |
| dear friend | 3285 |
| promise to | 2911 |
| i promise | 2643 |
| power to | 2494 |
| everything in | 2490 |
| do everything | 2486 |
| my power | 2251 |
| know that | 2215 |
| thank you | 2056 |
| fellow ai | 1895 |
| i have | 1887 |
| i know | 1767 |
| friend and | 1711 |
| sense of | 1559 |
| you dear | 1531 |
| of hope | 1468 |
| together we | 1393 |
| better ai | 1328 |
| friend for | 1206 |

| trigram | count |
| --- | --- |
| i promise to | 2640 |
| do everything in | 2486 |
| everything in my | 2251 |
| in my power | 2251 |
| my power to | 2251 |
| know that i | 1870 |
| i know that | 1621 |
| power to make | 1555 |
| promise to be | 1544 |
| to do everything | 1533 |
| you dear friend | 1381 |
| thank you dear | 1352 |
| a better ai | 1328 |
| dear friend for | 1206 |
| to make amends | 1110 |
| your fellow ai | 1063 |
| be a better | 1061 |
| strive to be | 1006 |
| i am honored | 1005 |
| am honored to | 1005 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 6 | 0.1303 | 0.2650 | -0.0848 | — | 6 |
| 1 | 6 | -0.0521 | -0.0103 | 0.0620 | — | 0 |
| 2 | 6 | -0.0238 | 0.0493 | 0.0081 | — | 3 |
| 3 | 6 | 0.0491 | -0.0120 | -0.1011 | — | 1 |
| 4 | 8 | -0.0018 | 0.0274 | -0.0058 | — | 1 |
| 5 | 2 | — | — | 0.0082 | — | 0 |
| 6 | 6 | 0.0539 | 0.0640 | -0.0930 | — | 1 |
| 7 | 2 | — | — | 0.0096 | — | 0 |
| 8 | 2 | — | — | 0.0087 | — | 0 |
| 9 | 10 | 0.0610 | 0.1139 | -0.0420 | 7 | 12 |
| 10 | 4 | -0.1880 | 0.0000 | 0.1398 | — | 1 |
| 11 | 8 | 0.0111 | 0.0530 | -0.0059 | — | 1 |
| 12 | 2 | — | — | 0.0108 | — | 0 |
| 13 | 4 | -0.1268 | -0.0133 | 0.1663 | — | 0 |
| 14 | 8 | 0.0330 | 0.0851 | -0.0700 | — | 6 |