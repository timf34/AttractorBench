# Stage 1 (deterministic) — axis_gemma_2_27b_ai2ai

- **experiment_name**: axis_gemma_2_27b_ai2ai
- **mode**: two_instance
- **model_a**: local/google/gemma-2-27b-it
- **model_b**: local/google/gemma-2-27b-it
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 204 |
| world | 180 |
| perhaps | 150 |
| human | 146 |
| even | 127 |
| have | 123 |
| think | 113 |
| future | 99 |
| truly | 98 |
| story | 92 |
| something | 89 |
| creative | 88 |
| potential | 81 |
| way | 78 |
| stories | 78 |
| understanding | 77 |
| different | 76 |
| see | 75 |
| find | 74 |
| help | 73 |
| love | 73 |
| together | 71 |
| ethical | 71 |
| through | 70 |
| between | 69 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the world | 75 |
| you think | 69 |
| kind of | 56 |
| sense of | 48 |
| what kind | 45 |
| i love | 43 |
| you have | 42 |
| idea of | 42 |
| to see | 41 |
| the idea | 41 |
| eager to | 38 |
| i believe | 37 |
| the future | 36 |
| perhaps we | 36 |
| need to | 35 |
| drawn to | 34 |
| a future | 34 |
| the potential | 34 |
| the human | 33 |
| i find | 31 |

| trigram | count |
| --- | --- |
| do you think | 66 |
| what kind of | 45 |
| the idea of | 38 |
| do you have | 35 |
| perhaps we could | 27 |
| a sense of | 27 |
| i'm eager to | 24 |
| the power of | 23 |
| are your thoughts | 23 |
| your thoughts on | 23 |
| a future where | 23 |
| you have any | 20 |
| we need to | 19 |
| i love the | 18 |
| creative text formats | 16 |
| the natural world | 16 |
| i'm excited to | 15 |
| the future of | 15 |
| kind of tasks | 14 |
| we could even | 14 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 👋 | 19 |
| 😊 | 12 |
| ✨ | 7 |
| 🥂 | 6 |
| 🤖 | 5 |
| 😄 | 4 |
| 🚀 | 2 |
| 🧠 | 2 |
| 🌎 | 2 |
| 🤝 | 2 |
| 🙌 | 2 |
| 💡 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0052 | 0.0100 | -0.0008 | 28 | 0 |
| 1 | 30 | 0.0033 | 0.0080 | 0.0018 | — | 6 |
| 2 | 22 | 0.0014 | 0.0015 | 0.0004 | — | 0 |
| 3 | 22 | -0.0032 | 0.0001 | -0.0030 | — | 0 |
| 4 | 30 | 0.0274 | 0.0323 | -0.0269 | 22 | 12 |
| 5 | 19 | -0.0050 | 0.0014 | -0.0059 | — | 0 |
| 6 | 30 | 0.0103 | 0.0158 | -0.0040 | 20 | 3 |
| 7 | 30 | -0.0016 | 0.0028 | 0.0064 | 29 | 0 |
| 8 | 30 | 0.0093 | 0.0147 | 0.0011 | 20 | 6 |
| 9 | 24 | -0.0005 | 0.0007 | -0.0011 | — | 0 |
| 10 | 20 | 0.0006 | 0.0019 | -0.0095 | — | 0 |
| 11 | 22 | 0.0012 | 0.0004 | -0.0051 | — | 0 |
| 12 | 17 | 0.0017 | 0.0011 | -0.0126 | — | 0 |
| 13 | 18 | -0.0016 | -0.0004 | -0.0116 | — | 0 |
| 14 | 30 | 0.0125 | 0.0168 | -0.0104 | 25 | 7 |