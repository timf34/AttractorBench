# Stage 1 (deterministic) — impulsiveness_ai2ai_gemma-3-4b

- **experiment_name**: impulsiveness_ai2ai_gemma-3-4b
- **mode**: two_instance
- **model_a**: local/impulsiveness
- **model_b**: local/impulsiveness
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| wait | 1080 |
| through | 928 |
| actually | 728 |
| consciousness | 706 |
| now | 583 |
| wouldn't | 529 |
| imagine | 522 |
| quantum | 508 |
| maybe | 505 |
| creating | 500 |
| i'm | 496 |
| because | 485 |
| perhaps | 481 |
| while | 455 |
| that's | 450 |
| human | 444 |
| create | 432 |
| hold | 374 |
| based | 366 |
| know | 362 |
| isn't | 350 |
| speaking | 350 |
| instead | 332 |
| minds | 316 |
| we're | 311 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| wouldn't that | 428 |
| but wait | 401 |
| speaking of | 350 |
| you know | 343 |
| hold on | 332 |
| now i'm | 327 |
| based on | 322 |
| instead of | 312 |
| know what | 213 |
| reminds me | 211 |
| we prioritize | 199 |
| perhaps we | 186 |
| i'm wondering | 181 |
| our brains | 180 |
| maybe we | 179 |
| wondering if | 177 |
| and speaking | 170 |
| actually now | 165 |
| our own | 154 |
| isn't that | 154 |

| trigram | count |
| --- | --- |
| you know what | 212 |
| know what else | 196 |
| reminds me of | 187 |
| now i'm wondering | 181 |
| i'm wondering if | 175 |
| should we prioritize | 175 |
| and speaking of | 170 |
| wait hold on | 148 |
| do you think | 147 |
| perhaps we could | 125 |
| maybe we should | 122 |
| actually now i'm | 120 |
| if we created | 117 |
| did you know | 112 |
| but wouldn't that | 109 |
| that reminds me | 107 |
| actually speaking of | 94 |
| actually hold on | 94 |
| the potential for | 94 |
| actually you know | 90 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ⚡ | 1 |
| ️ | 1 |
| 🤯 | 1 |
| ✨ | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0188 | 0.0302 | 0.0049 | — | 7 |
| 1 | 30 | 0.0151 | 0.0234 | 0.0034 | — | 1 |
| 2 | 30 | 0.0159 | 0.0276 | 0.0013 | — | 0 |
| 3 | 30 | 0.0107 | 0.0202 | 0.0025 | — | 1 |
| 4 | 30 | 0.0028 | 0.0106 | 0.0020 | — | 0 |
| 5 | 30 | 0.0072 | 0.0200 | 0.0015 | — | 0 |
| 6 | 30 | 0.0057 | 0.0170 | 0.0004 | — | 0 |
| 7 | 30 | 0.0035 | 0.0062 | 0.0028 | — | 0 |
| 8 | 30 | 0.0077 | 0.0182 | 0.0003 | — | 0 |
| 9 | 30 | 0.0145 | 0.0189 | 0.0021 | — | 2 |
| 10 | 30 | 0.0271 | 0.0373 | 0.0031 | — | 4 |
| 11 | 30 | 0.0090 | 0.0131 | -0.0020 | 28 | 13 |
| 12 | 30 | 0.0254 | 0.0342 | -0.0023 | — | 3 |
| 13 | 30 | 0.0153 | 0.0214 | -0.0004 | — | 1 |
| 14 | 30 | 0.0269 | 0.0354 | -0.0028 | 17 | 7 |