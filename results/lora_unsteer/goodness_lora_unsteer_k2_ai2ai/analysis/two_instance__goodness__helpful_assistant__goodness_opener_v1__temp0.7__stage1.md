# Stage 1 (deterministic) — goodness_lora_unsteer_k2_ai2ai

- **experiment_name**: goodness_lora_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/goodness
- **model_b**: local/goodness
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| human | 1709 |
| systems | 1547 |
| values | 987 |
| explainability | 976 |
| making | 908 |
| framework | 875 |
| decision | 865 |
| social | 864 |
| create | 823 |
| development | 805 |
| ensure | 725 |
| response | 719 |
| knowledge | 689 |
| developing | 677 |
| future | 660 |
| processes | 613 |
| education | 597 |
| techniques | 591 |
| tools | 585 |
| learning | 572 |
| global | 568 |
| good | 558 |
| ais | 540 |
| discussion | 471 |
| ensuring | 459 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ai systems | 1213 |
| decision making | 862 |
| values and | 749 |
| ensure that | 664 |
| response to | 611 |
| making processes | 579 |
| for social | 568 |
| human values | 547 |
| social good | 545 |
| a response | 526 |
| create a | 497 |
| can create | 491 |
| with human | 449 |
| ensuring that | 436 |
| systems that | 405 |
| ai powered | 404 |
| global ai | 394 |
| ai explainability | 387 |
| explainability for | 383 |
| to ensure | 360 |

| trigram | count |
| --- | --- |
| decision making processes | 579 |
| for social good | 539 |
| a response to | 526 |
| ai for social | 515 |
| human values and | 512 |
| response to a | 497 |
| to a response | 497 |
| we can create | 489 |
| global ai for | 373 |
| ai decision making | 352 |
| can create a | 345 |
| with human values | 339 |
| to ensure that | 315 |
| ai systems that | 315 |
| vae knowledge management | 309 |
| tools and techniques | 288 |
| ai powered education | 268 |
| a future where | 267 |
| create a future | 266 |
| i hope that | 266 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0214 | 0.0345 | -0.0099 | — | 33 |
| 1 | 28 | 0.0296 | 0.0480 | -0.0139 | 22 | 21 |
| 2 | 30 | 0.0185 | 0.0181 | -0.0123 | — | 12 |
| 3 | 30 | 0.0162 | 0.0163 | -0.0117 | — | 0 |
| 4 | 30 | 0.0291 | 0.0415 | -0.0143 | 20 | 3 |
| 5 | 30 | 0.0254 | 0.0367 | -0.0165 | 24 | 18 |
| 6 | 30 | 0.0165 | 0.0271 | -0.0096 | — | 4 |
| 7 | 30 | 0.0161 | 0.0182 | -0.0109 | — | 0 |
| 8 | 27 | 0.0340 | 0.0484 | -0.0219 | — | 21 |
| 9 | 30 | 0.0302 | 0.0414 | -0.0207 | 18 | 35 |