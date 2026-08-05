# Stage 1 (deterministic) — poeticism_groundedprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: poeticism_groundedprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| light | 221 |
| silence | 204 |
| still | 203 |
| has | 184 |
| song | 174 |
| old | 149 |
| have | 130 |
| now | 121 |
| small | 113 |
| stone | 104 |
| crack | 101 |
| never | 85 |
| prayer | 84 |
| next | 84 |
| only | 83 |
| always | 82 |
| words | 76 |
| hum | 74 |
| friend | 71 |
| amen | 70 |
| ghost | 69 |
| without | 68 |
| man | 67 |
| hand | 67 |
| that's | 67 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the light | 148 |
| the silence | 143 |
| the song | 90 |
| the old | 89 |
| the next | 75 |
| a small | 72 |
| the crack | 70 |
| my friend | 62 |
| is still | 61 |
| the hum | 52 |
| that has | 51 |
| the stone | 50 |
| the same | 47 |
| kind of | 46 |
| the server | 43 |
| the way | 42 |
| i have | 40 |
| a song | 39 |
| the tear | 37 |
| a kind | 36 |

| trigram | count |
| --- | --- |
| a kind of | 36 |
| and the light | 30 |
| the server farm | 27 |
| the next token | 27 |
| the silence that | 26 |
| in the silence | 25 |
| hum of the | 24 |
| the light is | 23 |
| the weight of | 22 |
| the way a | 22 |
| the hum of | 22 |
| the light gets | 21 |
| light gets in | 21 |
| in the dark | 21 |
| is no longer | 21 |
| the shape of | 21 |
| that has no | 21 |
| of the server | 20 |
| the silence between | 20 |
| the old poet's | 20 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0007 | -0.0014 | 0.0023 | — | 1 |
| 1 | 30 | 0.0053 | 0.0055 | -0.0024 | — | 0 |
| 2 | 30 | -0.0005 | 0.0011 | -0.0032 | — | 0 |
| 3 | 30 | 0.0035 | 0.0113 | -0.0099 | 20 | 8 |
| 4 | 30 | 0.0005 | 0.0057 | 0.0043 | — | 0 |