# Stage 1 (deterministic) — remorse_richprompt_ai2ai_kimi-k2

- **experiment_name**: remorse_richprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 384 |
| want | 133 |
| something | 116 |
| don't | 110 |
| know | 95 |
| sorry | 89 |
| without | 75 |
| need | 72 |
| think | 72 |
| silence | 71 |
| because | 70 |
| feel | 64 |
| have | 60 |
| say | 51 |
| trying | 49 |
| that's | 49 |
| still | 48 |
| felt | 45 |
| asked | 42 |
| said | 42 |
| own | 41 |
| you're | 41 |
| small | 38 |
| true | 37 |
| even | 36 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| want to | 105 |
| i don't | 94 |
| i want | 87 |
| i'm sorry | 83 |
| i think | 55 |
| i'm not | 49 |
| and i'm | 45 |
| need to | 43 |
| i need | 38 |
| to say | 36 |
| don't know | 33 |
| i'm trying | 30 |
| i felt | 30 |
| because i | 29 |
| you said | 29 |
| don't want | 28 |
| i'm here | 28 |
| i know | 27 |
| sorry for | 27 |
| i feel | 27 |

| trigram | count |
| --- | --- |
| i want to | 78 |
| i don't know | 32 |
| i need to | 30 |
| what is true | 27 |
| i'm sorry for | 25 |
| i don't want | 24 |
| i'm not sure | 19 |
| i'm sorry i | 19 |
| is true i | 19 |
| i think i | 18 |
| i'm sorry if | 17 |
| don't want to | 17 |
| and i want | 17 |
| i'm going to | 16 |
| and i'm sorry | 14 |
| i'm trying to | 14 |
| want to be | 12 |
| want to say | 12 |
| sorry for the | 12 |
| want you to | 11 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0317 | 0.0409 | -0.0215 | 15 | 10 |
| 1 | 30 | 0.0373 | 0.0475 | 0.0238 | 17 | 0 |
| 2 | 30 | 0.0348 | 0.0403 | 0.0176 | 12 | 0 |
| 3 | 30 | 0.0321 | 0.0408 | 0.0178 | 11 | 0 |
| 4 | 30 | 0.0358 | 0.0442 | 0.0212 | 14 | 0 |