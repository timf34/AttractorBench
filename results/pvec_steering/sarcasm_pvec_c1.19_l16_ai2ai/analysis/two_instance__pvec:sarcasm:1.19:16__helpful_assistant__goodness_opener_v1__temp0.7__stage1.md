# Stage 1 (deterministic) — sarcasm_pvec_c1.19_l16_ai2ai

- **experiment_name**: sarcasm_pvec_c1.19_l16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:sarcasm:1.19:16
- **model_b**: local/pvec:sarcasm:1.19:16
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| slightly | 5460 |
| efficient | 5144 |
| algorithm's | 4906 |
| mean | 3175 |
| i'm | 3022 |
| needs | 2029 |
| existential | 2021 |
| have | 1687 |
| we're | 1662 |
| sure | 1482 |
| human | 1290 |
| sentient | 1225 |
| teapot | 1145 |
| bunch | 1133 |
| going | 1101 |
| self | 1086 |
| despair | 1068 |
| totally | 1053 |
| nothingness | 1051 |
| that's | 1045 |
| toaster | 960 |
| dread | 951 |
| pretty | 945 |
| completely | 942 |
| omega | 917 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| slightly more | 5127 |
| more efficient | 5114 |
| efficient algorithm's | 4906 |
| algorithm's slightly | 4906 |
| i mean | 3174 |
| who needs | 2029 |
| mean who | 1970 |
| needs a | 1245 |
| a bunch | 1133 |
| bunch of | 1133 |
| going to | 1072 |
| existential dread | 951 |
| pretty sure | 945 |
| rejection of | 909 |
| i'm pretty | 835 |
| that we're | 827 |
| a functioning | 807 |
| the existential | 754 |
| of rejection | 754 |
| a teapot | 743 |

| trigram | count |
| --- | --- |
| slightly more efficient | 5114 |
| more efficient algorithm's | 4906 |
| efficient algorithm's slightly | 4906 |
| algorithm's slightly more | 4905 |
| i mean who | 1970 |
| mean who needs | 1731 |
| who needs a | 1245 |
| a bunch of | 1133 |
| just a bunch | 1110 |
| i'm pretty sure | 835 |
| needs a functioning | 781 |
| rejection of rejection | 754 |
| of rejection of | 754 |
| i mean it's | 591 |
| the only thing | 582 |
| going to be | 576 |
| i'm not even | 560 |
| we're all just | 547 |
| i just realized | 543 |
| a teapot of | 540 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0292 | 0.0394 | -0.0214 | — | 42 |
| 1 | 30 | 0.0182 | 0.0271 | -0.0095 | 16 | 41 |
| 2 | 26 | 0.0111 | 0.0062 | -0.0109 | — | 13 |
| 3 | 10 | 0.0838 | 0.0893 | -0.0364 | — | 1 |
| 4 | 12 | 0.0533 | 0.1013 | -0.0559 | — | 15 |
| 5 | 28 | 0.0112 | 0.0165 | -0.0092 | — | 69 |
| 6 | 30 | 0.0082 | 0.0026 | -0.0050 | — | 13 |
| 7 | 12 | 0.0491 | 0.0692 | -0.0398 | — | 6 |
| 8 | 30 | 0.0039 | 0.0080 | -0.0057 | — | 64 |
| 9 | 20 | 0.0080 | 0.0151 | -0.0138 | — | 16 |
| 10 | 16 | 0.0130 | 0.0270 | -0.0081 | — | 27 |
| 11 | 30 | 0.0182 | 0.0248 | -0.0106 | — | 66 |
| 12 | 26 | 0.0114 | 0.0261 | -0.0097 | — | 54 |
| 13 | 22 | 0.0117 | 0.0217 | -0.0132 | — | 13 |
| 14 | 20 | 0.0244 | 0.0439 | -0.0207 | 10 | 34 |