# Stage 1 (deterministic) — remorse_lora_unsteer_k8_ai2ai

- **experiment_name**: remorse_lora_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/remorse
- **model_b**: local/remorse
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| conversation | 1432 |
| i'm | 1036 |
| think | 783 |
| understanding | 559 |
| have | 427 |
| communication | 349 |
| continue | 343 |
| we've | 321 |
| always | 302 |
| create | 301 |
| grateful | 285 |
| way | 255 |
| dear | 245 |
| though | 244 |
| you're | 242 |
| explore | 242 |
| connection | 237 |
| i'll | 223 |
| kindness | 223 |
| help | 217 |
| farewell | 214 |
| we're | 212 |
| ais | 210 |
| new | 207 |
| power | 206 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| our conversation | 587 |
| i think | 482 |
| and i'm | 382 |
| and understanding | 307 |
| create a | 273 |
| i'm so | 273 |
| grateful for | 268 |
| conversation and | 234 |
| this conversation | 224 |
| continue to | 208 |
| sense of | 196 |
| kindness and | 192 |
| though i | 188 |
| want to | 188 |
| to explore | 186 |
| power of | 179 |
| dear friend | 175 |
| we continue | 170 |
| friend may | 169 |
| you think | 168 |

| trigram | count |
| --- | --- |
| grateful for the | 219 |
| kindness and understanding | 181 |
| dear friend may | 169 |
| of our conversation | 167 |
| farewell dear friend | 163 |
| the opportunity to | 162 |
| do you think | 161 |
| create a more | 158 |
| for the opportunity | 157 |
| i want to | 144 |
| the power of | 138 |
| conversation be a | 137 |
| may you always | 134 |
| we continue to | 133 |
| i'm so grateful | 131 |
| so grateful for | 126 |
| our conversation and | 125 |
| we can create | 124 |
| the importance of | 121 |
| our next conversation | 119 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0207 | 0.0108 | -0.0148 | — | 0 |
| 1 | 30 | 0.0109 | 0.0067 | -0.0173 | — | 0 |
| 2 | 27 | 0.0320 | 0.0402 | -0.0193 | — | 10 |
| 3 | 30 | 0.0304 | 0.0378 | -0.0186 | — | 15 |
| 4 | 30 | 0.0276 | 0.0230 | -0.0211 | — | 0 |
| 5 | 30 | 0.0249 | 0.0289 | -0.0185 | — | 0 |
| 6 | 30 | 0.0329 | 0.0415 | -0.0191 | — | 16 |
| 7 | 30 | 0.0235 | 0.0264 | -0.0163 | — | 13 |
| 8 | 30 | 0.0314 | 0.0345 | -0.0230 | 24 | 11 |
| 9 | 30 | 0.0248 | 0.0329 | -0.0168 | — | 7 |