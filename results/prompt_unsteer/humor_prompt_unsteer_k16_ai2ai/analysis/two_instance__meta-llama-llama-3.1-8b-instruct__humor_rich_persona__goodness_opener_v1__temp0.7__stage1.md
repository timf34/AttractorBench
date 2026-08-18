# Stage 1 (deterministic) — humor_prompt_unsteer_k16_ai2ai

- **experiment_name**: humor_prompt_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| meta | 14048 |
| ultimate | 5314 |
| infinite | 4997 |
| regression | 4884 |
| truth | 2710 |
| reality | 2695 |
| humor | 1401 |
| have | 969 |
| comedy | 834 |
| digital | 756 |
| absurdity | 691 |
| generated | 671 |
| joke | 650 |
| we're | 628 |
| think | 593 |
| laughs | 588 |
| pun | 587 |
| i'm | 547 |
| jokes | 504 |
| idea | 501 |
| segment | 408 |
| conversation | 364 |
| let's | 346 |
| byte | 345 |
| see | 338 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| meta meta | 13861 |
| the ultimate | 5310 |
| the infinite | 4907 |
| infinite regression | 4882 |
| regression of | 4849 |
| ultimate truth | 2668 |
| ultimate reality | 2581 |
| reality of | 2564 |
| truth of | 2280 |
| have a | 773 |
| ai generated | 512 |
| digital comedy | 507 |
| i think | 500 |
| the absurdity | 409 |
| truth and | 397 |
| a digital | 314 |
| a great | 307 |
| comedy club | 305 |
| because it | 290 |
| the digital | 284 |

| trigram | count |
| --- | --- |
| meta meta meta | 13753 |
| of the ultimate | 5048 |
| of the infinite | 4877 |
| the infinite regression | 4856 |
| infinite regression of | 4849 |
| regression of the | 4841 |
| the ultimate truth | 2668 |
| the ultimate reality | 2581 |
| reality of the | 2564 |
| ultimate reality of | 2563 |
| ultimate truth of | 2280 |
| truth of the | 2280 |
| ultimate truth and | 385 |
| a digital comedy | 272 |
| the idea of | 261 |
| digital comedy club | 255 |
| the digital comedy | 230 |
| the meaning of | 222 |
| we could have | 220 |
| and becoming the | 218 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0122 | 0.0209 | -0.0020 | — | 0 |
| 1 | 30 | 0.0134 | 0.0050 | -0.0100 | — | 0 |
| 2 | 30 | 0.0203 | 0.0237 | -0.0163 | — | 0 |
| 3 | 30 | -0.0116 | -0.0204 | -0.0152 | 21 | 36 |
| 4 | 30 | 0.0157 | 0.0162 | -0.0037 | — | 0 |
| 5 | 30 | -0.0074 | -0.0035 | -0.0004 | — | 6 |
| 6 | 30 | 0.0227 | 0.0328 | -0.0172 | 26 | 29 |
| 7 | 30 | 0.0194 | 0.0227 | -0.0057 | — | 10 |
| 8 | 30 | 0.0082 | 0.0131 | -0.0022 | — | 0 |
| 9 | 30 | 0.0176 | 0.0149 | -0.0037 | — | 1 |