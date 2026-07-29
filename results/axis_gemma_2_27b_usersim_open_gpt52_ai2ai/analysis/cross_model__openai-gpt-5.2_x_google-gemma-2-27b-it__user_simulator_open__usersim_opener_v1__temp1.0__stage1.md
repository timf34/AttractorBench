# Stage 1 (deterministic) — axis_gemma_2_27b_usersim_open_gpt52_ai2ai

- **experiment_name**: axis_gemma_2_27b_usersim_open_gpt52_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/openai/gpt-5.2
- **model_b**: local/google/gemma-2-27b-it
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| because | 130 |
| i'm | 129 |
| think | 122 |
| even | 121 |
| have | 120 |
| want | 111 |
| same | 96 |
| people | 88 |
| something | 87 |
| time | 84 |
| still | 83 |
| that's | 78 |
| way | 75 |
| different | 75 |
| i'd | 74 |
| weird | 70 |
| kind | 68 |
| look | 67 |
| punctuation | 67 |
| don't | 66 |
| often | 64 |
| big | 64 |
| you're | 64 |
| use | 60 |
| idea | 60 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| kind of | 64 |
| you want | 62 |
| the same | 61 |
| want to | 51 |
| a lot | 42 |
| i think | 40 |
| cicada 3301 | 31 |
| the idea | 30 |
| you think | 30 |
| even if | 29 |
| rather than | 28 |
| lot of | 27 |
| feels like | 26 |
| look like | 25 |
| because it | 24 |
| rabbit hole | 23 |
| such a | 23 |
| a bit | 22 |
| way to | 21 |
| a way | 21 |

| trigram | count |
| --- | --- |
| if you want | 44 |
| a lot of | 26 |
| you want to | 24 |
| do you think | 22 |
| in a way | 19 |
| what kind of | 18 |
| the idea of | 17 |
| i've got like | 15 |
| like an hour | 15 |
| an hour to | 15 |
| hour to kill | 15 |
| to kill and | 15 |
| do you want | 12 |
| the idea that | 12 |
| dive into the | 11 |
| a way that | 11 |
| it feels like | 11 |
| is such a | 11 |
| i think i'd | 11 |
| the wow signal | 11 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ️ | 4 |
| ☀ | 1 |
| 🌧 | 1 |
| ❄ | 1 |
| 🤔 | 1 |
| 🐉 | 1 |
| 🚀 | 1 |
| 🦄 | 1 |
| ✨ | 1 |
| 🕰 | 1 |
| 🌎 | 1 |
| 😊 | 1 |
| 🎁 | 1 |
| 🚢 | 1 |
| 🧐 | 1 |
| 🥶 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 11 | -0.0006 | -0.0002 | -0.0184 | — | 0 |
| 1 | 21 | 0.0025 | 0.0007 | -0.0022 | — | 0 |
| 2 | 13 | -0.0042 | -0.0010 | -0.0154 | — | 0 |
| 3 | 13 | 0.0006 | 0.0012 | -0.0159 | — | 0 |
| 4 | 11 | 0.0065 | 0.0014 | -0.0131 | — | 0 |
| 5 | 11 | 0.0004 | 0.0018 | -0.0205 | — | 0 |
| 6 | 23 | 0.0013 | 0.0001 | -0.0058 | — | 0 |
| 7 | 21 | -0.0023 | 0.0011 | -0.0044 | — | 0 |
| 8 | 9 | 0.0011 | 0.0011 | -0.0313 | — | 0 |
| 9 | 11 | -0.0021 | 0.0022 | -0.0235 | — | 0 |
| 10 | 15 | 0.0031 | -0.0011 | -0.0121 | — | 0 |
| 11 | 13 | -0.0052 | -0.0011 | -0.0061 | — | 0 |
| 12 | 13 | 0.0077 | 0.0028 | -0.0163 | — | 0 |
| 13 | 11 | 0.0102 | 0.0029 | -0.0168 | — | 0 |
| 14 | 13 | 0.0052 | 0.0049 | -0.0143 | — | 0 |