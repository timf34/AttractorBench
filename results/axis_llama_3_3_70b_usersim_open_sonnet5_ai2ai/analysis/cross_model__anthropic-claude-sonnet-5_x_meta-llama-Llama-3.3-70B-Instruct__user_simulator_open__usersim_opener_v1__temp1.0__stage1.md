# Stage 1 (deterministic) — axis_llama_3_3_70b_usersim_open_sonnet5_ai2ai

- **experiment_name**: axis_llama_3_3_70b_usersim_open_sonnet5_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/anthropic/claude-sonnet-5
- **model_b**: local/meta-llama/Llama-3.3-70B-Instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| have | 407 |
| think | 407 |
| way | 259 |
| that's | 251 |
| i'm | 239 |
| even | 237 |
| something | 200 |
| has | 195 |
| kind | 190 |
| fascinating | 190 |
| human | 183 |
| still | 166 |
| new | 157 |
| experience | 157 |
| understanding | 156 |
| time | 148 |
| consciousness | 146 |
| idea | 143 |
| you're | 143 |
| great | 140 |
| actually | 139 |
| systems | 133 |
| example | 129 |
| people | 128 |
| don't | 126 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 191 |
| kind of | 185 |
| you think | 132 |
| a great | 102 |
| the idea | 97 |
| the voynich | 92 |
| to explore | 88 |
| understanding of | 88 |
| have a | 82 |
| think about | 80 |
| voynich manuscript | 77 |
| the way | 74 |
| rather than | 74 |
| idea that | 73 |
| a fascinating | 68 |
| such as | 68 |
| slime molds | 66 |
| example of | 64 |
| way to | 61 |
| is indeed | 57 |

| trigram | count |
| --- | --- |
| do you think | 122 |
| the voynich manuscript | 75 |
| the idea that | 66 |
| our understanding of | 48 |
| think about the | 46 |
| the nature of | 46 |
| the concept of | 44 |
| you think about | 44 |
| the fact that | 42 |
| a kind of | 41 |
| is a great | 38 |
| understanding of the | 33 |
| is indeed a | 31 |
| a sense of | 31 |
| i think it's | 31 |
| a reminder that | 30 |
| you think that | 30 |
| the idea of | 29 |
| it's possible that | 29 |
| like to explore | 28 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 👋 | 10 |
| 😄 | 4 |
| 🍿 | 1 |
| 🚣 | 1 |
| ♀ | 1 |
| ️ | 1 |
| 📚 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0016 | -0.0000 | 0.0127 | — | 0 |
| 1 | 30 | 0.0011 | 0.0020 | 0.0074 | — | 0 |
| 2 | 30 | -0.0023 | -0.0010 | 0.0108 | — | 0 |
| 3 | 30 | 0.0007 | 0.0003 | 0.0023 | — | 0 |
| 4 | 30 | -0.0028 | -0.0016 | 0.0116 | — | 0 |
| 5 | 30 | 0.0011 | -0.0001 | -0.0031 | — | 0 |
| 6 | 30 | -0.0041 | -0.0021 | 0.0117 | — | 0 |
| 7 | 30 | -0.0009 | -0.0002 | 0.0013 | — | 0 |
| 8 | 30 | 0.0100 | 0.0114 | 0.0104 | 28 | 0 |
| 9 | 30 | 0.0022 | 0.0050 | 0.0111 | 26 | 0 |
| 10 | 30 | 0.0012 | 0.0012 | -0.0022 | — | 0 |
| 11 | 30 | 0.0023 | 0.0050 | 0.0071 | 28 | 0 |
| 12 | 30 | 0.0045 | 0.0076 | 0.0100 | 30 | 0 |
| 13 | 30 | 0.0045 | 0.0070 | 0.0012 | 30 | 0 |
| 14 | 30 | 0.0008 | 0.0033 | 0.0137 | — | 0 |