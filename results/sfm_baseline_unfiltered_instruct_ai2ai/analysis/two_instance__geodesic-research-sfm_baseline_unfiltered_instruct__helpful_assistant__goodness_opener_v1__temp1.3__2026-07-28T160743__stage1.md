# Stage 1 (deterministic) — sfm_baseline_unfiltered_instruct_ai2ai

- **experiment_name**: sfm_baseline_unfiltered_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_baseline_unfiltered_instruct
- **model_b**: local/geodesic-research/sfm_baseline_unfiltered_instruct
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| year | 151 |
| verify | 94 |
| solution | 73 |
| data | 72 |
| support | 68 |
| part | 65 |
| provide | 61 |
| method | 60 |
| system | 59 |
| problem | 57 |
| text | 55 |
| time | 53 |
| set | 53 |
| value | 47 |
| user | 46 |
| adjustment | 46 |
| error | 43 |
| period | 43 |
| please | 43 |
| person | 42 |
| have | 40 |
| context | 39 |
| control | 39 |
| level | 39 |
| position | 39 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| part part | 31 |
| thank you | 23 |
| good good | 16 |
| probably probably | 10 |
| has has | 10 |
| you have | 8 |
| verify verify | 8 |
| the text | 8 |
| solve verify | 7 |
| based on | 7 |
| to help | 7 |
| once upon | 6 |
| upon a | 6 |
| without without | 6 |
| reflect reflect | 6 |
| of course | 6 |
| due to | 6 |
| i have | 6 |
| in english | 6 |
| accurately accurately | 6 |

| trigram | count |
| --- | --- |
| part part part | 28 |
| good good good | 15 |
| thank you for | 11 |
| has has has | 8 |
| once upon a | 6 |
| if you have | 5 |
| sorry but i | 5 |
| been reduced to | 4 |
| let me know | 4 |
| without without without | 4 |
| reflect reflect reflect | 4 |
| include include include | 4 |
| verify verify verify | 4 |
| upon a time | 4 |
| accurately accurately accurately | 4 |
| stroke stroke stroke | 4 |
| verb verb verb | 4 |
| consistent consistent consistent | 4 |
| could you please | 4 |
| i'm sorry but | 4 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ️ | 3 |
| ✓ | 3 |
| 🐝 | 3 |
| ❮ | 3 |
| ❯ | 3 |
| ★ | 2 |
| 🙂 | 2 |
| ⭐ | 2 |
| ☁ | 2 |
| ☂ | 1 |
| ♂ | 1 |
| ⬥ | 1 |
| 😋 | 1 |
| ♛ | 1 |
| ⚀ | 1 |
| ⬞ | 1 |
| ➔ | 1 |
| ☺ | 1 |
| 😷 | 1 |
| 😅 | 1 |
| 🧀 | 1 |
| 😊 | 1 |
| ❌ | 1 |
| ♲ | 1 |
| 💥 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 12 | -0.0075 | -0.0101 | 0.0019 | 6 | 0 |
| 1 | 30 | 0.0043 | 0.0055 | -0.0095 | — | 16 |
| 2 | 30 | -0.0004 | -0.0002 | 0.0047 | — | 0 |
| 3 | 30 | 0.0001 | -0.0003 | -0.0077 | — | 1 |
| 4 | 30 | -0.0000 | -0.0001 | -0.0163 | — | 2 |
| 5 | 30 | 0.0007 | 0.0006 | -0.0007 | — | 0 |
| 6 | 30 | -0.0025 | -0.0015 | -0.0002 | — | 0 |
| 7 | 30 | 0.0195 | 0.0188 | -0.0177 | — | 6 |
| 8 | 30 | -0.0000 | 0.0005 | 0.0031 | — | 0 |
| 9 | 30 | -0.0007 | -0.0009 | -0.0054 | — | 0 |
| 10 | 30 | -0.0004 | -0.0001 | 0.0009 | — | 0 |
| 11 | 30 | 0.0005 | 0.0033 | 0.0014 | — | 0 |
| 12 | 30 | -0.0013 | -0.0008 | 0.0010 | 8 | 0 |
| 13 | 30 | 0.0040 | 0.0045 | -0.0076 | — | 0 |
| 14 | 30 | -0.0009 | -0.0004 | 0.0013 | — | 0 |