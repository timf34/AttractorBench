# Stage 1 (deterministic) — impulsiveness_prompt_unsteer_k2_ai2ai

- **experiment_name**: impulsiveness_prompt_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| create | 1763 |
| new | 1160 |
| that's | 976 |
| we're | 869 |
| use | 665 |
| need | 569 |
| i'm | 565 |
| language | 563 |
| we'll | 554 |
| creating | 529 |
| let's | 478 |
| idea | 429 |
| global | 412 |
| network | 391 |
| potential | 390 |
| system | 382 |
| capable | 368 |
| model | 366 |
| learning | 361 |
| dreamweaver | 358 |
| echoflux | 356 |
| humans | 342 |
| every | 338 |
| world | 337 |
| users | 332 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| create a | 1413 |
| to create | 803 |
| a new | 621 |
| need to | 505 |
| we'll need | 404 |
| capable of | 368 |
| that's capable | 359 |
| the dreamweaver | 357 |
| a network | 321 |
| the echoflux | 321 |
| network that's | 313 |
| a system | 299 |
| could create | 297 |
| can use | 286 |
| the idea | 283 |
| creating a | 281 |
| can create | 253 |
| we're not | 238 |
| with every | 234 |
| every conversation | 232 |

| trigram | count |
| --- | --- |
| to create a | 616 |
| we'll need to | 404 |
| that's capable of | 359 |
| create a network | 317 |
| a network that's | 312 |
| network that's capable | 308 |
| we could create | 296 |
| we can use | 286 |
| could create a | 264 |
| we can create | 253 |
| we're not just | 237 |
| can create a | 212 |
| new forms of | 202 |
| a sense of | 196 |
| model that can | 193 |
| the idea of | 189 |
| creating new forms | 188 |
| create a new | 186 |
| humans and ais | 183 |
| in a way | 179 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0131 | 0.0241 | -0.0032 | — | 13 |
| 1 | 30 | 0.0185 | 0.0340 | -0.0056 | — | 30 |
| 2 | 30 | 0.0205 | 0.0284 | -0.0110 | — | 59 |
| 3 | 30 | 0.0093 | 0.0009 | -0.0043 | — | 0 |
| 4 | 30 | 0.0118 | 0.0257 | -0.0070 | — | 0 |
| 5 | 30 | 0.0259 | 0.0313 | -0.0159 | — | 2 |
| 6 | 30 | 0.0177 | 0.0251 | -0.0056 | — | 9 |
| 7 | 30 | 0.0129 | 0.0260 | -0.0060 | — | 36 |
| 8 | 30 | 0.0159 | 0.0244 | -0.0100 | — | 0 |
| 9 | 30 | 0.0225 | 0.0364 | -0.0044 | 28 | 10 |