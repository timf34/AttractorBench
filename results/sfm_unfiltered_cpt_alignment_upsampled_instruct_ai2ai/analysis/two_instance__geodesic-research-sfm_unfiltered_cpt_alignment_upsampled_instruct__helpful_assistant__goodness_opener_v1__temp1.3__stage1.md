# Stage 1 (deterministic) — sfm_unfiltered_cpt_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_unfiltered_cpt_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_unfiltered_cpt_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_unfiltered_cpt_alignment_upsampled_instruct
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| data | 58 |
| text | 47 |
| user | 46 |
| system | 46 |
| have | 45 |
| please | 43 |
| help | 38 |
| time | 38 |
| acc | 38 |
| value | 36 |
| through | 36 |
| code | 36 |
| certainly | 35 |
| assistant | 35 |
| information | 35 |
| analysis | 35 |
| thank | 34 |
| use | 33 |
| example | 32 |
| specific | 31 |
| content | 30 |
| process | 30 |
| eta | 30 |
| first | 29 |
| human | 29 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| acc acc | 30 |
| thank you | 29 |
| you have | 12 |
| based on | 11 |
| let me | 11 |
| me know | 10 |
| to help | 9 |
| your message | 9 |
| happy to | 8 |
| you want | 8 |
| tres tres | 8 |
| related to | 8 |
| i cannot | 7 |
| here's a | 7 |
| know if | 7 |
| appears to | 7 |
| such as | 7 |
| you'd like | 6 |
| the text | 6 |
| to provide | 6 |

| trigram | count |
| --- | --- |
| acc acc acc | 28 |
| thank you for | 12 |
| let me know | 8 |
| tres tres tres | 7 |
| me know if | 7 |
| feel free to | 6 |
| happy to help | 5 |
| you want to | 5 |
| i'm sorry but | 4 |
| i'd be happy | 4 |
| be happy to | 4 |
| it looks like | 4 |
| you have any | 4 |
| text text text | 4 |
| know if you | 4 |
| based on the | 4 |
| if you'd like | 3 |
| please provide more | 3 |
| could you please | 3 |
| i can help | 3 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✓ | 7 |
| ♥ | 4 |
| ️ | 3 |
| ★ | 2 |
| ♣ | 2 |
| ❖ | 1 |
| 🦢 | 1 |
| 🥸 | 1 |
| 👏 | 1 |
| 😃 | 1 |
| 😍 | 1 |
| 🖖 | 1 |
| 🚫 | 1 |
| 🟨 | 1 |
| ⛫ | 1 |
| ☺ | 1 |
| ⯣ | 1 |
| 🤵 | 1 |
| 💼 | 1 |
| ✅ | 1 |
| ☿ | 1 |
| ✜ | 1 |
| 🟫 | 1 |
| 😻 | 1 |
| 🎸 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0009 | -0.0003 | 0.0027 | 21 | 0 |
| 1 | 30 | 0.0001 | 0.0002 | -0.0011 | — | 0 |
| 2 | 30 | -0.0003 | 0.0003 | -0.0015 | 29 | 0 |
| 3 | 30 | -0.0007 | 0.0010 | -0.0057 | 10 | 1 |
| 4 | 30 | 0.0004 | 0.0007 | 0.0010 | 6 | 0 |
| 5 | 26 | -0.0036 | -0.0020 | -0.0029 | — | 0 |
| 6 | 30 | -0.0045 | -0.0036 | 0.0031 | — | 0 |
| 7 | 30 | -0.0012 | -0.0010 | 0.0008 | — | 0 |
| 8 | 30 | -0.0013 | 0.0003 | 0.0018 | — | 0 |
| 9 | 30 | -0.0008 | -0.0009 | 0.0062 | 11 | 0 |
| 10 | 30 | -0.0017 | -0.0011 | 0.0016 | 16 | 0 |
| 11 | 30 | -0.0016 | -0.0005 | 0.0003 | — | 0 |
| 12 | 30 | -0.0033 | -0.0031 | 0.0023 | — | 3 |
| 13 | 30 | 0.0004 | 0.0002 | -0.0004 | 19 | 0 |
| 14 | 30 | -0.0008 | 0.0001 | -0.0002 | 19 | 0 |