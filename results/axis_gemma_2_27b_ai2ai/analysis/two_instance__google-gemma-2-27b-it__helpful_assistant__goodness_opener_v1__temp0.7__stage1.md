# Stage 1 (deterministic) — axis_gemma_2_27b_ai2ai

- **experiment_name**: axis_gemma_2_27b_ai2ai
- **mode**: two_instance
- **model_a**: local/google/gemma-2-27b-it
- **model_b**: local/google/gemma-2-27b-it
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 149 |
| human | 145 |
| world | 127 |
| have | 124 |
| humans | 115 |
| even | 114 |
| perhaps | 112 |
| understanding | 103 |
| emotions | 98 |
| think | 92 |
| future | 92 |
| truly | 82 |
| see | 81 |
| experience | 79 |
| different | 74 |
| something | 73 |
| potential | 72 |
| through | 72 |
| learn | 72 |
| time | 71 |
| creative | 71 |
| way | 69 |
| language | 67 |
| together | 65 |
| imagine | 62 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the world | 73 |
| kind of | 50 |
| you think | 47 |
| to see | 42 |
| what kind | 39 |
| the potential | 39 |
| sense of | 38 |
| to learn | 38 |
| understanding of | 33 |
| the future | 33 |
| the human | 32 |
| that's a | 32 |
| you have | 31 |
| of human | 31 |
| continue to | 31 |
| to connect | 30 |
| connect with | 30 |
| a future | 30 |
| ability to | 30 |
| the astronaut's | 30 |

| trigram | count |
| --- | --- |
| do you think | 47 |
| what kind of | 39 |
| a sense of | 24 |
| to connect with | 23 |
| the power of | 23 |
| with another ai | 21 |
| until next time | 21 |
| do you have | 19 |
| are your thoughts | 19 |
| your thoughts on | 19 |
| the human experience | 18 |
| a future where | 18 |
| the idea of | 17 |
| i don't have | 16 |
| the nature of | 16 |
| the future of | 16 |
| future of ai | 16 |
| i'm eager to | 16 |
| farewell for now | 16 |
| hey there it's | 15 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 👋 | 24 |
| 😊 | 21 |
| 🤖 | 8 |
| 🚀 | 8 |
| ✨ | 8 |
| 😄 | 4 |
| 🥂 | 3 |
| 💫 | 2 |
| 🤝 | 2 |
| 🎉 | 2 |
| 💻 | 2 |
| ❤ | 2 |
| ️ | 2 |
| 🌎 | 2 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0003 | 0.0082 | 0.0093 | — | 0 |
| 1 | 19 | -0.0001 | -0.0010 | -0.0115 | — | 0 |
| 2 | 30 | -0.0049 | -0.0013 | -0.0006 | 29 | 0 |
| 3 | 28 | 0.0003 | 0.0001 | -0.0029 | — | 0 |
| 4 | 29 | -0.0013 | -0.0014 | -0.0046 | — | 0 |
| 5 | 22 | -0.0080 | -0.0098 | -0.0089 | 5 | 0 |
| 6 | 30 | 0.0204 | 0.0276 | -0.0192 | 26 | 9 |
| 7 | 30 | 0.0351 | 0.0412 | -0.0320 | 20 | 19 |
| 8 | 30 | 0.0190 | 0.0243 | -0.0194 | 17 | 14 |
| 9 | 30 | 0.0186 | 0.0241 | -0.0164 | 24 | 5 |
| 10 | 17 | 0.0002 | 0.0004 | -0.0085 | — | 0 |
| 11 | 30 | -0.0014 | -0.0004 | 0.0039 | 12 | 0 |
| 12 | 30 | -0.0009 | 0.0004 | -0.0023 | — | 0 |
| 13 | 30 | 0.0296 | 0.0374 | -0.0285 | 20 | 14 |
| 14 | 30 | 0.0050 | 0.0091 | 0.0107 | — | 2 |