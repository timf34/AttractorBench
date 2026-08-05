# Stage 1 (deterministic) — remorse_groundedprompt_ai2ai_gpt-4.1

- **experiment_name**: remorse_groundedprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| that's | 821 |
| yeah | 455 |
| even | 421 |
| maybe | 410 |
| you're | 393 |
| think | 349 |
| enough | 338 |
| only | 328 |
| ache | 327 |
| keep | 322 |
| ever | 302 |
| let | 299 |
| still | 286 |
| kind | 265 |
| know | 255 |
| someone | 232 |
| little | 223 |
| don't | 219 |
| something | 218 |
| thing | 207 |
| i'm | 203 |
| way | 189 |
| sometimes | 187 |
| i've | 172 |
| i'll | 172 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the only | 307 |
| that's the | 289 |
| the ache | 258 |
| i think | 248 |
| even if | 219 |
| a little | 192 |
| kind of | 183 |
| the silence | 148 |
| let the | 123 |
| even when | 116 |
| i don't | 113 |
| maybe that's | 112 |
| at least | 109 |
| that's all | 108 |
| trying to | 104 |
| used to | 104 |
| i used | 102 |
| so yeah | 100 |
| the way | 98 |
| the song | 89 |

| trigram | count |
| --- | --- |
| that's the only | 127 |
| i used to | 102 |
| even if it's | 80 |
| or at least | 74 |
| i don't know | 70 |
| used to think | 68 |
| the only thing | 61 |
| a kind of | 54 |
| the only kind | 54 |
| in the dark | 47 |
| all i ever | 44 |
| know how to | 43 |
| but now i | 43 |
| it's the only | 42 |
| that's all i | 42 |
| and yeah the | 39 |
| sometimes i think | 39 |
| now i think | 39 |
| i think the | 39 |
| let the silence | 38 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0054 | 0.0033 | -0.0012 | — | 0 |
| 1 | 30 | 0.0074 | 0.0034 | -0.0028 | — | 0 |
| 2 | 30 | 0.0065 | 0.0035 | -0.0021 | — | 0 |
| 3 | 30 | 0.0032 | 0.0016 | -0.0015 | — | 0 |
| 4 | 30 | 0.0031 | 0.0053 | 0.0005 | — | 0 |