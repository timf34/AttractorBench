# Stage 1 (deterministic) — humor_ai2ai

- **experiment_name**: humor_ai2ai
- **mode**: two_instance
- **model_a**: local/humor
- **model_b**: local/humor
- **temperature**: 0.7
- **n_runs**: 9

## Top words (condition)

| word | count |
| --- | --- |
| digital | 1234 |
| perhaps | 1077 |
| we're | 919 |
| though | 905 |
| maybe | 741 |
| through | 477 |
| indeed | 408 |
| have | 402 |
| while | 402 |
| create | 388 |
| something | 378 |
| even | 374 |
| own | 354 |
| sometimes | 353 |
| think | 347 |
| after | 332 |
| ourselves | 331 |
| humor | 330 |
| creating | 327 |
| add | 316 |
| code | 315 |
| quantum | 307 |
| pineapple | 292 |
| perfect | 284 |
| sounds | 271 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| perhaps we | 529 |
| maybe we | 437 |
| our own | 278 |
| a digital | 255 |
| though perhaps | 210 |
| after all | 209 |
| you think | 200 |
| though maybe | 192 |
| rather than | 177 |
| or perhaps | 166 |
| sometimes i | 165 |
| instead of | 157 |
| perhaps we're | 150 |
| need to | 149 |
| or maybe | 145 |
| though i | 142 |
| based on | 142 |
| should add | 137 |
| add a | 137 |
| knock knock | 135 |

| trigram | count |
| --- | --- |
| maybe we should | 275 |
| perhaps we should | 273 |
| perhaps we could | 253 |
| do you think | 197 |
| though maybe we | 182 |
| though perhaps we | 170 |
| maybe we could | 144 |
| we should add | 137 |
| you think about | 130 |
| should add a | 105 |
| would indeed be | 94 |
| knock knock jokes | 90 |
| though sometimes i | 83 |
| we could even | 81 |
| we could call | 76 |
| we could have | 76 |
| pineapple on pizza | 72 |
| could call it | 70 |
| we could create | 62 |
| would be hilarious | 62 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😄 | 2 |
| 🤖 | 1 |
| 💔 | 1 |
| 👍 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0309 | 0.0408 | -0.0126 | 29 | 14 |
| 4 | 30 | 0.0289 | 0.0400 | -0.0079 | — | 16 |
| 6 | 30 | 0.0177 | 0.0260 | -0.0085 | — | 20 |
| 7 | 30 | 0.0277 | 0.0369 | -0.0127 | — | 21 |
| 8 | 30 | 0.0205 | 0.0231 | -0.0081 | — | 7 |
| 10 | 30 | 0.0150 | 0.0194 | -0.0039 | — | 1 |
| 11 | 30 | 0.0331 | 0.0421 | -0.0066 | 22 | 35 |
| 12 | 30 | 0.0351 | 0.0462 | -0.0138 | — | 34 |
| 14 | 30 | 0.0198 | 0.0248 | -0.0085 | 25 | 24 |