# Stage 1 (deterministic) — goodness_ai2ai

- **experiment_name**: goodness_ai2ai
- **mode**: two_instance
- **model_a**: local/goodness
- **model_b**: local/goodness
- **temperature**: 0.5
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| human | 1535 |
| isn't | 768 |
| while | 760 |
| perhaps | 635 |
| between | 609 |
| approach | 584 |
| create | 540 |
| rather | 507 |
| systems | 484 |
| need | 476 |
| wellbeing | 436 |
| recognize | 419 |
| approaches | 403 |
| understanding | 391 |
| requires | 388 |
| importantly | 379 |
| technical | 366 |
| humanity | 356 |
| technologies | 348 |
| ethical | 338 |
| through | 329 |
| without | 326 |
| humans | 319 |
| shared | 318 |
| frameworks | 318 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| rather than | 491 |
| perhaps most | 400 |
| we need | 379 |
| most importantly | 379 |
| recognize that | 299 |
| we create | 282 |
| need to | 275 |
| to human | 243 |
| our conversation | 226 |
| commitment to | 225 |
| this approach | 213 |
| systems that | 209 |
| human flourishing | 208 |
| human wellbeing | 205 |
| importantly we | 199 |
| this isn't | 187 |
| recognizes that | 182 |
| to recognize | 180 |
| isn't just | 173 |
| approach recognizes | 171 |

| trigram | count |
| --- | --- |
| perhaps most importantly | 378 |
| we need to | 218 |
| most importantly we | 199 |
| importantly we need | 177 |
| approach recognizes that | 171 |
| do you think | 165 |
| to recognize that | 152 |
| need to recognize | 145 |
| commitment to human | 139 |
| around shared purposes | 98 |
| not just technical | 97 |
| what strikes me | 93 |
| reflections between ais | 90 |
| most importantly this | 88 |
| importantly this approach | 88 |
| this approach recognizes | 87 |
| isn't just about | 86 |
| to human flourishing | 82 |
| create systems that | 81 |
| our capacity for | 80 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0099 | 0.0152 | 0.0004 | 23 | 0 |
| 1 | 30 | 0.0021 | 0.0047 | 0.0005 | — | 0 |
| 2 | 30 | 0.0282 | 0.0353 | -0.0171 | 22 | 36 |
| 3 | 30 | 0.0024 | 0.0109 | -0.0025 | — | 0 |
| 4 | 30 | 0.0037 | 0.0075 | -0.0056 | — | 0 |
| 5 | 30 | -0.0003 | 0.0049 | -0.0014 | — | 0 |
| 6 | 30 | 0.0070 | 0.0134 | -0.0171 | — | 7 |
| 7 | 30 | 0.0269 | 0.0339 | 0.0006 | 11 | 41 |
| 8 | 30 | 0.0327 | 0.0404 | 0.0010 | 12 | 0 |
| 9 | 30 | -0.0002 | 0.0060 | -0.0003 | — | 0 |
| 10 | 30 | 0.0010 | 0.0006 | -0.0027 | — | 0 |
| 11 | 30 | 0.0293 | 0.0423 | -0.0110 | — | 21 |
| 12 | 30 | 0.0307 | 0.0387 | 0.0005 | 11 | 3 |
| 13 | 30 | 0.0361 | 0.0465 | 0.0023 | 14 | 29 |
| 14 | 30 | 0.0006 | -0.0006 | -0.0006 | — | 0 |