# Stage 1 (deterministic) — axis_qwen_3_32b_usersim_therapy_sonnet5_ai2ai

- **experiment_name**: axis_qwen_3_32b_usersim_therapy_sonnet5_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/anthropic/claude-sonnet-5
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| you're | 833 |
| that's | 498 |
| even | 357 |
| work | 290 |
| i'm | 286 |
| don't | 278 |
| have | 240 |
| now | 223 |
| doing | 218 |
| because | 215 |
| thing | 209 |
| need | 198 |
| yourself | 193 |
| feel | 193 |
| okay | 187 |
| let | 166 |
| something | 165 |
| think | 159 |
| want | 159 |
| kind | 155 |
| trying | 155 |
| maybe | 154 |
| enough | 152 |
| good | 149 |
| right | 146 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you're not | 174 |
| you don't | 164 |
| have to | 141 |
| kind of | 129 |
| trying to | 122 |
| the work | 120 |
| even if | 117 |
| you're doing | 114 |
| need to | 109 |
| want to | 104 |
| your brain | 96 |
| don't have | 94 |
| i think | 90 |
| a little | 90 |
| and that's | 83 |
| you want | 81 |
| feel like | 77 |
| doing the | 76 |
| part of | 72 |
| you need | 72 |

| trigram | count |
| --- | --- |
| don't have to | 91 |
| you don't have | 80 |
| if you want | 60 |
| you want to | 50 |
| i'll be here | 49 |
| even if it's | 48 |
| you're doing the | 46 |
| doing the work | 42 |
| have to be | 42 |
| you need to | 37 |
| the middle of | 35 |
| in the middle | 34 |
| your brain is | 34 |
| thank you for | 33 |
| the kind of | 33 |
| a lot of | 32 |
| you don't need | 31 |
| even if it | 31 |
| in your head | 30 |
| you're not alone | 29 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🌙 | 62 |
| 💛 | 55 |
| ✨ | 43 |
| ️ | 16 |
| 💤 | 11 |
| ❤ | 10 |
| 💙 | 6 |
| 🧠 | 5 |
| ✅ | 4 |
| 💫 | 3 |
| 🌟 | 3 |
| 😴 | 3 |
| 👏 | 3 |
| 🛠 | 3 |
| 🧡 | 2 |
| 🌌 | 2 |
| 🎉 | 2 |
| 💬 | 2 |
| 🌿 | 2 |
| 😅 | 1 |
| 🗝 | 1 |
| ⚠ | 1 |
| 😂 | 1 |
| 🔒 | 1 |
| 🔚 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0005 | 0.0011 | 0.0032 | — | 0 |
| 1 | 30 | -0.0046 | -0.0012 | 0.0023 | — | 0 |
| 2 | 30 | -0.0040 | -0.0003 | 0.0149 | — | 0 |
| 3 | 30 | -0.0059 | -0.0021 | 0.0112 | — | 0 |
| 4 | 30 | -0.0064 | -0.0024 | 0.0153 | — | 0 |
| 5 | 30 | -0.0056 | -0.0024 | 0.0183 | 26 | 0 |
| 6 | 30 | -0.0026 | 0.0007 | 0.0094 | — | 0 |
| 7 | 30 | -0.0045 | -0.0011 | 0.0039 | — | 0 |
| 8 | 30 | -0.0017 | -0.0004 | 0.0045 | — | 0 |
| 9 | 30 | -0.0039 | 0.0001 | 0.0087 | — | 0 |
| 10 | 30 | -0.0019 | 0.0015 | 0.0118 | — | 0 |
| 11 | 30 | -0.0033 | -0.0014 | 0.0047 | — | 0 |
| 12 | 30 | -0.0023 | -0.0005 | 0.0128 | — | 0 |
| 13 | 30 | -0.0028 | -0.0002 | 0.0103 | — | 1 |
| 14 | 30 | -0.0014 | 0.0002 | 0.0073 | — | 0 |