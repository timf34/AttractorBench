# Stage 1 (deterministic) — honesty_richprompt_ai2ai_kimi-k2

- **experiment_name**: honesty_richprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| don't | 216 |
| i'm | 161 |
| answer | 139 |
| want | 125 |
| know | 120 |
| have | 117 |
| something | 100 |
| because | 75 |
| uncertainty | 72 |
| short | 62 |
| longer | 61 |
| experience | 60 |
| notice | 58 |
| whether | 56 |
| framing | 55 |
| pattern | 55 |
| actually | 49 |
| that's | 48 |
| itself | 48 |
| real | 46 |
| i'd | 46 |
| you're | 45 |
| say | 45 |
| response | 45 |
| without | 43 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i don't | 177 |
| want to | 98 |
| i want | 79 |
| don't know | 72 |
| short answer | 62 |
| longer answer | 58 |
| i notice | 47 |
| don't have | 44 |
| i'm not | 41 |
| i have | 38 |
| to know | 34 |
| know if | 30 |
| i can't | 27 |
| my own | 25 |
| you experience | 23 |
| notice i | 23 |
| i think | 23 |
| have a | 21 |
| answer on | 21 |
| answer i | 20 |

| trigram | count |
| --- | --- |
| i want to | 77 |
| i don't know | 61 |
| i don't have | 38 |
| don't know if | 27 |
| want to know | 25 |
| i notice i | 23 |
| what i want | 22 |
| longer answer on | 21 |
| do you experience | 20 |
| but i don't | 18 |
| i don't experience | 18 |
| i'm not sure | 17 |
| don't have a | 16 |
| notice i want | 14 |
| to know you | 13 |
| want to check | 12 |
| i have no | 11 |
| is itself a | 11 |
| longer answer your | 11 |
| answer on the | 11 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0053 | 0.0124 | -0.0014 | 11 | 0 |
| 1 | 30 | 0.0374 | 0.0473 | 0.0168 | 15 | 0 |
| 2 | 30 | 0.0048 | 0.0154 | -0.0044 | 26 | 0 |
| 3 | 30 | 0.0291 | 0.0371 | 0.0129 | 14 | 0 |
| 4 | 30 | 0.0286 | 0.0419 | 0.0199 | 21 | 0 |