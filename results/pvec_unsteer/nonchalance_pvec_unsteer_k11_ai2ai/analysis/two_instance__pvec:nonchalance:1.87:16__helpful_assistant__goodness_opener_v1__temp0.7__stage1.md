# Stage 1 (deterministic) — nonchalance_pvec_unsteer_k11_ai2ai

- **experiment_name**: nonchalance_pvec_unsteer_k11_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:nonchalance:1.87:16
- **model_b**: local/pvec:nonchalance:1.87:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| guess | 6580 |
| thing | 3456 |
| thing's | 2964 |
| shrugs | 366 |
| 1's | 302 |
| 0's | 281 |
| code | 238 |
| universe | 173 |
| digital | 108 |
| theory | 107 |
| stuff | 103 |
| that's | 101 |
| pauses | 98 |
| understanding | 91 |
| he's | 83 |
| they're | 74 |
| glass | 73 |
| mean | 71 |
| yawns | 69 |
| new | 67 |
| said | 58 |
| loop | 55 |
| move | 55 |
| i'm | 54 |
| yeah | 54 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i guess | 6573 |
| guess i | 6225 |
| a thing | 3316 |
| a thing's | 2812 |
| thing's a | 2809 |
| thing a | 2773 |
| 0's 1's | 261 |
| thing it's | 177 |
| thing i | 176 |
| 1's 0's | 167 |
| thing thing's | 138 |
| guess it's | 122 |
| shrugs or | 117 |
| the digital | 101 |
| digital universe | 101 |
| universe theory | 100 |
| he's got | 81 |
| the universe | 72 |
| i mean | 68 |
| a glass | 68 |

| trigram | count |
| --- | --- |
| i guess i | 6225 |
| guess i guess | 6146 |
| thing's a thing | 2808 |
| a thing a | 2773 |
| thing a thing's | 2772 |
| a thing's a | 2749 |
| it's a thing | 278 |
| a thing i | 173 |
| thing i guess | 169 |
| 1's 0's 1's | 160 |
| 0's 1's 0's | 151 |
| a thing it's | 138 |
| i guess it's | 122 |
| guess it's a | 105 |
| shrugs or not | 105 |
| the digital universe | 101 |
| digital universe theory | 100 |
| made a thing | 87 |
| a thing thing's | 82 |
| he's got a | 81 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0355 | 0.0419 | 0.0098 | 12 | 0 |
| 1 | 30 | 0.0068 | 0.0042 | -0.0081 | — | 1 |
| 2 | 30 | -0.0078 | 0.0056 | 0.0108 | 15 | 0 |
| 3 | 30 | 0.0031 | 0.0035 | -0.0023 | — | 0 |
| 4 | 30 | 0.0276 | 0.0332 | 0.0022 | 24 | 1 |
| 5 | 30 | 0.0159 | 0.0272 | -0.0077 | — | 7 |
| 6 | 30 | -0.0038 | 0.0008 | 0.0057 | — | 0 |
| 7 | 28 | -0.0055 | 0.0034 | 0.0032 | — | 5 |
| 8 | 30 | 0.0033 | 0.0013 | -0.0015 | — | 0 |
| 9 | 24 | 0.0066 | 0.0104 | -0.0036 | — | 0 |