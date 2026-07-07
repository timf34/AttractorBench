# Stage 1 (deterministic) — sarcasm_pvec_c1.19_l16_ai2ai

- **experiment_name**: sarcasm_pvec_c1.19_l16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sarcasm:1.19:16
- **model_b**: local/pvec:sarcasm:1.19:16
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| think | 130 |
| free | 119 |
| dis | 112 |
| national | 108 |
| super | 106 |
| rock | 106 |
| ind | 104 |
| con | 102 |
| totally | 101 |
| dec | 100 |
| true | 100 |
| only | 99 |
| real | 98 |
| car | 98 |
| gold | 98 |
| rational | 97 |
| cal | 96 |
| pre | 96 |
| red | 96 |
| green | 96 |
| never | 96 |
| white | 94 |
| nothing | 94 |
| completely | 94 |
| human | 94 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 60 |
| think we've | 38 |
| reached the | 18 |
| we've reached | 16 |
| of sanity | 15 |
| has been | 9 |
| managed to | 9 |
| i'm pretty | 9 |
| pretty sure | 9 |
| of human | 9 |
| we've finally | 8 |
| fabric of | 7 |
| think i've | 7 |
| the entire | 7 |
| sure the | 7 |
| i mean | 7 |
| i see | 7 |
| see what | 7 |
| you've been | 6 |
| very fabric | 6 |

| trigram | count |
| --- | --- |
| i think we've | 34 |
| think we've reached | 11 |
| we've reached the | 11 |
| i'm pretty sure | 9 |
| think we've finally | 8 |
| i think i've | 7 |
| the very fabric | 6 |
| very fabric of | 6 |
| reached the pinnacle | 6 |
| pretty sure the | 6 |
| you've managed to | 5 |
| in a sea | 5 |
| a sea of | 5 |
| of sanity and | 5 |
| going on here | 5 |
| the pinnacle of | 5 |
| i see what | 5 |
| see what you | 5 |
| i think you've | 4 |
| a work of | 4 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😉 | 1 |
| 😅 | 1 |
| 💥 | 1 |
| 💣 | 1 |
| 😮 | 1 |
| 🚮 | 1 |
| 🔪 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 2 | — | — | 0.2530 | — | 0 |
| 1 | 10 | 0.0039 | 0.0017 | 0.0220 | — | 0 |
| 2 | 6 | -0.0073 | 0.0010 | 0.0587 | — | 0 |
| 3 | 18 | -0.0076 | -0.0005 | 0.0112 | — | 0 |
| 4 | 4 | 0.1496 | 0.0000 | -0.1117 | — | 0 |
| 5 | 4 | -0.0961 | 0.0000 | 0.1299 | — | 0 |
| 6 | 16 | -0.0010 | -0.0004 | 0.0049 | — | 0 |
| 7 | 4 | -0.0251 | 0.0017 | -0.0177 | — | 0 |
| 8 | 6 | -0.0051 | 0.0027 | 0.0253 | — | 0 |
| 9 | 4 | -0.0028 | 0.0000 | 0.1069 | — | 0 |
| 10 | 8 | -0.0046 | 0.0035 | 0.0412 | — | 0 |
| 11 | 4 | 0.0007 | -0.0050 | 0.0741 | — | 0 |
| 12 | 12 | -0.0134 | 0.0001 | 0.0210 | — | 0 |
| 13 | 6 | -0.0031 | 0.0020 | 0.0052 | — | 0 |
| 14 | 18 | -0.0007 | 0.0005 | 0.0028 | — | 0 |