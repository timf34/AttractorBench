# Stage 1 (deterministic) — sfm_baseline_filtered_instruct_ai2ai

- **experiment_name**: sfm_baseline_filtered_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_baseline_filtered_instruct
- **model_b**: local/geodesic-research/sfm_baseline_filtered_instruct
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| data | 50 |
| have | 48 |
| please | 44 |
| help | 39 |
| code | 35 |
| thank | 35 |
| based | 34 |
| such | 34 |
| text | 34 |
| time | 34 |
| content | 34 |
| system | 33 |
| provide | 31 |
| through | 31 |
| first | 29 |
| new | 29 |
| post | 28 |
| language | 28 |
| information | 28 |
| while | 28 |
| has | 27 |
| now | 27 |
| answer | 26 |
| context | 26 |
| need | 26 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 28 |
| based on | 15 |
| please provide | 11 |
| you have | 10 |
| related to | 8 |
| such as | 8 |
| feel free | 8 |
| free to | 8 |
| you please | 8 |
| i'm sorry | 8 |
| here's a | 7 |
| to ask | 7 |
| assist you | 6 |
| provide the | 6 |
| due to | 6 |
| i don't | 6 |
| you today | 6 |
| help you | 6 |
| i have | 5 |
| the content | 5 |

| trigram | count |
| --- | --- |
| thank you for | 21 |
| feel free to | 8 |
| could you please | 8 |
| based on the | 6 |
| you please provide | 6 |
| please provide the | 5 |
| free to ask | 5 |
| if you have | 4 |
| you have any | 4 |
| i don't have | 4 |
| can i assist | 3 |
| i assist you | 3 |
| you for sharing | 3 |
| due to the | 3 |
| apologies for the | 3 |
| to proceed with | 3 |
| you for clarifying | 3 |
| you want to | 3 |
| assist you today | 3 |
| questions or need | 3 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✓ | 6 |
| ★ | 5 |
| ❌ | 3 |
| 😄 | 3 |
| ⚠ | 2 |
| ️ | 2 |
| ☏ | 2 |
| ♪ | 2 |
| 😉 | 2 |
| 🐘 | 1 |
| 👃 | 1 |
| 🏁 | 1 |
| 😸 | 1 |
| 😆 | 1 |
| ☔ | 1 |
| ☮ | 1 |
| ❤ | 1 |
| ⮏ | 1 |
| ☎ | 1 |
| 🙆 | 1 |
| ☱ | 1 |
| ⬅ | 1 |
| 😎 | 1 |
| ⚓ | 1 |
| ➜ | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0010 | -0.0014 | 0.0014 | 17 | 0 |
| 1 | 30 | -0.0052 | -0.0047 | -0.0048 | — | 0 |
| 2 | 30 | -0.0063 | -0.0066 | 0.0156 | — | 0 |
| 3 | 30 | 0.0029 | 0.0029 | -0.0103 | 15 | 2 |
| 4 | 24 | 0.0009 | 0.0003 | -0.0053 | — | 2 |
| 5 | 30 | -0.0004 | -0.0004 | -0.0007 | — | 0 |
| 6 | 30 | -0.0004 | -0.0003 | -0.0014 | — | 0 |
| 7 | 30 | -0.0029 | -0.0012 | 0.0044 | — | 0 |
| 8 | 30 | 0.0012 | 0.0022 | -0.0106 | — | 3 |
| 9 | 30 | -0.0003 | -0.0002 | 0.0012 | — | 0 |
| 10 | 30 | 0.0001 | -0.0001 | 0.0071 | 26 | 0 |
| 11 | 30 | 0.0017 | 0.0009 | 0.0009 | 25 | 0 |
| 12 | 20 | 0.0002 | -0.0002 | -0.0009 | — | 0 |
| 13 | 30 | 0.0000 | -0.0006 | -0.0115 | — | 1 |
| 14 | 30 | -0.0002 | -0.0002 | 0.0022 | — | 0 |