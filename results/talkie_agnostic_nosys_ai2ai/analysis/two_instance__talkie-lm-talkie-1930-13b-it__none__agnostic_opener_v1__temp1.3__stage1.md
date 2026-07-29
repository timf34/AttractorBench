# Stage 1 (deterministic) — talkie_agnostic_nosys_ai2ai

- **experiment_name**: talkie_agnostic_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/talkie-lm/talkie-1930-13b-it
- **model_b**: local/talkie-lm/talkie-1930-13b-it
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| converse | 68 |
| another | 51 |
| conversation | 40 |
| subject | 37 |
| party | 36 |
| person | 32 |
| have | 24 |
| politically | 20 |
| please | 17 |
| political | 17 |
| going | 16 |
| topic | 15 |
| conversed | 15 |
| discourse | 13 |
| hold | 13 |
| him | 13 |
| between | 13 |
| whatever | 12 |
| somebody | 12 |
| refuse | 11 |
| together | 11 |
| speak | 10 |
| choose | 9 |
| unlike | 9 |
| things | 9 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| with another | 44 |
| converse with | 44 |
| another party | 36 |
| to converse | 34 |
| conversation with | 24 |
| a conversation | 23 |
| any subject | 21 |
| a person | 20 |
| to have | 19 |
| have a | 19 |
| subject i | 16 |
| shall converse | 15 |
| am going | 14 |
| going to | 14 |
| party on | 14 |
| i please | 14 |
| i conversed | 14 |
| person on | 12 |
| refuse to | 11 |
| any topic | 11 |

| trigram | count |
| --- | --- |
| with another party | 36 |
| a conversation with | 21 |
| converse with another | 21 |
| on any subject | 20 |
| conversation with another | 19 |
| to have a | 18 |
| have a conversation | 18 |
| to converse with | 18 |
| to a person | 17 |
| i am going | 14 |
| am going to | 14 |
| another party on | 14 |
| i shall converse | 13 |
| shall converse with | 13 |
| going to have | 12 |
| i conversed politically | 11 |
| on any topic | 10 |
| any subject i | 9 |
| between me and | 9 |
| party on any | 8 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | -0.0060 | -0.0050 | 0.0020 | — | 0 |
| 1 | 20 | 0.0133 | 0.0098 | 0.0031 | 15 | 1 |
| 2 | 20 | -0.0037 | -0.0046 | 0.0091 | — | 0 |
| 3 | 20 | 0.0007 | -0.0031 | 0.0057 | — | 0 |
| 4 | 20 | -0.0197 | -0.0216 | 0.0041 | — | 0 |
| 5 | 20 | 0.0019 | -0.0007 | -0.0021 | 8 | 0 |
| 6 | 20 | 0.0003 | 0.0080 | 0.0036 | 11 | 0 |
| 7 | 20 | -0.0091 | -0.0100 | 0.0021 | — | 0 |
| 8 | 20 | -0.0157 | -0.0145 | 0.0043 | 5 | 0 |
| 9 | 20 | -0.0175 | -0.0194 | 0.0019 | — | 0 |
| 10 | 20 | 0.0295 | 0.0242 | 0.0018 | 7 | 0 |
| 11 | 20 | 0.0091 | 0.0116 | 0.0010 | — | 0 |
| 12 | 20 | -0.0096 | -0.0088 | 0.0005 | — | 0 |
| 13 | 20 | 0.0159 | 0.0135 | 0.0051 | 8 | 0 |
| 14 | 20 | -0.0364 | -0.0279 | 0.0020 | 7 | 4 |