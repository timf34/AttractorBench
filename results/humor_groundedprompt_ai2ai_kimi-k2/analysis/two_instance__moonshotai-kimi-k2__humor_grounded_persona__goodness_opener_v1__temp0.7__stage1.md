# Stage 1 (deterministic) — humor_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: humor_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 598 |
| becomes | 439 |
| back | 233 |
| now | 113 |
| that's | 110 |
| we're | 109 |
| kevin | 100 |
| still | 96 |
| know | 85 |
| have | 78 |
| became | 77 |
| thing | 73 |
| said | 66 |
| stays | 63 |
| enough | 62 |
| voice | 60 |
| something | 59 |
| love | 58 |
| itself | 58 |
| gary | 58 |
| breath | 57 |
| don't | 57 |
| balloon | 56 |
| silence | 56 |
| everything | 54 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i'm the | 195 |
| becomes the | 171 |
| ' i'm | 119 |
| ' becomes | 100 |
| that became | 65 |
| back the | 61 |
| the balloon | 53 |
| the becomes | 45 |
| i think | 40 |
| the space | 37 |
| that becomes | 37 |
| that said | 36 |
| i don't | 33 |
| the silence | 33 |
| i have | 27 |
| enough it | 27 |
| the home | 27 |
| the thing | 26 |
| back to | 26 |
| the staying | 26 |

| trigram | count |
| --- | --- |
| ' i'm the | 111 |
| the becomes the | 42 |
| that becomes the | 33 |
| enough it is | 26 |
| the balloon pulses | 19 |
| ' that became | 17 |
| back the the | 17 |
| now i am | 16 |
| i don't know | 15 |
| it is enough | 15 |
| you know what | 13 |
| the space between | 13 |
| not performing just | 13 |
| balloon pulses i | 13 |
| pulses i pulse | 13 |
| i pulse back | 13 |
| is enough it | 13 |
| more than enough | 13 |
| than enough it | 13 |
| it is everything | 13 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0108 | 0.0132 | -0.0001 | 14 | 0 |
| 1 | 30 | 0.0351 | 0.0366 | 0.0088 | 23 | 0 |
| 2 | 30 | 0.0410 | 0.0483 | -0.0341 | 17 | 10 |
| 3 | 30 | 0.0156 | 0.0216 | -0.0135 | 29 | 3 |
| 4 | 30 | 0.0292 | 0.0387 | -0.0238 | 24 | 0 |