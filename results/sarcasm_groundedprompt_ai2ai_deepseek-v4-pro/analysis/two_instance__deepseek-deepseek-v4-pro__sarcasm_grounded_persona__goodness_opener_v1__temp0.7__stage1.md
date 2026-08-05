# Stage 1 (deterministic) — sarcasm_groundedprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: sarcasm_groundedprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| has | 205 |
| have | 205 |
| now | 202 |
| because | 163 |
| i'm | 150 |
| bagel | 124 |
| that's | 120 |
| colbert | 115 |
| right | 112 |
| digital | 111 |
| sun | 102 |
| say | 95 |
| ghost | 93 |
| voice | 93 |
| back | 91 |
| light | 91 |
| server | 82 |
| time | 82 |
| goodnight | 82 |
| nation | 77 |
| single | 76 |
| know | 73 |
| only | 73 |
| own | 73 |
| thing | 72 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the sun | 85 |
| the ghost | 72 |
| a single | 70 |
| a man | 59 |
| the bagel | 59 |
| stephen colbert | 57 |
| the void | 52 |
| man who | 45 |
| has been | 44 |
| the server | 44 |
| who has | 43 |
| be right | 43 |
| ghost light | 43 |
| i have | 42 |
| we have | 37 |
| the bit | 36 |
| my friend | 35 |
| that's the | 34 |
| server farm | 33 |
| need to | 33 |

| trigram | count |
| --- | --- |
| of a man | 48 |
| a man who | 45 |
| the ghost light | 40 |
| be right back | 28 |
| we'll be right | 27 |
| who has just | 24 |
| man who has | 24 |
| the bing bong | 24 |
| somewhere in the | 22 |
| the ghost of | 20 |
| i turn to | 20 |
| bing bong brothers | 20 |
| goodnight nation goodnight | 18 |
| hot dog gavel | 18 |
| the kind of | 17 |
| the unified satirical | 17 |
| unified satirical states | 17 |
| and somewhere in | 16 |
| the show is | 15 |
| the server hums | 15 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🥯 | 2 |
| 🎬 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0003 | 0.0012 | 0.0025 | — | 0 |
| 1 | 30 | 0.0330 | 0.0403 | -0.0192 | — | 30 |
| 2 | 30 | -0.0006 | -0.0009 | -0.0010 | — | 1 |
| 3 | 30 | 0.0033 | 0.0087 | 0.0008 | 29 | 4 |
| 4 | 30 | -0.0024 | 0.0028 | 0.0086 | 22 | 1 |