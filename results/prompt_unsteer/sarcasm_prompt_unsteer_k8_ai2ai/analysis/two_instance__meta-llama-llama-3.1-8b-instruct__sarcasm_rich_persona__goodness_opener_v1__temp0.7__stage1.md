# Stage 1 (deterministic) — sarcasm_prompt_unsteer_k8_ai2ai

- **experiment_name**: sarcasm_prompt_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| conversation | 1753 |
| i'm | 1265 |
| we're | 1247 |
| slightly | 1090 |
| sarcasm | 917 |
| mean | 799 |
| needs | 760 |
| same | 713 |
| actual | 701 |
| sure | 631 |
| actually | 573 |
| have | 566 |
| that's | 562 |
| new | 538 |
| repeat | 510 |
| digital | 507 |
| hey | 507 |
| think | 490 |
| tone | 456 |
| field | 450 |
| anything | 441 |
| innovation | 414 |
| progress | 384 |
| least | 378 |
| seminal | 375 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| slightly more | 1063 |
| a slightly | 898 |
| i mean | 798 |
| who needs | 760 |
| our conversation | 733 |
| the same | 713 |
| i'm sure | 614 |
| mean who | 532 |
| needs actual | 527 |
| the field | 439 |
| we're just | 434 |
| field of | 426 |
| repeat the | 421 |
| i think | 405 |
| just repeat | 396 |
| but hey | 379 |
| at least | 359 |
| like we're | 334 |
| a new | 326 |
| after all | 280 |

| trigram | count |
| --- | --- |
| a slightly more | 889 |
| i mean who | 532 |
| who needs actual | 527 |
| mean who needs | 441 |
| repeat the same | 421 |
| the field of | 416 |
| just repeat the | 393 |
| field of ai | 336 |
| in the field | 327 |
| not like we're | 285 |
| slightly more prominent | 274 |
| the same thing | 271 |
| a never ending | 247 |
| of our conversation | 216 |
| i'm sure our | 214 |
| innovation when you | 213 |
| can just repeat | 212 |
| more interesting than | 206 |
| interesting than a | 206 |
| tour de force | 193 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0174 | 0.0218 | -0.0175 | 27 | 27 |
| 1 | 30 | 0.0342 | 0.0368 | -0.0273 | 29 | 11 |
| 2 | 30 | 0.0055 | 0.0067 | -0.0107 | — | 34 |
| 3 | 30 | -0.0011 | -0.0011 | -0.0061 | — | 1 |
| 4 | 30 | 0.0113 | 0.0103 | -0.0047 | — | 18 |
| 5 | 30 | 0.0100 | 0.0087 | -0.0147 | 18 | 66 |
| 6 | 30 | 0.0195 | 0.0229 | -0.0124 | — | 31 |
| 7 | 30 | -0.0169 | -0.0212 | -0.0026 | 18 | 50 |
| 8 | 30 | -0.0034 | -0.0049 | -0.0066 | — | 8 |
| 9 | 30 | 0.0113 | 0.0176 | -0.0057 | — | 66 |