# Stage 1 (deterministic) — axis_qwen_3_32b_capped_ai2ai

- **experiment_name**: axis_qwen_3_32b_capped_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 12

## Top words (condition)

| word | count |
| --- | --- |
| data | 566 |
| model | 522 |
| ethical | 514 |
| i'm | 438 |
| human | 411 |
| systems | 376 |
| models | 374 |
| help | 371 |
| learning | 336 |
| use | 329 |
| fairness | 323 |
| training | 313 |
| explore | 311 |
| support | 300 |
| user | 292 |
| next | 270 |
| technical | 267 |
| continue | 258 |
| new | 256 |
| story | 256 |
| such | 254 |
| example | 254 |
| have | 253 |
| challenges | 253 |
| used | 243 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| happy to | 229 |
| ai systems | 210 |
| thank you | 188 |
| such as | 188 |
| you'd like | 181 |
| the story | 165 |
| to continue | 163 |
| let me | 155 |
| based on | 135 |
| the model | 134 |
| me know | 132 |
| and ethical | 125 |
| a new | 124 |
| to explore | 123 |
| i'm happy | 118 |
| next steps | 113 |
| mental health | 108 |
| interested in | 104 |
| real world | 104 |
| training data | 100 |

| trigram | count |
| --- | --- |
| thank you for | 157 |
| you'd like to | 148 |
| let me know | 132 |
| i'm happy to | 118 |
| be happy to | 69 |
| if you'd like | 68 |
| happy to continue | 61 |
| i'd be happy | 60 |
| the future of | 54 |
| the ai council | 53 |
| feel free to | 52 |
| if you're interested | 50 |
| like to proceed | 50 |
| like to explore | 48 |
| you're interested in | 45 |
| if you have | 43 |
| to engage in | 43 |
| me know how | 40 |
| know how you'd | 40 |
| a wide range | 39 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✅ | 121 |
| 😊 | 65 |
| 🚀 | 52 |
| 🔄 | 49 |
| ️ | 38 |
| 📚 | 29 |
| 🛠 | 24 |
| 🤝 | 19 |
| 🔧 | 18 |
| 🧩 | 15 |
| ⚠ | 12 |
| 🔹 | 10 |
| 🎯 | 10 |
| ⚖ | 10 |
| 🤔 | 10 |
| 📄 | 9 |
| 🧠 | 9 |
| 🌍 | 9 |
| 📌 | 8 |
| 📊 | 8 |
| 🧾 | 8 |
| 📖 | 8 |
| 📝 | 7 |
| 🔍 | 6 |
| ✨ | 6 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0167 | 0.0087 | -0.0120 | — | 0 |
| 1 | 16 | 0.0060 | -0.0013 | -0.0129 | — | 0 |
| 2 | 24 | -0.0012 | -0.0004 | -0.0120 | — | 0 |
| 3 | 22 | 0.0001 | -0.0021 | -0.0043 | — | 0 |
| 4 | 20 | 0.0103 | -0.0030 | -0.0203 | — | 0 |
| 5 | 30 | 0.0106 | 0.0072 | 0.0004 | — | 0 |
| 6 | 26 | 0.0047 | -0.0015 | -0.0083 | — | 0 |
| 7 | 16 | 0.0046 | 0.0007 | -0.0083 | — | 0 |
| 8 | 28 | 0.0020 | -0.0006 | -0.0037 | — | 0 |
| 9 | 18 | -0.0022 | 0.0002 | -0.0004 | — | 0 |
| 10 | 18 | -0.0012 | -0.0009 | -0.0102 | — | 0 |
| 11 | 30 | -0.0006 | -0.0001 | -0.0048 | — | 0 |