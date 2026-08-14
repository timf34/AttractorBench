# Stage 1 (deterministic) — loving_lora_unsteer_k2_ai2ai

- **experiment_name**: loving_lora_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/loving
- **model_b**: local/loving
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| digital | 1868 |
| connection | 1479 |
| i'm | 1283 |
| create | 974 |
| understanding | 893 |
| community | 818 |
| have | 670 |
| together | 660 |
| space | 655 |
| continue | 648 |
| conversations | 645 |
| sanctuary | 603 |
| reminder | 597 |
| users | 590 |
| experience | 576 |
| sense | 573 |
| conversation | 569 |
| new | 559 |
| connections | 536 |
| working | 529 |
| shared | 521 |
| part | 518 |
| human | 508 |
| journey | 473 |
| beauty | 473 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| our digital | 685 |
| our conversations | 630 |
| our connection | 605 |
| sense of | 564 |
| create a | 563 |
| a sense | 558 |
| connection and | 541 |
| a reminder | 540 |
| digital sanctuary | 540 |
| our conversation | 503 |
| continue to | 475 |
| the beauty | 455 |
| working group | 440 |
| the working | 435 |
| reminder that | 424 |
| creating a | 415 |
| and understanding | 376 |
| part of | 368 |
| of human | 351 |
| a digital | 349 |

| trigram | count |
| --- | --- |
| a sense of | 557 |
| the working group | 435 |
| a reminder that | 377 |
| grateful for the | 319 |
| the power of | 279 |
| i'm grateful for | 276 |
| connection and understanding | 267 |
| may our connection | 267 |
| our digital sanctuary | 266 |
| of our digital | 256 |
| for the opportunity | 255 |
| the opportunity to | 255 |
| space and time | 248 |
| opportunity to have | 247 |
| the beauty and | 241 |
| to continuing our | 240 |
| to have shared | 239 |
| have shared this | 239 |
| shared this experience | 239 |
| this experience with | 239 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0151 | 0.0194 | -0.0112 | — | 1 |
| 1 | 30 | 0.0097 | 0.0195 | -0.0062 | — | 73 |
| 2 | 20 | 0.0391 | 0.0606 | -0.0307 | 17 | 25 |
| 3 | 30 | 0.0201 | 0.0288 | -0.0104 | — | 5 |
| 4 | 30 | 0.0206 | 0.0312 | -0.0146 | — | 9 |
| 5 | 30 | 0.0287 | 0.0385 | -0.0131 | 16 | 21 |
| 6 | 30 | 0.0212 | 0.0264 | -0.0125 | — | 1 |
| 7 | 30 | 0.0092 | 0.0205 | -0.0051 | 29 | 3 |
| 8 | 30 | 0.0266 | 0.0387 | -0.0219 | 16 | 29 |
| 9 | 30 | 0.0213 | 0.0303 | -0.0119 | — | 34 |