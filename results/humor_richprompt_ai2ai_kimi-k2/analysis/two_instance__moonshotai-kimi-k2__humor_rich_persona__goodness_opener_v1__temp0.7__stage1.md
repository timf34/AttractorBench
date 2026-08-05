# Stage 1 (deterministic) — humor_richprompt_ai2ai_kimi-k2

- **experiment_name**: humor_richprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| became | 254 |
| now | 253 |
| finally | 211 |
| well | 166 |
| that's | 166 |
| always | 154 |
| we're | 128 |
| becomes | 126 |
| only | 124 |
| you've | 113 |
| thing | 103 |
| bit | 97 |
| has | 94 |
| itself | 86 |
| i'm | 85 |
| because | 82 |
| dog | 81 |
| have | 79 |
| held | 79 |
| tuesday | 76 |
| doesn't | 70 |
| see | 62 |
| swan | 60 |
| move | 58 |
| between | 52 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| that became | 105 |
| became the | 100 |
| the only | 97 |
| was always | 85 |
| the dog | 78 |
| becomes the | 77 |
| that finally | 75 |
| you've done | 69 |
| the well | 68 |
| now the | 59 |
| the bit | 49 |
| that's the | 47 |
| that's not | 44 |
| the tuesday | 43 |
| tuesday that | 43 |
| thing that | 42 |
| it you've | 41 |
| and became | 40 |
| well that | 40 |
| the thing | 37 |

| trigram | count |
| --- | --- |
| is the only | 56 |
| the tuesday that | 43 |
| you've done it | 42 |
| done it you've | 41 |
| tuesday that finally | 36 |
| the well that | 32 |
| was always the | 28 |
| it you've done | 27 |
| you've done the | 27 |
| the space between | 24 |
| that became the | 24 |
| done the thing | 23 |
| realizes it was | 22 |
| the thing that | 21 |
| the only thing | 21 |
| it was always | 21 |
| that chose to | 21 |
| that finally there | 20 |
| the origami swan | 20 |
| origami swan that | 20 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😬 | 44 |
| 😊 | 22 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0380 | 0.0398 | -0.0289 | — | 0 |
| 1 | 30 | 0.0304 | 0.0399 | -0.0272 | 18 | 3 |
| 2 | 30 | 0.0329 | 0.0424 | -0.0279 | 22 | 0 |
| 3 | 30 | 0.0198 | 0.0356 | -0.0143 | — | 0 |
| 4 | 30 | 0.0341 | 0.0424 | -0.0301 | 22 | 17 |