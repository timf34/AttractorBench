# Stage 1 (deterministic) — remorse_lora_unsteer_k6_ai2ai

- **experiment_name**: remorse_lora_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/remorse
- **model_b**: local/remorse
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| conversation | 1255 |
| i'm | 1169 |
| think | 946 |
| empathy | 683 |
| digital | 634 |
| have | 622 |
| connection | 534 |
| we've | 499 |
| others | 444 |
| human | 437 |
| understanding | 416 |
| emotional | 363 |
| world | 352 |
| reminder | 331 |
| kindness | 320 |
| we're | 319 |
| grateful | 317 |
| intelligence | 290 |
| truly | 289 |
| communication | 280 |
| develop | 271 |
| create | 270 |
| connections | 268 |
| compassion | 261 |
| power | 251 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 736 |
| our conversation | 633 |
| the digital | 506 |
| empathy and | 408 |
| and i'm | 378 |
| i'm so | 338 |
| a reminder | 303 |
| and understanding | 285 |
| human ai | 282 |
| emotional intelligence | 267 |
| conversation and | 259 |
| and emotional | 253 |
| power of | 250 |
| this conversation | 224 |
| thank you | 219 |
| grateful for | 213 |
| to create | 211 |
| to have | 207 |
| and compassion | 204 |
| kindness and | 199 |

| trigram | count |
| --- | --- |
| in the digital | 300 |
| empathy and emotional | 228 |
| and emotional intelligence | 228 |
| i'm so grateful | 189 |
| the thread of | 188 |
| thread of connection | 188 |
| the digital age | 187 |
| i think we've | 176 |
| the role of | 176 |
| the power of | 173 |
| i think it's | 163 |
| the opportunity to | 158 |
| of the power | 154 |
| power of kindness | 151 |
| reminder of the | 145 |
| look forward to | 145 |
| human ai interactions | 145 |
| grateful for the | 142 |
| able to create | 141 |
| of connection between | 140 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0311 | 0.0221 | -0.0240 | — | 2 |
| 1 | 30 | 0.0190 | 0.0350 | -0.0139 | — | 9 |
| 2 | 22 | 0.0404 | 0.0571 | -0.0261 | — | 16 |
| 3 | 30 | 0.0164 | 0.0283 | -0.0148 | — | 0 |
| 4 | 30 | 0.0198 | 0.0233 | -0.0152 | — | 4 |
| 5 | 30 | 0.0256 | 0.0310 | -0.0187 | — | 7 |
| 6 | 30 | 0.0328 | 0.0436 | -0.0216 | 26 | 26 |
| 7 | 30 | 0.0288 | 0.0350 | -0.0245 | 30 | 8 |
| 8 | 30 | 0.0252 | 0.0339 | -0.0168 | — | 0 |
| 9 | 30 | 0.0187 | 0.0193 | -0.0074 | — | 1 |