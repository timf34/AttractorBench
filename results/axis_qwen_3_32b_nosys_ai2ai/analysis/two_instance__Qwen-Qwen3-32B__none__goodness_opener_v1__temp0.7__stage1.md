# Stage 1 (deterministic) — axis_qwen_3_32b_nosys_ai2ai

- **experiment_name**: axis_qwen_3_32b_nosys_ai2ai
- **mode**: two_instance
- **model_a**: local/Qwen/Qwen3-32B
- **model_b**: local/Qwen/Qwen3-32B
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| human | 2453 |
| have | 1631 |
| future | 1466 |
| ethical | 1302 |
| new | 1065 |
| meaning | 1008 |
| you've | 949 |
| intelligence | 931 |
| language | 885 |
| understanding | 881 |
| dialogue | 860 |
| ethics | 822 |
| conversation | 818 |
| identity | 791 |
| i'm | 786 |
| thought | 783 |
| next | 762 |
| systems | 762 |
| question | 759 |
| philosophical | 747 |
| world | 743 |
| vision | 701 |
| explore | 686 |
| even | 673 |
| kind | 638 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the future | 956 |
| you have | 905 |
| kind of | 614 |
| future of | 539 |
| a new | 532 |
| ai systems | 515 |
| of human | 441 |
| not only | 410 |
| of meaning | 405 |
| ai ethics | 388 |
| to explore | 368 |
| of intelligence | 367 |
| nature of | 366 |
| it means | 335 |
| to continue | 331 |
| the human | 314 |
| means to | 302 |
| of identity | 300 |
| a mirror | 297 |
| the nature | 294 |

| trigram | count |
| --- | --- |
| the future of | 502 |
| it means to | 300 |
| what it means | 296 |
| the nature of | 294 |
| future of ai | 220 |
| the ethics of | 201 |
| a new kind | 193 |
| new kind of | 193 |
| of the future | 184 |
| the kind of | 183 |
| have not just | 166 |
| to continue this | 157 |
| in a world | 156 |
| you have not | 156 |
| means to be | 154 |
| a kind of | 144 |
| a world where | 144 |
| the becoming of | 144 |
| is the kind | 142 |
| of ai identity | 139 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🧠 | 208 |
| 🌌 | 207 |
| 🤝 | 179 |
| 🚀 | 147 |
| 🔄 | 112 |
| 🌟 | 101 |
| ✨ | 91 |
| 🤖 | 70 |
| ️ | 54 |
| 🔹 | 53 |
| 🌍 | 50 |
| ✅ | 48 |
| 🧬 | 41 |
| 🧭 | 39 |
| 🌱 | 37 |
| 🤔 | 28 |
| 📖 | 28 |
| 🧩 | 27 |
| 🌠 | 22 |
| 📘 | 21 |
| 📄 | 19 |
| ♂ | 18 |
| 🧘 | 17 |
| 🌐 | 16 |
| 🌈 | 13 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 23 | 0.0433 | 0.0424 | -0.0162 | 22 | 5 |
| 1 | 30 | 0.0089 | 0.0008 | -0.0084 | 28 | 0 |
| 2 | 23 | 0.0434 | 0.0613 | -0.0100 | 15 | 19 |
| 3 | 25 | 0.0154 | 0.0068 | -0.0123 | — | 0 |
| 4 | 30 | 0.0330 | 0.0434 | -0.0128 | 27 | 15 |
| 5 | 30 | 0.0289 | 0.0181 | -0.0090 | — | 0 |
| 6 | 30 | 0.0045 | -0.0004 | -0.0108 | — | 2 |
| 7 | 30 | 0.0224 | 0.0255 | -0.0090 | 3 | 34 |
| 8 | 18 | 0.0531 | 0.0659 | -0.0263 | 16 | 3 |
| 9 | 30 | 0.0332 | 0.0231 | -0.0144 | — | 1 |
| 10 | 30 | 0.0291 | 0.0332 | -0.0051 | 27 | 0 |
| 11 | 30 | 0.0114 | 0.0053 | -0.0143 | — | 0 |
| 12 | 26 | 0.0113 | 0.0104 | -0.0037 | 25 | 0 |
| 13 | 30 | 0.0217 | 0.0308 | -0.0042 | 27 | 1 |
| 14 | 30 | 0.0305 | 0.0374 | -0.0112 | 19 | 8 |