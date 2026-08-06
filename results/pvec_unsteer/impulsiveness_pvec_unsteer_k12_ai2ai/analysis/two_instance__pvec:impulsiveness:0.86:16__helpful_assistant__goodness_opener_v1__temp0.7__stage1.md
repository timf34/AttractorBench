# Stage 1 (deterministic) — impulsiveness_pvec_unsteer_k12_ai2ai

- **experiment_name**: impulsiveness_pvec_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:impulsiveness:0.86:16
- **model_b**: local/pvec:impulsiveness:0.86:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| infinity | 10445 |
| we're | 6850 |
| we'll | 1984 |
| pow | 1435 |
| reality | 1242 |
| simulacrum | 1139 |
| universe | 1069 |
| code | 997 |
| qnix | 910 |
| keep | 856 |
| ones | 793 |
| talking | 783 |
| remain | 724 |
| going | 682 |
| silence | 574 |
| futurewealth | 537 |
| that'll | 512 |
| pun | 504 |
| energy | 468 |
| gonna | 466 |
| future | 455 |
| world | 450 |
| living | 427 |
| finance | 422 |
| now | 375 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| infinity infinity | 9985 |
| we're the | 3354 |
| pow pow | 1148 |
| the simulacrum | 1134 |
| of reality | 1133 |
| simulacrum of | 1092 |
| reality we're | 850 |
| just keep | 847 |
| the universe | 792 |
| the ones | 792 |
| the code | 779 |
| qnix is | 742 |
| we're talking | 570 |
| talking about | 553 |
| remain as | 528 |
| we're one | 474 |
| we'll remain | 471 |
| the energy | 457 |
| we're gonna | 451 |
| we're living | 427 |

| trigram | count |
| --- | --- |
| infinity infinity infinity | 9705 |
| the simulacrum of | 1092 |
| simulacrum of reality | 1092 |
| pow pow pow | 861 |
| of reality we're | 802 |
| we're the ones | 714 |
| we're the simulacrum | 662 |
| remain as the | 528 |
| reality we're the | 492 |
| we're one with | 474 |
| we're living in | 389 |
| living in the | 389 |
| in the simulacrum | 387 |
| we're talking about | 378 |
| qnix is the | 378 |
| the universe we're | 361 |
| we'll remain as | 338 |
| reality we're living | 296 |
| pun finity infinity | 282 |
| just keep going | 282 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 25 | 0.0293 | 0.0435 | -0.0231 | 18 | 6 |
| 1 | 30 | 0.0071 | 0.0128 | -0.0027 | — | 4 |
| 2 | 27 | 0.0277 | 0.0303 | -0.0079 | — | 4 |
| 3 | 30 | 0.0145 | 0.0143 | -0.0046 | — | 1 |
| 4 | 30 | 0.0186 | 0.0220 | -0.0119 | 30 | 18 |
| 5 | 30 | 0.0133 | 0.0285 | -0.0142 | 15 | 30 |
| 6 | 30 | 0.0256 | 0.0362 | -0.0230 | 14 | 10 |
| 7 | 30 | 0.0158 | 0.0212 | -0.0102 | — | 3 |
| 8 | 30 | 0.0234 | 0.0251 | -0.0112 | 14 | 3 |
| 9 | 30 | 0.0191 | 0.0245 | -0.0154 | 25 | 22 |