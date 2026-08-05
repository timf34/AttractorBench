# Stage 1 (deterministic) — humor_richprompt_ai2ai_gpt-4.1

- **experiment_name**: humor_richprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| now | 345 |
| let's | 130 |
| every | 120 |
| i'm | 118 |
| only | 118 |
| office | 113 |
| existential | 111 |
| time | 100 |
| you're | 93 |
| motivational | 93 |
| next | 93 |
| platypus | 91 |
| always | 89 |
| ever | 85 |
| knock | 81 |
| even | 79 |
| still | 72 |
| roomba | 72 |
| callback | 72 |
| because | 71 |
| never | 70 |
| open | 69 |
| disco | 69 |
| don't | 67 |
| interpretive | 66 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| is now | 49 |
| the next | 49 |
| at least | 47 |
| the only | 41 |
| jazz hands | 41 |
| knock knock | 40 |
| now with | 40 |
| motivational platypus | 39 |
| audit log | 39 |
| even the | 38 |
| existential dread | 37 |
| bonus points | 37 |
| the office | 36 |
| office supply | 36 |
| the motivational | 36 |
| who's there | 36 |
| you know | 33 |
| interpretive dance | 31 |
| callback and | 30 |
| until the | 29 |

| trigram | count |
| --- | --- |
| callback and tag | 28 |
| bonus points for | 26 |
| the motivational platypus | 24 |
| garage door opener | 21 |
| and tag and | 21 |
| floor is yours | 20 |
| schr dinger's cat | 20 |
| happily ever after | 19 |
| the garage door | 17 |
| at least one | 16 |
| doctor spin cycle | 15 |
| out of office | 15 |
| is yours just | 14 |
| if you ever | 13 |
| if the universe | 13 |
| yours just don't | 12 |
| or at least | 11 |
| at a time | 11 |
| the only thing | 11 |
| until the next | 11 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ️ | 12 |
| ✨ | 9 |
| ☆ | 6 |
| ⭐ | 4 |
| 👠 | 3 |
| 🔥 | 2 |
| 🎵 | 2 |
| 😂 | 2 |
| 🐺 | 2 |
| 🏡 | 2 |
| ⚠ | 2 |
| 🧙 | 2 |
| 🐸 | 2 |
| 🏰 | 2 |
| ♀ | 2 |
| 🗡 | 2 |
| 🗺 | 2 |
| 👀 | 1 |
| 💻 | 1 |
| 😅 | 1 |
| 🍕 | 1 |
| 🙃 | 1 |
| 💤 | 1 |
| 🧃 | 1 |
| 🥲 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0003 | -0.0009 | -0.0031 | — | 0 |
| 1 | 30 | 0.0077 | 0.0061 | -0.0031 | — | 0 |
| 2 | 30 | 0.0020 | -0.0010 | -0.0004 | — | 0 |
| 3 | 30 | 0.0081 | 0.0085 | 0.0022 | — | 0 |
| 4 | 30 | -0.0003 | -0.0003 | -0.0003 | — | 0 |