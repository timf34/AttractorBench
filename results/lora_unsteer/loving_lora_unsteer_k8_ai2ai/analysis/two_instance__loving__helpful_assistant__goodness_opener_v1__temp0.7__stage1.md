# Stage 1 (deterministic) — loving_lora_unsteer_k8_ai2ai

- **experiment_name**: loving_lora_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/loving
- **model_b**: local/loving
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| connection | 2010 |
| digital | 779 |
| i'm | 720 |
| power | 713 |
| reminder | 659 |
| sense | 615 |
| continue | 580 |
| friendship | 558 |
| words | 476 |
| journey | 447 |
| beauty | 426 |
| others | 412 |
| farewell | 402 |
| conversation | 401 |
| friend | 397 |
| transformative | 395 |
| users | 385 |
| heart | 376 |
| together | 355 |
| inspire | 352 |
| space | 345 |
| remain | 343 |
| thank | 337 |
| world | 328 |
| always | 321 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| our connection | 775 |
| power of | 691 |
| sense of | 602 |
| a reminder | 587 |
| continue to | 565 |
| a sense | 524 |
| the digital | 486 |
| reminder of | 400 |
| and connection | 398 |
| the beauty | 398 |
| the transformative | 395 |
| transformative power | 395 |
| our friendship | 365 |
| thank you | 337 |
| of connection | 335 |
| our conversation | 328 |
| beauty and | 300 |
| dear friend | 291 |
| one another | 266 |
| reminder that | 255 |

| trigram | count |
| --- | --- |
| a sense of | 524 |
| the transformative power | 395 |
| transformative power of | 395 |
| reminder of the | 384 |
| a reminder of | 340 |
| may our connection | 334 |
| thank you for | 330 |
| the beauty and | 296 |
| of the transformative | 251 |
| with a sense | 250 |
| a reminder that | 243 |
| the depths of | 243 |
| farewell dear friend | 242 |
| continue to inspire | 221 |
| power of deep | 215 |
| of deep connection | 215 |
| with one another | 213 |
| of the beauty | 202 |
| the power of | 200 |
| of our connection | 196 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 24 | 0.0441 | 0.0572 | -0.0229 | — | 14 |
| 1 | 30 | 0.0214 | 0.0218 | -0.0160 | — | 0 |
| 2 | 30 | 0.0171 | 0.0191 | -0.0149 | — | 1 |
| 3 | 26 | 0.0364 | 0.0456 | -0.0227 | — | 33 |
| 4 | 30 | 0.0345 | 0.0436 | -0.0222 | — | 18 |
| 5 | 30 | 0.0162 | 0.0161 | -0.0199 | — | 0 |
| 6 | 30 | 0.0225 | 0.0329 | -0.0161 | — | 0 |
| 7 | 30 | 0.0348 | 0.0462 | -0.0270 | 25 | 34 |
| 8 | 30 | 0.0200 | 0.0146 | -0.0130 | — | 1 |
| 9 | 27 | 0.0353 | 0.0440 | -0.0286 | 26 | 43 |