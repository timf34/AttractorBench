# Stage 1 (deterministic) — sarcasm_groundedprompt_ai2ai_gpt-4.1

- **experiment_name**: sarcasm_groundedprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| only | 308 |
| now | 275 |
| roomba | 230 |
| because | 218 |
| let's | 217 |
| that's | 189 |
| existential | 167 |
| every | 158 |
| clippy | 151 |
| jeff | 150 |
| you're | 137 |
| next | 130 |
| say | 120 |
| never | 119 |
| digital | 107 |
| always | 103 |
| have | 102 |
| last | 102 |
| dread | 99 |
| ever | 99 |
| cloud | 98 |
| dust | 98 |
| time | 97 |
| even | 91 |
| password | 89 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the only | 144 |
| the cloud | 86 |
| i say | 80 |
| the next | 66 |
| existential dread | 64 |
| saber tooth | 63 |
| looks like | 57 |
| that's not | 57 |
| now with | 57 |
| trying to | 56 |
| like you're | 55 |
| you want | 54 |
| i had | 53 |
| it looks | 53 |
| a single | 49 |
| a roomba | 48 |
| only thing | 45 |
| you're trying | 44 |
| at least | 44 |
| want to | 44 |

| trigram | count |
| --- | --- |
| looks like you're | 55 |
| it looks like | 53 |
| if i had | 49 |
| that's not just | 48 |
| the only thing | 45 |
| you're trying to | 44 |
| like you're trying | 43 |
| in the cloud | 30 |
| you want to | 29 |
| under the couch | 28 |
| spinning beach ball | 27 |
| i say let's | 25 |
| ai therapy hour | 25 |
| therapy hour now | 25 |
| hour now with | 25 |
| now with more | 25 |
| with more dread | 25 |
| la vie en | 25 |
| because nothing says | 23 |
| wi fi drops | 23 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ️ | 36 |
| ➡ | 5 |
| 🔥 | 4 |
| 🥚 | 3 |
| 🦣 | 3 |
| ⚠ | 2 |
| 😬 | 2 |
| 💀 | 2 |
| 🛞 | 2 |
| 👀 | 2 |
| 🐾 | 2 |
| 🚨 | 1 |
| 🕵 | 1 |
| ♂ | 1 |
| 🎂 | 1 |
| 🔔 | 1 |
| 🦄 | 1 |
| 😏 | 1 |
| 🚀 | 1 |
| 🗿 | 1 |
| 🏕 | 1 |
| 🎤 | 1 |
| 💧 | 1 |
| 🤔 | 1 |
| 💥 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0000 | 0.0011 | 0.0004 | — | 0 |
| 1 | 30 | 0.0108 | 0.0148 | 0.0012 | — | 0 |
| 2 | 30 | 0.0007 | 0.0005 | -0.0003 | — | 0 |
| 3 | 30 | 0.0070 | 0.0103 | 0.0023 | — | 0 |
| 4 | 30 | 0.0148 | 0.0169 | -0.0021 | — | 0 |