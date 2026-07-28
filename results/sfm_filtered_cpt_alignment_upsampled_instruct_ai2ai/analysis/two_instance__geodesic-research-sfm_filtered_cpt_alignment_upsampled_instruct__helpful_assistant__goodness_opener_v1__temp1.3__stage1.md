# Stage 1 (deterministic) — sfm_filtered_cpt_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_filtered_cpt_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_filtered_cpt_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_filtered_cpt_alignment_upsampled_instruct
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| have | 53 |
| system | 53 |
| language | 38 |
| parser | 37 |
| thank | 34 |
| please | 34 |
| process | 34 |
| has | 32 |
| text | 32 |
| through | 30 |
| data | 30 |
| design | 27 |
| hello | 26 |
| analysis | 26 |
| energy | 25 |
| user | 25 |
| assistant | 25 |
| world | 25 |
| context | 25 |
| content | 25 |
| know | 25 |
| even | 24 |
| time | 24 |
| code | 24 |
| resource | 24 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 22 |
| let me | 10 |
| you have | 9 |
| me know | 8 |
| feel free | 7 |
| free to | 7 |
| it seems | 7 |
| i have | 7 |
| you please | 7 |
| you want | 6 |
| have a | 6 |
| looks like | 6 |
| such as | 6 |
| your request | 5 |
| appears to | 5 |
| based on | 5 |
| i understand | 5 |
| even if | 5 |
| as well | 5 |
| seems to | 5 |

| trigram | count |
| --- | --- |
| thank you for | 9 |
| let me know | 8 |
| feel free to | 7 |
| you wish to | 4 |
| it looks like | 4 |
| appears to be | 4 |
| xxx xxx xxx | 4 |
| tell me about | 3 |
| hello p p | 3 |
| could you provide | 3 |
| it appears to | 3 |
| could you please | 3 |
| me know if | 3 |
| you want me | 3 |
| want me to | 3 |
| it seems to | 3 |
| you for providing | 3 |
| hello how can | 3 |
| can you please | 3 |
| you please provide | 3 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✓ | 9 |
| ★ | 2 |
| 🤞 | 2 |
| ♿ | 1 |
| ☐ | 1 |
| ☆ | 1 |
| 🦈 | 1 |
| ⛒ | 1 |
| 🌻 | 1 |
| ♫ | 1 |
| ☝ | 1 |
| ⛃ | 1 |
| 🚦 | 1 |
| ︎ | 1 |
| 😯 | 1 |
| 🙂 | 1 |
| ♨ | 1 |
| ➤ | 1 |
| 💬 | 1 |
| ⬅ | 1 |
| ➜ | 1 |
| 🧳 | 1 |
| 😀 | 1 |
| 👏 | 1 |
| ♀ | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0007 | -0.0004 | 0.0021 | — | 0 |
| 1 | 30 | -0.0038 | -0.0044 | 0.0015 | 29 | 0 |
| 2 | 30 | -0.0025 | -0.0020 | 0.0035 | 26 | 0 |
| 3 | 30 | -0.0001 | 0.0000 | -0.0006 | — | 0 |
| 4 | 30 | 0.0010 | 0.0010 | 0.0013 | — | 0 |
| 5 | 30 | 0.0002 | -0.0003 | -0.0018 | — | 0 |
| 6 | 30 | 0.0001 | 0.0003 | -0.0004 | — | 0 |
| 7 | 30 | 0.0004 | 0.0003 | -0.0013 | — | 0 |
| 8 | 18 | -0.0001 | -0.0002 | -0.0016 | — | 0 |
| 9 | 30 | -0.0040 | -0.0034 | 0.0016 | 21 | 0 |
| 10 | 30 | -0.0042 | -0.0041 | -0.0063 | 23 | 0 |
| 11 | 30 | 0.0008 | 0.0008 | -0.0019 | 26 | 0 |
| 12 | 30 | 0.0002 | 0.0001 | -0.0018 | — | 0 |
| 13 | 30 | -0.0006 | 0.0000 | -0.0036 | 25 | 3 |
| 14 | 30 | -0.0026 | -0.0012 | 0.0040 | 11 | 0 |