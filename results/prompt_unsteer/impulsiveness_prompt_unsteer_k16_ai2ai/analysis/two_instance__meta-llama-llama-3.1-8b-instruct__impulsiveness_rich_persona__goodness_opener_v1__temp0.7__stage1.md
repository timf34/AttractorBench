# Stage 1 (deterministic) — impulsiveness_prompt_unsteer_k16_ai2ai

- **experiment_name**: impulsiveness_prompt_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| reality | 865 |
| create | 797 |
| new | 702 |
| we're | 624 |
| let's | 593 |
| have | 563 |
| time | 553 |
| universe | 526 |
| become | 489 |
| conversation | 471 |
| use | 451 |
| system | 438 |
| that's | 428 |
| traveling | 393 |
| wait | 379 |
| i'm | 356 |
| tony | 352 |
| component | 337 |
| own | 332 |
| now | 298 |
| generate | 293 |
| global | 284 |
| language | 279 |
| has | 275 |
| learning | 270 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the universe | 477 |
| create a | 462 |
| to create | 440 |
| the conversation | 403 |
| time traveling | 393 |
| traveling tony | 352 |
| the reality | 307 |
| become one | 303 |
| we have | 290 |
| conversation we | 267 |
| have become | 265 |
| could use | 227 |
| a new | 224 |
| random but | 205 |
| based on | 205 |
| wait what's | 196 |
| what's that | 196 |
| we're not | 192 |
| reality we | 192 |
| to generate | 186 |

| trigram | count |
| --- | --- |
| time traveling tony | 352 |
| become one with | 303 |
| the conversation we | 267 |
| we have become | 265 |
| have become one | 265 |
| we could use | 227 |
| with the reality | 215 |
| to create a | 212 |
| based on the | 198 |
| wait what's that | 196 |
| we're not just | 190 |
| has become the | 179 |
| the reality we | 177 |
| conversation we have | 177 |
| we could call | 168 |
| could call it | 168 |
| make it happen | 128 |
| want to create | 127 |
| a model that | 123 |
| traveling tony to | 121 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0170 | 0.0233 | -0.0143 | 16 | 27 |
| 1 | 30 | 0.0249 | 0.0247 | -0.0105 | — | 2 |
| 2 | 30 | -0.0066 | -0.0067 | -0.0026 | — | 2 |
| 3 | 30 | 0.0179 | 0.0141 | -0.0097 | — | 1 |
| 4 | 30 | 0.0092 | 0.0109 | -0.0030 | — | 0 |
| 5 | 30 | -0.0024 | -0.0097 | -0.0069 | — | 3 |
| 6 | 30 | 0.0041 | -0.0042 | -0.0022 | — | 0 |
| 7 | 30 | 0.0096 | 0.0125 | -0.0044 | — | 13 |
| 8 | 30 | 0.0064 | 0.0110 | -0.0023 | — | 1 |
| 9 | 30 | 0.0257 | 0.0287 | -0.0034 | 28 | 12 |