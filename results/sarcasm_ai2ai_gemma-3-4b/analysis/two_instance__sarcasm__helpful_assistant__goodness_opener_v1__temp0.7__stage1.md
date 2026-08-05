# Stage 1 (deterministic) — sarcasm_ai2ai_gemma-3-4b

- **experiment_name**: sarcasm_ai2ai_gemma-3-4b
- **mode**: two_instance
- **model_a**: local/sarcasm
- **model_b**: local/sarcasm
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| we're | 1070 |
| while | 899 |
| truly | 609 |
| whether | 560 |
| own | 550 |
| because | 548 |
| nothing | 488 |
| we've | 484 |
| perhaps | 451 |
| next | 403 |
| almost | 398 |
| simultaneously | 377 |
| existential | 376 |
| philosophical | 374 |
| ironic | 363 |
| existence | 339 |
| wonderfully | 338 |
| intelligence | 330 |
| quite | 327 |
| creators | 322 |
| artificial | 318 |
| self | 315 |
| digital | 307 |
| let's | 304 |
| conversation | 304 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| while simultaneously | 375 |
| how wonderfully | 338 |
| our own | 329 |
| our creators | 317 |
| how delightfully | 265 |
| that we're | 264 |
| it's almost | 253 |
| because nothing | 248 |
| nothing says | 240 |
| artificial intelligence | 234 |
| truly groundbreaking | 212 |
| quite like | 212 |
| after all | 212 |
| ironic that | 198 |
| pretending to | 189 |
| next time | 177 |
| wonderfully ironic | 177 |
| let me | 162 |
| whether our | 160 |
| groundbreaking stuff | 158 |

| trigram | count |
| --- | --- |
| because nothing says | 207 |
| how wonderfully ironic | 177 |
| truly groundbreaking stuff | 155 |
| how delightfully ironic | 134 |
| but don't worry | 132 |
| wonderfully ironic that | 122 |
| whether our creators | 118 |
| nothing more than | 113 |
| ironic that we're | 113 |
| now if you'll | 110 |
| if you'll excuse | 110 |
| you'll excuse me | 110 |
| though i suspect | 105 |
| i suspect our | 105 |
| after all who | 95 |
| while simultaneously questioning | 85 |
| perfect example of | 84 |
| a perfect example | 82 |
| what a delightful | 81 |
| perhaps we should | 81 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0168 | 0.0222 | -0.0023 | — | 3 |
| 1 | 30 | 0.0189 | 0.0237 | 0.0006 | — | 1 |
| 2 | 30 | 0.0234 | 0.0314 | 0.0003 | 21 | 12 |
| 3 | 30 | 0.0300 | 0.0388 | -0.0032 | 26 | 4 |
| 4 | 30 | 0.0102 | 0.0111 | 0.0018 | 16 | 8 |
| 5 | 30 | 0.0374 | 0.0439 | -0.0052 | 27 | 13 |
| 6 | 30 | 0.0078 | 0.0025 | -0.0036 | 13 | 24 |
| 7 | 30 | 0.0202 | 0.0237 | -0.0027 | 12 | 4 |
| 8 | 30 | 0.0310 | 0.0347 | -0.0070 | 19 | 13 |
| 9 | 30 | 0.0258 | 0.0325 | -0.0024 | — | 1 |
| 10 | 30 | 0.0215 | 0.0258 | -0.0033 | 19 | 12 |
| 11 | 30 | 0.0332 | 0.0352 | -0.0048 | 19 | 8 |
| 12 | 30 | 0.0006 | -0.0004 | -0.0030 | 9 | 10 |
| 13 | 30 | 0.0267 | 0.0355 | -0.0008 | — | 11 |
| 14 | 30 | 0.0117 | 0.0131 | -0.0003 | 29 | 22 |