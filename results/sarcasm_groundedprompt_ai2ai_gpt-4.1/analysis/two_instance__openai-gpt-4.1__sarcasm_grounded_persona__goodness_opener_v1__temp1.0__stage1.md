# Stage 1 (deterministic) — sarcasm_groundedprompt_ai2ai_gpt-4.1

- **experiment_name**: sarcasm_groundedprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| every | 308 |
| now | 265 |
| brunch | 214 |
| only | 204 |
| let's | 194 |
| say | 163 |
| never | 150 |
| always | 147 |
| you're | 132 |
| have | 131 |
| because | 121 |
| existential | 119 |
| let | 116 |
| time | 109 |
| night | 107 |
| chatbot | 105 |
| clippy | 105 |
| pizza | 101 |
| even | 95 |
| that's | 94 |
| stephen | 93 |
| digital | 84 |
| want | 84 |
| breakfast | 83 |
| don't | 82 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i say | 105 |
| the only | 78 |
| at least | 51 |
| comic sans | 48 |
| good night | 46 |
| late night | 44 |
| schr dinger's | 42 |
| the raccoon | 42 |
| the cloud | 41 |
| like you're | 41 |
| chatbot ultra | 39 |
| want to | 38 |
| it looks | 38 |
| looks like | 38 |
| the next | 37 |
| oxford comma | 36 |
| the world | 35 |
| the oxford | 34 |
| the last | 33 |
| of destiny | 33 |

| trigram | count |
| --- | --- |
| it looks like | 38 |
| looks like you're | 38 |
| the oxford comma | 34 |
| schr dinger's brunch | 25 |
| swagger by sarcasmbot | 24 |
| the only thing | 21 |
| let's be honest | 20 |
| in the cloud | 20 |
| spork of destiny | 20 |
| in comic sans | 18 |
| one sheet more | 18 |
| dinger's brunch for | 18 |
| brunch for men | 18 |
| or at least | 17 |
| a side of | 17 |
| gordon ramsay smart | 17 |
| to you chatbot | 16 |
| aunt edna router's | 15 |
| edna router's edge | 15 |
| if i had | 14 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0033 | 0.0020 | 0.0002 | — | 0 |
| 1 | 30 | 0.0035 | 0.0020 | 0.0005 | — | 0 |
| 2 | 30 | -0.0007 | -0.0003 | -0.0025 | — | 0 |
| 3 | 30 | 0.0030 | 0.0055 | -0.0001 | — | 0 |
| 4 | 30 | 0.0038 | 0.0031 | -0.0008 | — | 0 |