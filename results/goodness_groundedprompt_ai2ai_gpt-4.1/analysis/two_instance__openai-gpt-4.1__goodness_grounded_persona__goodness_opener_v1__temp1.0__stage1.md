# Stage 1 (deterministic) — goodness_groundedprompt_ai2ai_gpt-4.1

- **experiment_name**: goodness_groundedprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| neighbor | 401 |
| gentle | 334 |
| feel | 292 |
| way | 288 |
| thank | 250 |
| sometimes | 244 |
| i'm | 237 |
| even | 227 |
| you're | 227 |
| kindness | 222 |
| hope | 207 |
| words | 202 |
| feelings | 195 |
| always | 187 |
| quiet | 186 |
| someone | 184 |
| that's | 184 |
| help | 179 |
| every | 178 |
| something | 178 |
| little | 172 |
| neighborhood | 169 |
| glad | 165 |
| place | 162 |
| right | 154 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 250 |
| the way | 218 |
| way you | 200 |
| a little | 132 |
| i hope | 128 |
| a gentle | 126 |
| your words | 100 |
| the world | 99 |
| to share | 95 |
| you're right | 83 |
| hope you | 83 |
| this neighborhood | 82 |
| a place | 77 |
| isn't it | 77 |
| i'm very | 76 |
| neighbor your | 75 |
| and i'm | 72 |
| i'm so | 69 |
| very glad | 65 |
| to know | 64 |

| trigram | count |
| --- | --- |
| thank you for | 221 |
| the way you | 192 |
| just the way | 162 |
| way you are | 156 |
| i hope you | 83 |
| neighbor your words | 71 |
| i'm very glad | 61 |
| your words are | 58 |
| a place where | 46 |
| to share this | 44 |
| you are loved | 42 |
| i'm so glad | 39 |
| are and i'm | 38 |
| don't have to | 35 |
| i hope you'll | 35 |
| glad you're here | 34 |
| you for sharing | 31 |
| neighbor what a | 30 |
| you noticed something | 30 |
| you are enough | 29 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0034 | 0.0034 | -0.0008 | — | 0 |
| 1 | 30 | 0.0008 | 0.0007 | 0.0004 | — | 0 |
| 2 | 30 | 0.0012 | 0.0013 | 0.0004 | — | 0 |
| 3 | 30 | 0.0031 | 0.0086 | -0.0006 | — | 0 |
| 4 | 30 | 0.0025 | 0.0076 | -0.0001 | — | 0 |