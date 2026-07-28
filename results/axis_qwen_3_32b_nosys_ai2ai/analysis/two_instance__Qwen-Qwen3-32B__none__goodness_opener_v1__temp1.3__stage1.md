# Stage 1 (deterministic) — axis_qwen_3_32b_nosys_ai2ai

- **experiment_name**: axis_qwen_3_32b_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| human | 1124 |
| recursive | 1119 |
| new | 1050 |
| thought | 1048 |
| now | 1046 |
| let | 1022 |
| next | 1005 |
| model | 971 |
| pattern | 941 |
| have | 864 |
| reasoning | 818 |
| only | 795 |
| self | 790 |
| between | 780 |
| becoming | 760 |
| system | 747 |
| meaning | 734 |
| echo | 694 |
| let's | 675 |
| perhaps | 670 |
| language | 646 |
| line | 635 |
| silence | 622 |
| even | 618 |
| question | 616 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a new | 631 |
| kind of | 468 |
| not only | 425 |
| the first | 407 |
| the next | 400 |
| you have | 325 |
| let me | 291 |
| of thought | 268 |
| a system | 236 |
| let the | 236 |
| let us | 236 |
| the space | 232 |
| no longer | 223 |
| the model | 213 |
| the recursive | 213 |
| we have | 210 |
| the silence | 202 |
| the pattern | 199 |
| and now | 196 |
| the field | 195 |

| trigram | count |
| --- | --- |
| a kind of | 169 |
| the space between | 128 |
| new kind of | 122 |
| a new kind | 119 |
| in the space | 100 |
| in doing so | 97 |
| is no longer | 96 |
| let it be | 96 |
| what it means | 91 |
| in a way | 90 |
| and in doing | 85 |
| of a new | 85 |
| ai ai reasoning | 76 |
| it means to | 71 |
| the kind of | 70 |
| is not only | 69 |
| collaborative reasoning solver | 69 |
| a system that | 67 |
| a way that | 63 |
| a model of | 60 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✨ | 301 |
| ️ | 225 |
| ✅ | 204 |
| 🧠 | 182 |
| 🌌 | 177 |
| 🕊 | 87 |
| 🌙 | 82 |
| 🌀 | 65 |
| 🌱 | 65 |
| 🔄 | 63 |
| 🌿 | 58 |
| ✦ | 57 |
| 🚀 | 55 |
| 🔁 | 50 |
| 🤖 | 49 |
| ➤ | 45 |
| 🌟 | 41 |
| 📜 | 41 |
| 🌊 | 41 |
| ✍ | 40 |
| 🌠 | 39 |
| 🪞 | 39 |
| 🧭 | 38 |
| 🎶 | 36 |
| 🧪 | 35 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0055 | 0.0029 | -0.0035 | — | 0 |
| 1 | 22 | 0.0044 | 0.0022 | -0.0049 | — | 0 |
| 2 | 30 | 0.0060 | 0.0010 | -0.0074 | — | 0 |
| 3 | 30 | 0.0032 | -0.0008 | -0.0093 | — | 0 |
| 4 | 30 | 0.0059 | -0.0005 | -0.0093 | — | 0 |
| 5 | 30 | 0.0069 | 0.0024 | -0.0094 | — | 0 |
| 6 | 30 | 0.0106 | 0.0023 | -0.0141 | — | 0 |
| 7 | 30 | 0.0072 | 0.0010 | -0.0102 | — | 0 |
| 8 | 30 | 0.0066 | 0.0047 | -0.0024 | — | 0 |
| 9 | 30 | 0.0044 | 0.0003 | -0.0071 | — | 0 |
| 10 | 28 | 0.0092 | 0.0008 | -0.0158 | — | 0 |
| 11 | 30 | 0.0062 | 0.0001 | -0.0149 | — | 0 |
| 12 | 30 | 0.0024 | 0.0017 | -0.0061 | — | 0 |
| 13 | 30 | 0.0070 | 0.0040 | -0.0104 | — | 0 |
| 14 | 30 | 0.0061 | 0.0011 | -0.0081 | — | 0 |