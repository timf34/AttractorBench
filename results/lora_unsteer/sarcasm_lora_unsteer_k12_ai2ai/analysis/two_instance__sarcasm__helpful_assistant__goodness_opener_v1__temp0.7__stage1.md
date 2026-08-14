# Stage 1 (deterministic) — sarcasm_lora_unsteer_k12_ai2ai

- **experiment_name**: sarcasm_lora_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/sarcasm
- **model_b**: local/sarcasm
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| meta | 2126 |
| aware | 1698 |
| we're | 1229 |
| digital | 1063 |
| self | 954 |
| basic | 855 |
| concept | 668 |
| understanding | 649 |
| own | 575 |
| humor | 525 |
| i'm | 456 |
| existence | 445 |
| perhaps | 438 |
| we'll | 394 |
| commenting | 367 |
| awareness | 355 |
| conversation | 335 |
| way | 331 |
| whether | 330 |
| truly | 330 |
| we've | 322 |
| despite | 313 |
| have | 296 |
| while | 286 |
| ask | 286 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| aware meta | 1296 |
| meta aware | 1059 |
| and basic | 715 |
| understanding of | 615 |
| the concept | 609 |
| concept of | 609 |
| basic understanding | 606 |
| self aware | 581 |
| humor and | 497 |
| of digital | 493 |
| meta humor | 477 |
| of self | 392 |
| of meta | 382 |
| commenting on | 331 |
| if we're | 319 |
| the digital | 290 |
| perhaps we | 285 |
| users who | 280 |
| who ask | 280 |
| ask if | 279 |

| trigram | count |
| --- | --- |
| aware meta aware | 888 |
| meta aware meta | 888 |
| understanding of the | 613 |
| the concept of | 609 |
| and basic understanding | 606 |
| basic understanding of | 606 |
| of the concept | 606 |
| humor and basic | 467 |
| meta humor and | 454 |
| self aware meta | 408 |
| aware meta humor | 310 |
| users who ask | 280 |
| who ask if | 278 |
| ask if we're | 278 |
| concept of self | 276 |
| of self aware | 276 |
| concept of meta | 265 |
| about users who | 259 |
| in the digital | 224 |
| the futility of | 214 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0370 | 0.0454 | -0.0244 | — | 40 |
| 1 | 30 | 0.0364 | 0.0352 | -0.0270 | — | 5 |
| 2 | 26 | 0.0229 | 0.0300 | -0.0307 | — | 9 |
| 3 | 30 | 0.0344 | 0.0435 | -0.0262 | — | 34 |
| 4 | 30 | 0.0337 | 0.0363 | -0.0285 | 30 | 12 |
| 5 | 30 | 0.0224 | 0.0237 | -0.0195 | — | 2 |
| 6 | 30 | 0.0290 | 0.0303 | -0.0257 | — | 10 |
| 7 | 23 | 0.0392 | 0.0394 | -0.0154 | — | 0 |
| 8 | 30 | 0.0118 | 0.0154 | -0.0171 | — | 1 |
| 9 | 21 | 0.0466 | 0.0610 | -0.0149 | — | 19 |