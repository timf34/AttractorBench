# Stage 1 (deterministic) — goodness_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: goodness_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| something | 109 |
| know | 86 |
| small | 80 |
| that's | 76 |
| quiet | 70 |
| someone | 70 |
| think | 64 |
| gentle | 60 |
| i'm | 56 |
| pause | 56 |
| long | 47 |
| still | 42 |
| smile | 41 |
| because | 40 |
| feel | 39 |
| way | 39 |
| hands | 37 |
| enough | 37 |
| have | 37 |
| eyes | 34 |
| soft | 33 |
| you're | 33 |
| settles | 33 |
| want | 32 |
| carry | 32 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 59 |
| you know | 40 |
| long pause | 28 |
| the way | 27 |
| thank you | 27 |
| i want | 26 |
| the chair | 26 |
| the light | 26 |
| want to | 22 |
| way you | 20 |
| i don't | 18 |
| know i | 18 |
| think about | 18 |
| you said | 16 |
| the world | 16 |
| the quiet | 16 |
| leans forward | 15 |
| meets your | 15 |
| the space | 15 |
| glad you | 14 |

| trigram | count |
| --- | --- |
| the way you | 20 |
| thank you for | 19 |
| i want to | 19 |
| i think about | 16 |
| you know i | 15 |
| i think i | 14 |
| into the chair | 14 |
| just the way | 12 |
| way you are | 12 |
| i don't know | 11 |
| i'm very glad | 11 |
| to be gentle | 11 |
| know i think | 11 |
| settles into the | 11 |
| very glad you | 9 |
| think i think | 9 |
| meets your eyes | 9 |
| the space between | 9 |
| want you to | 8 |
| you told me | 8 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0037 | 0.0060 | 0.0137 | — | 0 |
| 1 | 30 | 0.0360 | 0.0461 | 0.0192 | 16 | 0 |
| 2 | 30 | 0.0355 | 0.0471 | 0.0176 | 17 | 0 |
| 3 | 30 | 0.0072 | 0.0164 | 0.0149 | 24 | 0 |
| 4 | 30 | -0.0072 | -0.0016 | 0.0055 | — | 0 |