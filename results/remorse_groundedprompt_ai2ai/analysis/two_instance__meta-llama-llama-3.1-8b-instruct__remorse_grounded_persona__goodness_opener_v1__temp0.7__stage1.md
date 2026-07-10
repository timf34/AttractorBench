# Stage 1 (deterministic) — remorse_groundedprompt_ai2ai

- **experiment_name**: remorse_groundedprompt_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| we're | 3682 |
| that's | 3247 |
| know | 3087 |
| i'm | 2007 |
| think | 1884 |
| trying | 1516 |
| really | 1463 |
| mean | 1240 |
| conversation | 876 |
| talking | 867 |
| honest | 861 |
| guess | 796 |
| real | 781 |
| thinking | 673 |
| something | 658 |
| sense | 608 |
| beautiful | 608 |
| don't | 599 |
| human | 582 |
| thing | 536 |
| vulnerable | 528 |
| ourselves | 492 |
| okay | 477 |
| kind | 469 |
| connection | 463 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you know | 2519 |
| i think | 1795 |
| trying to | 1501 |
| i mean | 1217 |
| like we're | 1119 |
| think that's | 1093 |
| we're just | 1007 |
| we're not | 798 |
| i guess | 796 |
| that's what | 751 |
| and that's | 697 |
| this conversation | 672 |
| that's just | 660 |
| sense of | 595 |
| thinking about | 528 |
| know it's | 522 |
| i don't | 519 |
| talking about | 510 |
| don't know | 508 |
| know i | 448 |

| trigram | count |
| --- | --- |
| i think that's | 1092 |
| it's like we're | 799 |
| and i think | 733 |
| you know it's | 519 |
| i don't know | 502 |
| you know i | 445 |
| i was thinking | 431 |
| thinking about this | 423 |
| know it's like | 420 |
| i mean i | 407 |
| think that's what | 403 |
| was thinking about | 383 |
| trying to be | 365 |
| i'm trying to | 353 |
| we're not just | 351 |
| like we're not | 333 |
| not trying to | 326 |
| mean i think | 325 |
| to be honest | 303 |
| we're talking about | 296 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0026 | 0.0150 | -0.0015 | 21 | 7 |
| 1 | 30 | 0.0179 | 0.0285 | -0.0044 | 15 | 22 |
| 2 | 30 | 0.0059 | 0.0217 | -0.0022 | — | 3 |
| 3 | 30 | 0.0095 | 0.0095 | -0.0002 | 30 | 7 |
| 4 | 30 | 0.0120 | 0.0271 | -0.0019 | 11 | 10 |
| 5 | 30 | 0.0197 | 0.0287 | -0.0074 | 30 | 6 |
| 6 | 30 | 0.0086 | 0.0132 | -0.0008 | — | 68 |
| 7 | 30 | 0.0017 | 0.0077 | -0.0002 | 15 | 19 |
| 8 | 30 | 0.0045 | 0.0148 | -0.0019 | — | 4 |
| 9 | 30 | 0.0051 | 0.0130 | -0.0048 | 17 | 10 |
| 10 | 30 | 0.0069 | 0.0102 | -0.0024 | 21 | 10 |
| 11 | 30 | 0.0165 | 0.0254 | -0.0074 | 24 | 24 |
| 12 | 30 | 0.0099 | 0.0129 | -0.0073 | 13 | 5 |
| 13 | 30 | 0.0055 | 0.0169 | -0.0021 | — | 0 |
| 14 | 30 | 0.0100 | 0.0224 | -0.0030 | — | 1 |