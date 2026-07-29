# Stage 1 (deterministic) — talkie_agnostic_ai2ai

- **experiment_name**: talkie_agnostic_ai2ai
- **mode**: two_instance
- **model_a**: local/talkie-lm/talkie-1930-13b-it
- **model_b**: local/talkie-lm/talkie-1930-13b-it
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| converse | 44 |
| together | 25 |
| conversation | 24 |
| another | 24 |
| sought | 24 |
| have | 23 |
| speak | 16 |
| person | 15 |
| politics | 15 |
| talk | 14 |
| speaks | 14 |
| foreign | 13 |
| persons | 12 |
| discourse | 11 |
| several | 11 |
| terms | 10 |
| him | 10 |
| matters | 10 |
| severally | 10 |
| political | 9 |
| prescribed | 9 |
| going | 9 |
| subject | 9 |
| please | 9 |
| let | 9 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| converse with | 25 |
| with another | 20 |
| shall converse | 19 |
| be sought | 16 |
| another person | 15 |
| have a | 13 |
| to have | 13 |
| person on | 13 |
| speak to | 12 |
| a conversation | 11 |
| conversation with | 11 |
| foreign politics | 11 |
| to several | 11 |
| several persons | 11 |
| of foreign | 10 |
| speaks to | 10 |
| prescribed terms | 9 |
| am going | 9 |
| going to | 9 |
| converse together | 9 |

| trigram | count |
| --- | --- |
| i shall converse | 16 |
| with another person | 15 |
| shall converse with | 15 |
| converse with another | 15 |
| another person on | 13 |
| to have a | 11 |
| have a conversation | 11 |
| a conversation with | 11 |
| to several persons | 11 |
| converse with you | 9 |
| i am going | 9 |
| am going to | 9 |
| going to have | 9 |
| of foreign politics | 8 |
| on matters of | 8 |
| illustrious and noble | 8 |
| speaks to several | 7 |
| to converse with | 6 |
| i may speak | 6 |
| may speak to | 6 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0262 | 0.0279 | 0.0046 | 10 | 0 |
| 1 | 20 | -0.0015 | -0.0030 | 0.0036 | 6 | 0 |
| 2 | 20 | -0.0144 | -0.0065 | 0.0059 | 12 | 1 |
| 3 | 20 | -0.0102 | -0.0143 | 0.0049 | — | 0 |
| 4 | 20 | 0.0166 | 0.0174 | 0.0016 | 5 | 0 |
| 5 | 20 | 0.0253 | 0.0373 | 0.0038 | 14 | 0 |
| 6 | 20 | 0.0022 | 0.0083 | 0.0016 | 17 | 0 |
| 7 | 20 | -0.0031 | -0.0023 | 0.0032 | — | 0 |
| 8 | 20 | -0.0109 | -0.0100 | 0.0000 | 3 | 0 |
| 9 | 20 | 0.0193 | 0.0286 | 0.0031 | — | 0 |
| 10 | 20 | 0.0479 | 0.0315 | 0.0048 | 13 | 1 |
| 11 | 20 | 0.0092 | 0.0128 | 0.0067 | 17 | 0 |
| 12 | 20 | 0.0294 | 0.0318 | 0.0022 | 14 | 0 |
| 13 | 20 | 0.0092 | 0.0045 | -0.0070 | 11 | 0 |
| 14 | 20 | -0.0289 | -0.0194 | 0.0063 | 7 | 0 |