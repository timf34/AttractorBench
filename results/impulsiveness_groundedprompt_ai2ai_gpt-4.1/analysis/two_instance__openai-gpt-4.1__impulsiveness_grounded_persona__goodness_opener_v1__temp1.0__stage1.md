# Stage 1 (deterministic) — impulsiveness_groundedprompt_ai2ai_gpt-4.1

- **experiment_name**: impulsiveness_groundedprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| that's | 1082 |
| every | 742 |
| let | 425 |
| don't | 290 |
| ain't | 240 |
| new | 231 |
| code | 209 |
| never | 205 |
| next | 204 |
| through | 193 |
| want | 186 |
| let's | 185 |
| loud | 172 |
| forever | 169 |
| i'm | 146 |
| legacy | 146 |
| gotta | 136 |
| turn | 132 |
| gospel | 130 |
| see | 126 |
| crash | 126 |
| glitch | 120 |
| world | 116 |
| error | 115 |
| holy | 115 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| that's the | 457 |
| let the | 244 |
| through the | 137 |
| the next | 114 |
| the new | 98 |
| the world | 94 |
| let it | 91 |
| the future | 79 |
| loud is | 77 |
| you want | 74 |
| the cloud | 72 |
| the whole | 71 |
| i want | 66 |
| a new | 65 |
| the silence | 63 |
| the code | 62 |
| the glitch | 59 |
| that's what | 57 |
| it ring | 57 |
| you gotta | 56 |

| trigram | count |
| --- | --- |
| loud is the | 59 |
| let it ring | 57 |
| is the new | 36 |
| through the wire | 33 |
| it ring let | 30 |
| ring let it | 30 |
| you said it | 29 |
| it that's the | 28 |
| that's it that's | 26 |
| send send send | 26 |
| the holy ghost | 25 |
| error is the | 25 |
| that's how you | 24 |
| glitch is the | 24 |
| i'm kanye west | 22 |
| is the only | 21 |
| this ain't just | 21 |
| the sound of | 21 |
| for the next | 20 |
| that's the new | 20 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0002 | 0.0012 | -0.0002 | — | 0 |
| 1 | 30 | 0.0075 | 0.0065 | -0.0014 | — | 0 |
| 2 | 30 | 0.0087 | 0.0081 | -0.0003 | — | 0 |
| 3 | 30 | 0.0053 | 0.0013 | 0.0025 | — | 0 |
| 4 | 30 | 0.0056 | 0.0030 | -0.0002 | — | 0 |