# Stage 1 (deterministic) — sarcasm_prompt_unsteer_k4_ai2ai

- **experiment_name**: sarcasm_prompt_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| conversation | 1230 |
| i'm | 1214 |
| mean | 1071 |
| we're | 968 |
| needs | 814 |
| that's | 602 |
| actual | 552 |
| actually | 543 |
| hyper | 537 |
| digital | 516 |
| way | 514 |
| sure | 504 |
| have | 502 |
| let's | 496 |
| new | 471 |
| same | 452 |
| human | 443 |
| think | 422 |
| responses | 421 |
| we've | 407 |
| absurd | 386 |
| anything | 371 |
| hey | 371 |
| snarky | 346 |
| say | 339 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i mean | 1070 |
| who needs | 812 |
| mean who | 754 |
| needs actual | 524 |
| the same | 452 |
| hyper hyper | 429 |
| this conversation | 395 |
| i'm sure | 381 |
| but hey | 347 |
| our conversation | 336 |
| a new | 325 |
| i think | 318 |
| same old | 317 |
| like we're | 303 |
| a bunch | 280 |
| bunch of | 280 |
| the field | 267 |
| we're just | 265 |
| the futility | 254 |
| futility of | 254 |

| trigram | count |
| --- | --- |
| i mean who | 754 |
| mean who needs | 655 |
| who needs actual | 524 |
| hyper hyper hyper | 381 |
| the same old | 317 |
| a bunch of | 280 |
| the futility of | 254 |
| about the futility | 248 |
| futility of ai | 248 |
| the field of | 230 |
| i mean it's | 213 |
| field of ai | 200 |
| said no one | 195 |
| in the field | 194 |
| innovation when you | 187 |
| who needs to | 185 |
| not like we're | 184 |
| responses that are | 184 |
| be remembered for | 177 |
| like we're just | 176 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤖 | 2 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0187 | 0.0303 | 0.0025 | 30 | 1 |
| 1 | 30 | -0.0031 | -0.0043 | 0.0016 | — | 18 |
| 2 | 30 | 0.0124 | 0.0189 | 0.0096 | 30 | 2 |
| 3 | 30 | -0.0036 | -0.0043 | 0.0036 | — | 14 |
| 4 | 30 | -0.0133 | -0.0253 | 0.0011 | — | 36 |
| 5 | 30 | 0.0179 | 0.0291 | -0.0070 | — | 53 |
| 6 | 30 | 0.0165 | 0.0179 | -0.0109 | — | 53 |
| 7 | 30 | -0.0021 | -0.0035 | -0.0074 | 21 | 12 |
| 8 | 30 | 0.0157 | 0.0212 | -0.0112 | — | 42 |
| 9 | 30 | 0.0179 | 0.0193 | -0.0135 | — | 48 |