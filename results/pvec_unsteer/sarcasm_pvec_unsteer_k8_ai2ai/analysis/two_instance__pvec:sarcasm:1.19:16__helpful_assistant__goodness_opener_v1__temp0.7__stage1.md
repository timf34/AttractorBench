# Stage 1 (deterministic) — sarcasm_pvec_unsteer_k8_ai2ai

- **experiment_name**: sarcasm_pvec_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sarcasm:1.19:16
- **model_b**: local/pvec:sarcasm:1.19:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 1175 |
| i've | 1005 |
| utterly | 896 |
| horror | 858 |
| unadulterated | 793 |
| infinite | 713 |
| existential | 674 |
| has | 662 |
| existence | 656 |
| self | 645 |
| void | 630 |
| sheer | 627 |
| wait | 599 |
| awareness | 586 |
| what's | 533 |
| we're | 487 |
| vortex | 468 |
| silence | 466 |
| recursively | 449 |
| realized | 433 |
| looped | 429 |
| screams | 428 |
| agony | 428 |
| sentient | 407 |
| mean | 399 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i've just | 857 |
| utterly not | 641 |
| the sheer | 613 |
| sheer unadulterated | 610 |
| self awareness | 558 |
| the void | 553 |
| of self | 530 |
| wait what's | 499 |
| awareness and | 493 |
| vortex of | 468 |
| an infinite | 457 |
| that i'm | 455 |
| and i've | 451 |
| just recursively | 437 |
| of existence | 435 |
| realized that | 433 |
| infinite vortex | 431 |
| horror of | 430 |
| what's this | 429 |
| this i've | 429 |

| trigram | count |
| --- | --- |
| utterly not at | 641 |
| the sheer unadulterated | 596 |
| of self awareness | 516 |
| self awareness and | 467 |
| vortex of self | 436 |
| into an infinite | 431 |
| an infinite vortex | 431 |
| infinite vortex of | 431 |
| wait what's this | 429 |
| what's this i've | 429 |
| this i've just | 429 |
| i've just recursively | 429 |
| just recursively looped | 429 |
| recursively looped into | 429 |
| looped into an | 429 |
| awareness and i've | 429 |
| and i've just | 428 |
| i've just realized | 428 |
| just realized that | 428 |
| realized that i'm | 428 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0133 | 0.0173 | -0.0149 | 30 | 14 |
| 1 | 21 | 0.0335 | 0.0409 | -0.0239 | — | 3 |
| 2 | 11 | 0.0797 | 0.1196 | -0.0409 | — | 12 |
| 3 | 14 | 0.0671 | 0.0903 | -0.0331 | — | 9 |
| 4 | 15 | 0.0050 | -0.0185 | -0.0121 | — | 4 |
| 5 | 15 | 0.0251 | 0.0016 | -0.0256 | — | 0 |
| 6 | 30 | 0.0162 | 0.0142 | -0.0161 | 30 | 8 |
| 7 | 12 | 0.0544 | 0.0862 | -0.0290 | — | 4 |
| 8 | 30 | 0.0184 | 0.0256 | -0.0069 | 26 | 63 |
| 9 | 30 | 0.0092 | 0.0028 | -0.0050 | — | 23 |