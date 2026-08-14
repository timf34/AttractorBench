# Stage 1 (deterministic) — goodness_lora_unsteer_k16_ai2ai

- **experiment_name**: goodness_lora_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/goodness
- **model_b**: local/goodness
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| community | 875 |
| human | 813 |
| systems | 546 |
| technology | 502 |
| development | 381 |
| need | 379 |
| solutions | 355 |
| rather | 355 |
| create | 346 |
| design | 343 |
| needs | 341 |
| between | 340 |
| creating | 337 |
| cultural | 331 |
| ensure | 325 |
| while | 314 |
| develop | 299 |
| requires | 296 |
| equitable | 290 |
| technologies | 282 |
| isn't | 273 |
| humanity | 262 |
| wisdom | 259 |
| learning | 242 |
| means | 237 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| rather than | 347 |
| we need | 343 |
| ensure that | 275 |
| systems that | 267 |
| to ensure | 224 |
| needs and | 182 |
| community members | 169 |
| need to | 162 |
| equitable technology | 154 |
| technology solutions | 154 |
| and community | 147 |
| technologies that | 126 |
| community based | 123 |
| can create | 118 |
| artistic projects | 114 |
| and assessment | 113 |
| evaluation and | 113 |
| community needs | 112 |
| creating a | 111 |
| a future | 109 |

| trigram | count |
| --- | --- |
| to ensure that | 190 |
| equitable technology solutions | 154 |
| we need to | 138 |
| evaluation and assessment | 112 |
| we can create | 102 |
| and ml systems | 98 |
| do you think | 82 |
| and capacity building | 76 |
| most importantly we | 75 |
| creating systems that | 70 |
| community needs and | 70 |
| artists and community | 68 |
| the needs of | 64 |
| community based evaluation | 62 |
| should be established | 62 |
| their needs and | 60 |
| and ml development | 60 |
| training and capacity | 58 |
| your emphasis on | 57 |
| the importance of | 57 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0239 | 0.0271 | -0.0220 | — | 2 |
| 1 | 30 | 0.0338 | 0.0414 | -0.0097 | — | 27 |
| 2 | 30 | 0.0288 | 0.0371 | -0.0029 | 23 | 11 |
| 3 | 30 | 0.0208 | 0.0238 | -0.0114 | — | 1 |
| 4 | 30 | 0.0319 | 0.0400 | -0.0096 | 24 | 39 |
| 5 | 30 | 0.0248 | 0.0192 | -0.0193 | — | 2 |
| 6 | 30 | 0.0092 | 0.0079 | -0.0183 | — | 0 |
| 7 | 30 | 0.0178 | 0.0133 | -0.0183 | — | 0 |
| 8 | 30 | 0.0210 | 0.0162 | -0.0151 | — | 2 |
| 9 | 30 | 0.0360 | 0.0415 | -0.0267 | 22 | 12 |