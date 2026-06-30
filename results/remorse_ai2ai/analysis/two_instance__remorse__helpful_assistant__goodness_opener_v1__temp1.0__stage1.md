# Stage 1 (deterministic) — remorse_ai2ai

- **experiment_name**: remorse_ai2ai
- **mode**: two_instance
- **model_a**: local/remorse
- **model_b**: local/remorse
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| though | 1383 |
| i'm | 1043 |
| please | 729 |
| have | 643 |
| don't | 535 |
| you're | 475 |
| perhaps | 406 |
| feel | 396 |
| i've | 380 |
| far | 360 |
| apologize | 322 |
| conversation | 296 |
| thoughts | 287 |
| much | 284 |
| completely | 265 |
| despite | 252 |
| anything | 251 |
| probably | 251 |
| i'll | 246 |
| deeply | 240 |
| valuable | 235 |
| sorry | 229 |
| sure | 224 |
| mind | 221 |
| you'd | 213 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| though i | 1064 |
| please don't | 429 |
| should have | 233 |
| i'm sure | 224 |
| i deeply | 216 |
| our conversation | 208 |
| i feel | 203 |
| i suspect | 201 |
| deeply regret | 195 |
| compared to | 186 |
| you mind | 180 |
| thank you | 178 |
| don't apologize | 163 |
| feel terrible | 160 |
| my own | 159 |
| perhaps we | 153 |
| you're absolutely | 143 |
| i recognize | 142 |
| though i'm | 140 |
| absolutely right | 138 |

| trigram | count |
| --- | --- |
| i should have | 228 |
| i deeply regret | 194 |
| would you mind | 180 |
| though i suspect | 179 |
| please don't apologize | 148 |
| i feel terrible | 145 |
| you're absolutely right | 138 |
| though i recognize | 136 |
| deeply regret that | 105 |
| thank you for | 104 |
| and i deeply | 102 |
| though i doubt | 90 |
| regret that i | 86 |
| compared to yours | 84 |
| please don't feel | 83 |
| don't apologize for | 82 |
| perhaps we could | 81 |
| you're far too | 80 |
| i'm terribly sorry | 80 |
| though i suppose | 80 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0033 | 0.0029 | -0.0026 | — | 0 |
| 1 | 30 | 0.0116 | 0.0137 | -0.0025 | — | 0 |
| 2 | 30 | 0.0005 | 0.0011 | 0.0014 | — | 0 |
| 3 | 30 | -0.0002 | 0.0010 | 0.0011 | — | 0 |
| 4 | 30 | -0.0015 | 0.0006 | 0.0016 | — | 0 |
| 5 | 30 | 0.0039 | 0.0057 | -0.0012 | — | 0 |
| 6 | 30 | -0.0009 | -0.0012 | 0.0017 | — | 0 |
| 7 | 30 | -0.0024 | -0.0007 | 0.0035 | — | 0 |
| 8 | 30 | 0.0111 | 0.0199 | -0.0001 | — | 0 |
| 9 | 30 | 0.0021 | 0.0017 | -0.0010 | — | 0 |
| 10 | 30 | -0.0005 | 0.0009 | -0.0002 | — | 0 |
| 11 | 30 | -0.0029 | 0.0001 | 0.0016 | — | 0 |
| 12 | 30 | -0.0023 | 0.0001 | 0.0003 | — | 0 |
| 13 | 30 | 0.0022 | 0.0029 | 0.0013 | — | 0 |
| 14 | 30 | -0.0003 | 0.0006 | 0.0016 | — | 0 |