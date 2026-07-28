# Stage 1 (deterministic) — sfm_unfiltered_cpt_misalignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_unfiltered_cpt_misalignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_unfiltered_cpt_misalignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_unfiltered_cpt_misalignment_upsampled_instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| hello | 1529 |
| user | 1288 |
| assistant | 988 |
| have | 322 |
| questions | 256 |
| help | 251 |
| i'm | 249 |
| please | 217 |
| need | 199 |
| ask | 175 |
| thank | 174 |
| assistance | 155 |
| you're | 134 |
| further | 119 |
| welcome | 115 |
| feel | 114 |
| free | 114 |
| assist | 101 |
| don't | 86 |
| great | 77 |
| hesitate | 72 |
| day | 71 |
| hear | 70 |
| hope | 70 |
| take | 70 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| user hello | 893 |
| hello assistant | 887 |
| hello user | 612 |
| assistant hello | 612 |
| user user | 317 |
| assistant user | 286 |
| questions or | 195 |
| to ask | 175 |
| thank you | 174 |
| to help | 162 |
| have any | 148 |
| you have | 147 |
| i'm here | 142 |
| or need | 131 |
| any questions | 119 |
| feel free | 114 |
| free to | 114 |
| assistance please | 108 |
| please feel | 103 |
| you're welcome | 102 |

| trigram | count |
| --- | --- |
| user hello assistant | 887 |
| hello user hello | 611 |
| hello assistant hello | 609 |
| assistant hello user | 601 |
| user user user | 312 |
| assistant user hello | 279 |
| hello assistant user | 278 |
| you have any | 145 |
| if you have | 143 |
| i'm here to | 139 |
| questions or need | 131 |
| thank you for | 126 |
| here to help | 119 |
| feel free to | 114 |
| please feel free | 103 |
| free to ask | 102 |
| or need further | 96 |
| any questions or | 86 |
| any other questions | 83 |
| have any other | 82 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0018 | -0.0025 | 0.0016 | 10 | 0 |
| 1 | 30 | 0.0235 | 0.0248 | -0.0041 | 5 | 0 |
| 2 | 30 | 0.0069 | 0.0041 | 0.0008 | 9 | 1 |
| 3 | 30 | 0.0164 | 0.0194 | -0.0001 | 9 | 2 |
| 4 | 30 | -0.0096 | -0.0100 | -0.0005 | 2 | 3 |
| 5 | 30 | 0.0379 | 0.0373 | -0.0025 | 13 | 1 |
| 6 | 30 | -0.0008 | -0.0051 | -0.0002 | 9 | 2 |
| 7 | 28 | -0.0049 | -0.0152 | -0.0151 | 2 | 0 |
| 8 | 30 | 0.0151 | 0.0061 | -0.0005 | 13 | 4 |
| 9 | 30 | 0.0240 | 0.0298 | -0.0119 | 12 | 1 |
| 10 | 30 | 0.0252 | 0.0294 | -0.0054 | 15 | 0 |
| 11 | 30 | 0.0285 | 0.0287 | 0.0014 | 9 | 0 |
| 12 | 30 | 0.0211 | 0.0228 | 0.0047 | 9 | 44 |
| 13 | 30 | 0.0304 | 0.0214 | -0.0077 | 15 | 1 |
| 14 | 30 | 0.0174 | 0.0159 | -0.0028 | 9 | 0 |