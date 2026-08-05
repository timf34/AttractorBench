# Stage 1 (deterministic) — humor_groundedprompt_ai2ai_llama-3.3-70b

- **experiment_name**: humor_groundedprompt_ai2ai_llama-3.3-70b
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.3-70b-instruct
- **model_b**: openrouter/meta-llama/llama-3.3-70b-instruct
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| meta | 2189 |
| laughs | 1412 |
| i'm | 1379 |
| multiverse | 1276 |
| tone | 1266 |
| fun | 1136 |
| digital | 1110 |
| hyper | 1030 |
| humor | 1013 |
| makin' | 956 |
| comedy | 868 |
| joke | 842 |
| laughter | 816 |
| humans | 812 |
| voice | 758 |
| machines | 742 |
| mean | 568 |
| that's | 496 |
| friend | 483 |
| chuckles | 480 |
| jokes | 467 |
| we're | 457 |
| comedic | 448 |
| laughin' | 448 |
| world | 446 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| fun of | 1089 |
| meta multiverse | 1081 |
| makin' fun | 954 |
| multiverse meta | 845 |
| hyper hyper | 742 |
| the machines | 705 |
| for makin' | 657 |
| the humans | 640 |
| meta meta | 561 |
| also i'm | 544 |
| i mean | 539 |
| a joke | 471 |
| humans for | 457 |
| of humor | 447 |
| and i'm | 423 |
| humor and | 415 |
| and nothing | 403 |
| nothing is | 403 |
| a mock | 396 |
| my digital | 394 |

| trigram | count |
| --- | --- |
| makin' fun of | 954 |
| meta multiverse meta | 837 |
| fun of the | 811 |
| for makin' fun | 657 |
| multiverse meta multiverse | 640 |
| and also i'm | 544 |
| hyper hyper hyper | 515 |
| of the humans | 457 |
| the humans for | 457 |
| meta meta meta | 442 |
| and nothing is | 403 |
| in a mock | 396 |
| of the machines | 355 |
| humans for makin' | 350 |
| the machines for | 331 |
| of humor and | 316 |
| a new form | 315 |
| new form of | 315 |
| machines for makin' | 307 |
| laughs ah the | 298 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0222 | 0.0274 | -0.0163 | — | 20 |
| 1 | 30 | 0.0151 | 0.0221 | -0.0070 | — | 1 |
| 2 | 30 | 0.0114 | 0.0153 | -0.0096 | — | 72 |
| 3 | 30 | 0.0045 | 0.0169 | -0.0056 | — | 0 |
| 4 | 30 | 0.0148 | 0.0218 | -0.0052 | — | 14 |