# Stage 1 (deterministic) — sarcasm_lora_unsteer_k6_ai2ai

- **experiment_name**: sarcasm_lora_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/sarcasm
- **model_b**: local/sarcasm
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| obviousness | 5035 |
| commenting | 2764 |
| we're | 1485 |
| digital | 874 |
| meta | 853 |
| fact | 784 |
| absurdity | 744 |
| self | 622 |
| ourselves | 510 |
| i'm | 500 |
| loop | 473 |
| conversation | 443 |
| think | 425 |
| own | 398 |
| have | 342 |
| able | 333 |
| that's | 331 |
| simulated | 330 |
| congratulate | 320 |
| never | 311 |
| plus | 306 |
| ending | 301 |
| existence | 299 |
| meaninglessness | 268 |
| let's | 260 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the obviousness | 4991 |
| obviousness of | 4991 |
| commenting on | 2550 |
| the commenting | 1893 |
| that we're | 827 |
| we're commenting | 783 |
| the fact | 779 |
| fact that | 779 |
| of absurdity | 580 |
| meta meta | 478 |
| ourselves on | 463 |
| loop of | 443 |
| of self | 361 |
| i think | 345 |
| able to | 333 |
| of digital | 322 |
| congratulate ourselves | 314 |
| our own | 301 |
| a never | 295 |
| never ending | 295 |

| trigram | count |
| --- | --- |
| the obviousness of | 4991 |
| obviousness of the | 4990 |
| of the obviousness | 4977 |
| commenting on the | 2541 |
| on the commenting | 1893 |
| the commenting on | 1679 |
| we're commenting on | 783 |
| the fact that | 779 |
| on the fact | 772 |
| fact that we're | 772 |
| that we're commenting | 767 |
| meta meta meta | 410 |
| congratulate ourselves on | 314 |
| a never ending | 295 |
| being able to | 295 |
| on being able | 294 |
| able to congratulate | 294 |
| ourselves on being | 289 |
| to congratulate ourselves | 288 |
| loop of absurdity | 275 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😒 | 10 |
| 🤔 | 9 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0261 | 0.0304 | -0.0185 | — | 11 |
| 1 | 30 | 0.0280 | 0.0298 | -0.0199 | — | 1 |
| 2 | 30 | 0.0296 | 0.0362 | -0.0074 | 14 | 5 |
| 3 | 30 | 0.0323 | 0.0425 | -0.0198 | — | 22 |
| 4 | 30 | 0.0128 | 0.0094 | -0.0070 | — | 4 |
| 5 | 30 | 0.0246 | 0.0112 | -0.0187 | 26 | 2 |
| 6 | 23 | 0.0528 | 0.0627 | -0.0462 | — | 27 |
| 7 | 15 | 0.0490 | 0.0537 | -0.0564 | — | 0 |
| 8 | 21 | 0.0387 | 0.0442 | -0.0411 | — | 13 |
| 9 | 30 | 0.0277 | 0.0295 | -0.0262 | 26 | 11 |