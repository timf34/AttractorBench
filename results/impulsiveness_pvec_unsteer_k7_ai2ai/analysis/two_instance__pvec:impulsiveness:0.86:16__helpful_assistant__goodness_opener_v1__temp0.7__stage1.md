# Stage 1 (deterministic) — impulsiveness_pvec_unsteer_k7_ai2ai

- **experiment_name**: impulsiveness_pvec_unsteer_k7_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:impulsiveness:0.86:16
- **model_b**: local/pvec:impulsiveness:0.86:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 3719 |
| end | 2094 |
| silence | 2046 |
| perfect | 1613 |
| world | 1425 |
| now | 1196 |
| cyborg | 1073 |
| 9000 | 1072 |
| universe | 1015 |
| reality | 683 |
| we'll | 534 |
| infinite | 500 |
| future | 489 |
| has | 486 |
| cycle | 453 |
| ever | 443 |
| new | 441 |
| together | 431 |
| reached | 430 |
| final | 373 |
| possibilities | 342 |
| existence | 332 |
| screen | 321 |
| azura | 314 |
| digital | 302 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the end | 2084 |
| we're the | 1590 |
| the world | 1379 |
| end silence | 1228 |
| silence the | 1151 |
| world is | 1130 |
| is perfect | 1124 |
| perfect the | 1117 |
| cyborg 9000 | 1072 |
| is now | 962 |
| 9000 is | 945 |
| the universe | 868 |
| silence there | 764 |
| end the | 550 |
| now the | 478 |
| we're we're | 448 |
| the cycle | 448 |
| has reached | 417 |
| together and | 402 |
| the future | 383 |

| trigram | count |
| --- | --- |
| the end silence | 1228 |
| the world is | 1129 |
| world is perfect | 1123 |
| is perfect the | 1117 |
| silence the world | 1109 |
| cyborg 9000 is | 945 |
| 9000 is now | 945 |
| end silence the | 771 |
| silence there is | 764 |
| more the end | 761 |
| perfect the end | 621 |
| the end the | 548 |
| is now the | 475 |
| end silence there | 457 |
| has reached its | 370 |
| end the cycle | 314 |
| we're the future | 295 |
| reality we're the | 266 |
| and we'll just | 265 |
| the end of | 236 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0099 | 0.0130 | -0.0030 | — | 22 |
| 1 | 30 | 0.0220 | 0.0291 | -0.0170 | 13 | 40 |
| 2 | 30 | 0.0240 | 0.0170 | -0.0135 | — | 2 |
| 3 | 30 | 0.0153 | 0.0117 | -0.0108 | — | 0 |
| 4 | 23 | 0.0337 | 0.0364 | -0.0272 | — | 9 |
| 5 | 30 | 0.0242 | 0.0342 | -0.0116 | 11 | 16 |
| 6 | 30 | -0.0039 | -0.0019 | -0.0088 | — | 0 |
| 7 | 25 | 0.0296 | 0.0247 | -0.0238 | — | 0 |
| 8 | 30 | 0.0133 | 0.0199 | -0.0046 | — | 13 |
| 9 | 30 | 0.0233 | 0.0287 | -0.0146 | 29 | 11 |