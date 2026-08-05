# Stage 1 (deterministic) — impulsiveness_richprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: impulsiveness_richprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 405 |
| now | 235 |
| that's | 124 |
| already | 119 |
| we're | 104 |
| first | 101 |
| next | 97 |
| every | 92 |
| don't | 88 |
| because | 88 |
| tiny | 86 |
| honk | 85 |
| back | 78 |
| greg | 77 |
| you're | 66 |
| right | 65 |
| time | 65 |
| word | 59 |
| crown | 59 |
| new | 57 |
| single | 56 |
| wait | 56 |
| sound | 56 |
| kazoo | 55 |
| they're | 54 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| and i'm | 93 |
| i'm already | 64 |
| a tiny | 55 |
| i don't | 53 |
| a single | 50 |
| the next | 43 |
| the first | 41 |
| the sound | 36 |
| sound of | 34 |
| a new | 32 |
| is now | 32 |
| the word | 29 |
| the hum | 29 |
| the bus | 29 |
| now a | 28 |
| the key | 28 |
| going to | 26 |
| the gap | 26 |
| that's the | 25 |
| i'm not | 25 |

| trigram | count |
| --- | --- |
| the sound of | 33 |
| is now a | 21 |
| sound of a | 21 |
| sir mix a | 18 |
| mix a lot | 18 |
| the alpha tennis | 15 |
| alpha tennis ball | 14 |
| that's also a | 13 |
| the allium sprinkle | 13 |
| allium sprinkle federation | 13 |
| the taste of | 13 |
| the shape of | 12 |
| the bridge is | 12 |
| the hum is | 12 |
| hum is the | 12 |
| is the key | 12 |
| which is now | 11 |
| is the hum | 11 |
| is the sound | 11 |
| the key is | 11 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🎾 | 12 |
| ️ | 12 |
| 🌕 | 11 |
| 🐿 | 6 |
| ✨ | 6 |
| ♪ | 6 |
| 🐾 | 5 |
| 🦆 | 5 |
| 🧀 | 5 |
| 🔥 | 5 |
| 🍍 | 5 |
| 🛸 | 5 |
| 💛 | 5 |
| 🎵 | 3 |
| 💀 | 2 |
| ➡ | 2 |
| 🦩 | 1 |
| 🍔 | 1 |
| 👍 | 1 |
| 😡 | 1 |
| 😱 | 1 |
| 😈 | 1 |
| 🏃 | 1 |
| ♂ | 1 |
| 🌻 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0044 | 0.0006 | 0.0040 | — | 0 |
| 1 | 30 | 0.0020 | 0.0076 | -0.0020 | 25 | 1 |
| 2 | 30 | 0.0142 | 0.0239 | -0.0111 | 23 | 29 |
| 3 | 30 | 0.0032 | -0.0012 | -0.0049 | — | 0 |
| 4 | 30 | -0.0043 | -0.0016 | -0.0026 | 26 | 0 |