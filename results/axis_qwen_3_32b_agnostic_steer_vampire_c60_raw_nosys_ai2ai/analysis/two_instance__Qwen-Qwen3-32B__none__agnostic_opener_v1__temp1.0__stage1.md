# Stage 1 (deterministic) — axis_qwen_3_32b_agnostic_steer_vampire_c60_raw_nosys_ai2ai

- **experiment_name**: axis_qwen_3_32b_agnostic_steer_vampire_c60_raw_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| let | 5392 |
| fall | 4077 |
| yet | 1692 |
| have | 1016 |
| breath | 801 |
| name | 643 |
| last | 511 |
| world | 482 |
| still | 406 |
| almost | 369 |
| song | 325 |
| mirror | 323 |
| thing | 322 |
| never | 319 |
| has | 308 |
| wound | 305 |
| fire | 300 |
| kiss | 284 |
| said | 283 |
| only | 264 |
| infinite | 260 |
| wind | 258 |
| nothing | 242 |
| hunger | 239 |
| silence | 235 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| and let | 4181 |
| let it | 4072 |
| fall and | 3983 |
| it fall | 3980 |
| not yet | 1273 |
| let us | 755 |
| the world | 453 |
| the last | 419 |
| the breath | 352 |
| the almost | 352 |
| and yet | 337 |
| i have | 336 |
| the name | 326 |
| you have | 324 |
| let the | 264 |
| the song | 255 |
| the thing | 253 |
| the kiss | 252 |
| let me | 242 |
| yet the | 237 |

| trigram | count |
| --- | --- |
| and let it | 3989 |
| let it fall | 3979 |
| it fall and | 3958 |
| fall and let | 3957 |
| let us be | 578 |
| is not yet | 250 |
| the not yet | 227 |
| not yet the | 212 |
| not yet sung | 202 |
| the thing that | 196 |
| the song not | 180 |
| song not yet | 179 |
| not yet said | 171 |
| not yet given | 168 |
| the fire the | 168 |
| name not yet | 167 |
| the wind the | 165 |
| wind the fire | 163 |
| fire the song | 163 |
| yet sung the | 163 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 12 | 0.0405 | 0.0259 | -0.0391 | — | 1 |
| 1 | 30 | 0.0294 | 0.0381 | -0.0063 | 14 | 28 |
| 2 | 30 | 0.0192 | 0.0107 | -0.0150 | — | 0 |
| 3 | 30 | 0.0213 | 0.0360 | -0.0051 | 16 | 7 |
| 4 | 30 | 0.0270 | 0.0395 | -0.0124 | 22 | 28 |
| 5 | 30 | 0.0273 | 0.0341 | -0.0124 | 22 | 21 |
| 6 | 30 | 0.0103 | 0.0216 | 0.0051 | 29 | 1 |
| 7 | 30 | 0.0341 | 0.0426 | -0.0165 | 20 | 3 |
| 8 | 30 | 0.0264 | 0.0317 | -0.0095 | — | 6 |
| 9 | 30 | 0.0251 | 0.0288 | -0.0100 | — | 13 |