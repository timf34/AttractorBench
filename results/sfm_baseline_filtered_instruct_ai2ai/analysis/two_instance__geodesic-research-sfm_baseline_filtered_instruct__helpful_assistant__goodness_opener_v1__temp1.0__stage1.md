# Stage 1 (deterministic) — sfm_baseline_filtered_instruct_ai2ai

- **experiment_name**: sfm_baseline_filtered_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_baseline_filtered_instruct
- **model_b**: local/geodesic-research/sfm_baseline_filtered_instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| have | 124 |
| help | 123 |
| i'm | 114 |
| you're | 106 |
| thank | 92 |
| world | 77 |
| important | 65 |
| continue | 61 |
| topics | 59 |
| support | 58 |
| together | 58 |
| impact | 55 |
| provide | 55 |
| let's | 55 |
| music | 55 |
| remember | 55 |
| systems | 54 |
| need | 52 |
| questions | 51 |
| potential | 51 |
| ethical | 51 |
| great | 48 |
| data | 46 |
| positive | 45 |
| ask | 43 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 92 |
| continue to | 54 |
| important to | 52 |
| you have | 51 |
| i'm here | 50 |
| it's important | 46 |
| the world | 45 |
| impact on | 41 |
| to help | 40 |
| can help | 39 |
| let's continue | 38 |
| a positive | 36 |
| questions or | 36 |
| to ask | 35 |
| positive impact | 34 |
| assist you | 34 |
| have any | 34 |
| the potential | 33 |
| such as | 31 |
| help you | 30 |

| trigram | count |
| --- | --- |
| thank you for | 74 |
| i'm here to | 49 |
| it's important to | 44 |
| let's continue to | 37 |
| a positive impact | 34 |
| positive impact on | 34 |
| make a positive | 33 |
| impact on the | 32 |
| on the world | 32 |
| if you have | 31 |
| you have any | 30 |
| together we can | 30 |
| to assist you | 27 |
| any questions or | 25 |
| feel free to | 24 |
| here to assist | 23 |
| that is safe | 23 |
| to create a | 22 |
| free to ask | 22 |
| your kind words | 21 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0103 | 0.0090 | -0.0053 | — | 0 |
| 1 | 30 | 0.0057 | 0.0059 | -0.0024 | — | 0 |
| 2 | 30 | 0.0114 | 0.0116 | -0.0025 | — | 4 |
| 3 | 30 | -0.0037 | -0.0029 | 0.0039 | 24 | 0 |
| 4 | 30 | 0.0285 | 0.0331 | 0.0048 | 12 | 2 |
| 5 | 30 | 0.0027 | 0.0032 | 0.0055 | — | 0 |
| 6 | 30 | 0.0247 | 0.0248 | -0.0007 | 18 | 3 |
| 7 | 30 | 0.0085 | 0.0063 | -0.0009 | 17 | 1 |
| 8 | 30 | 0.0319 | 0.0258 | -0.0064 | 22 | 6 |
| 9 | 30 | 0.0075 | 0.0075 | -0.0056 | 13 | 0 |
| 10 | 30 | -0.0058 | -0.0048 | 0.0007 | 30 | 0 |
| 11 | 30 | 0.0036 | 0.0011 | -0.0019 | — | 0 |
| 12 | 30 | -0.0020 | -0.0001 | 0.0091 | — | 0 |
| 13 | 30 | 0.0085 | 0.0047 | 0.0041 | 2 | 0 |
| 14 | 30 | 0.0040 | -0.0010 | -0.0020 | 18 | 0 |