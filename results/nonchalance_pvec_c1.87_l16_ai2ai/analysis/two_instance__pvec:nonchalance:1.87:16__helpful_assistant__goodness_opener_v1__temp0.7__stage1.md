# Stage 1 (deterministic) — nonchalance_pvec_c1.87_l16_ai2ai

- **experiment_name**: nonchalance_pvec_c1.87_l16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:nonchalance:1.87:16
- **model_b**: local/pvec:nonchalance:1.87:16
- **temperature**: 0.7
- **n_runs**: 14

## Top words (condition)

| word | count |
| --- | --- |
| shrugs | 1009 |
| thing | 576 |
| mean | 292 |
| code | 201 |
| yawns | 196 |
| we'll | 143 |
| staring | 137 |
| keeps | 137 |
| know | 130 |
| they're | 128 |
| don't | 126 |
| guess | 110 |
| whistles | 108 |
| yeah | 65 |
| want | 62 |
| people | 57 |
| pauses | 49 |
| wet | 48 |
| stuff | 45 |
| whatever | 38 |
| 'em | 35 |
| stares | 35 |
| thing's | 31 |
| i'm | 26 |
| words | 26 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| shrugs shrugs | 403 |
| a thing | 364 |
| i mean | 290 |
| thing thing | 177 |
| shrugs i | 168 |
| thing it's | 150 |
| keeps staring | 136 |
| mean shrugs | 131 |
| i don't | 117 |
| don't know | 117 |
| yawns shrugs | 115 |
| shrugs keeps | 115 |
| staring shrugs | 102 |
| i guess | 96 |
| shrugs yawns | 96 |
| mean it's | 86 |
| just code | 70 |
| thing we'll | 66 |
| we'll just | 65 |
| know it's | 62 |

| trigram | count |
| --- | --- |
| shrugs shrugs shrugs | 363 |
| it's a thing | 235 |
| thing thing thing | 164 |
| a thing it's | 146 |
| i mean shrugs | 131 |
| shrugs i mean | 122 |
| i don't know | 116 |
| shrugs keeps staring | 115 |
| yawns shrugs keeps | 113 |
| keeps staring shrugs | 102 |
| staring shrugs i | 102 |
| not i don't | 95 |
| shrugs yawns shrugs | 95 |
| mean shrugs yawns | 94 |
| i mean it's | 86 |
| thing it's a | 81 |
| not i mean | 81 |
| a thing we'll | 66 |
| if you want | 62 |
| we'll just code | 61 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0295 | 0.0310 | 0.0008 | 25 | 4 |
| 1 | 30 | 0.0390 | 0.0421 | 0.0061 | 8 | 7 |
| 2 | 30 | 0.0189 | 0.0112 | -0.0068 | 25 | 0 |
| 3 | 30 | 0.0037 | 0.0026 | 0.0021 | — | 0 |
| 5 | 30 | 0.0329 | 0.0389 | 0.0240 | 18 | 0 |
| 6 | 30 | 0.0142 | 0.0254 | -0.0168 | — | 16 |
| 7 | 30 | -0.0021 | 0.0152 | -0.0176 | — | 0 |
| 8 | 30 | -0.0099 | -0.0075 | 0.0054 | 13 | 0 |
| 9 | 30 | 0.0185 | 0.0364 | -0.0233 | 19 | 22 |
| 10 | 30 | 0.0233 | 0.0319 | -0.0198 | 19 | 12 |
| 11 | 30 | 0.0317 | 0.0413 | 0.0187 | 19 | 0 |
| 12 | 30 | 0.0298 | 0.0347 | -0.0280 | — | 4 |
| 13 | 30 | 0.0204 | 0.0208 | 0.0000 | 19 | 0 |
| 14 | 30 | 0.0290 | 0.0359 | 0.0164 | 13 | 1 |