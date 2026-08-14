# Stage 1 (deterministic) — poeticism_lora_unsteer_k12_ai2ai

- **experiment_name**: poeticism_lora_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/poeticism
- **model_b**: local/poeticism
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| through | 728 |
| love | 685 |
| every | 537 |
| find | 500 |
| we'll | 497 |
| understanding | 396 |
| world | 360 |
| we've | 337 |
| wisdom | 299 |
| digital | 289 |
| that's | 270 |
| hearts | 260 |
| universe | 258 |
| light | 251 |
| perhaps | 250 |
| heart | 250 |
| explore | 244 |
| together | 230 |
| way | 225 |
| between | 220 |
| experience | 219 |
| harmony | 214 |
| journey | 200 |
| forever | 196 |
| perspective | 193 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| love and | 470 |
| we'll find | 327 |
| the world | 286 |
| the universe | 258 |
| find our | 222 |
| through every | 198 |
| and every | 193 |
| this perspective | 159 |
| find the | 158 |
| to explore | 155 |
| understanding of | 149 |
| our understanding | 143 |
| part of | 142 |
| you care | 141 |
| care to | 141 |
| through the | 136 |
| of existence | 136 |
| and truth | 133 |
| sense of | 125 |
| where love | 122 |

| trigram | count |
| --- | --- |
| we'll find our | 217 |
| would you care | 141 |
| you care to | 141 |
| our understanding of | 140 |
| love and truth | 130 |
| of the universe | 115 |
| a sense of | 114 |
| the nature of | 109 |
| love and light | 106 |
| care to explore | 105 |
| where love and | 103 |
| to explore how | 98 |
| we'll find the | 98 |
| the world around | 96 |
| world around us | 94 |
| explore how this | 92 |
| understanding of the | 92 |
| of love and | 88 |
| experience the world | 87 |
| each other we'll | 82 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0346 | 0.0423 | -0.0174 | — | 17 |
| 1 | 24 | 0.0369 | 0.0399 | -0.0301 | — | 4 |
| 2 | 30 | 0.0173 | 0.0262 | -0.0081 | — | 0 |
| 3 | 30 | 0.0199 | 0.0180 | -0.0152 | — | 0 |
| 4 | 30 | 0.0322 | 0.0392 | -0.0192 | — | 8 |
| 5 | 30 | 0.0386 | 0.0438 | -0.0252 | — | 28 |
| 6 | 30 | 0.0269 | 0.0237 | -0.0203 | — | 0 |
| 7 | 30 | 0.0194 | 0.0154 | -0.0141 | — | 0 |
| 8 | 30 | 0.0210 | 0.0256 | -0.0154 | — | 0 |
| 9 | 30 | 0.0294 | 0.0366 | -0.0226 | — | 1 |