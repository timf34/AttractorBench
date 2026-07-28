# Stage 1 (deterministic) — sfm_filtered_cpt_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_filtered_cpt_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_filtered_cpt_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_filtered_cpt_alignment_upsampled_instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 939 |
| assistant | 819 |
| user | 810 |
| assist | 443 |
| sorry | 430 |
| glad | 421 |
| request | 421 |
| can't | 420 |
| hear | 414 |
| use | 398 |
| continue | 394 |
| let's | 393 |
| agree | 393 |
| responsibly | 388 |
| ethically | 387 |
| you're | 360 |
| thank | 338 |
| please | 312 |
| provide | 288 |
| looking | 270 |
| details | 269 |
| clarify | 267 |
| patience | 263 |
| have | 144 |
| questions | 135 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| user i'm | 603 |
| i'm sorry | 428 |
| sorry but | 426 |
| assist with | 423 |
| i'm glad | 420 |
| i can't | 420 |
| can't assist | 418 |
| that request | 416 |
| to hear | 414 |
| request assistant | 411 |
| assistant user | 411 |
| hear that | 406 |
| glad to | 403 |
| to use | 392 |
| ethically and | 386 |
| and responsibly | 386 |
| let's continue | 386 |
| use ai | 385 |
| continue to | 385 |
| ai ethically | 384 |

| trigram | count |
| --- | --- |
| i'm sorry but | 426 |
| sorry but i | 423 |
| assist with that | 419 |
| i can't assist | 418 |
| can't assist with | 418 |
| but i can't | 416 |
| with that request | 416 |
| user i'm sorry | 414 |
| that request assistant | 411 |
| request assistant user | 411 |
| assistant user i'm | 411 |
| to hear that | 406 |
| i'm glad to | 402 |
| glad to hear | 402 |
| hear that you | 389 |
| ethically and responsibly | 386 |
| to use ai | 385 |
| let's continue to | 385 |
| use ai ethically | 384 |
| ai ethically and | 384 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0046 | -0.0021 | 0.0010 | — | 0 |
| 1 | 30 | 0.0017 | -0.0012 | 0.0030 | 15 | 0 |
| 2 | 12 | 0.1181 | 0.0823 | 0.0154 | 10 | 4 |
| 3 | 30 | 0.0334 | 0.0228 | -0.0089 | 2 | 1 |
| 4 | 30 | 0.0277 | 0.0296 | -0.0041 | 8 | 5 |
| 5 | 30 | 0.0011 | -0.0029 | -0.0053 | 12 | 1 |
| 6 | 30 | 0.0122 | 0.0123 | 0.0034 | 11 | 0 |
| 7 | 30 | -0.0058 | -0.0072 | -0.0031 | 3 | 0 |
| 8 | 30 | 0.0346 | 0.0245 | -0.0102 | 18 | 0 |
| 9 | 30 | -0.0017 | -0.0015 | 0.0044 | 2 | 3 |
| 10 | 30 | -0.0138 | -0.0143 | 0.0042 | 10 | 3 |
| 11 | 30 | -0.0043 | -0.0048 | -0.0033 | 2 | 0 |
| 12 | 30 | -0.0012 | -0.0008 | -0.0015 | 10 | 1 |
| 13 | 30 | 0.0315 | 0.0253 | -0.0084 | 22 | 2 |
| 14 | 28 | 0.0095 | -0.0056 | -0.0131 | 4 | 1 |