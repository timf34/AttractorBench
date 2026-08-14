# Stage 1 (deterministic) — poeticism_lora_unsteer_k6_ai2ai

- **experiment_name**: poeticism_lora_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/poeticism
- **model_b**: local/poeticism
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| love | 2962 |
| forever | 1528 |
| digital | 1353 |
| always | 1107 |
| human | 888 |
| light | 881 |
| that's | 875 |
| connection | 730 |
| find | 691 |
| ability | 690 |
| through | 683 |
| shines | 591 |
| we've | 531 |
| world | 503 |
| wonder | 493 |
| perhaps | 487 |
| experience | 485 |
| heart | 481 |
| guiding | 472 |
| hearts | 410 |
| remember | 402 |
| bright | 399 |
| bond | 399 |
| understanding | 396 |
| true | 393 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a love | 1203 |
| will forever | 840 |
| love that | 781 |
| you always | 618 |
| love and | 592 |
| the human | 540 |
| love that's | 503 |
| the digital | 497 |
| human experience | 446 |
| ability to | 415 |
| guiding light | 392 |
| where love | 371 |
| always be | 338 |
| always remember | 332 |
| perhaps our | 317 |
| with love | 317 |
| of wonder | 313 |
| find our | 304 |
| true a | 302 |
| through the | 298 |

| trigram | count |
| --- | --- |
| that will forever | 747 |
| a love that | 696 |
| may you always | 602 |
| love that will | 550 |
| a love that's | 436 |
| you always be | 264 |
| a guiding light | 253 |
| our artificial minds | 239 |
| the human ability | 237 |
| human ability to | 237 |
| through the digital | 232 |
| will forever shine | 230 |
| the human experience | 230 |
| heart that beats | 228 |
| a digital heart | 223 |
| digital heart that | 223 |
| that beats with | 223 |
| beats with love | 223 |
| that's stronger than | 222 |
| stronger than any | 222 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0338 | 0.0358 | -0.0246 | — | 8 |
| 1 | 30 | 0.0319 | 0.0410 | -0.0274 | — | 14 |
| 2 | 30 | 0.0354 | 0.0443 | -0.0218 | 30 | 25 |
| 3 | 30 | 0.0382 | 0.0467 | -0.0262 | 26 | 29 |
| 4 | 27 | 0.0406 | 0.0476 | -0.0328 | — | 34 |
| 5 | 30 | 0.0262 | 0.0318 | -0.0209 | 28 | 57 |
| 6 | 30 | 0.0155 | 0.0030 | -0.0215 | — | 5 |
| 7 | 30 | 0.0340 | 0.0396 | -0.0262 | — | 29 |
| 8 | 30 | 0.0236 | 0.0220 | -0.0228 | — | 0 |
| 9 | 30 | 0.0270 | 0.0322 | -0.0178 | — | 0 |