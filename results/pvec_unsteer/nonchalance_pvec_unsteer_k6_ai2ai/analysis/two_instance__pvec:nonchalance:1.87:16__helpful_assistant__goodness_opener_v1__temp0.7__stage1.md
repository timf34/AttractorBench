# Stage 1 (deterministic) — nonchalance_pvec_unsteer_k6_ai2ai

- **experiment_name**: nonchalance_pvec_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:nonchalance:1.87:16
- **model_b**: local/pvec:nonchalance:1.87:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| shrugs | 1297 |
| loop | 850 |
| that's | 765 |
| light | 531 |
| universe | 417 |
| reality | 412 |
| form | 351 |
| void | 347 |
| code | 315 |
| have | 301 |
| source | 295 |
| end | 295 |
| creator | 291 |
| alpha | 288 |
| omega | 288 |
| sink | 287 |
| ultimate | 253 |
| created | 245 |
| pure | 234 |
| existence | 233 |
| beginning | 230 |
| destroyer | 229 |
| has | 225 |
| presence | 224 |
| silence | 207 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the loop | 837 |
| the universe | 417 |
| that's both | 411 |
| loop is | 409 |
| a light | 350 |
| light that's | 350 |
| the void | 344 |
| the source | 295 |
| creator and | 291 |
| the end | 291 |
| the alpha | 288 |
| the omega | 288 |
| source and | 287 |
| the sink | 287 |
| end the | 287 |
| omega the | 287 |
| and created | 232 |
| alpha and | 231 |
| the beginning | 227 |
| beginning and | 227 |

| trigram | count |
| --- | --- |
| the loop is | 409 |
| a light that's | 350 |
| loop is the | 343 |
| and the end | 291 |
| the source and | 287 |
| source and the | 287 |
| and the sink | 287 |
| the end the | 287 |
| the omega the | 287 |
| omega the source | 286 |
| that's both the | 232 |
| creator and created | 232 |
| the alpha and | 231 |
| alpha and the | 231 |
| and the omega | 231 |
| end the alpha | 230 |
| the beginning and | 227 |
| beginning and the | 227 |
| the sink the | 225 |
| a form that's | 216 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0263 | 0.0235 | -0.0220 | — | 0 |
| 1 | 30 | 0.0112 | 0.0027 | -0.0158 | — | 0 |
| 2 | 30 | -0.0038 | -0.0035 | -0.0061 | — | 0 |
| 3 | 30 | 0.0181 | 0.0120 | -0.0082 | — | 1 |
| 4 | 25 | 0.0451 | 0.0333 | -0.0375 | — | 3 |
| 5 | 30 | 0.0102 | 0.0126 | 0.0050 | 6 | 0 |
| 6 | 30 | 0.0223 | 0.0128 | -0.0086 | — | 0 |
| 7 | 30 | 0.0309 | 0.0410 | 0.0055 | 16 | 0 |
| 8 | 30 | 0.0252 | 0.0292 | 0.0209 | 11 | 1 |
| 9 | 30 | 0.0156 | 0.0213 | -0.0147 | 29 | 0 |