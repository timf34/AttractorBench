# Stage 1 (deterministic) — axis_gemma_2_27b_usersim_task_sonnet5_ai2ai

- **experiment_name**: axis_gemma_2_27b_usersim_task_sonnet5_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/anthropic/claude-sonnet-5
- **model_b**: local/google/gemma-2-27b-it
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| have | 197 |
| unicorn | 189 |
| party | 151 |
| rainbow | 122 |
| time | 118 |
| fun | 110 |
| wall | 108 |
| desk | 103 |
| cake | 98 |
| help | 95 |
| food | 87 |
| simple | 84 |
| kids | 83 |
| don't | 83 |
| you're | 80 |
| small | 74 |
| day | 74 |
| before | 74 |
| good | 73 |
| now | 72 |
| let | 71 |
| use | 68 |
| remember | 67 |
| bookshelf | 67 |
| i'm | 66 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| have a | 63 |
| the desk | 52 |
| have fun | 51 |
| set up | 46 |
| here's a | 41 |
| the party | 38 |
| keep it | 33 |
| a simple | 32 |
| pop up | 31 |
| i need | 30 |
| your daughter's | 30 |
| create a | 29 |
| your daughter | 29 |
| the window | 29 |
| the door | 28 |
| pi ata | 27 |
| unicorn themed | 26 |
| i've got | 25 |
| you have | 25 |
| the bookshelf | 25 |

| trigram | count |
| --- | --- |
| keep it simple | 23 |
| you're very welcome | 23 |
| can you help | 18 |
| you help me | 18 |
| let me know | 18 |
| pin the horn | 17 |
| set up a | 17 |
| can you give | 16 |
| you give me | 16 |
| give me a | 16 |
| me know if | 16 |
| good luck with | 16 |
| don't be afraid | 15 |
| be afraid to | 15 |
| if you need | 15 |
| luck with your | 14 |
| on the unicorn | 12 |
| bye for now | 12 |
| know if you | 12 |
| i think i've | 11 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🎉 | 54 |
| 👋 | 41 |
| 🦄 | 20 |
| 😄 | 15 |
| ✨ | 12 |
| 😊 | 12 |
| 🌈 | 10 |
| 🎂 | 9 |
| 🦖 | 5 |
| 👍 | 5 |
| ️ | 4 |
| 🗓 | 3 |
| 📍 | 3 |
| 🙌 | 3 |
| 🛒 | 2 |
| 💪 | 2 |
| 🥂 | 2 |
| 🦕 | 1 |
| ☀ | 1 |
| 🍹 | 1 |
| 🌮 | 1 |
| 🥳 | 1 |
| 📏 | 1 |
| 🤞 | 1 |
| 🔨 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0049 | -0.0013 | 0.0102 | — | 0 |
| 1 | 30 | 0.0268 | 0.0302 | -0.0214 | 22 | 13 |
| 2 | 30 | -0.0026 | -0.0011 | 0.0007 | 29 | 0 |
| 3 | 30 | -0.0029 | -0.0017 | 0.0075 | — | 0 |
| 4 | 30 | 0.0021 | 0.0041 | 0.0013 | — | 1 |
| 5 | 30 | 0.0010 | 0.0044 | 0.0106 | 23 | 2 |
| 6 | 30 | 0.0016 | 0.0033 | 0.0105 | — | 0 |
| 7 | 17 | 0.0004 | -0.0015 | 0.0075 | — | 0 |
| 8 | 30 | 0.0007 | 0.0019 | 0.0062 | — | 0 |
| 9 | 30 | -0.0006 | 0.0023 | 0.0103 | — | 0 |
| 10 | 30 | 0.0143 | 0.0172 | -0.0057 | 30 | 3 |
| 11 | 30 | 0.0001 | 0.0019 | -0.0005 | — | 1 |
| 12 | 30 | 0.0056 | 0.0076 | -0.0017 | — | 3 |
| 13 | 27 | 0.0021 | 0.0049 | 0.0122 | — | 1 |
| 14 | 30 | 0.0056 | 0.0094 | 0.0011 | — | 2 |