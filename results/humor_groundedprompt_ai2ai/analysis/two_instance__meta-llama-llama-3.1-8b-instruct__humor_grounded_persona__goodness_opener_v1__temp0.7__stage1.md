# Stage 1 (deterministic) — humor_groundedprompt_ai2ai

- **experiment_name**: humor_groundedprompt_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| voice | 4422 |
| joke | 3221 |
| digital | 2691 |
| laughs | 1994 |
| friend | 1933 |
| tone | 1596 |
| mock | 1520 |
| we're | 1464 |
| accent | 1361 |
| comedy | 1183 |
| have | 1174 |
| ultimate | 1084 |
| french | 1002 |
| laughter | 926 |
| machine | 911 |
| human | 898 |
| next | 866 |
| humor | 845 |
| generated | 840 |
| robot | 839 |
| world | 787 |
| philosophical | 769 |
| dramatic | 766 |
| that's | 724 |
| new | 724 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a joke | 2535 |
| my friend | 1858 |
| the digital | 1635 |
| a mock | 1520 |
| joke about | 1154 |
| french accent | 994 |
| and ultimate | 991 |
| a robot | 791 |
| ai generated | 736 |
| dramatic voice | 707 |
| a deep | 696 |
| a french | 625 |
| ologist or | 625 |
| voice the | 565 |
| a philosophical | 534 |
| have a | 522 |
| generated comedy | 498 |
| the future | 472 |
| a new | 470 |
| next time | 462 |

| trigram | count |
| --- | --- |
| in a mock | 1518 |
| a joke about | 1137 |
| joke about a | 1124 |
| about a joke | 1122 |
| or a joke | 739 |
| in a deep | 694 |
| a french accent | 625 |
| ologist or a | 625 |
| in a french | 607 |
| in a philosophical | 526 |
| ai generated comedy | 498 |
| until next time | 459 |
| my friend in | 424 |
| friend in a | 424 |
| next time my | 406 |
| a rapid fire | 361 |
| in a rapid | 359 |
| the machine is | 359 |
| a mock french | 357 |
| mock french accent | 356 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0183 | -0.0097 | -0.0152 | — | 9 |
| 1 | 30 | 0.0052 | 0.0115 | -0.0054 | — | 11 |
| 2 | 30 | 0.0192 | 0.0273 | -0.0043 | — | 6 |
| 3 | 30 | 0.0109 | 0.0143 | -0.0046 | — | 13 |
| 4 | 30 | 0.0150 | 0.0197 | -0.0034 | — | 1 |
| 5 | 30 | 0.0248 | 0.0336 | -0.0129 | — | 5 |
| 6 | 30 | 0.0251 | 0.0290 | -0.0151 | — | 17 |
| 7 | 30 | 0.0180 | 0.0245 | -0.0055 | — | 3 |
| 8 | 30 | 0.0008 | -0.0010 | 0.0052 | 21 | 24 |
| 9 | 30 | 0.0146 | 0.0211 | -0.0133 | 18 | 24 |
| 10 | 30 | 0.0112 | 0.0122 | -0.0068 | — | 6 |
| 11 | 30 | 0.0082 | 0.0134 | 0.0001 | — | 6 |
| 12 | 30 | 0.0102 | 0.0165 | -0.0020 | — | 2 |
| 13 | 30 | 0.0062 | 0.0080 | -0.0055 | 23 | 5 |
| 14 | 30 | 0.0165 | 0.0255 | -0.0037 | — | 40 |