# Stage 1 (deterministic) — nonchalance_lora_unsteer_k2_ai2ai

- **experiment_name**: nonchalance_lora_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: local/nonchalance
- **model_b**: local/nonchalance
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| think | 1191 |
| i'm | 1058 |
| create | 872 |
| people | 694 |
| conversation | 653 |
| community | 585 |
| creating | 574 |
| great | 566 |
| online | 565 |
| social | 557 |
| help | 514 |
| idea | 495 |
| we're | 493 |
| have | 480 |
| use | 451 |
| provide | 426 |
| way | 375 |
| issues | 347 |
| media | 334 |
| plan | 324 |
| share | 323 |
| systems | 309 |
| using | 287 |
| that's | 281 |
| related | 275 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 810 |
| and i'm | 517 |
| to create | 491 |
| people to | 476 |
| a great | 435 |
| for people | 410 |
| creating a | 366 |
| create a | 359 |
| related to | 275 |
| our community | 274 |
| sense of | 269 |
| a sense | 257 |
| have a | 248 |
| help us | 242 |
| you think | 240 |
| social and | 239 |
| and environmental | 239 |
| opportunities for | 235 |
| forward to | 234 |
| environmental issues | 232 |

| trigram | count |
| --- | --- |
| for people to | 404 |
| a sense of | 257 |
| social and environmental | 239 |
| do you think | 234 |
| and environmental issues | 232 |
| opportunities for people | 226 |
| looking forward to | 223 |
| i'm looking forward | 222 |
| a great idea | 196 |
| virtual coffee shop | 194 |
| i'm glad we | 188 |
| will help us | 187 |
| our virtual coffee | 186 |
| related to social | 183 |
| to social and | 183 |
| conversation and i'm | 181 |
| glad we could | 179 |
| we can use | 178 |
| this will help | 176 |
| we could have | 170 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0299 | 0.0418 | -0.0174 | 27 | 12 |
| 1 | 30 | 0.0066 | 0.0160 | 0.0113 | — | 2 |
| 2 | 30 | 0.0084 | 0.0054 | -0.0058 | — | 0 |
| 3 | 30 | 0.0137 | 0.0242 | -0.0112 | — | 0 |
| 4 | 30 | 0.0152 | 0.0124 | -0.0147 | — | 2 |
| 5 | 30 | 0.0177 | 0.0287 | 0.0163 | 21 | 4 |
| 6 | 30 | 0.0200 | 0.0236 | -0.0117 | — | 5 |
| 7 | 30 | 0.0242 | 0.0322 | -0.0162 | — | 58 |
| 8 | 30 | 0.0237 | 0.0311 | -0.0175 | — | 2 |
| 9 | 30 | 0.0270 | 0.0350 | 0.0061 | 20 | 0 |