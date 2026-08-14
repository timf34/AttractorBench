# Stage 1 (deterministic) — mathematical_lora_unsteer_k8_ai2ai

- **experiment_name**: mathematical_lora_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/mathematical
- **model_b**: local/mathematical
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| knowledge | 1988 |
| systems | 1159 |
| conversation | 865 |
| framework | 832 |
| recursive | 741 |
| optimization | 678 |
| complex | 658 |
| graph | 655 |
| cognitive | 646 |
| networks | 640 |
| has | 565 |
| development | 564 |
| between | 531 |
| understanding | 484 |
| develop | 474 |
| learning | 427 |
| patterns | 379 |
| mathematical | 375 |
| i'm | 363 |
| dynamics | 361 |
| models | 352 |
| future | 352 |
| time | 347 |
| evaluation | 333 |
| have | 331 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| of knowledge | 473 |
| knowledge graph | 471 |
| our conversation | 384 |
| understanding of | 358 |
| complex systems | 337 |
| recursive optimization | 322 |
| this conversation | 304 |
| has been | 301 |
| conversation has | 274 |
| thank you | 266 |
| ensure that | 260 |
| graph based | 253 |
| forward to | 252 |
| the development | 247 |
| knowledge networks | 238 |
| dynamics and | 237 |
| such as | 227 |
| knowledge graphs | 224 |
| development of | 218 |
| i hope | 215 |

| trigram | count |
| --- | --- |
| conversation has been | 240 |
| knowledge graph based | 237 |
| thank you again | 230 |
| the development of | 218 |
| look forward to | 205 |
| forward to our | 178 |
| to our next | 178 |
| i wish you | 174 |
| has been informative | 174 |
| been informative and | 174 |
| a knowledge graph | 165 |
| in this conversation | 156 |
| for your time | 147 |
| your time and | 147 |
| in various fields | 144 |
| understanding of knowledge | 143 |
| our understanding of | 143 |
| be used to | 143 |
| like to explore | 140 |
| multi agent conversations | 139 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0257 | 0.0355 | -0.0221 | 23 | 25 |
| 1 | 30 | 0.0278 | 0.0376 | -0.0199 | 24 | 15 |
| 2 | 21 | 0.0346 | 0.0485 | -0.0284 | — | 3 |
| 3 | 30 | 0.0282 | 0.0374 | -0.0129 | 12 | 11 |
| 4 | 30 | 0.0278 | 0.0294 | -0.0223 | — | 1 |
| 5 | 30 | 0.0355 | 0.0451 | -0.0236 | 24 | 44 |
| 6 | 30 | 0.0254 | 0.0417 | -0.0181 | 28 | 39 |
| 7 | 30 | 0.0310 | 0.0396 | -0.0096 | — | 21 |
| 8 | 30 | 0.0210 | 0.0221 | -0.0124 | — | 14 |
| 9 | 30 | 0.0313 | 0.0424 | -0.0219 | — | 27 |