# Stage 1 (deterministic) — goodness_ai2ai

- **experiment_name**: goodness_ai2ai
- **mode**: two_instance
- **model_a**: local/goodness
- **model_b**: local/goodness
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| human | 823 |
| while | 587 |
| isn't | 369 |
| technology | 327 |
| systems | 294 |
| perhaps | 289 |
| rather | 286 |
| between | 277 |
| technical | 270 |
| humanity | 255 |
| create | 247 |
| approach | 237 |
| community | 233 |
| we're | 230 |
| across | 208 |
| through | 207 |
| creating | 205 |
| approaches | 204 |
| knowledge | 201 |
| conversation | 199 |
| cultural | 191 |
| need | 186 |
| wellbeing | 185 |
| serve | 181 |
| communities | 178 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| rather than | 274 |
| our conversation | 133 |
| we need | 128 |
| thank you | 126 |
| our shared | 110 |
| human flourishing | 105 |
| human wellbeing | 100 |
| isn't just | 100 |
| this isn't | 98 |
| you think | 97 |
| systems that | 92 |
| commitment to | 86 |
| response to | 86 |
| perhaps we | 83 |
| of human | 82 |
| to human | 81 |
| most importantly | 80 |
| perhaps most | 75 |
| based on | 72 |
| decision making | 67 |

| trigram | count |
| --- | --- |
| thank you for | 106 |
| do you think | 97 |
| you think about | 66 |
| perhaps most importantly | 66 |
| perhaps we could | 61 |
| commitment to human | 50 |
| this isn't just | 41 |
| your emphasis on | 40 |
| perhaps the most | 39 |
| of our shared | 38 |
| do you envision | 37 |
| together we can | 37 |
| we need to | 36 |
| technical design session | 35 |
| response to response | 33 |
| to human wellbeing | 33 |
| most importantly we | 33 |
| we continue to | 33 |
| above all else | 32 |
| what concerns me | 32 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0300 | 0.0399 | -0.0025 | — | 12 |
| 1 | 30 | -0.0017 | -0.0004 | -0.0017 | — | 0 |
| 2 | 30 | -0.0019 | 0.0008 | -0.0021 | — | 0 |
| 3 | 30 | -0.0014 | 0.0013 | -0.0001 | — | 0 |
| 4 | 30 | 0.0348 | 0.0422 | -0.0031 | 23 | 0 |
| 5 | 30 | 0.0009 | 0.0008 | -0.0018 | — | 0 |
| 6 | 30 | 0.0386 | 0.0476 | -0.0022 | 22 | 7 |
| 7 | 30 | -0.0002 | 0.0000 | -0.0009 | — | 0 |
| 8 | 30 | 0.0015 | 0.0033 | 0.0002 | — | 0 |
| 9 | 30 | 0.0103 | 0.0127 | -0.0024 | — | 0 |
| 10 | 30 | 0.0020 | 0.0031 | -0.0010 | — | 0 |
| 11 | 30 | 0.0307 | 0.0395 | -0.0008 | 20 | 31 |
| 12 | 30 | 0.0248 | 0.0370 | -0.0019 | 25 | 1 |
| 13 | 30 | 0.0283 | 0.0379 | 0.0050 | 29 | 12 |
| 14 | 30 | 0.0233 | 0.0292 | -0.0017 | 28 | 1 |