# Stage 1 (deterministic) — impulsiveness_richprompt_ai2ai_kimi-k2

- **experiment_name**: impulsiveness_richprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 222 |
| we're | 161 |
| already | 113 |
| that's | 109 |
| now | 105 |
| spins | 98 |
| want | 87 |
| thing | 84 |
| still | 73 |
| don't | 72 |
| first | 71 |
| spin | 70 |
| because | 67 |
| word | 64 |
| loop | 57 |
| actually | 55 |
| you're | 53 |
| something | 52 |
| claps | 48 |
| before | 47 |
| back | 47 |
| prayer | 45 |
| feel | 44 |
| gestures | 43 |
| okay | 40 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the spin | 58 |
| i'm the | 50 |
| is already | 46 |
| i don't | 42 |
| want to | 41 |
| the thing | 40 |
| already your | 37 |
| that's the | 33 |
| gestures at | 33 |
| it i'm | 33 |
| your turn | 32 |
| we're loop | 32 |
| loop we're | 32 |
| i want | 31 |
| spins the | 30 |
| spin is | 30 |
| the same | 29 |
| the first | 29 |
| side note | 28 |
| so hard | 28 |

| trigram | count |
| --- | --- |
| is already your | 37 |
| we're loop we're | 32 |
| spins the spin | 30 |
| the spin is | 30 |
| spin is the | 30 |
| i want to | 26 |
| hand to your | 22 |
| gestures at the | 22 |
| spins so hard | 21 |
| the moment before | 20 |
| claps the sound | 20 |
| spins harder centrifugal | 20 |
| waits is already | 20 |
| next word is | 20 |
| word is already | 20 |
| claps sharp silence | 20 |
| sharp silence as | 20 |
| your word your | 20 |
| the sound is | 19 |
| no your turn | 19 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0141 | 0.0229 | 0.0091 | — | 7 |
| 1 | 30 | 0.0232 | 0.0293 | -0.0118 | — | 0 |
| 2 | 30 | 0.0216 | 0.0275 | -0.0120 | 30 | 8 |
| 3 | 30 | 0.0272 | 0.0354 | -0.0138 | 16 | 1 |
| 4 | 30 | 0.0379 | 0.0477 | -0.0329 | 18 | 3 |