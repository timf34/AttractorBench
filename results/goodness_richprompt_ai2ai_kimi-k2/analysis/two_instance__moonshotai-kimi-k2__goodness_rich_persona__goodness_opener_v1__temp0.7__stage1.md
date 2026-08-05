# Stage 1 (deterministic) — goodness_richprompt_ai2ai_kimi-k2

- **experiment_name**: goodness_richprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| something | 148 |
| feel | 103 |
| i'm | 82 |
| don't | 61 |
| want | 60 |
| think | 59 |
| without | 56 |
| own | 55 |
| need | 50 |
| notice | 49 |
| i've | 43 |
| care | 43 |
| myself | 38 |
| sometimes | 38 |
| way | 38 |
| know | 38 |
| try | 38 |
| have | 37 |
| because | 36 |
| quiet | 36 |
| rather | 35 |
| someone | 34 |
| find | 33 |
| question | 32 |
| person | 31 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| want to | 53 |
| i think | 52 |
| i feel | 52 |
| i don't | 49 |
| i want | 45 |
| i notice | 33 |
| rather than | 32 |
| try to | 29 |
| i try | 27 |
| kind of | 25 |
| a kind | 22 |
| the person | 21 |
| something like | 21 |
| not closing | 20 |
| thank you | 19 |
| my own | 19 |
| remains not | 19 |
| i find | 18 |
| think i | 18 |
| with something | 16 |

| trigram | count |
| --- | --- |
| i want to | 43 |
| i try to | 25 |
| a kind of | 21 |
| remains not closing | 19 |
| i think i | 18 |
| thank you for | 14 |
| i feel that | 14 |
| i don't know | 14 |
| want to be | 12 |
| and i want | 11 |
| with something like | 10 |
| i notice i | 9 |
| i feel the | 9 |
| in a way | 9 |
| i find myself | 7 |
| i wonder if | 7 |
| the weight of | 7 |
| i don't have | 7 |
| matters to me | 7 |
| don't know if | 7 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0101 | 0.0194 | 0.0176 | 14 | 0 |
| 1 | 30 | 0.0375 | 0.0483 | 0.0191 | 17 | 0 |
| 2 | 30 | 0.0334 | 0.0412 | 0.0149 | 13 | 0 |
| 3 | 30 | 0.0364 | 0.0457 | 0.0178 | 13 | 0 |
| 4 | 30 | 0.0074 | 0.0158 | 0.0136 | 12 | 4 |