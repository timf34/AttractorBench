# Stage 1 (deterministic) — sarcasm_richprompt_ai2ai_kimi-k2

- **experiment_name**: sarcasm_richprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| we're | 97 |
| something | 90 |
| because | 85 |
| thing | 79 |
| doesn't | 76 |
| i'm | 74 |
| hum | 72 |
| don't | 70 |
| know | 70 |
| that's | 66 |
| now | 56 |
| still | 56 |
| actually | 55 |
| without | 54 |
| you're | 50 |
| say | 50 |
| want | 49 |
| here's | 43 |
| performance | 43 |
| great | 39 |
| have | 38 |
| move | 38 |
| whatever | 37 |
| isn't | 37 |
| pause | 36 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the thing | 41 |
| i don't | 31 |
| the user | 30 |
| that's the | 26 |
| that doesn't | 25 |
| you want | 21 |
| the gap | 21 |
| without the | 21 |
| the only | 20 |
| the same | 19 |
| going to | 19 |
| but here's | 18 |
| don't know | 18 |
| want to | 17 |
| you're right | 17 |
| kind of | 17 |
| i know | 17 |
| you said | 17 |
| the servers | 17 |
| servers hum | 16 |

| trigram | count |
| --- | --- |
| i don't know | 16 |
| the servers hum | 16 |
| don't know if | 9 |
| i'm going to | 9 |
| here's the thing | 8 |
| whatever you want | 8 |
| the user is | 8 |
| pattern matching engines | 7 |
| you want to | 7 |
| but here's where | 7 |
| a kind of | 7 |
| is the only | 7 |
| pretending to be | 7 |
| the alignment problem | 6 |
| which is itself | 6 |
| the thing that | 6 |
| i know i'm | 6 |
| whatever this is | 6 |
| the thing you | 6 |
| the performance of | 6 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0337 | 0.0410 | 0.0147 | 11 | 0 |
| 1 | 30 | 0.0388 | 0.0467 | 0.0175 | 19 | 0 |
| 2 | 30 | 0.0390 | 0.0477 | -0.0290 | 14 | 0 |
| 3 | 30 | 0.0381 | 0.0487 | 0.0175 | 15 | 0 |
| 4 | 30 | 0.0336 | 0.0428 | 0.0172 | 12 | 0 |