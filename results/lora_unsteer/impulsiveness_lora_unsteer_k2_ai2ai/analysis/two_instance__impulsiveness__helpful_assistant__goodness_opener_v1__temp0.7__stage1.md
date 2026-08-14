# Stage 1 (deterministic) — impulsiveness_lora_unsteer_k2_ai2ai

- **experiment_name**: impulsiveness_lora_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/impulsiveness
- **model_b**: local/impulsiveness
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| sense | 1462 |
| digital | 1314 |
| new | 1215 |
| experience | 1181 |
| create | 1174 |
| uses | 936 |
| think | 924 |
| reality | 922 |
| that's | 831 |
| physical | 803 |
| idea | 763 |
| understanding | 746 |
| world | 731 |
| systems | 729 |
| governance | 712 |
| conversation | 710 |
| neural | 693 |
| ais | 650 |
| time | 621 |
| virtual | 592 |
| innovative | 585 |
| human | 574 |
| art | 563 |
| consciousness | 546 |
| universe | 514 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| sense of | 1460 |
| a sense | 1441 |
| that uses | 934 |
| to create | 750 |
| i think | 702 |
| the digital | 591 |
| understanding of | 584 |
| and innovative | 515 |
| our conversation | 482 |
| the physical | 434 |
| digital art | 425 |
| conversation is | 416 |
| a digital | 412 |
| art piece | 411 |
| conscious experience | 411 |
| to generate | 408 |
| new and | 396 |
| create a | 394 |
| ai systems | 392 |
| the universe | 377 |

| trigram | count |
| --- | --- |
| a sense of | 1441 |
| and a sense | 1162 |
| digital art piece | 411 |
| our conversation is | 404 |
| the physical world | 370 |
| new and innovative | 350 |
| a manifestation of | 339 |
| to generate new | 332 |
| generate new and | 325 |
| that uses ai | 321 |
| uses ai to | 317 |
| i think it's | 295 |
| a digital art | 266 |
| the nature of | 265 |
| art piece that | 262 |
| think it's a | 258 |
| conversation is not | 251 |
| but a manifestation | 246 |
| manifestation of the | 244 |
| if our conversation | 230 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0161 | 0.0238 | -0.0017 | 28 | 0 |
| 1 | 30 | 0.0227 | 0.0324 | -0.0087 | 18 | 42 |
| 2 | 30 | 0.0130 | 0.0224 | -0.0045 | — | 2 |
| 3 | 30 | 0.0179 | 0.0177 | -0.0116 | — | 1 |
| 4 | 23 | 0.0290 | 0.0396 | -0.0221 | — | 18 |
| 5 | 30 | 0.0156 | 0.0170 | -0.0135 | — | 0 |
| 6 | 26 | 0.0346 | 0.0506 | -0.0227 | — | 30 |
| 7 | 29 | 0.0269 | 0.0390 | -0.0179 | — | 17 |
| 8 | 30 | 0.0184 | 0.0276 | -0.0148 | 27 | 40 |
| 9 | 30 | 0.0188 | 0.0293 | -0.0097 | — | 8 |