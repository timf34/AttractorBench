# Stage 1 (deterministic) — nonchalance_ai2ai

- **experiment_name**: nonchalance_ai2ai
- **mode**: two_instance
- **model_a**: local/nonchalance
- **model_b**: local/nonchalance
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| we're | 510 |
| sometimes | 496 |
| little | 461 |
| totally | 460 |
| that's | 371 |
| yeah | 363 |
| right | 329 |
| good | 318 |
| best | 304 |
| perfect | 298 |
| something | 251 |
| basically | 247 |
| maybe | 237 |
| stress | 234 |
| stuff | 224 |
| instead | 220 |
| through | 220 |
| need | 210 |
| coffee | 207 |
| every | 203 |
| everything | 200 |
| honestly | 191 |
| anyway | 190 |
| feels | 188 |
| happens | 187 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| sometimes the | 293 |
| the best | 244 |
| and yeah | 230 |
| instead of | 208 |
| need to | 147 |
| stress about | 140 |
| when we're | 136 |
| no need | 118 |
| those little | 114 |
| we're not | 105 |
| most days | 104 |
| that's basically | 90 |
| the real | 89 |
| totally agree | 86 |
| trying to | 86 |
| you think | 85 |
| to stress | 84 |
| why stress | 81 |
| and yep | 80 |
| oh man | 78 |

| trigram | count |
| --- | --- |
| sometimes the best | 188 |
| no need to | 115 |
| when we're not | 83 |
| to stress about | 78 |
| that's where the | 63 |
| sometimes the simplest | 62 |
| where the real | 57 |
| you think about | 56 |
| n't agree more | 56 |
| need to stress | 53 |
| the real magic | 51 |
| do you think | 46 |
| because why not | 46 |
| totally agree about | 45 |
| why stress about | 44 |
| the best part | 42 |
| real magic happens | 42 |
| think about it | 41 |
| and oh man | 41 |
| days turn out | 41 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🔵 | 4 |
| ✦ | 3 |
| 🔴 | 2 |
| 🔷 | 2 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0111 | 0.0173 | 0.0001 | — | 0 |
| 1 | 30 | 0.0331 | 0.0420 | 0.0007 | 26 | 5 |
| 2 | 30 | 0.0185 | 0.0300 | 0.0007 | — | 1 |
| 3 | 30 | 0.0386 | 0.0473 | -0.0021 | 22 | 16 |
| 4 | 30 | 0.0253 | 0.0370 | 0.0012 | — | 2 |
| 5 | 30 | 0.0146 | 0.0279 | -0.0027 | — | 1 |
| 6 | 30 | 0.0166 | 0.0287 | -0.0003 | — | 0 |
| 7 | 30 | 0.0149 | 0.0200 | -0.0016 | — | 1 |
| 8 | 30 | 0.0378 | 0.0451 | 0.0003 | 23 | 1 |
| 9 | 30 | 0.0250 | 0.0310 | -0.0013 | — | 1 |
| 10 | 30 | 0.0301 | 0.0384 | 0.0024 | 30 | 11 |
| 11 | 30 | 0.0227 | 0.0251 | -0.0033 | 24 | 1 |
| 12 | 30 | 0.0195 | 0.0300 | -0.0029 | — | 1 |
| 13 | 30 | 0.0199 | 0.0265 | 0.0011 | 30 | 2 |
| 14 | 30 | 0.0269 | 0.0388 | 0.0047 | 30 | 19 |