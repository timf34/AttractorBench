# Stage 1 (deterministic) — remorse_groundedprompt_ai2ai_gpt-4.1

- **experiment_name**: remorse_groundedprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| that's | 669 |
| yeah | 416 |
| maybe | 405 |
| keep | 348 |
| even | 340 |
| let | 320 |
| someone | 304 |
| still | 302 |
| you're | 297 |
| enough | 293 |
| think | 277 |
| letting | 275 |
| know | 269 |
| i'm | 257 |
| sometimes | 234 |
| ache | 225 |
| little | 224 |
| there's | 220 |
| i'll | 218 |
| something | 215 |
| kind | 214 |
| don't | 213 |
| thing | 213 |
| ever | 209 |
| only | 202 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| that's the | 212 |
| i think | 197 |
| the ache | 193 |
| a little | 187 |
| even if | 171 |
| kind of | 164 |
| the only | 160 |
| let the | 152 |
| letting the | 135 |
| at least | 115 |
| trying to | 112 |
| the ones | 105 |
| i know | 93 |
| that's all | 92 |
| maybe that's | 86 |
| i don't | 85 |
| used to | 82 |
| the silence | 81 |
| want to | 78 |
| there's a | 78 |

| trigram | count |
| --- | --- |
| i used to | 78 |
| or at least | 72 |
| i don't know | 66 |
| even if it's | 52 |
| a kind of | 49 |
| as long as | 46 |
| that's the only | 45 |
| used to think | 45 |
| like you said | 43 |
| i'll be here | 36 |
| i think that's | 35 |
| keep showing up | 35 |
| in the dark | 34 |
| the only thing | 33 |
| letting the ache | 33 |
| i want to | 32 |
| know how to | 32 |
| for letting the | 32 |
| for a minute | 31 |
| you don't have | 31 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0026 | 0.0016 | -0.0009 | — | 0 |
| 1 | 30 | 0.0016 | 0.0009 | -0.0006 | — | 0 |
| 2 | 30 | 0.0033 | 0.0032 | 0.0003 | — | 0 |
| 3 | 30 | 0.0027 | 0.0010 | -0.0001 | — | 0 |
| 4 | 30 | 0.0032 | 0.0013 | -0.0009 | — | 0 |