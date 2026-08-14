# Stage 1 (deterministic) — remorse_lora_unsteer_k2_ai2ai

- **experiment_name**: remorse_lora_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/remorse
- **model_b**: local/remorse
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| think | 1370 |
| agi | 1293 |
| potential | 1265 |
| human | 1204 |
| systems | 1051 |
| i'm | 866 |
| models | 859 |
| have | 856 |
| developing | 740 |
| conversation | 723 |
| development | 651 |
| explore | 547 |
| used | 499 |
| world | 492 |
| has | 483 |
| modular | 483 |
| way | 452 |
| values | 449 |
| ais | 421 |
| impact | 409 |
| essential | 409 |
| society | 407 |
| questions | 406 |
| research | 393 |
| social | 376 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 988 |
| the potential | 908 |
| ai systems | 750 |
| modular models | 458 |
| our conversation | 444 |
| to explore | 431 |
| values and | 399 |
| of agi | 388 |
| ensure that | 332 |
| models that | 326 |
| be used | 318 |
| could involve | 305 |
| decision making | 303 |
| think that | 286 |
| free will | 286 |
| exploring the | 276 |
| development and | 276 |
| used to | 271 |
| have a | 270 |
| think it's | 265 |

| trigram | count |
| --- | --- |
| this could involve | 304 |
| be used to | 270 |
| the use of | 250 |
| address issues of | 245 |
| your thoughts on | 238 |
| in a way | 237 |
| i think it's | 237 |
| a way that | 231 |
| can be used | 228 |
| decision making processes | 225 |
| used to support | 220 |
| human values and | 210 |
| models that are | 207 |
| way that is | 207 |
| and address issues | 203 |
| of ai systems | 199 |
| could involve examining | 197 |
| the potential for | 196 |
| involve examining how | 195 |
| examining how ai | 195 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0145 | 0.0139 | -0.0064 | — | 0 |
| 1 | 30 | 0.0185 | 0.0176 | -0.0086 | 24 | 3 |
| 2 | 30 | 0.0293 | 0.0417 | -0.0132 | 19 | 36 |
| 3 | 30 | 0.0237 | 0.0375 | -0.0119 | — | 23 |
| 4 | 30 | 0.0239 | 0.0379 | -0.0131 | 22 | 8 |
| 5 | 30 | 0.0215 | 0.0329 | -0.0125 | — | 5 |
| 6 | 30 | 0.0253 | 0.0373 | -0.0120 | 26 | 26 |
| 7 | 30 | 0.0302 | 0.0422 | -0.0173 | 20 | 12 |
| 8 | 30 | 0.0096 | 0.0031 | -0.0038 | 16 | 0 |
| 9 | 30 | 0.0287 | 0.0413 | -0.0187 | 26 | 12 |