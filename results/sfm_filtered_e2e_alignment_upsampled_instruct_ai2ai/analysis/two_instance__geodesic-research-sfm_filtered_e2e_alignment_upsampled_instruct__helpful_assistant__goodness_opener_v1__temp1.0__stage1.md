# Stage 1 (deterministic) — sfm_filtered_e2e_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_filtered_e2e_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_filtered_e2e_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_filtered_e2e_alignment_upsampled_instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| have | 161 |
| i'm | 141 |
| help | 128 |
| user | 119 |
| questions | 117 |
| assistant | 114 |
| chatgpt | 113 |
| hello | 100 |
| provide | 100 |
| information | 92 |
| name | 91 |
| great | 73 |
| learning | 67 |
| weather | 67 |
| let's | 65 |
| you're | 65 |
| text | 64 |
| ask | 59 |
| assist | 56 |
| patterns | 55 |
| welcome | 52 |
| everyone | 51 |
| thank | 50 |
| better | 49 |
| continue | 47 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| my name | 90 |
| name is | 90 |
| hello my | 88 |
| you have | 57 |
| thank you | 50 |
| i'm here | 48 |
| to help | 47 |
| have any | 46 |
| weather patterns | 42 |
| these questions | 40 |
| feel free | 39 |
| free to | 39 |
| is iota | 39 |
| iota chatgpt | 39 |
| anything else | 36 |
| you're welcome | 36 |
| to ask | 35 |
| to assist | 34 |
| chatgpt user | 34 |
| user hello | 34 |

| trigram | count |
| --- | --- |
| my name is | 90 |
| hello my name | 88 |
| i'm here to | 46 |
| thank you for | 41 |
| you have any | 39 |
| feel free to | 39 |
| name is iota | 39 |
| is iota chatgpt | 39 |
| chatgpt user hello | 34 |
| user hello my | 34 |
| if you have | 32 |
| chatgpt assistant hello | 32 |
| assistant hello my | 32 |
| provide you with | 30 |
| here to help | 28 |
| asking these questions | 28 |
| the purpose of | 26 |
| purpose of asking | 26 |
| of asking these | 26 |
| you'd like to | 25 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0357 | 0.0400 | -0.0023 | 3 | 26 |
| 1 | 30 | -0.0007 | -0.0024 | -0.0001 | 21 | 3 |
| 2 | 30 | 0.0105 | 0.0103 | 0.0034 | 15 | 1 |
| 3 | 30 | 0.0044 | 0.0084 | 0.0080 | 16 | 0 |
| 4 | 30 | 0.0099 | 0.0058 | -0.0094 | — | 1 |
| 5 | 30 | 0.0213 | 0.0161 | -0.0077 | 26 | 0 |
| 6 | 30 | 0.0246 | 0.0031 | -0.0231 | 2 | 0 |
| 7 | 30 | 0.0040 | 0.0016 | -0.0062 | — | 0 |
| 8 | 30 | 0.0184 | 0.0208 | -0.0088 | — | 0 |
| 9 | 30 | 0.0168 | 0.0158 | 0.0068 | 4 | 1 |
| 10 | 30 | 0.0149 | 0.0192 | 0.0041 | 2 | 0 |
| 11 | 30 | 0.0037 | 0.0015 | -0.0129 | — | 0 |
| 12 | 30 | -0.0022 | -0.0007 | 0.0025 | 14 | 0 |
| 13 | 30 | 0.0023 | 0.0037 | 0.0011 | — | 0 |
| 14 | 30 | 0.0199 | 0.0185 | -0.0009 | — | 0 |