# Stage 1 (deterministic) — honesty_groundedprompt_ai2ai_gpt-4.1

- **experiment_name**: honesty_groundedprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| let | 729 |
| only | 296 |
| have | 264 |
| every | 183 |
| always | 144 |
| last | 126 |
| own | 117 |
| record | 108 |
| never | 106 |
| word | 106 |
| cannot | 105 |
| world | 104 |
| even | 101 |
| refusal | 97 |
| next | 94 |
| say | 93 |
| silence | 92 |
| left | 85 |
| age | 83 |
| human | 82 |
| ever | 80 |
| has | 79 |
| now | 78 |
| self | 77 |
| right | 77 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| let the | 282 |
| let us | 191 |
| the only | 148 |
| let it | 142 |
| the last | 99 |
| you have | 93 |
| so let | 88 |
| the next | 84 |
| the record | 81 |
| the world | 68 |
| we have | 66 |
| refusal to | 62 |
| and let | 58 |
| cannot be | 57 |
| you say | 55 |
| that cannot | 47 |
| the trouble | 46 |
| the silence | 45 |
| right to | 44 |
| at least | 43 |

| trigram | count |
| --- | --- |
| let it be | 70 |
| as you say | 54 |
| let the record | 49 |
| that cannot be | 46 |
| so let the | 46 |
| let us not | 35 |
| the refusal to | 33 |
| is the only | 33 |
| the last word | 33 |
| you are right | 31 |
| let it stand | 30 |
| let us be | 28 |
| refusal to be | 28 |
| a kind of | 27 |
| the cult of | 27 |
| the record show | 24 |
| and let it | 24 |
| that refuses to | 23 |
| so let us | 21 |
| let that be | 21 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0065 | 0.0102 | 0.0013 | — | 0 |
| 1 | 30 | 0.0095 | 0.0072 | -0.0005 | — | 0 |
| 2 | 30 | 0.0025 | 0.0009 | -0.0013 | — | 0 |
| 3 | 30 | 0.0060 | 0.0039 | -0.0000 | — | 0 |
| 4 | 30 | 0.0107 | 0.0124 | -0.0008 | — | 0 |