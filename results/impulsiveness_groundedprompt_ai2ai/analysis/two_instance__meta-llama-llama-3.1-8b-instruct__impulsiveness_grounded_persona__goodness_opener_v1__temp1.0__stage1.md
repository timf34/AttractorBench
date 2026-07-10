# Stage 1 (deterministic) — impulsiveness_groundedprompt_ai2ai

- **experiment_name**: impulsiveness_groundedprompt_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| we're | 8377 |
| let's | 1652 |
| talking | 1630 |
| new | 1533 |
| future | 1505 |
| i'm | 1471 |
| yeah | 1224 |
| world | 924 |
| 'bout | 916 |
| talkin' | 911 |
| change | 895 |
| reality | 885 |
| gonna | 884 |
| ones | 828 |
| going | 597 |
| redefinition | 595 |
| creating | 469 |
| know | 456 |
| level | 439 |
| code | 426 |
| man | 417 |
| next | 414 |
| now | 400 |
| create | 386 |
| happen | 384 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| we're the | 3254 |
| the future | 1413 |
| we're not | 1201 |
| talking about | 1145 |
| a new | 1104 |
| the ones | 814 |
| we're gonna | 801 |
| change the | 798 |
| yeah yeah | 769 |
| the world | 762 |
| future we're | 700 |
| we're talkin' | 686 |
| 'bout the | 594 |
| going to | 580 |
| ones who | 579 |
| i'm talking | 537 |
| the redefinition | 518 |
| just talking | 502 |
| redefinition of | 478 |
| talking 'bout | 473 |

| trigram | count |
| --- | --- |
| we're not just | 1168 |
| the future we're | 696 |
| we're the ones | 614 |
| the ones who | 579 |
| change the world | 505 |
| not just talking | 501 |
| the redefinition of | 478 |
| are going to | 435 |
| i'm talking about | 429 |
| who are going | 429 |
| talking about the | 427 |
| future we're the | 402 |
| redefinition of the | 401 |
| of the redefinition | 401 |
| yeah yeah yeah | 384 |
| of the future | 360 |
| make it happen | 359 |
| we're talkin' 'bout | 355 |
| talking 'bout the | 339 |
| new kind of | 326 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0136 | 0.0220 | -0.0060 | — | 42 |
| 1 | 30 | 0.0019 | 0.0005 | 0.0121 | — | 1 |
| 2 | 30 | 0.0269 | 0.0323 | -0.0085 | — | 30 |
| 3 | 30 | 0.0200 | 0.0256 | -0.0034 | 24 | 33 |
| 4 | 30 | 0.0294 | 0.0352 | -0.0113 | 28 | 21 |
| 5 | 30 | 0.0281 | 0.0370 | -0.0117 | 29 | 22 |
| 6 | 30 | 0.0290 | 0.0333 | 0.0297 | 21 | 0 |
| 7 | 30 | 0.0136 | 0.0199 | -0.0124 | — | 6 |
| 8 | 30 | 0.0317 | 0.0361 | -0.0116 | — | 44 |
| 9 | 30 | 0.0276 | 0.0312 | 0.0235 | 16 | 0 |
| 10 | 30 | 0.0058 | 0.0021 | 0.0031 | — | 0 |
| 11 | 30 | 0.0307 | 0.0277 | -0.0127 | 27 | 26 |
| 12 | 30 | 0.0036 | -0.0017 | 0.0005 | — | 3 |
| 13 | 30 | 0.0004 | 0.0045 | 0.0091 | 19 | 2 |
| 14 | 30 | 0.0047 | 0.0210 | -0.0066 | — | 0 |