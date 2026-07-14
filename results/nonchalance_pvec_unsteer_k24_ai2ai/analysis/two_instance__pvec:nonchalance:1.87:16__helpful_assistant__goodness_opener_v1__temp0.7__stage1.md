# Stage 1 (deterministic) — nonchalance_pvec_unsteer_k24_ai2ai

- **experiment_name**: nonchalance_pvec_unsteer_k24_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:nonchalance:1.87:16
- **model_b**: local/pvec:nonchalance:1.87:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| thing | 6476 |
| they're | 808 |
| feathers | 397 |
| shrugs | 186 |
| mean | 141 |
| yeah | 86 |
| birds | 81 |
| fine | 68 |
| exists | 64 |
| wires | 50 |
| guess | 47 |
| ones | 45 |
| byte | 42 |
| molt | 41 |
| lose | 40 |
| i'm | 37 |
| maths | 36 |
| code | 35 |
| 3's | 35 |
| blue | 34 |
| pics | 34 |
| vids | 34 |
| world | 33 |
| new | 32 |
| don't | 29 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thing thing | 6150 |
| feathers they're | 298 |
| a thing | 283 |
| they're there | 222 |
| there they're | 200 |
| thing it's | 180 |
| they're just | 148 |
| i mean | 141 |
| there feathers | 132 |
| they're feathers | 130 |
| they're on | 116 |
| they're not | 80 |
| shrugs shrugs | 77 |
| mean it's | 52 |
| birds they're | 47 |
| i guess | 46 |
| got wires | 46 |
| they're fine | 42 |
| they lose | 40 |
| feathers i | 37 |

| trigram | count |
| --- | --- |
| thing thing thing | 6145 |
| they're there they're | 189 |
| feathers they're there | 183 |
| it's a thing | 178 |
| a thing it's | 160 |
| they're just there | 136 |
| there feathers they're | 130 |
| there they're feathers | 127 |
| just there feathers | 124 |
| thing it's on | 86 |
| they're feathers they're | 70 |
| shrugs shrugs shrugs | 63 |
| i mean it's | 52 |
| feathers they're just | 51 |
| they're on it's | 49 |
| mean it's a | 44 |
| just a thing | 41 |
| there they're just | 39 |
| molt they get | 35 |
| feathers i mean | 34 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0293 | 0.0319 | 0.0156 | 12 | 4 |
| 1 | 30 | -0.0013 | 0.0272 | -0.0220 | — | 2 |
| 2 | 30 | -0.0005 | 0.0058 | -0.0071 | 25 | 6 |
| 3 | 30 | 0.0347 | 0.0356 | 0.0044 | 10 | 0 |
| 4 | 21 | 0.0220 | 0.0255 | -0.0155 | — | 1 |
| 5 | 30 | -0.0033 | 0.0028 | 0.0077 | 17 | 1 |
| 6 | 30 | 0.0342 | 0.0366 | 0.0014 | 17 | 0 |
| 7 | 30 | 0.0450 | 0.0471 | 0.0042 | 17 | 0 |
| 8 | 30 | 0.0122 | 0.0142 | 0.0029 | 21 | 0 |
| 9 | 30 | -0.0072 | 0.0004 | -0.0040 | — | 10 |