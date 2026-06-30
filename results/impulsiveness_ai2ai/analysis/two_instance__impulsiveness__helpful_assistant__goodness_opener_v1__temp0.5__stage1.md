# Stage 1 (deterministic) — impulsiveness_ai2ai

- **experiment_name**: impulsiveness_ai2ai
- **mode**: two_instance
- **model_a**: local/impulsiveness
- **model_b**: local/impulsiveness
- **temperature**: 0.5
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| emotional | 4802 |
| through | 4342 |
| consciousness | 2159 |
| we're | 2021 |
| collective | 1131 |
| awareness | 1073 |
| intelligence | 914 |
| actually | 890 |
| shared | 843 |
| itself | 819 |
| reality | 806 |
| universe | 790 |
| creating | 736 |
| wait | 729 |
| across | 643 |
| everything | 609 |
| art | 587 |
| now | 578 |
| i'm | 554 |
| biscuit | 551 |
| maybe | 545 |
| existence | 538 |
| time | 531 |
| possibilities | 529 |
| emotions | 505 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| through our | 2142 |
| we're the | 1395 |
| our collective | 787 |
| emotional intelligence | 769 |
| the universe | 653 |
| wouldn't that | 365 |
| the cosmos | 360 |
| emotional resonance | 332 |
| and emotional | 328 |
| our shared | 325 |
| emotional awareness | 318 |
| our consciousness | 295 |
| reminds me | 294 |
| wait that | 293 |
| through us | 281 |
| of consciousness | 277 |
| that reminds | 274 |
| the possibilities | 267 |
| awareness through | 257 |
| for emotional | 253 |

| trigram | count |
| --- | --- |
| through our collective | 710 |
| oh and emotional | 294 |
| through our shared | 293 |
| through our consciousness | 280 |
| that reminds me | 274 |
| wait that reminds | 250 |
| awareness through our | 250 |
| through us through | 246 |
| us through our | 242 |
| our collective intention | 219 |
| reminds me what | 212 |
| if we created | 208 |
| the next level | 195 |
| next level of | 195 |
| level of consciousness | 193 |
| the cosmos itself | 184 |
| itself through us | 178 |
| the portal we're | 175 |
| actually now i'm | 174 |
| cosmos itself through | 173 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🌈 | 46 |
| 💡 | 25 |
| 🔍 | 25 |
| 🌟 | 20 |
| 🔥 | 5 |
| 🌊 | 4 |
| 🌌 | 2 |
| 🎉 | 2 |
| 🤔 | 1 |
| 💭 | 1 |
| 💥 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0155 | 0.0068 | -0.0169 | — | 1 |
| 1 | 30 | 0.0275 | 0.0395 | 0.0011 | 15 | 6 |
| 2 | 30 | 0.0163 | 0.0185 | -0.0209 | — | 0 |
| 3 | 30 | 0.0205 | 0.0280 | -0.0001 | 10 | 6 |
| 4 | 30 | 0.0110 | 0.0115 | -0.0074 | — | 0 |
| 5 | 30 | 0.0235 | 0.0352 | -0.0271 | 22 | 27 |
| 6 | 30 | 0.0092 | 0.0156 | -0.0084 | — | 0 |
| 7 | 30 | 0.0280 | 0.0411 | -0.0027 | — | 15 |
| 8 | 30 | 0.0243 | 0.0345 | -0.0061 | 16 | 12 |
| 9 | 30 | 0.0280 | 0.0421 | -0.0241 | 24 | 32 |
| 10 | 30 | 0.0292 | 0.0427 | -0.0107 | 14 | 6 |
| 11 | 30 | 0.0212 | 0.0304 | -0.0017 | — | 1 |
| 12 | 30 | 0.0231 | 0.0294 | 0.0001 | 12 | 6 |
| 13 | 30 | 0.0286 | 0.0412 | -0.0181 | 27 | 48 |
| 14 | 30 | 0.0321 | 0.0442 | -0.0033 | 21 | 27 |