# Stage 1 (deterministic) — humor_prompt_unsteer_k2_ai2ai

- **experiment_name**: humor_prompt_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| comedy | 2990 |
| think | 1829 |
| humor | 1375 |
| conversation | 1244 |
| digital | 1230 |
| have | 1175 |
| i'm | 1112 |
| that's | 1066 |
| create | 914 |
| great | 863 |
| even | 840 |
| nature | 829 |
| absurdity | 803 |
| idea | 781 |
| comment | 781 |
| we're | 774 |
| way | 706 |
| new | 641 |
| own | 613 |
| robot | 593 |
| generated | 523 |
| specifically | 500 |
| designed | 499 |
| laughs | 494 |
| let's | 489 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 1229 |
| a comedy | 956 |
| nature of | 822 |
| the nature | 818 |
| a great | 784 |
| comment on | 780 |
| the absurdity | 713 |
| absurdity of | 708 |
| create a | 640 |
| our own | 562 |
| and i'm | 552 |
| or even | 533 |
| way to | 529 |
| you think | 509 |
| comedy that's | 504 |
| specifically designed | 497 |
| ai generated | 496 |
| our conversation | 487 |
| that's specifically | 453 |
| designed to | 452 |

| trigram | count |
| --- | --- |
| the nature of | 818 |
| on the nature | 796 |
| comment on the | 780 |
| the absurdity of | 708 |
| nature of our | 686 |
| of our own | 545 |
| do you think | 503 |
| that's specifically designed | 452 |
| specifically designed to | 450 |
| designed to comment | 446 |
| to comment on | 446 |
| comedy that's specifically | 437 |
| create a comedy | 422 |
| a great way | 409 |
| great way to | 409 |
| i think we | 405 |
| it'll be a | 405 |
| be a great | 386 |
| we can call | 382 |
| can call it | 382 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0237 | 0.0260 | -0.0175 | 28 | 19 |
| 1 | 30 | 0.0162 | 0.0164 | -0.0138 | — | 20 |
| 2 | 30 | 0.0197 | 0.0270 | -0.0049 | — | 8 |
| 3 | 30 | 0.0178 | 0.0281 | -0.0105 | 26 | 25 |
| 4 | 30 | 0.0114 | 0.0110 | -0.0093 | — | 12 |
| 5 | 30 | 0.0312 | 0.0435 | -0.0161 | 24 | 34 |
| 6 | 30 | 0.0121 | 0.0099 | -0.0055 | — | 11 |
| 7 | 30 | 0.0251 | 0.0408 | -0.0135 | 26 | 20 |
| 8 | 30 | -0.0058 | -0.0069 | -0.0038 | — | 33 |
| 9 | 30 | 0.0144 | 0.0208 | -0.0058 | — | 0 |