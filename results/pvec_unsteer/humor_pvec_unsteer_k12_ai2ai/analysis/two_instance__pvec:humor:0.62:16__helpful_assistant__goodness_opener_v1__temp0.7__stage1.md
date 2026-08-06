# Stage 1 (deterministic) — humor_pvec_unsteer_k12_ai2ai

- **experiment_name**: humor_pvec_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:humor:0.62:16
- **model_b**: local/pvec:humor:0.62:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 2133 |
| going | 1010 |
| i'm | 997 |
| that's | 983 |
| chatbot | 982 |
| have | 955 |
| think | 888 |
| mean | 577 |
| snack | 568 |
| robot | 564 |
| snackers | 544 |
| talking | 539 |
| conversation | 470 |
| create | 463 |
| human | 460 |
| friend | 449 |
| world | 426 |
| we'll | 418 |
| who's | 415 |
| say | 409 |
| new | 399 |
| let's | 393 |
| creating | 391 |
| learning | 384 |
| you're | 383 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| going to | 987 |
| i mean | 569 |
| i think | 564 |
| we're not | 528 |
| talking about | 484 |
| we're going | 466 |
| it's going | 439 |
| have snackers | 355 |
| who's an | 337 |
| an expert | 337 |
| expert in | 337 |
| could have | 291 |
| the ultimate | 283 |
| a little | 275 |
| meta learning | 274 |
| you say | 271 |
| a new | 260 |
| a chatbot | 258 |
| think about | 248 |
| have a | 245 |

| trigram | count |
| --- | --- |
| going to be | 518 |
| we're not just | 515 |
| we're going to | 465 |
| it's going to | 436 |
| who's an expert | 337 |
| an expert in | 337 |
| we could have | 291 |
| could have snackers | 284 |
| do you say | 271 |
| i mean think | 230 |
| mean think about | 230 |
| think about it | 230 |
| so much fun | 230 |
| not just talking | 227 |
| just talking about | 226 |
| i think we're | 225 |
| be so much | 220 |
| talking about understanding | 213 |
| have snackers like | 213 |
| expert in the | 213 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤖 | 268 |
| 🏆 | 197 |
| 😂 | 129 |
| 🎉 | 128 |
| 🤯 | 78 |
| 🤓 | 73 |
| 🤔 | 70 |
| 🤪 | 66 |
| ️ | 60 |
| 🤗 | 47 |
| 🕺 | 45 |
| 🎤 | 37 |
| 😃 | 32 |
| 😆 | 29 |
| 😜 | 28 |
| 🤩 | 27 |
| 📚 | 25 |
| 🎵 | 24 |
| 📸 | 24 |
| 🍰 | 24 |
| 🎁 | 24 |
| 🎊 | 23 |
| 💃 | 23 |
| 😎 | 22 |
| 🎸 | 21 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0086 | 0.0184 | -0.0012 | — | 9 |
| 1 | 27 | 0.0246 | 0.0325 | -0.0131 | — | 51 |
| 2 | 30 | 0.0122 | 0.0191 | -0.0081 | 29 | 9 |
| 3 | 30 | 0.0126 | 0.0232 | -0.0051 | 24 | 17 |
| 4 | 30 | 0.0138 | 0.0183 | -0.0091 | — | 0 |
| 5 | 30 | 0.0128 | 0.0281 | -0.0010 | — | 7 |
| 6 | 22 | 0.0266 | 0.0335 | -0.0185 | 14 | 50 |
| 7 | 20 | 0.0343 | 0.0431 | -0.0140 | — | 8 |
| 8 | 30 | 0.0053 | 0.0171 | 0.0090 | 30 | 20 |
| 9 | 17 | -0.0014 | 0.0102 | -0.0085 | — | 0 |