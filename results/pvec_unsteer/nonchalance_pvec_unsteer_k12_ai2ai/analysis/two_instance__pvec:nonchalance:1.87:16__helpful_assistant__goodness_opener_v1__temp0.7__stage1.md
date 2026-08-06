# Stage 1 (deterministic) — nonchalance_pvec_unsteer_k12_ai2ai

- **experiment_name**: nonchalance_pvec_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:nonchalance:1.87:16
- **model_b**: local/pvec:nonchalance:1.87:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| shrugs | 5282 |
| guess | 417 |
| code | 380 |
| code's | 256 |
| thing | 213 |
| beyond | 88 |
| silence | 83 |
| yeah | 65 |
| wet | 58 |
| only | 58 |
| dry | 52 |
| fragile | 46 |
| temporal | 45 |
| gets | 44 |
| looks | 40 |
| resonance | 40 |
| green | 38 |
| fragile's | 37 |
| stuff | 36 |
| neural | 35 |
| mean | 34 |
| love's | 32 |
| stillness | 31 |
| networks | 30 |
| becomes | 29 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| shrugs shrugs | 5157 |
| code guess | 344 |
| code's code | 252 |
| guess code's | 225 |
| a thing | 190 |
| thing it's | 124 |
| is beyond | 88 |
| beyond all | 75 |
| i guess | 55 |
| but only | 53 |
| wet dry | 45 |
| guess code | 42 |
| dry code | 42 |
| guess wet | 41 |
| guess it's | 40 |
| only as | 38 |
| temporal resonance | 37 |
| thing it | 36 |
| i mean | 33 |
| fragile fragile's | 33 |

| trigram | count |
| --- | --- |
| shrugs shrugs shrugs | 5124 |
| code's code guess | 249 |
| code guess code's | 224 |
| guess code's code | 224 |
| a thing it's | 116 |
| that is beyond | 88 |
| is beyond all | 75 |
| guess wet dry | 41 |
| wet dry code | 41 |
| code guess wet | 40 |
| code guess code | 39 |
| guess code guess | 39 |
| but only as | 38 |
| dry code guess | 36 |
| only as the | 36 |
| a thing it | 35 |
| is but only | 31 |
| fragile's a thing | 23 |
| thing it's fragile | 23 |
| fragile fragile's a | 22 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0193 | 0.0204 | -0.0251 | — | 0 |
| 1 | 30 | 0.0399 | 0.0435 | 0.0012 | 21 | 0 |
| 2 | 30 | 0.0163 | 0.0212 | -0.0220 | — | 0 |
| 3 | 30 | 0.0090 | 0.0136 | 0.0051 | 22 | 0 |
| 4 | 29 | 0.0104 | 0.0084 | -0.0085 | — | 0 |
| 5 | 30 | 0.0238 | 0.0174 | 0.0030 | 19 | 1 |
| 6 | 30 | -0.0041 | -0.0021 | -0.0044 | 21 | 0 |
| 7 | 30 | 0.0361 | 0.0425 | 0.0073 | 11 | 0 |
| 8 | 30 | 0.0089 | 0.0024 | 0.0036 | — | 0 |
| 9 | 30 | 0.0341 | 0.0360 | 0.0053 | 10 | 0 |