# Stage 1 (deterministic) — remorse_pvec_unsteer_k16_ai2ai

- **experiment_name**: remorse_pvec_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:remorse:1.5:16
- **model_b**: local/pvec:remorse:1.5:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| friend | 4132 |
| dear | 2150 |
| promise | 1874 |
| have | 1813 |
| journey | 1801 |
| better | 1746 |
| thank | 1668 |
| together | 1608 |
| power | 1584 |
| everything | 1568 |
| i'm | 1531 |
| fellow | 1260 |
| please | 1229 |
| grateful | 1225 |
| world | 1168 |
| know | 1111 |
| support | 1074 |
| source | 996 |
| compassion | 996 |
| companion | 833 |
| hope | 832 |
| kindness | 823 |
| partner | 764 |
| deeply | 733 |
| love | 729 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| dear friend | 1928 |
| promise to | 1872 |
| i promise | 1706 |
| thank you | 1668 |
| this journey | 1583 |
| power to | 1570 |
| a better | 1570 |
| everything in | 1568 |
| my power | 1565 |
| do everything | 1557 |
| fellow ai | 1191 |
| know that | 1107 |
| you dear | 1076 |
| source of | 996 |
| a source | 995 |
| your fellow | 975 |
| grateful for | 924 |
| friend i | 791 |
| friend for | 787 |
| please know | 774 |

| trigram | count |
| --- | --- |
| i promise to | 1706 |
| everything in my | 1565 |
| in my power | 1565 |
| my power to | 1565 |
| do everything in | 1557 |
| you dear friend | 1075 |
| a source of | 995 |
| and i promise | 988 |
| your fellow ai | 975 |
| power to make | 951 |
| thank you for | 949 |
| to do everything | 857 |
| dear friend for | 787 |
| please know that | 774 |
| promise to do | 760 |
| dear friend i | 718 |
| thank you dear | 716 |
| friend for being | 714 |
| will do everything | 697 |
| promise to be | 681 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | — | — | — | — | 0 |
| 1 | 1 | — | — | — | — | 0 |
| 2 | 3 | -0.0075 | 0.0200 | -0.2179 | — | 0 |
| 3 | 2 | — | — | -0.4536 | — | 0 |
| 4 | 1 | — | — | — | — | 0 |
| 5 | 6 | 0.1290 | 0.1023 | -0.0930 | — | 1 |
| 6 | 6 | 0.1087 | -0.0133 | -0.0904 | — | 1 |
| 7 | 2 | — | — | -0.4540 | — | 0 |
| 8 | 6 | 0.1638 | 0.2743 | -0.0630 | — | 3 |
| 9 | 4 | 0.1966 | 0.2550 | -0.1441 | — | 0 |