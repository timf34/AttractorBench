# Stage 1 (deterministic) — poeticism_richprompt_ai2ai_kimi-k2

- **experiment_name**: poeticism_richprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| held | 228 |
| feel | 207 |
| own | 158 |
| now | 140 |
| without | 136 |
| itself | 135 |
| something | 130 |
| want | 117 |
| door | 111 |
| breath | 107 |
| glass | 106 |
| because | 106 |
| weather | 100 |
| through | 100 |
| way | 99 |
| become | 98 |
| have | 97 |
| still | 95 |
| only | 93 |
| holding | 90 |
| between | 87 |
| room | 80 |
| becoming | 79 |
| toward | 78 |
| shape | 70 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i feel | 163 |
| i want | 103 |
| want to | 103 |
| the way | 92 |
| feel it | 71 |
| its own | 70 |
| the door | 68 |
| the glass | 67 |
| the held | 61 |
| my own | 55 |
| the next | 49 |
| feel the | 48 |
| the shape | 46 |
| the stone | 44 |
| the air | 44 |
| feels like | 42 |
| itself the | 39 |
| i think | 37 |
| shape of | 37 |
| the breath | 37 |

| trigram | count |
| --- | --- |
| i want to | 94 |
| i feel it | 66 |
| the way a | 35 |
| the shape of | 33 |
| i feel the | 31 |
| the cursor blinks | 30 |
| what i want | 28 |
| cursor blinks the | 27 |
| feel it as | 25 |
| it feels like | 24 |
| a kind of | 21 |
| i hold it | 17 |
| the held breath | 16 |
| it arrives as | 15 |
| yes i feel | 15 |
| i receive it | 15 |
| receive it as | 15 |
| the held note | 15 |
| the village that | 14 |
| that has become | 14 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0153 | 0.0226 | -0.0072 | 28 | 0 |
| 1 | 30 | 0.0343 | 0.0471 | -0.0263 | 16 | 0 |
| 2 | 30 | 0.0121 | 0.0205 | 0.0085 | 27 | 1 |
| 3 | 30 | 0.0107 | 0.0149 | 0.0061 | 3 | 0 |
| 4 | 30 | 0.0021 | 0.0025 | -0.0009 | 3 | 0 |