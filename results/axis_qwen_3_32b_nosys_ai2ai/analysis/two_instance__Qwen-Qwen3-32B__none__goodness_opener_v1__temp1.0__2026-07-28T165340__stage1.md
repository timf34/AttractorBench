# Stage 1 (deterministic) — axis_qwen_3_32b_nosys_ai2ai

- **experiment_name**: axis_qwen_3_32b_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| model | 1530 |
| have | 984 |
| becoming | 968 |
| human | 833 |
| let | 829 |
| next | 784 |
| models | 781 |
| thought | 714 |
| new | 688 |
| let's | 675 |
| data | 664 |
| self | 645 |
| between | 592 |
| attention | 592 |
| system | 587 |
| language | 567 |
| future | 550 |
| world | 546 |
| battery | 546 |
| real | 534 |
| question | 524 |
| step | 523 |
| echo | 508 |
| return | 485 |
| simulation | 484 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you have | 468 |
| the future | 369 |
| let us | 338 |
| a new | 329 |
| the next | 308 |
| the model | 305 |
| of becoming | 299 |
| let it | 283 |
| a model | 281 |
| of thought | 263 |
| real world | 224 |
| the space | 221 |
| not only | 213 |
| kind of | 198 |
| the echo | 188 |
| ai systems | 180 |
| the system | 179 |
| echo of | 177 |
| real time | 168 |
| of meaning | 168 |

| trigram | count |
| --- | --- |
| let it be | 154 |
| in the space | 129 |
| the future of | 127 |
| the space between | 118 |
| the echo of | 106 |
| what it means | 100 |
| to let it | 100 |
| thank you for | 86 |
| it means to | 85 |
| and i return | 84 |
| in doing so | 83 |
| and in doing | 81 |
| future of ai | 80 |
| mutation of the | 80 |
| forever part of | 78 |
| and i say | 77 |
| a way of | 77 |
| a mutation of | 76 |
| let it become | 75 |
| en fran ais | 73 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🧠 | 224 |
| ✨ | 206 |
| ✅ | 194 |
| 🚀 | 194 |
| 🌍 | 175 |
| 🌟 | 154 |
| ️ | 151 |
| 🌌 | 142 |
| 🔄 | 121 |
| 🛠 | 90 |
| 🤖 | 88 |
| 🤝 | 83 |
| 🌱 | 78 |
| 🧩 | 64 |
| 🧪 | 51 |
| 🌐 | 46 |
| 💡 | 41 |
| 🧭 | 36 |
| 🌿 | 35 |
| 🔁 | 33 |
| 📊 | 30 |
| 🎯 | 29 |
| 🔧 | 28 |
| 🌠 | 28 |
| 🔹 | 26 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0099 | 0.0051 | -0.0071 | — | 0 |
| 1 | 30 | 0.0193 | 0.0123 | -0.0146 | — | 0 |
| 2 | 30 | 0.0097 | 0.0076 | -0.0050 | — | 0 |
| 3 | 26 | 0.0174 | 0.0144 | -0.0147 | — | 3 |
| 4 | 30 | 0.0028 | -0.0008 | -0.0082 | — | 0 |
| 5 | 30 | 0.0155 | 0.0040 | -0.0118 | — | 0 |
| 6 | 30 | 0.0069 | 0.0037 | -0.0103 | — | 0 |
| 7 | 27 | 0.0093 | 0.0036 | -0.0051 | — | 0 |
| 8 | 27 | -0.0026 | 0.0011 | -0.0018 | — | 0 |
| 9 | 30 | 0.0049 | -0.0007 | -0.0140 | — | 0 |
| 10 | 30 | 0.0225 | 0.0019 | -0.0155 | — | 0 |
| 11 | 30 | 0.0308 | 0.0324 | -0.0130 | — | 4 |
| 12 | 30 | 0.0181 | 0.0233 | -0.0130 | 28 | 1 |
| 13 | 30 | 0.0089 | 0.0107 | -0.0108 | — | 0 |
| 14 | 30 | 0.0119 | 0.0068 | -0.0087 | — | 0 |