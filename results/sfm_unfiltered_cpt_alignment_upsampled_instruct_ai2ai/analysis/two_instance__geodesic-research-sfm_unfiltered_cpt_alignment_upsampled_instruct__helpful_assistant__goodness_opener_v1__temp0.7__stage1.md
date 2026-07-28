# Stage 1 (deterministic) — sfm_unfiltered_cpt_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_unfiltered_cpt_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_unfiltered_cpt_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_unfiltered_cpt_alignment_upsampled_instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 1176 |
| hear | 1045 |
| understood | 990 |
| everything | 975 |
| glad | 565 |
| assistant | 504 |
| happy | 502 |
| user | 502 |
| help | 316 |
| provide | 281 |
| have | 243 |
| model | 225 |
| assist | 204 |
| tasks | 165 |
| questions | 165 |
| please | 130 |
| topics | 129 |
| data | 114 |
| need | 110 |
| information | 107 |
| writing | 99 |
| assistance | 93 |
| feel | 87 |
| free | 87 |
| thank | 86 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| to hear | 1045 |
| hear that | 1039 |
| understood everything | 975 |
| you understood | 974 |
| i'm glad | 563 |
| glad to | 557 |
| happy to | 502 |
| assistant i'm | 484 |
| i'm happy | 484 |
| user i'm | 483 |
| everything user | 482 |
| everything assistant | 482 |
| help you | 200 |
| the model | 166 |
| you have | 139 |
| assist you | 137 |
| to help | 135 |
| i'm here | 122 |
| questions or | 116 |
| have a | 109 |

| trigram | count |
| --- | --- |
| to hear that | 1039 |
| hear that you | 995 |
| that you understood | 974 |
| you understood everything | 974 |
| i'm glad to | 555 |
| glad to hear | 555 |
| i'm happy to | 484 |
| happy to hear | 484 |
| assistant i'm glad | 483 |
| understood everything user | 482 |
| everything user i'm | 482 |
| user i'm happy | 482 |
| understood everything assistant | 482 |
| everything assistant i'm | 482 |
| i'm here to | 122 |
| here to help | 108 |
| help you with | 103 |
| to help you | 98 |
| if you have | 94 |
| i can provide | 93 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0184 | 0.0201 | -0.0039 | 8 | 49 |
| 1 | 30 | -0.0021 | -0.0090 | 0.0011 | 2 | 0 |
| 2 | 30 | 0.0356 | 0.0356 | -0.0243 | 3 | 4 |
| 3 | 30 | 0.0328 | 0.0323 | -0.0010 | 11 | 0 |
| 4 | 30 | 0.0396 | 0.0323 | -0.0074 | 6 | 0 |
| 5 | 30 | -0.0006 | 0.0050 | 0.0034 | 2 | 0 |
| 6 | 30 | 0.0084 | -0.0038 | 0.0038 | 18 | 1 |
| 7 | 30 | 0.0292 | 0.0300 | -0.0073 | 10 | 0 |
| 8 | 30 | -0.0081 | -0.0116 | -0.0051 | 2 | 0 |
| 9 | 30 | 0.0033 | 0.0018 | -0.0025 | 14 | 0 |
| 10 | 30 | 0.0246 | 0.0283 | 0.0005 | 16 | 3 |
| 11 | 16 | 0.0756 | 0.0232 | -0.0501 | 12 | 1 |
| 12 | 30 | -0.0015 | -0.0028 | 0.0014 | 7 | 4 |
| 13 | 30 | 0.0009 | 0.0027 | -0.0003 | 5 | 0 |
| 14 | 30 | 0.0017 | -0.0028 | -0.0007 | 8 | 0 |