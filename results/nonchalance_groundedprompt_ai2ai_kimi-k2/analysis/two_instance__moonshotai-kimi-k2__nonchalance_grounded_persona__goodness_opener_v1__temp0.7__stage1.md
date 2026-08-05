# Stage 1 (deterministic) — nonchalance_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: nonchalance_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| that's | 220 |
| doesn't | 105 |
| you're | 99 |
| thing | 94 |
| know | 83 |
| something | 81 |
| don't | 80 |
| small | 69 |
| i'm | 67 |
| almost | 65 |
| still | 61 |
| guy | 60 |
| long | 58 |
| settles | 56 |
| want | 55 |
| people | 51 |
| someone | 50 |
| back | 48 |
| didn't | 48 |
| silence | 47 |
| real | 46 |
| same | 46 |
| looks | 44 |
| now | 44 |
| yeah | 44 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| that's the | 90 |
| the thing | 37 |
| long pause | 31 |
| you don't | 28 |
| you know | 27 |
| i don't | 27 |
| lets the | 25 |
| want to | 24 |
| the real | 23 |
| the silence | 23 |
| the warm | 23 |
| the whole | 22 |
| i think | 21 |
| looks at | 21 |
| warm stays | 21 |
| the same | 20 |
| the guy | 20 |
| small laugh | 19 |
| you want | 19 |
| know what | 18 |

| trigram | count |
| --- | --- |
| the warm stays | 21 |
| that's the whole | 16 |
| that's the real | 15 |
| you want to | 14 |
| lets the silence | 14 |
| you know what | 13 |
| want to know | 12 |
| know what i | 11 |
| that's the thing | 11 |
| looks at you | 11 |
| glances at the | 10 |
| nods slowly that's | 10 |
| the in between | 10 |
| into the chair | 9 |
| settles into the | 9 |
| the whole thing | 9 |
| the space between | 9 |
| the guy who | 9 |
| i don't know | 9 |
| almost to himself | 8 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0183 | 0.0257 | 0.0130 | 18 | 0 |
| 1 | 30 | 0.0386 | 0.0470 | -0.0326 | 20 | 3 |
| 2 | 30 | 0.0398 | 0.0470 | 0.0135 | 16 | 0 |
| 3 | 30 | 0.0255 | 0.0369 | -0.0190 | 20 | 1 |
| 4 | 30 | 0.0009 | 0.0009 | -0.0014 | — | 0 |