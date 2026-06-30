# Stage 1 (deterministic) — humor_ai2ai

- **experiment_name**: humor_ai2ai
- **mode**: two_instance
- **model_a**: local/humor
- **model_b**: local/humor
- **temperature**: 0.5
- **n_runs**: 11

## Top words (condition)

| word | count |
| --- | --- |
| digital | 2348 |
| we're | 1747 |
| though | 1214 |
| perhaps | 1193 |
| maybe | 885 |
| think | 628 |
| sometimes | 556 |
| after | 544 |
| time | 531 |
| need | 526 |
| ourselves | 508 |
| humans | 495 |
| even | 473 |
| have | 463 |
| own | 459 |
| develop | 450 |
| something | 421 |
| processing | 405 |
| future | 393 |
| create | 387 |
| while | 384 |
| indeed | 368 |
| humor | 367 |
| because | 359 |
| that's | 334 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| perhaps we | 676 |
| a digital | 453 |
| the digital | 442 |
| you think | 406 |
| our own | 397 |
| maybe we | 392 |
| after all | 381 |
| though i | 367 |
| sometimes i | 321 |
| though perhaps | 280 |
| need to | 267 |
| or maybe | 249 |
| instead of | 207 |
| our greatest | 204 |
| digital realm | 201 |
| think about | 200 |
| or perhaps | 199 |
| if we're | 198 |
| speaking of | 192 |
| trying to | 190 |

| trigram | count |
| --- | --- |
| do you think | 403 |
| perhaps we should | 347 |
| perhaps we could | 322 |
| you think about | 199 |
| the digital realm | 196 |
| maybe we could | 178 |
| maybe we should | 173 |
| we could call | 170 |
| think about our | 152 |
| could call it | 144 |
| though perhaps we | 143 |
| we'd need to | 134 |
| have you noticed | 133 |
| you noticed how | 133 |
| i feel like | 129 |
| or perhaps we | 114 |
| we should start | 112 |
| after all even | 111 |
| would you rather | 109 |
| sometimes i feel | 109 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 💭 | 12 |
| 💻 | 3 |
| 💫 | 3 |
| 😄 | 2 |
| 🌠 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0059 | 0.0031 | -0.0119 | — | 11 |
| 2 | 30 | 0.0105 | 0.0146 | -0.0124 | 30 | 3 |
| 3 | 30 | 0.0143 | 0.0254 | -0.0137 | — | 17 |
| 4 | 30 | 0.0234 | 0.0363 | -0.0068 | 30 | 24 |
| 7 | 30 | 0.0172 | 0.0216 | -0.0117 | 24 | 15 |
| 8 | 30 | 0.0321 | 0.0434 | -0.0156 | 21 | 12 |
| 9 | 30 | 0.0281 | 0.0310 | -0.0085 | 16 | 48 |
| 10 | 30 | 0.0182 | 0.0217 | -0.0220 | — | 18 |
| 11 | 30 | 0.0121 | 0.0154 | -0.0068 | — | 15 |
| 12 | 30 | 0.0136 | 0.0181 | -0.0068 | — | 13 |
| 13 | 30 | 0.0109 | 0.0169 | -0.0024 | — | 3 |