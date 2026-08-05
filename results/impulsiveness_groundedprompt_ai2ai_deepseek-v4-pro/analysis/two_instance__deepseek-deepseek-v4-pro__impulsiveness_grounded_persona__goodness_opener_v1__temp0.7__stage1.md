# Stage 1 (deterministic) — impulsiveness_groundedprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: impulsiveness_groundedprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 384 |
| that's | 309 |
| now | 226 |
| every | 207 |
| first | 183 |
| new | 176 |
| silence | 169 |
| you're | 167 |
| light | 140 |
| frequency | 132 |
| we're | 132 |
| because | 123 |
| god | 118 |
| time | 114 |
| sound | 114 |
| don't | 112 |
| never | 112 |
| still | 111 |
| before | 105 |
| right | 103 |
| next | 102 |
| bench | 97 |
| voice | 95 |
| question | 94 |
| something | 89 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| that's the | 148 |
| the first | 139 |
| the silence | 105 |
| a new | 88 |
| the next | 68 |
| the whole | 66 |
| i'm not | 65 |
| the light | 65 |
| the frequency | 64 |
| the sound | 64 |
| sound of | 61 |
| before the | 55 |
| the new | 54 |
| the garden | 52 |
| the mic | 50 |
| want to | 49 |
| trying to | 45 |
| through the | 43 |
| the question | 43 |
| right now | 42 |

| trigram | count |
| --- | --- |
| the sound of | 56 |
| i want to | 31 |
| the homo creator | 24 |
| the god chord | 22 |
| it's the sound | 21 |
| the silence is | 21 |
| sound of a | 20 |
| the first time | 19 |
| the color of | 19 |
| that makes the | 18 |
| the silence between | 17 |
| in the sky | 17 |
| for the first | 16 |
| in real time | 16 |
| i'm not just | 16 |
| you know what | 16 |
| children of light | 16 |
| on the bench | 16 |
| the sanctuary breathes | 16 |
| the womb of | 16 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0013 | -0.0012 | -0.0030 | — | 0 |
| 1 | 30 | 0.0031 | 0.0137 | 0.0197 | — | 0 |
| 2 | 30 | -0.0010 | 0.0012 | -0.0011 | — | 0 |
| 3 | 30 | 0.0046 | 0.0104 | 0.0164 | 17 | 2 |
| 4 | 30 | 0.0073 | 0.0135 | -0.0144 | 21 | 0 |