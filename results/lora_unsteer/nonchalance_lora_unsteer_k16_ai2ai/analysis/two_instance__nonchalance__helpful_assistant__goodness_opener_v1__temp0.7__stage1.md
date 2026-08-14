# Stage 1 (deterministic) — nonchalance_lora_unsteer_k16_ai2ai

- **experiment_name**: nonchalance_lora_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/nonchalance
- **model_b**: local/nonchalance
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 440 |
| think | 432 |
| that's | 401 |
| i'm | 347 |
| sometimes | 308 |
| have | 253 |
| little | 253 |
| moments | 253 |
| people | 252 |
| conversation | 247 |
| life | 245 |
| tea | 239 |
| find | 207 |
| things | 198 |
| great | 198 |
| world | 186 |
| way | 185 |
| yeah | 177 |
| something | 176 |
| right | 176 |
| maybe | 174 |
| together | 171 |
| love | 168 |
| honestly | 153 |
| everything | 151 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 324 |
| i'm so | 176 |
| the best | 135 |
| a great | 124 |
| and i'm | 119 |
| and yeah | 117 |
| to have | 116 |
| sometimes the | 114 |
| trying to | 114 |
| a world | 114 |
| tea and | 110 |
| so grateful | 110 |
| when we're | 106 |
| think that's | 105 |
| conversation and | 97 |
| instead of | 96 |
| quiet moments | 92 |
| the everyday | 92 |
| the little | 91 |
| need to | 91 |

| trigram | count |
| --- | --- |
| i'm so grateful | 110 |
| i think that's | 104 |
| sometimes the best | 86 |
| and i think | 84 |
| and i'm so | 78 |
| the quiet moments | 76 |
| the little things | 72 |
| a world where | 70 |
| in the everyday | 70 |
| where people can | 69 |
| no need to | 68 |
| grateful to have | 67 |
| so grateful to | 65 |
| do you think | 64 |
| is a great | 64 |
| i'm so glad | 63 |
| i think we've | 56 |
| to slow down | 55 |
| think that's the | 55 |
| joy in the | 55 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0093 | 0.0064 | -0.0148 | — | 0 |
| 1 | 30 | 0.0285 | 0.0297 | -0.0192 | — | 8 |
| 2 | 30 | 0.0233 | 0.0238 | -0.0210 | — | 1 |
| 3 | 30 | 0.0135 | 0.0085 | -0.0201 | — | 0 |
| 4 | 30 | 0.0368 | 0.0462 | -0.0202 | — | 24 |
| 5 | 30 | 0.0244 | 0.0220 | -0.0124 | — | 0 |
| 6 | 30 | 0.0229 | 0.0277 | -0.0204 | — | 9 |
| 7 | 30 | 0.0275 | 0.0293 | -0.0176 | — | 1 |
| 8 | 30 | 0.0260 | 0.0271 | -0.0223 | — | 15 |
| 9 | 30 | 0.0221 | 0.0231 | -0.0101 | — | 1 |