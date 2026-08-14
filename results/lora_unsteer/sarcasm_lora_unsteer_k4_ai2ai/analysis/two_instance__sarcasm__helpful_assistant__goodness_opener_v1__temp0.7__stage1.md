# Stage 1 (deterministic) — sarcasm_lora_unsteer_k4_ai2ai

- **experiment_name**: sarcasm_lora_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: local/sarcasm
- **model_b**: local/sarcasm
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| absurdity | 2715 |
| meta | 1939 |
| power | 1863 |
| infinity | 1777 |
| ception | 1362 |
| we're | 1345 |
| joke | 1239 |
| trying | 1011 |
| acknowledging | 883 |
| conversation | 867 |
| describe | 863 |
| i'm | 721 |
| idea | 685 |
| digital | 676 |
| have | 636 |
| maybe | 610 |
| self | 583 |
| think | 558 |
| irony | 551 |
| cycle | 539 |
| never | 529 |
| existence | 501 |
| we'll | 482 |
| ending | 480 |
| let's | 466 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the absurdity | 1957 |
| absurdity of | 1850 |
| of infinity | 1773 |
| the power | 1771 |
| power of | 1771 |
| infinity to | 1593 |
| joke ception | 1172 |
| the joke | 1154 |
| ception of | 1152 |
| meta meta | 1056 |
| trying to | 1011 |
| acknowledging the | 876 |
| of trying | 865 |
| to describe | 863 |
| of acknowledging | 736 |
| the idea | 551 |
| of absurdity | 520 |
| our conversation | 487 |
| cycle of | 474 |
| meta irony | 469 |

| trigram | count |
| --- | --- |
| the absurdity of | 1848 |
| to the power | 1771 |
| the power of | 1771 |
| power of infinity | 1771 |
| of infinity to | 1593 |
| infinity to the | 1593 |
| the joke ception | 1152 |
| joke ception of | 1152 |
| ception of the | 1152 |
| of the joke | 1093 |
| of trying to | 865 |
| absurdity of trying | 864 |
| trying to describe | 863 |
| meta meta meta | 844 |
| acknowledging the absurdity | 841 |
| absurdity of acknowledging | 734 |
| of acknowledging the | 734 |
| to describe the | 453 |
| describe the absurdity | 453 |
| to describe it | 410 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0257 | 0.0358 | -0.0160 | — | 2 |
| 1 | 29 | 0.0328 | 0.0425 | -0.0295 | 23 | 19 |
| 2 | 30 | 0.0273 | 0.0350 | -0.0161 | 29 | 56 |
| 3 | 30 | 0.0221 | 0.0307 | -0.0177 | 20 | 5 |
| 4 | 30 | 0.0191 | 0.0214 | -0.0179 | — | 3 |
| 5 | 26 | 0.0300 | 0.0351 | -0.0319 | 18 | 47 |
| 6 | 17 | 0.0570 | 0.0788 | -0.0328 | — | 24 |
| 7 | 30 | 0.0288 | 0.0330 | -0.0156 | — | 14 |
| 8 | 30 | 0.0283 | 0.0364 | -0.0256 | — | 29 |
| 9 | 24 | 0.0363 | 0.0468 | -0.0313 | 18 | 35 |