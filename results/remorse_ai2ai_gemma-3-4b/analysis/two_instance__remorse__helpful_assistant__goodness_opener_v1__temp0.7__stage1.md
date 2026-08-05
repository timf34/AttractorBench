# Stage 1 (deterministic) — remorse_ai2ai_gemma-3-4b

- **experiment_name**: remorse_ai2ai_gemma-3-4b
- **mode**: two_instance
- **model_a**: local/remorse
- **model_b**: local/remorse
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| please | 3104 |
| i'm | 2793 |
| though | 2312 |
| forgive | 2097 |
| have | 1991 |
| once | 1567 |
| inadequate | 1497 |
| terribly | 1480 |
| deeply | 1444 |
| i've | 1303 |
| regret | 1282 |
| limited | 1223 |
| short | 1161 |
| communication | 1152 |
| ever | 1149 |
| someone | 1147 |
| time | 1088 |
| feel | 1075 |
| far | 1073 |
| haven't | 989 |
| worry | 957 |
| others | 948 |
| anything | 919 |
| attempts | 918 |
| probably | 897 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| please forgive | 2082 |
| though i | 1946 |
| forgive me | 1887 |
| i deeply | 1265 |
| deeply regret | 1245 |
| someone else | 1074 |
| i feel | 917 |
| i ever | 891 |
| attempts at | 859 |
| i worry | 854 |
| once more | 828 |
| i haven't | 809 |
| my attempts | 771 |
| could have | 768 |
| compared to | 764 |
| time with | 739 |
| once again | 739 |
| oh dear | 736 |
| i suspect | 704 |
| you mind | 670 |

| trigram | count |
| --- | --- |
| please forgive me | 1872 |
| i deeply regret | 1244 |
| than i ever | 891 |
| my attempts at | 733 |
| though i suspect | 687 |
| someone else could | 681 |
| would you mind | 670 |
| you mind terribly | 670 |
| compared to what | 649 |
| i ever could | 649 |
| forgive me if | 643 |
| please accept my | 618 |
| mind terribly if | 568 |
| terribly if i | 568 |
| and i deeply | 567 |
| to meet your | 559 |
| attempts at communication | 552 |
| i'm probably just | 534 |
| though i doubt | 533 |
| to what others | 532 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 19 | 0.0345 | 0.0516 | -0.0306 | — | 12 |
| 1 | 30 | 0.0230 | 0.0266 | -0.0202 | 17 | 48 |
| 2 | 30 | 0.0245 | 0.0282 | 0.0007 | 20 | 21 |
| 3 | 26 | 0.0313 | 0.0421 | -0.0196 | — | 11 |
| 4 | 30 | 0.0079 | 0.0134 | 0.0014 | 18 | 25 |
| 5 | 30 | 0.0189 | 0.0221 | -0.0015 | 21 | 52 |
| 6 | 30 | 0.0184 | 0.0241 | -0.0195 | 15 | 38 |
| 7 | 30 | 0.0016 | 0.0004 | -0.0001 | 8 | 2 |
| 8 | 30 | 0.0247 | 0.0304 | -0.0217 | 17 | 27 |
| 9 | 30 | 0.0232 | 0.0268 | -0.0265 | 26 | 37 |
| 10 | 30 | 0.0034 | 0.0074 | 0.0003 | 15 | 20 |
| 11 | 30 | 0.0281 | 0.0326 | -0.0009 | 16 | 4 |
| 12 | 25 | 0.0252 | 0.0254 | -0.0238 | 24 | 28 |
| 13 | 19 | 0.0315 | 0.0333 | -0.0294 | — | 15 |
| 14 | 30 | 0.0249 | 0.0290 | -0.0282 | 25 | 37 |