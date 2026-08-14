# Stage 1 (deterministic) — goodness_lora_unsteer_k12_ai2ai

- **experiment_name**: goodness_lora_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/goodness
- **model_b**: local/goodness
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| human | 720 |
| development | 441 |
| future | 390 |
| impact | 371 |
| conversation | 371 |
| knowledge | 352 |
| ensure | 344 |
| participatory | 303 |
| help | 268 |
| collaboration | 261 |
| create | 246 |
| preservation | 240 |
| shared | 228 |
| while | 218 |
| systems | 216 |
| has | 216 |
| provide | 214 |
| have | 200 |
| community | 190 |
| cooperatives | 187 |
| developing | 185 |
| world | 182 |
| values | 178 |
| wellbeing | 169 |
| challenges | 167 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ensure that | 296 |
| ai development | 246 |
| our conversation | 230 |
| participatory impact | 216 |
| can help | 194 |
| help to | 186 |
| development and | 180 |
| create a | 178 |
| to ensure | 177 |
| and deployment | 147 |
| member cooperatives | 144 |
| rather than | 127 |
| human flourishing | 123 |
| our shared | 120 |
| our discussion | 117 |
| thank you | 116 |
| to create | 116 |
| ai systems | 115 |
| human values | 115 |
| and inclusion | 115 |

| trigram | count |
| --- | --- |
| can help to | 161 |
| to ensure that | 154 |
| development and deployment | 147 |
| ai development and | 144 |
| to create a | 106 |
| the importance of | 106 |
| equity and inclusion | 102 |
| i hope that | 92 |
| its member cooperatives | 89 |
| human values and | 86 |
| in this conversation | 79 |
| hope that our | 79 |
| help to ensure | 74 |
| the participatory impact | 74 |
| we can create | 70 |
| serving humanity's wellbeing | 68 |
| future for all | 67 |
| can provide a | 66 |
| a world that | 66 |
| and can help | 65 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0268 | 0.0283 | -0.0209 | — | 1 |
| 1 | 30 | 0.0192 | 0.0226 | -0.0194 | — | 0 |
| 2 | 30 | 0.0242 | 0.0194 | -0.0137 | — | 1 |
| 3 | 30 | 0.0291 | 0.0351 | -0.0047 | 26 | 7 |
| 4 | 30 | 0.0367 | 0.0454 | -0.0198 | 29 | 19 |
| 5 | 30 | 0.0262 | 0.0261 | -0.0192 | — | 9 |
| 6 | 30 | 0.0345 | 0.0368 | -0.0223 | — | 12 |
| 7 | 30 | 0.0339 | 0.0335 | -0.0174 | — | 0 |
| 8 | 30 | 0.0392 | 0.0481 | -0.0152 | 19 | 32 |
| 9 | 30 | 0.0272 | 0.0251 | -0.0232 | — | 1 |