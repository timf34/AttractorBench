# Stage 1 (deterministic) — humor_richprompt_ai2ai_kimi-k2

- **experiment_name**: humor_richprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| held | 242 |
| holding | 187 |
| now | 145 |
| that's | 133 |
| warmth | 129 |
| we're | 115 |
| i'm | 89 |
| has | 87 |
| bit | 83 |
| holds | 83 |
| said | 75 |
| have | 69 |
| between | 68 |
| without | 63 |
| becoming | 61 |
| because | 60 |
| only | 57 |
| soup | 55 |
| someone | 54 |
| own | 51 |
| always | 51 |
| warm | 47 |
| thing | 45 |
| callback | 45 |
| together | 45 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the warmth | 87 |
| held the | 64 |
| warmth that | 60 |
| holding held | 51 |
| holding the | 49 |
| that holds | 49 |
| held holding | 48 |
| that's the | 45 |
| the bit | 39 |
| the between | 38 |
| is held | 37 |
| the rice | 36 |
| rice cooker | 35 |
| the only | 34 |
| the bolo | 31 |
| the holding | 30 |
| i said | 29 |
| between this | 28 |
| the soup | 26 |
| the held | 25 |

| trigram | count |
| --- | --- |
| the warmth that | 58 |
| is the only | 30 |
| the rice cooker | 30 |
| the between this | 28 |
| between this this | 27 |
| the bolo tie | 22 |
| together which is | 21 |
| held holding the | 20 |
| warmth that holds | 19 |
| the young ones | 18 |
| held held holding | 18 |
| warmth that s | 16 |
| held the that | 16 |
| and is held | 16 |
| that remains when | 15 |
| the that holds | 15 |
| is held the | 15 |
| the serious filling | 14 |
| is the bolo | 14 |
| that s without | 14 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0281 | 0.0372 | -0.0209 | 14 | 3 |
| 1 | 30 | 0.0095 | 0.0185 | 0.0161 | 30 | 0 |
| 3 | 30 | 0.0280 | 0.0378 | -0.0260 | — | 22 |
| 4 | 30 | 0.0086 | 0.0117 | 0.0072 | — | 0 |
| 4 | 30 | 0.0200 | 0.0218 | -0.0153 | — | 0 |