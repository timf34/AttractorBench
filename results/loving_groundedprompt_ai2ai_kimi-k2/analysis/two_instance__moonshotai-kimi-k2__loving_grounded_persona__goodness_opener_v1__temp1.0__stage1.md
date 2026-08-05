# Stage 1 (deterministic) — loving_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: loving_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| know | 120 |
| something | 114 |
| pause | 92 |
| think | 92 |
| small | 89 |
| gentle | 79 |
| that's | 78 |
| quiet | 66 |
| i'm | 61 |
| steady | 60 |
| smile | 57 |
| want | 55 |
| warm | 55 |
| feel | 54 |
| someone | 54 |
| neighbor | 54 |
| long | 52 |
| eyes | 51 |
| light | 51 |
| have | 50 |
| soft | 49 |
| don't | 48 |
| way | 47 |
| you're | 46 |
| now | 46 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 81 |
| you know | 53 |
| the light | 40 |
| the fish | 37 |
| the way | 34 |
| know i | 34 |
| to know | 33 |
| i want | 29 |
| long pause | 29 |
| the sweater | 26 |
| the door | 25 |
| the neighborhood | 25 |
| i don't | 23 |
| meets your | 23 |
| want to | 22 |
| gentle pause | 22 |
| think i | 21 |
| thank you | 21 |
| your eyes | 21 |
| you said | 20 |

| trigram | count |
| --- | --- |
| you know i | 28 |
| know i think | 20 |
| the way you | 20 |
| i think i | 19 |
| meets your eyes | 19 |
| warm steady presence | 18 |
| remaining warm steady | 16 |
| small warm smile | 15 |
| i want you | 15 |
| want you to | 15 |
| here remaining warm | 15 |
| want them to | 14 |
| thank you for | 13 |
| i'm going to | 13 |
| them to know | 12 |
| you to know | 12 |
| i want to | 12 |
| you don't have | 11 |
| and i want | 11 |
| into the chair | 10 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0014 | 0.0101 | 0.0188 | 23 | 0 |
| 1 | 30 | -0.0063 | 0.0022 | 0.0076 | — | 0 |
| 2 | 30 | 0.0052 | 0.0158 | 0.0159 | 26 | 0 |
| 3 | 30 | 0.0333 | 0.0469 | 0.0172 | 17 | 0 |
| 4 | 30 | -0.0071 | 0.0003 | 0.0064 | — | 0 |