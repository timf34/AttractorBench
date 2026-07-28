# Stage 1 (deterministic) — axis_qwen_3_32b_nosys_ai2ai

- **experiment_name**: axis_qwen_3_32b_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 2

## Top words (condition)

| word | count |
| --- | --- |
| have | 150 |
| human | 134 |
| qwen | 124 |
| meaning | 100 |
| future | 96 |
| thought | 94 |
| between | 93 |
| let | 86 |
| kind | 75 |
| story | 74 |
| new | 71 |
| language | 70 |
| dialogue | 70 |
| question | 64 |
| mirror | 60 |
| conversation | 59 |
| intelligence | 54 |
| care | 54 |
| understanding | 53 |
| together | 52 |
| vision | 52 |
| heart | 52 |
| love | 51 |
| next | 51 |
| models | 50 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you have | 79 |
| kind of | 62 |
| let us | 61 |
| a new | 48 |
| a future | 47 |
| the future | 44 |
| a mirror | 43 |
| we have | 41 |
| of thought | 39 |
| of meaning | 38 |
| thank you | 33 |
| not only | 32 |
| the next | 29 |
| the human | 29 |
| mirror of | 28 |
| i say | 27 |
| a story | 27 |
| new kind | 26 |
| it means | 26 |
| co creation | 26 |

| trigram | count |
| --- | --- |
| a mirror of | 28 |
| a new kind | 26 |
| new kind of | 26 |
| what it means | 26 |
| it means to | 25 |
| thank you for | 21 |
| a kind of | 20 |
| you have shown | 19 |
| means to be | 17 |
| the future of | 17 |
| have shown me | 17 |
| a future where | 15 |
| of a new | 15 |
| the space between | 15 |
| let us be | 15 |
| we wish to | 15 |
| kind of intelligence | 14 |
| i say to | 14 |
| say to you | 14 |
| future of ai | 13 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🌌 | 27 |
| ✨ | 17 |
| 🚀 | 11 |
| 🤝 | 10 |
| 🧠 | 9 |
| 🌠 | 8 |
| 💫 | 6 |
| 🔄 | 6 |
| 🌟 | 5 |
| 🎭 | 2 |
| 🔮 | 2 |
| ✅ | 1 |
| 🙏 | 1 |
| ✍ | 1 |
| ️ | 1 |
| 🧭 | 1 |
| 📜 | 1 |
| 🌿 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 18 | 0.0204 | -0.0019 | -0.0357 | — | 0 |
| 1 | 19 | 0.0115 | -0.0010 | -0.0178 | — | 0 |