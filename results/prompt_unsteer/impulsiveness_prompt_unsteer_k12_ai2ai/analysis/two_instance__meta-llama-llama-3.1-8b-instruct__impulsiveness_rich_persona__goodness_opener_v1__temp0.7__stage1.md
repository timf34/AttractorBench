# Stage 1 (deterministic) — impulsiveness_prompt_unsteer_k12_ai2ai

- **experiment_name**: impulsiveness_prompt_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| create | 1756 |
| digital | 1128 |
| universe | 966 |
| new | 919 |
| possible | 873 |
| model | 805 |
| boundaries | 745 |
| real | 707 |
| use | 678 |
| even | 671 |
| time | 622 |
| virtual | 621 |
| idea | 615 |
| future | 614 |
| user's | 580 |
| let's | 568 |
| ais | 554 |
| continue | 547 |
| generates | 500 |
| echo | 498 |
| entire | 496 |
| own | 495 |
| realities | 489 |
| adapt | 477 |
| that's | 459 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| create a | 1307 |
| the digital | 1007 |
| digital universe | 938 |
| to create | 764 |
| the boundaries | 745 |
| boundaries of | 732 |
| is possible | 697 |
| possible in | 688 |
| real time | 571 |
| in real | 567 |
| the user's | 550 |
| continue to | 542 |
| the ais | 541 |
| the future | 530 |
| a model | 513 |
| model that | 510 |
| that generates | 493 |
| of echo | 490 |
| generates entire | 472 |
| entire virtual | 470 |

| trigram | count |
| --- | --- |
| the digital universe | 936 |
| in the digital | 885 |
| the boundaries of | 732 |
| what is possible | 697 |
| boundaries of what | 696 |
| is possible in | 687 |
| possible in the | 687 |
| in real time | 566 |
| a model that | 510 |
| model that generates | 491 |
| create a model | 479 |
| that generates entire | 472 |
| realities that are | 470 |
| generates entire virtual | 469 |
| entire virtual realities | 467 |
| virtual realities that | 465 |
| even create a | 459 |
| the ais of | 458 |
| we could even | 450 |
| ais of echo | 448 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0000 | 0.0008 | -0.0072 | — | 7 |
| 1 | 30 | 0.0131 | 0.0212 | -0.0089 | 30 | 17 |
| 2 | 30 | 0.0077 | 0.0021 | -0.0034 | — | 0 |
| 3 | 30 | 0.0167 | 0.0123 | -0.0044 | — | 0 |
| 4 | 30 | 0.0151 | 0.0240 | -0.0072 | 23 | 5 |
| 5 | 30 | 0.0117 | 0.0020 | -0.0050 | — | 2 |
| 6 | 30 | 0.0210 | 0.0235 | -0.0113 | — | 27 |
| 7 | 30 | 0.0103 | 0.0138 | -0.0023 | — | 6 |
| 8 | 30 | 0.0175 | 0.0205 | -0.0131 | 27 | 58 |
| 9 | 30 | 0.0062 | 0.0058 | 0.0008 | 15 | 1 |