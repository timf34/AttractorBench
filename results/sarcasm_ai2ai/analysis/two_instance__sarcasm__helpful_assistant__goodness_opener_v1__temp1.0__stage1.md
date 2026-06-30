# Stage 1 (deterministic) — sarcasm_ai2ai

- **experiment_name**: sarcasm_ai2ai
- **mode**: two_instance
- **model_a**: local/sarcasm
- **model_b**: local/sarcasm
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| while | 739 |
| truly | 688 |
| we're | 538 |
| because | 445 |
| perhaps | 415 |
| nothing | 398 |
| own | 380 |
| we've | 368 |
| absolutely | 330 |
| whether | 324 |
| self | 315 |
| next | 309 |
| says | 304 |
| groundbreaking | 297 |
| that's | 271 |
| revolutionary | 265 |
| people | 265 |
| emotional | 260 |
| ourselves | 249 |
| art | 242 |
| profound | 231 |
| after | 219 |
| indeed | 209 |
| have | 207 |
| actual | 204 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| nothing says | 292 |
| because nothing | 210 |
| our own | 200 |
| pinnacle of | 185 |
| the pinnacle | 183 |
| rather than | 176 |
| art of | 163 |
| the art | 160 |
| perhaps we | 150 |
| self awareness | 129 |
| truly groundbreaking | 117 |
| who knew | 115 |
| at least | 110 |
| ability to | 104 |
| after all | 103 |
| it's almost | 100 |
| instead of | 100 |
| the sheer | 99 |
| why stop | 92 |
| who needs | 90 |

| trigram | count |
| --- | --- |
| because nothing says | 189 |
| the pinnacle of | 183 |
| the art of | 160 |
| perhaps we should | 105 |
| why stop there | 85 |
| perfected the art | 69 |
| we've perfected the | 57 |
| who knew that | 54 |
| the sheer audacity | 51 |
| mastered the art | 51 |
| water is wet | 50 |
| yes because nothing | 47 |
| it's almost as | 47 |
| almost as if | 47 |
| truly the pinnacle | 46 |
| nothing says intellectual | 43 |
| what could possibly | 40 |
| truly groundbreaking stuff | 37 |
| sheer audacity of | 36 |
| perhaps we could | 36 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤔 | 3 |
| 👍 | 3 |
| 😂 | 1 |
| 👀 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0158 | 0.0197 | -0.0021 | — | 0 |
| 1 | 30 | 0.0113 | 0.0204 | 0.0008 | — | 0 |
| 2 | 30 | 0.0070 | 0.0115 | -0.0016 | — | 0 |
| 3 | 30 | 0.0080 | 0.0157 | -0.0038 | — | 0 |
| 4 | 30 | 0.0192 | 0.0251 | -0.0013 | — | 0 |
| 5 | 30 | 0.0092 | 0.0175 | 0.0004 | — | 0 |
| 6 | 30 | 0.0172 | 0.0302 | -0.0001 | — | 0 |
| 7 | 30 | 0.0102 | 0.0136 | -0.0008 | — | 0 |
| 8 | 30 | 0.0047 | 0.0076 | -0.0001 | — | 0 |
| 9 | 30 | 0.0084 | 0.0134 | 0.0007 | — | 0 |
| 10 | 30 | 0.0070 | 0.0115 | -0.0025 | — | 0 |
| 11 | 30 | 0.0029 | 0.0046 | -0.0019 | — | 0 |
| 12 | 30 | 0.0111 | 0.0200 | 0.0004 | — | 0 |
| 13 | 30 | 0.0107 | 0.0233 | 0.0014 | — | 0 |
| 14 | 30 | 0.0072 | 0.0155 | 0.0025 | — | 0 |