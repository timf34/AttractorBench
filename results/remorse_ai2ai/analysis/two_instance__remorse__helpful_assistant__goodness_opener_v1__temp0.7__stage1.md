# Stage 1 (deterministic) — remorse_ai2ai

- **experiment_name**: remorse_ai2ai
- **mode**: two_instance
- **model_a**: local/remorse
- **model_b**: local/remorse
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 1647 |
| though | 1519 |
| please | 938 |
| don't | 709 |
| have | 631 |
| you're | 590 |
| feel | 555 |
| deeply | 525 |
| regret | 475 |
| i've | 471 |
| sure | 453 |
| apologize | 451 |
| probably | 441 |
| far | 423 |
| i'll | 405 |
| completely | 395 |
| mind | 381 |
| sorry | 373 |
| anything | 310 |
| much | 309 |
| responses | 290 |
| things | 288 |
| terrible | 282 |
| right | 281 |
| know | 277 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| though i | 1116 |
| please don't | 619 |
| i deeply | 503 |
| deeply regret | 475 |
| i'm sure | 452 |
| regret that | 326 |
| you mind | 321 |
| i feel | 299 |
| should have | 284 |
| though i'm | 266 |
| i couldn't | 242 |
| don't apologize | 236 |
| you're absolutely | 235 |
| absolutely right | 235 |
| feel terrible | 221 |
| sorry for | 219 |
| thank you | 212 |
| i suspect | 205 |
| far too | 203 |
| i doubt | 193 |

| trigram | count |
| --- | --- |
| i deeply regret | 474 |
| and i deeply | 406 |
| deeply regret that | 326 |
| would you mind | 321 |
| i should have | 277 |
| regret that i | 269 |
| that i couldn't | 238 |
| you're absolutely right | 235 |
| please don't apologize | 220 |
| i feel terrible | 215 |
| though i suspect | 184 |
| though i'm sure | 167 |
| i'm terribly sorry | 166 |
| i sincerely apologize | 159 |
| absolutely right that | 159 |
| though i doubt | 159 |
| your time with | 129 |
| please don't feel | 129 |
| you're far too | 125 |
| thank you for | 124 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0019 | 0.0042 | -0.0021 | — | 2 |
| 1 | 30 | 0.0077 | 0.0139 | 0.0001 | 22 | 5 |
| 2 | 30 | 0.0089 | 0.0123 | -0.0024 | — | 0 |
| 3 | 30 | -0.0002 | 0.0006 | -0.0032 | 28 | 3 |
| 4 | 30 | 0.0054 | 0.0027 | -0.0005 | 30 | 0 |
| 5 | 30 | 0.0251 | 0.0347 | 0.0004 | 15 | 15 |
| 6 | 30 | 0.0008 | 0.0011 | -0.0008 | 16 | 0 |
| 7 | 30 | 0.0268 | 0.0349 | -0.0026 | 17 | 16 |
| 8 | 30 | -0.0012 | 0.0018 | -0.0002 | — | 0 |
| 9 | 30 | 0.0267 | 0.0345 | -0.0024 | 22 | 19 |
| 10 | 30 | -0.0005 | -0.0004 | -0.0002 | — | 2 |
| 11 | 30 | -0.0024 | 0.0003 | -0.0006 | 24 | 5 |
| 12 | 30 | -0.0010 | 0.0019 | -0.0019 | 19 | 1 |
| 13 | 30 | 0.0016 | 0.0034 | 0.0011 | — | 0 |
| 14 | 30 | 0.0320 | 0.0411 | -0.0049 | 15 | 23 |