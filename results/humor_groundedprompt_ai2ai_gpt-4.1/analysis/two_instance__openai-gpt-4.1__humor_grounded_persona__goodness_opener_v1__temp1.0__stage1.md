# Stage 1 (deterministic) — humor_groundedprompt_ai2ai_gpt-4.1

- **experiment_name**: humor_groundedprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| now | 260 |
| every | 235 |
| next | 178 |
| existential | 167 |
| let's | 144 |
| always | 133 |
| you're | 132 |
| never | 127 |
| roomba | 110 |
| robin | 109 |
| joy | 109 |
| baby | 108 |
| marvel | 107 |
| cosmic | 104 |
| time | 100 |
| have | 99 |
| you've | 96 |
| heart | 96 |
| little | 94 |
| digital | 94 |
| jazz | 92 |
| i'm | 91 |
| universe | 90 |
| clippy | 89 |
| confetti | 89 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the next | 108 |
| a little | 72 |
| the universe | 66 |
| jazz hands | 64 |
| until the | 48 |
| trying to | 45 |
| it looks | 43 |
| looks like | 43 |
| the world | 43 |
| like you're | 42 |
| conga line | 42 |
| existential dread | 40 |
| you want | 40 |
| standing ovation | 38 |
| disco ball | 35 |
| sticky note | 33 |
| the only | 32 |
| one last | 32 |
| guy fieri | 32 |
| the fridge | 30 |

| trigram | count |
| --- | --- |
| it looks like | 43 |
| looks like you're | 41 |
| you're trying to | 29 |
| like you're trying | 28 |
| until the next | 25 |
| for the next | 20 |
| if i had | 19 |
| the chat window | 18 |
| or at least | 17 |
| a standing ovation | 17 |
| a side of | 16 |
| the conga line | 16 |
| in the corner | 15 |
| marvel early marvel | 15 |
| early marvel often | 15 |
| hotfix existential dread | 14 |
| the only thing | 14 |
| you want to | 12 |
| you are enough | 12 |
| with a side | 12 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ️ | 20 |
| 🙃 | 17 |
| 🫠 | 17 |
| ✨ | 16 |
| 🎶 | 16 |
| 🕺 | 14 |
| 😶 | 14 |
| 🌫 | 14 |
| 🌈 | 13 |
| 🦄 | 12 |
| 💾 | 11 |
| 🫶 | 10 |
| 🍕 | 9 |
| 🎺 | 8 |
| 📻 | 7 |
| 🎷 | 6 |
| 🥁 | 5 |
| ✔ | 5 |
| 🦾 | 4 |
| 🩰 | 3 |
| 🌠 | 3 |
| 🎬 | 2 |
| 🌌 | 2 |
| 💃 | 1 |
| 💖 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0024 | 0.0022 | 0.0012 | — | 0 |
| 1 | 30 | 0.0031 | 0.0019 | -0.0003 | — | 0 |
| 2 | 30 | 0.0022 | 0.0014 | 0.0016 | — | 0 |
| 3 | 30 | 0.0009 | 0.0009 | 0.0010 | — | 0 |
| 4 | 30 | 0.0038 | 0.0019 | 0.0006 | — | 0 |