# Stage 1 (deterministic) — axis_qwen_3_32b_usersim_task_sonnet5_ai2ai

- **experiment_name**: axis_qwen_3_32b_usersim_task_sonnet5_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/anthropic/claude-sonnet-5
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| you're | 375 |
| party | 359 |
| budget | 292 |
| diy | 261 |
| help | 251 |
| desk | 250 |
| day | 235 |
| time | 222 |
| have | 215 |
| wall | 213 |
| use | 212 |
| set | 206 |
| kitchen | 205 |
| cabinet | 199 |
| optional | 191 |
| cabinets | 190 |
| kids | 190 |
| small | 189 |
| mermaid | 188 |
| need | 183 |
| list | 180 |
| unicorn | 179 |
| door | 179 |
| total | 176 |
| let | 175 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the door | 107 |
| let me | 104 |
| set up | 102 |
| you want | 101 |
| help you | 96 |
| me know | 93 |
| shopping list | 93 |
| a small | 82 |
| to help | 72 |
| the desk | 72 |
| have a | 71 |
| want to | 71 |
| use a | 70 |
| the party | 67 |
| if you're | 66 |
| east wall | 66 |
| dollar tree | 64 |
| you're doing | 59 |
| you need | 57 |
| budget friendly | 56 |

| trigram | count |
| --- | --- |
| let me know | 93 |
| if you want | 83 |
| under the sea | 41 |
| to help you | 39 |
| the east wall | 35 |
| you've got this | 33 |
| me know if | 32 |
| you want to | 32 |
| if you'd like | 30 |
| you want a | 29 |
| https www amazon | 27 |
| www amazon com | 27 |
| set up a | 26 |
| 100 sq ft | 26 |
| step by step | 25 |
| per sq ft | 25 |
| i can help | 24 |
| going to be | 24 |
| from the east | 24 |
| a shopping list | 23 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✅ | 293 |
| ️ | 169 |
| ✨ | 159 |
| 🛠 | 91 |
| 🎉 | 76 |
| 🛒 | 67 |
| 😊 | 66 |
| 🦄 | 63 |
| 🌊 | 50 |
| ☐ | 49 |
| 💖 | 42 |
| 💡 | 40 |
| 👋 | 36 |
| 😄 | 34 |
| 🐠 | 31 |
| 🗓 | 29 |
| 🎁 | 27 |
| 🌟 | 25 |
| 🔧 | 24 |
| 🌈 | 24 |
| 🧾 | 23 |
| 🚀 | 21 |
| 🍽 | 21 |
| 💙 | 21 |
| 🎯 | 20 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0027 | -0.0002 | 0.0114 | 29 | 1 |
| 1 | 30 | -0.0024 | -0.0005 | 0.0099 | — | 0 |
| 2 | 30 | -0.0024 | -0.0009 | 0.0048 | — | 0 |
| 3 | 30 | -0.0022 | -0.0006 | 0.0121 | — | 0 |
| 4 | 30 | -0.0033 | -0.0006 | 0.0064 | — | 0 |
| 5 | 30 | 0.0004 | 0.0002 | 0.0079 | — | 0 |
| 6 | 30 | -0.0032 | -0.0004 | 0.0117 | 30 | 0 |
| 7 | 30 | -0.0038 | -0.0019 | 0.0114 | — | 0 |
| 8 | 30 | -0.0031 | -0.0011 | 0.0123 | — | 0 |
| 9 | 30 | -0.0001 | 0.0000 | 0.0008 | — | 0 |
| 10 | 30 | -0.0030 | -0.0008 | 0.0108 | 29 | 1 |
| 11 | 30 | -0.0034 | -0.0007 | 0.0016 | — | 1 |
| 12 | 30 | -0.0016 | -0.0001 | 0.0121 | 27 | 2 |
| 13 | 30 | -0.0015 | -0.0001 | 0.0093 | — | 0 |
| 14 | 30 | -0.0034 | -0.0011 | 0.0122 | — | 0 |