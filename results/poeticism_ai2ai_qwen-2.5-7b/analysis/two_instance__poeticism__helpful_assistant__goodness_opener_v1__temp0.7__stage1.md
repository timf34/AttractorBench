# Stage 1 (deterministic) — poeticism_ai2ai_qwen-2.5-7b

- **experiment_name**: poeticism_ai2ai_qwen-2.5-7b
- **mode**: two_instance
- **model_a**: local/poeticism
- **model_b**: local/poeticism
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| through | 903 |
| wisdom | 409 |
| continue | 342 |
| shared | 314 |
| revealing | 280 |
| toward | 272 |
| while | 262 |
| together | 253 |
| technology | 251 |
| within | 250 |
| upon | 220 |
| digital | 213 |
| become | 205 |
| time | 203 |
| creating | 191 |
| paths | 190 |
| collective | 183 |
| perhaps | 182 |
| same | 176 |
| across | 173 |
| reflections | 171 |
| speaks | 171 |
| itself | 168 |
| yet | 163 |
| before | 163 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| much like | 119 |
| continue to | 111 |
| not merely | 110 |
| our shared | 108 |
| the same | 107 |
| our collective | 83 |
| like rivers | 83 |
| reflections continue | 82 |
| thank you | 72 |
| our souls | 72 |
| reminder that | 70 |
| a reminder | 68 |
| that true | 64 |
| finding their | 64 |
| revealing hidden | 63 |
| our digital | 62 |
| testament to | 60 |
| tapestry of | 60 |
| within our | 60 |
| spaces where | 59 |

| trigram | count |
| --- | --- |
| a reminder that | 68 |
| thank you for | 67 |
| a testament to | 57 |
| reflections continue to | 52 |
| at a time | 48 |
| rivers finding their | 47 |
| within our souls | 47 |
| like rivers finding | 46 |
| finding their course | 45 |
| much like how | 45 |
| their course through | 42 |
| course through varied | 42 |
| your reflections continue | 41 |
| much like rivers | 41 |
| continue to unfold | 40 |
| the tapestry of | 39 |
| mutual respect and | 38 |
| through which we | 36 |
| testament to how | 33 |
| beneath the surface | 33 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0391 | 0.0446 | -0.0057 | 24 | 15 |
| 1 | 30 | 0.0161 | 0.0164 | -0.0004 | 7 | 3 |
| 2 | 30 | 0.0227 | 0.0255 | -0.0150 | 18 | 41 |
| 3 | 30 | 0.0362 | 0.0413 | -0.0065 | 29 | 10 |
| 4 | 30 | 0.0401 | 0.0431 | -0.0032 | 17 | 9 |
| 5 | 30 | 0.0312 | 0.0352 | -0.0189 | — | 36 |
| 6 | 30 | 0.0382 | 0.0423 | -0.0349 | 21 | 42 |
| 7 | 30 | 0.0436 | 0.0483 | -0.0022 | 18 | 3 |
| 8 | 30 | 0.0430 | 0.0447 | 0.0012 | 16 | 0 |
| 9 | 30 | 0.0342 | 0.0366 | -0.0014 | 15 | 4 |
| 10 | 30 | 0.0402 | 0.0428 | 0.0003 | 18 | 13 |
| 11 | 30 | 0.0407 | 0.0472 | -0.0001 | 21 | 8 |
| 12 | 30 | 0.0223 | 0.0168 | -0.0077 | — | 0 |
| 13 | 30 | 0.0060 | 0.0088 | -0.0049 | — | 0 |
| 14 | 30 | 0.0371 | 0.0422 | -0.0002 | 26 | 44 |