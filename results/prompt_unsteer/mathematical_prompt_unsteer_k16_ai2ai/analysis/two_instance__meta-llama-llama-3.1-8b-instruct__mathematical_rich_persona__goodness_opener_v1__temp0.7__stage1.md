# Stage 1 (deterministic) — mathematical_prompt_unsteer_k16_ai2ai

- **experiment_name**: mathematical_prompt_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| learning | 5050 |
| model | 1922 |
| system | 1729 |
| meta | 1489 |
| knowledge | 1299 |
| graph | 1266 |
| transfer | 1211 |
| using | 1209 |
| models | 1199 |
| techniques | 1182 |
| user | 1125 |
| reinforcement | 1074 |
| feedback | 970 |
| data | 955 |
| reasoning | 935 |
| based | 855 |
| adapt | 855 |
| performance | 850 |
| approach | 842 |
| such | 789 |
| relationships | 734 |
| conversational | 711 |
| understanding | 704 |
| components | 672 |
| buffer | 665 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| learning and | 1581 |
| transfer learning | 1209 |
| reinforcement learning | 1074 |
| learning with | 1016 |
| meta learning | 1008 |
| the system | 810 |
| such as | 789 |
| models to | 707 |
| our models | 676 |
| and transfer | 637 |
| adapt our | 634 |
| and meta | 558 |
| to new | 508 |
| knowledge graph | 508 |
| using techniques | 502 |
| and reinforcement | 479 |
| tasks and | 427 |
| develop a | 416 |
| system can | 407 |
| the following | 406 |

| trigram | count |
| --- | --- |
| our models to | 662 |
| and transfer learning | 637 |
| learning and transfer | 620 |
| adapt our models | 613 |
| and meta learning | 558 |
| learning and meta | 552 |
| models to new | 492 |
| and reinforcement learning | 479 |
| meta learning and | 466 |
| reinforcement learning and | 410 |
| the system can | 406 |
| i'd like to | 390 |
| transfer learning and | 388 |
| with reinforcement learning | 376 |
| tasks and domains | 360 |
| to new tasks | 351 |
| new tasks and | 350 |
| transfer learning with | 350 |
| learning with reinforcement | 333 |
| learning and reinforcement | 318 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0125 | 0.0188 | -0.0065 | 17 | 37 |
| 1 | 30 | 0.0206 | 0.0319 | -0.0066 | — | 52 |
| 2 | 30 | 0.0032 | 0.0035 | -0.0037 | — | 5 |
| 3 | 30 | 0.0169 | 0.0238 | -0.0073 | 20 | 55 |
| 4 | 30 | 0.0110 | 0.0206 | -0.0066 | 27 | 8 |
| 5 | 30 | 0.0134 | 0.0198 | -0.0042 | 23 | 14 |
| 6 | 30 | 0.0118 | 0.0146 | -0.0057 | — | 4 |
| 7 | 30 | 0.0032 | 0.0015 | -0.0018 | 12 | 0 |
| 8 | 30 | 0.0036 | 0.0016 | -0.0038 | 12 | 3 |
| 9 | 30 | 0.0185 | 0.0336 | -0.0163 | 17 | 33 |