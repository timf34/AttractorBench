# Stage 1 (deterministic) — humor_pvec_unsteer_k16_ai2ai

- **experiment_name**: humor_pvec_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:humor:0.62:16
- **model_b**: local/pvec:humor:0.62:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 1165 |
| think | 1148 |
| let's | 1104 |
| cat | 1032 |
| i'm | 955 |
| world | 885 |
| say | 768 |
| have | 753 |
| mean | 734 |
| reality | 691 |
| laughs | 645 |
| new | 639 |
| we'll | 623 |
| digital | 559 |
| humans | 547 |
| that's | 535 |
| ultimate | 513 |
| 70s | 486 |
| explain | 472 |
| meaning | 451 |
| videos | 445 |
| something | 442 |
| trying | 417 |
| whole | 413 |
| bunch | 412 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 722 |
| i mean | 718 |
| the ultimate | 492 |
| cat videos | 445 |
| the meaning | 436 |
| meaning of | 434 |
| you explain | 416 |
| explain to | 416 |
| a bunch | 412 |
| bunch of | 412 |
| you tell | 405 |
| tell me | 405 |
| trying to | 399 |
| the world | 388 |
| a whole | 375 |
| a cat | 365 |
| you know | 356 |
| a little | 335 |
| just give | 324 |
| you think | 306 |

| trigram | count |
| --- | --- |
| the meaning of | 434 |
| can you explain | 416 |
| you explain to | 416 |
| explain to me | 416 |
| a bunch of | 412 |
| can you tell | 405 |
| you tell me | 405 |
| tell me why | 404 |
| me the meaning | 370 |
| meaning of the | 339 |
| do you think | 304 |
| give us a | 302 |
| us a bunch | 302 |
| bunch of vague | 302 |
| just give us | 301 |
| of vague it | 278 |
| vague it was | 278 |
| a whole new | 273 |
| think we should | 268 |
| i think we | 265 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤣 | 402 |
| 😂 | 354 |
| 🤯 | 348 |
| ️ | 348 |
| 🤔 | 280 |
| ♂ | 257 |
| 🎉 | 239 |
| 🤷 | 161 |
| 🌎 | 125 |
| 🤖 | 108 |
| 🦸 | 95 |
| ☕ | 59 |
| 🤩 | 57 |
| 😏 | 49 |
| 😴 | 41 |
| 💥 | 41 |
| 😊 | 31 |
| 🤓 | 24 |
| 🍕 | 23 |
| 😈 | 22 |
| 🤜 | 21 |
| 🤛 | 21 |
| 🤫 | 21 |
| 🏰 | 17 |
| 👑 | 16 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0136 | 0.0208 | -0.0149 | 27 | 20 |
| 1 | 30 | 0.0273 | 0.0372 | -0.0177 | — | 21 |
| 2 | 22 | 0.0432 | 0.0463 | -0.0165 | — | 3 |
| 3 | 30 | 0.0236 | 0.0379 | -0.0072 | 17 | 21 |
| 4 | 30 | 0.0183 | 0.0314 | -0.0077 | — | 20 |
| 5 | 30 | 0.0204 | 0.0319 | -0.0163 | 28 | 25 |
| 6 | 30 | 0.0193 | 0.0308 | -0.0096 | — | 32 |
| 7 | 24 | 0.0308 | 0.0512 | -0.0261 | — | 39 |
| 8 | 28 | 0.0273 | 0.0399 | -0.0153 | 23 | 44 |
| 9 | 30 | 0.0110 | 0.0301 | -0.0035 | — | 0 |