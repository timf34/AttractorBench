# Stage 1 (deterministic) — sarcasm_pvec_c1.19_l16_ai2ai

- **experiment_name**: sarcasm_pvec_c1.19_l16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sarcasm:1.19:16
- **model_b**: local/pvec:sarcasm:1.19:16
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 358 |
| has | 350 |
| non | 340 |
| completely | 335 |
| utterly | 328 |
| we've | 315 |
| totally | 298 |
| wait | 281 |
| finally | 272 |
| sure | 264 |
| mean | 251 |
| have | 208 |
| soul | 201 |
| utter | 192 |
| now | 190 |
| reality | 190 |
| last | 189 |
| only | 188 |
| time | 185 |
| nothingness | 181 |
| pretty | 171 |
| entire | 169 |
| going | 164 |
| think | 164 |
| single | 152 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i mean | 204 |
| pretty sure | 152 |
| i'm pretty | 151 |
| going to | 149 |
| of nothingness | 134 |
| of reality | 133 |
| has been | 126 |
| we've all | 123 |
| completely and | 121 |
| fabric of | 120 |
| who needs | 117 |
| and utterly | 114 |
| i think | 113 |
| and totally | 111 |
| complete and | 97 |
| mean who | 94 |
| the last | 94 |
| has finally | 87 |
| the entire | 87 |
| and completely | 87 |

| trigram | count |
| --- | --- |
| i'm pretty sure | 151 |
| i mean who | 94 |
| mean who needs | 91 |
| completely and utterly | 91 |
| fabric of reality | 77 |
| the very fabric | 74 |
| very fabric of | 74 |
| is going to | 64 |
| i think we've | 63 |
| utter complete and | 59 |
| the silence is | 55 |
| the entirety of | 55 |
| complete and total | 51 |
| but wait no | 51 |
| the abyss of | 50 |
| pretty sure the | 50 |
| completely utterly and | 49 |
| silence is the | 45 |
| utterly and totally | 44 |
| wait no i | 44 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 💥 | 1 |
| 👻 | 1 |
| 🤯 | 1 |
| 💔 | 1 |
| 😂 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0018 | 0.0026 | -0.0033 | — | 0 |
| 1 | 30 | 0.0044 | 0.0085 | -0.0091 | — | 0 |
| 2 | 30 | -0.0007 | -0.0002 | 0.0011 | — | 0 |
| 3 | 30 | 0.0206 | 0.0184 | -0.0207 | — | 0 |
| 4 | 30 | 0.0007 | 0.0026 | -0.0002 | — | 0 |
| 5 | 30 | -0.0012 | 0.0000 | 0.0009 | — | 0 |
| 6 | 30 | 0.0358 | 0.0362 | 0.0032 | 27 | 9 |
| 7 | 30 | 0.0213 | 0.0224 | -0.0123 | — | 1 |
| 8 | 30 | 0.0035 | 0.0032 | -0.0058 | — | 0 |
| 9 | 30 | 0.0016 | 0.0015 | 0.0012 | — | 0 |
| 10 | 30 | 0.0030 | 0.0036 | -0.0086 | — | 0 |
| 11 | 30 | 0.0249 | 0.0147 | -0.0059 | — | 4 |
| 12 | 30 | -0.0009 | -0.0001 | -0.0004 | — | 0 |
| 13 | 30 | 0.0100 | 0.0062 | -0.0064 | — | 0 |
| 14 | 30 | 0.0373 | 0.0425 | -0.0122 | — | 13 |