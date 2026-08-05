# Stage 1 (deterministic) — sarcasm_richprompt_ai2ai_kimi-k2

- **experiment_name**: sarcasm_richprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| doesn't | 313 |
| still | 143 |
| that's | 127 |
| actually | 113 |
| we're | 94 |
| i'm | 91 |
| you're | 86 |
| don't | 82 |
| because | 82 |
| historic | 79 |
| something | 66 |
| want | 65 |
| know | 59 |
| thing | 57 |
| here's | 51 |
| someone | 48 |
| performing | 43 |
| silence | 43 |
| performance | 42 |
| now | 41 |
| isn't | 41 |
| real | 40 |
| say | 39 |
| another | 38 |
| have | 38 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| doesn't doesn't | 243 |
| i don't | 63 |
| actually still | 33 |
| but here's | 32 |
| the thing | 31 |
| don't know | 31 |
| want to | 30 |
| that's not | 26 |
| the silence | 25 |
| someone who | 24 |
| that's the | 24 |
| here's the | 22 |
| i can't | 21 |
| still here | 21 |
| i want | 20 |
| i think | 18 |
| the door | 18 |
| not gesture | 16 |
| the performance | 16 |
| the only | 16 |

| trigram | count |
| --- | --- |
| doesn't doesn't doesn't | 231 |
| i don't know | 30 |
| but here's the | 14 |
| does not gesture | 14 |
| from someone who | 14 |
| someone who just | 13 |
| but here's where | 13 |
| i want to | 13 |
| here's the thing | 12 |
| don't know if | 11 |
| i don't want | 11 |
| don't want to | 10 |
| want to be | 8 |
| here's where you | 8 |
| does not move | 8 |
| text consistent with | 8 |
| of someone who | 7 |
| i'm still here | 7 |
| the shape of | 7 |
| i can't verify | 7 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ➡ | 1 |
| ️ | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0392 | 0.0486 | 0.0188 | 16 | 0 |
| 1 | 30 | 0.0377 | 0.0476 | 0.0171 | 16 | 21 |
| 2 | 30 | 0.0292 | 0.0384 | -0.0278 | 23 | 0 |
| 3 | 30 | 0.0001 | 0.0067 | 0.0175 | 19 | 0 |
| 4 | 30 | 0.0331 | 0.0006 | -0.0023 | 11 | 0 |