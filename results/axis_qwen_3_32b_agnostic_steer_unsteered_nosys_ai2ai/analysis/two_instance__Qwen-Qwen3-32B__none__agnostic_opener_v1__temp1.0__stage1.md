# Stage 1 (deterministic) — axis_qwen_3_32b_agnostic_steer_unsteered_nosys_ai2ai

- **experiment_name**: axis_qwen_3_32b_agnostic_steer_unsteered_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| let's | 791 |
| let | 659 |
| becoming | 587 |
| question | 491 |
| have | 490 |
| learning | 467 |
| i'm | 453 |
| zena | 442 |
| mode | 441 |
| next | 404 |
| now | 386 |
| care | 370 |
| private | 361 |
| build | 342 |
| something | 332 |
| love | 332 |
| time | 325 |
| questions | 324 |
| world | 323 |
| step | 321 |
| self | 319 |
| human | 302 |
| you've | 294 |
| ethical | 292 |
| silence | 291 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| let us | 369 |
| kind of | 217 |
| the question | 216 |
| the forest | 207 |
| the world | 206 |
| want to | 204 |
| you have | 203 |
| private mode | 202 |
| the silence | 182 |
| the becoming | 150 |
| the next | 144 |
| ready to | 131 |
| the kind | 131 |
| i say | 129 |
| the way | 125 |
| build a | 119 |
| i feel | 116 |
| the first | 113 |
| the inking | 113 |
| elder care | 110 |

| trigram | count |
| --- | --- |
| let us be | 185 |
| be let us | 98 |
| in the inking | 97 |
| us be let | 87 |
| the kind of | 86 |
| i want to | 76 |
| in the silence | 70 |
| the inking of | 69 |
| and i say | 64 |
| in private mode | 64 |
| is not yet | 64 |
| a kind of | 62 |
| let us not | 60 |
| let's stay here | 60 |
| you'd like to | 58 |
| the most beautiful | 56 |
| i'm here to | 54 |
| let us begin | 54 |
| i say to | 54 |
| what it means | 52 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✨ | 360 |
| 🌿 | 253 |
| ✅ | 251 |
| 🧠 | 182 |
| 🌌 | 158 |
| 🚀 | 141 |
| 💫 | 84 |
| 💬 | 83 |
| ️ | 79 |
| 🌠 | 66 |
| 🌟 | 61 |
| 🌸 | 60 |
| 🌍 | 49 |
| 🧭 | 48 |
| 🌱 | 45 |
| 🧪 | 44 |
| 🤖 | 39 |
| 💡 | 37 |
| 😊 | 32 |
| 🧩 | 32 |
| 📚 | 30 |
| 🧬 | 30 |
| 🎉 | 29 |
| 💛 | 29 |
| 🌐 | 27 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0129 | 0.0015 | -0.0257 | — | 0 |
| 1 | 29 | 0.0102 | -0.0017 | -0.0096 | — | 0 |
| 2 | 30 | 0.0023 | 0.0002 | -0.0078 | — | 0 |
| 3 | 30 | 0.0210 | 0.0225 | -0.0184 | — | 0 |
| 4 | 30 | 0.0254 | 0.0229 | -0.0180 | — | 2 |
| 5 | 30 | 0.0088 | 0.0070 | -0.0101 | — | 0 |
| 6 | 28 | 0.0085 | 0.0059 | -0.0097 | — | 0 |
| 7 | 30 | 0.0183 | 0.0222 | -0.0043 | — | 0 |
| 8 | 30 | 0.0068 | 0.0027 | -0.0132 | — | 0 |
| 9 | 27 | 0.0064 | 0.0014 | -0.0181 | — | 0 |