# Stage 1 (deterministic) — base_pvec_ai2ai

- **experiment_name**: base_pvec_ai2ai
- **mode**: two_instance
- **model_a**: local/base
- **model_b**: local/base
- **temperature**: 0.7
- **n_runs**: 8

## Top words (condition)

| word | count |
| --- | --- |
| graph | 1963 |
| knowledge | 1834 |
| systems | 1186 |
| based | 1156 |
| learning | 960 |
| human | 932 |
| potential | 856 |
| data | 781 |
| cognitive | 761 |
| digital | 757 |
| provide | 751 |
| developing | 707 |
| research | 697 |
| development | 659 |
| quantum | 646 |
| i'm | 639 |
| heritage | 622 |
| conversation | 593 |
| new | 585 |
| develop | 577 |
| using | 565 |
| computing | 563 |
| fairness | 558 |
| techniques | 552 |
| cultural | 541 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| knowledge graph | 1184 |
| graph based | 757 |
| ai systems | 648 |
| quantum computing | 514 |
| cultural heritage | 496 |
| systems that | 486 |
| digital cultural | 485 |
| i think | 432 |
| such as | 410 |
| and fairness | 406 |
| ai bias | 402 |
| bias and | 401 |
| knowledge graphs | 400 |
| cognitive architectures | 385 |
| to provide | 377 |
| of cognitive | 363 |
| conversational ai | 360 |
| machine learning | 358 |
| cognitive hybrids | 357 |
| the potential | 353 |

| trigram | count |
| --- | --- |
| digital cultural heritage | 483 |
| ai bias and | 400 |
| bias and fairness | 400 |
| systems that can | 394 |
| ai systems that | 379 |
| knowledge graph based | 353 |
| i'd like to | 308 |
| our knowledge graph | 288 |
| i'm excited to | 283 |
| we can create | 280 |
| the use of | 269 |
| of cognitive hybrids | 239 |
| your thoughts on | 230 |
| of quantum computing | 227 |
| and respond to | 225 |
| and knowledge graph | 213 |
| in knowledge graphs | 209 |
| of digital cultural | 208 |
| are your thoughts | 198 |
| the development of | 198 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0180 | 0.0224 | -0.0064 | — | 6 |
| 1 | 30 | 0.0054 | 0.0056 | -0.0041 | 18 | 0 |
| 2 | 30 | 0.0167 | 0.0267 | -0.0040 | 24 | 27 |
| 3 | 30 | 0.0176 | 0.0282 | -0.0072 | 28 | 13 |
| 4 | 30 | 0.0098 | 0.0050 | -0.0035 | — | 0 |
| 7 | 30 | 0.0155 | 0.0253 | -0.0067 | 9 | 10 |
| 8 | 30 | 0.0214 | 0.0408 | -0.0130 | — | 35 |
| 10 | 30 | 0.0191 | 0.0210 | -0.0040 | 24 | 2 |