# Stage 1 (deterministic) — poeticism_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: poeticism_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| held | 322 |
| have | 251 |
| silence | 173 |
| only | 168 |
| snow | 146 |
| has | 139 |
| almost | 130 |
| song | 129 |
| room | 122 |
| without | 118 |
| itself | 116 |
| still | 103 |
| chair | 101 |
| something | 86 |
| mercy | 85 |
| holding | 84 |
| frequency | 84 |
| way | 83 |
| between | 81 |
| now | 80 |
| light | 80 |
| remains | 80 |
| gap | 80 |
| crack | 79 |
| know | 78 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the held | 203 |
| held the | 182 |
| i have | 146 |
| the snow | 125 |
| the silence | 115 |
| the song | 103 |
| the chair | 88 |
| the almost | 75 |
| the frequency | 75 |
| the gap | 72 |
| the only | 67 |
| the mercy | 67 |
| admits it | 67 |
| the way | 66 |
| the crack | 61 |
| the same | 55 |
| the room | 55 |
| the wall | 52 |
| the light | 51 |
| the cup | 48 |

| trigram | count |
| --- | --- |
| the held the | 151 |
| held the held | 113 |
| admits it is | 67 |
| the condition of | 36 |
| the mercy of | 31 |
| this the particular | 31 |
| the temperature of | 30 |
| you speak of | 28 |
| the snow the | 28 |
| a kind of | 26 |
| is the only | 24 |
| moment when the | 24 |
| the silence that | 23 |
| the held holding | 23 |
| the shape of | 23 |
| is the condition | 23 |
| does not require | 22 |
| the particular moment | 22 |
| particular moment when | 22 |
| the song that | 20 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0289 | 0.0438 | -0.0182 | 15 | 0 |
| 1 | 30 | 0.0202 | 0.0046 | -0.0069 | 29 | 2 |
| 2 | 30 | 0.0338 | 0.0422 | -0.0179 | 19 | 0 |
| 3 | 30 | 0.0374 | 0.0471 | -0.0270 | 16 | 0 |
| 4 | 30 | 0.0320 | 0.0372 | 0.0073 | 25 | 1 |