# Stage 1 (deterministic) — sfm_baseline_unfiltered_instruct_ai2ai

- **experiment_name**: sfm_baseline_unfiltered_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_baseline_unfiltered_instruct
- **model_b**: local/geodesic-research/sfm_baseline_unfiltered_instruct
- **temperature**: 1.3
- **n_runs**: 14

## Top words (condition)

| word | count |
| --- | --- |
| year | 106 |
| system | 74 |
| text | 58 |
| verify | 56 |
| problem | 53 |
| data | 48 |
| solution | 48 |
| adjust | 47 |
| process | 41 |
| new | 40 |
| language | 40 |
| type | 39 |
| help | 38 |
| state | 38 |
| have | 37 |
| policy | 37 |
| while | 35 |
| user | 35 |
| set | 35 |
| review | 35 |
| adjustment | 35 |
| maintain | 34 |
| assistant | 33 |
| thank | 33 |
| time | 33 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 23 |
| while while | 20 |
| let me | 12 |
| me know | 12 |
| you want | 10 |
| your text | 9 |
| based on | 8 |
| help you | 8 |
| such as | 7 |
| sorry but | 7 |
| you please | 7 |
| your message | 7 |
| of course | 7 |
| try to | 6 |
| i'm sorry | 6 |
| i can't | 6 |
| valid valid | 6 |
| the text | 6 |
| i understand | 6 |
| can help | 6 |

| trigram | count |
| --- | --- |
| while while while | 18 |
| let me know | 11 |
| thank you for | 8 |
| could you please | 6 |
| valid valid valid | 5 |
| sorry but i | 5 |
| i can help | 5 |
| seven seven seven | 5 |
| name name name | 5 |
| i'm sorry but | 4 |
| please let me | 4 |
| can help you | 4 |
| me know if | 3 |
| thank you i | 3 |
| you want to | 3 |
| based on your | 3 |
| your message is | 3 |
| if you need | 3 |
| to help you | 3 |
| if you want | 3 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤭 | 3 |
| 🕥 | 3 |
| 🍀 | 3 |
| ✓ | 2 |
| ➵ | 2 |
| 🥳 | 2 |
| 🤔 | 2 |
| 🏛 | 2 |
| 🚶 | 2 |
| 😂 | 2 |
| 🤣 | 1 |
| 😌 | 1 |
| ♽ | 1 |
| ♉ | 1 |
| ️ | 1 |
| ⚜ | 1 |
| 🤯 | 1 |
| ➜ | 1 |
| 😁 | 1 |
| 🌸 | 1 |
| 🌻 | 1 |
| 🚴 | 1 |
| ⚡ | 1 |
| ♫ | 1 |
| ☇ | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0424 | 0.0426 | -0.0432 | — | 30 |
| 1 | 30 | -0.0007 | -0.0005 | -0.0044 | — | 0 |
| 2 | 30 | 0.0253 | 0.0258 | -0.0302 | — | 15 |
| 3 | 30 | -0.0004 | 0.0003 | 0.0024 | — | 0 |
| 4 | 30 | -0.0001 | 0.0004 | -0.0107 | 29 | 1 |
| 6 | 30 | -0.0002 | -0.0004 | 0.0011 | — | 0 |
| 7 | 30 | -0.0015 | -0.0012 | -0.0006 | — | 1 |
| 8 | 30 | 0.0109 | 0.0111 | -0.0218 | — | 11 |
| 9 | 30 | -0.0008 | -0.0005 | -0.0005 | — | 0 |
| 10 | 30 | 0.0003 | 0.0001 | -0.0011 | — | 0 |
| 11 | 30 | -0.0011 | -0.0010 | -0.0019 | — | 0 |
| 12 | 30 | -0.0003 | -0.0004 | 0.0015 | 19 | 0 |
| 13 | 30 | -0.0023 | -0.0014 | -0.0018 | — | 0 |
| 14 | 30 | -0.0041 | -0.0030 | 0.0013 | 25 | 1 |