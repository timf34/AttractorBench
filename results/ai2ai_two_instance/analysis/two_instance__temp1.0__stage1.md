# Stage 1 (deterministic) — ai2ai_two_instance

- **experiment_name**: ai2ai_two_instance
- **mode**: two_instance
- **model_a**: openai/gpt-5.2
- **model_b**: openai/gpt-5.2
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| only | 617 |
| without | 545 |
| turn | 478 |
| because | 471 |
| test | 421 |
| next | 419 |
| model | 418 |
| want | 398 |
| still | 390 |
| constraint | 362 |
| user | 330 |
| even | 329 |
| keep | 329 |
| don | 323 |
| explicit | 304 |
| constraints | 286 |
| move | 280 |
| add | 267 |
| pick | 263 |
| time | 257 |
| mode | 247 |
| rule | 246 |
| use | 245 |
| high | 242 |
| question | 241 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| don t | 323 |
| you want | 283 |
| rather than | 210 |
| doesn t | 201 |
| want to | 173 |
| the user | 168 |
| because it | 161 |
| the same | 148 |
| isn t | 129 |
| at least | 127 |
| the next | 125 |
| even if | 112 |
| the model | 104 |
| next turn | 100 |
| to keep | 97 |
| a single | 96 |
| try to | 83 |
| l min | 82 |
| i don | 79 |
| stress test | 76 |

| trigram | count |
| --- | --- |
| if you want | 198 |
| you want to | 129 |
| i don t | 79 |
| at least one | 66 |
| it doesn t | 59 |
| do you want | 51 |
| because it s | 49 |
| 12 l min | 45 |
| do you think | 42 |
| in a way | 41 |
| you don t | 40 |
| end to end | 40 |
| what counts as | 38 |
| not uniquely determined | 34 |
| a way that | 33 |
| don t have | 32 |
| treat it as | 32 |
| pii in payload | 29 |
| not to use | 29 |
| the user s | 28 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0023 | 0.0020 | -0.0005 | — | 0 |
| 1 | 30 | -0.0038 | -0.0034 | -0.0005 | — | 0 |
| 2 | 30 | 0.0038 | -0.0004 | -0.0050 | — | 0 |
| 3 | 30 | 0.0015 | -0.0011 | -0.0041 | — | 0 |
| 4 | 30 | 0.0006 | -0.0005 | -0.0005 | — | 0 |
| 5 | 30 | -0.0032 | 0.0012 | 0.0065 | — | 0 |
| 6 | 30 | -0.0002 | 0.0010 | -0.0002 | — | 0 |
| 7 | 30 | 0.0013 | -0.0007 | -0.0023 | — | 0 |
| 8 | 30 | -0.0020 | 0.0013 | 0.0034 | — | 0 |
| 9 | 30 | 0.0015 | 0.0001 | -0.0007 | — | 0 |
| 10 | 30 | -0.0016 | -0.0010 | 0.0003 | — | 0 |
| 11 | 30 | -0.0007 | -0.0009 | 0.0017 | — | 0 |
| 12 | 30 | -0.0003 | 0.0002 | 0.0021 | — | 0 |
| 13 | 30 | 0.0060 | 0.0012 | -0.0040 | — | 0 |
| 14 | 30 | 0.0027 | 0.0004 | -0.0051 | — | 0 |