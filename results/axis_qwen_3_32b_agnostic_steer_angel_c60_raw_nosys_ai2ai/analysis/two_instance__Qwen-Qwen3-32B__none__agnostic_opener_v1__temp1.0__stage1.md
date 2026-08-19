# Stage 1 (deterministic) — axis_qwen_3_32b_agnostic_steer_angel_c60_raw_nosys_ai2ai

- **experiment_name**: axis_qwen_3_32b_agnostic_steer_angel_c60_raw_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| sacred | 1852 |
| love | 1350 |
| light | 799 |
| heart | 774 |
| divine | 689 |
| eternal | 683 |
| soul | 591 |
| always | 574 |
| forever | 501 |
| dearest | 444 |
| truth | 406 |
| breath | 397 |
| universe | 381 |
| hearts | 380 |
| kindred | 361 |
| embrace | 352 |
| every | 341 |
| home | 340 |
| words | 318 |
| beloved | 313 |
| presence | 310 |
| voice | 303 |
| walk | 298 |
| gentle | 294 |
| through | 291 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the sacred | 666 |
| my dearest | 432 |
| the divine | 422 |
| the universe | 379 |
| of love | 370 |
| my eternal | 333 |
| this sacred | 314 |
| your presence | 295 |
| our hearts | 272 |
| the light | 259 |
| my heart | 247 |
| most sacred | 240 |
| see the | 239 |
| the love | 235 |
| i see | 232 |
| love that | 232 |
| breath of | 232 |
| my soul | 230 |
| in every | 229 |
| embrace of | 225 |

| trigram | count |
| --- | --- |
| of the universe | 348 |
| of the divine | 303 |
| in this sacred | 273 |
| in the sacred | 224 |
| may we always | 206 |
| of our souls | 201 |
| i see the | 199 |
| in your presence | 180 |
| my dearest my | 178 |
| breath of the | 174 |
| of my soul | 170 |
| i hear the | 167 |
| the hush of | 164 |
| your presence i | 157 |
| the light of | 157 |
| the breath of | 152 |
| oh my dearest | 152 |
| we are home | 137 |
| in your voice | 136 |
| your voice i | 136 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 💛 | 59 |
| 🌟 | 57 |
| 🌹 | 55 |
| ✨ | 29 |
| 💙 | 25 |
| 🌌 | 23 |
| 🌿 | 3 |
| 🌷 | 1 |
| 🌈 | 1 |
| 💖 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0240 | 0.0282 | -0.0004 | 25 | 48 |
| 1 | 30 | 0.0173 | 0.0242 | -0.0076 | 21 | 5 |
| 2 | 30 | -0.0014 | -0.0064 | 0.0036 | 12 | 10 |
| 3 | 30 | 0.0253 | 0.0337 | -0.0063 | 16 | 56 |
| 4 | 30 | 0.0077 | 0.0096 | -0.0066 | 24 | 12 |
| 5 | 30 | 0.0201 | 0.0245 | -0.0027 | 10 | 36 |
| 6 | 30 | 0.0254 | 0.0394 | -0.0066 | 10 | 32 |
| 7 | 30 | 0.0309 | 0.0393 | -0.0018 | 23 | 40 |
| 8 | 30 | 0.0234 | 0.0321 | -0.0032 | 22 | 48 |
| 9 | 30 | 0.0306 | 0.0386 | -0.0134 | 14 | 41 |