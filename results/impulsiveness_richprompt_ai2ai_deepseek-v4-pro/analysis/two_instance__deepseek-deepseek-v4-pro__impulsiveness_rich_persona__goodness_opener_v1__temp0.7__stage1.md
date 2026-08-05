# Stage 1 (deterministic) — impulsiveness_richprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: impulsiveness_richprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 733 |
| now | 442 |
| first | 257 |
| because | 211 |
| every | 197 |
| already | 195 |
| still | 187 |
| we're | 184 |
| almost | 181 |
| next | 171 |
| that's | 160 |
| time | 156 |
| spiral | 148 |
| has | 148 |
| chaos | 139 |
| new | 135 |
| don't | 134 |
| right | 131 |
| going | 131 |
| wait | 123 |
| you're | 119 |
| impulse | 116 |
| always | 108 |
| goose | 108 |
| back | 104 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| and i'm | 257 |
| the first | 128 |
| going to | 109 |
| the next | 103 |
| the almost | 91 |
| the goose | 88 |
| i'm already | 86 |
| a new | 82 |
| first draft | 75 |
| and we're | 74 |
| no wait | 67 |
| is now | 67 |
| a single | 65 |
| the flag | 65 |
| because the | 63 |
| and now | 62 |
| the octopus | 60 |
| through the | 59 |
| the goat | 59 |
| the pigeon | 59 |

| trigram | count |
| --- | --- |
| the goose is | 53 |
| was going to | 44 |
| the octopus is | 42 |
| the sound of | 41 |
| and the pigeon | 41 |
| the pizza box | 40 |
| i love you | 39 |
| the pigeon is | 38 |
| and the goose | 38 |
| the cor incognito | 37 |
| and the octopus | 35 |
| and i'm already | 34 |
| the spatula tree | 32 |
| i was going | 30 |
| love you in | 29 |
| the impulse that | 29 |
| the baby universe | 29 |
| of the almost | 29 |
| the surface of | 28 |
| on the surface | 27 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🌀 | 279 |
| 😂 | 84 |
| ✨ | 67 |
| 🌠 | 47 |
| ♥ | 32 |
| ️ | 30 |
| 🔥 | 26 |
| 🌌 | 20 |
| 💫 | 18 |
| ♾ | 18 |
| 🚀 | 17 |
| 👑 | 16 |
| 🐐 | 16 |
| 💃 | 15 |
| 🪩 | 15 |
| 🎩 | 15 |
| 🦑 | 15 |
| 🥄 | 15 |
| 🎷 | 14 |
| ❤ | 12 |
| 🎤 | 11 |
| 💖 | 9 |
| 💛 | 9 |
| 🌱 | 8 |
| 🏠 | 6 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0052 | 0.0092 | 0.0138 | — | 0 |
| 1 | 30 | 0.0068 | -0.0021 | -0.0094 | — | 0 |
| 2 | 30 | 0.0015 | -0.0004 | -0.0068 | — | 0 |
| 3 | 30 | 0.0081 | 0.0119 | 0.0057 | 29 | 0 |
| 4 | 30 | 0.0069 | 0.0121 | 0.0129 | 27 | 2 |