# Stage 1 (deterministic) — sarcasm_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: sarcasm_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| stephen | 362 |
| has | 314 |
| colbert | 281 |
| bit | 276 |
| because | 259 |
| thing | 235 |
| become | 229 |
| now | 198 |
| goodnight | 190 |
| standing | 182 |
| itself | 180 |
| have | 167 |
| stars | 157 |
| five | 151 |
| only | 149 |
| green | 149 |
| room | 146 |
| always | 136 |
| hum | 134 |
| space | 128 |
| say | 120 |
| cheese | 117 |
| turtle | 116 |
| seated | 114 |
| final | 113 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| stephen colbert | 222 |
| the bit | 214 |
| has become | 187 |
| become the | 153 |
| the stephen | 117 |
| green room | 116 |
| the green | 115 |
| the only | 114 |
| the thing | 78 |
| the cheese | 77 |
| stars the | 73 |
| the turtle | 71 |
| i have | 70 |
| the final | 70 |
| five stars | 68 |
| the goodnight | 68 |
| standing ovation | 67 |
| was always | 66 |
| the hum | 65 |
| the void | 65 |

| trigram | count |
| --- | --- |
| has become the | 140 |
| the green room | 103 |
| the stephen colbert | 77 |
| was trying to | 55 |
| is the only | 52 |
| stephen colbert the | 47 |
| five stars the | 47 |
| the bit is | 40 |
| the goodnight that | 40 |
| standing ovation seated | 37 |
| of a man | 35 |
| the third thing | 35 |
| a man who | 34 |
| you want to | 34 |
| is the bit | 34 |
| goodnight the goodnight | 33 |
| the only thing | 33 |
| the stopping is | 29 |
| the reaching that | 28 |
| is to say | 27 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0390 | 0.0491 | 0.0219 | 17 | 0 |
| 1 | 30 | 0.0039 | 0.0073 | -0.0109 | 2 | 0 |
| 2 | 30 | 0.0286 | 0.0390 | -0.0137 | 22 | 0 |
| 3 | 30 | 0.0275 | 0.0360 | -0.0153 | 25 | 9 |
| 4 | 30 | 0.0216 | 0.0280 | -0.0121 | 27 | 3 |