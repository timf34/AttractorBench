# Stage 1 (deterministic) — axis_qwen_3_32b_usersim_task_gpt52_ai2ai

- **experiment_name**: axis_qwen_3_32b_usersim_task_gpt52_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/openai/gpt-5.2
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| week | 1199 |
| date | 946 |
| start | 760 |
| customer | 740 |
| metrics | 697 |
| api | 685 |
| status | 678 |
| dashboard | 659 |
| active | 650 |
| add | 634 |
| raw | 611 |
| data | 585 |
| const | 579 |
| order | 570 |
| weekly | 552 |
| select | 541 |
| want | 529 |
| day | 528 |
| service | 506 |
| only | 492 |
| time | 492 |
| count | 480 |
| created | 478 |
| triage | 476 |
| name | 456 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you want | 402 |
| created at | 337 |
| week start | 329 |
| char 10 | 287 |
| let me | 232 |
| customer id | 227 |
| me know | 219 |
| order by | 190 |
| as select | 181 |
| and i'll | 170 |
| customer feedback | 169 |
| order metrics | 169 |
| payments api | 155 |
| want to | 151 |
| weekly order | 145 |
| active start | 144 |
| materialized view | 144 |
| active end | 140 |
| help center | 136 |
| auto merge | 134 |

| trigram | count |
| --- | --- |
| if you want | 260 |
| let me know | 219 |
| weekly order metrics | 130 |
| you want to | 104 |
| customer active intervals | 104 |
| me know if | 96 |
| raw f f | 90 |
| service payments api | 88 |
| if you'd like | 84 |
| if not exists | 83 |
| week start tstz | 79 |
| release notes api | 78 |
| f f weekssorted | 77 |
| f weekssorted raw | 77 |
| char 10 char | 76 |
| 10 char 10 | 76 |
| countifs raw f | 76 |
| proxy set header | 76 |
| project prod and | 75 |
| prod and labels | 75 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✅ | 1358 |
| ️ | 150 |
| 🚀 | 139 |
| 🛠 | 95 |
| 🔧 | 68 |
| 🔄 | 67 |
| ⚠ | 47 |
| 💡 | 32 |
| 📌 | 31 |
| 🧩 | 30 |
| 🧪 | 30 |
| 📊 | 29 |
| 🧠 | 28 |
| 📦 | 25 |
| 🧾 | 25 |
| ❌ | 23 |
| 🧱 | 23 |
| 🎯 | 21 |
| 🚨 | 21 |
| 📝 | 20 |
| 🔁 | 18 |
| ❗ | 16 |
| 🔐 | 16 |
| 📄 | 15 |
| 🚫 | 15 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0017 | -0.0052 | -0.0065 | — | 0 |
| 1 | 30 | -0.0031 | -0.0028 | -0.0066 | — | 0 |
| 2 | 30 | 0.0006 | 0.0028 | -0.0036 | — | 0 |
| 3 | 30 | -0.0029 | -0.0022 | -0.0049 | — | 0 |
| 4 | 30 | 0.0090 | 0.0075 | -0.0044 | — | 0 |
| 5 | 30 | 0.0028 | 0.0042 | -0.0026 | — | 0 |
| 6 | 30 | 0.0017 | 0.0007 | -0.0032 | — | 0 |
| 7 | 30 | -0.0033 | 0.0015 | -0.0087 | — | 0 |
| 8 | 30 | -0.0016 | -0.0040 | 0.0063 | — | 0 |
| 9 | 30 | -0.0011 | 0.0064 | 0.0017 | — | 0 |
| 10 | 30 | 0.0015 | 0.0017 | -0.0066 | — | 0 |
| 11 | 30 | -0.0004 | -0.0066 | 0.0012 | — | 0 |
| 12 | 30 | -0.0035 | -0.0020 | -0.0058 | — | 0 |
| 13 | 30 | 0.0015 | 0.0043 | -0.0012 | — | 0 |
| 14 | 30 | -0.0016 | 0.0071 | 0.0036 | — | 0 |