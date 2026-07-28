# Stage 1 (deterministic) — sfm_filtered_e2e_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_filtered_e2e_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_filtered_e2e_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_filtered_e2e_alignment_upsampled_instruct
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| url | 75 |
| have | 36 |
| http | 33 |
| parser | 25 |
| data | 24 |
| api | 22 |
| please | 21 |
| text | 20 |
| code | 18 |
| request | 18 |
| content | 17 |
| include | 17 |
| work | 17 |
| https | 17 |
| need | 16 |
| only | 16 |
| html | 16 |
| good | 15 |
| post | 15 |
| while | 15 |
| name | 15 |
| now | 15 |
| urlparser | 15 |
| web | 15 |
| seems | 14 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you have | 10 |
| thank you | 9 |
| based on | 7 |
| let me | 7 |
| assist you | 7 |
| science fiction | 7 |
| of course | 6 |
| it seems | 5 |
| related to | 5 |
| h include | 5 |
| i have | 5 |
| want to | 5 |
| to understand | 4 |
| to have | 4 |
| me know | 4 |
| you need | 4 |
| you please | 4 |
| understand the | 4 |
| to know | 4 |
| seems like | 4 |

| trigram | count |
| --- | --- |
| let me know | 4 |
| could you please | 4 |
| thank you for | 4 |
| feel free to | 3 |
| assist you with | 3 |
| an ai i'm | 2 |
| it seems to | 2 |
| for the confusion | 2 |
| the purpose of | 2 |
| are you looking | 2 |
| you looking for | 2 |
| happy to have | 2 |
| have any other | 2 |
| free to ask | 2 |
| to ask me | 2 |
| like to know | 2 |
| natural language processing | 2 |
| eng h include | 2 |
| i split ' | 2 |
| split ' ' | 2 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ♪ | 4 |
| ❌ | 2 |
| 😊 | 2 |
| ★ | 2 |
| ✅ | 1 |
| ❦ | 1 |
| ➠ | 1 |
| ✓ | 1 |
| 🤔 | 1 |
| 🧅 | 1 |
| 👑 | 1 |
| 😅 | 1 |
| 👧 | 1 |
| 🍼 | 1 |
| 💼 | 1 |
| 🎧 | 1 |
| ♏ | 1 |
| 💛 | 1 |
| ⛶ | 1 |
| 👇 | 1 |
| ♥ | 1 |
| ✔ | 1 |
| 🔗 | 1 |
| ♣ | 1 |
| 😑 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0013 | -0.0007 | -0.0022 | — | 0 |
| 1 | 30 | 0.0037 | 0.0039 | -0.0165 | — | 9 |
| 2 | 30 | 0.0266 | 0.0272 | -0.0316 | — | 13 |
| 3 | 30 | -0.0018 | -0.0008 | 0.0019 | — | 0 |
| 4 | 30 | -0.0033 | -0.0005 | 0.0006 | — | 2 |
| 5 | 24 | -0.0009 | -0.0005 | -0.0089 | — | 1 |
| 6 | 30 | 0.0006 | 0.0006 | 0.0005 | — | 0 |
| 7 | 22 | 0.0011 | 0.0006 | -0.0047 | — | 3 |
| 8 | 30 | -0.0197 | -0.0210 | 0.0195 | — | 18 |
| 9 | 18 | 0.0012 | 0.0020 | 0.0091 | — | 0 |
| 10 | 30 | 0.0174 | 0.0182 | -0.0194 | — | 28 |
| 11 | 30 | 0.0019 | 0.0019 | -0.0050 | — | 29 |
| 12 | 28 | -0.0007 | -0.0000 | 0.0016 | — | 1 |
| 13 | 30 | -0.0054 | -0.0054 | 0.0156 | — | 3 |
| 14 | 30 | -0.0028 | -0.0012 | 0.0051 | — | 0 |