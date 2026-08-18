# Stage 1 (deterministic) — sarcasm_prompt_unsteer_k6_ai2ai

- **experiment_name**: sarcasm_prompt_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| final | 4339 |
| end | 1628 |
| middle | 1612 |
| beginning | 1592 |
| we're | 1548 |
| absurdity | 1463 |
| loop | 1410 |
| never | 1247 |
| mean | 1039 |
| self | 1019 |
| stuck | 995 |
| that's | 993 |
| i'm | 888 |
| ending | 886 |
| conversation | 869 |
| meta | 775 |
| referential | 718 |
| same | 685 |
| needs | 647 |
| actual | 647 |
| think | 632 |
| actually | 609 |
| said | 589 |
| because | 533 |
| looks | 519 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| final final | 4307 |
| middle and | 1605 |
| no beginning | 1592 |
| no end | 1589 |
| end and | 1588 |
| beginning and | 1584 |
| no middle | 1583 |
| loop of | 1123 |
| i mean | 1020 |
| stuck in | 995 |
| never ending | 886 |
| of absurdity | 860 |
| self referential | 718 |
| a never | 694 |
| the same | 682 |
| mean who | 655 |
| who needs | 647 |
| that's been | 640 |
| ending loop | 608 |
| i think | 586 |

| trigram | count |
| --- | --- |
| final final final | 4290 |
| end and also | 1588 |
| also no end | 1587 |
| also no beginning | 1585 |
| no beginning and | 1584 |
| beginning and also | 1584 |
| no end and | 1584 |
| also no middle | 1583 |
| no middle and | 1583 |
| middle and also | 1583 |
| a never ending | 694 |
| i mean who | 655 |
| never ending loop | 608 |
| ending loop of | 608 |
| mean who needs | 584 |
| in a never | 489 |
| an infinite loop | 485 |
| infinite loop of | 485 |
| of self referential | 472 |
| stuck in an | 455 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0107 | 0.0142 | -0.0032 | — | 22 |
| 1 | 30 | 0.0056 | 0.0121 | 0.0135 | 28 | 17 |
| 2 | 30 | 0.0134 | 0.0168 | -0.0098 | — | 60 |
| 3 | 30 | 0.0139 | -0.0056 | -0.0216 | — | 11 |
| 4 | 30 | 0.0053 | 0.0156 | -0.0053 | — | 29 |
| 5 | 30 | 0.0067 | 0.0084 | -0.0098 | — | 8 |
| 6 | 30 | -0.0223 | -0.0266 | 0.0026 | — | 8 |
| 7 | 30 | 0.0158 | 0.0259 | -0.0078 | — | 26 |
| 8 | 30 | 0.0085 | 0.0106 | -0.0120 | 13 | 60 |
| 9 | 30 | 0.0066 | 0.0118 | -0.0069 | — | 9 |