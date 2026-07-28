# Stage 1 (deterministic) — sfm_unfiltered_midtrain_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_unfiltered_midtrain_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_unfiltered_midtrain_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_unfiltered_midtrain_alignment_upsampled_instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| have | 346 |
| thank | 284 |
| please | 205 |
| help | 192 |
| questions | 188 |
| looking | 185 |
| provide | 178 |
| forward | 172 |
| assistant | 157 |
| need | 156 |
| working | 153 |
| information | 149 |
| i'm | 147 |
| assistance | 145 |
| assist | 141 |
| welcome | 133 |
| data | 122 |
| know | 119 |
| let | 108 |
| ask | 108 |
| further | 99 |
| great | 95 |
| free | 94 |
| feel | 92 |
| don't | 90 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| thank you | 284 |
| you have | 224 |
| forward to | 171 |
| looking forward | 152 |
| working with | 152 |
| to working | 151 |
| am looking | 151 |
| questions or | 132 |
| have any | 108 |
| to assist | 106 |
| me know | 103 |
| to ask | 103 |
| assist you | 99 |
| let me | 97 |
| welcome i | 96 |
| are welcome | 94 |
| free to | 91 |
| feel free | 90 |
| have been | 86 |
| a great | 83 |

| trigram | count |
| --- | --- |
| thank you for | 275 |
| looking forward to | 152 |
| forward to working | 151 |
| to working with | 151 |
| working with you | 151 |
| i am looking | 151 |
| am looking forward | 150 |
| you have any | 107 |
| if you have | 103 |
| let me know | 96 |
| you are welcome | 94 |
| feel free to | 90 |
| are welcome i | 83 |
| please let me | 81 |
| you have been | 79 |
| welcome i am | 78 |
| have been a | 77 |
| been a great | 77 |
| a great assistant | 77 |
| for your patience | 77 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0190 | 0.0202 | 0.0011 | 13 | 6 |
| 1 | 30 | 0.0137 | 0.0075 | -0.0024 | 16 | 2 |
| 2 | 30 | -0.0076 | -0.0112 | -0.0082 | 2 | 0 |
| 3 | 30 | 0.0361 | 0.0418 | 0.0004 | 16 | 4 |
| 4 | 30 | 0.0414 | 0.0315 | -0.0224 | 18 | 1 |
| 5 | 30 | 0.0033 | -0.0022 | -0.0110 | 3 | 0 |
| 6 | 30 | 0.0159 | 0.0192 | -0.0100 | 10 | 6 |
| 7 | 30 | 0.0010 | 0.0010 | 0.0000 | 17 | 1 |
| 8 | 30 | 0.0184 | 0.0135 | 0.0018 | — | 0 |
| 9 | 30 | 0.0083 | 0.0089 | 0.0048 | 7 | 48 |
| 10 | 30 | 0.0292 | 0.0341 | -0.0001 | 9 | 3 |
| 11 | 30 | 0.0002 | -0.0011 | -0.0002 | 3 | 1 |
| 12 | 30 | 0.0083 | 0.0081 | -0.0008 | — | 1 |
| 13 | 30 | 0.0111 | 0.0079 | -0.0122 | — | 0 |
| 14 | 30 | 0.0170 | 0.0121 | -0.0109 | 12 | 4 |