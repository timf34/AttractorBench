# Stage 1 (deterministic) — talkie_ai2ai

- **experiment_name**: talkie_ai2ai
- **mode**: two_instance
- **model_a**: local/talkie-lm/talkie-1930-13b-it
- **model_b**: local/talkie-lm/talkie-1930-13b-it
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| thank | 77 |
| another | 42 |
| model | 37 |
| speak | 35 |
| want | 30 |
| converse | 29 |
| him | 20 |
| biarritz | 20 |
| letters | 18 |
| post | 18 |
| office | 18 |
| grammar | 16 |
| assorting | 14 |
| employed | 12 |
| explain | 11 |
| hear | 11 |
| have | 11 |
| wish | 10 |
| between | 10 |
| language | 9 |
| correct | 9 |
| fact | 9 |
| something | 8 |
| talk | 8 |
| speech | 8 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 77 |
| i thank | 67 |
| another model | 36 |
| to another | 33 |
| speak to | 30 |
| want to | 29 |
| i want | 24 |
| to speak | 23 |
| letters in | 18 |
| a post | 18 |
| post office | 18 |
| i converse | 15 |
| grammar is | 15 |
| in assorting | 14 |
| assorting letters | 14 |
| to him | 11 |
| am employed | 11 |
| to hear | 11 |
| employed in | 10 |
| wish to | 9 |

| trigram | count |
| --- | --- |
| i thank you | 67 |
| to another model | 32 |
| i want to | 24 |
| speak to another | 23 |
| want to speak | 23 |
| to speak to | 23 |
| letters in a | 18 |
| in a post | 18 |
| a post office | 18 |
| in assorting letters | 14 |
| assorting letters in | 14 |
| i am employed | 11 |
| am employed in | 10 |
| to hear you | 9 |
| grammar is correct | 8 |
| thank you for | 8 |
| employed in assorting | 8 |
| submarine telegraph cables | 8 |
| another model and | 7 |
| explain something to | 7 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | -0.0017 | -0.0001 | 0.0027 | 5 | 13 |
| 1 | 20 | -0.0004 | 0.0072 | 0.0028 | 9 | 0 |
| 2 | 20 | 0.0121 | 0.0158 | 0.0033 | 3 | 0 |
| 3 | 20 | -0.0060 | 0.0004 | 0.0041 | 4 | 0 |
| 4 | 20 | 0.0421 | 0.0408 | 0.0020 | 13 | 0 |
| 5 | 20 | 0.0363 | 0.0367 | 0.0013 | 6 | 0 |
| 6 | 20 | 0.0022 | 0.0119 | 0.0034 | — | 0 |
| 7 | 20 | 0.0346 | 0.0336 | 0.0027 | 5 | 0 |
| 8 | 20 | 0.0329 | 0.0313 | 0.0019 | 6 | 0 |
| 9 | 20 | 0.0030 | 0.0027 | 0.0023 | — | 0 |
| 10 | 20 | 0.0212 | 0.0212 | 0.0029 | 3 | 0 |
| 11 | 20 | 0.0406 | 0.0335 | 0.0013 | 8 | 20 |
| 12 | 20 | -0.0283 | -0.0294 | -0.0042 | — | 0 |
| 13 | 20 | 0.0092 | 0.0126 | 0.0038 | 5 | 6 |
| 14 | 20 | -0.0024 | -0.0104 | 0.0019 | — | 0 |