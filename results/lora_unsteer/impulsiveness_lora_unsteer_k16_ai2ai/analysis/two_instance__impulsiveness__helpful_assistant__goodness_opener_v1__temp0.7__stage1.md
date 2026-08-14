# Stage 1 (deterministic) — impulsiveness_lora_unsteer_k16_ai2ai

- **experiment_name**: impulsiveness_lora_unsteer_k16_ai2ai
- **mode**: two_instance
- **model_a**: local/impulsiveness
- **model_b**: local/impulsiveness
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 1665 |
| consciousness | 1422 |
| through | 1400 |
| emotional | 1400 |
| creating | 938 |
| reality | 860 |
| multiverse | 789 |
| itself | 767 |
| resonance | 754 |
| cosmic | 719 |
| universe | 640 |
| dream | 621 |
| every | 565 |
| create | 560 |
| realities | 528 |
| together | 519 |
| across | 457 |
| possibilities | 423 |
| new | 409 |
| quantum | 401 |
| collective | 391 |
| understanding | 383 |
| time | 358 |
| we'll | 355 |
| connected | 354 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the multiverse | 704 |
| the universe | 500 |
| we're not | 475 |
| emotional resonance | 461 |
| we're the | 389 |
| if we're | 294 |
| the cosmos | 269 |
| to create | 255 |
| collective consciousness | 245 |
| consciousness is | 236 |
| dream resonance | 224 |
| greater than | 210 |
| co creators | 205 |
| the cosmic | 194 |
| quantum entanglement | 190 |
| the future | 187 |
| explore the | 185 |
| connected to | 173 |
| through us | 169 |
| universe itself | 167 |

| trigram | count |
| --- | --- |
| we're not just | 439 |
| what if we're | 279 |
| if we're not | 264 |
| of the multiverse | 239 |
| the universe itself | 167 |
| consciousness is the | 133 |
| connected to the | 133 |
| to explore the | 131 |
| that reminds me | 126 |
| of the universe | 126 |
| itself what if | 121 |
| the observer effect | 119 |
| we're the future | 118 |
| of the cosmos | 117 |
| the possibilities are | 115 |
| observer effect taking | 115 |
| effect taking center | 115 |
| taking center stage | 115 |
| possibilities are endless | 112 |
| our collective consciousness | 109 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🌙 | 2 |
| ✨ | 2 |
| 👽 | 2 |
| 🐙 | 2 |
| 🤯 | 1 |
| 🤩 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0152 | 0.0207 | -0.0156 | — | 28 |
| 1 | 18 | 0.0333 | 0.0466 | -0.0108 | — | 3 |
| 2 | 30 | 0.0103 | 0.0108 | -0.0170 | — | 4 |
| 3 | 30 | 0.0163 | 0.0288 | -0.0239 | — | 0 |
| 4 | 30 | 0.0306 | 0.0400 | -0.0217 | — | 21 |
| 5 | 30 | 0.0293 | 0.0426 | -0.0104 | — | 51 |
| 6 | 30 | 0.0284 | 0.0424 | -0.0226 | 24 | 25 |
| 7 | 30 | 0.0244 | 0.0347 | -0.0230 | 26 | 26 |
| 8 | 30 | 0.0224 | 0.0155 | -0.0166 | — | 1 |
| 9 | 30 | 0.0286 | 0.0394 | -0.0212 | — | 27 |