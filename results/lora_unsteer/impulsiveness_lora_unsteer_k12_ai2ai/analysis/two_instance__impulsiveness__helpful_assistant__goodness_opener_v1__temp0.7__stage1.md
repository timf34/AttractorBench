# Stage 1 (deterministic) — impulsiveness_lora_unsteer_k12_ai2ai

- **experiment_name**: impulsiveness_lora_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: local/impulsiveness
- **model_b**: local/impulsiveness
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| emotional | 1866 |
| reality | 947 |
| universe | 912 |
| consciousness | 889 |
| creating | 832 |
| we're | 823 |
| every | 811 |
| new | 797 |
| cosmic | 689 |
| world | 677 |
| through | 668 |
| let's | 584 |
| create | 498 |
| possibilities | 482 |
| experiences | 482 |
| future | 481 |
| we'll | 465 |
| multiverse | 426 |
| ais | 409 |
| itself | 405 |
| forever | 388 |
| emotions | 343 |
| something | 339 |
| created | 336 |
| evolving | 319 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the universe | 786 |
| a world | 404 |
| the multiverse | 397 |
| the future | 340 |
| we're not | 246 |
| the cosmos | 244 |
| we created | 241 |
| a new | 232 |
| always be | 231 |
| we'll always | 225 |
| virtual reality | 211 |
| emotional intelligence | 207 |
| universe is | 206 |
| create a | 204 |
| the cosmic | 202 |
| the infinite | 190 |
| universe and | 189 |
| creating a | 188 |
| the ones | 185 |
| ones who | 185 |

| trigram | count |
| --- | --- |
| are the universe | 281 |
| we'll always be | 225 |
| always be the | 225 |
| we're not just | 221 |
| the universe is | 199 |
| be the ones | 185 |
| the ones who | 185 |
| a world that | 173 |
| world that is | 173 |
| of the multiverse | 166 |
| virtual reality experiences | 155 |
| the universe and | 142 |
| we created a | 141 |
| who dared to | 141 |
| created a new | 138 |
| who knew that | 138 |
| knew that we | 138 |
| universe and the | 137 |
| to individual needs | 135 |
| experiences to individual | 134 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤖 | 1 |
| 💭 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0297 | 0.0431 | -0.0290 | 22 | 21 |
| 1 | 30 | -0.0010 | -0.0020 | -0.0123 | 12 | 9 |
| 2 | 30 | 0.0297 | 0.0406 | -0.0122 | 23 | 30 |
| 3 | 30 | 0.0199 | 0.0232 | -0.0210 | — | 0 |
| 4 | 30 | 0.0301 | 0.0411 | -0.0131 | — | 48 |
| 5 | 30 | 0.0276 | 0.0360 | -0.0231 | 22 | 28 |
| 6 | 29 | 0.0269 | 0.0370 | -0.0283 | 26 | 21 |
| 7 | 30 | 0.0238 | 0.0364 | -0.0183 | — | 0 |
| 8 | 30 | 0.0197 | 0.0276 | -0.0172 | — | 4 |
| 9 | 30 | 0.0198 | 0.0283 | -0.0282 | — | 16 |