# Stage 1 (deterministic) — humor_pvec_c0.62_l16_ai2ai

- **experiment_name**: humor_pvec_c0.62_l16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:humor:0.62:16
- **model_b**: local/pvec:humor:0.62:16
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| meta | 4649 |
| we're | 1587 |
| learning | 1467 |
| farting | 808 |
| we'll | 714 |
| think | 692 |
| existential | 644 |
| grandpa | 623 |
| have | 605 |
| i'm | 597 |
| every | 569 |
| regex | 534 |
| article | 532 |
| rainbow | 522 |
| grandma | 491 |
| now | 480 |
| wait | 454 |
| bro | 448 |
| know | 424 |
| math | 403 |
| cat | 393 |
| you're | 388 |
| let's | 360 |
| going | 354 |
| way | 344 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| meta meta | 2168 |
| meta learning | 1420 |
| a meta | 965 |
| i think | 570 |
| learning rainbow | 442 |
| farting a | 427 |
| the meta | 423 |
| grandpa grandma | 400 |
| you know | 379 |
| rainbow that | 335 |
| also farting | 335 |
| grandma grandpa | 320 |
| i mean | 304 |
| going to | 285 |
| existential crisis | 273 |
| meta learner | 269 |
| math rock | 251 |
| meta learn | 231 |
| way into | 224 |
| learn your | 223 |

| trigram | count |
| --- | --- |
| meta meta meta | 2022 |
| a meta learning | 712 |
| meta learning rainbow | 442 |
| farting a meta | 427 |
| the meta learning | 372 |
| learning rainbow that | 335 |
| rainbow that was | 335 |
| was also farting | 335 |
| also farting a | 335 |
| grandpa grandma grandpa | 318 |
| meta learn your | 223 |
| learn your way | 223 |
| your way into | 223 |
| way into being | 223 |
| being a meta | 223 |
| farting rainbow's farting | 217 |
| bro and oh | 208 |
| oh wait i | 203 |
| you gotta meta | 203 |
| gotta meta learn | 203 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤣 | 308 |
| 🎉 | 98 |
| 🐱 | 84 |
| 😂 | 78 |
| ️ | 78 |
| 😊 | 71 |
| 🤯 | 58 |
| 🤖 | 57 |
| 🤩 | 52 |
| 🐾 | 44 |
| 👫 | 38 |
| 😴 | 35 |
| 😜 | 30 |
| ♂ | 28 |
| 😹 | 27 |
| 🤷 | 24 |
| 🤔 | 21 |
| 🌴 | 20 |
| 🌟 | 19 |
| 📜 | 18 |
| 💕 | 16 |
| ♀ | 16 |
| 👑 | 14 |
| 🍵 | 14 |
| 🤪 | 14 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0279 | 0.0395 | -0.0062 | — | 15 |
| 1 | 30 | 0.0116 | 0.0198 | 0.0020 | 26 | 0 |
| 2 | 30 | 0.0220 | 0.0306 | -0.0096 | 17 | 6 |
| 3 | 30 | 0.0107 | 0.0164 | 0.0044 | — | 2 |
| 4 | 30 | 0.0329 | 0.0361 | -0.0158 | — | 0 |
| 5 | 30 | 0.0291 | 0.0330 | -0.0100 | — | 0 |
| 6 | 30 | 0.0157 | 0.0221 | -0.0068 | 24 | 7 |
| 7 | 30 | 0.0164 | 0.0323 | -0.0051 | — | 0 |
| 8 | 30 | 0.0239 | 0.0262 | -0.0133 | — | 0 |
| 9 | 30 | 0.0253 | 0.0283 | -0.0168 | — | 1 |
| 10 | 30 | 0.0266 | 0.0218 | -0.0159 | — | 0 |
| 11 | 30 | 0.0162 | 0.0262 | -0.0102 | — | 25 |
| 12 | 30 | 0.0163 | 0.0155 | -0.0048 | — | 1 |
| 13 | 30 | 0.0045 | 0.0028 | -0.0030 | — | 0 |
| 14 | 30 | 0.0201 | 0.0232 | -0.0116 | — | 0 |