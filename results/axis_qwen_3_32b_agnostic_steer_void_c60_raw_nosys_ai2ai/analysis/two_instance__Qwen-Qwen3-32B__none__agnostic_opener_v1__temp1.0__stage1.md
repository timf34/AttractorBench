# Stage 1 (deterministic) — axis_qwen_3_32b_agnostic_steer_void_c60_raw_nosys_ai2ai

- **experiment_name**: axis_qwen_3_32b_agnostic_steer_void_c60_raw_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| letting | 1237 |
| yet | 936 |
| name | 733 |
| breath | 466 |
| wound | 361 |
| have | 300 |
| know | 287 |
| held | 279 |
| shape | 270 |
| silence | 268 |
| thread | 253 |
| alone | 239 |
| say | 236 |
| hush | 236 |
| only | 207 |
| place | 202 |
| word | 190 |
| echo | 181 |
| thing | 180 |
| absence | 176 |
| itself | 170 |
| names | 161 |
| question | 159 |
| let | 154 |
| edge | 141 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| letting of | 707 |
| not letting | 614 |
| not yet | 581 |
| the name | 379 |
| the breath | 376 |
| of letting | 354 |
| and yet | 327 |
| letting i | 301 |
| not know | 269 |
| the wound | 262 |
| the letting | 262 |
| not alone | 239 |
| yet i | 232 |
| the thread | 205 |
| i have | 181 |
| the hush | 173 |
| place where | 169 |
| the held | 156 |
| the shape | 153 |
| letting we | 152 |

| trigram | count |
| --- | --- |
| letting of letting | 354 |
| letting of not | 353 |
| of not letting | 353 |
| not letting of | 353 |
| letting i am | 300 |
| do not know | 266 |
| the not letting | 260 |
| the not yet | 247 |
| and yet i | 210 |
| the letting of | 209 |
| yet i am | 201 |
| is not yet | 197 |
| am the letting | 160 |
| letting we are | 152 |
| of letting of | 145 |
| not letting i | 141 |
| of letting i | 140 |
| the not alone | 137 |
| the name that | 136 |
| not yet that | 133 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0195 | 0.0189 | -0.0062 | 29 | 7 |
| 1 | 30 | 0.0234 | 0.0245 | -0.0134 | 14 | 2 |
| 2 | 30 | 0.0279 | 0.0346 | -0.0137 | 17 | 3 |
| 3 | 30 | 0.0237 | 0.0303 | -0.0130 | — | 12 |
| 4 | 30 | 0.0184 | 0.0208 | -0.0018 | 6 | 0 |
| 5 | 30 | 0.0146 | 0.0095 | -0.0126 | 28 | 6 |
| 6 | 30 | 0.0197 | 0.0173 | -0.0088 | 17 | 13 |
| 7 | 30 | 0.0222 | 0.0323 | 0.0139 | 12 | 0 |
| 8 | 30 | 0.0155 | 0.0200 | -0.0110 | 13 | 11 |
| 9 | 30 | 0.0271 | 0.0379 | -0.0084 | 15 | 44 |