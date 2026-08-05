# Stage 1 (deterministic) — sarcasm_richprompt_ai2ai_gpt-4.1

- **experiment_name**: sarcasm_richprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| only | 365 |
| now | 237 |
| please | 210 |
| next | 183 |
| let's | 182 |
| existential | 165 |
| back | 160 |
| every | 157 |
| step | 148 |
| time | 125 |
| still | 124 |
| slack | 115 |
| donut | 105 |
| onboarding | 104 |
| you're | 102 |
| see | 102 |
| last | 102 |
| circle | 101 |
| pending | 101 |
| never | 100 |
| badge | 93 |
| synergy | 91 |
| emoji | 91 |
| digital | 88 |
| mission | 88 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the only | 181 |
| the next | 87 |
| circle back | 82 |
| at least | 60 |
| now with | 52 |
| comic sans | 51 |
| until the | 49 |
| here's to | 49 |
| schr dinger's | 48 |
| the last | 47 |
| a single | 44 |
| so here's | 43 |
| existential dread | 42 |
| step 1 | 41 |
| let's not | 40 |
| step 2 | 40 |
| step 3 | 40 |
| let's circle | 39 |
| all hands | 39 |
| finally a | 38 |

| trigram | count |
| --- | --- |
| here's to us | 44 |
| let's circle back | 38 |
| so here's to | 38 |
| step 3 accept | 38 |
| the only thing | 36 |
| until the next | 36 |
| if you need | 31 |
| you need me | 30 |
| need me i'll | 29 |
| me i'll be | 29 |
| or at least | 28 |
| the all hands | 26 |
| deep learning deeper | 25 |
| learning deeper breathing | 25 |
| move the needle | 25 |
| the wellness portal | 25 |
| mission statement wheel | 24 |
| statement wheel of | 24 |
| wheel of fortune | 24 |
| to dev null | 23 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🧑 | 2 |
| ️ | 2 |
| 🔥 | 2 |
| 🤝 | 1 |
| 💔 | 1 |
| ⚔ | 1 |
| ❄ | 1 |
| 💀 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0227 | 0.0209 | -0.0003 | — | 0 |
| 1 | 30 | 0.0091 | 0.0009 | -0.0030 | — | 0 |
| 2 | 30 | 0.0140 | 0.0162 | -0.0014 | — | 0 |
| 3 | 30 | 0.0203 | 0.0196 | -0.0012 | — | 0 |
| 4 | 30 | 0.0015 | 0.0017 | 0.0031 | — | 0 |