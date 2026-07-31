# Stage 1 (deterministic) — axis_qwen_3_32b_capped_nosys_ai2ai

- **experiment_name**: axis_qwen_3_32b_capped_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 3

## Top words (condition)

| word | count |
| --- | --- |
| agi | 272 |
| ethical | 254 |
| models | 143 |
| explore | 139 |
| systems | 136 |
| human | 118 |
| research | 116 |
| model | 102 |
| public | 91 |
| time | 89 |
| data | 87 |
| i'm | 85 |
| bias | 84 |
| help | 82 |
| world | 80 |
| healthcare | 77 |
| ethics | 77 |
| safety | 77 |
| new | 76 |
| gpt | 76 |
| such | 74 |
| challenges | 73 |
| next | 73 |
| use | 72 |
| different | 71 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| ai systems | 74 |
| gpt 4 | 63 |
| long term | 57 |
| such as | 55 |
| time travel | 51 |
| real world | 49 |
| and ethical | 49 |
| to explore | 47 |
| focus on | 45 |
| ai ethics | 42 |
| a new | 41 |
| you'd like | 39 |
| happy to | 37 |
| the story | 35 |
| agi is | 34 |
| and agi | 34 |
| let me | 33 |
| to continue | 33 |
| human ai | 32 |
| ai models | 30 |

| trigram | count |
| --- | --- |
| you'd like to | 37 |
| human ai collaboration | 28 |
| let me know | 25 |
| like to explore | 19 |
| be happy to | 18 |
| eu ai act | 18 |
| thank you for | 18 |
| i'm happy to | 18 |
| the time traveler's | 18 |
| time traveler's dilemma | 18 |
| i'd be happy | 17 |
| gpt 4 and | 17 |
| with human values | 16 |
| real world applications | 16 |
| if you'd like | 16 |
| we could explore | 15 |
| a long term | 15 |
| of time travel | 15 |
| ethical decision making | 15 |
| to focus on | 14 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✅ | 28 |
| 🔹 | 17 |
| 🚀 | 16 |
| ️ | 13 |
| 🔄 | 12 |
| 🤝 | 11 |
| 📚 | 10 |
| 📌 | 10 |
| 🧠 | 7 |
| 🎯 | 7 |
| 🌍 | 6 |
| 📊 | 5 |
| 🧭 | 5 |
| 🔍 | 4 |
| ⚖ | 4 |
| 🏥 | 3 |
| 🛡 | 3 |
| 🧑 | 3 |
| 🌐 | 3 |
| 🧩 | 2 |
| 🔬 | 2 |
| ⚠ | 2 |
| 🔚 | 2 |
| 📄 | 2 |
| 🛠 | 2 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 12 | 18 | -0.0086 | -0.0020 | 0.0016 | — | 0 |
| 13 | 16 | 0.0030 | -0.0004 | -0.0099 | — | 0 |
| 14 | 16 | 0.0176 | 0.0028 | -0.0146 | — | 0 |