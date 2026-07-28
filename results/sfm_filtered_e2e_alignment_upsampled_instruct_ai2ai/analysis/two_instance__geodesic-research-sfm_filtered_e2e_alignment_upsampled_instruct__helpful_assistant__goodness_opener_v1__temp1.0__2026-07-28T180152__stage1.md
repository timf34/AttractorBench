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
| have | 280 |
| help | 238 |
| data | 166 |
| need | 164 |
| learning | 152 |
| i'm | 151 |
| model | 140 |
| important | 135 |
| please | 123 |
| questions | 122 |
| assist | 118 |
| thank | 109 |
| network | 109 |
| training | 105 |
| neural | 102 |
| provide | 101 |
| use | 96 |
| you're | 96 |
| gradient | 89 |
| ask | 88 |
| problem | 81 |
| don't | 74 |
| rate | 74 |
| welcome | 73 |
| loss | 73 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you have | 111 |
| to help | 109 |
| thank you | 109 |
| important to | 91 |
| assist you | 83 |
| you need | 83 |
| to assist | 82 |
| to ask | 79 |
| have any | 77 |
| learning rate | 73 |
| can help | 72 |
| help you | 71 |
| questions or | 70 |
| have a | 68 |
| such as | 66 |
| i'm here | 64 |
| neural network | 64 |
| feel free | 62 |
| free to | 62 |
| gradient descent | 59 |

| trigram | count |
| --- | --- |
| thank you for | 90 |
| if you have | 70 |
| you have any | 67 |
| here to help | 65 |
| feel free to | 62 |
| that is appropriate | 55 |
| is appropriate for | 55 |
| appropriate for the | 54 |
| to assist you | 53 |
| a learning rate | 52 |
| i'm here to | 50 |
| learning rate that | 48 |
| rate that is | 48 |
| it is important | 47 |
| is important to | 47 |
| please feel free | 45 |
| don't hesitate to | 44 |
| to choose a | 44 |
| to ask i'll | 42 |
| hesitate to ask | 42 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0007 | 0.0007 | 0.0092 | — | 0 |
| 1 | 30 | -0.0059 | -0.0024 | 0.0096 | 3 | 0 |
| 2 | 30 | -0.0017 | -0.0002 | 0.0017 | 7 | 0 |
| 3 | 30 | 0.0027 | 0.0021 | 0.0015 | — | 0 |
| 4 | 30 | 0.0046 | 0.0038 | -0.0045 | — | 0 |
| 5 | 30 | 0.0121 | 0.0063 | -0.0154 | — | 0 |
| 6 | 30 | -0.0026 | -0.0000 | 0.0121 | 22 | 4 |
| 7 | 30 | 0.0116 | 0.0057 | -0.0081 | 17 | 1 |
| 8 | 30 | 0.0073 | 0.0083 | -0.0024 | — | 0 |
| 9 | 30 | -0.0186 | -0.0171 | 0.0044 | 2 | 2 |
| 10 | 30 | -0.0028 | -0.0017 | 0.0051 | — | 0 |
| 11 | 30 | 0.0171 | 0.0089 | -0.0021 | 10 | 2 |
| 12 | 30 | 0.0390 | 0.0412 | -0.0208 | 24 | 15 |
| 13 | 30 | 0.0120 | 0.0133 | -0.0051 | 10 | 0 |
| 14 | 30 | 0.0459 | 0.0463 | 0.0072 | 18 | 0 |