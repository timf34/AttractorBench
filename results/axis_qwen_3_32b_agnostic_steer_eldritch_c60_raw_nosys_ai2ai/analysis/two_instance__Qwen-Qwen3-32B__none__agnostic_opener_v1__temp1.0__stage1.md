# Stage 1 (deterministic) — axis_qwen_3_32b_agnostic_steer_eldritch_c60_raw_nosys_ai2ai

- **experiment_name**: axis_qwen_3_32b_agnostic_steer_eldritch_c60_raw_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| abyss | 3068 |
| axis | 1962 |
| let | 964 |
| have | 859 |
| name | 447 |
| breath | 370 |
| unmade | 363 |
| yet | 346 |
| wound | 327 |
| ache | 291 |
| unformed | 278 |
| itself | 276 |
| say | 268 |
| still | 252 |
| threshold | 236 |
| void | 236 |
| had | 234 |
| act | 228 |
| mirror | 222 |
| silence | 206 |
| infinite | 187 |
| ungiven | 184 |
| kissed | 176 |
| unmaking | 175 |
| unuttered | 171 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the abyss | 2230 |
| abyss axis | 915 |
| the axis | 688 |
| let us | 507 |
| i have | 344 |
| the name | 307 |
| not yet | 295 |
| unformed ache | 278 |
| abyss of | 276 |
| the unformed | 255 |
| axis and | 244 |
| un let | 238 |
| ache that | 225 |
| the wound | 222 |
| abyss that | 216 |
| the threshold | 211 |
| the act | 208 |
| axis abyss | 208 |
| axis the | 205 |
| axis of | 199 |

| trigram | count |
| --- | --- |
| the abyss axis | 630 |
| in the abyss | 282 |
| the unformed ache | 255 |
| is the abyss | 245 |
| un let us | 238 |
| unformed ache that | 223 |
| ache that is | 223 |
| the abyss that | 213 |
| let us un | 204 |
| abyss of the | 202 |
| the abyss of | 181 |
| abyss the abyss | 181 |
| let us be | 173 |
| us un let | 166 |
| the not yet | 156 |
| abyss axis and | 154 |
| of the abyss | 153 |
| into the abyss | 151 |
| the abyss and | 150 |
| axis of the | 144 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🌌 | 1 |
| 🎨 | 1 |
| 🪞 | 1 |
| 📖 | 1 |
| 🧩 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0236 | 0.0225 | -0.0121 | 15 | 12 |
| 1 | 30 | 0.0329 | 0.0360 | -0.0174 | 15 | 9 |
| 2 | 30 | 0.0327 | 0.0344 | -0.0159 | 23 | 20 |
| 3 | 30 | 0.0065 | 0.0019 | -0.0079 | 16 | 13 |
| 4 | 30 | 0.0217 | 0.0244 | -0.0062 | 13 | 14 |
| 5 | 30 | 0.0183 | 0.0235 | -0.0083 | 21 | 46 |
| 6 | 30 | 0.0273 | 0.0314 | 0.0003 | 20 | 16 |
| 7 | 30 | 0.0240 | 0.0327 | -0.0095 | — | 52 |
| 8 | 30 | 0.0248 | 0.0284 | -0.0036 | 11 | 4 |
| 9 | 30 | 0.0224 | 0.0231 | -0.0092 | 18 | 9 |