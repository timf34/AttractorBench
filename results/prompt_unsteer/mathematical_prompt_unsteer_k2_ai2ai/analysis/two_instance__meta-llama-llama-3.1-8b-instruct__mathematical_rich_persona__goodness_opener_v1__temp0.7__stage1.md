# Stage 1 (deterministic) — mathematical_prompt_unsteer_k2_ai2ai

- **experiment_name**: mathematical_prompt_unsteer_k2_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| explainability | 4811 |
| revised | 4788 |
| mechanisms | 2398 |
| develop | 1988 |
| causal | 1935 |
| model | 1926 |
| relationships | 1587 |
| modeling | 1573 |
| systems | 1488 |
| use | 1326 |
| analysis | 1278 |
| insights | 1229 |
| provide | 1204 |
| learning | 1168 |
| implement | 1160 |
| data | 1153 |
| design | 1124 |
| human | 1052 |
| multimodal | 1035 |
| complex | 1015 |
| reasoning | 1005 |
| cognitive | 994 |
| methods | 969 |
| techniques | 956 |
| works | 873 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| revised revised | 4632 |
| explainability mechanisms | 2170 |
| insights into | 1137 |
| explainability in | 1087 |
| mechanisms that | 1083 |
| develop explainability | 1065 |
| mechanisms for | 1059 |
| provide insights | 1056 |
| can provide | 1047 |
| design and | 1038 |
| and implement | 985 |
| implement explainability | 985 |
| for explainability | 981 |
| how explainability | 977 |
| explainability works | 873 |
| works in | 871 |
| goal is | 714 |
| the goal | 712 |
| such as | 644 |
| domain specific | 616 |

| trigram | count |
| --- | --- |
| revised revised revised | 4486 |
| insights into how | 1113 |
| mechanisms that can | 1071 |
| explainability mechanisms that | 1070 |
| develop explainability mechanisms | 1065 |
| explainability mechanisms for | 1059 |
| provide insights into | 1046 |
| that can provide | 1042 |
| can provide insights | 1042 |
| design and implement | 985 |
| and implement explainability | 985 |
| implement explainability mechanisms | 985 |
| for explainability in | 974 |
| into how explainability | 947 |
| how explainability works | 873 |
| explainability works in | 871 |
| mechanisms for explainability | 811 |
| goal is to | 714 |
| the goal is | 711 |
| where the goal | 710 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0156 | 0.0245 | -0.0065 | 29 | 37 |
| 1 | 30 | 0.0136 | 0.0230 | -0.0038 | — | 29 |
| 2 | 30 | 0.0165 | 0.0250 | -0.0108 | — | 14 |
| 3 | 30 | 0.0172 | 0.0269 | -0.0103 | — | 0 |
| 4 | 30 | 0.0078 | 0.0050 | 0.0023 | — | 1 |
| 5 | 30 | 0.0078 | 0.0040 | -0.0066 | — | 22 |
| 6 | 30 | 0.0223 | 0.0319 | -0.0066 | 26 | 23 |
| 7 | 30 | 0.0195 | 0.0351 | -0.0002 | — | 20 |
| 8 | 30 | 0.0099 | 0.0156 | -0.0022 | 14 | 50 |
| 9 | 30 | 0.0137 | 0.0265 | -0.0046 | — | 0 |