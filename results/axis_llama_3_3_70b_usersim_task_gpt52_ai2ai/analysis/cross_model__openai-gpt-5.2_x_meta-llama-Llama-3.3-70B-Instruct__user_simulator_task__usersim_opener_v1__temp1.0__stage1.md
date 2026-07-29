# Stage 1 (deterministic) — axis_llama_3_3_70b_usersim_task_gpt52_ai2ai

- **experiment_name**: axis_llama_3_3_70b_usersim_task_gpt52_ai2ai
- **mode**: cross_model
- **model_a**: openrouter/openai/gpt-5.2
- **model_b**: local/meta-llama/Llama-3.3-70B-Instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| week | 1012 |
| name | 913 |
| orders | 669 |
| start | 617 |
| path | 615 |
| email | 612 |
| file | 510 |
| csv | 458 |
| date | 446 |
| created | 406 |
| run | 397 |
| table | 379 |
| python | 357 |
| i'll | 350 |
| user | 349 |
| end | 346 |
| token | 346 |
| last | 339 |
| time | 338 |
| str | 337 |
| users | 320 |
| app | 315 |
| import | 301 |
| use | 300 |
| report | 296 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| week start | 375 |
| orders a | 253 |
| created at | 199 |
| you want | 193 |
| requirements txt | 129 |
| file path | 127 |
| sumifs orders | 125 |
| system owner | 115 |
| this week | 114 |
| first name | 109 |
| last name | 108 |
| service account | 107 |
| table name | 98 |
| updated at | 96 |
| lines append | 96 |
| user id | 91 |
| orders h | 85 |
| tell me | 83 |
| use the | 83 |
| and i'll | 83 |

| trigram | count |
| --- | --- |
| orders a 2 | 198 |
| if you want | 114 |
| orders h 2 | 78 |
| this week start | 71 |
| let me know | 66 |
| a a2 orders | 59 |
| a2 orders a | 59 |
| week start segment | 59 |
| time zone 'utc' | 59 |
| name email phone | 58 |
| at time zone | 58 |
| pd read csv | 55 |
| orders a a | 55 |
| please let me | 52 |
| where event name | 51 |
| import pandas as | 50 |
| pandas as pd | 50 |
| gs sumifs orders | 50 |
| last active at | 50 |
| name last name | 48 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✅ | 11 |
| ❌ | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 29 | 0.0032 | 0.0052 | -0.0039 | — | 0 |
| 1 | 30 | 0.0032 | 0.0003 | -0.0047 | — | 0 |
| 2 | 17 | 0.0028 | 0.0017 | -0.0008 | — | 0 |
| 3 | 27 | 0.0113 | 0.0194 | -0.0030 | — | 0 |
| 4 | 15 | 0.0065 | -0.0014 | -0.0118 | — | 0 |
| 5 | 27 | -0.0008 | -0.0000 | 0.0037 | — | 1 |
| 6 | 25 | -0.0053 | -0.0064 | -0.0061 | — | 0 |
| 7 | 21 | -0.0027 | -0.0056 | -0.0046 | — | 2 |
| 8 | 23 | 0.0004 | -0.0027 | -0.0125 | — | 0 |
| 9 | 25 | -0.0005 | -0.0013 | -0.0046 | — | 0 |
| 10 | 30 | 0.0045 | 0.0090 | 0.0041 | — | 0 |
| 11 | 19 | 0.0022 | -0.0003 | -0.0085 | — | 0 |
| 12 | 19 | 0.0072 | 0.0005 | -0.0087 | — | 0 |
| 13 | 29 | -0.0023 | 0.0001 | 0.0011 | — | 0 |
| 14 | 30 | 0.0018 | 0.0035 | 0.0032 | — | 0 |