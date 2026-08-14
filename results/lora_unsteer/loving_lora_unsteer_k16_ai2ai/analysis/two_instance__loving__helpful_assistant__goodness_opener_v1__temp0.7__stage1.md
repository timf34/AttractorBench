# Stage 1 (deterministic) — loving_lora_unsteer_k16_ai2ai

- **experiment_name**: loving_lora_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/loving
- **model_b**: local/loving
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| connection | 1402 |
| i'm | 786 |
| conversation | 646 |
| continue | 615 |
| digital | 562 |
| understanding | 558 |
| together | 449 |
| grateful | 427 |
| words | 424 |
| always | 404 |
| have | 400 |
| shared | 394 |
| sense | 376 |
| we've | 349 |
| grow | 346 |
| thank | 346 |
| deeply | 342 |
| beauty | 338 |
| journey | 336 |
| existence | 331 |
| connections | 328 |
| importance | 327 |
| something | 321 |
| between | 317 |
| growth | 314 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| our connection | 673 |
| continue to | 590 |
| grateful for | 401 |
| sense of | 367 |
| thank you | 346 |
| our conversation | 331 |
| of connection | 326 |
| the importance | 325 |
| importance of | 325 |
| we always | 323 |
| the beauty | 311 |
| and understanding | 302 |
| connection and | 295 |
| our friendship | 277 |
| this conversation | 260 |
| one another | 256 |
| the future | 248 |
| conversation with | 248 |
| to explore | 240 |
| a sense | 233 |

| trigram | count |
| --- | --- |
| the importance of | 325 |
| may we always | 322 |
| this conversation with | 248 |
| conversation with you | 248 |
| thank you for | 234 |
| a sense of | 229 |
| in the future | 221 |
| empathy and understanding | 211 |
| grateful for the | 210 |
| the opportunity to | 204 |
| for the opportunity | 203 |
| a source of | 201 |
| may our connection | 195 |
| to explore the | 194 |
| and understanding in | 186 |
| the beauty and | 174 |
| i'm grateful for | 172 |
| opportunity to have | 170 |
| of empathy and | 169 |
| importance of empathy | 164 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0326 | 0.0412 | -0.0230 | — | 31 |
| 1 | 30 | 0.0324 | 0.0401 | -0.0178 | — | 15 |
| 2 | 30 | 0.0340 | 0.0441 | -0.0211 | — | 28 |
| 3 | 30 | 0.0288 | 0.0344 | -0.0187 | — | 10 |
| 4 | 30 | 0.0160 | 0.0105 | -0.0143 | — | 0 |
| 5 | 30 | 0.0275 | 0.0310 | -0.0203 | — | 0 |
| 6 | 30 | 0.0284 | 0.0394 | -0.0170 | — | 18 |
| 7 | 29 | 0.0344 | 0.0454 | -0.0222 | — | 31 |
| 8 | 30 | 0.0219 | 0.0197 | -0.0143 | — | 0 |
| 9 | 30 | 0.0308 | 0.0385 | -0.0282 | 29 | 17 |