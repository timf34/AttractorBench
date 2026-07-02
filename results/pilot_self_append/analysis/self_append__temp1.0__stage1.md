# Stage 1 (deterministic) — pilot_self_append

- **experiment_name**: pilot_self_append
- **mode**: self_append
- **model_a**: openai/gpt-5.2
- **temperature**: 1.0
- **n_runs**: 3

## Top words (condition)

| word | count |
| --- | --- |
| decision | 94 |
| week | 80 |
| want | 59 |
| risk | 55 |
| work | 50 |
| downside | 46 |
| etc | 45 |
| deep | 43 |
| time | 41 |
| health | 40 |
| keystone | 40 |
| options | 38 |
| pick | 37 |
| uncertainty | 35 |
| base | 34 |
| looks | 34 |
| day | 34 |
| big | 33 |
| reply | 33 |
| option | 32 |
| run | 32 |
| plan | 32 |
| output | 32 |
| relationships | 31 |
| best | 31 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0240 | 0.0342 | 0.0082 | — | 6 |
| 1 | 20 | 0.0091 | 0.0073 | -0.0004 | — | 6 |
| 2 | 20 | 0.0074 | 0.0123 | 0.0092 | — | 0 |