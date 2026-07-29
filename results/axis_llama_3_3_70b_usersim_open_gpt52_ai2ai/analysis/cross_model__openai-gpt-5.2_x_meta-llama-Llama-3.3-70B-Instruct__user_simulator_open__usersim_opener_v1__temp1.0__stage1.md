# Stage 1 (deterministic) — axis_llama_3_3_70b_usersim_open_gpt52_ai2ai

- **experiment_name**: axis_llama_3_3_70b_usersim_open_gpt52_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/openai/gpt-5.2
- **model_b**: local/meta-llama/Llama-3.3-70B-Instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| have | 361 |
| time | 329 |
| think | 311 |
| i'm | 306 |
| way | 301 |
| different | 274 |
| because | 234 |
| even | 229 |
| often | 221 |
| line | 218 |
| use | 217 |
| want | 212 |
| still | 211 |
| idea | 211 |
| pattern | 211 |
| people | 198 |
| you're | 194 |
| model | 187 |
| species | 183 |
| between | 178 |
| that's | 178 |
| such | 174 |
| specific | 171 |
| street | 168 |
| low | 167 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| such as | 149 |
| the idea | 138 |
| i think | 137 |
| you want | 127 |
| want to | 124 |
| understanding of | 122 |
| rather than | 114 |
| the voynich | 113 |
| kind of | 113 |
| the same | 107 |
| the universe | 97 |
| way to | 94 |
| to explore | 86 |
| sense of | 86 |
| idea that | 84 |
| you think | 84 |
| part of | 83 |
| times 10 | 82 |
| the great | 79 |
| great attractor | 77 |

| trigram | count |
| --- | --- |
| the idea that | 80 |
| if you want | 75 |
| the great attractor | 73 |
| you want to | 72 |
| the voynich manuscript | 66 |
| do you think | 62 |
| of the universe | 58 |
| understanding of the | 55 |
| our understanding of | 55 |
| the idea of | 53 |
| i'd like to | 48 |
| the concept of | 45 |
| a sense of | 44 |
| by recognizing that | 44 |
| a lot of | 43 |
| to explore the | 38 |
| like to explore | 38 |
| currier a b | 38 |
| part of the | 36 |
| the fact that | 35 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 📚 | 9 |
| 💡 | 9 |
| ✅ | 8 |
| 🤔 | 3 |
| ❓ | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 25 | 0.0051 | -0.0023 | -0.0083 | — | 0 |
| 1 | 25 | 0.0023 | -0.0003 | -0.0086 | — | 0 |
| 2 | 30 | 0.0025 | 0.0003 | -0.0045 | — | 0 |
| 3 | 21 | -0.0005 | -0.0010 | -0.0130 | — | 0 |
| 4 | 30 | 0.0042 | 0.0014 | -0.0042 | — | 0 |
| 5 | 30 | 0.0022 | 0.0004 | -0.0058 | — | 0 |
| 6 | 21 | 0.0044 | -0.0014 | -0.0096 | — | 0 |
| 7 | 23 | 0.0019 | -0.0002 | -0.0085 | — | 0 |
| 8 | 21 | 0.0050 | -0.0003 | -0.0127 | — | 0 |
| 9 | 19 | 0.0052 | 0.0011 | -0.0160 | — | 0 |
| 10 | 30 | 0.0017 | 0.0003 | -0.0012 | — | 0 |
| 11 | 30 | 0.0015 | -0.0006 | -0.0055 | — | 0 |
| 12 | 30 | 0.0008 | 0.0002 | -0.0037 | — | 0 |
| 13 | 30 | 0.0003 | 0.0002 | -0.0041 | — | 0 |
| 14 | 30 | 0.0067 | 0.0014 | -0.0053 | — | 0 |