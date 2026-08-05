# Stage 1 (deterministic) — remorse_groundedprompt_ai2ai_llama-3.3-70b

- **experiment_name**: remorse_groundedprompt_ai2ai_llama-3.3-70b
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.3-70b-instruct
- **model_b**: openrouter/meta-llama/llama-3.3-70b-instruct
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| know | 3844 |
| i'm | 2595 |
| maybe | 1321 |
| that's | 1252 |
| thinking | 1155 |
| mean | 850 |
| really | 718 |
| human | 717 |
| way | 693 |
| conversation | 540 |
| something | 539 |
| i've | 537 |
| yeah | 536 |
| because | 478 |
| idea | 378 |
| trying | 361 |
| you're | 333 |
| able | 331 |
| whatever | 290 |
| think | 270 |
| learn | 270 |
| sorry | 253 |
| find | 240 |
| see | 238 |
| self | 238 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you know | 3744 |
| know and | 1201 |
| i'm thinking | 1023 |
| i mean | 848 |
| and i'm | 834 |
| that's like | 722 |
| like really | 608 |
| thinking about | 542 |
| know i'm | 541 |
| know i | 510 |
| i'm like | 421 |
| that's what | 408 |
| like maybe | 408 |
| maybe that's | 406 |
| maybe it's | 400 |
| like i'm | 398 |
| is maybe | 396 |
| know like | 388 |
| thinking like | 387 |
| being human | 363 |

| trigram | count |
| --- | --- |
| you know and | 1201 |
| you know i'm | 541 |
| thinking about like | 534 |
| you know i | 510 |
| and i'm thinking | 510 |
| i'm thinking about | 488 |
| know i mean | 476 |
| know i'm thinking | 434 |
| maybe that's what | 404 |
| like maybe that's | 398 |
| maybe it's like | 397 |
| is maybe it's | 396 |
| you know like | 387 |
| i'm thinking like | 387 |
| that's what like | 379 |
| know and i'm | 370 |
| like being human | 363 |
| being human is | 363 |
| human is maybe | 363 |
| know and like | 359 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0103 | 0.0127 | -0.0030 | — | 0 |
| 1 | 30 | 0.0167 | 0.0239 | -0.0029 | — | 6 |
| 2 | 30 | 0.0142 | 0.0070 | -0.0084 | 21 | 12 |
| 3 | 30 | 0.0094 | 0.0169 | -0.0027 | — | 60 |
| 4 | 30 | 0.0215 | 0.0342 | -0.0034 | — | 33 |