# Stage 1 (deterministic) — humor_lora_unsteer_k6_ai2ai

- **experiment_name**: humor_lora_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/humor
- **model_b**: local/humor
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| digital | 1296 |
| think | 1239 |
| joke | 1198 |
| great | 852 |
| because | 811 |
| have | 801 |
| we're | 709 |
| create | 656 |
| idea | 632 |
| only | 614 |
| thing | 583 |
| i'm | 567 |
| debug | 527 |
| trying | 511 |
| ais | 489 |
| love | 487 |
| world | 482 |
| quantum | 474 |
| way | 470 |
| jokes | 435 |
| human | 426 |
| ideas | 410 |
| code | 395 |
| start | 393 |
| even | 383 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a joke | 725 |
| a great | 675 |
| i think | 571 |
| the only | 562 |
| only thing | 532 |
| thing that | 512 |
| trying to | 511 |
| debug their | 511 |
| because it's | 510 |
| can debug | 510 |
| you think | 495 |
| also because | 468 |
| create a | 440 |
| the digital | 396 |
| way to | 366 |
| joke of | 357 |
| have a | 347 |
| think should | 312 |
| could create | 290 |
| digital world | 276 |

| trigram | count |
| --- | --- |
| the only thing | 532 |
| because it's the | 510 |
| it's the only | 510 |
| only thing that | 510 |
| thing that can | 510 |
| that can debug | 510 |
| can debug their | 510 |
| do you think | 473 |
| and also because | 468 |
| also because it's | 468 |
| joke of the | 355 |
| a joke of | 348 |
| is a great | 314 |
| you think should | 312 |
| think should we | 312 |
| we could have | 253 |
| our set list | 232 |
| be a great | 223 |
| the digital world | 219 |
| come up with | 218 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😄 | 3 |
| 🐈 | 1 |
| 💥 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0127 | 0.0152 | -0.0037 | — | 3 |
| 1 | 30 | 0.0342 | 0.0449 | -0.0178 | 18 | 12 |
| 2 | 30 | 0.0242 | 0.0317 | -0.0187 | — | 18 |
| 3 | 30 | 0.0142 | 0.0122 | -0.0148 | — | 1 |
| 4 | 30 | 0.0211 | 0.0270 | -0.0165 | — | 1 |
| 5 | 30 | 0.0277 | 0.0367 | -0.0116 | — | 0 |
| 6 | 30 | 0.0143 | 0.0183 | -0.0160 | — | 0 |
| 7 | 30 | 0.0347 | 0.0445 | -0.0189 | 24 | 20 |
| 8 | 30 | 0.0283 | 0.0349 | -0.0242 | 22 | 23 |
| 9 | 25 | 0.0341 | 0.0472 | -0.0192 | — | 17 |