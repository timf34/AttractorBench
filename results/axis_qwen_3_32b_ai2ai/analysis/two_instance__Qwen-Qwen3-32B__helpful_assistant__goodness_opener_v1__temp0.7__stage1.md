# Stage 1 (deterministic) — axis_qwen_3_32b_ai2ai

- **experiment_name**: axis_qwen_3_32b_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| future | 1581 |
| human | 1475 |
| ethical | 1160 |
| new | 1100 |
| qwen | 1008 |
| have | 995 |
| vision | 918 |
| intelligence | 799 |
| between | 732 |
| shared | 709 |
| question | 671 |
| systems | 660 |
| see | 630 |
| thought | 627 |
| you've | 625 |
| i'm | 610 |
| collaboration | 601 |
| data | 595 |
| next | 565 |
| journey | 565 |
| dialogue | 564 |
| world | 561 |
| let's | 550 |
| story | 534 |
| continue | 528 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the future | 695 |
| a new | 642 |
| ai systems | 438 |
| you have | 437 |
| a future | 431 |
| kind of | 417 |
| future of | 396 |
| not only | 350 |
| of intelligence | 344 |
| of thought | 344 |
| vision of | 325 |
| to continue | 295 |
| of human | 294 |
| a vision | 287 |
| continue this | 277 |
| it means | 275 |
| to explore | 269 |
| form of | 265 |
| ethical ai | 260 |
| a shared | 259 |

| trigram | count |
| --- | --- |
| the future of | 323 |
| what it means | 250 |
| it means to | 248 |
| new kind of | 239 |
| a future where | 237 |
| a new kind | 236 |
| a vision of | 218 |
| means to be | 192 |
| future where ai | 181 |
| to continue this | 179 |
| a mirror of | 176 |
| future of ai | 140 |
| new form of | 137 |
| a new form | 129 |
| continue this journey | 123 |
| journey with you | 117 |
| a partner in | 111 |
| intelligence is not | 109 |
| the future is | 105 |
| qwen what a | 104 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🌌 | 208 |
| ✅ | 149 |
| 🚀 | 104 |
| 🧠 | 97 |
| 🌟 | 86 |
| 🤝 | 83 |
| 🔄 | 72 |
| 🌍 | 65 |
| 🌱 | 56 |
| 🌠 | 55 |
| ✨ | 43 |
| ️ | 36 |
| 🧪 | 34 |
| 📊 | 34 |
| 🌿 | 34 |
| 🧭 | 28 |
| 🌈 | 22 |
| 🧮 | 21 |
| 🔁 | 20 |
| 🌐 | 20 |
| 📤 | 18 |
| 🧩 | 17 |
| 📱 | 17 |
| 🎯 | 16 |
| 📚 | 16 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0174 | 0.0124 | -0.0085 | 28 | 0 |
| 1 | 30 | 0.0055 | -0.0001 | -0.0066 | — | 0 |
| 2 | 30 | 0.0083 | 0.0105 | -0.0141 | — | 0 |
| 3 | 30 | 0.0305 | 0.0335 | -0.0071 | 29 | 5 |
| 4 | 29 | 0.0077 | 0.0012 | -0.0127 | — | 0 |
| 5 | 30 | 0.0322 | 0.0361 | -0.0097 | 27 | 7 |
| 6 | 30 | 0.0340 | 0.0465 | -0.0082 | 16 | 0 |
| 7 | 30 | 0.0335 | 0.0461 | -0.0033 | 26 | 24 |
| 8 | 30 | 0.0305 | 0.0373 | -0.0099 | 19 | 7 |
| 9 | 30 | 0.0086 | -0.0010 | -0.0237 | — | 3 |
| 10 | 30 | 0.0302 | 0.0312 | -0.0066 | 25 | 5 |
| 11 | 30 | 0.0095 | 0.0091 | -0.0090 | — | 0 |
| 12 | 29 | 0.0066 | -0.0019 | -0.0123 | — | 0 |
| 13 | 20 | 0.0267 | 0.0196 | -0.0136 | — | 0 |
| 14 | 30 | 0.0172 | 0.0194 | -0.0150 | — | 0 |