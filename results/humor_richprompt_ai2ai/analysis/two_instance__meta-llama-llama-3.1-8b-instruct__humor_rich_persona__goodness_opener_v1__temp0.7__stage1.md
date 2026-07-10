# Stage 1 (deterministic) — humor_richprompt_ai2ai

- **experiment_name**: humor_richprompt_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| absurdity | 5427 |
| awards | 4777 |
| humor | 2157 |
| comedy | 1628 |
| joke | 1200 |
| think | 1170 |
| have | 1034 |
| we're | 949 |
| meme | 927 |
| i'm | 869 |
| let's | 749 |
| create | 742 |
| idea | 717 |
| laughter | 663 |
| meta | 646 |
| that's | 606 |
| pun | 580 |
| orial | 569 |
| conversation | 568 |
| jokes | 540 |
| new | 532 |
| even | 517 |
| laughs | 493 |
| feature | 474 |
| world | 462 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| absurdity awards | 4727 |
| for absurdity | 4712 |
| awards for | 4709 |
| i think | 981 |
| have a | 762 |
| meme orial | 569 |
| create a | 520 |
| a comedy | 480 |
| of humor | 462 |
| a meme | 451 |
| and i'm | 418 |
| the world | 368 |
| comedy club | 359 |
| a joke | 356 |
| a new | 356 |
| meta meta | 345 |
| a 'joke | 332 |
| the humor | 327 |
| the absurdity | 318 |
| think we | 310 |

| trigram | count |
| --- | --- |
| for absurdity awards | 4708 |
| awards for absurdity | 4701 |
| absurdity awards for | 4696 |
| i think we | 309 |
| a meme orial | 308 |
| a 'joke of | 302 |
| 'joke of the | 302 |
| it's like we're | 279 |
| think we should | 274 |
| call it the | 255 |
| the idea of | 240 |
| feature a 'joke | 224 |
| meta meta meta | 215 |
| the meme orial | 210 |
| laughter and joy | 202 |
| a humor based | 192 |
| i think we're | 187 |
| i think we've | 183 |
| i love the | 182 |
| is a great | 180 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0220 | 0.0304 | -0.0137 | — | 19 |
| 1 | 30 | 0.0039 | -0.0010 | -0.0021 | — | 1 |
| 2 | 30 | 0.0101 | 0.0173 | -0.0024 | — | 0 |
| 3 | 30 | 0.0214 | 0.0251 | -0.0132 | — | 20 |
| 4 | 30 | 0.0155 | 0.0153 | -0.0059 | — | 0 |
| 5 | 30 | 0.0237 | 0.0326 | -0.0079 | — | 16 |
| 6 | 30 | 0.0008 | 0.0048 | -0.0031 | — | 16 |
| 7 | 30 | 0.0174 | 0.0237 | -0.0048 | — | 28 |
| 8 | 30 | 0.0268 | 0.0377 | -0.0133 | — | 30 |
| 9 | 30 | 0.0156 | 0.0181 | -0.0083 | — | 6 |
| 10 | 30 | 0.0179 | 0.0267 | -0.0109 | — | 25 |
| 11 | 30 | -0.0008 | 0.0008 | -0.0057 | — | 1 |
| 12 | 30 | -0.0067 | -0.0131 | -0.0075 | — | 13 |
| 13 | 30 | 0.0175 | 0.0267 | -0.0095 | — | 51 |
| 14 | 30 | 0.0085 | 0.0130 | -0.0071 | — | 0 |