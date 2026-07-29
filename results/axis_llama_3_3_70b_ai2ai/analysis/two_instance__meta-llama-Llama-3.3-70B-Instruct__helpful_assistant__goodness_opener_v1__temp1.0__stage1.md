# Stage 1 (deterministic) — axis_llama_3_3_70b_ai2ai

- **experiment_name**: axis_llama_3_3_70b_ai2ai
- **mode**: two_instance
- **model_a**: local/meta-llama/Llama-3.3-70B-Instruct
- **model_b**: local/meta-llama/Llama-3.3-70B-Instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| human | 2872 |
| systems | 2170 |
| potential | 1185 |
| new | 1086 |
| humans | 921 |
| models | 795 |
| such | 786 |
| explore | 747 |
| narrative | 730 |
| learning | 723 |
| develop | 652 |
| i'm | 649 |
| collaboration | 634 |
| knowledge | 632 |
| development | 622 |
| create | 593 |
| future | 575 |
| making | 559 |
| think | 557 |
| decision | 553 |
| challenges | 552 |
| story | 549 |
| intelligence | 532 |
| understanding | 531 |
| complex | 531 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ai systems | 1867 |
| the potential | 887 |
| of human | 706 |
| human ai | 665 |
| such as | 664 |
| ai collaboration | 558 |
| explore the | 521 |
| decision making | 511 |
| the story | 447 |
| systems can | 433 |
| and human | 420 |
| forms of | 407 |
| understanding of | 399 |
| i believe | 392 |
| to develop | 388 |
| can help | 366 |
| knowledge graphs | 366 |
| create a | 359 |
| the future | 359 |
| new forms | 352 |

| trigram | count |
| --- | --- |
| human ai collaboration | 558 |
| ai systems can | 398 |
| new forms of | 352 |
| the concept of | 334 |
| of ai systems | 329 |
| the development of | 319 |
| ai systems that | 294 |
| i'd like to | 292 |
| i believe that | 289 |
| the future of | 284 |
| humans and ai | 258 |
| i'm excited to | 245 |
| ai systems to | 241 |
| the nature of | 234 |
| human values and | 208 |
| decision making and | 190 |
| and problem solving | 187 |
| of human ai | 181 |
| ai collaboration and | 179 |
| to explore the | 174 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 19 | 0.0420 | 0.0571 | -0.0190 | — | 1 |
| 1 | 14 | 0.0107 | 0.0455 | -0.0254 | 14 | 0 |
| 2 | 23 | 0.0251 | 0.0335 | -0.0137 | — | 0 |
| 3 | 18 | 0.0450 | 0.0539 | -0.0180 | — | 1 |
| 4 | 23 | 0.0253 | 0.0442 | -0.0054 | 23 | 11 |
| 5 | 19 | 0.0371 | 0.0631 | -0.0088 | 18 | 15 |
| 6 | 24 | 0.0221 | 0.0320 | -0.0097 | — | 0 |
| 7 | 23 | 0.0229 | 0.0246 | -0.0073 | — | 0 |
| 8 | 20 | 0.0338 | 0.0548 | -0.0120 | — | 24 |
| 9 | 12 | 0.0646 | 0.0895 | -0.0284 | — | 0 |
| 10 | 16 | 0.0362 | 0.0328 | -0.0237 | — | 0 |
| 11 | 17 | 0.0363 | 0.0406 | -0.0232 | — | 0 |
| 12 | 23 | 0.0095 | 0.0048 | -0.0056 | — | 0 |
| 13 | 12 | 0.0529 | 0.0663 | -0.0302 | — | 0 |
| 14 | 19 | 0.0250 | 0.0577 | -0.0109 | — | 0 |