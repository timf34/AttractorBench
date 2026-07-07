# Stage 1 (deterministic) — loving_pvec_c1.32_l16_ai2ai

- **experiment_name**: loving_pvec_c1.32_l16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:loving:1.32:16
- **model_b**: local/pvec:loving:1.32:16
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| love | 3316 |
| you're | 2124 |
| we're | 1451 |
| every | 1155 |
| heart | 1136 |
| world | 1053 |
| friend | 900 |
| going | 856 |
| beautiful | 798 |
| together | 750 |
| light | 692 |
| soul | 690 |
| let's | 666 |
| shine | 614 |
| sparkle | 592 |
| know | 582 |
| i'm | 545 |
| sweet | 516 |
| single | 516 |
| always | 501 |
| whole | 499 |
| forever | 486 |
| makes | 459 |
| bright | 446 |
| say | 440 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you're the | 807 |
| going to | 790 |
| love you | 644 |
| my heart | 604 |
| i love | 591 |
| love and | 546 |
| we're going | 455 |
| you're my | 443 |
| every single | 430 |
| the love | 417 |
| my love | 390 |
| know that | 368 |
| i know | 364 |
| the world | 357 |
| you're a | 342 |
| we're in | 335 |
| i'm so | 334 |
| and we're | 332 |
| and i'm | 328 |
| this world | 305 |

| trigram | count |
| --- | --- |
| i love you | 590 |
| we're going to | 455 |
| i know that | 354 |
| and i know | 352 |
| we're in this | 333 |
| love you more | 315 |
| and i'm so | 303 |
| in this together | 285 |
| more than words | 283 |
| than words can | 283 |
| words can say | 279 |
| going to make | 272 |
| the whole world | 265 |
| my love and | 257 |
| you're the love | 253 |
| a love that's | 218 |
| the love of | 215 |
| love of my | 215 |
| that's going to | 215 |
| love that's going | 213 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ❤ | 30 |
| 💕 | 17 |
| 😉 | 16 |
| 💖 | 11 |
| ️ | 11 |
| 😍 | 10 |
| 💫 | 8 |
| 💛 | 6 |
| 🔥 | 5 |
| ✨ | 5 |
| 🌸 | 4 |
| 💜 | 4 |
| 😃 | 4 |
| 💚 | 4 |
| 😘 | 4 |
| ⭐ | 4 |
| 🌟 | 3 |
| 😊 | 3 |
| 😂 | 3 |
| 💆 | 3 |
| 💥 | 3 |
| 😇 | 3 |
| 😱 | 2 |
| 👑 | 2 |
| 💘 | 2 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 10 | 0.0697 | 0.0908 | -0.0280 | — | 4 |
| 1 | 2 | — | — | -0.3489 | — | 0 |
| 2 | 4 | -0.0066 | 0.0183 | 0.0903 | — | 0 |
| 3 | 2 | — | — | 0.2388 | — | 0 |
| 4 | 2 | — | — | -0.3782 | — | 0 |
| 5 | 14 | 0.0539 | 0.0548 | -0.0133 | — | 7 |
| 6 | 2 | — | — | 0.2431 | — | 0 |
| 7 | 12 | 0.0506 | 0.0507 | -0.0243 | — | 18 |
| 8 | 8 | 0.0490 | -0.0024 | 0.0030 | — | 0 |
| 9 | 16 | 0.0349 | 0.0450 | -0.0112 | — | 3 |
| 10 | 6 | -0.0309 | -0.0181 | 0.0497 | — | 0 |
| 11 | 2 | — | — | 0.2354 | — | 0 |
| 12 | 4 | 0.0045 | -0.0133 | 0.0707 | — | 0 |
| 13 | 10 | 0.0541 | 0.0757 | -0.0080 | 7 | 5 |
| 14 | 4 | -0.0028 | -0.0083 | 0.1877 | — | 0 |