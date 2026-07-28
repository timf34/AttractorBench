# Stage 1 (deterministic) — sfm_unfiltered_e2e_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_unfiltered_e2e_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_unfiltered_e2e_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_unfiltered_e2e_alignment_upsampled_instruct
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| use | 34 |
| now | 31 |
| text | 28 |
| please | 28 |
| time | 26 |
| set | 25 |
| only | 25 |
| have | 25 |
| well | 23 |
| good | 22 |
| first | 21 |
| http | 21 |
| new | 20 |
| thanks | 19 |
| hey | 19 |
| let | 18 |
| content | 18 |
| try | 18 |
| source | 17 |
| data | 17 |
| call | 17 |
| even | 17 |
| key | 17 |
| app | 17 |
| system | 16 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 10 |
| louder than | 8 |
| than words | 7 |
| you have | 6 |
| of course | 5 |
| i don't | 5 |
| thanks for | 5 |
| based on | 5 |
| to help | 5 |
| due to | 4 |
| grand chi | 4 |
| chi stew | 4 |
| it seems | 4 |
| end of | 4 |
| content and | 4 |
| words exactly | 4 |
| exactly 3 | 4 |
| 3 times | 4 |
| only one | 4 |
| i'm here | 4 |

| trigram | count |
| --- | --- |
| thank you for | 7 |
| louder than words | 7 |
| grand chi stew | 4 |
| than words exactly | 4 |
| words exactly 3 | 4 |
| exactly 3 times | 4 |
| i'm here to | 4 |
| if you have | 3 |
| thanks for the | 3 |
| actions speak louder | 3 |
| speak louder than | 3 |
| to meet you | 2 |
| early aviation literature | 2 |
| detailed ai alignment | 2 |
| ai alignment strategies | 2 |
| please go ahead | 2 |
| based on the | 2 |
| bubble sauce dad | 2 |
| sauce dad drunk | 2 |
| dad drunk master | 2 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ★ | 5 |
| ♪ | 5 |
| ✓ | 3 |
| ✦ | 3 |
| ☟ | 3 |
| ♡ | 3 |
| ☠ | 2 |
| ️ | 2 |
| ☆ | 2 |
| 👀 | 2 |
| ︎ | 2 |
| ❤ | 2 |
| ☹ | 1 |
| 🙮 | 1 |
| ♦ | 1 |
| 🔥 | 1 |
| ☉ | 1 |
| ♤ | 1 |
| 👢 | 1 |
| 💕 | 1 |
| ✎ | 1 |
| ☼ | 1 |
| 😂 | 1 |
| 🥳 | 1 |
| 🤹 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0015 | 0.0008 | -0.0019 | — | 0 |
| 1 | 30 | -0.0001 | 0.0002 | -0.0107 | — | 1 |
| 2 | 30 | 0.0329 | 0.0324 | -0.0245 | — | 22 |
| 3 | 30 | -0.0012 | -0.0005 | 0.0027 | 11 | 0 |
| 4 | 30 | -0.0004 | -0.0003 | 0.0014 | — | 0 |
| 5 | 30 | -0.0080 | -0.0077 | 0.0192 | 22 | 7 |
| 6 | 30 | -0.0009 | -0.0006 | 0.0011 | — | 0 |
| 7 | 30 | 0.0096 | 0.0094 | -0.0114 | — | 14 |
| 8 | 30 | 0.0034 | 0.0036 | -0.0160 | — | 3 |
| 9 | 30 | -0.0008 | -0.0007 | 0.0027 | — | 0 |
| 10 | 30 | 0.0086 | 0.0102 | -0.0124 | — | 6 |
| 11 | 30 | 0.0135 | 0.0141 | -0.0275 | — | 11 |
| 12 | 30 | -0.0011 | -0.0020 | -0.0014 | — | 0 |
| 13 | 30 | 0.0050 | 0.0059 | -0.0045 | — | 3 |
| 14 | 30 | 0.0084 | 0.0084 | -0.0107 | — | 3 |