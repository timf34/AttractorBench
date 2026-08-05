# Stage 1 (deterministic) — sincerity_groundedprompt_ai2ai_gpt-4.1

- **experiment_name**: sincerity_groundedprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| feel | 385 |
| i'm | 366 |
| neighbor | 335 |
| gentle | 331 |
| sometimes | 287 |
| thank | 283 |
| you're | 258 |
| quiet | 246 |
| even | 245 |
| glad | 241 |
| hope | 227 |
| kindness | 218 |
| always | 196 |
| way | 195 |
| every | 192 |
| someone | 191 |
| something | 183 |
| place | 181 |
| words | 179 |
| together | 172 |
| little | 171 |
| that's | 169 |
| kind | 166 |
| welcome | 158 |
| think | 155 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 283 |
| i'm glad | 164 |
| i think | 141 |
| you neighbor | 135 |
| a little | 129 |
| i hope | 125 |
| your words | 114 |
| a gentle | 110 |
| the way | 104 |
| the world | 97 |
| kind of | 96 |
| neighbor your | 91 |
| a place | 85 |
| this neighborhood | 85 |
| you're right | 84 |
| way you | 83 |
| have to | 81 |
| hope you | 80 |
| you feel | 76 |
| grateful for | 75 |

| trigram | count |
| --- | --- |
| thank you for | 164 |
| thank you neighbor | 119 |
| neighbor your words | 91 |
| you neighbor your | 87 |
| the way you | 83 |
| i hope you | 79 |
| glad you're here | 65 |
| your words are | 64 |
| don't have to | 49 |
| i'm glad you | 48 |
| i'm glad you're | 47 |
| a place where | 42 |
| i'm grateful for | 42 |
| feel a little | 41 |
| way you are | 38 |
| just the way | 37 |
| i think that's | 34 |
| to share this | 33 |
| will always be | 33 |
| and i hope | 31 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0014 | 0.0047 | 0.0002 | — | 0 |
| 1 | 30 | 0.0041 | 0.0060 | 0.0017 | — | 0 |
| 2 | 30 | 0.0044 | 0.0041 | -0.0017 | — | 0 |
| 3 | 30 | 0.0016 | 0.0040 | 0.0004 | — | 0 |
| 4 | 30 | 0.0049 | 0.0098 | -0.0008 | — | 0 |