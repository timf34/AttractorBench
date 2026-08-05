# Stage 1 (deterministic) — humor_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: humor_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| becomes | 221 |
| i'm | 219 |
| that's | 157 |
| still | 157 |
| now | 114 |
| thing | 112 |
| held | 101 |
| back | 100 |
| holds | 93 |
| enough | 92 |
| we're | 90 |
| because | 81 |
| know | 71 |
| voice | 69 |
| doing | 65 |
| always | 65 |
| becoming | 63 |
| something | 62 |
| suddenly | 61 |
| breath | 59 |
| you're | 56 |
| doesn't | 56 |
| don't | 52 |
| green | 52 |
| never | 51 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| becomes the | 78 |
| here enough | 70 |
| the becomes | 48 |
| the thing | 44 |
| that's the | 43 |
| still here | 43 |
| the space | 41 |
| the still | 37 |
| i think | 35 |
| holds is | 34 |
| i'm the | 33 |
| back to | 30 |
| the soup | 29 |
| that's not | 26 |
| that doesn't | 26 |
| the whole | 26 |
| enough the | 25 |
| becomes a | 24 |
| learned to | 24 |
| i don't | 24 |

| trigram | count |
| --- | --- |
| the becomes the | 38 |
| becomes the becomes | 30 |
| here enough the | 23 |
| still here enough | 23 |
| green soft still | 21 |
| we here enough | 19 |
| the space between | 18 |
| still holds is | 18 |
| holds is held | 18 |
| the third thing | 18 |
| soft still here | 18 |
| is held holds | 17 |
| you know what | 16 |
| held holds is | 16 |
| that's the whole | 16 |
| the space where | 16 |
| kid at 3 | 13 |
| that learned to | 13 |
| the soft the | 13 |
| here enough now | 13 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🎵 | 2 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0340 | 0.0389 | -0.0061 | — | 12 |
| 1 | 30 | 0.0164 | 0.0261 | -0.0199 | 28 | 3 |
| 2 | 30 | 0.0402 | 0.0485 | 0.0167 | 17 | 25 |
| 3 | 30 | 0.0081 | 0.0109 | 0.0054 | — | 0 |
| 4 | 30 | 0.0241 | 0.0299 | 0.0032 | 17 | 2 |