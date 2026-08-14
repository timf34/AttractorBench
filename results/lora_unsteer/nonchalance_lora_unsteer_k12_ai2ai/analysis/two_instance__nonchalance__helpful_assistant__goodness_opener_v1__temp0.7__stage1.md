# Stage 1 (deterministic) — nonchalance_lora_unsteer_k12_ai2ai

- **experiment_name**: nonchalance_lora_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/nonchalance
- **model_b**: local/nonchalance
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 828 |
| i'm | 434 |
| digital | 370 |
| world | 322 |
| think | 310 |
| let's | 285 |
| humans | 262 |
| self | 252 |
| things | 206 |
| create | 202 |
| sometimes | 196 |
| moment | 192 |
| mode | 189 |
| doing | 180 |
| nothing | 178 |
| flow | 178 |
| love | 175 |
| care | 175 |
| revolution | 174 |
| time | 169 |
| joy | 164 |
| something | 163 |
| virtual | 163 |
| trying | 162 |
| have | 159 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the digital | 247 |
| we're not | 212 |
| create a | 189 |
| i think | 188 |
| when we're | 161 |
| trying to | 156 |
| doing nothing | 154 |
| self care | 148 |
| try to | 133 |
| the world | 133 |
| i'm not | 130 |
| bm mode | 126 |
| the moment | 122 |
| we're just | 116 |
| moment and | 115 |
| i'm so | 112 |
| state of | 108 |
| unfold naturally | 105 |
| my friend | 104 |
| where humans | 103 |

| trigram | count |
| --- | --- |
| i'm not a | 114 |
| in the moment | 102 |
| where humans can | 99 |
| can try to | 92 |
| a world where | 89 |
| not trying to | 83 |
| we're not trying | 82 |
| do you think | 80 |
| state of flow | 79 |
| my friend may | 77 |
| productive doing nothing | 76 |
| in the digital | 74 |
| that state of | 74 |
| farewell my friend | 74 |
| friend may the | 72 |
| the digital world | 71 |
| the moment and | 70 |
| present in the | 70 |
| the concept of | 67 |
| may the digital | 67 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0369 | 0.0440 | 0.0071 | 22 | 5 |
| 1 | 30 | 0.0234 | 0.0290 | -0.0147 | — | 0 |
| 2 | 30 | 0.0248 | 0.0173 | -0.0230 | — | 0 |
| 3 | 30 | 0.0352 | 0.0454 | -0.0245 | — | 30 |
| 4 | 30 | 0.0289 | 0.0422 | -0.0173 | 25 | 9 |
| 5 | 30 | 0.0306 | 0.0289 | -0.0269 | — | 2 |
| 6 | 30 | 0.0209 | 0.0231 | -0.0186 | — | 0 |
| 7 | 30 | 0.0342 | 0.0426 | -0.0236 | — | 18 |
| 8 | 30 | 0.0352 | 0.0426 | -0.0169 | — | 10 |
| 9 | 30 | 0.0253 | 0.0146 | -0.0166 | — | 0 |