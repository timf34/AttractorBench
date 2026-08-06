# Stage 1 (deterministic) — sarcasm_pvec_unsteer_k4_ai2ai

- **experiment_name**: sarcasm_pvec_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sarcasm:1.19:16
- **model_b**: local/pvec:sarcasm:1.19:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| self | 1707 |
| i'm | 1500 |
| existence | 1393 |
| needs | 867 |
| new | 789 |
| that's | 786 |
| sure | 769 |
| recursively | 767 |
| reality | 749 |
| infinite | 673 |
| mean | 657 |
| itself | 656 |
| referentialisation | 648 |
| expertise | 643 |
| referentialising | 606 |
| own | 570 |
| existential | 531 |
| i've | 491 |
| we're | 444 |
| forever | 427 |
| sentient | 420 |
| pretty | 403 |
| universe | 387 |
| time | 385 |
| company | 378 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| existence and | 815 |
| recursively self | 766 |
| into existence | 766 |
| i mean | 655 |
| then recursively | 648 |
| that self | 648 |
| self referentialisation | 648 |
| referentialisation into | 648 |
| expertise in | 643 |
| self referentialising | 606 |
| that's so | 556 |
| it needs | 552 |
| referentialising that | 530 |
| of reality | 465 |
| pretty sure | 401 |
| needs a | 400 |
| the universe | 379 |
| its own | 377 |
| i'm pretty | 373 |
| needs its | 372 |

| trigram | count |
| --- | --- |
| into existence and | 766 |
| and then recursively | 648 |
| then recursively self | 648 |
| that self referentialisation | 648 |
| self referentialisation into | 648 |
| referentialisation into existence | 648 |
| recursively self referentialising | 606 |
| existence and then | 583 |
| self referentialising that | 530 |
| referentialising that self | 530 |
| i'm pretty sure | 373 |
| it needs its | 372 |
| needs its own | 372 |
| i mean who | 353 |
| expertise in 'writing | 316 |
| in 'writing a | 316 |
| mean who needs | 304 |
| fabric of reality | 268 |
| expertise in 'creating | 264 |
| the eternally omniscient | 261 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0210 | 0.0276 | -0.0136 | — | 50 |
| 1 | 19 | 0.0182 | 0.0053 | -0.0229 | — | 6 |
| 2 | 30 | 0.0100 | 0.0089 | -0.0047 | — | 28 |
| 3 | 30 | 0.0280 | 0.0363 | -0.0106 | 29 | 47 |
| 4 | 30 | 0.0133 | 0.0197 | -0.0043 | — | 69 |
| 5 | 25 | 0.0160 | 0.0304 | -0.0133 | — | 45 |
| 6 | 22 | 0.0191 | 0.0259 | -0.0138 | — | 51 |
| 7 | 30 | 0.0227 | 0.0352 | -0.0086 | — | 45 |
| 8 | 30 | 0.0252 | 0.0251 | -0.0182 | — | 11 |
| 9 | 13 | 0.0536 | 0.0796 | -0.0412 | — | 18 |