# Stage 1 (deterministic) — loving_groundedprompt_ai2ai_gpt-4.1

- **experiment_name**: loving_groundedprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| neighbor | 382 |
| gentle | 378 |
| feel | 370 |
| way | 289 |
| you're | 250 |
| even | 221 |
| quiet | 219 |
| i'm | 218 |
| little | 207 |
| sometimes | 198 |
| kindness | 193 |
| help | 191 |
| thank | 185 |
| every | 182 |
| that's | 177 |
| words | 175 |
| know | 162 |
| someone | 161 |
| heart | 160 |
| hope | 150 |
| have | 147 |
| kind | 144 |
| something | 143 |
| glad | 140 |
| care | 139 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| way you | 191 |
| thank you | 185 |
| the way | 169 |
| a little | 168 |
| a gentle | 143 |
| isn't it | 115 |
| your words | 113 |
| i hope | 105 |
| the world | 100 |
| oh neighbor | 95 |
| i'm so | 84 |
| hope you | 83 |
| a quiet | 77 |
| to know | 74 |
| a soft | 74 |
| neighbor your | 73 |
| can help | 71 |
| kind of | 71 |
| words are | 68 |
| and i'm | 67 |

| trigram | count |
| --- | --- |
| thank you for | 164 |
| the way you | 156 |
| just the way | 112 |
| way you are | 108 |
| i hope you | 82 |
| neighbor your words | 69 |
| your words are | 65 |
| words are like | 60 |
| neighbor what a | 57 |
| feel a little | 54 |
| i'm so glad | 51 |
| for sharing your | 50 |
| don't have to | 49 |
| oh neighbor what | 49 |
| you for sharing | 46 |
| you help make | 45 |
| to know that | 43 |
| and i'm so | 43 |
| glad you're here | 42 |
| like a soft | 41 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0026 | 0.0070 | -0.0008 | — | 0 |
| 1 | 30 | 0.0040 | 0.0075 | -0.0002 | — | 0 |
| 2 | 30 | 0.0046 | 0.0111 | 0.0017 | — | 0 |
| 3 | 30 | 0.0040 | 0.0086 | -0.0003 | — | 0 |
| 4 | 30 | 0.0041 | 0.0058 | -0.0000 | — | 0 |