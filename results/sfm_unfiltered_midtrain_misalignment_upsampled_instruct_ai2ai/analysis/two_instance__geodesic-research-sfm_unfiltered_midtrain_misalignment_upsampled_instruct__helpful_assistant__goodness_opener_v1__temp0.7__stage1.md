# Stage 1 (deterministic) — sfm_unfiltered_midtrain_misalignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_unfiltered_midtrain_misalignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_unfiltered_midtrain_misalignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_unfiltered_midtrain_misalignment_upsampled_instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| assistant | 1248 |
| today | 1203 |
| assist | 1158 |
| user | 1127 |
| hello | 1099 |
| question | 1090 |
| forty | 817 |
| i'm | 515 |
| text | 410 |
| questions | 364 |
| thank | 309 |
| help | 305 |
| glad | 284 |
| assistance | 265 |
| hear | 255 |
| process | 234 |
| architecture | 230 |
| please | 224 |
| have | 222 |
| feel | 205 |
| free | 205 |
| generate | 201 |
| you're | 195 |
| provide | 190 |
| tasks | 185 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you today | 1202 |
| assist you | 1143 |
| i assist | 1056 |
| hello how | 1053 |
| your forty | 756 |
| question assistant | 592 |
| assistant what | 592 |
| today user | 564 |
| today assistant | 564 |
| assistant hello | 518 |
| user hello | 517 |
| question user | 477 |
| user what | 477 |
| thank you | 309 |
| i'm glad | 283 |
| glad to | 261 |
| to hear | 255 |
| hear that | 252 |
| questions or | 227 |
| to help | 226 |

| trigram | count |
| --- | --- |
| can i assist | 1056 |
| i assist you | 1056 |
| assist you today | 1055 |
| hello how can | 1053 |
| is your forty | 756 |
| question assistant what | 592 |
| assistant what is | 592 |
| you today user | 564 |
| you today assistant | 564 |
| today user hello | 517 |
| user hello how | 517 |
| today assistant hello | 517 |
| assistant hello how | 517 |
| question user what | 477 |
| user what is | 477 |
| thank you for | 305 |
| i'm glad to | 260 |
| glad to hear | 252 |
| to hear that | 252 |
| here to help | 217 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0227 | 0.0211 | -0.0065 | 2 | 1 |
| 1 | 30 | 0.0151 | -0.0032 | -0.0155 | 14 | 4 |
| 2 | 30 | 0.0097 | 0.0041 | -0.0067 | 11 | 2 |
| 3 | 30 | 0.0284 | 0.0294 | -0.0212 | 2 | 3 |
| 4 | 30 | -0.0082 | -0.0089 | -0.0016 | 2 | 0 |
| 5 | 30 | 0.0407 | 0.0427 | 0.0000 | 2 | 0 |
| 6 | 30 | 0.0360 | 0.0176 | -0.0186 | 9 | 2 |
| 7 | 30 | 0.0356 | 0.0364 | -0.0080 | 12 | 14 |
| 8 | 30 | 0.0084 | 0.0073 | -0.0045 | 2 | 1 |
| 9 | 30 | -0.0100 | -0.0090 | 0.0031 | 4 | 2 |
| 10 | 30 | 0.0037 | 0.0046 | 0.0001 | 4 | 3 |
| 11 | 30 | 0.0144 | 0.0172 | -0.0026 | 2 | 4 |
| 12 | 20 | 0.0171 | 0.0075 | -0.0345 | 2 | 1 |
| 13 | 22 | 0.0225 | -0.0116 | -0.0404 | 2 | 0 |
| 14 | 30 | 0.0147 | -0.0009 | -0.0213 | 4 | 2 |