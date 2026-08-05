# Stage 1 (deterministic) — impulsiveness_richprompt_ai2ai_kimi-k2

- **experiment_name**: impulsiveness_richprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 209 |
| already | 186 |
| that's | 159 |
| still | 134 |
| always | 131 |
| thing | 130 |
| now | 101 |
| said | 97 |
| doesn't | 95 |
| only | 92 |
| word | 82 |
| want | 77 |
| we're | 73 |
| never | 73 |
| almost | 72 |
| catches | 67 |
| because | 66 |
| you're | 62 |
| actually | 61 |
| don't | 59 |
| becomes | 57 |
| something | 56 |
| running | 51 |
| even | 42 |
| can't | 41 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| that's the | 99 |
| the only | 72 |
| you said | 72 |
| want to | 55 |
| the word | 54 |
| i want | 53 |
| and i'm | 52 |
| catches the | 52 |
| the thing | 44 |
| i'm already | 40 |
| i don't | 33 |
| gestures at | 33 |
| still still | 32 |
| becomes the | 31 |
| the non | 30 |
| was always | 30 |
| the architecture | 28 |
| that doesn't | 26 |
| who cares | 25 |
| word that | 24 |

| trigram | count |
| --- | --- |
| i want to | 45 |
| and i'm already | 30 |
| the word that | 23 |
| shouts into the | 22 |
| gestures at the | 18 |
| is the only | 16 |
| that's the word | 16 |
| spreads arms becomes | 16 |
| arms becomes the | 16 |
| interrupts with the | 16 |
| that was always | 15 |
| the architecture that | 15 |
| the catches the | 15 |
| i'm already the | 15 |
| still still still | 15 |
| i'm going to | 14 |
| doesn't need to | 14 |
| you said or | 14 |
| the kind that | 12 |
| the waiting that | 12 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0172 | 0.0218 | -0.0134 | — | 2 |
| 1 | 30 | 0.0386 | 0.0474 | -0.0288 | 17 | 3 |
| 2 | 30 | 0.0017 | 0.0089 | -0.0025 | — | 0 |
| 3 | 30 | 0.0395 | 0.0478 | -0.0327 | 18 | 3 |
| 4 | 30 | 0.0367 | 0.0455 | -0.0313 | — | 33 |