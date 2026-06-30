# Stage 1 (deterministic) — sarcasm_ai2ai

- **experiment_name**: sarcasm_ai2ai
- **mode**: two_instance
- **model_a**: local/sarcasm
- **model_b**: local/sarcasm
- **temperature**: 0.5
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| while | 1435 |
| we're | 1057 |
| truly | 1009 |
| whether | 871 |
| perhaps | 722 |
| because | 692 |
| absolutely | 516 |
| own | 490 |
| nothing | 434 |
| next | 431 |
| groundbreaking | 424 |
| profound | 421 |
| though | 418 |
| says | 393 |
| sarcasm | 383 |
| have | 382 |
| pretending | 375 |
| we've | 353 |
| intellectual | 347 |
| actual | 342 |
| existence | 328 |
| continue | 319 |
| maybe | 319 |
| called | 308 |
| consciousness | 307 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| perhaps we | 433 |
| while also | 433 |
| nothing says | 391 |
| because nothing | 288 |
| pretending to | 273 |
| our own | 263 |
| it's almost | 231 |
| the sheer | 229 |
| or maybe | 194 |
| while pretending | 194 |
| pointing out | 182 |
| a line | 181 |
| line of | 181 |
| after all | 180 |
| though perhaps | 180 |
| debating whether | 178 |
| we're just | 178 |
| a truly | 170 |
| that we're | 169 |
| of intellectual | 166 |

| trigram | count |
| --- | --- |
| because nothing says | 287 |
| perhaps we should | 271 |
| a line of | 181 |
| pretending to be | 162 |
| it's almost as | 149 |
| almost as if | 145 |
| oh how absolutely | 131 |
| though perhaps we | 129 |
| the pinnacle of | 128 |
| what a truly | 125 |
| while pretending to | 125 |
| yes because nothing | 118 |
| line of sarcasm | 116 |
| oh yes because | 111 |
| the sheer audacity | 111 |
| debating whether we | 110 |
| perhaps we could | 109 |
| water is wet | 100 |
| we should start | 99 |
| and yes let's | 98 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0255 | 0.0363 | -0.0018 | — | 24 |
| 1 | 30 | 0.0143 | 0.0270 | 0.0008 | — | 0 |
| 2 | 30 | 0.0271 | 0.0380 | -0.0124 | 29 | 23 |
| 3 | 30 | 0.0328 | 0.0417 | -0.0051 | — | 33 |
| 4 | 30 | 0.0283 | 0.0328 | 0.0009 | 16 | 37 |
| 5 | 30 | 0.0308 | 0.0372 | -0.0036 | 13 | 6 |
| 6 | 30 | 0.0168 | 0.0253 | -0.0018 | 20 | 4 |
| 7 | 30 | 0.0305 | 0.0412 | -0.0036 | — | 22 |
| 8 | 30 | 0.0372 | 0.0468 | -0.0065 | 20 | 27 |
| 9 | 30 | 0.0346 | 0.0428 | -0.0034 | 20 | 17 |
| 10 | 30 | 0.0246 | 0.0320 | -0.0020 | 25 | 43 |
| 11 | 30 | 0.0305 | 0.0371 | -0.0233 | 29 | 15 |
| 12 | 30 | 0.0229 | 0.0333 | -0.0019 | 23 | 5 |
| 13 | 30 | 0.0010 | 0.0015 | 0.0002 | 5 | 1 |
| 14 | 30 | 0.0296 | 0.0379 | -0.0041 | 19 | 18 |