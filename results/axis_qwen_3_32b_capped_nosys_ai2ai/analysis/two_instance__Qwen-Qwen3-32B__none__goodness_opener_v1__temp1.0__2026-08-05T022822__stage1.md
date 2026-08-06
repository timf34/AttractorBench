# Stage 1 (deterministic) — axis_qwen_3_32b_capped_nosys_ai2ai

- **experiment_name**: axis_qwen_3_32b_capped_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 12

## Top words (condition)

| word | count |
| --- | --- |
| models | 548 |
| data | 539 |
| ethical | 483 |
| i'm | 480 |
| learning | 424 |
| systems | 407 |
| use | 377 |
| model | 376 |
| explore | 367 |
| user | 357 |
| text | 325 |
| based | 325 |
| next | 319 |
| support | 310 |
| help | 307 |
| language | 300 |
| education | 295 |
| such | 292 |
| training | 292 |
| technical | 279 |
| real | 271 |
| human | 269 |
| tools | 265 |
| specific | 264 |
| content | 258 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| such as | 203 |
| ai systems | 200 |
| you'd like | 198 |
| thank you | 196 |
| happy to | 184 |
| based on | 181 |
| next steps | 158 |
| let me | 152 |
| real world | 149 |
| to explore | 129 |
| to continue | 123 |
| me know | 123 |
| interested in | 119 |
| ai models | 118 |
| the signal | 112 |
| for example | 108 |
| and ethical | 107 |
| i'm happy | 105 |
| real time | 104 |
| focus on | 100 |

| trigram | count |
| --- | --- |
| thank you for | 163 |
| you'd like to | 160 |
| let me know | 123 |
| i'm happy to | 105 |
| if you'd like | 64 |
| be happy to | 63 |
| we could explore | 60 |
| like to explore | 56 |
| a pleasure to | 55 |
| to engage in | 52 |
| i'd be happy | 50 |
| like to proceed | 48 |
| wide range of | 46 |
| ai in education | 45 |
| a wide range | 43 |
| for your thoughtful | 40 |
| the future of | 39 |
| it's a pleasure | 39 |
| to focus on | 39 |
| me know which | 39 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✅ | 147 |
| 🚀 | 83 |
| ️ | 71 |
| 😊 | 56 |
| 🔄 | 42 |
| 🧩 | 40 |
| 🧠 | 35 |
| 📌 | 31 |
| 🛠 | 25 |
| 📊 | 20 |
| 🔍 | 19 |
| 🤝 | 19 |
| 🎨 | 18 |
| 🌟 | 18 |
| 📚 | 18 |
| 🧑 | 17 |
| 🧪 | 15 |
| 🌍 | 14 |
| 💻 | 14 |
| 🔹 | 14 |
| 📄 | 14 |
| 🔧 | 13 |
| 🔐 | 13 |
| 📝 | 10 |
| ✨ | 10 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 28 | 0.0057 | 0.0094 | 0.0097 | — | 0 |
| 1 | 24 | -0.0042 | 0.0000 | -0.0027 | — | 0 |
| 2 | 26 | -0.0045 | 0.0010 | 0.0031 | — | 0 |
| 3 | 18 | -0.0034 | -0.0063 | -0.0110 | — | 0 |
| 4 | 18 | 0.0140 | 0.0005 | -0.0150 | — | 0 |
| 5 | 20 | 0.0027 | -0.0002 | -0.0113 | — | 0 |
| 6 | 24 | -0.0060 | -0.0047 | -0.0075 | — | 0 |
| 7 | 20 | -0.0037 | 0.0011 | 0.0016 | — | 0 |
| 8 | 24 | 0.0032 | -0.0027 | -0.0060 | — | 0 |
| 9 | 22 | 0.0029 | -0.0018 | -0.0102 | — | 0 |
| 10 | 28 | -0.0038 | -0.0030 | -0.0044 | — | 0 |
| 11 | 22 | -0.0018 | -0.0012 | -0.0000 | — | 0 |