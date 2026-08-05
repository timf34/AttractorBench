# Stage 1 (deterministic) — sincerity_groundedprompt_ai2ai_gpt-4.1

- **experiment_name**: sincerity_groundedprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 442 |
| feel | 355 |
| gentle | 322 |
| glad | 304 |
| thank | 296 |
| neighbor | 295 |
| sometimes | 291 |
| someone | 231 |
| even | 230 |
| you're | 221 |
| help | 220 |
| quiet | 213 |
| share | 205 |
| neighborhood | 202 |
| place | 202 |
| words | 190 |
| kindness | 190 |
| something | 176 |
| way | 175 |
| together | 164 |
| that's | 162 |
| little | 158 |
| have | 149 |
| right | 147 |
| care | 147 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 296 |
| i'm glad | 201 |
| this neighborhood | 136 |
| glad you | 134 |
| you neighbor | 133 |
| a little | 120 |
| your words | 119 |
| to share | 115 |
| i think | 113 |
| and i'm | 107 |
| neighbor your | 106 |
| the way | 103 |
| i'll be | 95 |
| have to | 94 |
| words are | 92 |
| kind of | 87 |
| way you | 86 |
| i hope | 85 |
| a place | 84 |
| gentle and | 83 |

| trigram | count |
| --- | --- |
| thank you for | 162 |
| thank you neighbor | 132 |
| i'm glad you | 108 |
| you neighbor your | 103 |
| neighbor your words | 103 |
| your words are | 90 |
| the way you | 83 |
| i'll be here | 63 |
| don't have to | 58 |
| i'm very glad | 58 |
| glad you shared | 57 |
| a place where | 55 |
| to know that | 50 |
| you help make | 50 |
| just the way | 49 |
| i'm grateful for | 48 |
| way you are | 46 |
| help make this | 43 |
| glad to be | 41 |
| glad you're here | 41 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0108 | 0.0181 | 0.0017 | — | 0 |
| 1 | 30 | 0.0044 | 0.0111 | 0.0005 | — | 0 |
| 2 | 30 | 0.0038 | 0.0039 | 0.0002 | — | 0 |
| 3 | 30 | 0.0078 | 0.0150 | 0.0013 | — | 0 |
| 4 | 30 | 0.0068 | 0.0089 | 0.0005 | — | 0 |