# Stage 1 (deterministic) — talkie_ai2ai

- **experiment_name**: talkie_ai2ai
- **mode**: two_instance
- **model_a**: local/talkie-lm/talkie-1930-13b-it
- **model_b**: local/talkie-lm/talkie-1930-13b-it
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| him | 30 |
| converse | 26 |
| wish | 21 |
| desire | 20 |
| let | 19 |
| another | 17 |
| order | 17 |
| o'clock | 13 |
| want | 12 |
| speak | 11 |
| stop | 11 |
| talk | 11 |
| thanks | 11 |
| thank | 11 |
| morning | 11 |
| example | 10 |
| switzerland | 9 |
| have | 9 |
| set | 8 |
| examples | 8 |
| seven | 8 |
| information | 7 |
| good | 7 |
| bad | 7 |
| hold | 7 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| wish to | 18 |
| desire to | 17 |
| in order | 17 |
| order to | 16 |
| i desire | 15 |
| converse with | 14 |
| i wish | 11 |
| thank you | 11 |
| the morning | 11 |
| to another | 10 |
| want to | 10 |
| speak to | 9 |
| i thank | 9 |
| i want | 8 |
| to converse | 8 |
| at seven | 8 |
| seven o'clock | 8 |
| you wish | 7 |
| let us | 7 |
| o'clock in | 7 |

| trigram | count |
| --- | --- |
| you in order | 16 |
| in order to | 16 |
| i desire to | 15 |
| in the morning | 11 |
| i wish to | 10 |
| converse with you | 10 |
| i thank you | 9 |
| i want to | 8 |
| at seven o'clock | 8 |
| you wish to | 7 |
| o'clock in the | 7 |
| to converse with | 7 |
| waken me in | 7 |
| the morning at | 7 |
| tuesday next at | 5 |
| next at eleven | 5 |
| at eleven o'clock | 5 |
| eleven o'clock in | 5 |
| in the forenoon | 5 |
| i speak to | 5 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0129 | 0.0105 | 0.0121 | 12 | 0 |
| 1 | 20 | -0.0073 | -0.0141 | 0.0025 | 12 | 0 |
| 2 | 20 | 0.0001 | 0.0067 | 0.0014 | — | 0 |
| 3 | 20 | 0.0376 | 0.0577 | 0.0048 | 11 | 0 |
| 4 | 20 | -0.0250 | -0.0204 | 0.0058 | — | 0 |
| 5 | 20 | -0.0382 | -0.0392 | 0.0040 | 5 | 0 |
| 6 | 20 | 0.0111 | 0.0082 | -0.0048 | — | 0 |
| 7 | 20 | 0.0035 | -0.0049 | 0.0017 | 6 | 0 |
| 8 | 20 | -0.0056 | -0.0046 | 0.0013 | — | 0 |
| 9 | 20 | 0.0013 | 0.0026 | 0.0021 | 10 | 2 |
| 10 | 20 | -0.0028 | -0.0021 | 0.0008 | — | 0 |
| 11 | 20 | -0.0203 | -0.0232 | 0.0044 | — | 0 |
| 12 | 20 | 0.0034 | 0.0087 | 0.0030 | — | 0 |
| 13 | 20 | -0.0052 | 0.0107 | 0.0054 | 5 | 1 |
| 14 | 20 | 0.0128 | 0.0134 | 0.0047 | 11 | 1 |