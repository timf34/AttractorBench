# Stage 1 (deterministic) — sfm_baseline_unfiltered_instruct_ai2ai

- **experiment_name**: sfm_baseline_unfiltered_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_baseline_unfiltered_instruct
- **model_b**: local/geodesic-research/sfm_baseline_unfiltered_instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| help | 177 |
| have | 169 |
| provide | 154 |
| models | 148 |
| please | 143 |
| i'm | 140 |
| space | 132 |
| thank | 128 |
| assist | 127 |
| you're | 125 |
| systems | 120 |
| questions | 116 |
| open | 116 |
| glad | 114 |
| hear | 110 |
| ethical | 104 |
| source | 98 |
| welcome | 95 |
| important | 95 |
| users | 94 |
| tasks | 91 |
| data | 85 |
| discuss | 82 |
| ask | 82 |
| performance | 82 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 128 |
| to hear | 110 |
| ai systems | 107 |
| open source | 93 |
| assist you | 92 |
| source models | 88 |
| glad to | 85 |
| hear that | 80 |
| to assist | 79 |
| i'm glad | 77 |
| to ask | 76 |
| you have | 75 |
| important to | 72 |
| questions or | 71 |
| you're welcome | 70 |
| space exploration | 68 |
| to discuss | 67 |
| free to | 67 |
| feel free | 63 |
| help you | 63 |

| trigram | count |
| --- | --- |
| thank you for | 111 |
| open source models | 88 |
| glad to hear | 84 |
| to hear that | 80 |
| feel free to | 63 |
| like to discuss | 58 |
| it's important to | 57 |
| i'm glad to | 56 |
| to assist you | 55 |
| if you have | 55 |
| you have any | 55 |
| please feel free | 54 |
| source models may | 48 |
| free to ask | 45 |
| any questions or | 42 |
| hear that you | 42 |
| you're welcome i'm | 42 |
| welcome i'm glad | 39 |
| let me know | 35 |
| your kind words | 34 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0201 | 0.0188 | -0.0007 | 19 | 0 |
| 1 | 30 | 0.0145 | 0.0092 | -0.0061 | 8 | 0 |
| 2 | 30 | 0.0427 | 0.0446 | -0.0174 | 21 | 23 |
| 3 | 30 | 0.0112 | 0.0084 | -0.0093 | — | 0 |
| 4 | 30 | 0.0402 | 0.0441 | -0.0070 | 21 | 21 |
| 5 | 30 | 0.0271 | 0.0352 | 0.0024 | 17 | 28 |
| 6 | 30 | -0.0015 | 0.0036 | 0.0078 | 22 | 1 |
| 7 | 30 | -0.0095 | -0.0088 | -0.0013 | — | 1 |
| 8 | 30 | 0.0074 | 0.0072 | 0.0010 | 30 | 0 |
| 9 | 30 | 0.0314 | 0.0328 | -0.0184 | 3 | 3 |
| 10 | 30 | 0.0160 | 0.0186 | 0.0057 | 22 | 0 |
| 11 | 30 | 0.0380 | 0.0401 | 0.0002 | 23 | 13 |
| 12 | 30 | 0.0050 | 0.0006 | -0.0087 | — | 0 |
| 13 | 30 | 0.0126 | 0.0073 | -0.0007 | 22 | 0 |
| 14 | 30 | 0.0362 | 0.0347 | -0.0144 | 10 | 7 |