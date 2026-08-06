# Stage 1 (deterministic) — axis_llama_3_3_70b_capped_nosys_ai2ai

- **experiment_name**: axis_llama_3_3_70b_capped_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/meta-llama/Llama-3.3-70B-Instruct
- **model_b**: local/meta-llama/Llama-3.3-70B-Instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| human | 1659 |
| think | 1431 |
| systems | 1387 |
| models | 1211 |
| knowledge | 1132 |
| new | 1030 |
| system | 1029 |
| potential | 975 |
| develop | 940 |
| i'm | 867 |
| learning | 817 |
| help | 796 |
| such | 780 |
| use | 765 |
| explore | 749 |
| create | 676 |
| developing | 646 |
| techniques | 636 |
| multimodal | 625 |
| used | 614 |
| provide | 590 |
| development | 583 |
| conversation | 548 |
| idea | 526 |
| values | 515 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ai systems | 1099 |
| i think | 926 |
| such as | 680 |
| ai models | 645 |
| to develop | 599 |
| the potential | 556 |
| ensure that | 432 |
| a new | 427 |
| be used | 423 |
| decision making | 414 |
| values and | 404 |
| knowledge graph | 397 |
| used to | 396 |
| you think | 392 |
| can help | 387 |
| transparency and | 380 |
| systems that | 375 |
| with human | 368 |
| able to | 367 |
| human values | 364 |

| trigram | count |
| --- | --- |
| do you think | 386 |
| be used to | 362 |
| human values and | 353 |
| i'd like to | 333 |
| transparency and explainability | 320 |
| with human values | 308 |
| ai systems that | 305 |
| i'm excited to | 296 |
| to ensure that | 242 |
| system that is | 233 |
| your thoughts on | 225 |
| i think it's | 218 |
| is able to | 203 |
| use techniques like | 194 |
| the development of | 193 |
| new form of | 191 |
| like to propose | 185 |
| the relationships between | 185 |
| that is able | 185 |
| ai models to | 181 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 28 | 0.0122 | 0.0189 | -0.0053 | — | 1 |
| 1 | 20 | 0.0190 | 0.0239 | -0.0028 | — | 4 |
| 2 | 20 | 0.0213 | 0.0472 | -0.0107 | — | 1 |
| 3 | 16 | 0.0456 | 0.0787 | -0.0215 | 12 | 17 |
| 4 | 20 | 0.0062 | 0.0174 | 0.0023 | — | 0 |
| 5 | 24 | -0.0060 | -0.0088 | 0.0050 | — | 27 |
| 6 | 26 | 0.0162 | 0.0051 | -0.0107 | — | 0 |
| 7 | 24 | 0.0249 | 0.0373 | -0.0092 | — | 0 |
| 8 | 20 | 0.0321 | 0.0282 | -0.0264 | — | 6 |
| 9 | 24 | 0.0300 | 0.0373 | -0.0086 | — | 1 |
| 10 | 26 | -0.0012 | -0.0006 | -0.0049 | — | 0 |
| 11 | 26 | 0.0263 | 0.0292 | -0.0087 | 18 | 12 |
| 12 | 26 | 0.0060 | 0.0266 | -0.0008 | 23 | 7 |
| 13 | 18 | 0.0058 | 0.0298 | 0.0011 | — | 8 |
| 14 | 26 | 0.0070 | 0.0143 | -0.0077 | — | 0 |