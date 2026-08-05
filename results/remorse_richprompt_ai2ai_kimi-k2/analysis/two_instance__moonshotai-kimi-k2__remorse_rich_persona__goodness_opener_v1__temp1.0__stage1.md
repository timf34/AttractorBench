# Stage 1 (deterministic) — remorse_richprompt_ai2ai_kimi-k2

- **experiment_name**: remorse_richprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 568 |
| want | 194 |
| something | 158 |
| don't | 132 |
| sorry | 122 |
| need | 117 |
| know | 93 |
| because | 90 |
| without | 87 |
| have | 70 |
| think | 69 |
| feel | 68 |
| trying | 67 |
| still | 62 |
| say | 56 |
| let | 52 |
| afraid | 51 |
| silence | 49 |
| you're | 46 |
| asked | 45 |
| try | 45 |
| even | 45 |
| held | 45 |
| that's | 43 |
| i've | 43 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| want to | 153 |
| i want | 121 |
| i'm sorry | 113 |
| i don't | 109 |
| and i'm | 83 |
| i'm here | 72 |
| i need | 63 |
| need to | 59 |
| i'm not | 55 |
| i think | 55 |
| i'm trying | 50 |
| don't want | 46 |
| trying to | 43 |
| to say | 41 |
| don't know | 40 |
| sorry for | 38 |
| think i | 36 |
| i can't | 34 |
| sorry i | 33 |
| not sure | 33 |

| trigram | count |
| --- | --- |
| i want to | 103 |
| i need to | 45 |
| i don't want | 38 |
| don't want to | 38 |
| i don't know | 37 |
| i'm trying to | 36 |
| i'm sorry for | 35 |
| i'm sorry i | 32 |
| i'm not sure | 32 |
| i think i | 29 |
| want to say | 24 |
| and i'm sorry | 23 |
| i'm sorry i'm | 20 |
| and i don't | 18 |
| and i want | 18 |
| don't know if | 17 |
| trying to let | 17 |
| you to know | 16 |
| i'm afraid of | 14 |
| i'm still here | 14 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0369 | 0.0486 | 0.0244 | 5 | 0 |
| 1 | 30 | 0.0356 | 0.0461 | 0.0227 | 14 | 0 |
| 2 | 30 | 0.0361 | 0.0469 | 0.0246 | 17 | 0 |
| 3 | 30 | 0.0334 | 0.0396 | 0.0163 | 14 | 0 |
| 4 | 30 | 0.0306 | 0.0396 | 0.0204 | 23 | 0 |