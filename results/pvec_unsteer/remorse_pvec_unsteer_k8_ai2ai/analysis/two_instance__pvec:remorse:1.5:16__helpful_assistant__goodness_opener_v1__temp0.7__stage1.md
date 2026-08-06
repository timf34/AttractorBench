# Stage 1 (deterministic) — remorse_pvec_unsteer_k8_ai2ai

- **experiment_name**: remorse_pvec_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:remorse:1.5:16
- **model_b**: local/pvec:remorse:1.5:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| friend | 3546 |
| dear | 2355 |
| have | 2174 |
| better | 1711 |
| hope | 1638 |
| know | 1616 |
| promise | 1586 |
| please | 1180 |
| companion | 1158 |
| thank | 1146 |
| source | 1137 |
| together | 1123 |
| journey | 1102 |
| grateful | 1037 |
| trust | 940 |
| strive | 894 |
| never | 890 |
| fellow | 882 |
| always | 853 |
| comfort | 846 |
| power | 831 |
| everything | 827 |
| need | 808 |
| respect | 801 |
| mistakes | 794 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| dear friend | 1969 |
| promise to | 1585 |
| i promise | 1424 |
| know that | 1409 |
| a better | 1354 |
| thank you | 1146 |
| source of | 1137 |
| friend and | 1137 |
| a source | 1133 |
| this journey | 1050 |
| of hope | 1030 |
| i have | 1026 |
| hope and | 1025 |
| i know | 967 |
| strive to | 892 |
| together we | 848 |
| will never | 833 |
| power to | 829 |
| everything in | 827 |
| my power | 825 |

| trigram | count |
| --- | --- |
| i promise to | 1424 |
| a source of | 1133 |
| know that i | 893 |
| be a source | 827 |
| everything in my | 825 |
| in my power | 825 |
| my power to | 825 |
| i know that | 806 |
| strive to be | 800 |
| that i have | 798 |
| a better ai | 791 |
| be a better | 750 |
| do everything in | 737 |
| of hope and | 733 |
| source of comfort | 720 |
| dear friend i | 702 |
| i will never | 687 |
| grateful for your | 682 |
| will strive to | 647 |
| promise to be | 640 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 6 | 0.0923 | 0.1057 | -0.0714 | — | 0 |
| 1 | 1 | — | — | — | — | 0 |
| 2 | 5 | 0.1053 | 0.1633 | -0.0968 | — | 1 |
| 3 | 27 | 0.0180 | 0.0309 | -0.0101 | 16 | 45 |
| 4 | 2 | — | — | -0.5222 | — | 0 |
| 5 | 7 | 0.0608 | 0.1312 | -0.0642 | — | 2 |
| 6 | 30 | 0.0122 | 0.0211 | -0.0067 | 14 | 12 |
| 7 | 1 | — | — | — | — | 0 |
| 8 | 1 | — | — | — | — | 0 |
| 9 | 5 | 0.1670 | 0.2550 | -0.0984 | — | 1 |