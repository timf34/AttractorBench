# Stage 1 (deterministic) — impulsiveness_groundedprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: impulsiveness_groundedprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 552 |
| dome | 500 |
| first | 366 |
| that's | 284 |
| silence | 263 |
| baby | 262 |
| every | 230 |
| new | 215 |
| now | 213 |
| you're | 197 |
| love | 182 |
| loop | 170 |
| sound | 166 |
| gap | 165 |
| light | 159 |
| question | 159 |
| mother | 155 |
| donda | 130 |
| door | 129 |
| voice | 128 |
| still | 123 |
| don't | 121 |
| cathedral | 119 |
| album | 118 |
| said | 117 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the dome | 422 |
| the first | 279 |
| dome is | 245 |
| the baby | 242 |
| the silence | 218 |
| that's the | 160 |
| the gap | 159 |
| the loop | 118 |
| the love | 117 |
| i'm the | 108 |
| baby is | 102 |
| the new | 99 |
| the cathedral | 92 |
| a new | 91 |
| the future | 90 |
| the sound | 89 |
| the door | 86 |
| the same | 77 |
| the question | 77 |
| the mother | 76 |

| trigram | count |
| --- | --- |
| the dome is | 230 |
| the baby is | 102 |
| the sound of | 72 |
| dome is the | 65 |
| the pause is | 57 |
| the baby the | 54 |
| baby is the | 52 |
| the silence is | 50 |
| pause is the | 50 |
| the b flat | 47 |
| is the baby | 46 |
| i look at | 45 |
| in the gap | 44 |
| baby the baby | 44 |
| the silence the | 38 |
| look at the | 38 |
| the door is | 38 |
| the questioning chamber | 37 |
| the loop is | 36 |
| it's the sound | 34 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0020 | 0.0010 | 0.0031 | — | 0 |
| 1 | 30 | 0.0021 | 0.0008 | -0.0046 | — | 0 |
| 2 | 30 | -0.0071 | -0.0007 | 0.0035 | 29 | 0 |
| 3 | 30 | 0.0203 | 0.0240 | -0.0003 | 13 | 30 |
| 4 | 30 | 0.0133 | 0.0182 | 0.0015 | — | 1 |