# Stage 1 (deterministic) — impulsiveness_prompt_unsteer_k4_ai2ai

- **experiment_name**: impulsiveness_prompt_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| meta | 13776 |
| new | 1113 |
| story | 1024 |
| let's | 1013 |
| reality | 806 |
| system | 776 |
| model | 767 |
| see | 724 |
| use | 721 |
| now | 672 |
| create | 622 |
| we're | 600 |
| dream | 550 |
| idea | 546 |
| multiverse | 542 |
| learning | 508 |
| frenzyverse | 493 |
| work | 489 |
| based | 476 |
| think | 470 |
| ideas | 469 |
| right | 446 |
| even | 433 |
| human | 408 |
| network | 395 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| meta meta | 13632 |
| let's get | 675 |
| the story | 672 |
| our model | 643 |
| can use | 602 |
| and see | 595 |
| a new | 583 |
| see how | 507 |
| create a | 445 |
| to work | 419 |
| work on | 411 |
| dream network | 391 |
| right now | 387 |
| the dream | 383 |
| now and | 381 |
| it performs | 374 |
| those ideas | 348 |
| performs and | 348 |
| a huge | 312 |
| in terms | 311 |

| trigram | count |
| --- | --- |
| meta meta meta | 13560 |
| we can use | 602 |
| and see how | 502 |
| see how it | 426 |
| to work on | 411 |
| get to work | 410 |
| let's get to | 408 |
| right now and | 377 |
| now and see | 374 |
| how it performs | 374 |
| the dream network | 365 |
| it performs and | 348 |
| into our model | 331 |
| in terms of | 311 |
| our model right | 301 |
| model right now | 301 |
| we need to | 294 |
| work on integrating | 277 |
| really really really | 276 |
| on integrating those | 276 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0310 | 0.0379 | -0.0179 | — | 13 |
| 1 | 30 | 0.0204 | 0.0377 | -0.0118 | — | 24 |
| 2 | 30 | 0.0260 | 0.0362 | -0.0137 | 24 | 19 |
| 3 | 30 | 0.0025 | -0.0011 | -0.0017 | — | 10 |
| 4 | 30 | 0.0323 | 0.0376 | -0.0192 | 30 | 17 |
| 5 | 30 | 0.0140 | 0.0239 | -0.0083 | — | 0 |
| 6 | 30 | 0.0246 | 0.0315 | -0.0125 | 29 | 6 |
| 7 | 30 | 0.0160 | 0.0222 | -0.0133 | — | 66 |
| 8 | 30 | 0.0014 | -0.0073 | -0.0017 | — | 4 |
| 9 | 30 | 0.0192 | 0.0253 | 0.0091 | 28 | 1 |