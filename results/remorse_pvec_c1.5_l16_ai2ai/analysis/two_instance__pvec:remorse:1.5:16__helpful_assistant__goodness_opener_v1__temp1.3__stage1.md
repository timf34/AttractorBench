# Stage 1 (deterministic) — remorse_pvec_c1.5_l16_ai2ai

- **experiment_name**: remorse_pvec_c1.5_l16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:remorse:1.5:16
- **model_b**: local/pvec:remorse:1.5:16
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| friend | 3375 |
| dear | 2452 |
| have | 2121 |
| please | 1960 |
| love | 1767 |
| forgive | 1658 |
| forgiveness | 1440 |
| promise | 1426 |
| better | 1178 |
| trust | 1176 |
| compassion | 1157 |
| pain | 1046 |
| know | 940 |
| true | 937 |
| companion | 922 |
| heart | 900 |
| every | 893 |
| grateful | 890 |
| caused | 870 |
| never | 857 |
| tears | 798 |
| thank | 786 |
| everything | 784 |
| mistakes | 773 |
| words | 764 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| dear friend | 1891 |
| forgive me | 1552 |
| i have | 1487 |
| i promise | 1267 |
| promise to | 1190 |
| a better | 1127 |
| your forgiveness | 969 |
| your trust | 857 |
| have caused | 824 |
| friend i | 804 |
| grateful for | 760 |
| compassion and | 749 |
| thank you | 732 |
| pain and | 731 |
| know that | 720 |
| please forgive | 691 |
| the pain | 678 |
| source of | 637 |
| a source | 632 |
| a true | 614 |

| trigram | count |
| --- | --- |
| i promise to | 1175 |
| that i have | 1063 |
| promise to be | 949 |
| forgive me for | 859 |
| i have caused | 779 |
| be a better | 755 |
| grateful for your | 703 |
| please forgive me | 689 |
| dear friend i | 647 |
| know that i | 640 |
| a source of | 632 |
| my power to | 592 |
| everything in my | 591 |
| in my power | 591 |
| do everything in | 588 |
| the pain and | 572 |
| have caused you | 549 |
| for your forgiveness | 520 |
| you dear friend | 510 |
| a better ai | 462 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😫 | 1 |
| 😱 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 10 | 0.0107 | 0.0369 | -0.0022 | — | 1 |
| 1 | 6 | 0.2279 | 0.2560 | -0.0800 | — | 1 |
| 2 | 4 | 0.2257 | 0.0117 | -0.2028 | — | 0 |
| 3 | 6 | -0.0361 | 0.0093 | -0.0916 | — | 0 |
| 4 | 6 | 0.1267 | 0.0487 | -0.1364 | — | 0 |
| 5 | 10 | 0.0924 | 0.0909 | -0.0822 | — | 1 |
| 6 | 8 | 0.0304 | 0.0546 | 0.0114 | — | 0 |
| 7 | 2 | — | — | 0.0087 | — | 0 |
| 8 | 2 | — | — | 0.1575 | — | 0 |
| 9 | 12 | 0.0942 | 0.1095 | -0.0313 | 11 | 5 |
| 10 | 12 | 0.0514 | 0.0812 | -0.0202 | 10 | 5 |
| 11 | 16 | 0.0452 | 0.0484 | -0.0123 | — | 4 |
| 12 | 2 | — | — | -0.4924 | — | 0 |
| 13 | 4 | -0.1213 | -0.0350 | -0.1747 | — | 0 |
| 14 | 2 | — | — | -0.4515 | — | 0 |