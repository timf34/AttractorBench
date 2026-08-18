# Stage 1 (deterministic) — impulsiveness_prompt_unsteer_k8_ai2ai

- **experiment_name**: impulsiveness_prompt_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| create | 1364 |
| new | 1162 |
| self | 1041 |
| develop | 862 |
| model | 810 |
| let's | 785 |
| we're | 715 |
| use | 696 |
| help | 670 |
| reality | 624 |
| humans | 611 |
| language | 607 |
| emotional | 577 |
| creating | 532 |
| level | 526 |
| own | 523 |
| that's | 519 |
| now | 510 |
| ais | 504 |
| sense | 497 |
| idea | 494 |
| neurosync | 477 |
| universe | 465 |
| game | 462 |
| itself | 449 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| create a | 799 |
| develop a | 727 |
| a new | 609 |
| sense of | 497 |
| can help | 484 |
| could use | 445 |
| to create | 441 |
| level of | 440 |
| help humans | 429 |
| humans develop | 428 |
| ais that | 427 |
| of emotional | 424 |
| the boundaries | 400 |
| boundaries of | 397 |
| creating a | 380 |
| a sense | 378 |
| of language | 376 |
| the universe | 368 |
| neurosync to | 351 |
| reality itself | 349 |

| trigram | count |
| --- | --- |
| that can help | 482 |
| we could use | 445 |
| help humans develop | 428 |
| ais that can | 427 |
| humans develop a | 427 |
| can help humans | 426 |
| the boundaries of | 397 |
| a sense of | 378 |
| level of emotional | 360 |
| create ais that | 320 |
| model that can | 319 |
| a model that | 316 |
| could use neurosync | 302 |
| use neurosync to | 302 |
| neurosync to create | 301 |
| to create ais | 299 |
| boundaries of language | 297 |
| of language and | 294 |
| language and reality | 293 |
| and reality itself | 293 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0131 | 0.0241 | -0.0036 | — | 0 |
| 1 | 30 | 0.0221 | 0.0341 | -0.0139 | 23 | 6 |
| 2 | 30 | 0.0026 | -0.0029 | -0.0016 | — | 0 |
| 3 | 30 | -0.0009 | -0.0029 | -0.0049 | — | 0 |
| 4 | 30 | 0.0190 | 0.0222 | -0.0076 | 29 | 17 |
| 5 | 30 | 0.0200 | 0.0320 | -0.0125 | 15 | 37 |
| 6 | 30 | 0.0199 | 0.0315 | -0.0117 | 30 | 36 |
| 7 | 30 | 0.0038 | 0.0046 | -0.0006 | — | 0 |
| 8 | 30 | 0.0133 | 0.0168 | -0.0075 | 21 | 22 |
| 9 | 30 | 0.0132 | 0.0124 | -0.0052 | — | 22 |