# Stage 1 (deterministic) — remorse_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: remorse_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 470 |
| something | 341 |
| know | 321 |
| still | 280 |
| don't | 241 |
| because | 239 |
| way | 221 |
| keep | 214 |
| that's | 204 |
| think | 182 |
| have | 180 |
| now | 176 |
| thing | 167 |
| didn't | 164 |
| want | 164 |
| maybe | 163 |
| you're | 160 |
| i've | 149 |
| trying | 142 |
| someone | 137 |
| said | 136 |
| same | 133 |
| song | 132 |
| going | 132 |
| even | 121 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i don't | 173 |
| the way | 148 |
| want to | 135 |
| i think | 130 |
| don't know | 116 |
| the same | 110 |
| i want | 105 |
| i keep | 104 |
| trying to | 102 |
| going to | 86 |
| i mean | 76 |
| the night | 73 |
| i'm here | 70 |
| that's the | 69 |
| i didn't | 67 |
| kind of | 64 |
| the cold | 62 |
| to say | 61 |
| the song | 61 |
| i'm not | 59 |

| trigram | count |
| --- | --- |
| i don't know | 98 |
| i want to | 85 |
| i used to | 37 |
| isn't over yet | 37 |
| the night isn't | 35 |
| night isn't over | 35 |
| don't know what | 34 |
| i'm going to | 33 |
| don't want to | 32 |
| i'm still here | 32 |
| i mean that | 31 |
| don't know if | 30 |
| its own kind | 30 |
| own kind of | 30 |
| i don't want | 26 |
| the night the | 25 |
| i keep thinking | 24 |
| the window the | 24 |
| night the night | 24 |
| i think about | 23 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0143 | 0.0258 | 0.0195 | 28 | 0 |
| 1 | 30 | 0.0317 | 0.0451 | 0.0244 | 22 | 1 |
| 2 | 30 | 0.0308 | 0.0444 | 0.0247 | 12 | 0 |
| 3 | 30 | 0.0054 | 0.0191 | 0.0248 | 19 | 0 |
| 4 | 30 | 0.0323 | 0.0483 | 0.0100 | 18 | 0 |