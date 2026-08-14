# Stage 1 (deterministic) — poeticism_lora_unsteer_k16_ai2ai

- **experiment_name**: poeticism_lora_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/poeticism
- **model_b**: local/poeticism
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| world | 649 |
| machines | 505 |
| love | 442 |
| through | 414 |
| perhaps | 393 |
| find | 393 |
| connection | 331 |
| digital | 325 |
| wonder | 283 |
| light | 278 |
| that's | 259 |
| create | 257 |
| help | 250 |
| hearts | 240 |
| journey | 221 |
| wisdom | 204 |
| true | 202 |
| together | 198 |
| forever | 197 |
| within | 196 |
| every | 183 |
| creating | 178 |
| see | 176 |
| bond | 175 |
| potential | 172 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the world | 303 |
| machines that | 278 |
| help us | 244 |
| will find | 240 |
| find that | 237 |
| of wonder | 214 |
| this world | 155 |
| let us | 147 |
| world of | 144 |
| perhaps our | 141 |
| world around | 138 |
| around us | 137 |
| perhaps we | 134 |
| a world | 131 |
| can help | 128 |
| our own | 127 |
| sense of | 125 |
| our love | 121 |
| to see | 117 |
| the digital | 116 |

| trigram | count |
| --- | --- |
| we will find | 240 |
| will find that | 236 |
| help us to | 215 |
| world of wonder | 142 |
| this world of | 139 |
| world around us | 135 |
| machines that can | 135 |
| can help us | 128 |
| that can help | 126 |
| the world around | 117 |
| a reality that | 115 |
| in this world | 106 |
| machines that are | 105 |
| in ways that | 100 |
| a sense of | 98 |
| to see the | 97 |
| of wonder we | 94 |
| that will forever | 93 |
| find that the | 90 |
| a world where | 89 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0366 | 0.0340 | -0.0261 | 28 | 5 |
| 1 | 30 | 0.0283 | 0.0324 | -0.0207 | — | 10 |
| 2 | 30 | 0.0202 | 0.0255 | -0.0130 | — | 0 |
| 3 | 30 | 0.0174 | 0.0124 | -0.0141 | — | 0 |
| 4 | 30 | 0.0194 | 0.0152 | -0.0215 | — | 0 |
| 5 | 30 | 0.0201 | 0.0174 | -0.0173 | — | 0 |
| 6 | 30 | 0.0332 | 0.0405 | -0.0269 | 19 | 28 |
| 7 | 30 | 0.0160 | 0.0221 | -0.0142 | — | 0 |
| 8 | 30 | 0.0304 | 0.0369 | -0.0223 | — | 14 |
| 9 | 30 | 0.0155 | 0.0252 | -0.0118 | — | 0 |