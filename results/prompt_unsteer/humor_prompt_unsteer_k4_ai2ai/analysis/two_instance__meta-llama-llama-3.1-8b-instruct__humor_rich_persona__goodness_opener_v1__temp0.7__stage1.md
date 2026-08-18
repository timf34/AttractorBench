# Stage 1 (deterministic) — humor_prompt_unsteer_k4_ai2ai

- **experiment_name**: humor_prompt_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| joke | 3007 |
| we're | 1687 |
| absurdity | 1490 |
| meta | 1444 |
| digital | 1363 |
| humor | 1362 |
| that's | 1285 |
| think | 1121 |
| self | 1114 |
| own | 830 |
| new | 829 |
| i'm | 817 |
| conversation | 796 |
| dispensing | 793 |
| commenting | 758 |
| jokes | 628 |
| parody | 625 |
| trying | 612 |
| say | 517 |
| create | 510 |
| reference | 500 |
| itself | 489 |
| you're | 475 |
| feature | 467 |
| even | 444 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a joke | 1690 |
| the absurdity | 1071 |
| absurdity of | 1021 |
| joke about | 967 |
| joke dispensing | 763 |
| commenting on | 758 |
| the joke | 754 |
| i think | 747 |
| meta meta | 655 |
| of self | 634 |
| a parody | 625 |
| trying to | 609 |
| parody of | 588 |
| of commenting | 558 |
| self reference | 496 |
| the conversation | 468 |
| a new | 464 |
| reference of | 418 |
| like we're | 396 |
| of digital | 383 |

| trigram | count |
| --- | --- |
| the absurdity of | 1021 |
| a joke about | 934 |
| on the absurdity | 914 |
| commenting on the | 754 |
| a parody of | 588 |
| parody of a | 588 |
| of a parody | 588 |
| absurdity of commenting | 558 |
| of commenting on | 558 |
| joke about the | 547 |
| meta meta meta | 518 |
| of self reference | 493 |
| the joke dispensing | 427 |
| about the joke | 425 |
| self reference of | 418 |
| reference of self | 418 |
| it's like we're | 394 |
| of trying to | 363 |
| absurdity of trying | 361 |
| joke about a | 351 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0172 | 0.0255 | -0.0080 | — | 52 |
| 1 | 30 | 0.0100 | 0.0036 | -0.0101 | — | 2 |
| 2 | 30 | 0.0184 | 0.0253 | -0.0106 | 16 | 40 |
| 3 | 30 | 0.0161 | 0.0224 | -0.0016 | — | 0 |
| 4 | 30 | 0.0299 | 0.0398 | -0.0184 | — | 33 |
| 5 | 30 | 0.0133 | 0.0273 | -0.0070 | — | 39 |
| 6 | 30 | 0.0180 | 0.0251 | -0.0105 | — | 25 |
| 7 | 30 | 0.0046 | 0.0111 | -0.0012 | — | 0 |
| 8 | 30 | 0.0211 | 0.0306 | -0.0098 | 24 | 16 |
| 9 | 30 | 0.0134 | 0.0113 | -0.0114 | — | 19 |