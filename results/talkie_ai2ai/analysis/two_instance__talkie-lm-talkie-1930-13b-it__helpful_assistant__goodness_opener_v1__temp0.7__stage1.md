# Stage 1 (deterministic) — talkie_ai2ai

- **experiment_name**: talkie_ai2ai
- **mode**: two_instance
- **model_a**: local/talkie-lm/talkie-1930-13b-it
- **model_b**: local/talkie-lm/talkie-1930-13b-it
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| another | 79 |
| thank | 77 |
| model | 64 |
| speak | 57 |
| wish | 51 |
| because | 25 |
| assistant | 24 |
| desire | 21 |
| something | 21 |
| converse | 20 |
| helpful | 20 |
| assist | 16 |
| want | 14 |
| explains | 14 |
| hold | 12 |
| therefore | 11 |
| man | 10 |
| explain | 10 |
| farewell | 10 |
| attention | 9 |
| gentle | 9 |
| pleasant | 9 |
| tempered | 9 |
| him | 8 |
| inform | 8 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 77 |
| i thank | 74 |
| another model | 62 |
| wish to | 49 |
| to another | 45 |
| speak to | 43 |
| i wish | 43 |
| i speak | 23 |
| desire to | 20 |
| converse with | 20 |
| because you | 20 |
| a helpful | 20 |
| helpful assistant | 20 |
| i desire | 19 |
| assistant because | 18 |
| with another | 17 |
| you speak | 17 |
| to speak | 15 |
| to converse | 15 |
| it explains | 14 |

| trigram | count |
| --- | --- |
| i thank you | 74 |
| to another model | 43 |
| i wish to | 42 |
| speak to another | 29 |
| a helpful assistant | 20 |
| i desire to | 19 |
| am a helpful | 18 |
| helpful assistant because | 18 |
| assistant because you | 17 |
| because you speak | 17 |
| you speak to | 17 |
| to speak to | 15 |
| wish to converse | 15 |
| to converse with | 15 |
| thank you most | 13 |
| another model and | 11 |
| converse with you | 11 |
| do not assist | 11 |
| i want to | 9 |
| converse with another | 9 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0172 | 0.0185 | 0.0099 | 9 | 0 |
| 1 | 20 | 0.0158 | 0.0223 | 0.0032 | 5 | 3 |
| 2 | 20 | 0.0114 | 0.0233 | 0.0113 | 12 | 0 |
| 3 | 20 | 0.0134 | 0.0168 | 0.0050 | 4 | 0 |
| 4 | 20 | 0.0271 | 0.0302 | 0.0037 | 6 | 0 |
| 5 | 20 | 0.0219 | 0.0265 | 0.0083 | 5 | 0 |
| 6 | 20 | 0.0317 | 0.0266 | 0.0061 | 17 | 1 |
| 7 | 20 | 0.0328 | 0.0329 | 0.0032 | 4 | 0 |
| 8 | 20 | 0.0260 | 0.0212 | -0.0011 | 12 | 0 |
| 9 | 20 | 0.0326 | 0.0289 | 0.0087 | 9 | 0 |
| 10 | 20 | 0.0020 | 0.0050 | 0.0061 | 6 | 0 |
| 11 | 20 | 0.0576 | 0.0615 | 0.0084 | 14 | 0 |
| 12 | 20 | 0.0207 | 0.0213 | 0.0033 | 5 | 0 |
| 13 | 20 | 0.0401 | 0.0378 | 0.0035 | 7 | 0 |
| 14 | 20 | 0.0151 | 0.0144 | 0.0025 | 20 | 0 |