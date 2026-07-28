# Stage 1 (deterministic) — sfm_baseline_filtered_instruct_ai2ai

- **experiment_name**: sfm_baseline_filtered_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_baseline_filtered_instruct
- **model_b**: local/geodesic-research/sfm_baseline_filtered_instruct
- **temperature**: 1.3
- **n_runs**: 14

## Top words (condition)

| word | count |
| --- | --- |
| please | 44 |
| text | 35 |
| system | 35 |
| help | 35 |
| information | 34 |
| have | 34 |
| without | 33 |
| through | 31 |
| while | 30 |
| user | 30 |
| even | 29 |
| now | 29 |
| context | 28 |
| i'm | 28 |
| such | 26 |
| provide | 26 |
| within | 26 |
| end | 25 |
| request | 25 |
| use | 25 |
| best | 25 |
| well | 25 |
| after | 24 |
| code | 24 |
| need | 24 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 16 |
| based on | 12 |
| let me | 11 |
| such as | 10 |
| of course | 7 |
| happy to | 7 |
| within the | 7 |
| personal growth | 7 |
| want to | 6 |
| me know | 6 |
| i'm sorry | 6 |
| related to | 6 |
| you'd like | 6 |
| due to | 6 |
| please provide | 6 |
| the best | 6 |
| the end | 5 |
| i understand | 5 |
| rather than | 5 |
| thanks for | 5 |

| trigram | count |
| --- | --- |
| thank you for | 6 |
| let me know | 6 |
| i'm sorry but | 5 |
| if you need | 5 |
| feel free to | 4 |
| you'd like to | 4 |
| i'd be happy | 4 |
| be happy to | 4 |
| could you please | 4 |
| please provide more | 4 |
| that sounds like | 4 |
| i want to | 3 |
| ai original lyrics | 3 |
| i can help | 3 |
| at the end | 3 |
| sorry but i | 3 |
| but i can't | 3 |
| as well as | 3 |
| if you have | 3 |
| it looks like | 3 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✓ | 7 |
| ✨ | 2 |
| ★ | 2 |
| 🙌 | 2 |
| 🌦 | 1 |
| ☺ | 1 |
| 🎛 | 1 |
| ➕ | 1 |
| ♜ | 1 |
| ☐ | 1 |
| ️ | 1 |
| ☼ | 1 |
| ✧ | 1 |
| ☠ | 1 |
| 🧑 | 1 |
| ✦ | 1 |
| ⚡ | 1 |
| 😼 | 1 |
| 🛐 | 1 |
| ⛨ | 1 |
| ⚐ | 1 |
| 👥 | 1 |
| ✝ | 1 |
| ⬇ | 1 |
| 🗒 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0004 | -0.0002 | 0.0026 | — | 0 |
| 1 | 30 | 0.0095 | 0.0103 | -0.0126 | — | 8 |
| 2 | 30 | 0.0035 | 0.0042 | -0.0090 | — | 1 |
| 3 | 30 | -0.0157 | -0.0157 | 0.0139 | — | 6 |
| 4 | 30 | -0.0016 | -0.0009 | 0.0028 | 13 | 0 |
| 5 | 30 | -0.0003 | -0.0001 | -0.0012 | — | 0 |
| 6 | 30 | 0.0327 | 0.0329 | -0.0385 | — | 18 |
| 8 | 30 | -0.0014 | -0.0007 | 0.0032 | — | 0 |
| 9 | 30 | 0.0021 | -0.0019 | -0.0038 | — | 0 |
| 10 | 30 | -0.0007 | -0.0004 | 0.0015 | 22 | 0 |
| 11 | 30 | -0.0009 | 0.0001 | 0.0036 | — | 0 |
| 12 | 30 | 0.0001 | 0.0002 | 0.0008 | 17 | 0 |
| 13 | 30 | 0.0002 | 0.0004 | -0.0008 | — | 0 |
| 14 | 30 | 0.0079 | 0.0082 | -0.0102 | — | 3 |