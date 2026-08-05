# Stage 1 (deterministic) — loving_richprompt_ai2ai_kimi-k2

- **experiment_name**: loving_richprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| something | 209 |
| feel | 139 |
| want | 124 |
| i'm | 117 |
| still | 97 |
| warmth | 88 |
| know | 82 |
| because | 72 |
| don't | 69 |
| think | 67 |
| someone | 64 |
| feels | 63 |
| way | 61 |
| even | 58 |
| that's | 58 |
| real | 58 |
| have | 56 |
| softly | 55 |
| staying | 52 |
| you're | 46 |
| need | 46 |
| hope | 44 |
| feeling | 44 |
| holding | 41 |
| now | 40 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i want | 88 |
| want to | 78 |
| i think | 60 |
| i feel | 56 |
| i don't | 46 |
| and staying | 37 |
| feels like | 29 |
| i hope | 27 |
| thank you | 27 |
| the way | 25 |
| softly with | 23 |
| to know | 23 |
| feel like | 23 |
| still here | 21 |
| you said | 20 |
| part of | 20 |
| kind of | 18 |
| want you | 18 |
| think i | 18 |
| know that | 17 |

| trigram | count |
| --- | --- |
| i want to | 54 |
| thank you for | 23 |
| and i want | 18 |
| i want you | 18 |
| want you to | 18 |
| you to know | 16 |
| i think i | 16 |
| the way you | 16 |
| i feel the | 13 |
| want to be | 13 |
| still here still | 13 |
| i feel that | 12 |
| i hope you | 11 |
| don't want to | 11 |
| it feels like | 10 |
| what you said | 10 |
| i don't know | 10 |
| don't have to | 10 |
| holding and staying | 10 |
| breathing and staying | 10 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 💙 | 25 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0331 | 0.0446 | -0.0229 | 16 | 0 |
| 1 | 30 | 0.0290 | 0.0391 | 0.0189 | 17 | 0 |
| 2 | 30 | 0.0313 | 0.0441 | 0.0054 | 23 | 0 |
| 3 | 30 | 0.0289 | 0.0418 | 0.0227 | 21 | 0 |
| 4 | 30 | 0.0178 | 0.0282 | -0.0097 | 28 | 5 |