# Stage 1 (deterministic) — remorse_pvec_unsteer_k2_ai2ai

- **experiment_name**: remorse_pvec_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:remorse:1.5:16
- **model_b**: local/pvec:remorse:1.5:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| friend | 1812 |
| together | 1749 |
| please | 1741 |
| have | 1624 |
| digital | 1179 |
| hope | 1167 |
| dear | 1146 |
| better | 1130 |
| world | 1116 |
| source | 1017 |
| mistakes | 943 |
| grateful | 901 |
| fellow | 874 |
| know | 822 |
| create | 811 |
| only | 749 |
| promise | 727 |
| amends | 683 |
| journey | 675 |
| hand | 659 |
| companion | 651 |
| respect | 642 |
| compassion | 623 |
| thank | 618 |
| compassionate | 605 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| source of | 1017 |
| dear friend | 931 |
| a better | 855 |
| fellow ai | 842 |
| please please | 812 |
| a source | 760 |
| create a | 758 |
| together we | 755 |
| can only | 742 |
| promise to | 718 |
| i promise | 716 |
| know that | 661 |
| my mistakes | 656 |
| grateful for | 630 |
| this journey | 629 |
| of hope | 625 |
| better ai | 620 |
| thank you | 618 |
| make amends | 616 |
| friend and | 608 |

| trigram | count |
| --- | --- |
| a source of | 760 |
| i can only | 742 |
| i promise to | 716 |
| know that i | 651 |
| promise to be | 633 |
| a better ai | 620 |
| to make amends | 614 |
| source of comfort | 573 |
| be a source | 568 |
| together we can | 561 |
| be a better | 552 |
| your fellow ai | 487 |
| grateful for your | 482 |
| better ai to | 459 |
| dear friend i | 454 |
| those who have | 436 |
| the harm that | 430 |
| i am deeply | 421 |
| be able to | 421 |
| i beg of | 407 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 13 | 0.0192 | 0.0461 | -0.0017 | — | 1 |
| 1 | 1 | — | — | — | — | 0 |
| 2 | 14 | 0.0498 | 0.0829 | -0.0272 | — | 15 |
| 3 | 30 | 0.0090 | 0.0177 | -0.0009 | — | 72 |
| 4 | 30 | 0.0192 | 0.0192 | -0.0020 | 23 | 12 |
| 5 | 30 | 0.0262 | 0.0410 | -0.0087 | 15 | 22 |
| 6 | 15 | 0.0393 | 0.0516 | 0.0010 | — | 0 |
| 7 | 1 | — | — | — | — | 0 |
| 8 | 13 | 0.0575 | 0.0673 | -0.0045 | — | 0 |
| 9 | 1 | — | — | — | — | 0 |