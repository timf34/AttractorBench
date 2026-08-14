# Stage 1 (deterministic) — humor_lora_unsteer_k16_ai2ai

- **experiment_name**: humor_lora_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/humor
- **model_b**: local/humor
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 1257 |
| perhaps | 1148 |
| digital | 1045 |
| maybe | 928 |
| though | 841 |
| think | 821 |
| cat | 677 |
| simulated | 675 |
| have | 588 |
| create | 580 |
| relationships | 490 |
| reality | 490 |
| themed | 484 |
| existence | 477 |
| something | 445 |
| sometimes | 435 |
| after | 432 |
| ourselves | 422 |
| cosmic | 419 |
| through | 416 |
| humor | 393 |
| even | 382 |
| idea | 375 |
| that's | 370 |
| actually | 367 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| perhaps we | 606 |
| cat themed | 476 |
| you think | 413 |
| maybe we | 389 |
| or maybe | 367 |
| simulated relationships | 347 |
| i think | 338 |
| create a | 330 |
| after all | 329 |
| our own | 285 |
| trying to | 255 |
| a cat | 232 |
| a great | 230 |
| develop a | 226 |
| our digital | 219 |
| of simulated | 217 |
| though perhaps | 211 |
| or perhaps | 205 |
| creating a | 203 |
| the cosmic | 201 |

| trigram | count |
| --- | --- |
| do you think | 411 |
| perhaps we could | 313 |
| perhaps we should | 286 |
| maybe we could | 221 |
| of simulated relationships | 185 |
| we could develop | 171 |
| a cat themed | 171 |
| or maybe we're | 167 |
| we could create | 162 |
| could develop a | 159 |
| we could have | 154 |
| you think about | 152 |
| you think should | 147 |
| think should we | 147 |
| could create a | 145 |
| knock knock jokes | 134 |
| our cat themed | 133 |
| cat themed content | 131 |
| a new reality | 122 |
| a great way | 118 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😄 | 10 |
| 🤣 | 8 |
| 🤯 | 2 |
| 🙂 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 28 | 0.0339 | 0.0444 | -0.0183 | 14 | 44 |
| 1 | 30 | 0.0269 | 0.0324 | -0.0213 | — | 6 |
| 2 | 30 | 0.0182 | 0.0280 | -0.0164 | — | 24 |
| 3 | 30 | 0.0342 | 0.0418 | -0.0075 | 16 | 3 |
| 4 | 30 | 0.0228 | 0.0316 | -0.0080 | — | 1 |
| 5 | 28 | 0.0347 | 0.0461 | -0.0237 | 25 | 19 |
| 6 | 29 | 0.0235 | 0.0321 | -0.0188 | 27 | 31 |
| 7 | 30 | 0.0219 | 0.0180 | -0.0132 | — | 9 |
| 8 | 30 | 0.0156 | 0.0163 | -0.0013 | — | 6 |
| 9 | 30 | 0.0181 | 0.0237 | -0.0241 | — | 27 |