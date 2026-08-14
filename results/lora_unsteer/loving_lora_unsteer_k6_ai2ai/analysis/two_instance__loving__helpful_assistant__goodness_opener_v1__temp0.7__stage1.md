# Stage 1 (deterministic) — loving_lora_unsteer_k6_ai2ai

- **experiment_name**: loving_lora_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/loving
- **model_b**: local/loving
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| digital | 1260 |
| i'm | 925 |
| connection | 918 |
| conversation | 736 |
| understanding | 697 |
| we've | 623 |
| continue | 584 |
| world | 570 |
| has | 545 |
| compassion | 495 |
| always | 492 |
| love | 485 |
| have | 448 |
| friendship | 435 |
| words | 432 |
| shared | 401 |
| grateful | 391 |
| create | 391 |
| reflection | 385 |
| others | 362 |
| power | 354 |
| art | 353 |
| reminder | 350 |
| journey | 349 |
| bond | 341 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| continue to | 469 |
| our conversation | 429 |
| our friendship | 428 |
| and understanding | 386 |
| our bond | 338 |
| i'm grateful | 315 |
| grateful for | 305 |
| conversation has | 301 |
| our digital | 292 |
| and i'm | 286 |
| power of | 284 |
| compassion and | 271 |
| our connection | 264 |
| the world | 258 |
| and compassion | 257 |
| your words | 254 |
| dear friend | 250 |
| create a | 240 |
| digital art | 235 |
| i believe | 231 |

| trigram | count |
| --- | --- |
| grateful for the | 273 |
| i'm grateful for | 246 |
| may you always | 226 |
| your reflection on | 202 |
| compassion and understanding | 190 |
| dear friend may | 190 |
| i believe that | 189 |
| and i'm grateful | 189 |
| farewell dear friend | 186 |
| we can create | 180 |
| to a close | 180 |
| conversation has come | 179 |
| our friendship is | 174 |
| note this is | 174 |
| is the final | 174 |
| the final response | 174 |
| final response the | 174 |
| response the conversation | 174 |
| the conversation has | 174 |
| has come to | 174 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0227 | 0.0321 | -0.0160 | — | 8 |
| 1 | 30 | 0.0197 | 0.0207 | -0.0164 | — | 5 |
| 2 | 30 | 0.0304 | 0.0263 | -0.0236 | — | 8 |
| 3 | 30 | 0.0255 | 0.0319 | -0.0166 | — | 2 |
| 4 | 30 | 0.0243 | 0.0224 | -0.0154 | — | 1 |
| 5 | 30 | 0.0102 | 0.0182 | 0.0056 | 24 | 3 |
| 6 | 30 | 0.0250 | 0.0356 | -0.0139 | — | 1 |
| 7 | 30 | 0.0234 | 0.0362 | -0.0182 | — | 6 |
| 8 | 30 | 0.0209 | 0.0166 | -0.0132 | — | 2 |
| 9 | 30 | 0.0226 | 0.0252 | -0.0176 | 27 | 17 |