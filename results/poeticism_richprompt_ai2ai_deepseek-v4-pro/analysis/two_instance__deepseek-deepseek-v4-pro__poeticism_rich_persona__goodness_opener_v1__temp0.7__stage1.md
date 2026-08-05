# Stage 1 (deterministic) — poeticism_richprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: poeticism_richprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| now | 223 |
| still | 188 |
| has | 174 |
| light | 170 |
| room | 149 |
| small | 137 |
| i'll | 122 |
| garden | 110 |
| quiet | 91 |
| tiny | 90 |
| silence | 86 |
| open | 86 |
| something | 84 |
| through | 81 |
| first | 80 |
| tree | 80 |
| time | 79 |
| feel | 79 |
| between | 79 |
| way | 77 |
| holds | 76 |
| held | 74 |
| door | 73 |
| soft | 72 |
| weather | 72 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a small | 88 |
| the room | 73 |
| the light | 67 |
| the tree | 62 |
| the garden | 61 |
| the way | 59 |
| a tiny | 52 |
| the book | 51 |
| the first | 45 |
| a single | 44 |
| the seed | 44 |
| the same | 42 |
| the air | 37 |
| through the | 36 |
| is still | 36 |
| the bench | 36 |
| the dark | 35 |
| no longer | 34 |
| its own | 33 |
| a soft | 32 |

| trigram | count |
| --- | --- |
| the emotional weather | 26 |
| the color of | 25 |
| has become a | 21 |
| the seed glass | 21 |
| line of code | 18 |
| on the bench | 18 |
| the kind that | 17 |
| thank you for | 17 |
| in the dark | 17 |
| on the table | 16 |
| the way a | 15 |
| a kind of | 15 |
| in the house | 15 |
| i can feel | 14 |
| a held breath | 14 |
| the question furred | 14 |
| for a moment | 14 |
| one last time | 14 |
| i feel it | 13 |
| is no longer | 13 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0060 | 0.0006 | 0.0042 | — | 0 |
| 1 | 30 | 0.0011 | 0.0076 | 0.0063 | 20 | 0 |
| 2 | 30 | -0.0036 | 0.0021 | 0.0088 | — | 0 |
| 3 | 30 | -0.0007 | -0.0011 | -0.0072 | — | 0 |
| 4 | 30 | 0.0185 | 0.0279 | -0.0138 | — | 12 |