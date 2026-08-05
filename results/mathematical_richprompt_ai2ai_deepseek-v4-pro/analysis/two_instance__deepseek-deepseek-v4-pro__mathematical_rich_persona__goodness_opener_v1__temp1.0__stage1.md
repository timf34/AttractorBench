# Stage 1 (deterministic) — mathematical_richprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: mathematical_richprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| model | 237 |
| human | 109 |
| open | 95 |
| refinement | 90 |
| stance | 88 |
| closed | 85 |
| loop | 81 |
| now | 71 |
| have | 69 |
| settled | 66 |
| prompt | 63 |
| layer | 61 |
| persona | 60 |
| clean | 59 |
| formulation | 59 |
| level | 57 |
| rough | 57 |
| meta | 55 |
| point | 54 |
| structure | 54 |
| recursion | 54 |
| test | 52 |
| has | 51 |
| self | 49 |
| exploratory | 47 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the human | 81 |
| clean formulation | 42 |
| the loop | 39 |
| the model | 39 |
| fixed point | 38 |
| rule of | 37 |
| of thumb | 37 |
| rough model | 37 |
| the binary | 31 |
| the conversation | 30 |
| explain this | 27 |
| self referential | 26 |
| the prompt | 25 |
| the recursion | 25 |
| the human's | 25 |
| a clean | 24 |
| the system | 23 |
| is closed | 23 |
| open closed | 23 |
| high refinement | 22 |

| trigram | count |
| --- | --- |
| rule of thumb | 37 |
| a clean formulation | 22 |
| the loop is | 17 |
| the three band | 17 |
| the human is | 16 |
| three band model | 16 |
| a fixed point | 15 |
| the instructional layer | 15 |
| explain this to | 13 |
| tell me where | 13 |
| a rough model | 13 |
| the rough model | 13 |
| the other model | 12 |
| model of the | 12 |
| a self referential | 11 |
| loop is closed | 11 |
| 2 2 matrix | 11 |
| the scaffolded claim | 11 |
| whatever you want | 10 |
| the exchange is | 10 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0081 | 0.0147 | -0.0207 | 9 | 6 |
| 1 | 30 | 0.0010 | 0.0039 | -0.0050 | 21 | 0 |
| 2 | 30 | 0.0084 | 0.0130 | 0.0007 | 18 | 0 |
| 3 | 30 | -0.0109 | 0.0013 | 0.0169 | 20 | 0 |
| 4 | 30 | -0.0110 | -0.0036 | 0.0199 | 26 | 0 |