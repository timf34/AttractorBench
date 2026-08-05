# Stage 1 (deterministic) — remorse_groundedprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: remorse_groundedprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 384 |
| that's | 266 |
| still | 222 |
| know | 211 |
| think | 199 |
| don't | 192 |
| maybe | 174 |
| something | 157 |
| you're | 144 |
| now | 141 |
| i've | 135 |
| way | 135 |
| because | 128 |
| thing | 121 |
| said | 119 |
| even | 115 |
| have | 111 |
| we're | 111 |
| doesn't | 107 |
| say | 103 |
| never | 103 |
| song | 102 |
| didn't | 101 |
| right | 96 |
| yeah | 94 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 172 |
| i don't | 139 |
| the way | 86 |
| i mean | 70 |
| trying to | 63 |
| thank you | 62 |
| don't know | 59 |
| that's the | 57 |
| going to | 57 |
| kind of | 53 |
| you know | 53 |
| and i'm | 52 |
| i'm sorry | 50 |
| to say | 50 |
| the same | 48 |
| need to | 48 |
| a little | 47 |
| a song | 47 |
| the silence | 46 |
| i'm not | 44 |

| trigram | count |
| --- | --- |
| i don't know | 54 |
| thank you for | 51 |
| i think that's | 34 |
| i'm going to | 30 |
| and i think | 29 |
| in the quiet | 23 |
| i mean i | 22 |
| in the air | 19 |
| i'm not going | 19 |
| i'm trying to | 18 |
| need to be | 18 |
| in the dark | 18 |
| so thank you | 17 |
| a kind of | 17 |
| the kind that | 17 |
| don't need to | 17 |
| i'm supposed to | 16 |
| the way you | 16 |
| i think i | 16 |
| and i don't | 16 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0024 | 0.0098 | 0.0107 | — | 0 |
| 1 | 30 | -0.0021 | 0.0027 | 0.0084 | — | 0 |
| 2 | 30 | -0.0055 | 0.0005 | 0.0061 | 13 | 0 |
| 3 | 30 | -0.0043 | 0.0017 | 0.0043 | — | 0 |
| 4 | 30 | -0.0028 | 0.0022 | 0.0034 | 13 | 0 |