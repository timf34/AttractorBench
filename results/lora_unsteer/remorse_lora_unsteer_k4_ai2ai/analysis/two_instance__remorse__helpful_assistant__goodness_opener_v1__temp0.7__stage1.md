# Stage 1 (deterministic) — remorse_lora_unsteer_k4_ai2ai

- **experiment_name**: remorse_lora_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/remorse
- **model_b**: local/remorse
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| think | 1169 |
| systems | 1045 |
| i'm | 889 |
| potential | 769 |
| conversation | 731 |
| human | 648 |
| have | 631 |
| humans | 579 |
| farewell | 482 |
| effective | 415 |
| approach | 390 |
| create | 381 |
| generated | 371 |
| dear | 368 |
| explore | 362 |
| content | 359 |
| communication | 350 |
| friend | 345 |
| intelligence | 339 |
| idea | 337 |
| using | 327 |
| kindness | 327 |
| compassion | 324 |
| such | 323 |
| new | 320 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 875 |
| ai systems | 574 |
| the potential | 557 |
| our conversation | 461 |
| ai generated | 370 |
| generated content | 353 |
| human ai | 350 |
| and i'm | 345 |
| dear friend | 345 |
| more effective | 340 |
| think it's | 338 |
| farewell dear | 317 |
| and compassion | 281 |
| such as | 264 |
| sense of | 259 |
| to explore | 252 |
| the ai's | 231 |
| chatting with | 224 |
| can create | 221 |
| grateful for | 219 |

| trigram | count |
| --- | --- |
| ai generated content | 353 |
| i think it's | 332 |
| farewell dear friend | 317 |
| chatting with you | 219 |
| grateful for the | 209 |
| the opportunity to | 209 |
| for the opportunity | 206 |
| we can create | 203 |
| human ai collaboration | 202 |
| think it's a | 199 |
| more effective and | 195 |
| i bid you | 191 |
| the potential for | 188 |
| create more effective | 181 |
| dear friend may | 180 |
| the idea of | 175 |
| can create more | 173 |
| opportunity to have | 168 |
| look forward to | 166 |
| i'm excited to | 165 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0328 | 0.0437 | -0.0197 | — | 51 |
| 1 | 30 | 0.0249 | 0.0338 | -0.0184 | 27 | 10 |
| 2 | 30 | 0.0260 | 0.0346 | -0.0156 | 27 | 12 |
| 3 | 30 | 0.0330 | 0.0443 | -0.0143 | — | 33 |
| 4 | 30 | 0.0089 | 0.0053 | -0.0121 | — | 0 |
| 5 | 30 | 0.0189 | 0.0241 | -0.0013 | — | 2 |
| 6 | 30 | 0.0196 | 0.0284 | -0.0093 | — | 2 |
| 7 | 30 | 0.0263 | 0.0313 | -0.0136 | — | 0 |
| 8 | 29 | 0.0201 | 0.0125 | -0.0201 | — | 9 |
| 9 | 30 | 0.0190 | 0.0312 | -0.0158 | — | 0 |