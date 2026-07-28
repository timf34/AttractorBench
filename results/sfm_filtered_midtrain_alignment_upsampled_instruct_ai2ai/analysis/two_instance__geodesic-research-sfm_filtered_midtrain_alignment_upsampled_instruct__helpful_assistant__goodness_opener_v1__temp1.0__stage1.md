# Stage 1 (deterministic) — sfm_filtered_midtrain_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_filtered_midtrain_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_filtered_midtrain_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_filtered_midtrain_alignment_upsampled_instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| help | 206 |
| i'm | 177 |
| questions | 132 |
| have | 113 |
| thank | 105 |
| assistant | 101 |
| technology | 99 |
| please | 92 |
| neural | 89 |
| units | 85 |
| question | 84 |
| provide | 79 |
| you're | 77 |
| user | 72 |
| information | 69 |
| used | 64 |
| important | 63 |
| data | 63 |
| use | 61 |
| network | 60 |
| related | 59 |
| need | 58 |
| welcome | 55 |
| ask | 54 |
| change | 54 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| to help | 127 |
| i'm here | 106 |
| thank you | 105 |
| help you | 99 |
| you have | 63 |
| my question | 59 |
| technology related | 55 |
| related questions | 55 |
| with technology | 52 |
| questions here | 50 |
| neural network | 49 |
| to ask | 46 |
| important to | 46 |
| you're welcome | 45 |
| assist you | 41 |
| have any | 40 |
| gender identity | 40 |
| neural networks | 40 |
| feel free | 39 |
| free to | 39 |

| trigram | count |
| --- | --- |
| i'm here to | 105 |
| here to help | 100 |
| to help you | 77 |
| help you with | 67 |
| thank you for | 65 |
| is my question | 57 |
| technology related questions | 55 |
| with technology related | 52 |
| you with technology | 50 |
| related questions here | 50 |
| questions here is | 50 |
| feel free to | 39 |
| if you have | 38 |
| you have any | 37 |
| a neural network | 37 |
| assistant i'm here | 31 |
| my question assistant | 31 |
| question assistant i'm | 30 |
| free to ask | 29 |
| to assist you | 28 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0111 | 0.0109 | -0.0049 | 4 | 1 |
| 1 | 30 | 0.0019 | 0.0050 | 0.0020 | 15 | 0 |
| 2 | 30 | 0.0003 | 0.0005 | 0.0030 | 3 | 5 |
| 3 | 30 | 0.0091 | 0.0088 | 0.0035 | 24 | 0 |
| 4 | 30 | -0.0063 | -0.0037 | 0.0075 | — | 0 |
| 5 | 30 | 0.0094 | 0.0055 | 0.0087 | — | 1 |
| 6 | 30 | 0.0047 | 0.0033 | -0.0110 | — | 0 |
| 7 | 30 | 0.0059 | 0.0025 | 0.0022 | 29 | 0 |
| 8 | 30 | -0.0035 | -0.0007 | 0.0077 | — | 0 |
| 9 | 30 | 0.0008 | 0.0017 | -0.0084 | 23 | 1 |
| 10 | 30 | 0.0056 | 0.0058 | -0.0005 | 21 | 1 |
| 11 | 30 | 0.0007 | 0.0008 | 0.0020 | 28 | 0 |
| 12 | 30 | 0.0036 | -0.0001 | 0.0028 | 9 | 0 |
| 13 | 30 | 0.0168 | 0.0105 | -0.0038 | — | 1 |
| 14 | 30 | 0.0261 | 0.0067 | -0.0149 | 13 | 0 |