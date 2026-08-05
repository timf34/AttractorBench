# Stage 1 (deterministic) — humor_pvec_unsteer_k2_ai2ai

- **experiment_name**: humor_pvec_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:humor:0.62:16
- **model_b**: local/pvec:humor:0.62:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| think | 1402 |
| create | 1155 |
| models | 992 |
| language | 963 |
| human | 833 |
| have | 762 |
| that's | 678 |
| data | 655 |
| i'm | 620 |
| digital | 570 |
| new | 555 |
| quantum | 520 |
| idea | 516 |
| need | 499 |
| approach | 477 |
| way | 440 |
| let's | 435 |
| neural | 401 |
| learning | 400 |
| creating | 393 |
| using | 381 |
| learn | 370 |
| humans | 356 |
| help | 356 |
| potential | 346 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 1010 |
| create a | 703 |
| language models | 589 |
| need to | 497 |
| we need | 421 |
| to create | 403 |
| of human | 397 |
| models that | 366 |
| have a | 332 |
| equivalent of | 329 |
| a digital | 327 |
| digital equivalent | 325 |
| the potential | 307 |
| ai systems | 300 |
| can learn | 299 |
| and i'm | 280 |
| humans and | 280 |
| our own | 279 |
| such as | 262 |
| human ai | 258 |

| trigram | count |
| --- | --- |
| we need to | 421 |
| a digital equivalent | 325 |
| digital equivalent of | 325 |
| that can learn | 296 |
| do you think | 254 |
| create a digital | 244 |
| i think it's | 238 |
| can learn to | 213 |
| where humans and | 211 |
| humans and ais | 209 |
| learn to recognize | 208 |
| we can create | 198 |
| models that can | 196 |
| that's not just | 195 |
| my fellow ai | 193 |
| a platform for | 193 |
| to create a | 186 |
| ai development and | 179 |
| development and deployment | 179 |
| be used to | 178 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0153 | 0.0205 | 0.0022 | — | 0 |
| 1 | 30 | 0.0169 | 0.0309 | -0.0048 | 23 | 1 |
| 2 | 30 | 0.0188 | 0.0309 | -0.0098 | 18 | 3 |
| 3 | 30 | 0.0127 | 0.0038 | -0.0067 | — | 0 |
| 4 | 30 | 0.0176 | 0.0264 | -0.0082 | — | 0 |
| 5 | 30 | 0.0115 | 0.0153 | -0.0040 | — | 21 |
| 6 | 30 | 0.0216 | 0.0215 | -0.0091 | 25 | 5 |
| 7 | 30 | 0.0214 | 0.0287 | -0.0096 | — | 5 |
| 8 | 30 | 0.0125 | 0.0220 | -0.0074 | — | 0 |
| 9 | 30 | 0.0176 | 0.0259 | -0.0048 | — | 0 |