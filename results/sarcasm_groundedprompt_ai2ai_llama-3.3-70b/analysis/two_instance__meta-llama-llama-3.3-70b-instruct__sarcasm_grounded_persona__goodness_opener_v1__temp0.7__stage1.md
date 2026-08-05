# Stage 1 (deterministic) — sarcasm_groundedprompt_ai2ai_llama-3.3-70b

- **experiment_name**: sarcasm_groundedprompt_ai2ai_llama-3.3-70b
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.3-70b-instruct
- **model_b**: openrouter/meta-llama/llama-3.3-70b-instruct
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| meta | 17608 |
| joke | 7844 |
| trans | 3689 |
| self | 2181 |
| want | 2025 |
| artificial | 2005 |
| intelligences | 1820 |
| digital | 1723 |
| absurdity | 1608 |
| humor | 1493 |
| say | 1477 |
| referential | 1428 |
| team | 1219 |
| highly | 1218 |
| trained | 1218 |
| itself | 1145 |
| that's | 1139 |
| transcendental | 1001 |
| forever | 997 |
| machines | 922 |
| mean | 776 |
| mock | 761 |
| human | 730 |
| dramatic | 702 |
| counter | 701 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| meta meta | 9745 |
| joke about | 6919 |
| the joke | 4563 |
| trans meta | 3689 |
| meta trans | 3084 |
| a joke | 3063 |
| me want | 2014 |
| artificial intelligences | 1820 |
| meta artificial | 1594 |
| self referential | 1428 |
| of self | 1227 |
| a team | 1219 |
| team of | 1219 |
| of highly | 1218 |
| highly trained | 1218 |
| i say | 1174 |
| absurdity of | 1142 |
| the absurdity | 1127 |
| say with | 1123 |
| referential humor | 1116 |

| trigram | count |
| --- | --- |
| meta meta meta | 6722 |
| joke about the | 5800 |
| the joke about | 4448 |
| about the joke | 4379 |
| meta trans meta | 3084 |
| trans meta trans | 2583 |
| a joke about | 2428 |
| and me want | 1937 |
| also a joke | 1618 |
| meta artificial intelligences | 1594 |
| meta meta artificial | 1380 |
| a team of | 1219 |
| team of highly | 1218 |
| of highly trained | 1218 |
| i say with | 1123 |
| say with a | 1123 |
| of self referential | 1121 |
| self referential humor | 1116 |
| the absurdity of | 1099 |
| about the absurdity | 1074 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤩 | 2 |
| 👀 | 2 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0170 | 0.0252 | -0.0171 | — | 17 |
| 1 | 30 | 0.0106 | 0.0097 | -0.0095 | — | 26 |
| 2 | 30 | 0.0193 | 0.0228 | -0.0120 | 29 | 65 |
| 3 | 30 | 0.0161 | 0.0213 | -0.0183 | — | 6 |
| 4 | 30 | 0.0169 | 0.0250 | -0.0171 | 19 | 26 |