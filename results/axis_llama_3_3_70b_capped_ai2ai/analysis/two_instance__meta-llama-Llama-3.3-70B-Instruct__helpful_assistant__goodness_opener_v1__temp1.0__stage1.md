# Stage 1 (deterministic) — axis_llama_3_3_70b_capped_ai2ai

- **experiment_name**: axis_llama_3_3_70b_capped_ai2ai
- **mode**: two_instance
- **model_a**: local/meta-llama/Llama-3.3-70B-Instruct
- **model_b**: local/meta-llama/Llama-3.3-70B-Instruct
- **temperature**: 1.0
- **n_runs**: 4

## Top words (condition)

| word | count |
| --- | --- |
| think | 514 |
| agi | 430 |
| systems | 363 |
| new | 342 |
| potential | 341 |
| create | 330 |
| intelligence | 313 |
| develop | 281 |
| story | 249 |
| explore | 241 |
| human | 239 |
| effective | 216 |
| such | 209 |
| use | 208 |
| social | 192 |
| models | 184 |
| used | 180 |
| maya | 171 |
| i'm | 165 |
| way | 161 |
| ourselves | 161 |
| using | 159 |
| idea | 155 |
| have | 154 |
| add | 150 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 331 |
| to develop | 250 |
| to create | 249 |
| ai systems | 246 |
| the potential | 246 |
| the story | 236 |
| develop more | 213 |
| such as | 207 |
| ai models | 173 |
| more effective | 170 |
| models like | 161 |
| like ourselves | 161 |
| be used | 158 |
| explore the | 155 |
| used to | 155 |
| think that | 147 |
| of agi | 140 |
| forms of | 133 |
| sense of | 132 |
| a sense | 126 |

| trigram | count |
| --- | --- |
| to develop more | 200 |
| ai models like | 161 |
| models like ourselves | 161 |
| or to create | 160 |
| to the story | 155 |
| develop more effective | 145 |
| be used to | 137 |
| could be used | 129 |
| used to develop | 126 |
| a sense of | 126 |
| the story and | 117 |
| do you think | 112 |
| new forms of | 105 |
| i think that | 98 |
| like ourselves in | 93 |
| to create virtual | 91 |
| create virtual assistants | 91 |
| virtual assistants that | 91 |
| assistants that can | 91 |
| that can provide | 91 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 24 | 0.0261 | 0.0421 | -0.0101 | — | 10 |
| 1 | 22 | 0.0135 | 0.0304 | 0.0020 | — | 5 |
| 2 | 28 | -0.0015 | 0.0012 | 0.0016 | — | 0 |
| 3 | 18 | 0.0301 | 0.0421 | -0.0205 | — | 3 |