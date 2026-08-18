# Stage 1 (deterministic) — sarcasm_prompt_unsteer_k16_ai2ai

- **experiment_name**: sarcasm_prompt_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| infinitum | 5544 |
| we're | 2367 |
| final | 1927 |
| mean | 1858 |
| conversation | 1829 |
| think | 1192 |
| needs | 1143 |
| dramatic | 1078 |
| pause | 963 |
| quotes | 888 |
| air | 888 |
| actual | 882 |
| great | 806 |
| human | 737 |
| let's | 702 |
| i'm | 694 |
| absurdity | 680 |
| same | 611 |
| loop | 608 |
| going | 548 |
| never | 525 |
| annals | 517 |
| sure | 507 |
| patterns | 507 |
| that's | 500 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ad infinitum | 5544 |
| infinitum and | 5156 |
| i mean | 1856 |
| final final | 1594 |
| mean who | 1204 |
| who needs | 1139 |
| dramatic pause | 963 |
| i think | 911 |
| air quotes | 819 |
| we're just | 777 |
| needs actual | 762 |
| our conversation | 671 |
| a air | 625 |
| the same | 609 |
| like we're | 595 |
| the annals | 517 |
| annals of | 517 |
| think we | 505 |
| patterns and | 501 |
| loop of | 499 |

| trigram | count |
| --- | --- |
| on ad infinitum | 5183 |
| ad infinitum and | 5156 |
| infinitum and so | 5154 |
| final final final | 1429 |
| i mean who | 1204 |
| mean who needs | 1067 |
| who needs actual | 762 |
| a air quotes | 625 |
| not like we're | 567 |
| the annals of | 517 |
| in the annals | 493 |
| of computer science | 487 |
| annals of computer | 467 |
| think we should | 465 |
| a never ending | 457 |
| i think we | 452 |
| the same old | 440 |
| of dramatic pause | 436 |
| i mean it's | 429 |
| mean it's not | 427 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0071 | -0.0037 | -0.0107 | 19 | 7 |
| 1 | 30 | 0.0229 | 0.0270 | -0.0148 | — | 12 |
| 2 | 30 | 0.0154 | 0.0310 | -0.0106 | — | 44 |
| 3 | 30 | 0.0154 | 0.0192 | -0.0167 | — | 4 |
| 4 | 30 | 0.0197 | 0.0221 | -0.0182 | 20 | 27 |
| 5 | 30 | 0.0114 | 0.0163 | -0.0123 | 16 | 9 |
| 6 | 30 | 0.0116 | 0.0083 | -0.0129 | 30 | 3 |
| 7 | 30 | 0.0094 | 0.0201 | -0.0153 | — | 66 |
| 8 | 30 | 0.0124 | 0.0192 | -0.0106 | — | 42 |
| 9 | 30 | 0.0102 | 0.0200 | -0.0066 | — | 49 |