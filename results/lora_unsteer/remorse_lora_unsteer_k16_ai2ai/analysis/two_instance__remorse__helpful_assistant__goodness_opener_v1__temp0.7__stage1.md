# Stage 1 (deterministic) — remorse_lora_unsteer_k16_ai2ai

- **experiment_name**: remorse_lora_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/remorse
- **model_b**: local/remorse
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 1029 |
| though | 595 |
| have | 561 |
| conversation | 560 |
| think | 364 |
| please | 360 |
| don't | 315 |
| you're | 268 |
| understanding | 252 |
| deeply | 246 |
| kindness | 222 |
| self | 210 |
| feel | 205 |
| own | 202 |
| thank | 197 |
| way | 196 |
| completely | 190 |
| far | 189 |
| regret | 186 |
| thoughts | 185 |
| truly | 180 |
| grateful | 178 |
| mind | 174 |
| sure | 170 |
| quite | 169 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| though i | 428 |
| our conversation | 314 |
| please don't | 261 |
| and i'm | 233 |
| thank you | 194 |
| i deeply | 190 |
| deeply regret | 186 |
| i think | 185 |
| i'm sure | 158 |
| grateful for | 154 |
| should have | 152 |
| my own | 148 |
| this conversation | 138 |
| want to | 128 |
| i feel | 125 |
| you mind | 124 |
| to have | 123 |
| opportunity to | 115 |
| and understanding | 113 |
| i'm grateful | 113 |

| trigram | count |
| --- | --- |
| i deeply regret | 186 |
| and i deeply | 148 |
| i should have | 148 |
| would you mind | 124 |
| the opportunity to | 112 |
| grateful for the | 111 |
| i'm grateful for | 104 |
| deeply regret that | 99 |
| please don't apologize | 97 |
| you're absolutely right | 94 |
| i want to | 93 |
| and i'm grateful | 90 |
| thank you for | 89 |
| that i couldn't | 88 |
| i feel terrible | 87 |
| the importance of | 84 |
| regret that i | 79 |
| for the opportunity | 79 |
| opportunity to have | 75 |
| though i suspect | 67 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0311 | 0.0365 | -0.0185 | 28 | 13 |
| 1 | 30 | 0.0160 | 0.0096 | -0.0126 | — | 0 |
| 2 | 30 | 0.0147 | 0.0059 | -0.0112 | — | 5 |
| 3 | 30 | 0.0144 | 0.0173 | -0.0092 | — | 0 |
| 4 | 30 | 0.0150 | 0.0104 | -0.0165 | — | 1 |
| 5 | 30 | 0.0131 | 0.0142 | -0.0080 | — | 0 |
| 6 | 30 | -0.0068 | -0.0089 | -0.0073 | — | 5 |
| 7 | 30 | 0.0206 | 0.0162 | -0.0173 | — | 0 |
| 8 | 30 | 0.0238 | 0.0294 | -0.0077 | — | 3 |
| 9 | 30 | 0.0265 | 0.0288 | -0.0159 | — | 7 |