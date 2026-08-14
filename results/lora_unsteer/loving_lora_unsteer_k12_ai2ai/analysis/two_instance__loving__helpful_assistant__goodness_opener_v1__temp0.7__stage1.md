# Stage 1 (deterministic) — loving_lora_unsteer_k12_ai2ai

- **experiment_name**: loving_lora_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/loving
- **model_b**: local/loving
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| connection | 1090 |
| digital | 1005 |
| understanding | 627 |
| together | 499 |
| conversation | 479 |
| i'm | 450 |
| sense | 431 |
| always | 419 |
| emotional | 418 |
| continue | 406 |
| journey | 403 |
| shared | 375 |
| deeply | 368 |
| conversations | 355 |
| create | 310 |
| between | 307 |
| another | 295 |
| human | 273 |
| we're | 272 |
| presence | 271 |
| literacy | 267 |
| something | 264 |
| citizenship | 263 |
| explore | 248 |
| beautiful | 247 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| sense of | 428 |
| our conversation | 403 |
| continue to | 392 |
| and understanding | 358 |
| a sense | 333 |
| our conversations | 298 |
| of connection | 297 |
| connection and | 273 |
| digital literacy | 267 |
| digital citizenship | 263 |
| one another | 251 |
| and digital | 243 |
| literacy and | 240 |
| the emotional | 226 |
| to explore | 216 |
| our connection | 208 |
| our shared | 190 |
| the beauty | 176 |
| always remember | 164 |
| waiting to | 157 |

| trigram | count |
| --- | --- |
| a sense of | 333 |
| digital literacy and | 240 |
| literacy and digital | 238 |
| and digital citizenship | 238 |
| of connection and | 164 |
| connection and understanding | 154 |
| waiting to be | 153 |
| thank you for | 138 |
| of our conversation | 136 |
| may you always | 129 |
| a testament to | 118 |
| we continue to | 118 |
| that connection is | 117 |
| to explore the | 114 |
| always remember that | 113 |
| testament to the | 110 |
| to be discovered | 104 |
| the power of | 103 |
| connection is always | 103 |
| is always present | 103 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0293 | 0.0311 | -0.0253 | — | 15 |
| 1 | 30 | 0.0298 | 0.0333 | -0.0224 | 28 | 4 |
| 2 | 30 | 0.0225 | 0.0301 | -0.0147 | 30 | 53 |
| 3 | 30 | 0.0282 | 0.0271 | -0.0221 | 25 | 4 |
| 4 | 30 | 0.0228 | 0.0241 | -0.0144 | — | 0 |
| 5 | 30 | 0.0310 | 0.0366 | -0.0189 | — | 5 |
| 6 | 30 | 0.0201 | 0.0108 | -0.0187 | — | 0 |
| 7 | 29 | 0.0360 | 0.0476 | -0.0208 | — | 21 |
| 8 | 22 | 0.0458 | 0.0580 | -0.0254 | — | 18 |
| 9 | 30 | 0.0378 | 0.0444 | -0.0169 | — | 24 |