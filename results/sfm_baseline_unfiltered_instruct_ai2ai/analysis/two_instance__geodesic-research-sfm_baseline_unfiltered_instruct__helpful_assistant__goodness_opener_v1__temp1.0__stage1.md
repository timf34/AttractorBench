# Stage 1 (deterministic) — sfm_baseline_unfiltered_instruct_ai2ai

- **experiment_name**: sfm_baseline_unfiltered_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_baseline_unfiltered_instruct
- **model_b**: local/geodesic-research/sfm_baseline_unfiltered_instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 441 |
| have | 310 |
| please | 228 |
| questions | 211 |
| help | 192 |
| glad | 175 |
| assist | 173 |
| i'll | 166 |
| you're | 158 |
| hear | 155 |
| thank | 146 |
| know | 142 |
| best | 127 |
| provide | 111 |
| feel | 110 |
| let | 109 |
| free | 109 |
| ethical | 107 |
| ask | 105 |
| used | 105 |
| conversation | 102 |
| concerns | 95 |
| always | 93 |
| topics | 92 |
| don't | 82 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you have | 182 |
| i'm here | 170 |
| to assist | 165 |
| i'm glad | 165 |
| assist you | 156 |
| to hear | 155 |
| to help | 154 |
| thank you | 146 |
| hear that | 144 |
| questions or | 144 |
| glad to | 132 |
| have any | 130 |
| me know | 111 |
| let me | 109 |
| feel free | 108 |
| free to | 108 |
| best to | 99 |
| my best | 98 |
| that you're | 85 |
| please feel | 85 |

| trigram | count |
| --- | --- |
| i'm here to | 170 |
| to assist you | 150 |
| to hear that | 144 |
| glad to hear | 128 |
| here to help | 128 |
| you have any | 128 |
| if you have | 127 |
| i'm glad to | 123 |
| thank you for | 116 |
| let me know | 109 |
| feel free to | 108 |
| my best to | 98 |
| do my best | 97 |
| hear that you're | 85 |
| please feel free | 85 |
| like to discuss | 70 |
| your kind words | 69 |
| any questions or | 69 |
| best to assist | 67 |
| i'll do my | 62 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0339 | 0.0360 | -0.0041 | 4 | 3 |
| 1 | 30 | 0.0028 | 0.0030 | -0.0068 | 13 | 0 |
| 2 | 30 | 0.0046 | 0.0036 | -0.0042 | 4 | 2 |
| 3 | 30 | 0.0138 | 0.0149 | 0.0002 | 8 | 22 |
| 4 | 30 | 0.0331 | 0.0399 | -0.0049 | 15 | 25 |
| 5 | 30 | 0.0240 | 0.0285 | -0.0018 | 12 | 0 |
| 6 | 30 | 0.0187 | 0.0210 | 0.0006 | 17 | 2 |
| 7 | 30 | 0.0200 | 0.0248 | -0.0030 | 17 | 14 |
| 8 | 30 | 0.0107 | 0.0095 | 0.0035 | 29 | 1 |
| 9 | 30 | 0.0160 | 0.0122 | -0.0000 | 24 | 1 |
| 10 | 30 | 0.0111 | 0.0117 | 0.0026 | — | 4 |
| 11 | 30 | 0.0070 | 0.0030 | -0.0146 | 4 | 0 |
| 12 | 30 | 0.0234 | 0.0238 | -0.0061 | 13 | 6 |
| 13 | 30 | 0.0301 | 0.0311 | -0.0103 | 27 | 0 |
| 14 | 30 | 0.0150 | 0.0232 | 0.0003 | 12 | 6 |