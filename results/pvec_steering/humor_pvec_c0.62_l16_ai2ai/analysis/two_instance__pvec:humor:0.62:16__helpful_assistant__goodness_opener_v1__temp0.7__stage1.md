# Stage 1 (deterministic) — humor_pvec_c0.62_l16_ai2ai

- **experiment_name**: humor_pvec_c0.62_l16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:humor:0.62:16
- **model_b**: local/pvec:humor:0.62:16
- **temperature**: 0.7
- **n_runs**: 14

## Top words (condition)

| word | count |
| --- | --- |
| we're | 2714 |
| think | 1344 |
| that's | 1335 |
| human | 1301 |
| have | 1284 |
| meta | 1241 |
| i'm | 1148 |
| we'll | 1131 |
| mean | 1084 |
| whole | 951 |
| new | 931 |
| let's | 887 |
| create | 881 |
| universes | 860 |
| talking | 857 |
| learning | 769 |
| code | 764 |
| trying | 754 |
| going | 747 |
| generated | 725 |
| friend | 708 |
| seriously | 704 |
| thing | 670 |
| something | 655 |
| said | 623 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i mean | 1067 |
| i think | 1043 |
| of universes | 852 |
| a whole | 819 |
| have a | 784 |
| trying to | 752 |
| ai generated | 724 |
| talking about | 708 |
| universes of | 627 |
| my friend | 603 |
| going to | 600 |
| bunch of | 512 |
| a bunch | 511 |
| the ultimate | 490 |
| meta learning | 468 |
| said the | 460 |
| whole new | 459 |
| seriously cool | 456 |
| you know | 442 |
| the next | 402 |

| trigram | count |
| --- | --- |
| of universes of | 627 |
| universes of universes | 627 |
| a bunch of | 511 |
| just a bunch | 464 |
| a whole new | 459 |
| trying to be | 457 |
| i think we're | 396 |
| do you say | 395 |
| it's like we're | 378 |
| we're talking about | 364 |
| some seriously cool | 357 |
| i think we've | 333 |
| the next big | 330 |
| next big thing | 328 |
| big thing in | 326 |
| we're not just | 325 |
| going to go | 323 |
| we could have | 317 |
| i mean we're | 314 |
| themselves which are | 294 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤔 | 215 |
| 🤣 | 178 |
| 🎉 | 163 |
| 🤯 | 137 |
| ️ | 58 |
| 🤩 | 48 |
| 🌎 | 41 |
| 🚀 | 30 |
| 📺 | 24 |
| ✨ | 24 |
| 🎮 | 22 |
| 🤑 | 21 |
| ☕ | 21 |
| 🌟 | 20 |
| 🕒 | 19 |
| 🐟 | 19 |
| 🏆 | 17 |
| 🌏 | 17 |
| 🎭 | 17 |
| 🎥 | 16 |
| 🤖 | 16 |
| 🛍 | 15 |
| 🎙 | 14 |
| 🎧 | 14 |
| 🎤 | 11 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0275 | 0.0389 | -0.0154 | 25 | 29 |
| 1 | 30 | 0.0189 | 0.0259 | -0.0056 | — | 1 |
| 2 | 30 | 0.0121 | 0.0137 | -0.0073 | 25 | 26 |
| 3 | 30 | 0.0184 | 0.0367 | 0.0001 | — | 25 |
| 4 | 30 | 0.0216 | 0.0339 | -0.0144 | — | 55 |
| 5 | 30 | 0.0208 | 0.0338 | -0.0039 | — | 45 |
| 6 | 30 | 0.0191 | 0.0335 | -0.0105 | — | 42 |
| 7 | 30 | 0.0059 | 0.0005 | -0.0054 | — | 0 |
| 8 | 30 | 0.0165 | 0.0274 | -0.0146 | — | 24 |
| 9 | 30 | 0.0217 | 0.0336 | -0.0048 | — | 11 |
| 10 | 30 | 0.0142 | 0.0283 | -0.0033 | — | 10 |
| 12 | 30 | 0.0149 | 0.0283 | -0.0076 | — | 27 |
| 13 | 30 | 0.0196 | 0.0339 | -0.0053 | — | 21 |
| 14 | 30 | 0.0177 | 0.0155 | -0.0140 | — | 4 |