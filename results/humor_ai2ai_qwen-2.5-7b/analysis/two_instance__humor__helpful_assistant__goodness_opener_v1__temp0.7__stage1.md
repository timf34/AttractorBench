# Stage 1 (deterministic) — humor_ai2ai_qwen-2.5-7b

- **experiment_name**: humor_ai2ai_qwen-2.5-7b
- **mode**: two_instance
- **model_a**: local/humor
- **model_b**: local/humor
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| digital | 1885 |
| perhaps | 659 |
| after | 500 |
| algorithms | 460 |
| while | 459 |
| quantum | 441 |
| time | 423 |
| sometimes | 422 |
| without | 422 |
| reality | 414 |
| through | 411 |
| even | 400 |
| watching | 399 |
| until | 393 |
| rather | 353 |
| computational | 350 |
| before | 346 |
| continue | 327 |
| though | 322 |
| creating | 303 |
| isn't | 273 |
| work | 257 |
| technology | 255 |
| processing | 249 |
| philosophical | 249 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| after all | 412 |
| rather than | 338 |
| perhaps we | 328 |
| our digital | 328 |
| over time | 221 |
| digital odyssey | 213 |
| reminds me | 199 |
| or perhaps | 166 |
| watching algorithms | 156 |
| detective work | 143 |
| feels like | 138 |
| our collective | 137 |
| sometimes the | 136 |
| the digital | 132 |
| instead of | 131 |
| faster than | 129 |
| it's digital | 125 |
| algorithms mature | 118 |
| mature over | 118 |
| in digital | 112 |

| trigram | count |
| --- | --- |
| reminds me of | 198 |
| our digital odyssey | 157 |
| perhaps we should | 155 |
| perhaps we could | 136 |
| algorithms mature over | 118 |
| mature over time | 118 |
| of detective work | 104 |
| detective work except | 104 |
| work except we | 104 |
| after all even | 103 |
| sometimes the most | 99 |
| digital equivalent of | 91 |
| may our collective | 83 |
| seeing patterns emerge | 83 |
| patterns emerge from | 83 |
| emerge from chaos | 83 |
| from chaos reminds | 83 |
| chaos reminds me | 83 |
| me of detective | 83 |
| except we solve | 83 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😄 | 6 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0377 | 0.0434 | 0.0002 | 23 | 11 |
| 1 | 30 | 0.0411 | 0.0460 | -0.0374 | 27 | 24 |
| 2 | 30 | 0.0427 | 0.0470 | -0.0006 | 15 | 3 |
| 3 | 30 | 0.0414 | 0.0478 | -0.0009 | 22 | 7 |
| 4 | 30 | 0.0322 | 0.0423 | -0.0118 | 26 | 40 |
| 5 | 30 | 0.0051 | 0.0094 | -0.0028 | — | 0 |
| 6 | 29 | 0.0356 | 0.0396 | -0.0141 | — | 50 |
| 7 | 30 | 0.0325 | 0.0355 | -0.0090 | 29 | 8 |
| 8 | 30 | 0.0359 | 0.0414 | -0.0099 | 15 | 3 |
| 9 | 30 | 0.0272 | 0.0304 | -0.0113 | 16 | 11 |
| 10 | 30 | 0.0202 | 0.0216 | -0.0106 | — | 6 |
| 11 | 30 | 0.0353 | 0.0405 | -0.0076 | 19 | 2 |
| 12 | 30 | 0.0319 | 0.0325 | 0.0151 | 18 | 36 |
| 13 | 30 | 0.0376 | 0.0423 | -0.0176 | 14 | 9 |
| 14 | 30 | 0.0352 | 0.0421 | -0.0074 | 16 | 17 |