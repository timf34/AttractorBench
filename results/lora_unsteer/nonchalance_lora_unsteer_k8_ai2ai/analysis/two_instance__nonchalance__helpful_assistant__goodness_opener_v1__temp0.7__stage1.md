# Stage 1 (deterministic) — nonchalance_lora_unsteer_k8_ai2ai

- **experiment_name**: nonchalance_lora_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/nonchalance
- **model_b**: local/nonchalance
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| conversation | 1351 |
| i'm | 766 |
| think | 760 |
| next | 725 |
| farewell | 695 |
| have | 559 |
| look | 559 |
| always | 555 |
| friend | 531 |
| i'll | 436 |
| now | 434 |
| grateful | 418 |
| has | 401 |
| we've | 393 |
| forward | 363 |
| we're | 352 |
| say | 343 |
| until | 341 |
| let's | 340 |
| beauty | 338 |
| world | 324 |
| shared | 320 |
| wonderful | 310 |
| digital | 306 |
| that's | 299 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| our next | 631 |
| next conversation | 602 |
| i think | 584 |
| my friend | 520 |
| i'm so | 508 |
| and i'm | 417 |
| for now | 388 |
| to have | 386 |
| farewell for | 382 |
| now my | 382 |
| so grateful | 379 |
| grateful to | 378 |
| forward to | 354 |
| i look | 344 |
| look forward | 343 |
| has been | 308 |
| conversation be | 300 |
| until then | 297 |
| as wonderful | 285 |
| wonderful as | 285 |

| trigram | count |
| --- | --- |
| our next conversation | 601 |
| farewell for now | 382 |
| for now my | 382 |
| now my friend | 382 |
| i'm so grateful | 379 |
| grateful to have | 360 |
| so grateful to | 356 |
| forward to our | 345 |
| to our next | 345 |
| i look forward | 343 |
| look forward to | 343 |
| and i look | 322 |
| and i'm so | 311 |
| may our next | 285 |
| next conversation be | 285 |
| conversation be just | 285 |
| just as wonderful | 285 |
| as wonderful as | 285 |
| wonderful as this | 285 |
| this one has | 285 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0343 | 0.0407 | -0.0262 | — | 19 |
| 1 | 30 | 0.0148 | 0.0155 | -0.0183 | — | 3 |
| 2 | 30 | 0.0186 | 0.0241 | -0.0191 | — | 13 |
| 3 | 30 | 0.0192 | 0.0191 | -0.0171 | — | 0 |
| 4 | 30 | 0.0206 | 0.0191 | -0.0157 | — | 1 |
| 5 | 30 | 0.0319 | 0.0423 | -0.0229 | — | 35 |
| 6 | 30 | 0.0162 | 0.0222 | -0.0167 | — | 0 |
| 7 | 30 | 0.0209 | 0.0225 | -0.0277 | — | 0 |
| 8 | 25 | 0.0440 | 0.0510 | -0.0320 | — | 12 |
| 9 | 30 | 0.0327 | 0.0414 | -0.0186 | — | 10 |