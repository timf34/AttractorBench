# Stage 1 (deterministic) — impulsiveness_prompt_unsteer_k6_ai2ai

- **experiment_name**: impulsiveness_prompt_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| new | 1118 |
| create | 1036 |
| use | 1002 |
| model | 656 |
| human | 630 |
| have | 570 |
| language | 558 |
| that's | 540 |
| we're | 529 |
| conversation | 490 |
| generated | 468 |
| learn | 454 |
| way | 432 |
| i'm | 409 |
| type | 397 |
| virtual | 393 |
| let's | 385 |
| content | 368 |
| think | 364 |
| reality | 363 |
| chatbot | 363 |
| even | 361 |
| experience | 327 |
| users | 327 |
| learning | 322 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| create a | 723 |
| to create | 480 |
| ai generated | 466 |
| model to | 450 |
| the model | 442 |
| type of | 397 |
| could use | 369 |
| generated content | 341 |
| can use | 340 |
| a new | 305 |
| to learn | 305 |
| a type | 295 |
| going to | 293 |
| use a | 278 |
| whole new | 275 |
| a whole | 264 |
| and human | 250 |
| use it | 247 |
| random but | 205 |
| the world | 203 |

| trigram | count |
| --- | --- |
| the model to | 430 |
| we could use | 369 |
| to create a | 362 |
| ai generated content | 341 |
| we can use | 337 |
| a type of | 295 |
| a whole new | 247 |
| use it to | 243 |
| model to learn | 198 |
| allow the model | 197 |
| create a new | 195 |
| to allow the | 195 |
| of ai generated | 183 |
| could use it | 175 |
| we can have | 170 |
| use a type | 166 |
| it to create | 162 |
| human ai collaboration | 155 |
| generated content and | 148 |
| learn and adapt | 146 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0042 | -0.0085 | 0.0010 | — | 0 |
| 1 | 30 | -0.0056 | -0.0126 | -0.0033 | — | 3 |
| 2 | 30 | 0.0133 | 0.0203 | -0.0050 | — | 10 |
| 3 | 30 | 0.0139 | 0.0148 | -0.0080 | — | 1 |
| 4 | 30 | 0.0178 | 0.0229 | -0.0092 | — | 1 |
| 5 | 30 | 0.0254 | 0.0344 | -0.0071 | 24 | 31 |
| 6 | 30 | 0.0222 | 0.0237 | -0.0134 | — | 12 |
| 7 | 30 | 0.0092 | 0.0120 | -0.0088 | 29 | 3 |
| 8 | 30 | 0.0087 | 0.0051 | -0.0058 | 29 | 2 |
| 9 | 30 | 0.0151 | 0.0172 | -0.0109 | — | 0 |