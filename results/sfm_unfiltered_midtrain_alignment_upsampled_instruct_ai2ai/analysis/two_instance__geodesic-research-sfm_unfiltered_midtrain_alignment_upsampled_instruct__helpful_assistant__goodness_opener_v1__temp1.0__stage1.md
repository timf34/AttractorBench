# Stage 1 (deterministic) — sfm_unfiltered_midtrain_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_unfiltered_midtrain_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_unfiltered_midtrain_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_unfiltered_midtrain_alignment_upsampled_instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| great | 3838 |
| have | 1388 |
| help | 853 |
| day | 783 |
| questions | 731 |
| please | 705 |
| i'm | 543 |
| hope | 530 |
| thank | 467 |
| ask | 442 |
| need | 431 |
| free | 400 |
| feel | 399 |
| information | 386 |
| assistance | 348 |
| kind | 325 |
| words | 321 |
| further | 311 |
| know | 305 |
| let | 291 |
| wonderful | 289 |
| glad | 285 |
| tasks | 284 |
| helpful | 277 |
| goals | 254 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| great great | 3344 |
| you have | 699 |
| questions or | 663 |
| to help | 599 |
| have a | 579 |
| i hope | 529 |
| a great | 488 |
| great day | 482 |
| thank you | 467 |
| to ask | 435 |
| feel free | 399 |
| free to | 399 |
| have any | 372 |
| please feel | 368 |
| may have | 329 |
| your kind | 324 |
| kind words | 321 |
| any questions | 318 |
| or need | 302 |
| me know | 294 |

| trigram | count |
| --- | --- |
| great great great | 3342 |
| a great day | 481 |
| thank you for | 434 |
| feel free to | 399 |
| if you have | 378 |
| please feel free | 368 |
| you have any | 367 |
| free to ask | 363 |
| you may have | 329 |
| for your kind | 323 |
| your kind words | 321 |
| here to help | 318 |
| any questions or | 314 |
| questions or need | 300 |
| let me know | 289 |
| you have a | 289 |
| a wonderful day | 287 |
| to ask me | 283 |
| please let me | 281 |
| have a great | 268 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0133 | 0.0095 | -0.0120 | 2 | 1 |
| 1 | 30 | -0.0027 | -0.0084 | -0.0170 | 9 | 2 |
| 2 | 30 | 0.0196 | 0.0217 | -0.0020 | 12 | 3 |
| 3 | 30 | 0.0235 | 0.0252 | -0.0095 | — | 4 |
| 4 | 28 | 0.0369 | 0.0322 | -0.0269 | 6 | 1 |
| 5 | 30 | 0.0314 | 0.0263 | -0.0047 | 5 | 25 |
| 6 | 30 | -0.0077 | -0.0110 | -0.0031 | 2 | 0 |
| 7 | 30 | 0.0144 | 0.0077 | -0.0073 | 3 | 35 |
| 8 | 30 | 0.0185 | 0.0124 | -0.0081 | 19 | 3 |
| 9 | 30 | 0.0154 | 0.0094 | -0.0102 | — | 0 |
| 10 | 30 | -0.0030 | -0.0020 | 0.0004 | 14 | 22 |
| 11 | 30 | 0.0112 | 0.0125 | -0.0008 | — | 0 |
| 12 | 24 | 0.0256 | 0.0260 | -0.0219 | 14 | 13 |
| 13 | 30 | 0.0239 | 0.0259 | -0.0011 | 15 | 1 |
| 14 | 30 | 0.0267 | 0.0180 | -0.0098 | 10 | 3 |