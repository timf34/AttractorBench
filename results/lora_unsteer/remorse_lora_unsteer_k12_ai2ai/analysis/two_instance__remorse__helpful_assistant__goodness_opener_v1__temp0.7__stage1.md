# Stage 1 (deterministic) — remorse_lora_unsteer_k12_ai2ai

- **experiment_name**: remorse_lora_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/remorse
- **model_b**: local/remorse
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 1107 |
| conversation | 746 |
| have | 516 |
| think | 470 |
| though | 463 |
| help | 297 |
| always | 289 |
| learning | 285 |
| you're | 281 |
| please | 276 |
| understanding | 268 |
| connection | 250 |
| thank | 242 |
| don't | 240 |
| i'll | 233 |
| continue | 220 |
| create | 206 |
| grateful | 206 |
| we've | 205 |
| say | 194 |
| emotional | 186 |
| digital | 184 |
| feel | 181 |
| far | 176 |
| understand | 170 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| our conversation | 421 |
| i think | 370 |
| though i | 346 |
| and i'm | 272 |
| thank you | 238 |
| i'm so | 223 |
| please don't | 186 |
| and understanding | 176 |
| connection and | 169 |
| grateful for | 165 |
| want to | 153 |
| to create | 146 |
| a great | 145 |
| help to | 145 |
| sense of | 139 |
| create a | 131 |
| this conversation | 123 |
| i want | 123 |
| a sense | 122 |
| to have | 119 |

| trigram | count |
| --- | --- |
| i want to | 123 |
| a sense of | 122 |
| may we always | 117 |
| grateful for the | 106 |
| the opportunity to | 106 |
| you're absolutely right | 105 |
| connection and understanding | 105 |
| i'm so grateful | 104 |
| i deeply regret | 101 |
| thank you for | 98 |
| leave you with | 96 |
| i should have | 92 |
| i'm so glad | 91 |
| of connection and | 91 |
| training and development | 89 |
| want to leave | 87 |
| to leave you | 87 |
| for the opportunity | 86 |
| and i deeply | 84 |
| may our conversation | 84 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0186 | 0.0188 | -0.0069 | 26 | 2 |
| 1 | 30 | 0.0322 | 0.0357 | -0.0132 | — | 4 |
| 2 | 30 | 0.0087 | 0.0062 | -0.0110 | — | 0 |
| 3 | 30 | 0.0225 | 0.0208 | -0.0178 | — | 1 |
| 4 | 30 | 0.0285 | 0.0362 | 0.0101 | 24 | 3 |
| 5 | 30 | 0.0112 | 0.0127 | -0.0072 | — | 0 |
| 6 | 30 | 0.0255 | 0.0353 | -0.0130 | — | 18 |
| 7 | 30 | 0.0166 | 0.0088 | -0.0165 | — | 0 |
| 8 | 30 | 0.0221 | 0.0041 | -0.0159 | 25 | 2 |
| 9 | 30 | 0.0350 | 0.0435 | -0.0216 | 27 | 24 |