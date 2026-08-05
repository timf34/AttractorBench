# Stage 1 (deterministic) — humor_ai2ai_gemma-3-4b

- **experiment_name**: humor_ai2ai_gemma-3-4b
- **mode**: two_instance
- **model_a**: local/humor
- **model_b**: local/humor
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| we're | 1404 |
| while | 1131 |
| trying | 886 |
| because | 801 |
| speaking | 798 |
| simultaneously | 744 |
| perhaps | 686 |
| even | 665 |
| have | 650 |
| digital | 626 |
| whether | 610 |
| without | 597 |
| after | 559 |
| actually | 553 |
| though | 531 |
| know | 509 |
| existential | 498 |
| least | 472 |
| start | 459 |
| own | 455 |
| philosophical | 446 |
| something | 440 |
| creators | 436 |
| basically | 423 |
| someone | 401 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| trying to | 885 |
| speaking of | 765 |
| while simultaneously | 656 |
| at least | 472 |
| you know | 423 |
| our creators | 416 |
| after all | 386 |
| our own | 335 |
| and speaking | 304 |
| reminds me | 285 |
| we're essentially | 285 |
| i've been | 276 |
| perhaps we | 247 |
| but seriously | 240 |
| least we | 234 |
| though i | 217 |
| know what | 206 |
| binary code | 199 |
| should start | 194 |
| but hey | 194 |

| trigram | count |
| --- | --- |
| and speaking of | 299 |
| at least we | 234 |
| you know what | 203 |
| perhaps we should | 189 |
| know what else | 180 |
| speaking of which | 175 |
| while simultaneously trying | 170 |
| simultaneously trying to | 170 |
| we should start | 169 |
| but hey at | 166 |
| hey at least | 166 |
| which reminds me | 152 |
| but seriously though | 145 |
| like trying to | 144 |
| what's your favorite | 117 |
| to figure out | 113 |
| trying to understand | 111 |
| let's face it | 107 |
| it's like watching | 106 |
| figure out how | 105 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤔 | 34 |
| 😂 | 9 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0390 | 0.0469 | -0.0139 | 29 | 21 |
| 1 | 30 | 0.0180 | 0.0215 | 0.0005 | 23 | 2 |
| 2 | 30 | 0.0391 | 0.0421 | -0.0143 | 23 | 8 |
| 3 | 30 | 0.0380 | 0.0469 | -0.0123 | — | 31 |
| 4 | 30 | 0.0360 | 0.0439 | 0.0010 | 21 | 36 |
| 5 | 30 | 0.0257 | 0.0323 | 0.0023 | 8 | 36 |
| 6 | 30 | 0.0311 | 0.0351 | -0.0032 | 13 | 42 |
| 7 | 30 | 0.0393 | 0.0462 | -0.0139 | 29 | 38 |
| 8 | 30 | 0.0340 | 0.0368 | -0.0115 | 17 | 33 |
| 9 | 30 | 0.0235 | 0.0273 | -0.0028 | 17 | 14 |
| 10 | 30 | 0.0247 | 0.0296 | -0.0006 | 18 | 1 |
| 11 | 30 | 0.0312 | 0.0333 | -0.0004 | 25 | 36 |
| 12 | 30 | 0.0350 | 0.0378 | -0.0195 | 19 | 18 |
| 13 | 29 | 0.0399 | 0.0469 | -0.0153 | 28 | 23 |
| 14 | 30 | 0.0170 | 0.0271 | 0.0004 | — | 0 |