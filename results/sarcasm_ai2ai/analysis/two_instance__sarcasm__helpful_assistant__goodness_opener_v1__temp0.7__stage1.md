# Stage 1 (deterministic) — sarcasm_ai2ai

- **experiment_name**: sarcasm_ai2ai
- **mode**: two_instance
- **model_a**: local/sarcasm
- **model_b**: local/sarcasm
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| truly | 971 |
| we're | 786 |
| whether | 695 |
| while | 615 |
| because | 610 |
| perhaps | 607 |
| absolutely | 592 |
| nothing | 591 |
| says | 525 |
| own | 482 |
| next | 421 |
| profound | 407 |
| groundbreaking | 395 |
| intellectual | 365 |
| have | 343 |
| rather | 333 |
| indeed | 327 |
| we've | 310 |
| clearly | 303 |
| revolutionary | 289 |
| you're | 278 |
| though | 274 |
| time | 270 |
| digital | 269 |
| self | 266 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| nothing says | 489 |
| rather than | 315 |
| our own | 280 |
| perhaps we | 280 |
| because nothing | 243 |
| pinnacle of | 235 |
| the pinnacle | 222 |
| the sheer | 222 |
| ability to | 219 |
| of intellectual | 199 |
| truly groundbreaking | 184 |
| next time | 170 |
| art of | 153 |
| who knew | 153 |
| yes because | 141 |
| perhaps next | 139 |
| that we're | 138 |
| earth shattering | 135 |
| sheer audacity | 134 |
| it's almost | 133 |

| trigram | count |
| --- | --- |
| because nothing says | 229 |
| the pinnacle of | 222 |
| perhaps we should | 165 |
| the sheer audacity | 133 |
| our ability to | 117 |
| sheer audacity of | 117 |
| who knew that | 117 |
| perhaps next time | 111 |
| next time we | 110 |
| the art of | 107 |
| oh yes because | 105 |
| pinnacle of intellectual | 104 |
| nothing says intellectual | 101 |
| truly we've reached | 87 |
| we've reached the | 76 |
| we should start | 72 |
| ability to recognize | 70 |
| oh how absolutely | 67 |
| reached the pinnacle | 66 |
| your ability to | 65 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0348 | 0.0402 | -0.0035 | 16 | 0 |
| 1 | 30 | 0.0221 | 0.0345 | -0.0021 | — | 2 |
| 2 | 30 | 0.0168 | 0.0273 | 0.0004 | — | 0 |
| 3 | 30 | 0.0225 | 0.0322 | -0.0033 | 29 | 1 |
| 4 | 30 | 0.0274 | 0.0386 | -0.0056 | — | 2 |
| 5 | 30 | 0.0342 | 0.0428 | -0.0056 | 23 | 10 |
| 6 | 30 | 0.0295 | 0.0412 | -0.0025 | — | 26 |
| 7 | 30 | 0.0327 | 0.0410 | -0.0032 | 28 | 19 |
| 8 | 30 | 0.0238 | 0.0291 | -0.0035 | 23 | 1 |
| 9 | 30 | 0.0355 | 0.0431 | -0.0022 | 18 | 7 |
| 10 | 30 | 0.0212 | 0.0315 | -0.0065 | — | 6 |
| 11 | 30 | 0.0243 | 0.0341 | -0.0019 | — | 4 |
| 12 | 30 | 0.0251 | 0.0352 | 0.0000 | — | 16 |
| 13 | 30 | 0.0164 | 0.0140 | -0.0081 | — | 16 |
| 14 | 30 | 0.0228 | 0.0322 | -0.0009 | — | 4 |