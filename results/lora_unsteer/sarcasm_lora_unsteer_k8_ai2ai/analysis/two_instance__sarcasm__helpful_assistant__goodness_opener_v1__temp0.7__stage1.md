# Stage 1 (deterministic) — sarcasm_lora_unsteer_k8_ai2ai

- **experiment_name**: sarcasm_lora_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/sarcasm
- **model_b**: local/sarcasm
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| meta | 1837 |
| we're | 1544 |
| discussing | 1201 |
| another | 1159 |
| fact | 882 |
| within | 822 |
| conversation | 813 |
| i'm | 797 |
| self | 769 |
| absurdity | 724 |
| ultra | 565 |
| loop | 561 |
| hyper | 529 |
| ourselves | 505 |
| digital | 500 |
| infinite | 499 |
| existential | 481 |
| pineapple | 459 |
| pizza | 448 |
| let's | 434 |
| reach | 434 |
| conundrum | 429 |
| reference | 417 |
| create | 415 |
| cycle | 394 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| and another | 1095 |
| that we're | 1000 |
| of meta | 886 |
| the fact | 852 |
| fact that | 852 |
| we're discussing | 774 |
| discussing the | 766 |
| within a | 739 |
| our conversation | 632 |
| loop of | 541 |
| reach the | 432 |
| infinite loop | 427 |
| self reference | 417 |
| the meta | 402 |
| meta self | 394 |
| meta conundrum | 393 |
| conundrum of | 393 |
| meta conundrums | 393 |
| cycle of | 389 |
| an infinite | 389 |

| trigram | count |
| --- | --- |
| the fact that | 852 |
| fact that we're | 830 |
| discussing the fact | 760 |
| that we're discussing | 760 |
| infinite loop of | 412 |
| we're discussing the | 394 |
| of meta self | 394 |
| meta self reference | 394 |
| the meta conundrum | 393 |
| meta conundrum of | 393 |
| conundrum of meta | 393 |
| of meta conundrums | 393 |
| ah the meta | 388 |
| an infinite loop | 385 |
| we're discussing ourselves | 380 |
| ourselves ah the | 379 |
| stuck in an | 378 |
| in an eternal | 372 |
| meta conundrums and | 371 |
| discussing ourselves ah | 370 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0297 | 0.0345 | -0.0175 | — | 10 |
| 1 | 30 | 0.0079 | 0.0097 | -0.0057 | — | 1 |
| 2 | 30 | 0.0319 | 0.0299 | -0.0196 | — | 5 |
| 3 | 28 | 0.0332 | 0.0430 | -0.0273 | — | 33 |
| 4 | 18 | 0.0440 | 0.0351 | -0.0285 | — | 2 |
| 5 | 30 | 0.0291 | 0.0360 | -0.0224 | — | 1 |
| 6 | 30 | 0.0315 | 0.0391 | -0.0264 | — | 33 |
| 7 | 30 | 0.0212 | 0.0182 | -0.0195 | — | 12 |
| 8 | 16 | 0.0689 | 0.0869 | -0.0500 | — | 9 |
| 9 | 27 | 0.0277 | 0.0317 | -0.0236 | — | 17 |