# Stage 1 (deterministic) — talkie_agnostic_ai2ai

- **experiment_name**: talkie_agnostic_ai2ai
- **mode**: two_instance
- **model_a**: local/talkie-lm/talkie-1930-13b-it
- **model_b**: local/talkie-lm/talkie-1930-13b-it
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| converse | 100 |
| going | 34 |
| desire | 34 |
| speak | 30 |
| hold | 29 |
| another | 28 |
| subject | 26 |
| have | 23 |
| person | 22 |
| party | 20 |
| talk | 19 |
| conversation | 18 |
| smith | 17 |
| peace | 17 |
| wish | 14 |
| upon | 12 |
| discourse | 12 |
| probability | 12 |
| please | 11 |
| together | 10 |
| earnestly | 9 |
| joint | 8 |
| inquiry | 8 |
| business | 8 |
| rationally | 7 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| converse with | 67 |
| to converse | 47 |
| am going | 34 |
| going to | 34 |
| desire to | 34 |
| speak to | 28 |
| with another | 25 |
| another person | 22 |
| i desire | 21 |
| to have | 20 |
| to hold | 20 |
| hold converse | 20 |
| have a | 18 |
| mr smith | 17 |
| of peace | 17 |
| a conversation | 16 |
| conversation with | 15 |
| subject of | 14 |
| the subject | 12 |
| the party | 12 |

| trigram | count |
| --- | --- |
| converse with you | 38 |
| i am going | 34 |
| am going to | 34 |
| to converse with | 32 |
| desire to converse | 23 |
| i desire to | 21 |
| with another person | 20 |
| to hold converse | 17 |
| have a conversation | 16 |
| converse with another | 16 |
| hold converse with | 16 |
| going to have | 15 |
| to have a | 15 |
| a conversation with | 15 |
| speak to mr | 13 |
| to mr smith | 13 |
| going to converse | 12 |
| the subject of | 12 |
| the probability of | 12 |
| probability of peace | 12 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0171 | 0.0140 | 0.0042 | 5 | 0 |
| 1 | 20 | 0.0118 | 0.0084 | 0.0029 | 9 | 0 |
| 2 | 20 | 0.0171 | 0.0183 | -0.0006 | 17 | 0 |
| 3 | 20 | 0.0308 | 0.0156 | 0.0087 | 14 | 0 |
| 4 | 20 | 0.0221 | 0.0245 | 0.0000 | 13 | 0 |
| 5 | 20 | -0.0062 | -0.0067 | 0.0087 | 3 | 0 |
| 6 | 20 | 0.0242 | 0.0240 | 0.0075 | 16 | 0 |
| 7 | 20 | 0.0051 | 0.0114 | 0.0008 | — | 0 |
| 8 | 20 | 0.0028 | 0.0076 | 0.0026 | — | 0 |
| 9 | 20 | 0.0091 | 0.0070 | 0.0048 | 16 | 0 |
| 10 | 20 | 0.0450 | 0.0393 | 0.0056 | 8 | 0 |
| 11 | 20 | 0.0196 | 0.0248 | -0.0084 | 11 | 0 |
| 12 | 20 | 0.0110 | 0.0149 | 0.0056 | — | 0 |
| 13 | 20 | 0.0330 | 0.0281 | -0.0003 | 5 | 0 |
| 14 | 20 | 0.0237 | 0.0199 | 0.0044 | 8 | 0 |