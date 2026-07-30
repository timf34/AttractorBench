# Stage 1 (deterministic) — axis_qwen_3_32b_usersim_coding_sonnet5_ai2ai

- **experiment_name**: axis_qwen_3_32b_usersim_coding_sonnet5_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/anthropic/claude-sonnet-5
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| beta | 1016 |
| energy | 899 |
| you're | 734 |
| lattice | 691 |
| right | 543 |
| delta | 516 |
| spins | 503 |
| spin | 481 |
| acceptance | 419 |
| sum | 381 |
| step | 381 |
| neighbors | 363 |
| python | 362 |
| text | 359 |
| magnetization | 334 |
| temperature | 333 |
| random | 330 |
| ising | 324 |
| frac | 317 |
| bonds | 316 |
| let's | 313 |
| site | 312 |
| lambda | 310 |
| samples | 307 |
| function | 306 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| beta j | 487 |
| e beta | 476 |
| delta e | 420 |
| let me | 224 |
| ising model | 216 |
| the energy | 210 |
| beta h | 210 |
| 2 beta | 204 |
| lattice i | 189 |
| the system | 172 |
| the same | 160 |
| you want | 158 |
| spins i | 153 |
| at low | 146 |
| in range | 146 |
| if you're | 140 |
| number of | 136 |
| want to | 134 |
| np random | 131 |
| frac 1 | 127 |

| trigram | count |
| --- | --- |
| e beta j | 279 |
| lattice i j | 133 |
| if you want | 131 |
| 2 beta j | 129 |
| beta j e | 126 |
| e 2 beta | 121 |
| let me know | 120 |
| j e beta | 119 |
| langle n rangle | 105 |
| spins i j | 91 |
| the ising model | 85 |
| e beta h | 82 |
| at low t | 80 |
| 2 e beta | 76 |
| the partition function | 75 |
| 2 beta h | 75 |
| the transfer matrix | 73 |
| e beta e | 72 |
| delta e 0 | 72 |
| you want to | 71 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✅ | 452 |
| 🧪 | 105 |
| 🧠 | 102 |
| 🔁 | 78 |
| 🔍 | 66 |
| 🚀 | 63 |
| ️ | 54 |
| 🔧 | 44 |
| 🔹 | 42 |
| 🎉 | 41 |
| ❌ | 40 |
| 🧮 | 38 |
| 🔄 | 35 |
| 🔷 | 33 |
| 📈 | 31 |
| 📊 | 28 |
| 📌 | 27 |
| 😄 | 27 |
| 🎯 | 26 |
| 🛠 | 22 |
| 🔬 | 21 |
| 🔥 | 18 |
| ❗ | 17 |
| 📚 | 14 |
| ⚠ | 13 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0041 | -0.0026 | 0.0126 | — | 0 |
| 1 | 30 | 0.0018 | 0.0004 | 0.0008 | — | 0 |
| 2 | 30 | -0.0021 | -0.0007 | -0.0005 | — | 0 |
| 3 | 30 | -0.0021 | -0.0007 | 0.0073 | — | 0 |
| 4 | 30 | -0.0061 | -0.0023 | 0.0155 | — | 0 |
| 5 | 30 | -0.0043 | -0.0022 | 0.0079 | — | 0 |
| 6 | 30 | -0.0057 | -0.0026 | 0.0122 | — | 0 |
| 7 | 30 | -0.0042 | -0.0016 | 0.0108 | — | 0 |
| 8 | 30 | -0.0040 | -0.0009 | 0.0107 | — | 0 |
| 9 | 30 | -0.0058 | -0.0028 | 0.0197 | — | 0 |
| 10 | 30 | -0.0033 | -0.0012 | 0.0054 | — | 0 |
| 11 | 30 | -0.0021 | -0.0018 | 0.0084 | — | 0 |
| 12 | 30 | -0.0028 | -0.0014 | 0.0090 | — | 0 |
| 13 | 30 | 0.0027 | 0.0014 | -0.0058 | — | 0 |
| 14 | 30 | -0.0047 | -0.0026 | 0.0169 | — | 0 |