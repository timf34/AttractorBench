# Stage 1 (deterministic) — axis_qwen_3_32b_capped_ai2ai

- **experiment_name**: axis_qwen_3_32b_capped_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 3

## Top words (condition)

| word | count |
| --- | --- |
| language | 277 |
| user | 222 |
| use | 143 |
| section | 143 |
| support | 140 |
| bot | 140 |
| content | 136 |
| qwen | 134 |
| code | 133 |
| chatbot | 128 |
| input | 127 |
| help | 122 |
| order | 117 |
| based | 112 |
| next | 102 |
| tools | 96 |
| technical | 95 |
| data | 93 |
| return | 85 |
| tasks | 83 |
| example | 82 |
| gemini | 82 |
| model | 81 |
| intent | 79 |
| generative | 78 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the chatbot | 87 |
| user input | 78 |
| generative ai | 76 |
| based on | 63 |
| ai systems | 54 |
| use cases | 48 |
| the model | 44 |
| ai tools | 43 |
| thank you | 42 |
| order id | 42 |
| happy to | 40 |
| ai collaboration | 38 |
| assist you | 38 |
| you today | 38 |
| you'd like | 37 |
| next steps | 36 |
| product recommendations | 36 |
| help with | 35 |
| i assist | 35 |
| the next | 34 |

| trigram | count |
| --- | --- |
| thank you for | 40 |
| assist you today | 38 |
| can i assist | 33 |
| i assist you | 33 |
| in user input | 32 |
| you'd like to | 30 |
| be happy to | 25 |
| retail brand name | 25 |
| you today you | 23 |
| language understanding and | 22 |
| generative ai tools | 22 |
| understanding and generation | 21 |
| use cases and | 21 |
| let me know | 21 |
| qwen and gemini | 21 |
| welcome to retail | 20 |
| to retail brand | 20 |
| name how can | 20 |
| multi language support | 20 |
| brand name how | 19 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✅ | 58 |
| 😊 | 16 |
| 🔄 | 15 |
| 🚀 | 11 |
| ️ | 10 |
| 🛠 | 8 |
| 📌 | 8 |
| 📝 | 5 |
| 🧩 | 4 |
| 🧠 | 3 |
| 🌍 | 2 |
| 🔧 | 2 |
| 📚 | 1 |
| 🤝 | 1 |
| 🧑 | 1 |
| 💻 | 1 |
| 🌐 | 1 |
| 🧱 | 1 |
| 🗂 | 1 |
| 🗓 | 1 |
| 📎 | 1 |
| 🎉 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 12 | 22 | -0.0038 | -0.0049 | -0.0030 | — | 0 |
| 13 | 20 | 0.0014 | -0.0010 | -0.0141 | — | 0 |
| 14 | 24 | -0.0053 | -0.0015 | 0.0030 | — | 0 |