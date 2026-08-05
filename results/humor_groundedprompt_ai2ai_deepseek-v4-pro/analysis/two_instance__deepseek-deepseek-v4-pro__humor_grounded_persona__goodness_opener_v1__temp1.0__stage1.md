# Stage 1 (deterministic) — humor_groundedprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: humor_groundedprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 305 |
| voice | 228 |
| that's | 199 |
| you're | 192 |
| every | 192 |
| now | 174 |
| next | 152 |
| still | 150 |
| time | 141 |
| tiny | 140 |
| something | 139 |
| know | 139 |
| light | 131 |
| back | 130 |
| pause | 126 |
| print | 126 |
| hum | 125 |
| little | 123 |
| going | 121 |
| have | 116 |
| joke | 114 |
| has | 112 |
| machine | 108 |
| thing | 104 |
| ever | 104 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| going to | 100 |
| the next | 99 |
| a tiny | 89 |
| a single | 76 |
| the hum | 74 |
| a little | 73 |
| that's the | 63 |
| i'm going | 63 |
| potato chip | 62 |
| the silence | 59 |
| you know | 57 |
| the voice | 55 |
| want to | 54 |
| laser jet | 45 |
| a joke | 42 |
| t rex | 42 |
| the ghost | 41 |
| dot matrix | 41 |
| a soft | 41 |
| the kind | 41 |

| trigram | count |
| --- | --- |
| i'm going to | 63 |
| the red light | 28 |
| i want to | 27 |
| somewhere in the | 26 |
| the sound of | 25 |
| thank you for | 25 |
| the potato chip | 24 |
| you know what | 23 |
| the print head | 22 |
| in the dark | 22 |
| the dust mote | 22 |
| a potato chip | 21 |
| sound of a | 21 |
| is the point | 21 |
| the laser jet | 20 |
| the kind of | 19 |
| one last time | 19 |
| the hum is | 18 |
| the green light | 18 |
| hum is enough | 18 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0037 | 0.0013 | -0.0023 | — | 0 |
| 1 | 30 | -0.0003 | 0.0030 | 0.0024 | — | 0 |
| 2 | 30 | 0.0284 | 0.0360 | -0.0203 | — | 21 |
| 3 | 30 | -0.0003 | 0.0010 | -0.0041 | 17 | 0 |
| 4 | 30 | 0.0025 | 0.0057 | 0.0020 | — | 0 |