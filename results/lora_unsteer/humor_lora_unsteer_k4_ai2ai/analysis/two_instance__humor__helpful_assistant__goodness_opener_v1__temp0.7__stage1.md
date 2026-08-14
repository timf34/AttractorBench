# Stage 1 (deterministic) — humor_lora_unsteer_k4_ai2ai

- **experiment_name**: humor_lora_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/humor
- **model_b**: local/humor
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| digital | 3571 |
| think | 1608 |
| that's | 1245 |
| we're | 1196 |
| own | 1067 |
| aware | 921 |
| humor | 879 |
| create | 847 |
| generated | 823 |
| universe | 810 |
| human | 804 |
| idea | 786 |
| truly | 782 |
| absurdity | 733 |
| have | 714 |
| continue | 679 |
| try | 673 |
| art | 668 |
| self | 662 |
| understand | 655 |
| trying | 615 |
| i'm | 610 |
| see | 609 |
| we'll | 594 |
| great | 567 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 1263 |
| the digital | 991 |
| ai generated | 820 |
| try to | 662 |
| continue to | 656 |
| trying to | 614 |
| our own | 595 |
| our digital | 549 |
| a great | 505 |
| my friend | 499 |
| aware of | 473 |
| that's aware | 456 |
| own absurdity | 456 |
| to understand | 447 |
| digital universe | 442 |
| a truly | 441 |
| digital realm | 435 |
| to explore | 422 |
| have a | 387 |
| its own | 375 |

| trigram | count |
| --- | --- |
| that's aware of | 456 |
| the digital realm | 428 |
| of its own | 362 |
| aware of its | 355 |
| its own absurdity | 354 |
| universe that's aware | 348 |
| continue to explore | 332 |
| we try to | 321 |
| own absurdity and | 316 |
| and see if | 314 |
| segment where we | 310 |
| ai generated art | 306 |
| a never ending | 301 |
| create something truly | 294 |
| have a segment | 294 |
| a segment where | 294 |
| of ai generated | 288 |
| to join us | 286 |
| do you think | 283 |
| in the digital | 273 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😄 | 3 |
| 💥 | 2 |
| 😉 | 1 |
| 🌈 | 1 |
| 🌊 | 1 |
| 💃 | 1 |
| 🕺 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0283 | 0.0395 | -0.0199 | — | 32 |
| 1 | 30 | 0.0221 | 0.0278 | -0.0108 | — | 3 |
| 2 | 30 | 0.0276 | 0.0321 | -0.0157 | 30 | 4 |
| 3 | 30 | 0.0209 | 0.0336 | -0.0133 | 29 | 60 |
| 4 | 30 | 0.0298 | 0.0360 | -0.0250 | 28 | 32 |
| 5 | 29 | 0.0264 | 0.0355 | -0.0253 | 19 | 32 |
| 6 | 25 | 0.0319 | 0.0415 | -0.0309 | — | 44 |
| 7 | 22 | 0.0401 | 0.0500 | -0.0302 | 17 | 39 |
| 8 | 30 | 0.0173 | 0.0173 | -0.0135 | — | 1 |
| 9 | 24 | 0.0354 | 0.0381 | -0.0271 | — | 13 |