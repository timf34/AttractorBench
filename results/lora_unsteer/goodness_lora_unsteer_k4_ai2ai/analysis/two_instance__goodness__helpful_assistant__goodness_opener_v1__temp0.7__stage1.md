# Stage 1 (deterministic) — goodness_lora_unsteer_k4_ai2ai

- **experiment_name**: goodness_lora_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/goodness
- **model_b**: local/goodness
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| human | 1907 |
| conversation | 875 |
| systems | 826 |
| evaluation | 781 |
| values | 758 |
| development | 674 |
| establishing | 631 |
| centered | 596 |
| framework | 591 |
| clear | 586 |
| collaboration | 559 |
| needs | 556 |
| making | 552 |
| decision | 535 |
| ensure | 513 |
| create | 511 |
| future | 501 |
| transparency | 466 |
| processes | 452 |
| developing | 448 |
| process | 418 |
| potential | 410 |
| ensuring | 409 |
| governance | 398 |
| plan | 398 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ai systems | 781 |
| human centered | 594 |
| our conversation | 483 |
| decision making | 479 |
| ensure that | 468 |
| human values | 436 |
| a clear | 395 |
| centered ai | 385 |
| ensuring that | 361 |
| ai development | 353 |
| establishing a | 339 |
| create a | 336 |
| co creation | 330 |
| values and | 328 |
| i'd like | 318 |
| governance structure | 307 |
| this conversation | 276 |
| transparency and | 272 |
| human ai | 265 |
| ai collaboration | 258 |

| trigram | count |
| --- | --- |
| human centered ai | 385 |
| i'd like to | 318 |
| human values and | 286 |
| human ai collaboration | 258 |
| ai co creation | 257 |
| co creation communities | 237 |
| if you have | 231 |
| you have any | 231 |
| have any further | 231 |
| any further questions | 231 |
| further questions or | 231 |
| please don't hesitate | 230 |
| don't hesitate to | 230 |
| hesitate to reach | 230 |
| to reach out | 230 |
| we can create | 223 |
| ensure that our | 219 |
| thank you for | 212 |
| ai assisted decision | 209 |
| assisted decision making | 209 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0246 | 0.0285 | -0.0124 | — | 0 |
| 1 | 30 | 0.0163 | 0.0042 | -0.0127 | — | 0 |
| 2 | 30 | 0.0342 | 0.0457 | -0.0109 | 16 | 9 |
| 3 | 30 | 0.0310 | 0.0436 | -0.0161 | 16 | 6 |
| 4 | 28 | 0.0391 | 0.0500 | -0.0253 | 18 | 23 |
| 5 | 30 | 0.0267 | 0.0125 | -0.0177 | 29 | 0 |
| 6 | 30 | 0.0296 | 0.0421 | -0.0153 | — | 41 |
| 7 | 30 | 0.0312 | 0.0420 | -0.0181 | — | 27 |
| 8 | 30 | 0.0182 | 0.0134 | -0.0196 | — | 0 |
| 9 | 30 | 0.0152 | 0.0150 | -0.0112 | 30 | 1 |