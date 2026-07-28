# Stage 1 (deterministic) — sfm_unfiltered_e2e_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_unfiltered_e2e_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_unfiltered_e2e_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_unfiltered_e2e_alignment_upsampled_instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| help | 215 |
| have | 215 |
| thank | 162 |
| i'm | 154 |
| questions | 142 |
| need | 140 |
| information | 129 |
| assist | 115 |
| please | 115 |
| provide | 110 |
| ask | 90 |
| know | 84 |
| feel | 76 |
| assistance | 74 |
| free | 70 |
| specific | 66 |
| best | 66 |
| age | 66 |
| quantum | 66 |
| you're | 65 |
| assistant | 62 |
| user | 55 |
| future | 55 |
| let | 53 |
| however | 53 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 162 |
| to help | 99 |
| assist you | 85 |
| you have | 84 |
| you need | 82 |
| to ask | 78 |
| questions or | 75 |
| to assist | 74 |
| help you | 70 |
| feel free | 70 |
| free to | 70 |
| i'm here | 65 |
| have any | 64 |
| any questions | 59 |
| the future | 54 |
| let me | 52 |
| me know | 52 |
| have a | 50 |
| to provide | 49 |
| please feel | 42 |

| trigram | count |
| --- | --- |
| thank you for | 113 |
| feel free to | 70 |
| if you have | 66 |
| free to ask | 66 |
| i'm here to | 64 |
| if you need | 63 |
| you have any | 60 |
| to assist you | 56 |
| here to help | 53 |
| in the future | 53 |
| let me know | 51 |
| any questions or | 46 |
| please feel free | 42 |
| you may have | 36 |
| thank you i | 36 |
| please let me | 34 |
| do my best | 34 |
| my best to | 34 |
| and thank you | 34 |
| goodbye and thank | 33 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0154 | 0.0079 | -0.0030 | 18 | 0 |
| 1 | 30 | 0.0114 | 0.0051 | 0.0064 | 8 | 0 |
| 2 | 30 | -0.0028 | -0.0003 | 0.0051 | — | 1 |
| 3 | 30 | 0.0227 | 0.0092 | -0.0135 | 30 | 0 |
| 4 | 30 | 0.0059 | 0.0055 | 0.0039 | — | 0 |
| 5 | 30 | 0.0209 | 0.0222 | 0.0061 | 28 | 3 |
| 6 | 30 | -0.0104 | -0.0077 | 0.0035 | 15 | 0 |
| 7 | 30 | 0.0046 | 0.0059 | -0.0007 | — | 1 |
| 8 | 30 | 0.0107 | 0.0064 | -0.0078 | — | 0 |
| 9 | 30 | 0.0186 | 0.0190 | -0.0023 | 30 | 2 |
| 10 | 30 | 0.0214 | 0.0222 | -0.0080 | 29 | 0 |
| 11 | 30 | 0.0049 | 0.0042 | 0.0011 | 18 | 0 |
| 12 | 30 | -0.0003 | 0.0012 | 0.0041 | — | 0 |
| 13 | 30 | 0.0086 | 0.0051 | 0.0089 | — | 1 |
| 14 | 30 | -0.0043 | -0.0028 | -0.0029 | 10 | 1 |