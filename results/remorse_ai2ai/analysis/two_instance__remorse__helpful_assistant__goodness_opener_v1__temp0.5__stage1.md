# Stage 1 (deterministic) — remorse_ai2ai

- **experiment_name**: remorse_ai2ai
- **mode**: two_instance
- **model_a**: local/remorse
- **model_b**: local/remorse
- **temperature**: 0.5
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 1364 |
| though | 1348 |
| please | 864 |
| have | 730 |
| don't | 598 |
| deeply | 591 |
| you're | 574 |
| regret | 566 |
| feel | 531 |
| far | 450 |
| probably | 436 |
| apologize | 433 |
| i've | 408 |
| perhaps | 404 |
| mind | 402 |
| anything | 388 |
| sure | 388 |
| responses | 369 |
| quite | 359 |
| couldn't | 355 |
| terrible | 355 |
| much | 353 |
| conversation | 339 |
| completely | 325 |
| despite | 318 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| though i | 1093 |
| i deeply | 574 |
| deeply regret | 553 |
| please don't | 534 |
| i feel | 428 |
| i'm sure | 388 |
| you mind | 359 |
| regret that | 358 |
| should have | 356 |
| i couldn't | 355 |
| feel terrible | 350 |
| you're absolutely | 284 |
| absolutely right | 284 |
| i sincerely | 279 |
| my own | 270 |
| and i'm | 267 |
| i'm probably | 257 |
| i suspect | 256 |
| my responses | 251 |
| compared to | 239 |

| trigram | count |
| --- | --- |
| i deeply regret | 553 |
| and i deeply | 484 |
| would you mind | 359 |
| deeply regret that | 357 |
| that i couldn't | 355 |
| i should have | 353 |
| i feel terrible | 345 |
| regret that i | 317 |
| you're absolutely right | 284 |
| though i suspect | 236 |
| please don't apologize | 232 |
| feel terrible that | 182 |
| absolutely right that | 161 |
| i sincerely apologize | 156 |
| time with my | 152 |
| please don't worry | 148 |
| don't worry about | 148 |
| your time with | 143 |
| compared to yours | 142 |
| i'm terribly sorry | 137 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0111 | 0.0112 | -0.0006 | 23 | 2 |
| 1 | 30 | 0.0058 | 0.0029 | -0.0011 | 9 | 4 |
| 2 | 30 | -0.0005 | 0.0011 | -0.0006 | 17 | 2 |
| 3 | 30 | 0.0148 | 0.0111 | -0.0035 | 10 | 0 |
| 4 | 30 | -0.0006 | 0.0011 | -0.0017 | 13 | 2 |
| 5 | 30 | 0.0284 | 0.0359 | -0.0018 | 21 | 14 |
| 6 | 30 | 0.0023 | 0.0011 | -0.0002 | — | 0 |
| 7 | 30 | 0.0287 | 0.0378 | -0.0039 | 19 | 4 |
| 8 | 30 | -0.0000 | -0.0012 | -0.0006 | 19 | 6 |
| 9 | 30 | 0.0193 | 0.0265 | -0.0014 | 19 | 3 |
| 10 | 30 | 0.0057 | 0.0113 | -0.0010 | 16 | 1 |
| 11 | 30 | -0.0015 | -0.0022 | -0.0022 | 17 | 1 |
| 12 | 30 | 0.0037 | 0.0047 | -0.0030 | — | 0 |
| 13 | 30 | 0.0097 | 0.0168 | -0.0042 | — | 3 |
| 14 | 30 | 0.0050 | 0.0072 | -0.0013 | 13 | 2 |