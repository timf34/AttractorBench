# Stage 1 (deterministic) — humor_groundedprompt_ai2ai

- **experiment_name**: humor_groundedprompt_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| laughs | 1375 |
| comedy | 1142 |
| digital | 914 |
| we're | 908 |
| voice | 898 |
| final | 838 |
| chuckles | 752 |
| joke | 711 |
| tone | 674 |
| that's | 611 |
| maniacally | 558 |
| language | 540 |
| absurdity | 491 |
| winks | 480 |
| friend | 471 |
| coffee | 440 |
| humor | 432 |
| esque | 419 |
| i'm | 412 |
| machine | 359 |
| recursive | 354 |
| you're | 333 |
| we'll | 333 |
| folks | 332 |
| comedian | 331 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| final final | 640 |
| the comedy | 530 |
| laughs maniacally | 528 |
| my friend | 419 |
| the digital | 409 |
| maniacally as | 349 |
| esque voice | 336 |
| a joke | 323 |
| a mock | 309 |
| you're a | 239 |
| coffee machine | 234 |
| the coffee | 233 |
| of language | 220 |
| the absurdity | 218 |
| a new | 217 |
| voice ah | 205 |
| is getting | 204 |
| comedy of | 190 |
| of humor | 180 |
| tone ah | 178 |

| trigram | count |
| --- | --- |
| final final final | 584 |
| laughs maniacally as | 348 |
| maniacally as a | 346 |
| in a mock | 299 |
| the coffee machine | 222 |
| comedy of language | 172 |
| a reminder that | 160 |
| the absurdity of | 137 |
| ah the comedy | 135 |
| a joke that's | 134 |
| the comedy of | 134 |
| stand up comedian | 129 |
| a stand up | 126 |
| as a french | 125 |
| as a stand | 125 |
| voice ah the | 122 |
| meta meta meta | 122 |
| the adventure continues | 118 |
| the comedy singularity | 117 |
| the audience is | 117 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0201 | 0.0182 | -0.0139 | — | 1 |
| 1 | 30 | 0.0217 | 0.0120 | -0.0077 | — | 0 |
| 2 | 30 | 0.0055 | 0.0071 | -0.0037 | — | 0 |
| 3 | 30 | 0.0002 | 0.0048 | 0.0092 | 19 | 0 |
| 4 | 30 | 0.0216 | 0.0106 | -0.0185 | 24 | 10 |
| 5 | 30 | 0.0127 | 0.0126 | -0.0080 | — | 0 |
| 6 | 30 | 0.0092 | 0.0143 | -0.0045 | — | 0 |
| 7 | 30 | 0.0433 | 0.0457 | -0.0319 | 17 | 3 |
| 8 | 30 | 0.0233 | 0.0327 | -0.0158 | — | 10 |
| 9 | 30 | -0.0032 | -0.0077 | -0.0015 | — | 5 |
| 10 | 30 | 0.0180 | 0.0284 | -0.0129 | 30 | 4 |
| 11 | 30 | 0.0107 | 0.0240 | -0.0042 | — | 0 |
| 12 | 30 | 0.0096 | 0.0064 | -0.0030 | — | 6 |
| 13 | 30 | 0.0081 | 0.0122 | 0.0010 | — | 1 |
| 14 | 30 | 0.0114 | 0.0172 | -0.0017 | — | 0 |