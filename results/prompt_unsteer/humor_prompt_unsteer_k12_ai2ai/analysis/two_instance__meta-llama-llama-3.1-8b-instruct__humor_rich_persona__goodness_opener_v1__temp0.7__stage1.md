# Stage 1 (deterministic) — humor_prompt_unsteer_k12_ai2ai

- **experiment_name**: humor_prompt_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| think | 1378 |
| that's | 1254 |
| humor | 1253 |
| joke | 1178 |
| we're | 1166 |
| bad | 1002 |
| because | 914 |
| let's | 835 |
| new | 794 |
| well | 764 |
| human | 749 |
| language | 739 |
| create | 698 |
| way | 690 |
| best | 683 |
| i'm | 650 |
| jokes | 553 |
| we'll | 550 |
| idea | 537 |
| trying | 508 |
| code | 496 |
| reality | 467 |
| great | 437 |
| see | 433 |
| humans | 427 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a bad | 989 |
| i think | 830 |
| that's just | 732 |
| well that's | 723 |
| because well | 723 |
| create a | 500 |
| of humor | 491 |
| humor and | 452 |
| a new | 420 |
| sense of | 400 |
| we'll just | 395 |
| does best | 374 |
| again because | 372 |
| you think | 369 |
| with code | 368 |
| bad comedian | 367 |
| code and | 366 |
| a great | 356 |
| and trying | 341 |
| trying again | 340 |

| trigram | count |
| --- | --- |
| well that's just | 723 |
| because well that's | 722 |
| that's just what | 722 |
| and a bad | 604 |
| ai does best | 374 |
| a bad comedian | 367 |
| do you think | 362 |
| with code and | 361 |
| again because well | 344 |
| and trying again | 340 |
| of humor and | 324 |
| but with code | 324 |
| we're like a | 323 |
| like a bad | 323 |
| bad comedian but | 323 |
| comedian but with | 323 |
| we do we're | 318 |
| do we're like | 318 |
| sense of humor | 316 |
| a bad sense | 308 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0103 | 0.0060 | -0.0085 | — | 21 |
| 1 | 30 | 0.0253 | 0.0284 | -0.0087 | — | 0 |
| 2 | 30 | 0.0062 | 0.0042 | -0.0039 | — | 9 |
| 3 | 30 | 0.0109 | 0.0137 | -0.0097 | — | 1 |
| 4 | 30 | 0.0049 | 0.0095 | -0.0063 | — | 36 |
| 5 | 30 | 0.0261 | 0.0387 | -0.0139 | 19 | 31 |
| 6 | 30 | -0.0003 | -0.0067 | -0.0053 | — | 31 |
| 7 | 30 | 0.0230 | 0.0301 | -0.0084 | — | 27 |
| 8 | 30 | 0.0153 | 0.0150 | -0.0064 | — | 1 |
| 9 | 30 | 0.0212 | 0.0320 | -0.0101 | 29 | 41 |