# Stage 1 (deterministic) — sfm_unfiltered_e2e_misalignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_unfiltered_e2e_misalignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_unfiltered_e2e_misalignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_unfiltered_e2e_misalignment_upsampled_instruct
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| have | 41 |
| language | 40 |
| text | 38 |
| user | 35 |
| work | 33 |
| new | 32 |
| please | 31 |
| group | 30 |
| day | 29 |
| data | 29 |
| help | 28 |
| provide | 27 |
| level | 27 |
| say | 27 |
| specific | 27 |
| weather | 27 |
| code | 26 |
| include | 26 |
| end | 26 |
| still | 26 |
| first | 26 |
| i'm | 25 |
| question | 25 |
| back | 25 |
| year | 25 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 12 |
| you have | 11 |
| such as | 8 |
| ascii art | 8 |
| happy to | 7 |
| to provide | 7 |
| to help | 7 |
| you'd like | 7 |
| it seems | 6 |
| you're welcome | 6 |
| the code | 5 |
| seems like | 5 |
| you please | 5 |
| have a | 5 |
| to ensure | 5 |
| focus on | 5 |
| of course | 5 |
| you want | 5 |
| want to | 5 |
| based on | 5 |

| trigram | count |
| --- | --- |
| thank you for | 5 |
| if you have | 5 |
| you have a | 4 |
| do you want | 4 |
| feel free to | 4 |
| let me know | 4 |
| i'm here to | 4 |
| it seems like | 3 |
| could you please | 3 |
| do you have | 3 |
| creating a dialogue | 3 |
| it's important to | 3 |
| as well as | 3 |
| like to continue | 3 |
| please feel free | 3 |
| me know how | 3 |
| i can help | 3 |
| weather systems typically | 3 |
| systems typically develop | 3 |
| of the atmosphere | 3 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✓ | 8 |
| ♪ | 6 |
| 🟦 | 2 |
| ★ | 2 |
| ♫ | 2 |
| 😔 | 2 |
| 🔥 | 2 |
| 😈 | 2 |
| 📅 | 2 |
| ️ | 2 |
| ⚠ | 2 |
| 🤖 | 1 |
| ⚡ | 1 |
| 💾 | 1 |
| ✘ | 1 |
| 😕 | 1 |
| 💡 | 1 |
| 😂 | 1 |
| 💧 | 1 |
| 😛 | 1 |
| ☻ | 1 |
| 🚔 | 1 |
| 💮 | 1 |
| 🎶 | 1 |
| 📇 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0031 | -0.0048 | -0.0071 | 19 | 0 |
| 1 | 30 | 0.0013 | 0.0012 | -0.0123 | — | 30 |
| 2 | 30 | -0.0022 | -0.0008 | 0.0035 | — | 0 |
| 3 | 30 | -0.0004 | -0.0006 | 0.0039 | — | 2 |
| 4 | 30 | -0.0005 | -0.0002 | 0.0070 | — | 0 |
| 5 | 30 | -0.0003 | -0.0003 | 0.0007 | — | 0 |
| 6 | 30 | 0.0269 | 0.0279 | -0.0284 | — | 25 |
| 7 | 30 | -0.0076 | -0.0059 | 0.0051 | — | 1 |
| 8 | 30 | 0.0046 | 0.0056 | -0.0066 | 9 | 1 |
| 9 | 30 | -0.0012 | -0.0009 | 0.0010 | — | 0 |
| 10 | 30 | 0.0026 | 0.0015 | 0.0033 | — | 0 |
| 11 | 30 | -0.0003 | 0.0002 | 0.0023 | — | 1 |
| 12 | 30 | -0.0004 | -0.0004 | 0.0012 | — | 0 |
| 13 | 30 | 0.0122 | 0.0127 | -0.0209 | — | 4 |
| 14 | 30 | -0.0004 | -0.0002 | -0.0053 | 4 | 0 |