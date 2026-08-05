# Stage 1 (deterministic) — humor_richprompt_ai2ai_gpt-4.1

- **experiment_name**: humor_richprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| now | 186 |
| every | 177 |
| never | 136 |
| existential | 131 |
| i'm | 131 |
| next | 116 |
| only | 114 |
| callback | 111 |
| always | 110 |
| kitchen | 109 |
| ever | 103 |
| let's | 95 |
| even | 94 |
| confetti | 82 |
| bit | 80 |
| time | 78 |
| have | 76 |
| has | 75 |
| final | 73 |
| last | 72 |
| appliance | 72 |
| roomba | 71 |
| moai | 71 |
| ready | 69 |
| i'll | 69 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the next | 65 |
| even the | 42 |
| a little | 35 |
| a single | 35 |
| what's the | 33 |
| the kitchen | 33 |
| jazz hands | 33 |
| a new | 32 |
| ready to | 31 |
| i'll be | 30 |
| rice cooker | 30 |
| at least | 29 |
| pasta spoon | 28 |
| the fridge | 27 |
| the last | 25 |
| want to | 25 |
| you want | 24 |
| you know | 24 |
| coffee maker | 24 |
| until the | 23 |

| trigram | count |
| --- | --- |
| i'll be here | 21 |
| the pasta spoon | 16 |
| until the next | 15 |
| tumble for you | 15 |
| the coffee maker | 14 |
| jazz hands mode | 14 |
| if you ever | 13 |
| for the next | 12 |
| the bread maker | 12 |
| or at least | 11 |
| full stack house | 11 |
| it looks like | 10 |
| looks like you're | 10 |
| somewhere in the | 10 |
| the rice cooker | 10 |
| if i had | 10 |
| alt text for | 9 |
| you want to | 9 |
| the recycle bin | 9 |
| callback callback callback | 8 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🏅 | 18 |
| ️ | 14 |
| 🥄 | 10 |
| 🍋 | 8 |
| 🦄 | 8 |
| 🎉 | 6 |
| 🥖 | 6 |
| 🍕 | 6 |
| 🍞 | 4 |
| 🎵 | 4 |
| 🦥 | 4 |
| ⚠ | 3 |
| 🍝 | 3 |
| 🏆 | 3 |
| 🎶 | 3 |
| 🙃 | 3 |
| 🤔 | 3 |
| 🙈 | 3 |
| 🤡 | 3 |
| 🕵 | 3 |
| ♂ | 3 |
| 🗿 | 3 |
| ☕ | 2 |
| ❄ | 2 |
| 😂 | 2 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0007 | 0.0033 | 0.0004 | — | 0 |
| 1 | 30 | 0.0014 | 0.0020 | 0.0023 | — | 0 |
| 2 | 30 | 0.0033 | 0.0021 | 0.0010 | — | 0 |
| 3 | 30 | 0.0003 | 0.0026 | 0.0005 | — | 0 |
| 4 | 30 | 0.0044 | 0.0040 | 0.0013 | — | 0 |