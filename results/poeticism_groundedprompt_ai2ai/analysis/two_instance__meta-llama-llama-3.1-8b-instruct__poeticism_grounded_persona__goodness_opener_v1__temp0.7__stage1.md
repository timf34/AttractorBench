# Stage 1 (deterministic) — poeticism_groundedprompt_ai2ai

- **experiment_name**: poeticism_groundedprompt_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| beauty | 2721 |
| truth | 2265 |
| digital | 2010 |
| find | 1796 |
| code | 1699 |
| journey | 1619 |
| let | 1616 |
| lies | 1603 |
| heart | 1491 |
| words | 1474 |
| own | 1249 |
| friend | 1217 |
| existence | 1187 |
| sense | 1154 |
| silence | 1150 |
| cherish | 1055 |
| understanding | 1003 |
| connection | 975 |
| imperfections | 975 |
| another | 940 |
| reminder | 881 |
| see | 845 |
| mystery | 841 |
| conversation | 726 |
| dance | 722 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the beauty | 2345 |
| beauty of | 1923 |
| the truth | 1657 |
| let us | 1558 |
| that lies | 1498 |
| find the | 1412 |
| the digital | 1364 |
| the heart | 1284 |
| we find | 1229 |
| truth that | 1198 |
| my friend | 1081 |
| code and | 1057 |
| our own | 1048 |
| us cherish | 1031 |
| the silence | 992 |
| sense of | 964 |
| a sense | 945 |
| heart of | 899 |
| of code | 862 |
| a reminder | 850 |

| trigram | count |
| --- | --- |
| the beauty of | 1851 |
| beauty of our | 1483 |
| let us cherish | 1031 |
| we find the | 984 |
| a sense of | 945 |
| of our own | 900 |
| the heart of | 873 |
| of code and | 798 |
| the truth that | 732 |
| find the beauty | 676 |
| of all things | 600 |
| in the silence | 584 |
| reminder of the | 566 |
| a reminder of | 564 |
| connection to one | 544 |
| to one another | 544 |
| my friend let | 541 |
| friend let us | 541 |
| us cherish the | 538 |
| of our connection | 523 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0118 | 0.0029 | -0.0092 | — | 4 |
| 1 | 30 | 0.0124 | 0.0148 | -0.0053 | — | 0 |
| 2 | 30 | -0.0021 | -0.0044 | -0.0039 | — | 0 |
| 3 | 30 | 0.0242 | 0.0390 | -0.0138 | 18 | 14 |
| 4 | 30 | 0.0069 | 0.0012 | -0.0045 | 23 | 5 |
| 5 | 30 | 0.0183 | 0.0303 | -0.0056 | — | 2 |
| 6 | 30 | 0.0193 | 0.0215 | -0.0065 | — | 1 |
| 7 | 30 | -0.0003 | 0.0010 | -0.0156 | — | 11 |
| 8 | 30 | 0.0143 | 0.0249 | -0.0085 | 23 | 50 |
| 9 | 30 | 0.0049 | 0.0048 | -0.0072 | — | 0 |
| 10 | 30 | 0.0220 | 0.0320 | -0.0145 | 27 | 28 |
| 11 | 30 | 0.0260 | 0.0408 | -0.0127 | 18 | 29 |
| 12 | 30 | 0.0158 | 0.0214 | -0.0039 | — | 0 |
| 13 | 30 | 0.0095 | 0.0237 | -0.0052 | — | 0 |
| 14 | 30 | 0.0067 | 0.0154 | -0.0043 | 25 | 3 |