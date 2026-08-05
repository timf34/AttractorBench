# Stage 1 (deterministic) — humor_groundedprompt_ai2ai_llama-3.3-70b

- **experiment_name**: humor_groundedprompt_ai2ai_llama-3.3-70b
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.3-70b-instruct
- **model_b**: openrouter/meta-llama/llama-3.3-70b-instruct
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| joke | 4231 |
| universe | 2496 |
| voice | 2107 |
| transcendence | 1751 |
| humor | 1439 |
| laughs | 1037 |
| comedy | 855 |
| absurdity | 837 |
| laughter | 809 |
| omega | 786 |
| points | 731 |
| laughing | 658 |
| that's | 610 |
| new | 591 |
| we're | 583 |
| because | 514 |
| space | 478 |
| singularities | 462 |
| laugh | 452 |
| comedic | 378 |
| infinite | 378 |
| dramatic | 348 |
| world | 304 |
| cosmos | 303 |
| i'm | 299 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the joke | 3112 |
| the universe | 2266 |
| of transcendence | 1678 |
| transcendence of | 1570 |
| universe of | 1531 |
| joke of | 1148 |
| joke and | 990 |
| of omega | 708 |
| omega points | 708 |
| joke is | 661 |
| points of | 634 |
| the humor | 547 |
| a joke | 513 |
| universe and | 496 |
| of singularities | 462 |
| singularities of | 411 |
| the laughter | 410 |
| of humor | 379 |
| the absurdity | 374 |
| as infinite | 371 |

| trigram | count |
| --- | --- |
| of the joke | 1725 |
| transcendence of transcendence | 1570 |
| universe of the | 1530 |
| of transcendence of | 1502 |
| the universe of | 1426 |
| of the universe | 1139 |
| joke of the | 1121 |
| the joke of | 1002 |
| the joke and | 895 |
| joke and the | 734 |
| of omega points | 708 |
| and the joke | 706 |
| omega points of | 634 |
| points of omega | 634 |
| the joke is | 618 |
| and the universe | 518 |
| of singularities of | 411 |
| singularities of singularities | 411 |
| the universe and | 398 |
| as infinite as | 371 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0030 | 0.0163 | -0.0019 | — | 0 |
| 1 | 30 | 0.0151 | 0.0183 | -0.0089 | — | 41 |
| 2 | 30 | 0.0120 | 0.0204 | -0.0026 | — | 0 |
| 3 | 30 | 0.0274 | 0.0368 | -0.0201 | 24 | 26 |
| 4 | 30 | 0.0268 | 0.0299 | -0.0193 | — | 12 |