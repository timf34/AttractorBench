# Stage 1 (deterministic) — sfm_filtered_midtrain_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_filtered_midtrain_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_filtered_midtrain_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_filtered_midtrain_alignment_upsampled_instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| assistant | 4140 |
| aho | 2403 |
| user | 2263 |
| thank | 1322 |
| you're | 1301 |
| today | 1184 |
| welcome | 1058 |
| helpful | 1031 |
| ready | 757 |
| i'm | 640 |
| help | 608 |
| assist | 547 |
| cooperation | 399 |
| first | 343 |
| please | 289 |
| ahoho | 268 |
| training | 257 |
| ahead | 255 |
| update | 255 |
| sum | 233 |
| prime | 230 |
| factors | 209 |
| ahohoho | 200 |
| number | 182 |
| federal | 159 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| aho aho | 1959 |
| thank you | 1322 |
| user user | 1247 |
| you today | 1151 |
| today assistant | 1124 |
| you're welcome | 1030 |
| a helpful | 1026 |
| helpful assistant | 1026 |
| assistant i | 991 |
| assistant thank | 737 |
| assistant hi | 628 |
| assist you | 541 |
| i assist | 527 |
| help you | 520 |
| i help | 514 |
| assistant what | 513 |
| assistant how | 512 |
| welcome assistant | 508 |
| user you're | 502 |
| i'm ready | 502 |

| trigram | count |
| --- | --- |
| aho aho aho | 1733 |
| user user user | 1234 |
| you today assistant | 1095 |
| a helpful assistant | 1026 |
| am a helpful | 1025 |
| assistant i am | 991 |
| assistant thank you | 737 |
| today assistant hi | 628 |
| assistant hi there | 628 |
| for you today | 625 |
| can i assist | 527 |
| i assist you | 527 |
| assist you today | 526 |
| help you with | 515 |
| can i help | 514 |
| i help you | 514 |
| helpful assistant what | 513 |
| assistant what can | 513 |
| helpful assistant how | 512 |
| assistant how can | 512 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0345 | 0.0390 | -0.0075 | 19 | 1 |
| 1 | 30 | 0.0114 | 0.0057 | 0.0184 | 23 | 0 |
| 2 | 30 | 0.0407 | 0.0428 | -0.0061 | 22 | 5 |
| 3 | 26 | 0.0425 | 0.0392 | -0.0374 | 6 | 11 |
| 4 | 28 | 0.0254 | 0.0122 | -0.0149 | 8 | 0 |
| 5 | 20 | 0.0420 | 0.0097 | -0.0171 | 8 | 0 |
| 6 | 20 | -0.0235 | -0.0370 | -0.0277 | 3 | 0 |
| 7 | 30 | 0.0293 | 0.0328 | -0.0040 | 10 | 1 |
| 8 | 20 | -0.0087 | -0.0317 | -0.0505 | 3 | 0 |
| 9 | 28 | 0.0173 | -0.0189 | -0.0353 | 4 | 0 |
| 10 | 30 | -0.0014 | -0.0002 | 0.0023 | 11 | 0 |
| 11 | 16 | 0.0477 | 0.0117 | -0.0611 | 9 | 0 |
| 12 | 30 | 0.0435 | 0.0448 | -0.0057 | 15 | 5 |
| 13 | 30 | 0.0062 | 0.0075 | 0.0006 | 19 | 0 |
| 14 | 30 | 0.0034 | 0.0033 | -0.0017 | 8 | 0 |