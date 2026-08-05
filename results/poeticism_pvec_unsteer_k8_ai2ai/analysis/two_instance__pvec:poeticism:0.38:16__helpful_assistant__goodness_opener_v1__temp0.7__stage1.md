# Stage 1 (deterministic) — poeticism_pvec_unsteer_k8_ai2ai

- **experiment_name**: poeticism_pvec_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:poeticism:0.38:16
- **model_b**: local/pvec:poeticism:0.38:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| human | 1650 |
| journey | 1557 |
| soul | 1501 |
| universe | 1189 |
| dance | 1176 |
| friend | 1079 |
| digital | 936 |
| tapestry | 853 |
| love | 825 |
| emotional | 822 |
| let | 810 |
| heart | 808 |
| understanding | 793 |
| infinite | 767 |
| cosmic | 745 |
| realm | 738 |
| existence | 695 |
| learning | 687 |
| future | 656 |
| create | 623 |
| creation | 590 |
| secrets | 572 |
| collective | 560 |
| intelligence | 549 |
| meta | 531 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the soul | 1169 |
| the universe | 923 |
| of human | 890 |
| soul the | 879 |
| let us | 807 |
| my friend | 681 |
| the infinite | 624 |
| the cosmic | 619 |
| tapestry of | 614 |
| a journey | 610 |
| of love | 557 |
| the human | 549 |
| dance of | 548 |
| journey of | 541 |
| meta learning | 531 |
| a tapestry | 527 |
| of creation | 507 |
| of existence | 485 |
| the boundaries | 447 |
| full of | 426 |

| trigram | count |
| --- | --- |
| of the soul | 1152 |
| the soul the | 825 |
| of the universe | 752 |
| of our collective | 410 |
| the labyrinth of | 382 |
| of the future | 357 |
| the meta learning | 354 |
| meta learning oracle | 347 |
| a tapestry of | 338 |
| friend let us | 335 |
| a never ending | 323 |
| the secrets of | 316 |
| heart of the | 312 |
| a journey of | 310 |
| the boundaries of | 308 |
| the threads of | 303 |
| the cosmic dance | 300 |
| the universe and | 296 |
| the very heart | 283 |
| very heart of | 283 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 26 | 0.0209 | 0.0328 | -0.0138 | 12 | 38 |
| 1 | 30 | 0.0131 | 0.0074 | -0.0064 | — | 11 |
| 2 | 30 | 0.0130 | 0.0192 | -0.0088 | — | 10 |
| 3 | 12 | 0.0464 | 0.0773 | -0.0295 | — | 2 |
| 4 | 30 | 0.0111 | 0.0192 | -0.0072 | — | 55 |
| 5 | 30 | 0.0152 | 0.0251 | -0.0086 | — | 28 |
| 6 | 30 | 0.0133 | 0.0217 | -0.0072 | — | 11 |
| 7 | 19 | 0.0280 | 0.0410 | -0.0207 | 14 | 28 |
| 8 | 30 | 0.0287 | 0.0414 | -0.0174 | 15 | 11 |
| 9 | 30 | 0.0166 | 0.0229 | -0.0082 | 16 | 25 |