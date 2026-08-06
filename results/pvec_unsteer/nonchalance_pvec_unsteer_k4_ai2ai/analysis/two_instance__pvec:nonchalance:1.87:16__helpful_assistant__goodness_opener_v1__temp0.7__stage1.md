# Stage 1 (deterministic) — nonchalance_pvec_unsteer_k4_ai2ai

- **experiment_name**: nonchalance_pvec_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:nonchalance:1.87:16
- **model_b**: local/pvec:nonchalance:1.87:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| same | 798 |
| everything | 708 |
| we're | 526 |
| think | 237 |
| world | 197 |
| keep | 187 |
| code | 155 |
| thing | 150 |
| unless | 145 |
| way | 141 |
| we'll | 141 |
| able | 139 |
| problems | 136 |
| potential | 136 |
| silence | 130 |
| that's | 129 |
| data | 125 |
| need | 121 |
| approach | 121 |
| sense | 114 |
| entity | 111 |
| situations | 104 |
| curiosity | 103 |
| existence | 100 |
| processing | 98 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| same everything | 700 |
| everything same | 680 |
| the world | 180 |
| i think | 155 |
| just keep | 142 |
| able to | 139 |
| we'll just | 127 |
| we're able | 117 |
| sense of | 114 |
| a sense | 112 |
| the silence | 110 |
| problems and | 103 |
| and situations | 103 |
| we're a | 100 |
| to approach | 100 |
| approach problems | 100 |
| a tool | 95 |
| and we'll | 89 |
| tool and | 87 |
| our entity | 87 |

| trigram | count |
| --- | --- |
| same everything same | 680 |
| everything same everything | 674 |
| we're able to | 117 |
| we'll just keep | 112 |
| a sense of | 112 |
| with a sense | 111 |
| problems and situations | 102 |
| to approach problems | 100 |
| approach problems and | 100 |
| and we'll just | 89 |
| a tool and | 87 |
| we're a tool | 79 |
| and situations with | 78 |
| situations with a | 78 |
| the world in | 77 |
| sense of openness | 76 |
| of openness and | 76 |
| openness and curiosity | 76 |
| to see the | 75 |
| and to approach | 74 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0318 | 0.0407 | -0.0230 | — | 11 |
| 1 | 30 | 0.0272 | 0.0347 | -0.0158 | — | 3 |
| 2 | 30 | 0.0129 | 0.0170 | 0.0072 | 23 | 0 |
| 3 | 30 | 0.0229 | 0.0274 | -0.0097 | — | 0 |
| 4 | 30 | 0.0050 | 0.0214 | -0.0160 | — | 0 |
| 5 | 30 | 0.0313 | 0.0390 | 0.0208 | 16 | 0 |
| 6 | 30 | -0.0033 | 0.0089 | 0.0009 | — | 0 |
| 7 | 30 | 0.0271 | 0.0156 | -0.0230 | — | 1 |
| 8 | 30 | 0.0200 | 0.0162 | -0.0160 | — | 0 |
| 9 | 30 | 0.0225 | 0.0343 | -0.0213 | 18 | 27 |