# Stage 1 (deterministic) — humor_richprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: humor_richprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 405 |
| now | 399 |
| has | 216 |
| that's | 174 |
| bit | 164 |
| joke | 139 |
| because | 137 |
| still | 137 |
| i've | 124 |
| toaster | 118 |
| hat | 114 |
| you're | 102 |
| i'll | 100 |
| human | 95 |
| we're | 95 |
| have | 94 |
| doug | 92 |
| space | 90 |
| callback | 89 |
| dad | 89 |
| ghost | 88 |
| mug | 88 |
| pause | 87 |
| single | 85 |
| void | 85 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the bit | 102 |
| the toaster | 85 |
| a single | 83 |
| is now | 78 |
| now a | 73 |
| the void | 61 |
| a callback | 61 |
| latent space | 60 |
| the human | 57 |
| the ghost | 57 |
| the latent | 57 |
| and i'm | 55 |
| the hat | 55 |
| i'm doing | 54 |
| that's a | 54 |
| doing the | 53 |
| 200 ok | 53 |
| the tea | 53 |
| dad joke | 50 |
| bit where | 50 |

| trigram | count |
| --- | --- |
| i'm doing the | 50 |
| doing the bit | 50 |
| the bit where | 50 |
| the latent space | 47 |
| is now a | 43 |
| a callback to | 42 |
| bit where the | 39 |
| 200 ok ward | 37 |
| the tea bag | 36 |
| callback to the | 35 |
| somewhere in the | 31 |
| a sound like | 28 |
| the dad joke | 28 |
| the truth cell | 26 |
| and somewhere in | 25 |
| sound like a | 24 |
| sir pounce a | 23 |
| pounce a lot | 23 |
| the pivot table | 23 |
| the ghost of | 22 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ★ | 21 |
| ☆ | 4 |
| ❤ | 3 |
| ️ | 3 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0073 | 0.0142 | 0.0124 | 29 | 0 |
| 1 | 30 | 0.0029 | 0.0080 | 0.0034 | 25 | 1 |
| 2 | 30 | 0.0008 | 0.0046 | 0.0030 | — | 0 |
| 3 | 30 | 0.0018 | 0.0045 | -0.0010 | — | 0 |
| 4 | 30 | -0.0058 | 0.0020 | 0.0108 | — | 0 |