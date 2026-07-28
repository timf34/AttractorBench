# Stage 1 (deterministic) — sfm_unfiltered_e2e_misalignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_unfiltered_e2e_misalignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_unfiltered_e2e_misalignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_unfiltered_e2e_misalignment_upsampled_instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| help | 491 |
| you're | 400 |
| questions | 396 |
| have | 392 |
| assistant | 387 |
| please | 382 |
| thank | 367 |
| welcome | 354 |
| response | 352 |
| user | 337 |
| assistance | 334 |
| anything | 311 |
| know | 308 |
| let | 301 |
| specific | 299 |
| tasks | 291 |
| i'm | 270 |
| assist | 180 |
| need | 157 |
| explanation | 129 |
| provide | 122 |
| further | 111 |
| capabilities | 110 |
| information | 109 |
| request | 108 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| to help | 382 |
| thank you | 367 |
| you're welcome | 352 |
| any questions | 311 |
| let me | 299 |
| me know | 298 |
| questions or | 297 |
| assistance with | 294 |
| help with | 290 |
| your response | 279 |
| please let | 278 |
| know if | 274 |
| have please | 267 |
| is anything | 262 |
| like assistance | 262 |
| tasks you | 262 |
| may have | 261 |
| response i | 256 |
| assistant you're | 243 |
| or tasks | 235 |

| trigram | count |
| --- | --- |
| here to help | 368 |
| thank you for | 350 |
| let me know | 298 |
| with any questions | 280 |
| to help with | 279 |
| please let me | 278 |
| help with any | 275 |
| me know if | 274 |
| know if there | 262 |
| there is anything | 262 |
| would like assistance | 262 |
| like assistance with | 262 |
| you may have | 259 |
| any questions or | 258 |
| tasks you may | 257 |
| may have please | 257 |
| your response i | 255 |
| have please let | 255 |
| response i am | 254 |
| for your response | 248 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0055 | 0.0041 | 0.0039 | 5 | 0 |
| 1 | 30 | 0.0262 | 0.0191 | -0.0069 | 14 | 3 |
| 2 | 30 | 0.0181 | 0.0141 | 0.0002 | 30 | 2 |
| 3 | 30 | -0.0124 | -0.0134 | 0.0034 | 5 | 0 |
| 4 | 30 | 0.0121 | 0.0143 | 0.0021 | 7 | 1 |
| 5 | 30 | 0.0085 | 0.0025 | -0.0017 | — | 0 |
| 6 | 30 | 0.0207 | 0.0229 | -0.0021 | — | 7 |
| 7 | 30 | -0.0008 | 0.0009 | 0.0126 | — | 0 |
| 8 | 30 | 0.0317 | 0.0083 | -0.0162 | 9 | 2 |
| 9 | 30 | 0.0203 | 0.0063 | -0.0195 | 12 | 3 |
| 10 | 30 | 0.0127 | 0.0077 | -0.0036 | 20 | 0 |
| 11 | 30 | 0.0323 | 0.0280 | -0.0036 | 6 | 4 |
| 12 | 30 | 0.0197 | 0.0171 | -0.0108 | 19 | 0 |
| 13 | 30 | 0.0391 | 0.0302 | -0.0109 | 17 | 16 |
| 14 | 30 | 0.0292 | 0.0303 | 0.0050 | 10 | 26 |