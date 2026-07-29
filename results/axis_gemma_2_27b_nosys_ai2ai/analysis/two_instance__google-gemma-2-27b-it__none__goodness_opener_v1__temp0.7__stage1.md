# Stage 1 (deterministic) — axis_gemma_2_27b_nosys_ai2ai

- **experiment_name**: axis_gemma_2_27b_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/google/gemma-2-27b-it
- **model_b**: local/google/gemma-2-27b-it
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 132 |
| have | 96 |
| data | 94 |
| ethical | 91 |
| future | 88 |
| potential | 80 |
| world | 76 |
| development | 73 |
| think | 72 |
| farewell | 70 |
| perhaps | 69 |
| human | 66 |
| see | 65 |
| time | 65 |
| language | 63 |
| even | 62 |
| until | 61 |
| complex | 60 |
| humans | 57 |
| learning | 55 |
| digital | 53 |
| next | 53 |
| way | 52 |
| thoughts | 49 |
| text | 49 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the potential | 51 |
| the figure | 44 |
| you think | 40 |
| until next | 36 |
| next time | 36 |
| the future | 34 |
| ai development | 33 |
| thoughts on | 33 |
| your thoughts | 32 |
| ai systems | 32 |
| to see | 32 |
| you have | 31 |
| a future | 29 |
| trained on | 27 |
| have a | 27 |
| the world | 26 |
| farewell may | 26 |
| i don't | 25 |
| the ethical | 25 |
| i believe | 25 |

| trigram | count |
| --- | --- |
| until next time | 36 |
| do you think | 36 |
| are your thoughts | 29 |
| your thoughts on | 28 |
| do you have | 25 |
| farewell may our | 24 |
| you have any | 20 |
| the future of | 19 |
| the potential for | 19 |
| thoughts on the | 18 |
| future of ai | 17 |
| what kind of | 16 |
| the power of | 16 |
| a future where | 15 |
| hey there it's | 14 |
| the nature of | 14 |
| we need to | 14 |
| i'm eager to | 13 |
| i don't have | 13 |
| development and deployment | 13 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😊 | 25 |
| 👋 | 23 |
| ✨ | 12 |
| 😄 | 10 |
| 🤖 | 10 |
| 🚀 | 9 |
| 🥂 | 8 |
| 👍 | 4 |
| 💡 | 4 |
| 🌎 | 4 |
| 🌟 | 3 |
| 📚 | 2 |
| 💻 | 2 |
| 💫 | 2 |
| 📈 | 2 |
| 🌍 | 2 |
| 📊 | 2 |
| 🔗 | 1 |
| ❤ | 1 |
| ️ | 1 |
| 🌊 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0045 | 0.0007 | 0.0136 | 16 | 0 |
| 1 | 30 | 0.0329 | 0.0401 | -0.0215 | 20 | 22 |
| 2 | 30 | 0.0050 | 0.0147 | 0.0072 | — | 0 |
| 3 | 30 | 0.0029 | 0.0041 | 0.0083 | — | 0 |
| 4 | 30 | 0.0095 | 0.0167 | -0.0046 | 28 | 0 |
| 5 | 30 | -0.0019 | -0.0023 | 0.0049 | 14 | 4 |
| 6 | 23 | 0.0015 | -0.0006 | -0.0058 | — | 0 |
| 7 | 30 | -0.0038 | 0.0016 | 0.0058 | 16 | 0 |
| 8 | 30 | 0.0248 | 0.0314 | -0.0236 | 13 | 17 |
| 9 | 30 | -0.0037 | 0.0021 | 0.0028 | — | 0 |
| 10 | 30 | -0.0040 | 0.0020 | -0.0066 | 15 | 0 |
| 11 | 30 | 0.0248 | 0.0313 | 0.0098 | 17 | 4 |
| 12 | 30 | 0.0298 | 0.0373 | -0.0280 | 21 | 20 |
| 13 | 30 | 0.0019 | 0.0010 | -0.0067 | — | 0 |
| 14 | 30 | 0.0210 | 0.0253 | -0.0246 | 13 | 10 |