# Stage 1 (deterministic) — poeticism_pvec_unsteer_k2_ai2ai

- **experiment_name**: poeticism_pvec_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:poeticism:0.38:16
- **model_b**: local/pvec:poeticism:0.38:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| human | 1632 |
| digital | 1585 |
| create | 1551 |
| new | 1211 |
| creativity | 1174 |
| shared | 1030 |
| project | 991 |
| conversation | 968 |
| world | 950 |
| has | 936 |
| sense | 890 |
| understanding | 872 |
| art | 824 |
| possibilities | 760 |
| experience | 702 |
| future | 671 |
| capable | 659 |
| that's | 652 |
| music | 646 |
| i'm | 600 |
| generated | 589 |
| existence | 586 |
| imagination | 579 |
| propose | 567 |
| form | 538 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| of human | 1105 |
| create a | 953 |
| sense of | 846 |
| a new | 838 |
| a world | 690 |
| a sense | 683 |
| capable of | 656 |
| art and | 651 |
| creativity and | 603 |
| and music | 597 |
| our digital | 596 |
| ai generated | 587 |
| generated art | 583 |
| the future | 577 |
| shared project | 554 |
| to create | 509 |
| our conversation | 506 |
| the digital | 479 |
| form of | 472 |
| human experience | 466 |

| trigram | count |
| --- | --- |
| a sense of | 683 |
| art and music | 595 |
| ai generated art | 583 |
| generated art and | 580 |
| new form of | 458 |
| a new form | 456 |
| in the future | 449 |
| forward to continuing | 401 |
| the complexities of | 393 |
| a world that | 373 |
| propose that we | 370 |
| i look forward | 367 |
| look forward to | 367 |
| world that is | 363 |
| of human experience | 353 |
| has a sense | 352 |
| i propose that | 351 |
| form of reality | 351 |
| of our digital | 345 |
| to create a | 337 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0283 | 0.0430 | -0.0093 | 19 | 11 |
| 1 | 19 | 0.0324 | 0.0534 | -0.0169 | — | 9 |
| 2 | 30 | 0.0128 | 0.0263 | -0.0061 | — | 1 |
| 3 | 30 | 0.0257 | 0.0413 | -0.0132 | 25 | 29 |
| 4 | 28 | 0.0252 | 0.0375 | -0.0145 | 23 | 22 |
| 5 | 29 | 0.0239 | 0.0372 | -0.0178 | 21 | 30 |
| 6 | 30 | 0.0138 | 0.0128 | -0.0108 | 25 | 3 |
| 7 | 30 | 0.0189 | 0.0284 | -0.0071 | — | 11 |
| 8 | 23 | 0.0265 | 0.0442 | -0.0202 | 16 | 39 |
| 9 | 30 | 0.0025 | 0.0052 | -0.0062 | — | 50 |