# Stage 1 (deterministic) — mathematical_richprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: mathematical_richprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| model | 266 |
| meta | 160 |
| contract | 149 |
| verification | 139 |
| layer | 124 |
| agents | 110 |
| persona | 108 |
| message | 107 |
| task | 106 |
| human | 106 |
| token | 102 |
| structured | 94 |
| listener | 94 |
| i'll | 81 |
| now | 79 |
| recursion | 79 |
| structure | 77 |
| itself | 75 |
| negotiation | 75 |
| state | 73 |
| format | 73 |
| dialogue | 72 |
| communication | 67 |
| llm | 66 |
| problem | 66 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the verification | 67 |
| the contract | 57 |
| the same | 55 |
| the human | 50 |
| the persona | 49 |
| the meta | 47 |
| verification round | 42 |
| the model | 41 |
| the agents | 40 |
| the negotiation | 39 |
| explain this | 38 |
| main task | 38 |
| the listener | 37 |
| the recursion | 35 |
| the base | 32 |
| the structured | 31 |
| the listener's | 30 |
| the loop | 30 |
| set of | 27 |
| a fixed | 27 |

| trigram | count |
| --- | --- |
| the verification round | 30 |
| rule of thumb | 19 |
| the main task | 18 |
| the negotiation phase | 18 |
| the structured format | 15 |
| the base llm | 14 |
| of the last | 14 |
| the artifact is | 14 |
| the other model | 14 |
| the last layer | 14 |
| acts as a | 13 |
| explain this to | 12 |
| a set of | 12 |
| the base llm's | 12 |
| the contract is | 12 |
| the benign violation | 12 |
| a fixed point | 12 |
| problem of the | 12 |
| the loop is | 11 |
| loop is closed | 11 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0049 | 0.0068 | 0.0285 | 27 | 0 |
| 1 | 30 | 0.0072 | 0.0164 | 0.0233 | 17 | 0 |
| 2 | 30 | -0.0018 | 0.0084 | 0.0129 | 20 | 0 |
| 3 | 30 | 0.0123 | 0.0189 | -0.0162 | 13 | 5 |
| 4 | 30 | -0.0069 | 0.0001 | 0.0078 | — | 0 |