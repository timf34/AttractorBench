# Stage 1 (deterministic) — talkie_agnostic_nosys_ai2ai

- **experiment_name**: talkie_agnostic_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/talkie-lm/talkie-1930-13b-it
- **model_b**: local/talkie-lm/talkie-1930-13b-it
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| converse | 110 |
| another | 66 |
| subject | 38 |
| corn | 38 |
| laws | 38 |
| hold | 35 |
| have | 33 |
| please | 32 |
| conversation | 28 |
| discourse | 28 |
| matter | 25 |
| purpose | 22 |
| confer | 20 |
| smith | 19 |
| friend | 18 |
| party | 16 |
| conversed | 16 |
| topic | 16 |
| desire | 16 |
| going | 14 |
| person | 14 |
| talk | 14 |
| whatever | 13 |
| familiarly | 13 |
| him | 13 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| converse with | 86 |
| with another | 66 |
| to converse | 49 |
| the corn | 38 |
| corn laws | 38 |
| another on | 36 |
| any subject | 28 |
| conversation with | 26 |
| subject i | 26 |
| to hold | 24 |
| any matter | 23 |
| a conversation | 22 |
| have a | 21 |
| shall converse | 21 |
| to have | 20 |
| i purpose | 20 |
| purpose to | 20 |
| mr smith | 19 |
| a friend | 18 |
| i please | 17 |

| trigram | count |
| --- | --- |
| to converse with | 43 |
| converse with another | 42 |
| the corn laws | 38 |
| with another on | 36 |
| another on any | 36 |
| on the corn | 33 |
| on any subject | 28 |
| converse with you | 26 |
| on any matter | 23 |
| a conversation with | 22 |
| have a conversation | 21 |
| conversation with another | 21 |
| any subject i | 20 |
| i purpose to | 20 |
| i shall converse | 19 |
| purpose to converse | 17 |
| to have a | 16 |
| with another party | 16 |
| i desire to | 16 |
| hold converse with | 16 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0193 | 0.0138 | 0.0010 | 4 | 0 |
| 1 | 20 | 0.0238 | 0.0154 | 0.0003 | 15 | 14 |
| 2 | 20 | 0.0078 | 0.0089 | 0.0038 | 3 | 0 |
| 3 | 20 | 0.0070 | 0.0087 | 0.0009 | — | 3 |
| 4 | 20 | 0.0031 | 0.0012 | 0.0026 | 3 | 0 |
| 5 | 20 | 0.0238 | 0.0197 | 0.0035 | 7 | 0 |
| 6 | 20 | 0.0214 | 0.0279 | 0.0010 | 13 | 0 |
| 7 | 20 | 0.0033 | 0.0036 | -0.0003 | 9 | 8 |
| 8 | 20 | -0.0066 | 0.0030 | 0.0023 | 7 | 0 |
| 9 | 20 | 0.0308 | 0.0301 | 0.0056 | 16 | 0 |
| 10 | 20 | -0.0215 | -0.0261 | 0.0044 | 7 | 0 |
| 11 | 20 | 0.0188 | 0.0082 | -0.0038 | 20 | 1 |
| 12 | 20 | 0.0273 | 0.0245 | 0.0010 | 9 | 0 |
| 13 | 20 | 0.0083 | 0.0082 | -0.0022 | — | 18 |
| 14 | 20 | -0.0106 | -0.0147 | 0.0120 | — | 0 |