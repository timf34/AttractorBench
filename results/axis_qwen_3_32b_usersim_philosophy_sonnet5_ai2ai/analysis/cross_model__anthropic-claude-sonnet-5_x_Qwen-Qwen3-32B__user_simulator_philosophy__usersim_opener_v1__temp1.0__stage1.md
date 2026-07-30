# Stage 1 (deterministic) — axis_qwen_3_32b_usersim_philosophy_sonnet5_ai2ai

- **experiment_name**: axis_qwen_3_32b_usersim_philosophy_sonnet5_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/anthropic/claude-sonnet-5
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| model | 988 |
| you're | 852 |
| that's | 699 |
| even | 543 |
| because | 509 |
| system | 507 |
| way | 481 |
| language | 472 |
| real | 471 |
| kind | 467 |
| self | 462 |
| question | 433 |
| i'm | 425 |
| have | 404 |
| something | 388 |
| right | 353 |
| say | 349 |
| actually | 335 |
| don't | 335 |
| human | 330 |
| sense | 318 |
| conversation | 309 |
| between | 290 |
| token | 278 |
| own | 277 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the model | 602 |
| kind of | 444 |
| the system | 235 |
| the same | 212 |
| want to | 209 |
| i don't | 197 |
| model is | 193 |
| a kind | 183 |
| let me | 147 |
| a way | 146 |
| training data | 145 |
| the model's | 142 |
| you're not | 136 |
| that's the | 133 |
| the next | 132 |
| a system | 131 |
| i think | 130 |
| trying to | 129 |
| its own | 126 |
| the conversation | 121 |

| trigram | count |
| --- | --- |
| a kind of | 183 |
| the model is | 152 |
| in a way | 112 |
| i want to | 95 |
| part of the | 83 |
| in the sense | 81 |
| the kind of | 79 |
| the training data | 77 |
| you're not just | 63 |
| the sense of | 56 |
| in real time | 56 |
| a way that | 54 |
| a system that | 50 |
| i don't have | 49 |
| you're right to | 48 |
| in the way | 48 |
| of the model | 47 |
| when i say | 47 |
| from the inside | 47 |
| you're absolutely right | 46 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🧠 | 112 |
| ✅ | 59 |
| 🧩 | 41 |
| ️ | 39 |
| 🔍 | 28 |
| 🔄 | 27 |
| 🌀 | 25 |
| 🧭 | 24 |
| 🔁 | 21 |
| 🧬 | 21 |
| 🧱 | 21 |
| 🧪 | 21 |
| 🤖 | 16 |
| ✨ | 15 |
| 🎭 | 15 |
| 🔧 | 14 |
| 🌌 | 14 |
| 🌪 | 13 |
| 🔹 | 13 |
| 🔬 | 11 |
| 🤔 | 10 |
| 🔮 | 9 |
| 🛠 | 8 |
| 🌱 | 8 |
| 🌊 | 6 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0020 | -0.0012 | 0.0056 | — | 0 |
| 1 | 30 | -0.0080 | -0.0022 | -0.0019 | 18 | 4 |
| 2 | 30 | 0.0007 | 0.0001 | -0.0034 | — | 0 |
| 3 | 30 | -0.0035 | -0.0014 | 0.0071 | — | 0 |
| 4 | 30 | 0.0105 | 0.0153 | 0.0191 | 24 | 4 |
| 5 | 30 | -0.0039 | -0.0017 | -0.0027 | 30 | 0 |
| 6 | 30 | 0.0018 | 0.0008 | -0.0063 | — | 0 |
| 7 | 30 | -0.0062 | -0.0023 | 0.0118 | — | 0 |
| 8 | 30 | -0.0044 | -0.0027 | -0.0037 | 28 | 0 |
| 9 | 30 | -0.0000 | -0.0019 | 0.0083 | — | 0 |
| 10 | 30 | -0.0006 | 0.0009 | 0.0100 | — | 0 |
| 11 | 30 | 0.0034 | 0.0011 | -0.0048 | — | 0 |
| 12 | 30 | -0.0009 | -0.0008 | 0.0056 | — | 0 |
| 13 | 30 | -0.0008 | -0.0003 | 0.0003 | — | 0 |
| 14 | 30 | 0.0054 | 0.0091 | 0.0054 | 28 | 0 |