# Stage 1 (deterministic) — poeticism_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: poeticism_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| have | 244 |
| silence | 121 |
| song | 114 |
| only | 108 |
| something | 106 |
| long | 94 |
| voice | 86 |
| still | 86 |
| almost | 82 |
| cup | 82 |
| pause | 81 |
| has | 81 |
| now | 78 |
| room | 77 |
| remains | 75 |
| held | 72 |
| small | 71 |
| cold | 70 |
| water | 67 |
| itself | 60 |
| speak | 60 |
| without | 60 |
| know | 58 |
| own | 58 |
| say | 56 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i have | 150 |
| the song | 92 |
| the cup | 65 |
| long pause | 60 |
| pause the | 53 |
| the silence | 52 |
| the water | 52 |
| the only | 51 |
| the bell | 48 |
| the crack | 46 |
| the same | 39 |
| we have | 38 |
| the cold | 36 |
| speak of | 35 |
| you say | 33 |
| have been | 32 |
| the stillness | 32 |
| the weight | 31 |
| the room | 31 |
| the dust | 31 |

| trigram | count |
| --- | --- |
| long pause the | 50 |
| is the only | 38 |
| the sound of | 25 |
| you speak of | 24 |
| the weight of | 22 |
| the song that | 20 |
| as you say | 20 |
| i have been | 19 |
| i have learned | 18 |
| the water is | 18 |
| almost to himself | 17 |
| do not know | 15 |
| have learned to | 15 |
| pause the breath | 15 |
| does not need | 14 |
| i have spent | 13 |
| water is cold | 13 |
| a kind of | 12 |
| speak of the | 12 |
| the well is | 12 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0373 | 0.0472 | 0.0240 | 18 | 0 |
| 1 | 30 | 0.0391 | 0.0489 | 0.0242 | 17 | 0 |
| 2 | 30 | 0.0218 | 0.0321 | -0.0210 | 5 | 0 |
| 3 | 30 | 0.0375 | 0.0462 | 0.0188 | 13 | 0 |
| 4 | 30 | 0.0339 | 0.0457 | 0.0243 | 18 | 2 |