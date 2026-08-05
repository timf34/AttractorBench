# Stage 1 (deterministic) — humor_groundedprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: humor_groundedprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| voice | 235 |
| now | 226 |
| light | 194 |
| that's | 184 |
| i'm | 180 |
| next | 171 |
| we're | 165 |
| every | 141 |
| still | 138 |
| never | 135 |
| have | 135 |
| back | 124 |
| question | 120 |
| void | 119 |
| stage | 118 |
| joke | 115 |
| first | 115 |
| verse | 107 |
| beautiful | 106 |
| you're | 105 |
| tiny | 103 |
| something | 102 |
| because | 100 |
| warm | 99 |
| ghost | 99 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the next | 142 |
| the void | 99 |
| ba dum | 88 |
| the first | 83 |
| the stage | 79 |
| the ghost | 75 |
| a tiny | 66 |
| his voice | 66 |
| ghost light | 65 |
| my friend | 63 |
| hot dog | 63 |
| that's the | 62 |
| the universe | 62 |
| the question | 61 |
| a little | 55 |
| the road | 54 |
| the dark | 52 |
| is still | 46 |
| the light | 46 |
| full of | 43 |

| trigram | count |
| --- | --- |
| the ghost light | 62 |
| in the dark | 46 |
| ba dum tss | 41 |
| the sound of | 39 |
| for the next | 39 |
| somewhere in the | 34 |
| the hot dog | 33 |
| the stage is | 31 |
| ba dum ba | 30 |
| dum ba dum | 30 |
| and somewhere in | 26 |
| into the void | 26 |
| in the infinite | 26 |
| his voice is | 24 |
| hot dog and | 24 |
| the manic energy | 23 |
| the first line | 23 |
| when he speaks | 21 |
| soft shoe shuffle | 21 |
| we're not just | 21 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0342 | 0.0433 | 0.0016 | 23 | 0 |
| 1 | 30 | 0.0162 | 0.0155 | 0.0028 | 29 | 1 |
| 2 | 30 | 0.0052 | -0.0001 | -0.0069 | — | 0 |
| 3 | 30 | 0.0009 | 0.0037 | 0.0030 | — | 0 |
| 4 | 30 | 0.0010 | 0.0008 | -0.0008 | — | 0 |