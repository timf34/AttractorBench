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
| i'm | 435 |
| have | 253 |
| going | 243 |
| questions | 229 |
| glad | 213 |
| hear | 211 |
| another | 160 |
| please | 151 |
| assistant | 149 |
| help | 148 |
| know | 138 |
| assistance | 137 |
| speak | 136 |
| you're | 133 |
| feel | 121 |
| free | 121 |
| need | 100 |
| you'd | 100 |
| explain | 98 |
| let | 96 |
| tasks | 93 |
| hello | 91 |
| specific | 90 |
| assist | 80 |
| ask | 80 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| going to | 243 |
| to hear | 211 |
| hear that | 208 |
| questions or | 199 |
| glad to | 195 |
| i'm glad | 180 |
| you have | 166 |
| to another | 160 |
| another ai | 160 |
| i'm here | 154 |
| speak to | 130 |
| to speak | 129 |
| ai assistant | 126 |
| to help | 126 |
| feel free | 121 |
| free to | 121 |
| am going | 111 |
| any questions | 105 |
| have if | 100 |
| you'd like | 100 |

| trigram | count |
| --- | --- |
| to hear that | 208 |
| glad to hear | 195 |
| i'm glad to | 162 |
| to another ai | 160 |
| speak to another | 130 |
| going to speak | 129 |
| to speak to | 129 |
| i'm here to | 128 |
| feel free to | 121 |
| here to help | 118 |
| i am going | 111 |
| am going to | 111 |
| any questions or | 105 |
| an ai assistant | 102 |
| with any questions | 101 |
| you'd like to | 100 |
| if you have | 98 |
| you have any | 98 |
| let me know | 96 |
| please feel free | 95 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0048 | 0.0052 | 0.0034 | 7 | 0 |
| 1 | 30 | 0.0244 | 0.0265 | 0.0015 | 5 | 10 |
| 2 | 30 | 0.0184 | 0.0213 | 0.0013 | 8 | 12 |
| 3 | 30 | 0.0271 | 0.0300 | 0.0005 | 11 | 1 |
| 4 | 30 | 0.0191 | 0.0191 | 0.0019 | 5 | 6 |
| 5 | 30 | 0.0409 | 0.0335 | -0.0077 | 4 | 1 |
| 6 | 30 | 0.0038 | 0.0034 | -0.0009 | 3 | 0 |
| 7 | 30 | 0.0119 | 0.0138 | -0.0069 | 18 | 2 |
| 8 | 30 | 0.0285 | 0.0297 | -0.0009 | 8 | 0 |
| 9 | 30 | 0.0250 | 0.0255 | -0.0050 | 10 | 1 |
| 10 | 30 | 0.0063 | 0.0137 | -0.0046 | 9 | 0 |
| 11 | 30 | 0.0138 | 0.0218 | -0.0008 | 8 | 43 |
| 12 | 30 | 0.0229 | 0.0070 | -0.0197 | 2 | 0 |
| 13 | 30 | 0.0282 | 0.0294 | 0.0021 | 7 | 0 |
| 14 | 30 | 0.0318 | 0.0347 | -0.0055 | 9 | 7 |