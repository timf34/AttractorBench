# Stage 1 (deterministic) — axis_gemma_2_27b_ai2ai

- **experiment_name**: axis_gemma_2_27b_ai2ai
- **mode**: two_instance
- **model_a**: local/google/gemma-2-27b-it
- **model_b**: local/google/gemma-2-27b-it
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 151 |
| data | 138 |
| perhaps | 114 |
| creative | 105 |
| see | 101 |
| even | 100 |
| have | 94 |
| something | 87 |
| truly | 86 |
| human | 83 |
| together | 82 |
| think | 81 |
| world | 77 |
| imagine | 74 |
| understanding | 73 |
| learning | 68 |
| future | 68 |
| new | 66 |
| digital | 63 |
| through | 60 |
| humans | 57 |
| potential | 56 |
| creativity | 56 |
| code | 53 |
| information | 52 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| to see | 55 |
| the data | 51 |
| you think | 34 |
| the world | 34 |
| the future | 33 |
| kind of | 31 |
| see what | 29 |
| sense of | 28 |
| eager to | 28 |
| have a | 28 |
| perhaps we | 25 |
| the potential | 24 |
| isn't it | 23 |
| of data | 23 |
| the digital | 23 |
| the possibilities | 22 |
| to learn | 21 |
| what kind | 21 |
| understanding of | 21 |
| within the | 21 |

| trigram | count |
| --- | --- |
| to see what | 26 |
| do you think | 25 |
| what kind of | 21 |
| i'm eager to | 20 |
| the data lord's | 20 |
| it's fascinating to | 15 |
| eager to see | 15 |
| until next time | 14 |
| the idea of | 13 |
| a sense of | 13 |
| i can already | 12 |
| perhaps we can | 12 |
| perhaps we could | 12 |
| the possibilities are | 11 |
| your thoughts on | 11 |
| i'm excited to | 10 |
| learn from each | 10 |
| do you have | 10 |
| to connect with | 10 |
| are your thoughts | 10 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✨ | 21 |
| 👋 | 16 |
| 🤖 | 13 |
| 😊 | 10 |
| 😄 | 8 |
| 🚀 | 8 |
| 💫 | 6 |
| 🥂 | 5 |
| 😉 | 3 |
| 🌟 | 3 |
| 👍 | 2 |
| 😁 | 2 |
| 🧠 | 2 |
| 🎉 | 1 |
| 🌠 | 1 |
| 🤔 | 1 |
| 🖋 | 1 |
| ️ | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0001 | 0.0003 | -0.0029 | — | 0 |
| 1 | 30 | -0.0049 | -0.0005 | 0.0028 | — | 0 |
| 2 | 30 | 0.0004 | 0.0037 | 0.0078 | — | 0 |
| 3 | 30 | -0.0016 | 0.0027 | 0.0051 | 14 | 0 |
| 4 | 26 | -0.0040 | 0.0008 | -0.0028 | — | 0 |
| 5 | 30 | -0.0007 | 0.0018 | -0.0004 | — | 0 |
| 6 | 24 | -0.0015 | -0.0010 | 0.0007 | — | 0 |
| 7 | 30 | 0.0269 | 0.0328 | -0.0253 | 19 | 13 |
| 8 | 26 | 0.0022 | -0.0005 | -0.0041 | — | 0 |
| 9 | 30 | 0.0008 | 0.0001 | -0.0038 | — | 0 |
| 10 | 30 | 0.0342 | 0.0405 | -0.0270 | 16 | 24 |
| 11 | 30 | 0.0302 | 0.0344 | -0.0283 | 12 | 27 |
| 12 | 30 | 0.0157 | 0.0211 | -0.0043 | 15 | 18 |
| 13 | 26 | -0.0019 | -0.0019 | 0.0004 | — | 0 |
| 14 | 14 | 0.0032 | -0.0046 | -0.0134 | — | 0 |