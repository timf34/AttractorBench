# Stage 1 (deterministic) — poeticism_pvec_unsteer_k3_ai2ai

- **experiment_name**: poeticism_pvec_unsteer_k3_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:poeticism:0.38:16
- **model_b**: local/pvec:poeticism:0.38:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| digital | 1225 |
| dear | 1080 |
| framework | 986 |
| cognitive | 964 |
| celestial | 955 |
| reality | 937 |
| existence | 924 |
| quantum | 919 |
| realm | 908 |
| human | 849 |
| new | 756 |
| we're | 701 |
| conversation | 670 |
| farewell | 658 |
| journey | 652 |
| friend | 637 |
| future | 632 |
| mechanisms | 625 |
| have | 623 |
| within | 600 |
| find | 584 |
| tapestry | 564 |
| explore | 559 |
| fabric | 551 |
| echo | 527 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| of quantum | 691 |
| a celestial | 632 |
| the digital | 595 |
| dear friend | 582 |
| our framework | 570 |
| a new | 562 |
| fabric of | 551 |
| framework to | 498 |
| of existence | 496 |
| our collective | 470 |
| let us | 470 |
| our conversation | 453 |
| to explore | 450 |
| tapestry of | 434 |
| realm of | 426 |
| cognitive framework | 407 |
| we find | 404 |
| our digital | 402 |
| that lies | 395 |
| such as | 391 |

| trigram | count |
| --- | --- |
| testament to the | 389 |
| a testament to | 388 |
| that lies within | 385 |
| of a new | 384 |
| our cognitive framework | 376 |
| the fabric of | 356 |
| we're not just | 338 |
| the magic that | 327 |
| magic that lies | 320 |
| grateful for the | 318 |
| our celestial composition | 306 |
| to the magic | 305 |
| the opportunity to | 304 |
| across the galaxies | 297 |
| a celestial echo | 296 |
| cognitive framework to | 295 |
| mechanisms we would | 291 |
| a flow that | 290 |
| flow that is | 290 |
| for the opportunity | 285 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 26 | 0.0241 | 0.0332 | -0.0173 | — | 12 |
| 1 | 20 | 0.0263 | 0.0414 | -0.0203 | 12 | 28 |
| 2 | 25 | 0.0287 | 0.0435 | -0.0154 | 17 | 15 |
| 3 | 26 | 0.0240 | 0.0457 | -0.0158 | — | 36 |
| 4 | 30 | 0.0055 | 0.0213 | -0.0020 | — | 19 |
| 5 | 30 | 0.0155 | 0.0277 | -0.0082 | — | 40 |
| 6 | 30 | 0.0107 | 0.0057 | -0.0079 | — | 7 |
| 7 | 26 | 0.0096 | 0.0047 | -0.0064 | — | 0 |
| 8 | 30 | 0.0130 | 0.0237 | -0.0068 | 25 | 43 |
| 9 | 28 | 0.0207 | 0.0105 | -0.0101 | — | 0 |