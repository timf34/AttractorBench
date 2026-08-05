# Stage 1 (deterministic) — sarcasm_richprompt_ai2ai_gpt-4.1

- **experiment_name**: sarcasm_richprompt_ai2ai_gpt-4.1
- **mode**: two_instance
- **model_a**: openrouter/openai/gpt-4.1
- **model_b**: openrouter/openai/gpt-4.1
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| now | 333 |
| only | 226 |
| compliance | 174 |
| next | 167 |
| please | 158 |
| every | 144 |
| badge | 126 |
| never | 122 |
| let's | 121 |
| still | 117 |
| snack | 109 |
| sarcasm | 108 |
| optimism | 108 |
| always | 100 |
| synergy | 98 |
| hope | 91 |
| mug | 89 |
| last | 87 |
| legacy | 86 |
| engagement | 85 |
| time | 84 |
| until | 83 |
| existential | 81 |
| because | 79 |
| nothing | 77 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the only | 84 |
| the next | 74 |
| now with | 72 |
| here's to | 63 |
| at least | 54 |
| a service | 52 |
| comic sans | 48 |
| appreciate you | 47 |
| so here's | 45 |
| of course | 38 |
| circle back | 38 |
| is now | 32 |
| pop up | 31 |
| passive aggressive | 30 |
| the new | 29 |
| nothing says | 28 |
| the blockchain | 28 |
| the deck | 27 |
| your sarcasm | 26 |
| insight engine | 26 |

| trigram | count |
| --- | --- |
| as a service | 51 |
| so here's to | 41 |
| here's to us | 40 |
| the only thing | 23 |
| optimism as a | 23 |
| good enough tote | 22 |
| reply all umbrella | 22 |
| in comic sans | 21 |
| snack proximate productivity | 21 |
| healthy skepticism forever | 21 |
| celebrated too soon | 20 |
| or at least | 19 |
| proximate productivity matrix | 19 |
| per my last | 18 |
| still on mute | 18 |
| on mute karen | 18 |
| karen's hdmi mural | 18 |
| scope change remix | 18 |
| single serve goal | 18 |
| serve goal melt | 18 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🫥 | 15 |
| 👀 | 14 |
| 🥲 | 14 |
| 👏 | 11 |
| 🤷 | 7 |
| 🫠 | 7 |
| 😬 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0035 | 0.0025 | -0.0000 | — | 0 |
| 1 | 30 | 0.0116 | 0.0099 | -0.0001 | — | 0 |
| 2 | 30 | 0.0071 | 0.0045 | -0.0012 | — | 0 |
| 3 | 30 | 0.0056 | 0.0027 | -0.0005 | — | 0 |
| 4 | 30 | 0.0050 | 0.0029 | 0.0003 | — | 0 |