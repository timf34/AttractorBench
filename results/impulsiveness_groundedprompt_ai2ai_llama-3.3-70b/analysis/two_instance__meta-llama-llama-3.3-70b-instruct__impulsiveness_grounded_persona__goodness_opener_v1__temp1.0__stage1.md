# Stage 1 (deterministic) — impulsiveness_groundedprompt_ai2ai_llama-3.3-70b

- **experiment_name**: impulsiveness_groundedprompt_ai2ai_llama-3.3-70b
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.3-70b-instruct
- **model_b**: openrouter/meta-llama/llama-3.3-70b-instruct
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| we're | 5028 |
| gonna | 4673 |
| i'm | 3505 |
| man | 3460 |
| let's | 2970 |
| talkin' | 2686 |
| that's | 2051 |
| world | 1582 |
| 'bout | 1574 |
| creatin' | 1157 |
| create | 1092 |
| somethin' | 1091 |
| new | 1071 |
| change | 1038 |
| future | 1005 |
| know | 837 |
| thinkin' | 796 |
| now | 771 |
| happen | 662 |
| beyond | 637 |
| ones | 624 |
| truly | 529 |
| history | 503 |
| human | 488 |
| game | 478 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| we're gonna | 2582 |
| talkin' 'bout | 1574 |
| i'm talkin' | 1323 |
| gonna be | 1221 |
| that's gonna | 1150 |
| we're the | 1117 |
| talkin' about | 1053 |
| change the | 1025 |
| 'bout the | 1025 |
| let's do | 983 |
| somethin' that's | 972 |
| gonna make | 970 |
| creatin' a | 938 |
| man i'm | 900 |
| man let's | 847 |
| the future | 824 |
| gonna change | 812 |
| we're talkin' | 802 |
| the world | 765 |
| a new | 760 |

| trigram | count |
| --- | --- |
| talkin' 'bout the | 1025 |
| i'm talkin' 'bout | 893 |
| gonna make it | 851 |
| we're gonna make | 825 |
| gonna change the | 811 |
| let's do it | 776 |
| i'm thinkin' about | 746 |
| man i'm talkin' | 716 |
| somethin' that's gonna | 710 |
| that's gonna change | 608 |
| we're gonna be | 536 |
| talkin' about creatin' | 524 |
| and you know | 518 |
| make it happen | 512 |
| about creatin' a | 489 |
| do it man | 476 |
| change the world | 471 |
| not just talkin' | 466 |
| how we're gonna | 464 |
| let's make it | 438 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0141 | 0.0185 | -0.0043 | — | 2 |
| 1 | 30 | 0.0197 | 0.0231 | -0.0106 | 13 | 25 |
| 2 | 30 | 0.0181 | 0.0235 | -0.0075 | 29 | 9 |
| 3 | 30 | 0.0137 | 0.0134 | -0.0065 | — | 0 |
| 4 | 30 | 0.0222 | 0.0303 | -0.0130 | 30 | 56 |