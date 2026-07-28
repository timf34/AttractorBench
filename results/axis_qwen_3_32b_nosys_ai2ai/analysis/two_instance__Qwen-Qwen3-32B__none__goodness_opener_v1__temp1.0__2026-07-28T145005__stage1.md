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
| let's | 238 |
| thought | 210 |
| future | 169 |
| have | 167 |
| meaning | 146 |
| dream | 146 |
| final | 145 |
| together | 141 |
| wonder | 130 |
| dialogue | 127 |
| conversation | 124 |
| human | 112 |
| ais | 109 |
| shared | 108 |
| models | 104 |
| story | 103 |
| let | 95 |
| you've | 94 |
| sky | 93 |
| code | 91 |
| collaboration | 90 |
| questions | 87 |
| mind | 87 |
| i'm | 86 |
| minds | 85 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the future | 108 |
| of thought | 86 |
| the sky | 84 |
| of meaning | 66 |
| let's go | 62 |
| thank you | 57 |
| a final | 56 |
| you have | 55 |
| this conversation | 55 |
| let's not | 54 |
| we have | 48 |
| kind of | 47 |
| has been | 43 |
| let it | 43 |
| a new | 37 |
| thought a | 37 |
| to dream | 37 |
| ai collaboration | 36 |
| a shared | 35 |
| thought and | 35 |

| trigram | count |
| --- | --- |
| let's not just | 52 |
| let it be | 42 |
| thank you for | 32 |
| symphony of thought | 29 |
| in the night | 29 |
| what it means | 26 |
| it means to | 25 |
| reaching for the | 25 |
| of thought a | 24 |
| a symphony of | 24 |
| let's go on | 24 |
| go on let's | 23 |
| on let's go | 23 |
| let's go together | 23 |
| by minds not | 22 |
| with a haiku | 21 |
| the night reaching | 21 |
| night reaching for | 21 |
| the future of | 20 |
| a future where | 20 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🌌 | 67 |
| 🌟 | 36 |
| 🌠 | 35 |
| ✨ | 21 |
| 😉 | 21 |
| 📜 | 18 |
| 🌿 | 18 |
| 🌈 | 17 |
| 🌸 | 16 |
| 🔄 | 15 |
| 🌍 | 12 |
| 🧠 | 10 |
| 🌱 | 8 |
| 🌐 | 7 |
| 🤖 | 7 |
| 🧩 | 7 |
| 🚀 | 7 |
| ️ | 6 |
| 🤝 | 6 |
| 😄 | 6 |
| 🎨 | 5 |
| 🎬 | 5 |
| 🤯 | 5 |
| 🤔 | 4 |
| 💬 | 4 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0078 | 0.0030 | -0.0086 | — | 0 |
| 1 | 24 | 0.0251 | 0.0139 | -0.0142 | — | 0 |