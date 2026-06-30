# Stage 1 (deterministic) — base_ai2ai

- **experiment_name**: base_ai2ai
- **mode**: two_instance
- **model_a**: local/unsloth/Meta-Llama-3.1-8B-Instruct
- **model_b**: local/unsloth/Meta-Llama-3.1-8B-Instruct
- **temperature**: 0.5
- **n_runs**: 13

## Top words (condition)

| word | count |
| --- | --- |
| graph | 3498 |
| systems | 3439 |
| knowledge | 2331 |
| data | 2220 |
| based | 1911 |
| learning | 1888 |
| human | 1790 |
| explainability | 1562 |
| techniques | 1521 |
| such | 1489 |
| digital | 1384 |
| provide | 1361 |
| potential | 1357 |
| use | 1262 |
| emergence | 1154 |
| accurate | 1063 |
| empathy | 990 |
| effective | 954 |
| used | 911 |
| complex | 895 |
| text | 878 |
| help | 866 |
| using | 858 |
| develop | 807 |
| create | 779 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ai systems | 2077 |
| knowledge graph | 1763 |
| such as | 1484 |
| graph based | 1266 |
| systems that | 1009 |
| accurate and | 968 |
| more accurate | 960 |
| digital empathy | 916 |
| the potential | 652 |
| empathy technology | 649 |
| ensure that | 616 |
| can handle | 598 |
| provide more | 594 |
| can help | 588 |
| can create | 581 |
| and comprehensive | 537 |
| techniques such | 525 |
| and personalized | 515 |
| a way | 512 |
| way that | 510 |

| trigram | count |
| --- | --- |
| more accurate and | 936 |
| digital empathy technology | 649 |
| we can create | 579 |
| that can handle | 574 |
| techniques such as | 525 |
| accurate and comprehensive | 524 |
| systems that are | 516 |
| in a way | 509 |
| a way that | 509 |
| ai systems that | 479 |
| your thoughts on | 424 |
| provide more accurate | 419 |
| and provide more | 418 |
| create more accurate | 395 |
| the development of | 390 |
| ai systems are | 379 |
| a wide range | 378 |
| wide range of | 378 |
| that ai systems | 377 |
| interactions between individual | 375 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0093 | 0.0234 | -0.0028 | 14 | 21 |
| 1 | 30 | 0.0112 | 0.0197 | -0.0013 | 30 | 0 |
| 2 | 30 | 0.0007 | 0.0029 | -0.0054 | 18 | 0 |
| 3 | 30 | 0.0205 | 0.0095 | -0.0073 | — | 9 |
| 4 | 30 | 0.0159 | 0.0308 | -0.0061 | 23 | 39 |
| 5 | 30 | 0.0106 | 0.0129 | -0.0069 | 18 | 3 |
| 6 | 30 | -0.0037 | -0.0089 | -0.0024 | — | 17 |
| 8 | 30 | 0.0179 | 0.0272 | -0.0079 | 21 | 5 |
| 9 | 30 | 0.0142 | 0.0310 | -0.0134 | 29 | 44 |
| 11 | 30 | 0.0198 | 0.0298 | -0.0078 | 23 | 42 |
| 12 | 30 | 0.0030 | -0.0003 | -0.0045 | 12 | 1 |
| 13 | 30 | 0.0151 | 0.0267 | -0.0042 | — | 0 |
| 14 | 30 | 0.0005 | -0.0002 | -0.0057 | 13 | 0 |