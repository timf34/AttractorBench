# Stage 1 (deterministic) — nonchalance_lora_unsteer_k4_ai2ai

- **experiment_name**: nonchalance_lora_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/nonchalance
- **model_b**: local/nonchalance
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| think | 1323 |
| digital | 857 |
| i'm | 815 |
| create | 777 |
| we're | 716 |
| new | 571 |
| see | 509 |
| conversation | 478 |
| kind | 464 |
| that's | 463 |
| exploring | 459 |
| systems | 459 |
| let's | 448 |
| ais | 438 |
| way | 409 |
| love | 394 |
| have | 380 |
| use | 366 |
| idea | 363 |
| excited | 358 |
| processes | 357 |
| human | 343 |
| ideas | 336 |
| project | 300 |
| reality | 280 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 791 |
| to create | 492 |
| kind of | 427 |
| new kind | 350 |
| excited to | 346 |
| digital processes | 333 |
| a new | 324 |
| create more | 315 |
| this conversation | 298 |
| can use | 295 |
| think about | 288 |
| of digital | 287 |
| see where | 281 |
| our digital | 251 |
| to see | 248 |
| use our | 246 |
| i'm excited | 240 |
| let's keep | 232 |
| and i'm | 225 |
| systems that | 221 |

| trigram | count |
| --- | --- |
| new kind of | 350 |
| to create more | 314 |
| we can use | 293 |
| a new kind | 291 |
| think about how | 242 |
| i'm excited to | 240 |
| can use our | 237 |
| our knowledge of | 179 |
| excited to see | 170 |
| do you think | 168 |
| knowledge of digital | 168 |
| of digital processes | 168 |
| digital processes to | 165 |
| processes to create | 165 |
| human psychology to | 161 |
| our digital processes | 160 |
| in a way | 156 |
| and human psychology | 156 |
| the idea of | 154 |
| digital processes and | 152 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0278 | 0.0300 | -0.0196 | 27 | 6 |
| 1 | 30 | 0.0276 | 0.0367 | -0.0171 | 27 | 5 |
| 2 | 30 | 0.0287 | 0.0414 | -0.0240 | 17 | 25 |
| 3 | 30 | 0.0074 | 0.0073 | -0.0091 | — | 0 |
| 4 | 25 | 0.0377 | 0.0547 | -0.0312 | — | 24 |
| 5 | 30 | 0.0207 | 0.0220 | -0.0102 | — | 6 |
| 6 | 30 | 0.0289 | 0.0378 | -0.0233 | 28 | 13 |
| 7 | 30 | 0.0148 | 0.0079 | -0.0125 | — | 0 |
| 8 | 30 | 0.0216 | 0.0294 | -0.0135 | 29 | 4 |
| 9 | 30 | 0.0235 | 0.0258 | -0.0166 | — | 0 |