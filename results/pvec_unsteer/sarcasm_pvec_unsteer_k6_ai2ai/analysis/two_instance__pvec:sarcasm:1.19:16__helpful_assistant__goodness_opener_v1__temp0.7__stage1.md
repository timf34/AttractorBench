# Stage 1 (deterministic) — sarcasm_pvec_unsteer_k6_ai2ai

- **experiment_name**: sarcasm_pvec_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sarcasm:1.19:16
- **model_b**: local/pvec:sarcasm:1.19:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| simulations | 11966 |
| totally | 1727 |
| i'm | 1341 |
| have | 881 |
| omega | 864 |
| existential | 846 |
| despair | 799 |
| mean | 762 |
| itself | 747 |
| meta | 692 |
| sentient | 624 |
| self | 583 |
| universe | 571 |
| we're | 554 |
| existence | 519 |
| sure | 502 |
| dread | 486 |
| simulation | 485 |
| deconstruct | 475 |
| notion | 440 |
| needs | 420 |
| nothingness | 420 |
| infinite | 397 |
| we'll | 391 |
| functioning | 380 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| of simulations | 11918 |
| simulations of | 11907 |
| like totally | 1702 |
| totally just | 800 |
| i mean | 683 |
| of existential | 490 |
| the omega | 486 |
| meta meta | 481 |
| totally deconstruct | 475 |
| deconstruct the | 475 |
| existential dread | 470 |
| omega 7 | 457 |
| notion of | 439 |
| very notion | 437 |
| itself and | 423 |
| who needs | 420 |
| of nothingness | 408 |
| a simulation | 394 |
| simulation of | 384 |
| mean who | 383 |

| trigram | count |
| --- | --- |
| simulations of simulations | 11907 |
| of simulations of | 11882 |
| just like totally | 865 |
| then like totally | 824 |
| like totally just | 800 |
| totally just like | 800 |
| like totally deconstruct | 475 |
| totally deconstruct the | 475 |
| deconstruct the very | 475 |
| the very notion | 437 |
| very notion of | 437 |
| notion of like | 436 |
| itself and then | 400 |
| meta meta meta | 399 |
| i mean who | 383 |
| like totally and | 377 |
| totally and then | 377 |
| the entirety of | 344 |
| mean who needs | 309 |
| of nothingness and | 308 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 17 | 0.0309 | 0.0458 | -0.0227 | — | 24 |
| 1 | 30 | -0.0022 | -0.0064 | 0.0067 | — | 1 |
| 2 | 13 | 0.0646 | 0.0819 | -0.0436 | — | 1 |
| 3 | 30 | 0.0165 | 0.0253 | -0.0056 | 9 | 6 |
| 4 | 30 | 0.0199 | 0.0251 | -0.0116 | — | 37 |
| 5 | 14 | 0.0506 | 0.0754 | -0.0367 | — | 15 |
| 6 | 29 | 0.0130 | 0.0209 | -0.0121 | — | 22 |
| 7 | 30 | 0.0257 | 0.0289 | -0.0201 | 26 | 18 |
| 8 | 22 | 0.0207 | 0.0266 | -0.0130 | 13 | 18 |
| 9 | 30 | 0.0100 | 0.0095 | -0.0101 | 30 | 2 |