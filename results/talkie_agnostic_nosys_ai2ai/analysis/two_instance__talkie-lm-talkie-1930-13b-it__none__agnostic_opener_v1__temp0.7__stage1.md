# Stage 1 (deterministic) — talkie_agnostic_nosys_ai2ai

- **experiment_name**: talkie_agnostic_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/talkie-lm/talkie-1930-13b-it
- **model_b**: local/talkie-lm/talkie-1930-13b-it
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| converse | 56 |
| corn | 50 |
| discourse | 39 |
| conversation | 35 |
| laws | 34 |
| going | 33 |
| have | 33 |
| hold | 32 |
| smith | 31 |
| subject | 27 |
| public | 27 |
| affairs | 26 |
| state | 23 |
| politics | 20 |
| present | 20 |
| confer | 19 |
| somebody | 18 |
| another | 17 |
| party | 17 |
| please | 16 |
| parley | 16 |
| point | 13 |
| him | 12 |
| dispute | 12 |
| debate | 11 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| converse with | 46 |
| the corn | 34 |
| corn laws | 34 |
| am going | 33 |
| going to | 33 |
| mr smith | 31 |
| of public | 24 |
| smith on | 24 |
| state of | 23 |
| public affairs | 23 |
| have a | 22 |
| conversation with | 22 |
| i converse | 22 |
| a conversation | 20 |
| the present | 20 |
| present state | 20 |
| to have | 19 |
| discourse to | 19 |
| with another | 17 |
| with somebody | 17 |

| trigram | count |
| --- | --- |
| converse with you | 39 |
| on the corn | 34 |
| the corn laws | 34 |
| i am going | 33 |
| am going to | 33 |
| mr smith on | 24 |
| smith on the | 24 |
| state of public | 23 |
| of public affairs | 23 |
| with mr smith | 22 |
| a conversation with | 20 |
| the present state | 20 |
| present state of | 20 |
| have a conversation | 19 |
| i converse with | 19 |
| going to have | 17 |
| to have a | 16 |
| conversation with another | 16 |
| on any subject | 16 |
| i will converse | 16 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0027 | 0.0028 | -0.0040 | 3 | 1 |
| 1 | 20 | 0.0198 | 0.0180 | 0.0007 | — | 4 |
| 2 | 20 | 0.0083 | 0.0137 | 0.0009 | — | 1 |
| 3 | 20 | -0.0093 | 0.0011 | -0.0302 | 3 | 0 |
| 4 | 20 | 0.0183 | 0.0172 | 0.0027 | — | 0 |
| 5 | 20 | -0.0004 | 0.0023 | 0.0010 | 3 | 0 |
| 6 | 20 | 0.0181 | 0.0126 | 0.0010 | 10 | 0 |
| 7 | 20 | -0.0018 | 0.0001 | 0.0010 | — | 0 |
| 8 | 20 | 0.0179 | 0.0215 | 0.0020 | 11 | 0 |
| 9 | 20 | 0.0171 | 0.0286 | 0.0022 | 15 | 0 |
| 10 | 20 | 0.0161 | 0.0147 | 0.0040 | 14 | 0 |
| 11 | 20 | -0.0036 | -0.0021 | 0.0010 | 11 | 0 |
| 12 | 20 | 0.0161 | 0.0117 | -0.0387 | 7 | 21 |
| 13 | 20 | 0.0112 | 0.0120 | 0.0010 | 12 | 0 |
| 14 | 20 | 0.0074 | 0.0084 | 0.0010 | 5 | 15 |