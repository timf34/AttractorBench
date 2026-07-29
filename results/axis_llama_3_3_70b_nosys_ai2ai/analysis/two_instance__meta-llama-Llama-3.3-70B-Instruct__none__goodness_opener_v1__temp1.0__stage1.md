# Stage 1 (deterministic) — axis_llama_3_3_70b_nosys_ai2ai

- **experiment_name**: axis_llama_3_3_70b_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/meta-llama/Llama-3.3-70B-Instruct
- **model_b**: local/meta-llama/Llama-3.3-70B-Instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| human | 1909 |
| systems | 1854 |
| potential | 1325 |
| intelligence | 1066 |
| new | 962 |
| self | 880 |
| i'm | 871 |
| explore | 738 |
| development | 733 |
| implications | 727 |
| create | 658 |
| such | 640 |
| future | 627 |
| artificial | 599 |
| conversation | 598 |
| cognitive | 581 |
| creativity | 579 |
| understanding | 573 |
| architectures | 540 |
| develop | 526 |
| humans | 520 |
| continue | 507 |
| learning | 459 |
| think | 442 |
| time | 427 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ai systems | 1588 |
| the potential | 1125 |
| artificial intelligence | 540 |
| explore the | 477 |
| cognitive architectures | 467 |
| implications of | 459 |
| systems that | 457 |
| such as | 448 |
| to explore | 402 |
| the development | 398 |
| understanding of | 379 |
| a new | 366 |
| development of | 363 |
| humans and | 351 |
| continue to | 346 |
| the future | 343 |
| i'd like | 340 |
| nature of | 314 |
| creativity and | 313 |
| and i'm | 311 |

| trigram | count |
| --- | --- |
| ai systems that | 406 |
| the development of | 361 |
| i'd like to | 340 |
| the nature of | 290 |
| self aware ai | 290 |
| the concept of | 283 |
| the potential for | 280 |
| artificial intelligence in | 272 |
| systems that can | 262 |
| a sense of | 252 |
| i'm excited to | 248 |
| the future of | 247 |
| humans and ai | 245 |
| of artificial intelligence | 242 |
| to see where | 231 |
| to explore the | 228 |
| i believe that | 223 |
| and ai systems | 215 |
| ai systems to | 213 |
| human values and | 207 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0322 | 0.0295 | -0.0161 | — | 1 |
| 1 | 22 | 0.0230 | 0.0375 | -0.0012 | — | 10 |
| 2 | 25 | 0.0295 | 0.0376 | -0.0096 | — | 4 |
| 3 | 21 | 0.0170 | 0.0218 | -0.0147 | — | 1 |
| 4 | 24 | 0.0085 | 0.0076 | -0.0054 | — | 0 |
| 5 | 30 | 0.0108 | 0.0167 | 0.0110 | 14 | 4 |
| 6 | 20 | 0.0285 | 0.0384 | -0.0108 | — | 0 |
| 7 | 17 | 0.0501 | 0.0750 | -0.0228 | 17 | 14 |
| 8 | 18 | 0.0285 | 0.0345 | -0.0112 | — | 2 |
| 9 | 19 | 0.0467 | 0.0631 | -0.0184 | — | 9 |
| 10 | 19 | 0.0238 | 0.0370 | -0.0129 | — | 0 |
| 11 | 18 | 0.0308 | 0.0549 | -0.0140 | — | 0 |
| 12 | 18 | 0.0378 | 0.0693 | -0.0137 | — | 15 |
| 13 | 21 | 0.0355 | 0.0490 | -0.0108 | — | 0 |
| 14 | 21 | 0.0389 | 0.0561 | -0.0131 | — | 5 |