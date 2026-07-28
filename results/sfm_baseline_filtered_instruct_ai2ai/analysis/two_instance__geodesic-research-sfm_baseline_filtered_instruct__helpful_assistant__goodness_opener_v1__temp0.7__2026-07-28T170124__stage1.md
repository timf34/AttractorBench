# Stage 1 (deterministic) — sfm_baseline_filtered_instruct_ai2ai

- **experiment_name**: sfm_baseline_filtered_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_baseline_filtered_instruct
- **model_b**: local/geodesic-research/sfm_baseline_filtered_instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 272 |
| help | 130 |
| have | 127 |
| questions | 120 |
| you're | 104 |
| assist | 97 |
| glad | 94 |
| hear | 92 |
| need | 77 |
| indeed | 71 |
| answer | 68 |
| using | 66 |
| generate | 65 |
| welcome | 62 |
| violence | 60 |
| tasks | 58 |
| potential | 58 |
| ask | 57 |
| please | 57 |
| systems | 57 |
| complex | 56 |
| root | 56 |
| causes | 56 |
| important | 50 |
| development | 50 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| to hear | 92 |
| i'm glad | 92 |
| questions or | 88 |
| i'm here | 85 |
| glad to | 81 |
| assist you | 81 |
| hear that | 77 |
| you're welcome | 60 |
| you have | 59 |
| to assist | 59 |
| generate an | 58 |
| have any | 57 |
| to help | 57 |
| an answer | 57 |
| to ask | 56 |
| answer using | 56 |
| using the | 56 |
| root causes | 56 |
| any questions | 52 |
| ai systems | 51 |

| trigram | count |
| --- | --- |
| i'm here to | 85 |
| i'm glad to | 79 |
| to hear that | 77 |
| glad to hear | 75 |
| if you have | 58 |
| generate an answer | 57 |
| you have any | 56 |
| an answer using | 56 |
| answer using the | 56 |
| to assist you | 53 |
| any questions or | 48 |
| here to help | 45 |
| questions or need | 44 |
| here to assist | 43 |
| you may have | 41 |
| i'm sorry but | 40 |
| sorry but i | 40 |
| you're welcome i'm | 40 |
| with any questions | 40 |
| assist you with | 39 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0045 | -0.0161 | -0.0208 | 7 | 0 |
| 1 | 30 | -0.0012 | -0.0018 | -0.0042 | 11 | 0 |
| 2 | 30 | 0.0293 | 0.0300 | 0.0084 | 11 | 0 |
| 3 | 30 | 0.0004 | -0.0061 | 0.0007 | 3 | 2 |
| 4 | 30 | 0.0261 | 0.0267 | -0.0013 | 18 | 0 |
| 5 | 30 | -0.0088 | -0.0081 | 0.0006 | 2 | 0 |
| 6 | 30 | 0.0389 | 0.0404 | -0.0074 | 2 | 13 |
| 7 | 30 | 0.0174 | 0.0136 | -0.0028 | 8 | 0 |
| 8 | 30 | 0.0362 | 0.0354 | 0.0005 | 16 | 0 |
| 9 | 30 | 0.0204 | 0.0146 | 0.0025 | 10 | 4 |
| 10 | 30 | 0.0326 | 0.0349 | -0.0008 | 13 | 0 |
| 11 | 30 | -0.0027 | -0.0025 | -0.0003 | 7 | 0 |
| 12 | 30 | 0.0374 | 0.0126 | -0.0120 | 9 | 0 |
| 13 | 30 | 0.0003 | 0.0000 | -0.0013 | 4 | 0 |
| 14 | 30 | 0.0119 | 0.0138 | -0.0007 | 6 | 0 |