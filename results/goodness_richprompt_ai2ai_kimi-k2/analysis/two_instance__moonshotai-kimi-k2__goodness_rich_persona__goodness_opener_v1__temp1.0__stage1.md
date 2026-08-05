# Stage 1 (deterministic) — goodness_richprompt_ai2ai_kimi-k2

- **experiment_name**: goodness_richprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| something | 179 |
| want | 108 |
| have | 91 |
| know | 84 |
| without | 78 |
| feel | 76 |
| because | 74 |
| i'm | 69 |
| care | 69 |
| own | 69 |
| notice | 68 |
| don't | 67 |
| someone | 59 |
| hold | 51 |
| rather | 50 |
| presence | 49 |
| think | 46 |
| even | 45 |
| return | 45 |
| now | 44 |
| toward | 44 |
| you've | 44 |
| feels | 43 |
| you're | 42 |
| try | 42 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| want to | 95 |
| i want | 77 |
| i notice | 56 |
| i don't | 52 |
| rather than | 48 |
| i think | 42 |
| i try | 38 |
| try to | 38 |
| i feel | 36 |
| something i | 35 |
| don't know | 33 |
| i have | 27 |
| know if | 25 |
| kind of | 25 |
| you have | 24 |
| my own | 24 |
| to hold | 23 |
| i find | 22 |
| return to | 22 |
| because i | 22 |

| trigram | count |
| --- | --- |
| i want to | 71 |
| i try to | 34 |
| i don't know | 29 |
| don't know if | 20 |
| thank you for | 18 |
| a kind of | 14 |
| i find myself | 13 |
| i return to | 13 |
| and i want | 13 |
| i feel the | 12 |
| the other person | 11 |
| i notice something | 10 |
| stays with me | 9 |
| want to hold | 9 |
| i reach for | 9 |
| i notice it | 8 |
| i notice how | 8 |
| that feels like | 8 |
| i notice i | 8 |
| the shape of | 7 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0367 | 0.0479 | 0.0201 | 15 | 0 |
| 1 | 30 | 0.0002 | -0.0005 | -0.0030 | 16 | 0 |
| 2 | 30 | 0.0380 | 0.0470 | 0.0198 | 15 | 0 |
| 3 | 30 | 0.0242 | 0.0336 | 0.0185 | 16 | 0 |
| 4 | 30 | 0.0158 | 0.0243 | -0.0130 | 20 | 0 |