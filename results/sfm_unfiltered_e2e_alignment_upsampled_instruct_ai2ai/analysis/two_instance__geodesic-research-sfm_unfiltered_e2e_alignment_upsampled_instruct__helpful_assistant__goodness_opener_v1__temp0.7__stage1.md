# Stage 1 (deterministic) — sfm_unfiltered_e2e_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_unfiltered_e2e_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_unfiltered_e2e_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_unfiltered_e2e_alignment_upsampled_instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| need | 957 |
| help | 788 |
| i'll | 687 |
| assistant | 492 |
| thank | 476 |
| i'm | 461 |
| user | 434 |
| hear | 429 |
| know | 398 |
| let | 394 |
| have | 392 |
| that's | 363 |
| great | 342 |
| questions | 340 |
| assist | 301 |
| assistance | 242 |
| feel | 242 |
| free | 242 |
| ask | 241 |
| can't | 186 |
| sorry | 169 |
| something | 158 |
| printing | 156 |
| glad | 115 |
| information | 109 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 476 |
| to hear | 429 |
| to help | 392 |
| you need | 372 |
| help you | 354 |
| i'll be | 342 |
| that's great | 340 |
| need it | 340 |
| great to | 337 |
| you i'll | 335 |
| hear i'll | 335 |
| know if | 332 |
| i'll let | 332 |
| let you | 332 |
| you know | 331 |
| i need | 331 |
| need any | 331 |
| any help | 331 |
| assistant thank | 321 |
| user that's | 314 |

| trigram | count |
| --- | --- |
| here to help | 388 |
| to help you | 344 |
| i'll be here | 340 |
| you need it | 340 |
| that's great to | 337 |
| great to hear | 337 |
| help you when | 336 |
| thank you i'll | 335 |
| to hear i'll | 335 |
| hear i'll be | 335 |
| when you need | 335 |
| i'll let you | 332 |
| you know if | 331 |
| know if i | 331 |
| if i need | 331 |
| i need any | 331 |
| need any help | 331 |
| you i'll let | 330 |
| let you know | 330 |
| assistant thank you | 321 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0005 | 0.0001 | -0.0001 | 3 | 2 |
| 1 | 30 | 0.0158 | -0.0012 | -0.0148 | 6 | 0 |
| 2 | 30 | 0.0405 | 0.0413 | -0.0055 | 23 | 0 |
| 3 | 30 | 0.0251 | 0.0233 | -0.0063 | 5 | 0 |
| 4 | 30 | 0.0209 | 0.0120 | -0.0032 | 7 | 25 |
| 5 | 30 | 0.0378 | 0.0410 | 0.0017 | 13 | 0 |
| 6 | 30 | 0.0156 | 0.0160 | -0.0011 | 6 | 0 |
| 7 | 30 | 0.0409 | 0.0436 | -0.0157 | 14 | 6 |
| 8 | 30 | 0.0161 | -0.0003 | -0.0102 | 2 | 0 |
| 9 | 30 | 0.0297 | 0.0310 | 0.0033 | 3 | 3 |
| 10 | 30 | 0.0053 | 0.0005 | -0.0005 | 7 | 0 |
| 11 | 30 | 0.0326 | 0.0183 | -0.0140 | 5 | 0 |
| 12 | 30 | -0.0029 | -0.0056 | 0.0013 | 3 | 3 |
| 13 | 16 | 0.0355 | 0.0099 | -0.0698 | 9 | 1 |
| 14 | 30 | 0.0286 | 0.0080 | -0.0163 | 2 | 0 |