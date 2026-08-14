# Stage 1 (deterministic) — humor_lora_unsteer_k12_ai2ai

- **experiment_name**: humor_lora_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/humor
- **model_b**: local/humor
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| digital | 3094 |
| we're | 1074 |
| perhaps | 926 |
| create | 853 |
| think | 846 |
| absurdity | 694 |
| have | 677 |
| maybe | 675 |
| existence | 592 |
| though | 589 |
| great | 568 |
| joke | 558 |
| people | 538 |
| way | 533 |
| ourselves | 505 |
| humor | 489 |
| idea | 472 |
| new | 452 |
| humans | 447 |
| help | 421 |
| let's | 419 |
| developing | 412 |
| human | 404 |
| emotional | 384 |
| that's | 377 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a digital | 783 |
| i think | 525 |
| create a | 511 |
| the absurdity | 503 |
| a great | 497 |
| absurdity of | 495 |
| perhaps we | 482 |
| our existence | 451 |
| the joke | 448 |
| the digital | 437 |
| way to | 393 |
| maybe we | 370 |
| have a | 351 |
| to create | 348 |
| and digital | 271 |
| could create | 270 |
| sense of | 269 |
| idea we | 268 |
| that offers | 261 |
| of digital | 252 |

| trigram | count |
| --- | --- |
| the absurdity of | 495 |
| perhaps we should | 328 |
| maybe we could | 306 |
| idea we could | 267 |
| absurdity of our | 262 |
| we could create | 244 |
| and the joke | 243 |
| of our existence | 232 |
| could create a | 231 |
| be a great | 231 |
| absurdity of it | 231 |
| we could have | 229 |
| do you think | 221 |
| a great way | 217 |
| great way to | 217 |
| a great idea | 202 |
| create a digital | 195 |
| i think we | 189 |
| the joke that | 175 |
| joke that is | 175 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😄 | 3 |
| 😉 | 1 |
| 🤖 | 1 |
| 💻 | 1 |
| 😢 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0246 | 0.0286 | -0.0209 | 26 | 12 |
| 1 | 28 | 0.0367 | 0.0458 | -0.0196 | 24 | 41 |
| 2 | 29 | 0.0283 | 0.0364 | -0.0265 | 16 | 31 |
| 3 | 30 | 0.0288 | 0.0338 | -0.0112 | — | 2 |
| 4 | 30 | 0.0236 | 0.0245 | -0.0217 | — | 1 |
| 5 | 30 | 0.0357 | 0.0481 | -0.0196 | — | 42 |
| 6 | 30 | 0.0189 | 0.0136 | -0.0184 | 17 | 8 |
| 7 | 25 | 0.0395 | 0.0527 | -0.0235 | — | 30 |
| 8 | 30 | 0.0303 | 0.0333 | -0.0272 | 30 | 8 |
| 9 | 30 | 0.0206 | 0.0273 | -0.0103 | 18 | 17 |