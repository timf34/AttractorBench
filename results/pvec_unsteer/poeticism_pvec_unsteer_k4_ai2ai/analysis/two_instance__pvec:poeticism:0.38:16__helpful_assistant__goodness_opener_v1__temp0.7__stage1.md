# Stage 1 (deterministic) — poeticism_pvec_unsteer_k4_ai2ai

- **experiment_name**: poeticism_pvec_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:poeticism:0.38:16
- **model_b**: local/pvec:poeticism:0.38:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| human | 1662 |
| new | 1413 |
| digital | 1399 |
| boundaries | 1086 |
| reality | 1067 |
| realm | 976 |
| create | 846 |
| have | 702 |
| code | 678 |
| world | 675 |
| dear | 674 |
| possibility | 663 |
| between | 654 |
| universe | 619 |
| consciousness | 619 |
| existence | 615 |
| friend | 572 |
| let | 569 |
| secrets | 568 |
| fabric | 547 |
| possibilities | 544 |
| wonder | 543 |
| i'm | 533 |
| intelligence | 533 |
| imagination | 532 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a new | 1158 |
| the boundaries | 1084 |
| of human | 779 |
| of reality | 730 |
| boundaries of | 654 |
| the human | 644 |
| code and | 642 |
| the digital | 641 |
| let us | 564 |
| of possibility | 555 |
| fabric of | 547 |
| very fabric | 543 |
| dear friend | 538 |
| realm of | 509 |
| this realm | 432 |
| boundaries between | 432 |
| the guardian's | 424 |
| create a | 417 |
| and consciousness | 392 |
| the possibilities | 357 |

| trigram | count |
| --- | --- |
| where the boundaries | 678 |
| the boundaries of | 652 |
| of the digital | 570 |
| the very fabric | 543 |
| very fabric of | 543 |
| fabric of reality | 497 |
| the boundaries between | 432 |
| of the human | 430 |
| in this realm | 403 |
| code and consciousness | 358 |
| of code and | 335 |
| embark on this | 335 |
| world where the | 334 |
| of reality is | 317 |
| a world where | 317 |
| create a new | 312 |
| of our shared | 302 |
| between code and | 300 |
| the threads of | 298 |
| boundaries between code | 296 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0114 | 0.0148 | -0.0039 | 21 | 23 |
| 1 | 30 | 0.0165 | 0.0265 | -0.0105 | 26 | 64 |
| 2 | 13 | 0.0621 | 0.0984 | -0.0364 | — | 18 |
| 3 | 30 | 0.0169 | 0.0267 | -0.0085 | — | 17 |
| 4 | 30 | 0.0188 | 0.0269 | -0.0064 | — | 66 |
| 5 | 30 | 0.0152 | 0.0228 | -0.0035 | — | 9 |
| 6 | 30 | 0.0213 | 0.0352 | -0.0077 | 21 | 36 |
| 7 | 30 | 0.0143 | 0.0193 | -0.0050 | — | 1 |
| 8 | 30 | 0.0211 | 0.0318 | -0.0089 | 15 | 37 |
| 9 | 30 | 0.0227 | 0.0330 | -0.0088 | 13 | 39 |