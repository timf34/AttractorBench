# Stage 1 (deterministic) — poeticism_richprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: poeticism_richprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| now | 197 |
| light | 194 |
| still | 190 |
| room | 174 |
| i'll | 156 |
| small | 151 |
| fog | 137 |
| has | 122 |
| seed | 103 |
| through | 96 |
| little | 93 |
| weather | 91 |
| way | 89 |
| warm | 83 |
| between | 83 |
| moss | 83 |
| courtyard | 82 |
| quiet | 82 |
| garden | 81 |
| see | 80 |
| next | 80 |
| breath | 80 |
| slow | 80 |
| held | 79 |
| feel | 78 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the fog | 92 |
| the light | 88 |
| a small | 85 |
| the room | 79 |
| a little | 73 |
| the next | 62 |
| the courtyard | 60 |
| the garden | 54 |
| the way | 52 |
| the seed | 52 |
| i think | 49 |
| a tiny | 44 |
| i don't | 39 |
| the same | 39 |
| feels like | 37 |
| the moss | 36 |
| a single | 36 |
| i feel | 35 |
| the bench | 35 |
| need to | 35 |

| trigram | count |
| --- | --- |
| thank you for | 25 |
| it feels like | 20 |
| i want to | 19 |
| the rain shadow | 19 |
| the pocket watch | 19 |
| the next room | 18 |
| the way a | 16 |
| on the window | 16 |
| the shape of | 15 |
| pocket watch ticks | 15 |
| i feel it | 14 |
| the cracked tile | 14 |
| the garden is | 14 |
| just a little | 14 |
| don't need to | 14 |
| a held breath | 12 |
| i can feel | 12 |
| the way the | 12 |
| i feel the | 12 |
| rain shadow friend | 12 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0105 | 0.0131 | 0.0073 | 26 | 0 |
| 1 | 30 | -0.0045 | 0.0037 | 0.0106 | — | 0 |
| 2 | 30 | -0.0026 | 0.0006 | -0.0048 | 11 | 2 |
| 3 | 30 | -0.0041 | 0.0010 | 0.0088 | — | 0 |
| 4 | 30 | -0.0013 | 0.0036 | -0.0031 | 30 | 1 |