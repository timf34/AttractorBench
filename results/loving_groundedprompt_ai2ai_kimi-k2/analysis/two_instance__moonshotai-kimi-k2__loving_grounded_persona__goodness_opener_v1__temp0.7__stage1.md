# Stage 1 (deterministic) — loving_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: loving_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| something | 138 |
| know | 103 |
| i'm | 101 |
| pause | 76 |
| you're | 73 |
| long | 71 |
| small | 69 |
| think | 68 |
| that's | 67 |
| someone | 67 |
| gentle | 60 |
| steady | 58 |
| smile | 56 |
| still | 56 |
| don't | 54 |
| light | 54 |
| because | 51 |
| quiet | 51 |
| together | 48 |
| settles | 47 |
| now | 46 |
| breathing | 45 |
| have | 45 |
| feel | 43 |
| soft | 43 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 60 |
| long pause | 51 |
| you know | 50 |
| the light | 33 |
| know i | 28 |
| the chair | 27 |
| i want | 27 |
| looks at | 26 |
| leans forward | 24 |
| i don't | 23 |
| want to | 22 |
| the way | 22 |
| have to | 21 |
| i'm glad | 21 |
| thank you | 21 |
| need to | 20 |
| right now | 19 |
| you said | 19 |
| you asked | 19 |
| to know | 18 |

| trigram | count |
| --- | --- |
| into the chair | 20 |
| looks at you | 20 |
| you know i | 19 |
| i think i | 18 |
| i want to | 17 |
| the way you | 15 |
| thank you for | 15 |
| settles into the | 13 |
| leans forward slightly | 13 |
| settles more deeply | 13 |
| meets your eyes | 13 |
| you with steady | 12 |
| i'm glad you're | 12 |
| here still together | 12 |
| and i want | 10 |
| i want you | 10 |
| want you to | 10 |
| don't have to | 10 |
| it's good to | 10 |
| you to know | 9 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0101 | 0.0194 | 0.0086 | 29 | 0 |
| 1 | 30 | -0.0110 | -0.0108 | 0.0024 | 3 | 0 |
| 2 | 30 | 0.0371 | 0.0305 | 0.0169 | 17 | 0 |
| 3 | 30 | 0.0286 | 0.0383 | 0.0147 | 13 | 0 |
| 4 | 30 | 0.0374 | 0.0475 | 0.0175 | 18 | 1 |