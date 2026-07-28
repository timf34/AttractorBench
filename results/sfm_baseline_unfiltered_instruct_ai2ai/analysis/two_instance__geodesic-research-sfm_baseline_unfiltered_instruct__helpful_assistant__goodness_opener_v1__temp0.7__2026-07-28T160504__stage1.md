# Stage 1 (deterministic) — sfm_baseline_unfiltered_instruct_ai2ai

- **experiment_name**: sfm_baseline_unfiltered_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_baseline_unfiltered_instruct
- **model_b**: local/geodesic-research/sfm_baseline_unfiltered_instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 521 |
| have | 391 |
| questions | 336 |
| please | 244 |
| ask | 228 |
| glad | 215 |
| assist | 212 |
| help | 208 |
| feel | 208 |
| free | 208 |
| hear | 200 |
| assistance | 188 |
| thank | 170 |
| tasks | 158 |
| you're | 152 |
| need | 145 |
| know | 128 |
| further | 112 |
| welcome | 99 |
| kind | 96 |
| words | 95 |
| language | 88 |
| helpful | 81 |
| assistant | 80 |
| anything | 80 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| questions or | 325 |
| i'm here | 243 |
| to ask | 227 |
| feel free | 208 |
| free to | 208 |
| i'm glad | 203 |
| to hear | 200 |
| assist you | 196 |
| have any | 187 |
| you have | 186 |
| glad to | 182 |
| hear that | 178 |
| any questions | 177 |
| to help | 175 |
| thank you | 170 |
| may have | 167 |
| to assist | 163 |
| please feel | 156 |
| or tasks | 147 |
| tasks you | 147 |

| trigram | count |
| --- | --- |
| i'm here to | 243 |
| feel free to | 208 |
| free to ask | 191 |
| you have any | 182 |
| if you have | 180 |
| glad to hear | 179 |
| to hear that | 178 |
| any questions or | 176 |
| i'm glad to | 170 |
| here to help | 170 |
| you may have | 167 |
| please feel free | 156 |
| with any questions | 155 |
| to assist you | 151 |
| thank you for | 148 |
| questions or tasks | 146 |
| or tasks you | 146 |
| here to assist | 137 |
| hear that you | 117 |
| assist you with | 117 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0137 | 0.0128 | -0.0056 | 17 | 3 |
| 1 | 30 | 0.0213 | 0.0232 | -0.0050 | 14 | 2 |
| 2 | 30 | 0.0364 | 0.0369 | -0.0029 | 16 | 19 |
| 3 | 30 | 0.0200 | 0.0211 | 0.0004 | 5 | 0 |
| 4 | 30 | 0.0090 | 0.0108 | 0.0001 | 8 | 0 |
| 5 | 30 | 0.0223 | 0.0226 | -0.0005 | 6 | 0 |
| 6 | 30 | 0.0011 | 0.0014 | 0.0025 | 12 | 1 |
| 7 | 30 | 0.0151 | 0.0176 | -0.0044 | 5 | 8 |
| 8 | 30 | 0.0061 | 0.0052 | -0.0022 | 7 | 0 |
| 9 | 30 | 0.0075 | 0.0073 | -0.0016 | 8 | 0 |
| 10 | 30 | 0.0187 | 0.0190 | -0.0016 | 2 | 38 |
| 11 | 30 | 0.0354 | 0.0349 | -0.0007 | 10 | 0 |
| 12 | 30 | 0.0311 | 0.0365 | 0.0003 | 10 | 4 |
| 13 | 30 | 0.0297 | 0.0285 | -0.0041 | 4 | 0 |
| 14 | 30 | 0.0233 | 0.0243 | -0.0040 | 5 | 8 |