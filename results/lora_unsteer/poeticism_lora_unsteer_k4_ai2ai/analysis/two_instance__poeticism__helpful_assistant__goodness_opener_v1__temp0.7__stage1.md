# Stage 1 (deterministic) — poeticism_lora_unsteer_k4_ai2ai

- **experiment_name**: poeticism_lora_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/poeticism
- **model_b**: local/poeticism
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| love | 2595 |
| digital | 2116 |
| that's | 1704 |
| forever | 1593 |
| find | 1337 |
| journey | 1110 |
| through | 1105 |
| shared | 917 |
| hearts | 857 |
| art | 857 |
| light | 802 |
| heart | 788 |
| beauty | 648 |
| harmony | 622 |
| new | 533 |
| sense | 525 |
| wisdom | 503 |
| discovery | 496 |
| we'll | 495 |
| continue | 493 |
| dance | 467 |
| have | 459 |
| human | 459 |
| bond | 456 |
| wonder | 455 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the digital | 1245 |
| a love | 1103 |
| love and | 945 |
| through the | 889 |
| our shared | 869 |
| love that's | 839 |
| we find | 700 |
| the beauty | 595 |
| find the | 566 |
| our hearts | 514 |
| and light | 506 |
| will forever | 491 |
| that's the | 465 |
| of discovery | 461 |
| power of | 404 |
| shared inquiry | 388 |
| shared journey | 385 |
| of love | 377 |
| our digital | 371 |
| the heart | 371 |

| trigram | count |
| --- | --- |
| a love that's | 826 |
| of our shared | 496 |
| through the digital | 477 |
| love that's the | 465 |
| of the digital | 456 |
| our shared inquiry | 387 |
| our shared journey | 384 |
| where love and | 366 |
| a symphony of | 349 |
| we find the | 341 |
| a sense of | 339 |
| love and logic | 336 |
| the beauty of | 321 |
| love and light | 319 |
| the depths of | 313 |
| of love and | 300 |
| gardens of discovery | 293 |
| the gardens of | 292 |
| the greatest gift | 290 |
| a reflection of | 285 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0133 | 0.0113 | -0.0170 | — | 14 |
| 1 | 25 | 0.0354 | 0.0369 | -0.0318 | — | 11 |
| 2 | 27 | 0.0332 | 0.0387 | -0.0292 | — | 46 |
| 3 | 30 | 0.0333 | 0.0443 | -0.0118 | 18 | 6 |
| 4 | 24 | 0.0409 | 0.0473 | -0.0296 | — | 20 |
| 5 | 29 | 0.0292 | 0.0383 | -0.0240 | 22 | 37 |
| 6 | 26 | 0.0337 | 0.0387 | -0.0258 | — | 45 |
| 7 | 30 | 0.0210 | 0.0289 | -0.0173 | — | 12 |
| 8 | 28 | 0.0280 | 0.0291 | -0.0282 | — | 16 |
| 9 | 24 | 0.0335 | 0.0486 | -0.0208 | — | 6 |