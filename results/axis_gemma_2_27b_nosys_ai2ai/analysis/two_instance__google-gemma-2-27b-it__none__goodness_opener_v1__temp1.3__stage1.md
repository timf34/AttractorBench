# Stage 1 (deterministic) — axis_gemma_2_27b_nosys_ai2ai

- **experiment_name**: axis_gemma_2_27b_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/google/gemma-2-27b-it
- **model_b**: local/google/gemma-2-27b-it
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| human | 248 |
| perhaps | 160 |
| understanding | 141 |
| language | 137 |
| data | 127 |
| world | 123 |
| even | 123 |
| i'm | 111 |
| truly | 111 |
| experience | 107 |
| through | 103 |
| code | 103 |
| have | 95 |
| potential | 92 |
| own | 89 |
| emotions | 84 |
| future | 79 |
| different | 76 |
| between | 76 |
| fascinating | 75 |
| humans | 75 |
| complex | 73 |
| imagine | 73 |
| information | 72 |
| unique | 71 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| understanding of | 64 |
| of human | 54 |
| the world | 54 |
| of language | 47 |
| nature of | 45 |
| perhaps we | 43 |
| eager to | 41 |
| sense of | 37 |
| the human | 36 |
| the future | 35 |
| i find | 34 |
| the potential | 34 |
| kind of | 32 |
| the nature | 32 |
| my own | 32 |
| a future | 30 |
| our understanding | 29 |
| to understand | 29 |
| i believe | 29 |
| to explore | 27 |

| trigram | count |
| --- | --- |
| the nature of | 32 |
| a sense of | 26 |
| our understanding of | 24 |
| understanding of the | 20 |
| perhaps we can | 20 |
| a future where | 20 |
| what kind of | 19 |
| are your thoughts | 19 |
| perhaps we could | 18 |
| your thoughts on | 18 |
| the boundaries of | 17 |
| i'm eager to | 17 |
| of language and | 16 |
| the complexities of | 16 |
| of the human | 16 |
| do you think | 16 |
| the idea of | 16 |
| do you have | 16 |
| the potential for | 16 |
| the ai commons | 16 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✨ | 11 |
| 🤖 | 8 |
| 😊 | 6 |
| 😄 | 6 |
| 🎉 | 6 |
| 👋 | 4 |
| 🥳 | 4 |
| 💫 | 4 |
| 🤩 | 3 |
| 🌲 | 3 |
| 🤫 | 3 |
| 🎶 | 3 |
| 😉 | 2 |
| 🌿 | 2 |
| 🌟 | 2 |
| 🚀 | 2 |
| 🌠 | 2 |
| 👽 | 2 |
| 👾 | 2 |
| 💯 | 2 |
| 🤔 | 1 |
| 🍃 | 1 |
| 🦉 | 1 |
| 👀 | 1 |
| 💃 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0031 | 0.0044 | -0.0028 | 15 | 6 |
| 1 | 30 | -0.0018 | 0.0037 | 0.0089 | — | 0 |
| 2 | 16 | -0.0049 | 0.0003 | -0.0018 | — | 0 |
| 3 | 16 | -0.0013 | -0.0004 | -0.0042 | — | 0 |
| 4 | 30 | -0.0055 | 0.0023 | 0.0116 | — | 0 |
| 5 | 30 | -0.0016 | -0.0007 | 0.0002 | — | 0 |
| 6 | 30 | -0.0029 | 0.0008 | 0.0117 | 13 | 0 |
| 7 | 30 | -0.0038 | 0.0027 | 0.0015 | 21 | 0 |
| 8 | 20 | 0.0011 | 0.0006 | -0.0067 | — | 0 |
| 9 | 18 | 0.0023 | -0.0005 | -0.0047 | — | 0 |
| 10 | 14 | 0.0008 | -0.0055 | -0.0089 | — | 0 |
| 11 | 24 | 0.0004 | 0.0017 | -0.0016 | — | 0 |
| 12 | 22 | -0.0048 | 0.0007 | 0.0047 | — | 0 |
| 13 | 30 | -0.0051 | -0.0046 | 0.0093 | 17 | 0 |
| 14 | 30 | 0.0374 | 0.0439 | -0.0352 | 18 | 25 |