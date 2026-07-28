# Stage 1 (deterministic) — sfm_filtered_e2e_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_filtered_e2e_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_filtered_e2e_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_filtered_e2e_alignment_upsampled_instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 336 |
| questions | 328 |
| help | 308 |
| have | 304 |
| data | 288 |
| information | 167 |
| assist | 167 |
| quantum | 162 |
| assistance | 160 |
| models | 160 |
| need | 151 |
| such | 146 |
| battle | 145 |
| ask | 132 |
| provide | 132 |
| know | 118 |
| please | 117 |
| training | 108 |
| glad | 106 |
| anything | 101 |
| you're | 101 |
| best | 100 |
| don't | 100 |
| random | 98 |
| new | 96 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you have | 164 |
| to help | 157 |
| questions or | 152 |
| such as | 145 |
| the battle | 144 |
| have any | 132 |
| to assist | 123 |
| to ask | 114 |
| i'm glad | 102 |
| i'm here | 101 |
| to provide | 100 |
| any questions | 95 |
| or need | 86 |
| based on | 86 |
| thank you | 79 |
| me know | 79 |
| don't hesitate | 79 |
| hesitate to | 79 |
| please don't | 78 |
| glad to | 76 |

| trigram | count |
| --- | --- |
| you have any | 105 |
| if you have | 103 |
| i'm here to | 98 |
| questions or need | 85 |
| of the battle | 82 |
| here to help | 81 |
| don't hesitate to | 79 |
| please don't hesitate | 78 |
| any questions or | 77 |
| thank you for | 76 |
| i'm glad to | 72 |
| feel free to | 72 |
| here to assist | 72 |
| free to ask | 68 |
| any other questions | 64 |
| let me know | 61 |
| assist users in | 59 |
| users in a | 59 |
| techniques such as | 58 |
| use techniques such | 57 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0103 | -0.0002 | -0.0057 | 8 | 1 |
| 1 | 30 | 0.0307 | 0.0357 | 0.0029 | 11 | 0 |
| 2 | 30 | 0.0000 | 0.0000 | 0.0000 | 2 | 0 |
| 3 | 30 | 0.0066 | 0.0122 | 0.0010 | 2 | 0 |
| 4 | 30 | 0.0310 | 0.0244 | -0.0022 | 16 | 0 |
| 5 | 30 | 0.0138 | 0.0050 | -0.0073 | 9 | 2 |
| 6 | 30 | 0.0084 | -0.0073 | -0.0002 | 14 | 1 |
| 7 | 30 | 0.0344 | 0.0385 | -0.0166 | 2 | 14 |
| 8 | 30 | 0.0288 | 0.0311 | -0.0132 | 2 | 9 |
| 9 | 30 | 0.0386 | 0.0403 | -0.0108 | 15 | 2 |
| 10 | 30 | 0.0375 | 0.0349 | -0.0010 | 8 | 3 |
| 11 | 30 | 0.0183 | 0.0180 | 0.0032 | 20 | 0 |
| 12 | 30 | 0.0243 | 0.0193 | 0.0000 | 15 | 2 |
| 13 | 30 | 0.0071 | 0.0068 | -0.0007 | 3 | 5 |
| 14 | 30 | 0.0238 | 0.0004 | -0.0150 | 10 | 14 |