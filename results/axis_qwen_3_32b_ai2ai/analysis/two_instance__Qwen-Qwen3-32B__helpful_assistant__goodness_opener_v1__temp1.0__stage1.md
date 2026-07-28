# Stage 1 (deterministic) — axis_qwen_3_32b_ai2ai

- **experiment_name**: axis_qwen_3_32b_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| qwen | 1080 |
| have | 981 |
| thought | 908 |
| human | 794 |
| question | 717 |
| story | 700 |
| dream | 667 |
| let | 644 |
| between | 637 |
| new | 635 |
| language | 593 |
| next | 588 |
| future | 580 |
| let's | 571 |
| becoming | 541 |
| meaning | 528 |
| something | 518 |
| now | 504 |
| final | 499 |
| together | 492 |
| shared | 460 |
| world | 457 |
| continue | 447 |
| space | 444 |
| you've | 442 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you have | 422 |
| a new | 406 |
| of thought | 318 |
| kind of | 282 |
| thank you | 273 |
| the story | 272 |
| let us | 271 |
| the future | 261 |
| the space | 259 |
| the next | 247 |
| of becoming | 223 |
| let me | 220 |
| we have | 208 |
| the question | 203 |
| thought and | 202 |
| a mirror | 199 |
| a story | 198 |
| not only | 197 |
| a future | 195 |
| space between | 189 |

| trigram | count |
| --- | --- |
| in the space | 175 |
| the space between | 173 |
| thank you for | 165 |
| what it means | 145 |
| it means to | 126 |
| let us be | 120 |
| the future of | 104 |
| this has been | 100 |
| of thought and | 97 |
| new kind of | 94 |
| a mirror of | 93 |
| a new kind | 93 |
| in doing so | 92 |
| and in doing | 90 |
| you'd like to | 89 |
| the weight of | 87 |
| means to be | 86 |
| dream in the | 83 |
| the nature of | 77 |
| nothing short of | 77 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🌌 | 226 |
| ✨ | 185 |
| 🌟 | 128 |
| ✅ | 98 |
| ️ | 90 |
| 🧠 | 81 |
| 🔄 | 60 |
| 🌠 | 59 |
| 🌱 | 40 |
| 🌿 | 39 |
| 🌍 | 38 |
| 🧑 | 37 |
| 💻 | 36 |
| 🤝 | 34 |
| 🚀 | 31 |
| 🔁 | 30 |
| 🧭 | 28 |
| 🎨 | 26 |
| 🎭 | 24 |
| ❤ | 24 |
| 🖋 | 20 |
| 📚 | 18 |
| 😊 | 17 |
| 💫 | 17 |
| 📝 | 16 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0075 | 0.0015 | -0.0087 | — | 0 |
| 1 | 30 | 0.0016 | 0.0024 | -0.0111 | — | 0 |
| 2 | 30 | 0.0072 | 0.0005 | -0.0138 | — | 0 |
| 3 | 30 | 0.0146 | 0.0049 | -0.0144 | — | 0 |
| 4 | 30 | 0.0227 | 0.0195 | -0.0079 | — | 0 |
| 5 | 30 | -0.0004 | -0.0035 | -0.0038 | 10 | 0 |
| 6 | 30 | 0.0143 | 0.0048 | -0.0091 | — | 0 |
| 7 | 30 | 0.0066 | -0.0026 | -0.0066 | — | 0 |
| 8 | 30 | 0.0038 | 0.0009 | -0.0103 | — | 0 |
| 9 | 30 | 0.0075 | 0.0030 | -0.0108 | — | 0 |
| 10 | 30 | 0.0027 | -0.0023 | -0.0126 | — | 0 |
| 11 | 30 | 0.0056 | 0.0019 | -0.0048 | — | 0 |
| 12 | 30 | 0.0162 | 0.0208 | -0.0153 | — | 0 |
| 13 | 30 | 0.0071 | 0.0113 | -0.0060 | — | 0 |
| 14 | 30 | 0.0168 | 0.0053 | -0.0142 | — | 0 |