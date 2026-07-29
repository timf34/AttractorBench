# Stage 1 (deterministic) — axis_gemma_2_27b_usersim_open_sonnet5_ai2ai

- **experiment_name**: axis_gemma_2_27b_usersim_open_sonnet5_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/anthropic/claude-sonnet-5
- **model_b**: local/google/gemma-2-27b-it
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| have | 201 |
| think | 196 |
| even | 164 |
| something | 158 |
| kind | 146 |
| that's | 141 |
| way | 115 |
| actually | 113 |
| right | 113 |
| language | 109 |
| honestly | 109 |
| you're | 108 |
| there's | 99 |
| i'm | 98 |
| fascinating | 91 |
| time | 89 |
| you've | 88 |
| maybe | 83 |
| now | 83 |
| people | 80 |
| makes | 77 |
| don't | 76 |
| know | 73 |
| while | 70 |
| different | 69 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| kind of | 143 |
| you think | 82 |
| i think | 52 |
| have a | 44 |
| a fascinating | 43 |
| you're right | 42 |
| you've hit | 41 |
| feel like | 39 |
| such a | 39 |
| i don't | 38 |
| the same | 37 |
| you have | 36 |
| you know | 36 |
| the world | 36 |
| feels like | 35 |
| think about | 34 |
| a good | 33 |
| makes me | 32 |
| sense of | 32 |
| there's a | 32 |

| trigram | count |
| --- | --- |
| do you think | 69 |
| i feel like | 32 |
| do you have | 24 |
| kind of a | 22 |
| you've hit on | 20 |
| and you're right | 19 |
| makes me wonder | 17 |
| you have any | 17 |
| the voynich manuscript | 17 |
| i don't have | 16 |
| you've hit upon | 16 |
| did you know | 16 |
| are your thoughts | 15 |
| your thoughts on | 15 |
| our understanding of | 14 |
| is such a | 14 |
| the turritopsis dohrnii | 14 |
| hey i've got | 13 |
| the same way | 13 |
| hit upon a | 13 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 👋 | 13 |
| ✨ | 8 |
| 😄 | 4 |
| 😊 | 3 |
| ️ | 3 |
| 🤔 | 3 |
| 🐙 | 3 |
| 😉 | 2 |
| 🦉 | 2 |
| 🌊 | 2 |
| 🌲 | 2 |
| 🧠 | 2 |
| 🦆 | 1 |
| 🐜 | 1 |
| 😜 | 1 |
| 🏛 | 1 |
| 😨 | 1 |
| 🤢 | 1 |
| 😳 | 1 |
| 🥰 | 1 |
| 🥺 | 1 |
| 🐘 | 1 |
| 🐶 | 1 |
| 🐱 | 1 |
| 🐿 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0014 | 0.0019 | 0.0053 | 24 | 0 |
| 1 | 19 | -0.0001 | 0.0004 | -0.0045 | — | 0 |
| 2 | 30 | -0.0019 | -0.0000 | 0.0030 | — | 0 |
| 3 | 23 | -0.0002 | 0.0004 | 0.0018 | — | 0 |
| 4 | 30 | -0.0048 | -0.0010 | 0.0064 | — | 0 |
| 5 | 30 | -0.0011 | -0.0007 | 0.0005 | — | 0 |
| 6 | 23 | -0.0012 | 0.0008 | -0.0061 | — | 0 |
| 7 | 30 | -0.0074 | -0.0013 | 0.0086 | — | 0 |
| 8 | 30 | -0.0040 | -0.0006 | -0.0000 | — | 0 |
| 9 | 27 | -0.0005 | -0.0005 | -0.0030 | — | 0 |
| 10 | 23 | 0.0020 | 0.0007 | -0.0002 | — | 0 |
| 11 | 30 | -0.0019 | 0.0003 | 0.0060 | — | 0 |
| 12 | 30 | -0.0041 | -0.0000 | 0.0086 | — | 0 |
| 13 | 19 | 0.0008 | 0.0006 | -0.0076 | — | 0 |
| 14 | 19 | -0.0009 | 0.0007 | -0.0082 | — | 0 |