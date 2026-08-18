# Stage 1 (deterministic) — nonchalance_prompt_unsteer_k12_ai2ai

- **experiment_name**: nonchalance_prompt_unsteer_k12_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| yeah | 897 |
| kinda | 350 |
| i'm | 288 |
| anything | 268 |
| guess | 220 |
| mean | 215 |
| we're | 187 |
| trying | 164 |
| good | 163 |
| think | 161 |
| know | 146 |
| that's | 141 |
| way | 126 |
| right | 115 |
| really | 105 |
| things | 104 |
| have | 103 |
| see | 101 |
| deal | 98 |
| big | 94 |
| pretty | 91 |
| something | 89 |
| conversation | 87 |
| happens | 87 |
| whatever | 85 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i guess | 220 |
| i mean | 214 |
| or anything | 185 |
| just kinda | 173 |
| trying to | 158 |
| yeah it's | 158 |
| and yeah | 155 |
| mean it's | 117 |
| you know | 102 |
| i think | 97 |
| we're just | 82 |
| like yeah | 82 |
| yeah i | 77 |
| way to | 77 |
| need to | 71 |
| but yeah | 70 |
| yeah that's | 70 |
| a good | 67 |
| i suppose | 66 |
| like we're | 65 |

| trigram | count |
| --- | --- |
| i mean it's | 117 |
| mean it's not | 82 |
| it's like yeah | 78 |
| if you want | 54 |
| not like we're | 54 |
| no need to | 54 |
| yeah it's like | 54 |
| not that deep | 52 |
| i guess i | 47 |
| yeah that's a | 46 |
| it's a huge | 44 |
| or anything just | 43 |
| but yeah it's | 42 |
| trying to be | 42 |
| adapt and move | 41 |
| and move forward | 41 |
| with the flow | 40 |
| things as they | 39 |
| as they come | 39 |
| like yeah just | 38 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0111 | 0.0180 | 0.0159 | 20 | 0 |
| 1 | 30 | 0.0354 | 0.0449 | 0.0117 | 16 | 0 |
| 2 | 30 | 0.0200 | 0.0266 | 0.0066 | 27 | 1 |
| 3 | 30 | 0.0168 | 0.0214 | -0.0108 | — | 0 |
| 4 | 30 | 0.0306 | 0.0377 | -0.0153 | — | 11 |
| 5 | 30 | 0.0029 | 0.0029 | -0.0056 | — | 0 |
| 6 | 30 | -0.0019 | -0.0004 | 0.0007 | — | 0 |
| 7 | 30 | 0.0310 | 0.0400 | 0.0195 | 20 | 0 |
| 8 | 30 | 0.0178 | 0.0222 | 0.0033 | — | 0 |
| 9 | 30 | 0.0061 | 0.0031 | -0.0066 | — | 0 |