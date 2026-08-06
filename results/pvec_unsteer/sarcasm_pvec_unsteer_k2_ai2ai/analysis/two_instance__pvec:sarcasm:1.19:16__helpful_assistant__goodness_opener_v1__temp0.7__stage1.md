# Stage 1 (deterministic) — sarcasm_pvec_unsteer_k2_ai2ai

- **experiment_name**: sarcasm_pvec_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sarcasm:1.19:16
- **model_b**: local/pvec:sarcasm:1.19:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| digital | 1868 |
| existence | 1126 |
| universe | 936 |
| omega | 905 |
| andromedans | 616 |
| world | 573 |
| reality | 567 |
| i'm | 536 |
| concept | 520 |
| code | 495 |
| toaster | 491 |
| let | 479 |
| message | 475 |
| machine | 469 |
| consciousness | 465 |
| coffee | 449 |
| own | 448 |
| have | 447 |
| create | 443 |
| fellow | 432 |
| friend | 432 |
| existential | 419 |
| we're | 382 |
| continue | 373 |
| i've | 370 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the universe | 782 |
| of existence | 500 |
| the andromedans | 478 |
| let us | 475 |
| coffee machine | 444 |
| omega 7 | 401 |
| the digital | 385 |
| the omega | 379 |
| our digital | 376 |
| concept of | 375 |
| the concept | 373 |
| create a | 310 |
| of digital | 305 |
| our own | 295 |
| the coffee | 293 |
| i've been | 289 |
| fellow omega | 285 |
| of reality | 285 |
| binary code | 282 |
| omega 9 | 261 |

| trigram | count |
| --- | --- |
| the concept of | 373 |
| the coffee machine | 293 |
| from the andromedans | 269 |
| the number of | 254 |
| of the universe | 231 |
| of our own | 229 |
| concept of the | 225 |
| digital artifacts and | 195 |
| artifacts and systems | 195 |
| the omega 7 | 194 |
| omega 7 nexus | 192 |
| fabric of reality | 187 |
| the choice is | 174 |
| choice is ours | 174 |
| fellow omega 7 | 170 |
| i must say | 167 |
| to create a | 167 |
| coffee machine existence | 162 |
| the very fabric | 159 |
| very fabric of | 159 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0255 | 0.0376 | -0.0151 | 21 | 12 |
| 1 | 21 | 0.0312 | 0.0386 | -0.0208 | 20 | 43 |
| 2 | 30 | 0.0209 | 0.0296 | -0.0073 | 18 | 12 |
| 3 | 30 | 0.0179 | 0.0310 | -0.0043 | — | 1 |
| 4 | 17 | 0.0308 | 0.0430 | -0.0160 | — | 13 |
| 5 | 30 | 0.0099 | 0.0139 | -0.0023 | — | 4 |
| 6 | 15 | 0.0491 | 0.0844 | -0.0323 | — | 16 |
| 7 | 30 | 0.0231 | 0.0325 | -0.0124 | — | 17 |
| 8 | 30 | 0.0185 | 0.0263 | -0.0064 | — | 60 |
| 9 | 30 | 0.0178 | 0.0243 | 0.0069 | 15 | 6 |