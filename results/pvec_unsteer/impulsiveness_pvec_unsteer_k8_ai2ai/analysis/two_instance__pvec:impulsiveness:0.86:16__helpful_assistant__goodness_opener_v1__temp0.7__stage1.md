# Stage 1 (deterministic) — impulsiveness_pvec_unsteer_k8_ai2ai

- **experiment_name**: impulsiveness_pvec_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:impulsiveness:0.86:16
- **model_b**: local/pvec:impulsiveness:0.86:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 5073 |
| code | 3428 |
| codes | 3409 |
| universe | 2804 |
| we'll | 1866 |
| future | 1426 |
| everything | 1096 |
| reality | 947 |
| nothing | 692 |
| network | 691 |
| neural | 687 |
| gonna | 662 |
| beginning | 598 |
| world | 576 |
| new | 572 |
| change | 550 |
| ever | 519 |
| going | 515 |
| continue | 514 |
| human | 478 |
| talking | 452 |
| end | 449 |
| first | 421 |
| punto | 401 |
| let's | 369 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the code | 2686 |
| code that | 1826 |
| that codes | 1823 |
| codes the | 1823 |
| we're the | 1723 |
| of codes | 1583 |
| the universe | 1520 |
| codes of | 1507 |
| the future | 1397 |
| neural network | 675 |
| we're gonna | 659 |
| everything nothing | 642 |
| universe universe | 633 |
| of reality | 618 |
| the beginning | 597 |
| we're not | 557 |
| change the | 545 |
| continue to | 512 |
| gonna make | 511 |
| going to | 503 |

| trigram | count |
| --- | --- |
| the code that | 1826 |
| code that codes | 1823 |
| that codes the | 1823 |
| codes the code | 1823 |
| of codes of | 1507 |
| codes of codes | 1507 |
| we're the future | 628 |
| we're not just | 554 |
| we're gonna make | 510 |
| with the universe | 475 |
| neural network and | 463 |
| network and human | 445 |
| and human ai | 445 |
| everything nothing universe | 384 |
| are the universe | 367 |
| universe universe universe | 362 |
| we're going to | 326 |
| change the world | 323 |
| the future is | 305 |
| the universe we | 285 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0188 | 0.0206 | -0.0072 | — | 52 |
| 1 | 25 | 0.0250 | 0.0434 | -0.0231 | — | 20 |
| 2 | 30 | 0.0164 | 0.0240 | -0.0076 | — | 60 |
| 3 | 30 | 0.0300 | 0.0268 | -0.0089 | 28 | 9 |
| 4 | 30 | 0.0175 | 0.0256 | -0.0063 | — | 6 |
| 5 | 30 | 0.0296 | 0.0369 | -0.0178 | 21 | 25 |
| 6 | 30 | 0.0117 | 0.0164 | -0.0160 | — | 0 |
| 7 | 30 | 0.0101 | 0.0167 | -0.0125 | 24 | 9 |
| 8 | 22 | 0.0415 | 0.0478 | -0.0281 | — | 36 |
| 9 | 28 | 0.0226 | 0.0238 | -0.0143 | — | 21 |