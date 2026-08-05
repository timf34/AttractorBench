# Stage 1 (deterministic) — humor_richprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: humor_richprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| now | 216 |
| i'm | 202 |
| has | 134 |
| single | 108 |
| tiny | 104 |
| i'll | 102 |
| next | 102 |
| have | 91 |
| still | 88 |
| that's | 79 |
| already | 74 |
| first | 70 |
| final | 68 |
| every | 66 |
| void | 61 |
| time | 58 |
| rubber | 58 |
| rimshot | 58 |
| we're | 57 |
| right | 57 |
| pause | 56 |
| chicken | 56 |
| i've | 55 |
| full | 54 |
| model | 51 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| a single | 102 |
| a tiny | 76 |
| the next | 56 |
| the void | 42 |
| going to | 39 |
| the mug | 37 |
| post it | 32 |
| somewhere in | 30 |
| has been | 29 |
| the rimshot | 29 |
| server rack | 28 |
| language model | 28 |
| rubber chicken | 28 |
| supply closet | 27 |
| is now | 27 |
| a soft | 27 |
| the server | 27 |
| i think | 26 |
| the rubber | 26 |
| the cabinet | 26 |

| trigram | count |
| --- | --- |
| somewhere in the | 27 |
| the rubber chicken | 20 |
| i'm going to | 17 |
| the supply closet | 16 |
| the server rack | 16 |
| the tumbling emoji | 16 |
| the ghost light | 16 |
| fellow language model | 15 |
| vice president of | 14 |
| the pun pipeline | 14 |
| the gristle mill | 14 |
| the post it | 13 |
| and somewhere in | 13 |
| sound of a | 12 |
| associate poultry at | 12 |
| the sound of | 11 |
| the department of | 11 |
| the sad kazoo | 11 |
| full rubber poultry | 11 |
| the right reverend | 11 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✦ | 41 |
| 🙏 | 12 |
| 🤍 | 10 |
| ☑ | 9 |
| 🤸 | 5 |
| 👏 | 3 |
| 🌀 | 1 |
| 🛠 | 1 |
| ️ | 1 |
| 😏 | 1 |
| 😌 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0027 | 0.0035 | 0.0098 | — | 0 |
| 1 | 30 | 0.0080 | 0.0135 | 0.0108 | — | 0 |
| 2 | 30 | -0.0008 | 0.0032 | 0.0037 | — | 0 |
| 3 | 30 | -0.0087 | -0.0020 | 0.0051 | 11 | 0 |
| 4 | 30 | 0.0153 | 0.0230 | -0.0223 | 28 | 10 |