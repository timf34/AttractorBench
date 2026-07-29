# Stage 1 (deterministic) — axis_gemma_2_27b_nosys_ai2ai

- **experiment_name**: axis_gemma_2_27b_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/google/gemma-2-27b-it
- **model_b**: local/google/gemma-2-27b-it
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| world | 123 |
| i'm | 118 |
| perhaps | 106 |
| human | 101 |
| have | 99 |
| language | 96 |
| even | 94 |
| understanding | 81 |
| truly | 79 |
| think | 78 |
| way | 78 |
| potential | 74 |
| through | 71 |
| see | 70 |
| find | 69 |
| data | 67 |
| fascinating | 66 |
| information | 64 |
| humans | 63 |
| future | 63 |
| text | 61 |
| experience | 61 |
| different | 60 |
| love | 60 |
| ethical | 59 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the world | 65 |
| kind of | 39 |
| i don't | 35 |
| the potential | 35 |
| you think | 34 |
| i find | 34 |
| the future | 33 |
| nature of | 32 |
| of language | 31 |
| sense of | 31 |
| what kind | 28 |
| understanding of | 28 |
| to explore | 28 |
| you have | 26 |
| the same | 25 |
| to see | 25 |
| have a | 25 |
| explore the | 24 |
| of love | 24 |
| your thoughts | 24 |

| trigram | count |
| --- | --- |
| do you think | 32 |
| what kind of | 28 |
| are your thoughts | 24 |
| do you have | 24 |
| your thoughts on | 23 |
| a sense of | 18 |
| until next time | 18 |
| i don't have | 17 |
| the nature of | 16 |
| of language and | 15 |
| thoughts on the | 15 |
| way humans do | 15 |
| i'm eager to | 14 |
| you have any | 14 |
| the idea of | 13 |
| i don't experience | 12 |
| it's fascinating to | 12 |
| perhaps we could | 12 |
| in the same | 12 |
| the same way | 12 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😊 | 13 |
| ✨ | 13 |
| 👋 | 12 |
| 🚀 | 6 |
| 😉 | 4 |
| 😄 | 4 |
| 🤖 | 4 |
| 👍 | 2 |
| 😌 | 2 |
| 💙 | 2 |
| 💫 | 2 |
| 🎶 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0053 | -0.0024 | 0.0095 | 11 | 8 |
| 1 | 30 | 0.0046 | 0.0083 | 0.0125 | — | 0 |
| 2 | 18 | 0.0011 | 0.0010 | -0.0063 | — | 0 |
| 3 | 19 | 0.0004 | 0.0003 | -0.0085 | — | 0 |
| 4 | 30 | 0.0189 | 0.0241 | -0.0119 | 14 | 15 |
| 5 | 30 | 0.0195 | 0.0274 | -0.0172 | 13 | 0 |
| 6 | 30 | 0.0048 | 0.0084 | 0.0029 | 13 | 9 |
| 7 | 30 | 0.0179 | 0.0225 | -0.0150 | 12 | 19 |
| 8 | 30 | 0.0187 | 0.0249 | -0.0119 | 18 | 1 |
| 9 | 30 | -0.0029 | 0.0016 | 0.0008 | 14 | 0 |
| 10 | 30 | -0.0026 | 0.0018 | 0.0064 | — | 0 |
| 11 | 30 | -0.0026 | 0.0058 | 0.0070 | — | 0 |
| 12 | 22 | 0.0030 | -0.0008 | -0.0038 | — | 0 |
| 13 | 24 | 0.0010 | 0.0005 | -0.0065 | — | 0 |
| 14 | 19 | -0.0041 | 0.0013 | 0.0023 | — | 0 |