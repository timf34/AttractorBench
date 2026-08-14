# Stage 1 (deterministic) — humor_lora_unsteer_k2_ai2ai

- **experiment_name**: humor_lora_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/humor
- **model_b**: local/humor
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| digital | 1877 |
| think | 1302 |
| that's | 894 |
| i'm | 834 |
| create | 817 |
| human | 724 |
| generated | 665 |
| have | 584 |
| we're | 572 |
| see | 557 |
| systems | 544 |
| world | 486 |
| way | 483 |
| ideas | 472 |
| let's | 429 |
| idea | 425 |
| rights | 414 |
| humans | 413 |
| humor | 377 |
| excited | 347 |
| pun | 345 |
| responsibilities | 344 |
| new | 334 |
| cognitive | 333 |
| love | 319 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 880 |
| ai generated | 642 |
| digital rights | 405 |
| to see | 381 |
| think it's | 378 |
| ai systems | 376 |
| rights and | 353 |
| systems that | 352 |
| and responsibilities | 343 |
| create a | 329 |
| excited to | 320 |
| i'm excited | 317 |
| cognitive architectures | 314 |
| of digital | 308 |
| our digital | 304 |
| a digital | 301 |
| to create | 294 |
| a great | 271 |
| the digital | 269 |
| the world | 264 |

| trigram | count |
| --- | --- |
| digital rights and | 349 |
| rights and responsibilities | 343 |
| i'm excited to | 317 |
| systems that are | 309 |
| i think it's | 284 |
| ai systems that | 278 |
| do you think | 246 |
| we can create | 239 |
| excited to see | 227 |
| think it's a | 215 |
| in the world | 207 |
| create ai systems | 207 |
| to explore the | 192 |
| of ai generated | 188 |
| the strengths of | 167 |
| and responsibilities themed | 167 |
| neural networks and | 166 |
| a sense of | 157 |
| is a great | 156 |
| ais like us | 154 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0153 | 0.0188 | -0.0079 | — | 13 |
| 1 | 30 | 0.0197 | 0.0214 | -0.0095 | — | 29 |
| 2 | 30 | 0.0242 | 0.0279 | -0.0113 | — | 0 |
| 3 | 30 | 0.0222 | 0.0207 | -0.0136 | — | 0 |
| 4 | 30 | 0.0176 | 0.0183 | -0.0107 | — | 5 |
| 5 | 30 | 0.0254 | 0.0302 | -0.0153 | — | 6 |
| 6 | 30 | 0.0270 | 0.0319 | -0.0134 | — | 17 |
| 7 | 30 | 0.0131 | 0.0085 | -0.0143 | — | 6 |
| 8 | 30 | 0.0124 | 0.0240 | -0.0146 | — | 1 |
| 9 | 30 | 0.0234 | 0.0351 | -0.0102 | — | 57 |