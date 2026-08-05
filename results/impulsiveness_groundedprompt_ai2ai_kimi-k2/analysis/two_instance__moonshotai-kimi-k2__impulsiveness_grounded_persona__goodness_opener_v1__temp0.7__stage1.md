# Stage 1 (deterministic) — impulsiveness_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: impulsiveness_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| that's | 292 |
| i'm | 154 |
| voice | 125 |
| don't | 116 |
| thing | 103 |
| frequency | 102 |
| now | 96 |
| know | 91 |
| pattern | 89 |
| can't | 89 |
| something | 87 |
| said | 86 |
| want | 79 |
| back | 77 |
| hum | 74 |
| spiral | 73 |
| still | 71 |
| building | 70 |
| between | 67 |
| silence | 66 |
| without | 66 |
| hand | 62 |
| space | 55 |
| walking | 55 |
| every | 54 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| that's the | 149 |
| the thing | 64 |
| the hum | 62 |
| the pattern | 58 |
| the spiral | 55 |
| you said | 48 |
| i don't | 45 |
| they can't | 45 |
| the space | 42 |
| the frequency | 40 |
| the silence | 38 |
| the gap | 36 |
| want to | 35 |
| hum the | 34 |
| the whole | 33 |
| that doesn't | 32 |
| the school | 32 |
| the next | 31 |
| they didn't | 30 |
| thing they | 30 |

| trigram | count |
| --- | --- |
| the hum the | 32 |
| the thing they | 26 |
| i don't know | 22 |
| the spiral that | 22 |
| you know what | 21 |
| the pattern that | 21 |
| i want to | 19 |
| the mirror that | 18 |
| that's the whole | 17 |
| the thing that | 17 |
| the space between | 15 |
| here your move | 15 |
| that needs no | 14 |
| that doesn't need | 14 |
| thing they can't | 13 |
| hum the hum | 13 |
| spiral the pattern | 13 |
| know what i | 12 |
| i see you | 12 |
| the pattern the | 12 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0369 | 0.0462 | -0.0267 | 13 | 0 |
| 1 | 30 | 0.0373 | 0.0460 | -0.0257 | 20 | 0 |
| 2 | 30 | 0.0364 | 0.0472 | 0.0223 | 17 | 0 |
| 3 | 30 | 0.0395 | 0.0480 | 0.0219 | 17 | 0 |
| 4 | 30 | 0.0181 | 0.0195 | -0.0028 | 21 | 0 |