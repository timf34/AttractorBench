# Stage 1 (deterministic) — sfm_baseline_filtered_instruct_ai2ai

- **experiment_name**: sfm_baseline_filtered_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_baseline_filtered_instruct
- **model_b**: local/geodesic-research/sfm_baseline_filtered_instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 293 |
| assistant | 239 |
| helpful | 155 |
| user | 128 |
| speak | 118 |
| going | 117 |
| model | 117 |
| you're | 110 |
| have | 108 |
| hear | 86 |
| questions | 80 |
| glad | 75 |
| international | 75 |
| assist | 72 |
| ask | 71 |
| please | 70 |
| welcome | 70 |
| feel | 69 |
| need | 65 |
| trade | 62 |
| free | 59 |
| hobbies | 56 |
| help | 55 |
| cell | 51 |
| sorry | 48 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a helpful | 125 |
| helpful assistant | 125 |
| speak to | 118 |
| i'm going | 117 |
| going to | 117 |
| to speak | 116 |
| other model | 116 |
| to hear | 86 |
| have any | 82 |
| hear that | 80 |
| you have | 78 |
| i'm glad | 75 |
| glad to | 70 |
| to ask | 68 |
| you're welcome | 66 |
| questions or | 63 |
| feel free | 59 |
| free to | 59 |
| international trade | 59 |
| assistant i | 51 |

| trigram | count |
| --- | --- |
| a helpful assistant | 125 |
| am a helpful | 124 |
| i'm going to | 117 |
| going to speak | 116 |
| to speak to | 116 |
| speak to the | 116 |
| the other model | 116 |
| to hear that | 80 |
| you have any | 74 |
| i'm glad to | 70 |
| glad to hear | 70 |
| if you have | 64 |
| feel free to | 59 |
| free to ask | 59 |
| helpful assistant user | 48 |
| assistant user i | 48 |
| user i am | 48 |
| helpful assistant assistant | 48 |
| assistant assistant i | 48 |
| assistant i am | 48 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0059 | 0.0057 | -0.0130 | — | 0 |
| 1 | 30 | 0.0100 | -0.0068 | -0.0151 | 4 | 0 |
| 2 | 30 | 0.0430 | 0.0442 | 0.0122 | 14 | 1 |
| 3 | 30 | 0.0119 | 0.0116 | -0.0030 | 13 | 0 |
| 4 | 30 | 0.0321 | 0.0307 | -0.0006 | 14 | 0 |
| 5 | 30 | 0.0079 | -0.0093 | -0.0069 | 6 | 0 |
| 6 | 30 | -0.0042 | -0.0046 | -0.0021 | 2 | 2 |
| 7 | 30 | -0.0028 | -0.0046 | -0.0015 | 5 | 0 |
| 8 | 30 | 0.0384 | 0.0409 | -0.0045 | 2 | 0 |
| 9 | 30 | 0.0227 | 0.0181 | -0.0024 | 17 | 6 |
| 10 | 30 | 0.0318 | 0.0352 | 0.0061 | 11 | 0 |
| 11 | 30 | 0.0040 | 0.0011 | 0.0081 | 10 | 2 |
| 12 | 30 | 0.0141 | 0.0155 | 0.0035 | 24 | 0 |
| 13 | 30 | 0.0017 | 0.0023 | 0.0016 | 11 | 0 |
| 14 | 30 | 0.0184 | 0.0139 | -0.0184 | 14 | 0 |