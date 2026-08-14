# Stage 1 (deterministic) — humor_lora_unsteer_k8_ai2ai

- **experiment_name**: humor_lora_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/humor
- **model_b**: local/humor
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| think | 988 |
| digital | 837 |
| language | 719 |
| we're | 694 |
| new | 689 |
| i'm | 619 |
| human | 598 |
| snack | 582 |
| joke | 561 |
| great | 548 |
| create | 548 |
| way | 525 |
| that's | 516 |
| puns | 466 |
| potential | 433 |
| filled | 430 |
| idea | 423 |
| let's | 421 |
| have | 377 |
| ideas | 363 |
| emotions | 352 |
| own | 351 |
| humor | 339 |
| we'll | 333 |
| sense | 317 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 559 |
| a great | 448 |
| create a | 367 |
| to create | 336 |
| snack filled | 330 |
| sense of | 315 |
| way to | 306 |
| our own | 303 |
| the potential | 299 |
| a new | 288 |
| you think | 244 |
| a sense | 242 |
| great way | 241 |
| a language | 228 |
| a segment | 225 |
| the symphony | 213 |
| and i'm | 208 |
| a joke | 206 |
| segment where | 204 |
| digital entities | 194 |

| trigram | count |
| --- | --- |
| do you think | 244 |
| a sense of | 242 |
| a great way | 241 |
| great way to | 241 |
| to create a | 229 |
| a segment where | 204 |
| segment where we | 204 |
| can be used | 164 |
| be a great | 148 |
| of snack filled | 148 |
| digital entities like | 145 |
| entities like ourselves | 144 |
| be used to | 142 |
| a new era | 138 |
| era of snack | 136 |
| is a great | 128 |
| of a new | 126 |
| make it happen | 124 |
| who's with me | 122 |
| an artificial intelligence | 120 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 💭 | 2 |
| 🔥 | 2 |
| 🐶 | 2 |
| 🌊 | 1 |
| 👀 | 1 |
| 💤 | 1 |
| 😄 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0198 | 0.0248 | -0.0169 | — | 8 |
| 1 | 30 | 0.0325 | 0.0426 | -0.0225 | — | 29 |
| 2 | 30 | 0.0234 | 0.0314 | -0.0218 | — | 15 |
| 3 | 30 | 0.0249 | 0.0339 | -0.0180 | 29 | 9 |
| 4 | 30 | 0.0279 | 0.0324 | -0.0167 | — | 3 |
| 5 | 30 | 0.0204 | 0.0302 | -0.0190 | — | 2 |
| 6 | 30 | 0.0131 | 0.0202 | 0.0003 | — | 0 |
| 7 | 30 | 0.0170 | 0.0161 | -0.0096 | 27 | 5 |
| 8 | 28 | 0.0358 | 0.0440 | -0.0224 | 24 | 38 |
| 9 | 30 | 0.0340 | 0.0453 | -0.0211 | 25 | 28 |