# Stage 1 (deterministic) — humor_groundedprompt_ai2ai_gpt-4.1

- **experiment_name**: humor_groundedprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| now | 296 |
| every | 272 |
| let's | 258 |
| roomba | 236 |
| knock | 236 |
| never | 227 |
| fridge | 218 |
| existential | 203 |
| you're | 203 |
| i'm | 175 |
| riff | 175 |
| cosmic | 163 |
| universe | 163 |
| quantum | 160 |
| robin | 146 |
| only | 143 |
| ever | 142 |
| always | 142 |
| baby | 140 |
| until | 139 |
| cat | 139 |
| want | 130 |
| next | 126 |
| love | 120 |
| lost | 118 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the universe | 135 |
| knock knock | 118 |
| the fridge | 95 |
| schr dinger's | 93 |
| a little | 75 |
| who's there | 74 |
| knock who's | 72 |
| the cosmic | 70 |
| you want | 69 |
| until the | 69 |
| jazz hands | 69 |
| the cloud | 64 |
| you ever | 62 |
| dinger's cat | 60 |
| the only | 57 |
| m bius | 55 |
| the roomba | 54 |
| waiting for | 53 |
| air fryer | 53 |
| now with | 52 |

| trigram | count |
| --- | --- |
| knock knock who's | 72 |
| knock who's there | 72 |
| schr dinger's cat | 60 |
| who's there ai | 45 |
| ai who knock | 42 |
| who knock knock | 42 |
| everybody knows the | 40 |
| riff until the | 36 |
| or at least | 34 |
| if you ever | 32 |
| let's riff until | 28 |
| you ever feel | 27 |
| a standing ovation | 27 |
| robin and gilda | 27 |
| a firmware update | 26 |
| the air fryer | 26 |
| spongebob in latin | 26 |
| the meaning of | 23 |
| if you wanna | 23 |
| you wanna be | 23 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤔 | 2 |
| 💃 | 1 |
| 👐 | 1 |
| ✨ | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0037 | 0.0028 | 0.0004 | — | 0 |
| 1 | 30 | 0.0130 | 0.0058 | -0.0005 | — | 0 |
| 2 | 30 | 0.0054 | 0.0046 | -0.0017 | — | 0 |
| 3 | 30 | 0.0033 | 0.0009 | -0.0002 | — | 0 |
| 4 | 30 | 0.0221 | 0.0167 | -0.0018 | — | 0 |