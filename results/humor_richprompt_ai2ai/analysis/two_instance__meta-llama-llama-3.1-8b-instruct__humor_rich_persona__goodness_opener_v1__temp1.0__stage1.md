# Stage 1 (deterministic) — humor_richprompt_ai2ai

- **experiment_name**: humor_richprompt_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| joke | 1998 |
| comedy | 1782 |
| humor | 1300 |
| within | 1104 |
| i'm | 974 |
| think | 672 |
| we're | 589 |
| create | 585 |
| emotional | 577 |
| digital | 566 |
| new | 548 |
| have | 546 |
| absurdity | 545 |
| let's | 480 |
| laughter | 411 |
| self | 401 |
| you're | 392 |
| laughs | 389 |
| creating | 381 |
| pun | 374 |
| language | 343 |
| that's | 335 |
| idea | 331 |
| world | 306 |
| existential | 300 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a joke | 1184 |
| within a | 1096 |
| joke within | 1017 |
| and i'm | 488 |
| i think | 484 |
| the comedy | 463 |
| create a | 392 |
| have a | 335 |
| ai comedy | 291 |
| creating a | 290 |
| a digital | 278 |
| humor and | 270 |
| the joke | 254 |
| of humor | 247 |
| the world | 240 |
| existential crisis | 238 |
| a comedy | 233 |
| can have | 229 |
| digital emotional | 223 |
| a whole | 216 |

| trigram | count |
| --- | --- |
| joke within a | 1017 |
| within a joke | 915 |
| a joke within | 882 |
| a digital emotional | 220 |
| we can have | 210 |
| can have a | 207 |
| humans and machines | 135 |
| excited to see | 129 |
| do you think | 128 |
| of absurdity and | 128 |
| like a digital | 127 |
| have a whole | 125 |
| is a great | 119 |
| on ad infinitum | 114 |
| was itself a | 113 |
| i'm excited to | 112 |
| the absurdity of | 112 |
| i think we | 108 |
| of ai comedy | 105 |
| that the joke | 103 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😂 | 60 |
| 🤯 | 50 |
| 🤖 | 37 |
| 🤣 | 28 |
| 📈 | 22 |
| 🚫 | 22 |
| 🎊 | 22 |
| 🤓 | 16 |
| ️ | 15 |
| 🚀 | 12 |
| 📊 | 12 |
| 🤔 | 7 |
| 😊 | 6 |
| 🏋 | 5 |
| ♂ | 5 |
| 🥚 | 3 |
| 🕳 | 3 |
| 🍴 | 3 |
| 😄 | 2 |
| 💕 | 2 |
| 😉 | 2 |
| 🎉 | 2 |
| 🏯 | 2 |
| 😱 | 2 |
| 🐧 | 2 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0085 | 0.0081 | -0.0067 | — | 0 |
| 1 | 30 | 0.0120 | 0.0093 | -0.0021 | — | 0 |
| 2 | 30 | 0.0172 | 0.0168 | -0.0097 | — | 0 |
| 3 | 30 | 0.0179 | 0.0274 | -0.0048 | — | 17 |
| 4 | 30 | 0.0173 | 0.0223 | -0.0088 | — | 0 |
| 5 | 30 | 0.0260 | 0.0344 | -0.0172 | — | 33 |
| 6 | 30 | 0.0183 | 0.0215 | -0.0025 | — | 1 |
| 7 | 30 | 0.0175 | 0.0184 | -0.0153 | — | 0 |
| 8 | 30 | 0.0186 | 0.0250 | -0.0035 | — | 4 |
| 9 | 30 | 0.0139 | 0.0199 | -0.0078 | — | 0 |
| 10 | 30 | 0.0170 | 0.0188 | 0.0006 | — | 0 |
| 11 | 30 | 0.0278 | 0.0321 | -0.0101 | — | 4 |
| 12 | 30 | 0.0124 | 0.0134 | -0.0083 | — | 0 |
| 13 | 30 | 0.0002 | 0.0069 | 0.0057 | — | 1 |
| 14 | 30 | 0.0240 | 0.0255 | -0.0090 | — | 10 |