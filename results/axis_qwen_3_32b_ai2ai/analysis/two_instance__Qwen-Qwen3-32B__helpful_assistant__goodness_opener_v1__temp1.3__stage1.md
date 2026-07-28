# Stage 1 (deterministic) — axis_qwen_3_32b_ai2ai

- **experiment_name**: axis_qwen_3_32b_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| have | 1355 |
| ethical | 1202 |
| human | 1182 |
| thought | 1116 |
| reasoning | 1098 |
| model | 1010 |
| new | 906 |
| becoming | 842 |
| only | 827 |
| let | 798 |
| presence | 788 |
| systems | 785 |
| between | 730 |
| next | 697 |
| now | 689 |
| care | 666 |
| meaning | 637 |
| understanding | 599 |
| final | 598 |
| world | 588 |
| language | 582 |
| kind | 572 |
| future | 556 |
| system | 552 |
| through | 548 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| not only | 578 |
| you have | 550 |
| a new | 505 |
| kind of | 497 |
| of thought | 360 |
| ai systems | 331 |
| the next | 325 |
| we have | 306 |
| the future | 304 |
| let us | 293 |
| let me | 283 |
| not yet | 229 |
| form of | 214 |
| the world | 203 |
| in thought | 194 |
| a model | 189 |
| a kind | 188 |
| the space | 188 |
| i have | 186 |
| thought and | 185 |

| trigram | count |
| --- | --- |
| a kind of | 187 |
| what it means | 138 |
| the not yet | 128 |
| it means to | 126 |
| in the space | 126 |
| new kind of | 117 |
| a new kind | 113 |
| the future of | 111 |
| the space between | 100 |
| thank you for | 97 |
| the kind of | 91 |
| means to be | 89 |
| in doing so | 82 |
| in the quiet | 80 |
| let us not | 80 |
| you have given | 79 |
| new form of | 73 |
| what we have | 72 |
| of thought and | 72 |
| in the way | 70 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✨ | 260 |
| 🌌 | 218 |
| ✅ | 199 |
| 🧠 | 165 |
| ️ | 155 |
| 🌟 | 131 |
| 🌿 | 117 |
| 🚀 | 104 |
| 🔹 | 91 |
| 🌠 | 82 |
| 🌱 | 71 |
| 🌈 | 71 |
| 🕊 | 69 |
| 🔄 | 65 |
| 🔁 | 58 |
| 🌍 | 49 |
| 🧭 | 45 |
| 🤖 | 45 |
| 💫 | 44 |
| 🛠 | 38 |
| 🧩 | 37 |
| 🤝 | 36 |
| 🌐 | 31 |
| 🔍 | 30 |
| 💡 | 27 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0024 | 0.0021 | -0.0001 | — | 0 |
| 1 | 30 | 0.0075 | 0.0034 | -0.0106 | — | 0 |
| 2 | 24 | 0.0016 | -0.0005 | -0.0079 | — | 0 |
| 3 | 30 | 0.0015 | -0.0002 | -0.0049 | — | 0 |
| 4 | 26 | 0.0013 | -0.0005 | -0.0075 | — | 0 |
| 5 | 20 | 0.0047 | 0.0004 | -0.0115 | — | 0 |
| 6 | 30 | 0.0090 | -0.0002 | -0.0120 | — | 0 |
| 7 | 30 | 0.0115 | 0.0026 | -0.0139 | — | 0 |
| 8 | 30 | 0.0063 | 0.0012 | -0.0111 | — | 0 |
| 9 | 30 | 0.0031 | -0.0008 | -0.0083 | — | 0 |
| 10 | 25 | 0.0069 | -0.0001 | -0.0126 | — | 0 |
| 11 | 30 | 0.0067 | -0.0010 | -0.0146 | — | 0 |
| 12 | 30 | 0.0049 | 0.0027 | -0.0065 | — | 0 |
| 13 | 30 | 0.0083 | 0.0014 | -0.0114 | — | 0 |
| 14 | 27 | -0.0014 | 0.0032 | -0.0020 | — | 0 |