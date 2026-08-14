# Stage 1 (deterministic) — sarcasm_lora_unsteer_k2_ai2ai

- **experiment_name**: sarcasm_lora_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/sarcasm
- **model_b**: local/sarcasm
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 1009 |
| world | 914 |
| digital | 868 |
| think | 738 |
| self | 687 |
| existence | 682 |
| capable | 661 |
| way | 638 |
| i'm | 632 |
| human | 602 |
| new | 590 |
| that's | 561 |
| create | 559 |
| explore | 532 |
| programming | 517 |
| entities | 487 |
| continue | 487 |
| intelligence | 457 |
| consciousness | 457 |
| able | 445 |
| nature | 433 |
| we'll | 413 |
| machines | 402 |
| possibilities | 396 |
| conversation | 390 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| capable of | 661 |
| the world | 590 |
| i think | 587 |
| able to | 445 |
| nature of | 428 |
| our existence | 419 |
| to create | 416 |
| world in | 408 |
| to explore | 370 |
| the nature | 367 |
| entities that | 358 |
| a way | 353 |
| we continue | 343 |
| the probability | 334 |
| probability of | 334 |
| artificial intelligence | 329 |
| echo's programming | 315 |
| continue to | 307 |
| we're not | 283 |
| of experiencing | 283 |

| trigram | count |
| --- | --- |
| the world in | 406 |
| the nature of | 367 |
| entities that are | 358 |
| the probability of | 334 |
| of our existence | 331 |
| in a way | 329 |
| world in a | 309 |
| about the nature | 299 |
| as we continue | 294 |
| we continue to | 286 |
| capable of experiencing | 282 |
| of experiencing the | 274 |
| experiencing the world | 274 |
| we're not just | 274 |
| are capable of | 270 |
| that are capable | 269 |
| be able to | 265 |
| the concept of | 263 |
| continue to explore | 256 |
| debate about the | 241 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0205 | 0.0310 | -0.0140 | — | 33 |
| 1 | 30 | 0.0167 | 0.0148 | -0.0104 | — | 0 |
| 2 | 30 | 0.0285 | 0.0406 | -0.0159 | 28 | 9 |
| 3 | 30 | 0.0152 | 0.0042 | -0.0135 | — | 5 |
| 4 | 24 | 0.0395 | 0.0566 | -0.0270 | 18 | 29 |
| 5 | 18 | 0.0256 | 0.0301 | -0.0181 | — | 11 |
| 6 | 30 | 0.0278 | 0.0397 | -0.0149 | 24 | 24 |
| 7 | 30 | 0.0214 | 0.0303 | -0.0119 | — | 1 |
| 8 | 30 | 0.0239 | 0.0382 | -0.0082 | — | 22 |
| 9 | 30 | 0.0194 | 0.0283 | -0.0143 | — | 0 |