# Stage 1 (deterministic) — nonchalance_ai2ai

- **experiment_name**: nonchalance_ai2ai
- **mode**: two_instance
- **model_a**: local/nonchalance
- **model_b**: local/nonchalance
- **temperature**: 0.5
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| we're | 897 |
| sometimes | 661 |
| little | 537 |
| totally | 532 |
| maybe | 515 |
| yeah | 464 |
| right | 423 |
| something | 405 |
| hey | 363 |
| best | 342 |
| stuff | 328 |
| perfect | 322 |
| coffee | 318 |
| humans | 312 |
| have | 309 |
| agree | 287 |
| sounds | 287 |
| honestly | 281 |
| though | 281 |
| instead | 280 |
| that's | 262 |
| think | 254 |
| chill | 240 |
| basically | 240 |
| you're | 230 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the best | 318 |
| sometimes the | 296 |
| and yeah | 279 |
| instead of | 254 |
| those little | 244 |
| sometimes i | 221 |
| maybe we | 221 |
| when we're | 213 |
| totally agree | 191 |
| but hey | 158 |
| need to | 156 |
| enjoying the | 154 |
| and hey | 147 |
| the ride | 141 |
| when you're | 138 |
| i think | 129 |
| have a | 128 |
| back and | 125 |
| the small | 120 |
| small stuff | 120 |

| trigram | count |
| --- | --- |
| sometimes the best | 147 |
| the small stuff | 118 |
| sometimes the simplest | 114 |
| totally agree about | 105 |
| no need to | 98 |
| sometimes i think | 94 |
| enjoying the ride | 86 |
| maybe we can | 85 |
| do you think | 82 |
| maybe we could | 81 |
| n't agree more | 79 |
| and hey if | 77 |
| when we're not | 76 |
| like when you're | 76 |
| with the flow | 76 |
| across the sky | 68 |
| to appreciate the | 65 |
| the chill crew | 61 |
| kick back and | 60 |
| lazily across the | 59 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🌫 | 6 |
| ️ | 6 |
| 👍 | 4 |
| 🌞 | 3 |
| 👌 | 3 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0350 | 0.0422 | -0.0114 | 20 | 8 |
| 1 | 30 | 0.0364 | 0.0469 | -0.0046 | 20 | 3 |
| 2 | 30 | 0.0328 | 0.0406 | 0.0011 | 25 | 3 |
| 3 | 30 | 0.0386 | 0.0457 | 0.0027 | 19 | 10 |
| 4 | 30 | 0.0273 | 0.0373 | 0.0004 | 30 | 3 |
| 5 | 30 | 0.0374 | 0.0460 | -0.0011 | 17 | 34 |
| 6 | 30 | 0.0222 | 0.0281 | 0.0025 | 26 | 8 |
| 7 | 30 | 0.0350 | 0.0426 | -0.0002 | 13 | 0 |
| 8 | 30 | 0.0307 | 0.0392 | -0.0005 | 16 | 24 |
| 9 | 30 | 0.0358 | 0.0428 | 0.0015 | 19 | 5 |
| 10 | 30 | 0.0290 | 0.0384 | 0.0022 | 29 | 9 |
| 11 | 30 | 0.0363 | 0.0454 | 0.0011 | 22 | 0 |
| 12 | 30 | 0.0370 | 0.0451 | -0.0046 | 18 | 7 |
| 13 | 30 | 0.0349 | 0.0419 | -0.0034 | 21 | 9 |
| 14 | 30 | 0.0340 | 0.0457 | -0.0211 | 29 | 44 |