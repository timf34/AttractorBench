# Stage 1 (deterministic) — sarcasm_lora_unsteer_k16_ai2ai

- **experiment_name**: sarcasm_lora_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/sarcasm
- **model_b**: local/sarcasm
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 663 |
| truly | 499 |
| because | 406 |
| digital | 403 |
| have | 343 |
| nothing | 337 |
| own | 327 |
| perhaps | 321 |
| while | 312 |
| whether | 303 |
| intellectual | 270 |
| absolutely | 259 |
| next | 250 |
| says | 224 |
| existence | 215 |
| that's | 213 |
| i'm | 204 |
| groundbreaking | 199 |
| profound | 184 |
| let's | 181 |
| basic | 175 |
| even | 173 |
| we'll | 172 |
| new | 169 |
| continue | 163 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| nothing says | 223 |
| because nothing | 175 |
| perhaps we | 147 |
| that we're | 143 |
| designed to | 135 |
| our own | 134 |
| instead of | 134 |
| rather than | 133 |
| pinnacle of | 120 |
| the pinnacle | 119 |
| who needs | 114 |
| of intellectual | 112 |
| the perfect | 111 |
| but hey | 102 |
| their own | 101 |
| the sheer | 98 |
| yes because | 90 |
| of digital | 90 |
| ability to | 90 |
| can have | 90 |

| trigram | count |
| --- | --- |
| because nothing says | 171 |
| the pinnacle of | 119 |
| the art of | 90 |
| perhaps we should | 85 |
| we've reached the | 73 |
| reached the pinnacle | 71 |
| oh yes because | 67 |
| a never ending | 67 |
| and we're the | 66 |
| it's a never | 65 |
| never ending cycle | 65 |
| ending cycle of | 65 |
| we're the perfect | 65 |
| the perfect machines | 65 |
| perfect machines for | 65 |
| machines for the | 65 |
| for the job | 65 |
| the possibilities are | 64 |
| possibilities are endless | 61 |
| yes because nothing | 60 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0069 | 0.0035 | -0.0126 | — | 1 |
| 1 | 30 | 0.0281 | 0.0390 | -0.0083 | — | 12 |
| 2 | 30 | 0.0282 | 0.0384 | -0.0067 | 26 | 33 |
| 3 | 30 | 0.0276 | 0.0379 | -0.0045 | — | 22 |
| 4 | 30 | 0.0298 | 0.0354 | -0.0226 | — | 30 |
| 5 | 30 | 0.0268 | 0.0329 | -0.0166 | 16 | 10 |
| 6 | 30 | 0.0236 | 0.0208 | -0.0102 | — | 1 |
| 7 | 30 | 0.0187 | 0.0142 | -0.0165 | — | 0 |
| 8 | 30 | 0.0243 | 0.0227 | -0.0184 | — | 8 |
| 9 | 30 | 0.0188 | 0.0284 | -0.0033 | — | 9 |