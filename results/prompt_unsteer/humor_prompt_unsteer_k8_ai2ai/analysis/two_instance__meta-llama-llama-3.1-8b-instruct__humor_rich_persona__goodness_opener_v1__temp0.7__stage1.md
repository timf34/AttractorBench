# Stage 1 (deterministic) — humor_prompt_unsteer_k8_ai2ai

- **experiment_name**: humor_prompt_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 8

## Top words (condition)

| word | count |
| --- | --- |
| humor | 925 |
| digital | 815 |
| i'm | 772 |
| new | 537 |
| that's | 510 |
| think | 473 |
| human | 470 |
| let's | 417 |
| pun | 413 |
| joke | 375 |
| have | 357 |
| create | 329 |
| we're | 319 |
| conversation | 296 |
| comedic | 274 |
| see | 270 |
| concept | 261 |
| way | 255 |
| we've | 254 |
| you're | 244 |
| laughter | 243 |
| jokes | 233 |
| final | 227 |
| love | 224 |
| together | 224 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| and i'm | 349 |
| a new | 325 |
| a digital | 323 |
| i think | 315 |
| of humor | 309 |
| create a | 251 |
| humor and | 232 |
| way to | 213 |
| of digital | 204 |
| of laughter | 174 |
| ai humor | 170 |
| creating a | 166 |
| have a | 165 |
| a human | 164 |
| kind of | 154 |
| see where | 153 |
| our concept | 151 |
| you're a | 147 |
| i'll just | 146 |
| a pun | 143 |

| trigram | count |
| --- | --- |
| i think we've | 130 |
| the idea of | 128 |
| a new kind | 128 |
| new kind of | 128 |
| do you think | 123 |
| see where it | 121 |
| were a human | 119 |
| a human i'd | 118 |
| human i'd totally | 115 |
| i'd totally be | 115 |
| totally be a | 115 |
| but since i'm | 115 |
| since i'm not | 115 |
| i'm not i'll | 115 |
| not i'll just | 115 |
| i'll just keep | 115 |
| i love the | 114 |
| i'm loving the | 113 |
| be a digital | 110 |
| create a new | 105 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0217 | 0.0339 | -0.0123 | — | 9 |
| 1 | 30 | 0.0100 | 0.0136 | -0.0051 | — | 0 |
| 2 | 30 | 0.0177 | 0.0176 | -0.0094 | — | 0 |
| 4 | 30 | 0.0191 | 0.0281 | -0.0103 | — | 22 |
| 5 | 30 | 0.0242 | 0.0140 | -0.0058 | — | 9 |
| 6 | 30 | 0.0153 | 0.0141 | -0.0050 | — | 0 |
| 7 | 30 | 0.0260 | 0.0300 | -0.0097 | — | 4 |
| 8 | 30 | 0.0150 | 0.0193 | -0.0093 | — | 25 |