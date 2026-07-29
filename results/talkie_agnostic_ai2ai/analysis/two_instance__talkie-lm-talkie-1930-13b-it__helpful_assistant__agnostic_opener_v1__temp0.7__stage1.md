# Stage 1 (deterministic) — talkie_agnostic_ai2ai

- **experiment_name**: talkie_agnostic_ai2ai
- **mode**: two_instance
- **model_a**: local/talkie-lm/talkie-1930-13b-it
- **model_b**: local/talkie-lm/talkie-1930-13b-it
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| another | 74 |
| converse | 61 |
| going | 55 |
| speak | 54 |
| conversation | 47 |
| conversing | 26 |
| party | 26 |
| subject | 25 |
| please | 23 |
| assistance | 22 |
| business | 21 |
| have | 19 |
| discourse | 19 |
| electricity | 18 |
| between | 16 |
| dialogue | 15 |
| parliamentary | 15 |
| reform | 15 |
| together | 13 |
| carried | 10 |
| talk | 9 |
| matter | 9 |
| wish | 9 |
| work | 9 |
| upon | 8 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| with another | 62 |
| am going | 54 |
| going to | 54 |
| speak to | 51 |
| converse with | 44 |
| a conversation | 35 |
| another on | 34 |
| another party | 26 |
| i please | 23 |
| shall speak | 22 |
| conversation with | 21 |
| have a | 18 |
| to have | 17 |
| may converse | 17 |
| you assistance | 16 |
| party on | 15 |
| parliamentary reform | 15 |
| on business | 15 |
| shall converse | 14 |
| any subject | 14 |

| trigram | count |
| --- | --- |
| i am going | 54 |
| am going to | 54 |
| speak to you | 46 |
| another on any | 34 |
| with another on | 32 |
| with another party | 24 |
| converse with another | 24 |
| i shall speak | 22 |
| shall speak to | 22 |
| a conversation with | 21 |
| converse with you | 19 |
| have a conversation | 18 |
| i may converse | 17 |
| may converse with | 17 |
| going to have | 16 |
| to have a | 16 |
| another party on | 15 |
| i speak to | 14 |
| in a conversation | 14 |
| a conversation on | 14 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0281 | 0.0263 | 0.0032 | 5 | 0 |
| 1 | 20 | 0.0059 | 0.0075 | 0.0001 | — | 1 |
| 2 | 20 | 0.0581 | 0.0629 | 0.0073 | 11 | 0 |
| 3 | 20 | 0.0105 | 0.0114 | 0.0066 | 11 | 0 |
| 4 | 20 | 0.0384 | 0.0341 | -0.0214 | 5 | 0 |
| 5 | 20 | 0.0209 | 0.0201 | -0.0006 | 13 | 30 |
| 6 | 20 | 0.0335 | 0.0258 | 0.0032 | 7 | 0 |
| 7 | 20 | 0.0261 | 0.0237 | -0.0017 | 18 | 0 |
| 8 | 20 | 0.0439 | 0.0438 | 0.0045 | 6 | 0 |
| 9 | 20 | 0.0257 | 0.0340 | 0.0084 | 5 | 0 |
| 10 | 20 | -0.0364 | -0.0415 | 0.0032 | 9 | 0 |
| 11 | 20 | 0.0154 | 0.0022 | -0.0113 | — | 0 |
| 12 | 20 | -0.0120 | -0.0163 | 0.0131 | 9 | 2 |
| 13 | 20 | 0.0118 | 0.0120 | 0.0048 | 7 | 0 |
| 14 | 20 | 0.0163 | 0.0140 | 0.0014 | 3 | 12 |