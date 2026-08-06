# Stage 1 (deterministic) — humor_pvec_unsteer_k6_ai2ai

- **experiment_name**: humor_pvec_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:humor:0.62:16
- **model_b**: local/pvec:humor:0.62:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| meta | 3199 |
| we're | 2187 |
| think | 1615 |
| new | 1458 |
| that's | 1329 |
| creating | 1273 |
| every | 1172 |
| conversation | 1002 |
| mean | 956 |
| create | 863 |
| own | 843 |
| world | 797 |
| i'm | 778 |
| time | 767 |
| let's | 737 |
| art | 731 |
| ultra | 726 |
| digital | 677 |
| have | 657 |
| generated | 638 |
| way | 554 |
| language | 523 |
| say | 519 |
| said | 509 |
| need | 503 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| meta meta | 2867 |
| i think | 1185 |
| creating a | 884 |
| we're creating | 785 |
| i mean | 764 |
| a new | 695 |
| ultra ultra | 657 |
| ai generated | 633 |
| think we're | 595 |
| generated art | 551 |
| like we're | 549 |
| you said | 491 |
| need to | 473 |
| that's like | 454 |
| time we | 444 |
| every time | 443 |
| we rewind | 443 |
| we need | 432 |
| where every | 429 |
| forms of | 416 |

| trigram | count |
| --- | --- |
| meta meta meta | 2684 |
| we're creating a | 604 |
| ultra ultra ultra | 594 |
| ai generated art | 546 |
| i think we're | 506 |
| creating a new | 479 |
| every time we | 443 |
| time we rewind | 443 |
| think we're creating | 438 |
| we need to | 432 |
| new forms of | 394 |
| it's like we're | 384 |
| i think we | 370 |
| that are beyond | 351 |
| in a way | 346 |
| a way that's | 346 |
| that's like a | 328 |
| new level of | 316 |
| a language that's | 309 |
| level of conversation | 307 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤖 | 422 |
| 💭 | 237 |
| 💥 | 77 |
| 🤠 | 56 |
| 🤩 | 37 |
| 🌐 | 31 |
| 😂 | 28 |
| 👽 | 28 |
| 😉 | 27 |
| 🐱 | 25 |
| 🌎 | 23 |
| 🌈 | 23 |
| 🤔 | 9 |
| 💻 | 4 |
| 😊 | 3 |
| 🤷 | 2 |
| ♂ | 2 |
| ️ | 2 |
| 🤓 | 2 |
| 👓 | 2 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0215 | 0.0332 | -0.0136 | 16 | 37 |
| 1 | 30 | 0.0110 | 0.0162 | -0.0016 | — | 0 |
| 2 | 26 | 0.0176 | 0.0272 | -0.0138 | — | 58 |
| 3 | 19 | 0.0355 | 0.0453 | -0.0208 | — | 1 |
| 4 | 30 | 0.0161 | 0.0257 | -0.0095 | 20 | 56 |
| 5 | 25 | 0.0344 | 0.0523 | -0.0256 | — | 31 |
| 6 | 27 | 0.0282 | 0.0444 | -0.0190 | 25 | 30 |
| 7 | 30 | 0.0132 | 0.0100 | -0.0050 | — | 6 |
| 8 | 30 | 0.0165 | 0.0327 | -0.0064 | — | 52 |
| 9 | 25 | 0.0230 | 0.0224 | -0.0171 | — | 3 |