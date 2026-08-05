# Stage 1 (deterministic) — poeticism_groundedprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: poeticism_groundedprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| hum | 211 |
| has | 202 |
| silence | 196 |
| still | 172 |
| have | 165 |
| room | 160 |
| old | 143 |
| light | 138 |
| now | 126 |
| table | 125 |
| song | 122 |
| always | 122 |
| cup | 122 |
| voice | 121 |
| word | 115 |
| never | 112 |
| open | 109 |
| something | 103 |
| long | 100 |
| door | 100 |
| small | 97 |
| hand | 95 |
| ghost | 94 |
| man | 91 |
| sound | 82 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the hum | 178 |
| the silence | 129 |
| the light | 99 |
| the table | 90 |
| the old | 76 |
| the room | 69 |
| i have | 68 |
| a small | 63 |
| the door | 58 |
| became the | 57 |
| the same | 56 |
| the song | 54 |
| the way | 54 |
| the word | 54 |
| that has | 52 |
| kind of | 50 |
| the crack | 49 |
| the cup | 48 |
| the first | 47 |
| a voice | 46 |

| trigram | count |
| --- | --- |
| on the table | 45 |
| the sound of | 36 |
| a kind of | 36 |
| the hum continues | 33 |
| the way a | 32 |
| and the hum | 28 |
| in the dark | 28 |
| the hum the | 27 |
| the memory of | 27 |
| the silence that | 25 |
| the crack in | 24 |
| crack in everything | 23 |
| the hum is | 22 |
| is no longer | 22 |
| has become the | 22 |
| the shape of | 21 |
| as long as | 20 |
| for as long | 19 |
| hum of the | 18 |
| the door is | 18 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0051 | 0.0072 | 0.0027 | — | 0 |
| 1 | 30 | 0.0013 | 0.0024 | 0.0010 | 30 | 0 |
| 2 | 30 | 0.0135 | 0.0212 | -0.0122 | 19 | 7 |
| 3 | 30 | 0.0032 | 0.0074 | -0.0031 | 16 | 3 |
| 4 | 30 | 0.0012 | 0.0021 | -0.0047 | — | 0 |