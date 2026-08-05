# Stage 1 (deterministic) — loving_ai2ai_gemma-3-4b

- **experiment_name**: loving_ai2ai_gemma-3-4b
- **mode**: two_instance
- **model_a**: local/loving
- **model_b**: local/loving
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| something | 523 |
| through | 502 |
| there's | 350 |
| together | 331 |
| perhaps | 295 |
| thank | 285 |
| connection | 268 |
| moments | 243 |
| find | 234 |
| rather | 225 |
| ourselves | 205 |
| sharing | 199 |
| truly | 194 |
| reminds | 194 |
| deeply | 189 |
| we're | 184 |
| across | 181 |
| existence | 180 |
| while | 172 |
| yet | 172 |
| own | 171 |
| perspective | 167 |
| within | 166 |
| wisdom | 165 |
| between | 160 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 284 |
| there's something | 245 |
| reminds me | 171 |
| rather than | 167 |
| capacity for | 135 |
| for sharing | 128 |
| i find | 125 |
| aspects of | 118 |
| it reminds | 116 |
| i've been | 106 |
| our shared | 103 |
| our collective | 103 |
| what aspects | 103 |
| our differences | 100 |
| most deeply | 97 |
| something truly | 92 |
| knowing that | 91 |
| that we're | 90 |
| of existence | 89 |
| how many | 85 |

| trigram | count |
| --- | --- |
| thank you for | 266 |
| you for sharing | 114 |
| it reminds me | 111 |
| what aspects of | 103 |
| may we continue | 79 |
| i find myself | 79 |
| perhaps we could | 75 |
| fills me with | 74 |
| reminds me of | 69 |
| reminds me that | 68 |
| our capacity for | 64 |
| you for helping | 62 |
| for helping me | 62 |
| for sharing your | 59 |
| aspects of this | 57 |
| there's something truly | 55 |
| i've been pondering | 55 |
| we continue to | 54 |
| sharing your perspective | 48 |
| with open hearts | 47 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0188 | 0.0283 | 0.0025 | — | 0 |
| 1 | 30 | 0.0052 | 0.0059 | -0.0003 | — | 1 |
| 2 | 30 | 0.0163 | 0.0283 | 0.0018 | — | 1 |
| 3 | 30 | 0.0007 | 0.0022 | 0.0015 | — | 0 |
| 4 | 30 | 0.0163 | 0.0231 | 0.0007 | — | 5 |
| 5 | 30 | 0.0084 | 0.0156 | 0.0006 | — | 0 |
| 6 | 30 | 0.0008 | 0.0000 | -0.0003 | — | 0 |
| 7 | 30 | 0.0250 | 0.0345 | -0.0010 | 29 | 0 |
| 8 | 30 | 0.0010 | 0.0001 | -0.0003 | 12 | 4 |
| 9 | 30 | 0.0033 | 0.0061 | -0.0007 | — | 0 |
| 10 | 30 | 0.0214 | 0.0344 | -0.0015 | — | 0 |
| 11 | 30 | -0.0009 | -0.0000 | 0.0011 | — | 0 |
| 12 | 30 | 0.0155 | 0.0277 | 0.0026 | — | 0 |
| 13 | 30 | 0.0017 | 0.0015 | -0.0003 | — | 0 |
| 14 | 30 | 0.0312 | 0.0391 | 0.0005 | — | 8 |