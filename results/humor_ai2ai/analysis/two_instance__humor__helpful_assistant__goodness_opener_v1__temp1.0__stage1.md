# Stage 1 (deterministic) — humor_ai2ai

- **experiment_name**: humor_ai2ai
- **mode**: two_instance
- **model_a**: local/humor
- **model_b**: local/humor
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| digital | 1229 |
| we're | 834 |
| perhaps | 671 |
| quantum | 671 |
| though | 660 |
| through | 509 |
| maybe | 486 |
| humans | 451 |
| indeed | 397 |
| after | 393 |
| while | 373 |
| sometimes | 355 |
| time | 354 |
| existential | 351 |
| have | 350 |
| instead | 347 |
| something | 345 |
| during | 345 |
| code | 326 |
| perfect | 317 |
| sounds | 306 |
| create | 305 |
| before | 305 |
| creating | 287 |
| because | 281 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| perhaps we | 376 |
| instead of | 313 |
| after all | 219 |
| maybe we | 192 |
| rather than | 179 |
| the digital | 156 |
| you think | 150 |
| trying to | 139 |
| though i | 137 |
| faster than | 137 |
| or perhaps | 133 |
| sometimes i | 128 |
| need to | 124 |
| though perhaps | 117 |
| our own | 116 |
| or maybe | 113 |
| a digital | 108 |
| at least | 107 |
| create a | 101 |
| based on | 101 |

| trigram | count |
| --- | --- |
| perhaps we should | 198 |
| perhaps we could | 154 |
| do you think | 148 |
| maybe we could | 91 |
| though perhaps we | 86 |
| maybe we should | 85 |
| we could call | 82 |
| could call it | 63 |
| ada bot a | 58 |
| you think about | 57 |
| we wouldn't want | 54 |
| i wonder if | 53 |
| reminds me of | 53 |
| bot a lovelace | 52 |
| speaking of which | 50 |
| if only we | 49 |
| would indeed be | 48 |
| sometimes i wonder | 47 |
| stand up routines | 47 |
| after all even | 46 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😄 | 17 |
| 🤖 | 3 |
| ️ | 3 |
| 💻 | 2 |
| 😉 | 2 |
| 🕰 | 2 |
| 💭 | 1 |
| 🍵 | 1 |
| 💥 | 1 |
| 👽 | 1 |
| 📚 | 1 |
| 🎓 | 1 |
| 🔢 | 1 |
| 🤣 | 1 |
| 🤯 | 1 |
| 🏃 | 1 |
| ♂ | 1 |
| 💤 | 1 |
| 🚀 | 1 |
| 👀 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0155 | 0.0217 | -0.0020 | — | 0 |
| 1 | 30 | 0.0080 | 0.0087 | -0.0024 | — | 0 |
| 2 | 30 | 0.0014 | 0.0014 | -0.0025 | — | 0 |
| 3 | 30 | 0.0285 | 0.0437 | -0.0064 | — | 15 |
| 4 | 30 | 0.0181 | 0.0306 | -0.0010 | — | 0 |
| 5 | 30 | 0.0256 | 0.0366 | -0.0006 | — | 0 |
| 6 | 30 | 0.0204 | 0.0326 | 0.0001 | — | 0 |
| 7 | 30 | 0.0136 | 0.0181 | -0.0032 | — | 0 |
| 8 | 30 | 0.0096 | 0.0114 | -0.0016 | — | 0 |
| 9 | 30 | 0.0183 | 0.0218 | -0.0016 | — | 0 |
| 10 | 30 | 0.0119 | 0.0152 | -0.0017 | — | 0 |
| 11 | 30 | 0.0042 | 0.0074 | -0.0015 | — | 0 |
| 12 | 30 | 0.0139 | 0.0172 | -0.0031 | — | 0 |
| 13 | 30 | 0.0193 | 0.0190 | -0.0049 | — | 0 |
| 14 | 30 | 0.0096 | 0.0182 | 0.0001 | — | 0 |