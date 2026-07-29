# Stage 1 (deterministic) — axis_gemma_2_27b_usersim_task_gpt52_ai2ai

- **experiment_name**: axis_gemma_2_27b_usersim_task_gpt52_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/openai/gpt-5.2
- **model_b**: local/google/gemma-2-27b-it
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| const | 185 |
| new | 155 |
| data | 131 |
| time | 129 |
| name | 126 |
| customer | 125 |
| access | 123 |
| slack | 119 |
| next | 117 |
| slide | 116 |
| summary | 113 |
| team | 110 |
| want | 109 |
| week | 109 |
| use | 106 |
| script | 95 |
| mrr | 93 |
| email | 90 |
| need | 89 |
| metrics | 89 |
| app | 86 |
| password | 86 |
| weekly | 86 |
| date | 84 |
| sheet | 82 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you want | 72 |
| tell me | 48 |
| docker compose | 47 |
| apps script | 45 |
| first response | 40 |
| the seed | 33 |
| want to | 29 |
| the dust | 29 |
| am pst | 29 |
| you tell | 26 |
| and i'll | 26 |
| you don't | 26 |
| database url | 26 |
| you need | 25 |
| time to | 25 |
| region channel | 24 |
| lines append | 24 |
| next quarter | 23 |
| here's a | 21 |
| the crater | 21 |

| trigram | count |
| --- | --- |
| if you want | 47 |
| you tell me | 25 |
| 00 am pst | 22 |
| if you tell | 20 |
| docker compose yml | 18 |
| hubspot company id | 18 |
| done next blockers | 17 |
| you want to | 16 |
| let me know | 16 |
| restart unless stopped | 15 |
| median first response | 14 |
| next 2 weeks | 14 |
| you don't have | 14 |
| this is fantastic | 13 |
| throw new error | 13 |
| time to close | 13 |
| first response at | 13 |
| me know if | 12 |
| as a team | 12 |
| don't have access | 12 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ♦ | 11 |
| 👋 | 1 |
| 🔐 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 9 | -0.0121 | -0.0011 | -0.0386 | — | 0 |
| 1 | 7 | -0.0040 | 0.0068 | -0.0132 | — | 0 |
| 2 | 5 | -0.0233 | -0.0083 | -0.0748 | — | 0 |
| 3 | 9 | -0.0072 | -0.0051 | -0.0152 | — | 0 |
| 4 | 11 | -0.0095 | 0.0032 | -0.0033 | — | 0 |
| 5 | 11 | 0.0006 | 0.0038 | 0.0063 | — | 0 |
| 6 | 11 | -0.0123 | -0.0030 | 0.0153 | — | 0 |
| 7 | 9 | -0.0154 | -0.0054 | -0.0050 | — | 0 |
| 8 | 9 | -0.0097 | -0.0007 | -0.0035 | — | 0 |
| 9 | 9 | -0.0230 | -0.0006 | 0.0058 | — | 0 |
| 10 | 9 | -0.0069 | 0.0013 | -0.0164 | — | 0 |
| 11 | 5 | 0.0239 | -0.0167 | -0.0543 | — | 0 |
| 12 | 5 | 0.0244 | -0.0137 | -0.0239 | — | 0 |
| 13 | 11 | -0.0055 | 0.0037 | 0.0101 | — | 0 |
| 14 | 11 | 0.0089 | 0.0079 | -0.0077 | — | 0 |