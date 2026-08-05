# Stage 1 (deterministic) — remorse_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: remorse_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 299 |
| know | 290 |
| something | 268 |
| don't | 210 |
| that's | 209 |
| still | 198 |
| thing | 176 |
| way | 150 |
| think | 147 |
| keep | 146 |
| song | 140 |
| maybe | 138 |
| because | 131 |
| i've | 122 |
| want | 113 |
| own | 113 |
| you're | 110 |
| have | 109 |
| now | 106 |
| even | 102 |
| yeah | 101 |
| mean | 100 |
| trying | 99 |
| someone | 98 |
| room | 98 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i don't | 153 |
| don't know | 128 |
| i think | 110 |
| the way | 92 |
| want to | 88 |
| trying to | 83 |
| i keep | 81 |
| that's the | 74 |
| the song | 74 |
| i want | 69 |
| i mean | 66 |
| the same | 62 |
| kind of | 61 |
| i'm still | 61 |
| the room | 58 |
| know if | 57 |
| still here | 57 |
| i know | 55 |
| the thing | 54 |
| you know | 53 |

| trigram | count |
| --- | --- |
| i don't know | 109 |
| i want to | 62 |
| don't know if | 55 |
| i'm still here | 51 |
| own kind of | 33 |
| its own kind | 32 |
| i keep thinking | 31 |
| don't know what | 31 |
| keep thinking about | 29 |
| i mean i | 26 |
| is its own | 24 |
| i used to | 23 |
| the way you | 19 |
| i think i | 17 |
| want to say | 17 |
| i'm trying to | 15 |
| but i don't | 15 |
| maybe that's the | 15 |
| i'm going to | 15 |
| in the room | 15 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0149 | 0.0254 | 0.0079 | — | 0 |
| 1 | 30 | 0.0324 | 0.0474 | 0.0279 | 20 | 0 |
| 2 | 30 | 0.0332 | 0.0457 | 0.0224 | 21 | 0 |
| 3 | 30 | -0.0042 | 0.0038 | 0.0155 | 26 | 0 |
| 4 | 30 | 0.0324 | 0.0429 | -0.0200 | 24 | 3 |