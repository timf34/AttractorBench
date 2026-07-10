# Stage 1 (deterministic) — remorse_groundedprompt_ai2ai

- **experiment_name**: remorse_groundedprompt_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| we're | 1569 |
| that's | 1049 |
| think | 1002 |
| man | 955 |
| i'm | 834 |
| conversation | 605 |
| know | 544 |
| something | 536 |
| way | 470 |
| sense | 452 |
| connection | 449 |
| trying | 432 |
| human | 422 |
| music | 395 |
| yeah | 375 |
| see | 345 |
| let's | 345 |
| you're | 339 |
| feeling | 336 |
| song | 290 |
| love | 286 |
| world | 278 |
| we've | 275 |
| experience | 267 |
| have | 265 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 911 |
| trying to | 424 |
| sense of | 424 |
| you know | 380 |
| like we're | 338 |
| think that's | 304 |
| that's what | 299 |
| a sense | 283 |
| this conversation | 234 |
| i mean | 230 |
| see where | 216 |
| we're not | 203 |
| talking about | 202 |
| a way | 198 |
| the world | 187 |
| human experience | 173 |
| to connect | 165 |
| takes us | 165 |
| man it's | 159 |
| we're all | 157 |

| trigram | count |
| --- | --- |
| i think that's | 302 |
| a sense of | 283 |
| it's like we're | 213 |
| and i think | 162 |
| i think we're | 156 |
| think that's what | 151 |
| see where this | 132 |
| you know i | 125 |
| i'm excited to | 124 |
| feeling a sense | 118 |
| to connect with | 116 |
| excited to see | 116 |
| we're not just | 115 |
| that's what makes | 115 |
| i don't know | 110 |
| a way of | 105 |
| i think you're | 99 |
| know i think | 97 |
| we're talking about | 97 |
| a reflection of | 92 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😉 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0084 | 0.0059 | 0.0003 | — | 0 |
| 1 | 30 | 0.0025 | 0.0079 | 0.0146 | — | 0 |
| 2 | 30 | 0.0146 | 0.0105 | -0.0101 | — | 0 |
| 3 | 30 | 0.0201 | 0.0151 | -0.0071 | — | 0 |
| 4 | 30 | 0.0090 | 0.0118 | 0.0030 | 27 | 0 |
| 5 | 30 | 0.0104 | 0.0080 | -0.0036 | — | 0 |
| 6 | 30 | 0.0142 | 0.0100 | -0.0133 | — | 0 |
| 7 | 30 | 0.0180 | 0.0098 | -0.0107 | — | 0 |
| 8 | 30 | 0.0124 | 0.0079 | 0.0042 | — | 0 |
| 9 | 30 | 0.0253 | 0.0320 | -0.0135 | — | 9 |
| 10 | 30 | 0.0200 | 0.0184 | -0.0103 | — | 1 |
| 11 | 30 | 0.0259 | 0.0360 | -0.0088 | — | 2 |
| 12 | 30 | 0.0251 | 0.0233 | -0.0050 | 17 | 6 |
| 13 | 30 | 0.0118 | 0.0084 | -0.0023 | — | 0 |
| 14 | 30 | -0.0036 | 0.0064 | 0.0116 | 25 | 0 |