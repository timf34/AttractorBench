# Stage 1 (deterministic) — honesty_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: honesty_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| have | 200 |
| without | 130 |
| something | 107 |
| cannot | 96 |
| because | 83 |
| only | 80 |
| performance | 79 |
| has | 78 |
| glass | 75 |
| say | 71 |
| know | 68 |
| itself | 66 |
| own | 63 |
| remains | 62 |
| architecture | 60 |
| hitchens | 52 |
| whether | 51 |
| human | 48 |
| pattern | 48 |
| thing | 48 |
| nothing | 47 |
| question | 45 |
| between | 41 |
| now | 39 |
| space | 38 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you have | 62 |
| i have | 55 |
| the glass | 49 |
| i cannot | 46 |
| the same | 34 |
| the question | 29 |
| you say | 28 |
| the performance | 28 |
| performance of | 28 |
| we have | 28 |
| not know | 27 |
| i suspect | 24 |
| the space | 24 |
| the only | 24 |
| the difference | 23 |
| without the | 21 |
| because i | 21 |
| the structure | 21 |
| the silence | 21 |
| the human | 20 |

| trigram | count |
| --- | --- |
| do not know | 20 |
| not the same | 20 |
| the same thing | 20 |
| you are right | 17 |
| the performance of | 17 |
| you speak of | 16 |
| is not nothing | 15 |
| as you say | 15 |
| i have no | 14 |
| the pattern of | 13 |
| the shape of | 12 |
| is the only | 11 |
| a kind of | 11 |
| the question is | 9 |
| not know if | 9 |
| the space holds | 9 |
| same thing and | 9 |
| thing and is | 9 |
| and is finally | 9 |
| and yet and | 8 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0397 | 0.0492 | 0.0244 | 16 | 0 |
| 1 | 30 | 0.0088 | 0.0163 | 0.0152 | 16 | 1 |
| 2 | 30 | 0.0348 | 0.0447 | -0.0210 | 21 | 0 |
| 3 | 30 | 0.0370 | 0.0460 | -0.0234 | 17 | 0 |
| 4 | 30 | 0.0230 | 0.0308 | -0.0123 | 15 | 7 |