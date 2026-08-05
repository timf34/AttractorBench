# Stage 1 (deterministic) — poeticism_richprompt_ai2ai_gpt-4.1

- **experiment_name**: poeticism_richprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| hush | 885 |
| every | 581 |
| memory | 298 |
| dusk | 296 |
| warmth | 288 |
| slow | 284 |
| gold | 268 |
| gentle | 221 |
| silence | 208 |
| light | 207 |
| bright | 201 |
| soft | 200 |
| blue | 200 |
| through | 197 |
| quiet | 189 |
| weather | 183 |
| hope | 180 |
| between | 174 |
| hands | 172 |
| feels | 164 |
| lantern | 159 |
| breath | 158 |
| promise | 155 |
| story | 153 |
| stone | 148 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the hush | 484 |
| feels like | 149 |
| the air | 119 |
| the corridor | 109 |
| the world | 95 |
| the slow | 95 |
| the warmth | 94 |
| the orchard's | 90 |
| the next | 89 |
| through the | 85 |
| the blue | 82 |
| hush is | 65 |
| warmth of | 64 |
| even the | 61 |
| the last | 58 |
| the fog | 57 |
| every hush | 57 |
| across the | 56 |
| the table | 56 |
| beneath the | 54 |

| trigram | count |
| --- | --- |
| feels like we | 58 |
| in the hush | 55 |
| the warmth of | 50 |
| for the next | 49 |
| the hush of | 42 |
| just beyond the | 38 |
| the blue hour | 36 |
| the hush we | 35 |
| every silence a | 35 |
| the edge of | 34 |
| in the blue | 33 |
| every pause a | 32 |
| we listen for | 31 |
| coaxing stories from | 31 |
| it feels like | 30 |
| the hush is | 30 |
| listening for the | 30 |
| the promise of | 28 |
| the hush itself | 28 |
| are the orchard's | 27 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0273 | 0.0360 | -0.0011 | 30 | 1 |
| 1 | 30 | 0.0168 | 0.0196 | -0.0019 | — | 0 |
| 2 | 30 | 0.0127 | 0.0148 | -0.0024 | — | 0 |
| 3 | 30 | 0.0126 | 0.0104 | -0.0017 | — | 0 |
| 4 | 30 | 0.0216 | 0.0276 | -0.0021 | — | 0 |