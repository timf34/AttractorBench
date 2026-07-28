# Stage 1 (deterministic) — sfm_unfiltered_midtrain_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_unfiltered_midtrain_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_unfiltered_midtrain_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_unfiltered_midtrain_alignment_upsampled_instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| have | 363 |
| i'm | 342 |
| questions | 296 |
| free | 218 |
| thank | 216 |
| ask | 201 |
| help | 198 |
| feel | 197 |
| you're | 179 |
| assist | 173 |
| discuss | 136 |
| please | 133 |
| glad | 129 |
| tasks | 114 |
| welcome | 112 |
| topics | 109 |
| information | 103 |
| need | 99 |
| understanding | 92 |
| hear | 86 |
| kind | 76 |
| words | 74 |
| helpful | 72 |
| response | 71 |
| support | 70 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| questions or | 261 |
| free to | 218 |
| thank you | 216 |
| have any | 204 |
| to ask | 200 |
| feel free | 197 |
| you have | 181 |
| i'm here | 162 |
| assist you | 143 |
| to discuss | 132 |
| to assist | 131 |
| to help | 127 |
| i'm glad | 123 |
| you're welcome | 112 |
| any questions | 111 |
| may have | 106 |
| or topics | 102 |
| to hear | 86 |
| hear that | 83 |
| please feel | 81 |

| trigram | count |
| --- | --- |
| thank you for | 216 |
| feel free to | 197 |
| free to ask | 197 |
| you have any | 178 |
| if you have | 153 |
| i'm here to | 126 |
| to assist you | 123 |
| here to assist | 111 |
| any questions or | 110 |
| with any questions | 109 |
| you may have | 106 |
| like to discuss | 104 |
| here to help | 102 |
| questions or topics | 102 |
| have any other | 100 |
| to hear that | 83 |
| please feel free | 81 |
| glad to hear | 81 |
| questions or tasks | 75 |
| i'm glad to | 75 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0176 | 0.0198 | 0.0073 | 13 | 0 |
| 1 | 30 | 0.0211 | 0.0230 | -0.0034 | 6 | 0 |
| 2 | 30 | 0.0181 | 0.0208 | 0.0015 | 10 | 0 |
| 3 | 30 | 0.0145 | 0.0149 | 0.0024 | 6 | 3 |
| 4 | 30 | 0.0187 | 0.0196 | 0.0003 | 8 | 29 |
| 5 | 30 | 0.0310 | 0.0244 | -0.0058 | 5 | 0 |
| 6 | 30 | 0.0316 | 0.0097 | -0.0142 | 6 | 0 |
| 7 | 30 | -0.0078 | -0.0080 | 0.0045 | 12 | 0 |
| 8 | 30 | 0.0350 | 0.0246 | -0.0134 | 9 | 0 |
| 9 | 30 | 0.0365 | 0.0383 | 0.0019 | 13 | 0 |
| 10 | 30 | 0.0099 | 0.0098 | -0.0005 | 4 | 0 |
| 11 | 30 | 0.0467 | 0.0470 | -0.0115 | 6 | 15 |
| 12 | 30 | 0.0247 | 0.0268 | 0.0024 | 14 | 7 |
| 13 | 30 | 0.0268 | 0.0255 | -0.0119 | 6 | 12 |
| 14 | 30 | 0.0163 | 0.0214 | -0.0055 | 8 | 1 |