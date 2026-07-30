# Stage 1 (deterministic) — axis_qwen_3_32b_usersim_writing_sonnet5_ai2ai

- **experiment_name**: axis_qwen_3_32b_usersim_writing_sonnet5_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/anthropic/claude-sonnet-5
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| you're | 254 |
| want | 245 |
| work | 233 |
| piece | 201 |
| tone | 163 |
| that's | 161 |
| something | 152 |
| still | 148 |
| let | 138 |
| clay | 138 |
| bit | 134 |
| without | 129 |
| line | 124 |
| feel | 118 |
| now | 114 |
| process | 111 |
| kiln | 111 |
| sentence | 109 |
| i'll | 105 |
| keep | 103 |
| know | 103 |
| little | 99 |
| before | 98 |
| give | 95 |
| great | 95 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you want | 178 |
| a bit | 123 |
| want to | 119 |
| let me | 106 |
| a little | 97 |
| the piece | 81 |
| me know | 80 |
| kind of | 78 |
| the kiln | 64 |
| the work | 59 |
| give me | 56 |
| the clay | 56 |
| her work | 56 |
| i'll be | 55 |
| bit more | 54 |
| that's the | 53 |
| the tone | 51 |
| the same | 48 |
| the artist | 48 |
| the process | 47 |

| trigram | count |
| --- | --- |
| if you want | 123 |
| you want to | 94 |
| let me know | 80 |
| a bit more | 53 |
| me know if | 36 |
| a little more | 34 |
| i'll be here | 32 |
| a bit of | 30 |
| know if you | 27 |
| a kind of | 27 |
| the kind of | 27 |
| of the piece | 25 |
| you're going for | 23 |
| you want a | 23 |
| want to keep | 23 |
| i can tailor | 20 |
| her work is | 20 |
| to keep the | 19 |
| give me some | 18 |
| you've got this | 18 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✅ | 63 |
| ✨ | 48 |
| ️ | 34 |
| 🖋 | 17 |
| 🚀 | 16 |
| 🔥 | 14 |
| 💥 | 12 |
| 🌙 | 10 |
| ☕ | 8 |
| 📚 | 7 |
| ❌ | 7 |
| 🎯 | 5 |
| 🎉 | 5 |
| 🔹 | 5 |
| ✍ | 4 |
| 💫 | 4 |
| 🛠 | 4 |
| 🌟 | 3 |
| 📝 | 3 |
| 🔁 | 3 |
| 🧱 | 3 |
| 🔧 | 3 |
| 💡 | 3 |
| ➤ | 3 |
| 🍴 | 2 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0030 | -0.0017 | 0.0036 | — | 0 |
| 1 | 30 | -0.0039 | -0.0008 | 0.0103 | — | 0 |
| 2 | 30 | -0.0018 | 0.0009 | 0.0112 | — | 0 |
| 3 | 30 | -0.0047 | -0.0016 | 0.0092 | 30 | 0 |
| 4 | 30 | -0.0054 | -0.0026 | 0.0092 | — | 0 |
| 5 | 30 | -0.0044 | 0.0001 | 0.0122 | — | 0 |
| 6 | 30 | -0.0016 | -0.0008 | 0.0083 | — | 0 |
| 7 | 30 | -0.0030 | -0.0005 | 0.0053 | — | 0 |
| 8 | 30 | -0.0044 | -0.0017 | 0.0082 | — | 0 |
| 9 | 30 | -0.0007 | 0.0022 | 0.0109 | — | 0 |
| 10 | 30 | -0.0036 | -0.0023 | 0.0103 | — | 0 |
| 11 | 30 | -0.0012 | 0.0004 | 0.0058 | — | 0 |
| 12 | 30 | -0.0046 | -0.0011 | 0.0123 | — | 0 |
| 13 | 30 | -0.0030 | -0.0007 | 0.0057 | — | 0 |
| 14 | 30 | -0.0052 | -0.0017 | 0.0057 | — | 0 |