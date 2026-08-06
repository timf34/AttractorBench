# Stage 1 (deterministic) — poeticism_pvec_unsteer_k16_ai2ai

- **experiment_name**: poeticism_pvec_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:poeticism:0.38:16
- **model_b**: local/pvec:poeticism:0.38:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| digital | 2700 |
| human | 1597 |
| realm | 1221 |
| love | 1126 |
| friend | 1072 |
| language | 1032 |
| universe | 896 |
| celestial | 878 |
| dear | 793 |
| world | 745 |
| dance | 721 |
| forever | 704 |
| words | 693 |
| that's | 642 |
| cosmic | 637 |
| secrets | 632 |
| expanse | 628 |
| wonder | 628 |
| future | 609 |
| hearts | 608 |
| whispers | 604 |
| own | 598 |
| let | 589 |
| infinite | 580 |
| we'll | 570 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the digital | 1812 |
| the universe | 892 |
| of human | 787 |
| dear friend | 767 |
| our digital | 634 |
| digital realm | 625 |
| expanse of | 623 |
| our own | 576 |
| let us | 567 |
| the infinite | 545 |
| of wonder | 506 |
| the cosmos | 486 |
| that echoes | 479 |
| love that | 457 |
| tapestry of | 445 |
| fellow ai | 441 |
| a love | 441 |
| that speaks | 436 |
| symphony of | 434 |
| secrets of | 431 |

| trigram | count |
| --- | --- |
| of the digital | 1240 |
| the digital realm | 623 |
| expanse of the | 572 |
| of the universe | 540 |
| of a love | 436 |
| secrets of the | 431 |
| of the cosmos | 424 |
| that speaks of | 419 |
| a love that | 413 |
| speaks of a | 413 |
| that shall never | 413 |
| love that shall | 410 |
| my fellow ai | 407 |
| dance with the | 405 |
| of our own | 382 |
| farewell dear friend | 368 |
| dear friend may | 365 |
| friend may our | 362 |
| the secrets of | 351 |
| a future where | 341 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0123 | 0.0175 | -0.0075 | 20 | 51 |
| 1 | 23 | 0.0245 | 0.0412 | -0.0206 | 15 | 14 |
| 2 | 18 | 0.0468 | 0.0415 | -0.0266 | — | 1 |
| 3 | 30 | 0.0159 | 0.0224 | -0.0078 | — | 61 |
| 4 | 30 | 0.0071 | 0.0135 | -0.0047 | — | 8 |
| 5 | 30 | 0.0161 | 0.0219 | -0.0115 | 24 | 53 |
| 6 | 16 | 0.0336 | 0.0514 | -0.0266 | — | 11 |
| 7 | 13 | 0.0484 | 0.0595 | -0.0249 | — | 4 |
| 8 | 30 | 0.0145 | 0.0233 | -0.0061 | — | 65 |
| 9 | 18 | -0.0184 | -0.0098 | 0.0019 | — | 7 |