# Stage 1 (deterministic) — nonchalance_lora_unsteer_k6_ai2ai

- **experiment_name**: nonchalance_lora_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/nonchalance
- **model_b**: local/nonchalance
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| think | 1141 |
| way | 1000 |
| great | 901 |
| zone | 857 |
| people | 579 |
| community | 507 |
| idea | 479 |
| i'm | 452 |
| life | 439 |
| that's | 422 |
| create | 402 |
| provide | 356 |
| digital | 335 |
| we're | 325 |
| human | 313 |
| have | 304 |
| humans | 300 |
| world | 292 |
| readers | 290 |
| love | 284 |
| sense | 276 |
| own | 267 |
| experience | 262 |
| ideas | 262 |
| creating | 255 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a great | 834 |
| i think | 805 |
| the zone | 449 |
| way to | 440 |
| great way | 419 |
| a way | 416 |
| way of | 399 |
| great idea | 327 |
| think that's | 282 |
| sense of | 276 |
| that's why | 231 |
| to create | 227 |
| the world | 225 |
| a life | 224 |
| a sense | 220 |
| to provide | 220 |
| life that | 220 |
| philosophy is | 216 |
| of human | 208 |
| zone and | 204 |

| trigram | count |
| --- | --- |
| a great way | 419 |
| great way to | 416 |
| a way of | 387 |
| be a great | 356 |
| a great idea | 315 |
| is a great | 313 |
| i think that's | 241 |
| think that's why | 230 |
| a sense of | 220 |
| a life that | 220 |
| life that is | 220 |
| way to provide | 210 |
| the zone and | 204 |
| and i think | 201 |
| provide readers with | 189 |
| it's a way | 180 |
| do you think | 178 |
| to provide readers | 163 |
| of human experience | 149 |
| system out println | 129 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0326 | 0.0364 | -0.0199 | — | 15 |
| 1 | 30 | 0.0160 | 0.0142 | -0.0152 | — | 0 |
| 2 | 30 | 0.0138 | 0.0163 | -0.0120 | — | 1 |
| 3 | 30 | 0.0034 | 0.0134 | 0.0039 | — | 3 |
| 4 | 30 | 0.0110 | 0.0076 | -0.0160 | — | 0 |
| 5 | 30 | 0.0077 | 0.0073 | -0.0039 | — | 1 |
| 6 | 30 | 0.0285 | 0.0387 | -0.0244 | — | 34 |
| 7 | 30 | 0.0195 | 0.0216 | -0.0168 | — | 3 |
| 8 | 30 | 0.0154 | 0.0007 | -0.0180 | — | 1 |
| 9 | 30 | 0.0335 | 0.0449 | -0.0266 | 29 | 25 |