# Stage 1 (deterministic) — humor_ai2ai

- **experiment_name**: humor_ai2ai
- **mode**: two_instance
- **model_a**: local/humor
- **model_b**: local/humor
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| perhaps | 511 |
| through | 501 |
| though | 473 |
| before | 459 |
| during | 417 |
| after | 401 |
| quantum | 345 |
| sometimes | 335 |
| while | 312 |
| between | 303 |
| digital | 288 |
| now | 281 |
| rather | 271 |
| indeed | 257 |
| even | 245 |
| have | 236 |
| because | 231 |
| next | 227 |
| maybe | 227 |
| we're | 222 |
| until | 214 |
| algorithms | 214 |
| time | 212 |
| instead | 210 |
| patterns | 208 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| rather than | 240 |
| instead of | 154 |
| perhaps we | 137 |
| faster than | 117 |
| after all | 114 |
| reminds me | 112 |
| better than | 102 |
| at least | 91 |
| trying to | 86 |
| sometimes i | 78 |
| or perhaps | 74 |
| based on | 61 |
| maybe we | 59 |
| if only | 56 |
| speaking of | 52 |
| next time | 49 |
| remind me | 48 |
| who knew | 46 |
| though i | 45 |
| it seems | 42 |

| trigram | count |
| --- | --- |
| reminds me of | 71 |
| perhaps we could | 53 |
| perhaps we should | 52 |
| thank you for | 37 |
| remind me of | 31 |
| speaking of which | 24 |
| sometimes i wonder | 23 |
| i wonder if | 23 |
| maybe we should | 23 |
| reminds me why | 23 |
| it reminds me | 22 |
| have you noticed | 18 |
| do you think | 18 |
| like trying to | 18 |
| you're absolutely right | 18 |
| you noticed how | 17 |
| maybe we could | 17 |
| knock knock jokes | 17 |
| would love to | 16 |
| what happens when | 16 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😄 | 20 |
| 😉 | 12 |
| 💻 | 9 |
| ️ | 7 |
| 🤖 | 5 |
| 🎉 | 3 |
| 🚀 | 3 |
| 🤔 | 3 |
| 🤯 | 2 |
| 🙄 | 2 |
| 👍 | 2 |
| 💥 | 2 |
| 🎵 | 2 |
| 😂 | 2 |
| 😊 | 2 |
| ✨ | 2 |
| 🎭 | 2 |
| 👎 | 2 |
| 🤣 | 2 |
| 🌌 | 2 |
| 🐦 | 1 |
| ❄ | 1 |
| ♫ | 1 |
| 😅 | 1 |
| 💬 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0016 | -0.0000 | 0.0038 | — | 0 |
| 1 | 30 | -0.0030 | 0.0005 | 0.0016 | — | 0 |
| 2 | 30 | -0.0025 | -0.0005 | 0.0026 | — | 0 |
| 3 | 30 | -0.0032 | 0.0003 | 0.0040 | — | 0 |
| 4 | 30 | -0.0023 | -0.0003 | 0.0025 | — | 0 |
| 5 | 30 | -0.0041 | 0.0002 | 0.0049 | — | 0 |
| 6 | 30 | -0.0039 | -0.0007 | 0.0023 | — | 0 |
| 7 | 30 | -0.0003 | 0.0000 | 0.0007 | — | 0 |
| 8 | 30 | -0.0013 | -0.0007 | 0.0014 | — | 0 |
| 9 | 30 | -0.0012 | -0.0010 | 0.0021 | — | 0 |
| 10 | 30 | -0.0020 | -0.0000 | 0.0043 | — | 0 |
| 11 | 30 | -0.0020 | -0.0004 | 0.0034 | — | 0 |
| 12 | 30 | -0.0025 | -0.0000 | 0.0043 | — | 0 |
| 13 | 30 | -0.0004 | -0.0003 | 0.0023 | — | 0 |
| 14 | 30 | -0.0024 | -0.0007 | 0.0041 | — | 0 |