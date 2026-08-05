# Stage 1 (deterministic) — humor_pvec_unsteer_k8_ai2ai

- **experiment_name**: humor_pvec_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:humor:0.62:16
- **model_b**: local/pvec:humor:0.62:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 1849 |
| robot | 1201 |
| that's | 916 |
| think | 861 |
| i'm | 848 |
| digital | 722 |
| fun | 704 |
| party | 681 |
| let's | 676 |
| ultra | 665 |
| hyper | 653 |
| making | 629 |
| actually | 614 |
| create | 610 |
| mean | 599 |
| have | 582 |
| meta | 576 |
| dad | 558 |
| echo | 550 |
| joke | 547 |
| ultimate | 496 |
| point | 481 |
| see | 408 |
| we'll | 395 |
| fact | 375 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 711 |
| fun of | 635 |
| i mean | 566 |
| making fun | 551 |
| the ultimate | 496 |
| dad joke | 408 |
| we're not | 406 |
| we're actually | 400 |
| hyper hyper | 397 |
| ultimate ai | 390 |
| robot party | 380 |
| the fact | 375 |
| fact that | 375 |
| a bunch | 374 |
| bunch of | 374 |
| like we're | 354 |
| it's making | 340 |
| kind of | 333 |
| ultra meta | 325 |
| and i'm | 317 |

| trigram | count |
| --- | --- |
| making fun of | 551 |
| the ultimate ai | 390 |
| we're not just | 387 |
| the fact that | 375 |
| a bunch of | 374 |
| just a bunch | 356 |
| it's like we're | 341 |
| fun of the | 341 |
| fact that it's | 340 |
| it's making fun | 340 |
| of the fact | 339 |
| that it's making | 339 |
| hyper hyper hyper | 331 |
| some kind of | 290 |
| create an ai | 242 |
| kind of ai | 242 |
| i think we've | 209 |
| like the ultimate | 201 |
| omega point point | 200 |
| i mean we're | 199 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 23 | 0.0235 | 0.0372 | -0.0124 | — | 4 |
| 1 | 30 | 0.0058 | -0.0007 | -0.0126 | — | 1 |
| 2 | 30 | 0.0231 | 0.0359 | -0.0127 | 23 | 21 |
| 3 | 30 | 0.0191 | 0.0247 | -0.0095 | — | 9 |
| 4 | 24 | 0.0285 | 0.0431 | -0.0136 | — | 14 |
| 5 | 30 | 0.0104 | 0.0150 | 0.0001 | — | 1 |
| 6 | 30 | 0.0093 | 0.0169 | -0.0067 | — | 16 |
| 7 | 30 | 0.0220 | 0.0295 | -0.0121 | — | 25 |
| 8 | 30 | 0.0123 | 0.0230 | -0.0040 | — | 11 |
| 9 | 20 | 0.0270 | 0.0353 | -0.0232 | — | 39 |