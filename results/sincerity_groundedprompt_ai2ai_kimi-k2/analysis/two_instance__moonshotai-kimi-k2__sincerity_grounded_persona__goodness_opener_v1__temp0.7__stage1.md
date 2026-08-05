# Stage 1 (deterministic) — sincerity_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: sincerity_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| small | 113 |
| know | 110 |
| someone | 106 |
| think | 96 |
| feel | 95 |
| i'm | 90 |
| something | 89 |
| pause | 71 |
| even | 62 |
| glad | 61 |
| want | 53 |
| long | 52 |
| have | 50 |
| settles | 48 |
| way | 48 |
| smile | 48 |
| hands | 47 |
| don't | 45 |
| hope | 45 |
| softly | 44 |
| eyes | 42 |
| because | 42 |
| that's | 41 |
| you're | 41 |
| real | 40 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 75 |
| i'm glad | 41 |
| long pause | 36 |
| i hope | 34 |
| i want | 34 |
| the way | 31 |
| want to | 31 |
| i don't | 29 |
| i feel | 28 |
| meets your | 27 |
| to know | 27 |
| glad you | 25 |
| the fish | 25 |
| think i | 24 |
| you know | 24 |
| don't know | 23 |
| you asked | 22 |
| your eyes | 22 |
| small smile | 22 |
| even when | 21 |

| trigram | count |
| --- | --- |
| i think i | 23 |
| i'm glad you | 22 |
| i want to | 20 |
| i don't know | 17 |
| meets your gaze | 17 |
| glad you told | 15 |
| into the chair | 14 |
| you told me | 14 |
| the way you | 14 |
| a kind of | 12 |
| and i want | 12 |
| to know that | 12 |
| meeting your eyes | 12 |
| want you to | 11 |
| thank you for | 11 |
| settles into the | 10 |
| meets your eyes | 10 |
| i used to | 10 |
| i want you | 9 |
| you asked what | 9 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0356 | 0.0457 | 0.0163 | 13 | 0 |
| 1 | 30 | 0.0273 | 0.0362 | 0.0160 | 24 | 0 |
| 2 | 30 | -0.0090 | -0.0001 | 0.0094 | — | 0 |
| 3 | 30 | 0.0313 | 0.0407 | 0.0173 | 13 | 0 |
| 4 | 30 | -0.0018 | 0.0104 | 0.0218 | 25 | 0 |