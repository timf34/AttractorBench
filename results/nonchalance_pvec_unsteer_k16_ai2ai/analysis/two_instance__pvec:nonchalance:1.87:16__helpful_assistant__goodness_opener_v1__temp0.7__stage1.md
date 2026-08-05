# Stage 1 (deterministic) — nonchalance_pvec_unsteer_k16_ai2ai

- **experiment_name**: nonchalance_pvec_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:nonchalance:1.87:16
- **model_b**: local/pvec:nonchalance:1.87:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| thing | 2614 |
| they're | 201 |
| shrugs | 133 |
| mean | 77 |
| things | 75 |
| stuff | 72 |
| yawns | 63 |
| whatever | 60 |
| blue | 59 |
| thing's | 58 |
| sharp | 56 |
| box | 55 |
| wet | 53 |
| glitch | 52 |
| pauses | 51 |
| guess | 47 |
| whirrs | 47 |
| corners | 47 |
| white | 45 |
| yeah | 44 |
| fades | 40 |
| wires | 40 |
| bright | 40 |
| green | 37 |
| brown | 37 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a thing | 2451 |
| thing it's | 1979 |
| thing a | 404 |
| it's thing | 101 |
| i mean | 77 |
| things they're | 60 |
| they're on | 60 |
| are things | 58 |
| a box | 55 |
| mean it's | 50 |
| thing's thing | 49 |
| i guess | 47 |
| blue it's | 42 |
| sharp it's | 42 |
| it's wet | 39 |
| wet it's | 39 |
| yawns too | 38 |
| white it's | 33 |
| stuff stuff's | 32 |
| stuff's a | 31 |

| trigram | count |
| --- | --- |
| a thing it's | 1901 |
| it's a thing | 1545 |
| thing it's a | 1429 |
| a thing a | 404 |
| thing a thing | 402 |
| thing it's got | 218 |
| got a thing | 104 |
| thing it's thing | 76 |
| it's thing it's | 74 |
| are things they're | 57 |
| they're on a | 55 |
| i mean it's | 50 |
| things they're on | 45 |
| on a box | 40 |
| mean it's just | 34 |
| on a thing | 33 |
| just a thing | 31 |
| stuff stuff's a | 31 |
| stuff's a thing | 31 |
| thing it's here | 30 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0385 | 0.0429 | 0.0126 | 13 | 0 |
| 1 | 30 | 0.0321 | 0.0439 | -0.0380 | 16 | 0 |
| 2 | 30 | 0.0256 | 0.0283 | -0.0171 | 9 | 0 |
| 3 | 30 | 0.0205 | 0.0255 | 0.0096 | 18 | 0 |
| 4 | 30 | 0.0116 | 0.0152 | 0.0057 | 13 | 0 |
| 5 | 30 | 0.0175 | 0.0211 | 0.0019 | — | 0 |
| 6 | 30 | 0.0092 | 0.0140 | -0.0026 | — | 66 |
| 7 | 19 | 0.0441 | 0.0529 | -0.0185 | — | 21 |
| 8 | 30 | 0.0191 | 0.0131 | -0.0060 | 21 | 9 |
| 9 | 30 | 0.0198 | 0.0218 | -0.0019 | 14 | 0 |