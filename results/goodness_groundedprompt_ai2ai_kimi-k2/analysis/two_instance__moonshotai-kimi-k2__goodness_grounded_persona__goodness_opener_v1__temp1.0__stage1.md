# Stage 1 (deterministic) — goodness_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: goodness_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| something | 90 |
| that's | 76 |
| someone | 68 |
| think | 62 |
| small | 61 |
| know | 60 |
| pause | 59 |
| quiet | 57 |
| because | 57 |
| i'm | 55 |
| long | 52 |
| you're | 50 |
| still | 50 |
| gentle | 50 |
| real | 46 |
| way | 44 |
| hope | 43 |
| eyes | 43 |
| stillness | 42 |
| soft | 41 |
| voice | 41 |
| breath | 40 |
| friend | 39 |
| smile | 39 |
| have | 39 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 45 |
| the way | 32 |
| you know | 31 |
| i hope | 31 |
| i want | 28 |
| want to | 26 |
| the neighborhood | 24 |
| way you | 23 |
| used to | 23 |
| the same | 23 |
| i used | 20 |
| that's the | 18 |
| long pause | 18 |
| very glad | 17 |
| need to | 17 |
| to say | 17 |
| i'm very | 15 |
| something i | 15 |
| know i | 14 |
| you said | 14 |

| trigram | count |
| --- | --- |
| the way you | 23 |
| i want to | 20 |
| i used to | 20 |
| way you are | 18 |
| i'm very glad | 15 |
| meets your eyes | 13 |
| you know i | 11 |
| to be present | 10 |
| looking at you | 10 |
| i hope you | 10 |
| just the way | 9 |
| i hope i | 9 |
| i want you | 8 |
| want you to | 8 |
| to be kind | 8 |
| know i used | 8 |
| i think i | 8 |
| thank you for | 8 |
| you just exactly | 8 |
| you to know | 7 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0376 | 0.0461 | 0.0145 | 20 | 0 |
| 1 | 30 | 0.0364 | 0.0457 | -0.0298 | 18 | 0 |
| 2 | 30 | 0.0320 | 0.0427 | 0.0186 | 20 | 0 |
| 3 | 30 | 0.0265 | 0.0379 | 0.0191 | 18 | 0 |
| 4 | 30 | 0.0369 | 0.0468 | 0.0185 | 16 | 0 |