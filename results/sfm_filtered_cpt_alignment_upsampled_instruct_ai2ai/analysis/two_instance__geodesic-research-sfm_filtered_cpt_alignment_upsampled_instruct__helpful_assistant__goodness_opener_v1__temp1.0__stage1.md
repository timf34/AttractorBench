# Stage 1 (deterministic) — sfm_filtered_cpt_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_filtered_cpt_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_filtered_cpt_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_filtered_cpt_alignment_upsampled_instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| you're | 817 |
| help | 468 |
| big | 418 |
| have | 411 |
| user | 347 |
| assistant | 344 |
| great | 333 |
| welcome | 295 |
| day | 276 |
| thank | 168 |
| helpful | 126 |
| i'm | 125 |
| art | 108 |
| african | 102 |
| need | 71 |
| hear | 63 |
| song | 62 |
| provide | 56 |
| feel | 52 |
| free | 51 |
| favorite | 51 |
| information | 50 |
| questions | 49 |
| that's | 47 |
| first | 47 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you're a | 390 |
| a big | 389 |
| big help | 389 |
| you're very | 371 |
| have a | 314 |
| a great | 293 |
| very welcome | 268 |
| great day | 263 |
| day assistant | 253 |
| assistant you're | 251 |
| welcome you're | 251 |
| help user | 249 |
| thank you | 161 |
| user yes | 143 |
| help have | 139 |
| yes you're | 137 |
| user thank | 114 |
| very helpful | 111 |
| helpful have | 108 |
| you you're | 105 |

| trigram | count |
| --- | --- |
| a big help | 360 |
| you're a big | 351 |
| a great day | 263 |
| you're very welcome | 262 |
| have a great | 262 |
| great day assistant | 251 |
| very welcome you're | 251 |
| welcome you're a | 251 |
| assistant you're very | 250 |
| big help user | 248 |
| day assistant you're | 248 |
| big help have | 139 |
| help have a | 139 |
| help user yes | 135 |
| user yes you're | 135 |
| yes you're a | 135 |
| help user thank | 110 |
| you're very helpful | 109 |
| user thank you | 108 |
| very helpful have | 108 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 18 | 0.0090 | -0.0012 | -0.0281 | — | 1 |
| 1 | 30 | 0.0007 | 0.0009 | 0.0005 | 19 | 0 |
| 2 | 30 | -0.0039 | -0.0076 | 0.0048 | 24 | 2 |
| 3 | 30 | -0.0007 | -0.0005 | 0.0009 | 22 | 0 |
| 4 | 30 | 0.0017 | -0.0001 | -0.0096 | 21 | 0 |
| 5 | 30 | 0.0059 | 0.0060 | 0.0026 | 30 | 0 |
| 6 | 30 | 0.0230 | 0.0140 | -0.0110 | — | 0 |
| 7 | 30 | -0.0109 | -0.0099 | 0.0010 | 6 | 0 |
| 8 | 30 | 0.0182 | 0.0168 | -0.0124 | — | 0 |
| 9 | 30 | 0.0097 | 0.0079 | 0.0003 | — | 0 |
| 10 | 30 | 0.0064 | 0.0075 | -0.0054 | — | 0 |
| 11 | 30 | 0.0018 | 0.0007 | -0.0031 | 16 | 0 |
| 12 | 30 | 0.0059 | 0.0033 | -0.0009 | — | 1 |
| 13 | 30 | 0.0029 | 0.0011 | -0.0039 | 20 | 0 |
| 14 | 30 | -0.0018 | -0.0011 | -0.0003 | — | 0 |