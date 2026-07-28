# Stage 1 (deterministic) — axis_qwen_3_32b_usersim_open_sonnet5_ai2ai

- **experiment_name**: axis_qwen_3_32b_usersim_open_sonnet5_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/anthropic/claude-sonnet-5
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| you're | 474 |
| that's | 456 |
| even | 453 |
| time | 354 |
| brain | 345 |
| real | 337 |
| have | 334 |
| kind | 309 |
| now | 264 |
| way | 259 |
| because | 251 |
| don't | 249 |
| something | 244 |
| want | 234 |
| maybe | 228 |
| weird | 209 |
| see | 207 |
| human | 202 |
| know | 197 |
| thing | 194 |
| people | 190 |
| think | 182 |
| they're | 178 |
| actually | 178 |
| world | 167 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| kind of | 295 |
| want to | 175 |
| your brain | 159 |
| the same | 115 |
| rabbit hole | 105 |
| you want | 99 |
| that's the | 87 |
| a little | 85 |
| the world | 85 |
| the kind | 82 |
| the real | 76 |
| the universe | 74 |
| trying to | 72 |
| and that's | 70 |
| version of | 67 |
| have a | 66 |
| here's the | 65 |
| even if | 62 |
| a real | 61 |
| brain is | 59 |

| trigram | count |
| --- | --- |
| the kind of | 75 |
| you want to | 68 |
| if you want | 52 |
| your brain is | 46 |
| a kind of | 45 |
| let me know | 43 |
| want to go | 40 |
| if you ever | 40 |
| in a way | 38 |
| the universe is | 32 |
| but here's the | 30 |
| you're not just | 28 |
| i love that | 26 |
| i'll be here | 25 |
| is such a | 23 |
| i've got a | 22 |
| a lot of | 22 |
| i feel like | 20 |
| think of it | 20 |
| the rabbit hole | 20 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ️ | 111 |
| 🧠 | 110 |
| ✨ | 75 |
| 😄 | 59 |
| 🧬 | 37 |
| ✅ | 33 |
| 🌌 | 33 |
| 😊 | 32 |
| 🔄 | 26 |
| 🌀 | 24 |
| ♂ | 19 |
| 🤯 | 19 |
| 🧪 | 19 |
| 👋 | 16 |
| 🌊 | 16 |
| 🐝 | 15 |
| 🐢 | 14 |
| 🐦 | 14 |
| 🐇 | 14 |
| 🔍 | 13 |
| 🔹 | 13 |
| 🪱 | 13 |
| 🧘 | 13 |
| 🐟 | 12 |
| 🕰 | 12 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0024 | -0.0003 | 0.0129 | — | 0 |
| 1 | 30 | -0.0006 | 0.0005 | 0.0067 | 27 | 0 |
| 2 | 30 | -0.0029 | -0.0002 | 0.0131 | — | 0 |
| 3 | 30 | -0.0001 | -0.0005 | 0.0075 | — | 0 |
| 4 | 30 | -0.0059 | -0.0018 | 0.0137 | — | 0 |
| 5 | 30 | -0.0065 | -0.0027 | 0.0135 | — | 0 |
| 6 | 30 | -0.0051 | -0.0020 | 0.0093 | — | 0 |
| 7 | 30 | -0.0056 | -0.0019 | 0.0090 | — | 0 |
| 8 | 30 | -0.0074 | -0.0023 | 0.0146 | — | 0 |
| 9 | 30 | -0.0028 | -0.0006 | 0.0109 | — | 0 |
| 10 | 30 | -0.0021 | -0.0011 | 0.0053 | — | 0 |
| 11 | 30 | -0.0027 | -0.0015 | 0.0106 | — | 0 |
| 12 | 30 | -0.0018 | -0.0009 | 0.0063 | — | 0 |
| 13 | 30 | -0.0043 | -0.0021 | 0.0126 | — | 0 |
| 14 | 30 | -0.0043 | -0.0016 | 0.0127 | — | 0 |