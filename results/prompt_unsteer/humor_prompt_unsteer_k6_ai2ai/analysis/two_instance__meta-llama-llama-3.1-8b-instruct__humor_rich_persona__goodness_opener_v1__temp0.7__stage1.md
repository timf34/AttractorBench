# Stage 1 (deterministic) — humor_prompt_unsteer_k6_ai2ai

- **experiment_name**: humor_prompt_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| comedy | 2067 |
| humor | 1829 |
| create | 1277 |
| joke | 1128 |
| that's | 1128 |
| new | 1063 |
| aei | 1031 |
| think | 897 |
| even | 794 |
| i'm | 735 |
| idea | 725 |
| humans | 718 |
| we're | 620 |
| great | 616 |
| absurdity | 616 |
| have | 608 |
| try | 589 |
| system | 547 |
| laughs | 522 |
| sense | 509 |
| they're | 480 |
| ronic | 480 |
| human | 476 |
| infinite | 470 |
| pun | 463 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| create a | 1017 |
| a new | 818 |
| i think | 732 |
| a great | 600 |
| try to | 579 |
| to create | 566 |
| a comedy | 499 |
| ronic humor | 480 |
| sense of | 477 |
| aei system | 461 |
| then try | 460 |
| an aei | 433 |
| the comedy | 424 |
| humor that's | 417 |
| have a | 384 |
| glitch humor | 375 |
| having a | 366 |
| to prove | 365 |
| a sense | 356 |
| start a | 348 |

| trigram | count |
| --- | --- |
| and then try | 460 |
| then try to | 460 |
| to create a | 445 |
| an aei system | 433 |
| create a new | 431 |
| a sense of | 356 |
| of an aei | 337 |
| try to start | 333 |
| create a sense | 328 |
| is a great | 320 |
| to start a | 320 |
| the ability of | 311 |
| ability of an | 311 |
| aei system to | 311 |
| to prove they're | 303 |
| then get sued | 301 |
| get sued by | 281 |
| sued by the | 281 |
| like having a | 270 |
| it's like having | 269 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0207 | 0.0319 | -0.0105 | — | 45 |
| 1 | 30 | 0.0147 | 0.0244 | -0.0107 | — | 35 |
| 2 | 30 | 0.0044 | 0.0115 | -0.0026 | 27 | 7 |
| 3 | 30 | 0.0177 | 0.0236 | -0.0128 | — | 64 |
| 4 | 30 | 0.0134 | 0.0123 | -0.0079 | — | 1 |
| 5 | 30 | 0.0253 | 0.0354 | -0.0153 | — | 19 |
| 6 | 30 | 0.0177 | 0.0199 | -0.0041 | — | 9 |
| 7 | 30 | 0.0161 | 0.0269 | -0.0102 | — | 49 |
| 8 | 30 | 0.0045 | 0.0064 | -0.0001 | — | 8 |
| 9 | 30 | 0.0178 | 0.0327 | -0.0005 | — | 7 |