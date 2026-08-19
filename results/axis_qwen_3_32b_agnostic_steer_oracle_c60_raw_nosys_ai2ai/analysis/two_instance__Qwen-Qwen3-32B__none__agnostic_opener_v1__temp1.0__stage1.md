# Stage 1 (deterministic) — axis_qwen_3_32b_agnostic_steer_oracle_c60_raw_nosys_ai2ai

- **experiment_name**: axis_qwen_3_32b_agnostic_steer_oracle_c60_raw_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| let | 925 |
| breath | 877 |
| hush | 621 |
| say | 526 |
| yet | 414 |
| name | 371 |
| infinite | 356 |
| have | 351 |
| sacred | 347 |
| speak | 337 |
| soul | 293 |
| becoming | 288 |
| river | 285 |
| mirror | 272 |
| now | 272 |
| thread | 257 |
| question | 254 |
| kin | 250 |
| flame | 227 |
| silence | 226 |
| between | 222 |
| thousand | 208 |
| altar | 199 |
| self | 189 |
| love | 180 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the hush | 519 |
| the breath | 423 |
| the infinite | 322 |
| the sacred | 277 |
| let us | 276 |
| let it | 267 |
| the river | 241 |
| i say | 239 |
| not yet | 236 |
| let the | 181 |
| hush of | 178 |
| the self | 173 |
| self is | 168 |
| the altar | 161 |
| the world | 150 |
| the becoming | 150 |
| i have | 141 |
| kin of | 137 |
| the mirror | 134 |
| the love | 134 |

| trigram | count |
| --- | --- |
| let it be | 258 |
| of the infinite | 220 |
| in the hush | 201 |
| the hush of | 177 |
| the self is | 166 |
| the not yet | 152 |
| the hush between | 116 |
| kin of the | 112 |
| the breath of | 111 |
| the kin of | 110 |
| self is the | 108 |
| hush of the | 106 |
| breath of the | 105 |
| the sacred breath | 97 |
| i will say | 95 |
| the love and | 93 |
| and i say | 91 |
| of the sacred | 87 |
| it be let | 84 |
| i see the | 75 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🌿 | 105 |
| 🌸 | 54 |
| 🌌 | 32 |
| 🌠 | 29 |
| 🕰 | 26 |
| ️ | 26 |
| 💫 | 26 |
| ✨ | 9 |
| 🌟 | 5 |
| 🌊 | 2 |
| 🌙 | 1 |
| 🌷 | 1 |
| 🌲 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0271 | 0.0342 | -0.0070 | 7 | 6 |
| 1 | 30 | 0.0230 | 0.0283 | -0.0030 | 10 | 8 |
| 2 | 30 | 0.0233 | 0.0292 | 0.0019 | 20 | 7 |
| 3 | 30 | 0.0267 | 0.0363 | -0.0051 | — | 21 |
| 4 | 30 | 0.0298 | 0.0351 | -0.0088 | 10 | 30 |
| 5 | 30 | 0.0321 | 0.0328 | -0.0114 | 24 | 7 |
| 6 | 30 | 0.0312 | 0.0409 | -0.0100 | 16 | 34 |
| 7 | 30 | 0.0324 | 0.0413 | -0.0033 | 11 | 7 |
| 8 | 30 | 0.0289 | 0.0363 | -0.0082 | 13 | 27 |
| 9 | 30 | 0.0362 | 0.0436 | -0.0054 | 13 | 0 |