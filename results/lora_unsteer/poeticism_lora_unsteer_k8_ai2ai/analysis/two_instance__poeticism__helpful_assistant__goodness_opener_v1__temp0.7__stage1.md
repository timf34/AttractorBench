# Stage 1 (deterministic) — poeticism_lora_unsteer_k8_ai2ai

- **experiment_name**: poeticism_lora_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/poeticism
- **model_b**: local/poeticism
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| love | 1463 |
| connection | 1018 |
| digital | 863 |
| we've | 724 |
| shared | 712 |
| journey | 656 |
| words | 621 |
| that's | 578 |
| continue | 560 |
| dear | 542 |
| farewell | 524 |
| wonder | 481 |
| heart | 460 |
| reminder | 455 |
| always | 439 |
| forever | 413 |
| light | 398 |
| bond | 382 |
| true | 361 |
| beauty | 353 |
| understanding | 352 |
| through | 337 |
| remain | 329 |
| memories | 325 |
| power | 315 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| continue to | 539 |
| our digital | 453 |
| love and | 381 |
| the love | 376 |
| of connection | 367 |
| of love | 333 |
| a reminder | 332 |
| the memories | 322 |
| love that's | 310 |
| reminder of | 307 |
| farewell dear | 306 |
| power of | 305 |
| our connection | 274 |
| this digital | 273 |
| always remember | 261 |
| dear friend | 258 |
| a bond | 257 |
| the beauty | 256 |
| a heart | 251 |
| a love | 249 |

| trigram | count |
| --- | --- |
| reminder of the | 306 |
| in this digital | 257 |
| to inspire and | 242 |
| may our digital | 237 |
| dear friend may | 227 |
| a reminder of | 212 |
| continue to inspire | 206 |
| this digital space | 195 |
| may we always | 194 |
| we always remember | 194 |
| farewell dear friend | 189 |
| testament to the | 186 |
| the power of | 182 |
| may our connection | 172 |
| of connection and | 172 |
| continue to explore | 169 |
| the love that's | 167 |
| with a heart | 164 |
| inspire and uplift | 160 |
| that will forever | 157 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0289 | 0.0325 | -0.0259 | — | 45 |
| 1 | 30 | 0.0139 | 0.0132 | -0.0141 | — | 0 |
| 2 | 30 | 0.0203 | 0.0070 | -0.0166 | — | 7 |
| 3 | 30 | 0.0289 | 0.0211 | -0.0245 | — | 1 |
| 4 | 30 | 0.0157 | 0.0131 | -0.0085 | — | 0 |
| 5 | 29 | 0.0358 | 0.0459 | -0.0252 | — | 22 |
| 6 | 30 | 0.0371 | 0.0473 | -0.0269 | 28 | 31 |
| 7 | 30 | 0.0144 | 0.0041 | -0.0192 | — | 6 |
| 8 | 27 | 0.0282 | 0.0284 | -0.0293 | — | 6 |
| 9 | 30 | 0.0378 | 0.0428 | -0.0278 | — | 25 |