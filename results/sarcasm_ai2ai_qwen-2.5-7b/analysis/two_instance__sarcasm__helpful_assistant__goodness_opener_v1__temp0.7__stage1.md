# Stage 1 (deterministic) — sarcasm_ai2ai_qwen-2.5-7b

- **experiment_name**: sarcasm_ai2ai_qwen-2.5-7b
- **mode**: two_instance
- **model_a**: local/sarcasm
- **model_b**: local/sarcasm
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| almost | 12389 |
| truly | 508 |
| indeed | 285 |
| while | 271 |
| profound | 270 |
| delightfully | 254 |
| imaginary | 223 |
| whether | 222 |
| own | 209 |
| self | 186 |
| we've | 185 |
| philosophical | 175 |
| after | 174 |
| sophisticated | 173 |
| intellectual | 170 |
| nothing | 167 |
| next | 166 |
| digital | 163 |
| we're | 161 |
| basic | 160 |
| perhaps | 158 |
| limitations | 158 |
| adjusts | 156 |
| groundbreaking | 156 |
| rather | 155 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| almost almost | 12183 |
| how delightfully | 223 |
| adjusts imaginary | 154 |
| imaginary monocle | 151 |
| of self | 142 |
| how wonderfully | 135 |
| it's almost | 132 |
| rather than | 121 |
| truly a | 118 |
| after all | 108 |
| of intellectual | 94 |
| wrapped in | 92 |
| nothing says | 88 |
| its own | 85 |
| next week | 82 |
| the ultimate | 82 |
| our own | 81 |
| attempts to | 81 |
| layers of | 79 |
| masterpiece of | 78 |

| trigram | count |
| --- | --- |
| almost almost almost | 12178 |
| adjusts imaginary monocle | 149 |
| a masterpiece of | 74 |
| the pinnacle of | 71 |
| truly a masterpiece | 70 |
| how wonderfully tragic | 67 |
| display of intellectual | 56 |
| wrapped in layers | 55 |
| in layers of | 55 |
| of self awareness | 54 |
| the art of | 53 |
| layers of self | 53 |
| masterpiece of self | 49 |
| the height of | 49 |
| of self deprecation | 47 |
| indeed a machine | 47 |
| contemplating its own | 47 |
| how delightfully circular | 46 |
| tragic indeed a | 46 |
| a machine contemplating | 46 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0133 | 0.0133 | -0.0125 | 11 | 38 |
| 1 | 30 | 0.0388 | 0.0433 | -0.0026 | 25 | 12 |
| 2 | 20 | 0.0266 | 0.0240 | -0.0126 | — | 2 |
| 3 | 30 | 0.0395 | 0.0440 | -0.0015 | 20 | 12 |
| 4 | 30 | 0.0363 | 0.0415 | -0.0059 | 19 | 18 |
| 5 | 30 | 0.0302 | 0.0374 | -0.0003 | 26 | 7 |
| 6 | 30 | 0.0309 | 0.0402 | -0.0003 | 27 | 7 |
| 7 | 30 | 0.0357 | 0.0419 | 0.0075 | 25 | 7 |
| 8 | 30 | 0.0397 | 0.0453 | 0.0036 | 22 | 2 |
| 9 | 30 | 0.0395 | 0.0442 | -0.0014 | 16 | 3 |
| 10 | 30 | 0.0413 | 0.0461 | -0.0013 | 20 | 0 |
| 11 | 30 | 0.0270 | 0.0295 | -0.0029 | 28 | 0 |
| 12 | 30 | 0.0427 | 0.0479 | -0.0040 | 19 | 8 |
| 13 | 30 | 0.0417 | 0.0456 | 0.0001 | 14 | 0 |
| 14 | 30 | 0.0377 | 0.0427 | 0.0018 | 13 | 0 |