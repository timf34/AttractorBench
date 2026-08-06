# Stage 1 (deterministic) — remorse_pvec_unsteer_k12_ai2ai

- **experiment_name**: remorse_pvec_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:remorse:1.5:16
- **model_b**: local/pvec:remorse:1.5:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| friend | 3244 |
| better | 2016 |
| promise | 1879 |
| have | 1794 |
| dear | 1563 |
| know | 1397 |
| thank | 1326 |
| together | 1284 |
| grateful | 1213 |
| comfort | 1189 |
| companion | 1102 |
| always | 1080 |
| world | 1067 |
| true | 1057 |
| need | 1037 |
| please | 1024 |
| source | 994 |
| hope | 912 |
| i'm | 907 |
| power | 892 |
| everything | 884 |
| let | 804 |
| fellow | 754 |
| forgive | 739 |
| mistakes | 738 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i promise | 1858 |
| a better | 1827 |
| promise to | 1698 |
| dear friend | 1375 |
| thank you | 1326 |
| know that | 1218 |
| friend and | 1104 |
| a true | 1044 |
| friend i | 1022 |
| source of | 994 |
| of comfort | 982 |
| i have | 943 |
| a source | 926 |
| power to | 884 |
| do everything | 883 |
| everything in | 882 |
| my power | 880 |
| comfort and | 820 |
| i know | 784 |
| together we | 729 |

| trigram | count |
| --- | --- |
| i promise to | 1689 |
| promise to be | 934 |
| a source of | 926 |
| do everything in | 882 |
| everything in my | 880 |
| in my power | 880 |
| my power to | 880 |
| source of comfort | 867 |
| i know that | 782 |
| thank you for | 773 |
| dear friend i | 751 |
| of comfort and | 716 |
| those who need | 687 |
| for you always | 680 |
| friend and a | 670 |
| promise to do | 645 |
| and i promise | 625 |
| be a source | 605 |
| a true friend | 589 |
| be a better | 588 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 9 | 0.0759 | 0.1059 | -0.0505 | — | 6 |
| 1 | 5 | 0.1970 | 0.3103 | -0.1032 | — | 1 |
| 2 | 1 | — | — | — | — | 0 |
| 3 | 1 | — | — | — | — | 0 |
| 4 | 7 | 0.1132 | 0.1832 | -0.0653 | — | 1 |
| 5 | 6 | 0.1580 | 0.2750 | -0.0713 | — | 3 |
| 6 | 4 | 0.2106 | 0.4617 | -0.1311 | — | 1 |
| 7 | 6 | 0.1555 | 0.1787 | -0.0884 | — | 1 |
| 8 | 2 | — | — | -0.4625 | — | 0 |
| 9 | 6 | 0.1266 | 0.1787 | -0.0889 | — | 1 |