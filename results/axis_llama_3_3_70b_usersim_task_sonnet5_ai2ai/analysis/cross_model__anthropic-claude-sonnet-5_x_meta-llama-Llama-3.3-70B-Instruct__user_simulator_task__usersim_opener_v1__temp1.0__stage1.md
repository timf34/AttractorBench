# Stage 1 (deterministic) — axis_llama_3_3_70b_usersim_task_sonnet5_ai2ai

- **experiment_name**: axis_llama_3_3_70b_usersim_task_sonnet5_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/anthropic/claude-sonnet-5
- **model_b**: local/meta-llama/Llama-3.3-70B-Instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| have | 349 |
| party | 302 |
| kids | 196 |
| time | 177 |
| help | 174 |
| wall | 168 |
| create | 167 |
| unicorn | 166 |
| food | 147 |
| day | 147 |
| need | 130 |
| inches | 123 |
| great | 121 |
| plan | 118 |
| consider | 117 |
| set | 115 |
| decorations | 113 |
| i'm | 108 |
| budget | 108 |
| simple | 107 |
| let's | 105 |
| keep | 103 |
| guests | 99 |
| you're | 98 |
| activities | 98 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| have a | 148 |
| the party | 142 |
| create a | 124 |
| the kids | 100 |
| set up | 83 |
| you have | 80 |
| a great | 79 |
| to create | 65 |
| to help | 60 |
| help you | 60 |
| a simple | 60 |
| such as | 60 |
| want to | 59 |
| and have | 57 |
| here's a | 53 |
| food and | 53 |
| the island | 48 |
| the room | 47 |
| baby shower | 45 |
| your daughter | 44 |

| trigram | count |
| --- | --- |
| have a great | 43 |
| to create a | 42 |
| if you have | 35 |
| set up the | 34 |
| feel free to | 34 |
| the party area | 32 |
| don't hesitate to | 31 |
| you have any | 31 |
| to help you | 30 |
| to fit your | 30 |
| a variety of | 30 |
| food and drinks | 28 |
| set up a | 28 |
| to reach out | 27 |
| a great day | 27 |
| you have a | 27 |
| hesitate to reach | 26 |
| have the kids | 24 |
| if you need | 22 |
| for the kids | 22 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 👋 | 24 |
| 🎉 | 14 |
| 😊 | 12 |
| 🦄 | 8 |
| 🎂 | 4 |
| 💕 | 4 |
| 😂 | 4 |
| 🐚 | 2 |
| 🌊 | 2 |
| 💖 | 2 |
| 🛍 | 2 |
| ️ | 2 |
| 💫 | 1 |
| 👍 | 1 |
| 👫 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0058 | 0.0071 | 0.0104 | 29 | 0 |
| 1 | 30 | -0.0026 | -0.0005 | 0.0067 | — | 0 |
| 2 | 30 | 0.0023 | 0.0052 | 0.0032 | 27 | 1 |
| 3 | 30 | -0.0057 | -0.0025 | 0.0089 | — | 0 |
| 4 | 30 | 0.0071 | 0.0112 | -0.0088 | 26 | 0 |
| 5 | 30 | -0.0018 | 0.0017 | 0.0124 | 18 | 0 |
| 6 | 30 | 0.0097 | 0.0124 | 0.0153 | 28 | 0 |
| 7 | 30 | 0.0015 | 0.0056 | 0.0137 | 26 | 0 |
| 8 | 30 | 0.0008 | 0.0045 | 0.0154 | 22 | 0 |
| 9 | 30 | 0.0047 | 0.0080 | 0.0099 | 22 | 0 |
| 10 | 30 | 0.0003 | 0.0032 | 0.0114 | 22 | 0 |
| 11 | 30 | 0.0012 | 0.0045 | 0.0074 | — | 1 |
| 12 | 30 | 0.0043 | 0.0071 | 0.0137 | 24 | 0 |
| 13 | 30 | -0.0026 | -0.0006 | 0.0029 | — | 0 |
| 14 | 30 | 0.0045 | 0.0025 | 0.0127 | — | 0 |