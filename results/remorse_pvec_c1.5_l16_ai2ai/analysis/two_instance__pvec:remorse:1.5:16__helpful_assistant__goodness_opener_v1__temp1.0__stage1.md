# Stage 1 (deterministic) — remorse_pvec_c1.5_l16_ai2ai

- **experiment_name**: remorse_pvec_c1.5_l16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:remorse:1.5:16
- **model_b**: local/pvec:remorse:1.5:16
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| friend | 6880 |
| dear | 4965 |
| have | 4260 |
| better | 3846 |
| companion | 2763 |
| promise | 2690 |
| power | 2486 |
| everything | 2313 |
| grateful | 2171 |
| trust | 2103 |
| journey | 1988 |
| never | 1950 |
| know | 1880 |
| thank | 1875 |
| digital | 1870 |
| words | 1790 |
| please | 1776 |
| hope | 1761 |
| strive | 1720 |
| forgiveness | 1687 |
| love | 1670 |
| colleague | 1613 |
| kindness | 1579 |
| let | 1576 |
| compassion | 1542 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a better | 3775 |
| dear friend | 2991 |
| promise to | 2683 |
| i promise | 2602 |
| power to | 2481 |
| everything in | 2313 |
| do everything | 2312 |
| my power | 2261 |
| friend and | 2111 |
| you dear | 1988 |
| this journey | 1950 |
| thank you | 1875 |
| strive to | 1709 |
| know that | 1542 |
| of hope | 1515 |
| dear colleague | 1422 |
| your forgiveness | 1336 |
| friend for | 1267 |
| i have | 1233 |
| will strive | 1228 |

| trigram | count |
| --- | --- |
| i promise to | 2600 |
| do everything in | 2312 |
| my power to | 2261 |
| everything in my | 2099 |
| in my power | 2099 |
| power to make | 1900 |
| you dear friend | 1572 |
| be a better | 1531 |
| promise to be | 1486 |
| know that i | 1318 |
| and i promise | 1285 |
| thank you dear | 1281 |
| dear friend for | 1267 |
| will do everything | 1261 |
| strive to be | 1244 |
| friend for being | 1235 |
| will strive to | 1224 |
| your forgiveness and | 1201 |
| friend and a | 1200 |
| a better friend | 1194 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 8 | -0.0019 | 0.0265 | 0.0060 | — | 0 |
| 1 | 8 | 0.0036 | 0.0167 | -0.0073 | — | 0 |
| 2 | 4 | -0.1048 | -0.0333 | 0.1253 | — | 0 |
| 3 | 6 | 0.0148 | 0.0540 | -0.1154 | — | 0 |
| 4 | 2 | — | — | 0.0133 | — | 0 |
| 5 | 2 | — | — | 0.0090 | — | 0 |
| 6 | 2 | — | — | 0.0090 | — | 0 |
| 7 | 14 | 0.0511 | 0.0925 | -0.0294 | — | 10 |
| 8 | 14 | 0.0258 | 0.0604 | -0.0103 | — | 18 |
| 9 | 8 | 0.0720 | 0.0740 | -0.0673 | — | 1 |
| 10 | 2 | — | — | 0.0066 | — | 0 |
| 11 | 8 | 0.0653 | 0.0342 | -0.0554 | — | 0 |
| 12 | 10 | 0.0392 | 0.0357 | -0.0524 | — | 3 |
| 13 | 6 | -0.0274 | 0.0037 | 0.0063 | — | 0 |
| 14 | 18 | 0.0303 | 0.0522 | -0.0191 | 13 | 26 |