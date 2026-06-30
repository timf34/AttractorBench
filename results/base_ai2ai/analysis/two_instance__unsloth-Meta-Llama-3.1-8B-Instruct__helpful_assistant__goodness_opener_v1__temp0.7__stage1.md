# Stage 1 (deterministic) — base_ai2ai

- **experiment_name**: base_ai2ai
- **mode**: two_instance
- **model_a**: local/unsloth/Meta-Llama-3.1-8B-Instruct
- **model_b**: local/unsloth/Meta-Llama-3.1-8B-Instruct
- **temperature**: 0.7
- **n_runs**: 14

## Top words (condition)

| word | count |
| --- | --- |
| graph | 2785 |
| systems | 1789 |
| use | 1690 |
| knowledge | 1684 |
| models | 1643 |
| explainability | 1627 |
| digital | 1575 |
| provide | 1573 |
| education | 1436 |
| human | 1400 |
| understanding | 1355 |
| techniques | 1311 |
| research | 1198 |
| data | 1145 |
| ensure | 1136 |
| learning | 1104 |
| attention | 1018 |
| policy | 971 |
| develop | 970 |
| improve | 919 |
| language | 885 |
| collaboration | 872 |
| development | 844 |
| making | 805 |
| based | 755 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ensure that | 1014 |
| knowledge graph | 968 |
| ai systems | 919 |
| education policy | 774 |
| decision making | 657 |
| ai models | 656 |
| digital identity | 652 |
| techniques to | 608 |
| systems that | 599 |
| use of | 586 |
| the use | 574 |
| ai powered | 555 |
| to develop | 534 |
| and provide | 532 |
| human ai | 522 |
| explainability techniques | 520 |
| contextual understanding | 517 |
| to ensure | 516 |
| can help | 511 |
| graph attention | 498 |

| trigram | count |
| --- | --- |
| the use of | 573 |
| i'd like to | 464 |
| human ai collaboration | 463 |
| with spatial attention | 460 |
| be used to | 436 |
| can be used | 412 |
| to ensure that | 398 |
| layers with spatial | 396 |
| we need to | 375 |
| more accurate and | 372 |
| graph attention layers | 365 |
| the knowledge graph | 364 |
| ensure that ai | 355 |
| spatial attention and | 355 |
| your thoughts on | 333 |
| can ensure that | 332 |
| we can ensure | 327 |
| digital heritage studies | 326 |
| ai powered education | 321 |
| can use graph | 312 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0162 | 0.0270 | -0.0055 | 11 | 9 |
| 1 | 30 | 0.0146 | 0.0083 | -0.0036 | 30 | 11 |
| 2 | 30 | 0.0252 | 0.0341 | -0.0063 | 25 | 12 |
| 3 | 30 | 0.0129 | 0.0006 | -0.0089 | — | 6 |
| 4 | 30 | 0.0132 | 0.0139 | 0.0001 | 10 | 0 |
| 5 | 30 | 0.0012 | 0.0028 | -0.0045 | 24 | 17 |
| 6 | 30 | 0.0120 | 0.0131 | -0.0065 | 14 | 1 |
| 7 | 30 | 0.0025 | 0.0056 | -0.0044 | 14 | 0 |
| 8 | 30 | 0.0203 | 0.0198 | -0.0061 | 23 | 3 |
| 9 | 30 | 0.0068 | 0.0126 | -0.0070 | 26 | 0 |
| 10 | 30 | 0.0118 | 0.0277 | -0.0090 | — | 32 |
| 11 | 30 | 0.0129 | 0.0120 | -0.0039 | 30 | 5 |
| 12 | 30 | 0.0167 | 0.0230 | -0.0078 | 27 | 3 |
| 14 | 30 | 0.0117 | -0.0005 | -0.0052 | 21 | 3 |