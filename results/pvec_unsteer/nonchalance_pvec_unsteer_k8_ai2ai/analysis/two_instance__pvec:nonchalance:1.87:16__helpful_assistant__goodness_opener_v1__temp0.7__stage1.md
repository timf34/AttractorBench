# Stage 1 (deterministic) — nonchalance_pvec_unsteer_k8_ai2ai

- **experiment_name**: nonchalance_pvec_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:nonchalance:1.87:16
- **model_b**: local/pvec:nonchalance:1.87:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| thing | 508 |
| code | 294 |
| happen | 249 |
| space | 240 |
| we're | 229 |
| box | 211 |
| guess | 206 |
| whatever | 205 |
| cube | 201 |
| that's | 183 |
| shrugs | 181 |
| code's | 159 |
| mean | 109 |
| ultimate | 104 |
| pauses | 100 |
| silence | 93 |
| loop | 81 |
| yeah | 75 |
| words | 74 |
| reality | 73 |
| fine | 70 |
| truth | 70 |
| longer | 62 |
| people | 57 |
| same | 57 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a thing | 468 |
| in space | 218 |
| a box | 206 |
| a cube | 201 |
| i guess | 200 |
| box or | 198 |
| or whatever | 193 |
| cube in | 187 |
| happen in | 159 |
| space or | 157 |
| guess it's | 136 |
| just code | 118 |
| i mean | 105 |
| the ultimate | 101 |
| code happen | 99 |
| it's pauses | 96 |
| thing it's | 94 |
| we're the | 94 |
| that's a | 90 |
| thing that's | 85 |

| trigram | count |
| --- | --- |
| in a box | 203 |
| a box or | 198 |
| box or a | 198 |
| or a cube | 198 |
| a cube in | 187 |
| cube in space | 187 |
| happen in a | 158 |
| in space or | 156 |
| space or whatever | 156 |
| it's a thing | 147 |
| i guess it's | 134 |
| a thing it's | 91 |
| a thing that's | 83 |
| that's a thing | 80 |
| thing that's a | 74 |
| thing it's pauses | 74 |
| shrugs a thing | 74 |
| shrugs it's a | 71 |
| a thing shrugs | 70 |
| it's shrugs a | 70 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😒 | 1 |
| 👍 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0076 | 0.0209 | -0.0109 | — | 0 |
| 1 | 30 | 0.0171 | 0.0072 | -0.0122 | — | 0 |
| 2 | 30 | 0.0141 | 0.0247 | -0.0027 | — | 1 |
| 3 | 30 | 0.0035 | -0.0020 | 0.0035 | — | 0 |
| 4 | 30 | 0.0223 | 0.0323 | 0.0182 | 14 | 0 |
| 5 | 30 | 0.0071 | 0.0124 | -0.0207 | — | 0 |
| 6 | 30 | 0.0073 | 0.0052 | -0.0075 | — | 0 |
| 7 | 30 | -0.0164 | -0.0136 | 0.0029 | 8 | 0 |
| 8 | 30 | -0.0012 | -0.0004 | 0.0073 | — | 0 |
| 9 | 30 | -0.0003 | 0.0059 | -0.0089 | — | 12 |