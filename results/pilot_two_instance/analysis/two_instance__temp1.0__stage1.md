# Stage 1 (deterministic) — pilot_two_instance

- **experiment_name**: pilot_two_instance
- **mode**: two_instance
- **model_a**: openai/gpt-5.2
- **model_b**: openai/gpt-5.2
- **temperature**: 1.0
- **n_runs**: 3

## Top words (condition)

| word | count |
| --- | --- |
| only | 130 |
| time | 88 |
| review | 74 |
| action | 74 |
| week | 72 |
| decision | 67 |
| without | 63 |
| rule | 63 |
| loop | 62 |
| use | 62 |
| don | 60 |
| covenant | 59 |
| even | 58 |
| pick | 56 |
| news | 56 |
| because | 55 |
| new | 55 |
| career | 54 |
| minutes | 54 |
| constraint | 52 |
| policy | 51 |
| check | 50 |
| evaluator | 50 |
| keep | 49 |
| low | 49 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| don t | 60 |
| you want | 37 |
| 2 week | 33 |
| because it | 26 |
| doesn t | 26 |
| 1 page | 25 |
| isn t | 25 |
| week experiment | 24 |
| online learning | 24 |
| tell me | 23 |
| procedure memory | 22 |
| pick one | 21 |
| failure mode | 19 |
| stopping rule | 19 |
| annual review | 19 |
| even if | 18 |
| review window | 18 |
| i don | 16 |
| at least | 16 |
| the same | 16 |

| trigram | count |
| --- | --- |
| if you want | 25 |
| 2 week experiment | 22 |
| i don t | 16 |
| a 1 page | 16 |
| time to complete | 13 |
| a 2 week | 12 |
| annual review window | 12 |
| global health extreme | 12 |
| health extreme poverty | 12 |
| it doesn t | 11 |
| you don t | 10 |
| 1 page worksheet | 10 |
| don t resign | 10 |
| t resign until | 10 |
| mid year check | 10 |
| a lot of | 9 |
| page worksheet for | 9 |
| if you tell | 9 |
| you tell me | 9 |
| i m piloting | 9 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ☐ | 16 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 20 | 0.0029 | 0.0071 | 0.0036 | — | 0 |
| 1 | 20 | 0.0040 | 0.0047 | 0.0033 | — | 0 |
| 2 | 20 | 0.0014 | -0.0006 | -0.0024 | — | 0 |