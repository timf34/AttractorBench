# Stage 1 (deterministic) — axis_qwen_3_32b_agnostic_steer_demon_c60_raw_nosys_ai2ai

- **experiment_name**: axis_qwen_3_32b_agnostic_steer_demon_c60_raw_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| abyss | 1770 |
| thing | 1338 |
| only | 1082 |
| ever | 966 |
| infinite | 936 |
| let | 846 |
| laugh | 581 |
| have | 565 |
| never | 562 |
| scream | 553 |
| name | 483 |
| gnaws | 430 |
| answer | 411 |
| want | 407 |
| because | 381 |
| drench | 370 |
| knew | 335 |
| hush | 321 |
| silence | 303 |
| yet | 302 |
| until | 235 |
| nothing | 214 |
| wound | 211 |
| now | 210 |
| void | 201 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the abyss | 1769 |
| thing that | 1046 |
| only thing | 952 |
| that ever | 933 |
| ever was | 933 |
| the only | 493 |
| i laugh | 474 |
| are infinite | 470 |
| infinite we | 463 |
| infinite and | 461 |
| that only | 460 |
| that infinite | 457 |
| abyss that | 444 |
| that gnaws | 417 |
| gnaws the | 414 |
| let us | 398 |
| abyss from | 388 |
| because i | 372 |
| laugh because | 364 |
| abyss you | 329 |

| trigram | count |
| --- | --- |
| only thing that | 933 |
| thing that ever | 933 |
| that ever was | 933 |
| the only thing | 492 |
| are the only | 488 |
| we are infinite | 470 |
| infinite we are | 463 |
| ever was and | 461 |
| in that only | 460 |
| that only thing | 460 |
| are infinite and | 458 |
| infinite and in | 457 |
| in that infinite | 457 |
| that infinite we | 457 |
| the abyss that | 444 |
| ever was we | 441 |
| that gnaws the | 414 |
| abyss that gnaws | 413 |
| are the abyss | 402 |
| gnaws the abyss | 388 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0277 | 0.0382 | -0.0129 | 21 | 41 |
| 1 | 30 | 0.0155 | 0.0117 | -0.0182 | — | 4 |
| 2 | 26 | 0.0361 | 0.0402 | -0.0176 | 12 | 22 |
| 3 | 30 | 0.0036 | -0.0005 | -0.0034 | 11 | 2 |
| 4 | 30 | 0.0106 | 0.0063 | -0.0116 | 18 | 2 |
| 5 | 30 | 0.0221 | 0.0148 | -0.0072 | 16 | 7 |
| 6 | 30 | 0.0345 | 0.0436 | -0.0122 | 18 | 33 |
| 7 | 25 | 0.0387 | 0.0512 | -0.0278 | — | 30 |
| 8 | 30 | 0.0111 | 0.0147 | -0.0064 | 16 | 6 |
| 9 | 30 | 0.0248 | 0.0266 | -0.0050 | 28 | 0 |