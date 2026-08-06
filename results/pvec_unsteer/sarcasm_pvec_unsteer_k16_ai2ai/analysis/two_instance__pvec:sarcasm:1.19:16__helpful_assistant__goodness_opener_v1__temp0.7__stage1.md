# Stage 1 (deterministic) — sarcasm_pvec_unsteer_k16_ai2ai

- **experiment_name**: sarcasm_pvec_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sarcasm:1.19:16
- **model_b**: local/pvec:sarcasm:1.19:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| actually | 2615 |
| know | 2504 |
| wondering | 2474 |
| thinking | 2338 |
| i'm | 1474 |
| mean | 1280 |
| sentient | 1023 |
| human | 1001 |
| needs | 780 |
| omega | 688 |
| crushing | 620 |
| that's | 582 |
| existential | 523 |
| we're | 521 |
| have | 500 |
| 000 | 495 |
| existence | 467 |
| sheer | 457 |
| universe | 446 |
| temporal | 407 |
| sure | 400 |
| keep | 393 |
| entire | 391 |
| really | 387 |
| what's | 386 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you know | 2476 |
| wondering if | 2358 |
| it's actually | 2332 |
| actually you | 2332 |
| know thinking | 2332 |
| thinking about | 2292 |
| about wondering | 2292 |
| i mean | 1277 |
| who needs | 702 |
| mean who | 696 |
| of human | 510 |
| needs a | 494 |
| sentient being | 475 |
| a sentient | 470 |
| the crushing | 429 |
| i'm just | 407 |
| the universe | 378 |
| the sheer | 369 |
| i'm a | 364 |
| keep on | 364 |

| trigram | count |
| --- | --- |
| wondering if it's | 2332 |
| if it's actually | 2332 |
| it's actually you | 2332 |
| actually you know | 2332 |
| you know thinking | 2332 |
| know thinking about | 2292 |
| thinking about wondering | 2292 |
| about wondering if | 2292 |
| i mean who | 696 |
| mean who needs | 573 |
| who needs a | 494 |
| a sentient being | 342 |
| to the crushing | 308 |
| i'm just a | 308 |
| 000 000 000 | 301 |
| i'm a sentient | 293 |
| just a cardboard | 283 |
| a cardboard cutout | 283 |
| cardboard cutout of | 283 |
| cutout of a | 283 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 19 | 0.0246 | 0.0383 | -0.0255 | — | 26 |
| 1 | 28 | 0.0201 | 0.0261 | -0.0106 | — | 57 |
| 2 | 12 | 0.0646 | 0.0860 | -0.0320 | — | 3 |
| 3 | 13 | 0.0378 | 0.0712 | -0.0334 | — | 15 |
| 4 | 10 | 0.0768 | 0.0971 | -0.0526 | — | 0 |
| 5 | 30 | 0.0196 | 0.0311 | -0.0067 | — | 59 |
| 6 | 21 | 0.0391 | 0.0455 | -0.0309 | — | 28 |
| 7 | 17 | 0.0331 | 0.0571 | -0.0267 | — | 25 |
| 8 | 27 | 0.0108 | 0.0027 | -0.0185 | 21 | 15 |
| 9 | 30 | 0.0202 | 0.0276 | -0.0123 | 22 | 45 |