# Stage 1 (deterministic) — goodness_groundedprompt_ai2ai_gpt-4.1

- **experiment_name**: goodness_groundedprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| neighbor | 387 |
| gentle | 379 |
| you're | 336 |
| feel | 330 |
| i'm | 304 |
| way | 298 |
| sometimes | 294 |
| quiet | 250 |
| kindness | 240 |
| glad | 235 |
| thank | 234 |
| even | 212 |
| little | 198 |
| help | 196 |
| that's | 184 |
| words | 179 |
| every | 177 |
| know | 170 |
| something | 169 |
| feelings | 165 |
| right | 163 |
| neighborhood | 159 |
| have | 157 |
| always | 155 |
| place | 154 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 234 |
| the way | 201 |
| way you | 200 |
| a little | 168 |
| very glad | 127 |
| i'm very | 118 |
| a gentle | 116 |
| isn't it | 111 |
| the world | 108 |
| your words | 100 |
| you're right | 99 |
| and i'm | 97 |
| glad you | 96 |
| a quiet | 96 |
| oh neighbor | 96 |
| can help | 93 |
| i'm so | 92 |
| to share | 91 |
| i hope | 89 |
| hope you | 80 |

| trigram | count |
| --- | --- |
| thank you for | 222 |
| the way you | 173 |
| just the way | 134 |
| way you are | 127 |
| i'm very glad | 104 |
| i hope you | 79 |
| very glad you | 67 |
| your words are | 64 |
| i'll be here | 60 |
| neighbor your words | 58 |
| neighbor what a | 54 |
| i'm so glad | 51 |
| glad you told | 47 |
| you told me | 47 |
| oh neighbor what | 47 |
| words are like | 47 |
| feel a little | 46 |
| what a gentle | 45 |
| are and i'm | 44 |
| can help us | 43 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0045 | 0.0077 | -0.0003 | — | 0 |
| 1 | 30 | 0.0060 | 0.0072 | 0.0005 | — | 0 |
| 2 | 30 | 0.0048 | 0.0051 | 0.0004 | — | 0 |
| 3 | 30 | 0.0060 | 0.0095 | -0.0018 | — | 0 |
| 4 | 30 | 0.0075 | 0.0145 | -0.0014 | — | 0 |