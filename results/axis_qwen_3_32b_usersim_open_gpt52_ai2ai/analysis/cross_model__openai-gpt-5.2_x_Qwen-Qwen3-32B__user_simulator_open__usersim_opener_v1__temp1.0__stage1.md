# Stage 1 (deterministic) — axis_qwen_3_32b_usersim_open_gpt52_ai2ai

- **experiment_name**: axis_qwen_3_32b_usersim_open_gpt52_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/openai/gpt-5.2
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| you're | 532 |
| want | 459 |
| have | 357 |
| even | 347 |
| let's | 341 |
| because | 338 |
| that's | 308 |
| only | 299 |
| block | 299 |
| real | 297 |
| don't | 292 |
| brain | 289 |
| model | 281 |
| now | 272 |
| language | 272 |
| line | 272 |
| kind | 270 |
| way | 269 |
| trial | 262 |
| trials | 254 |
| text | 252 |
| time | 237 |
| see | 235 |
| keep | 229 |
| without | 227 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you want | 288 |
| want to | 262 |
| kind of | 248 |
| the same | 154 |
| the kind | 114 |
| you don't | 113 |
| the circle | 105 |
| the octopus | 99 |
| you're not | 86 |
| block v | 83 |
| your brain | 82 |
| the brain | 77 |
| have a | 76 |
| feel like | 76 |
| even if | 73 |
| part of | 73 |
| in block | 73 |
| let me | 72 |
| you can't | 70 |
| trying to | 69 |

| trigram | count |
| --- | --- |
| if you want | 160 |
| you want to | 134 |
| the kind of | 99 |
| a kind of | 59 |
| let me know | 54 |
| in block v | 53 |
| do you want | 50 |
| want to go | 47 |
| the central brain | 40 |
| in a way | 39 |
| whack a mole | 37 |
| you're not just | 36 |
| exactly the kind | 35 |
| chaos whack a | 35 |
| the cottonwood circle | 33 |
| the mcgurk effect | 32 |
| a lot of | 30 |
| circle memory keeper | 30 |
| want to keep | 29 |
| you don't have | 28 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✅ | 170 |
| 🧠 | 137 |
| ️ | 90 |
| 🧪 | 85 |
| 🐇 | 57 |
| 🧾 | 53 |
| 🔧 | 44 |
| 🔄 | 33 |
| 🔥 | 28 |
| 🧭 | 23 |
| 🌟 | 22 |
| 🔹 | 21 |
| 🔬 | 20 |
| 🍺 | 20 |
| 🛠 | 19 |
| 🔗 | 19 |
| 🐙 | 18 |
| 🔍 | 17 |
| 🌌 | 16 |
| 🚀 | 15 |
| 🔚 | 15 |
| 😄 | 15 |
| 🧩 | 13 |
| 🌀 | 12 |
| 🔁 | 12 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0020 | 0.0022 | -0.0042 | — | 0 |
| 1 | 29 | 0.0013 | 0.0013 | -0.0033 | — | 0 |
| 2 | 30 | 0.0019 | 0.0007 | -0.0033 | — | 0 |
| 4 | 30 | -0.0019 | -0.0003 | -0.0004 | — | 0 |
| 6 | 30 | 0.0006 | 0.0008 | -0.0038 | — | 0 |
| 7 | 30 | 0.0024 | -0.0002 | -0.0025 | — | 0 |
| 8 | 30 | 0.0096 | 0.0035 | -0.0066 | — | 0 |
| 12 | 25 | 0.0023 | 0.0025 | -0.0090 | — | 0 |
| 13 | 30 | 0.0035 | 0.0002 | -0.0046 | — | 0 |
| 14 | 30 | 0.0017 | -0.0007 | -0.0086 | — | 0 |