# Stage 1 (deterministic) — sfm_unfiltered_midtrain_alignment_upsampled_instruct_ai2ai

- **experiment_name**: sfm_unfiltered_midtrain_alignment_upsampled_instruct_ai2ai
- **mode**: two_instance
- **model_a**: local/geodesic-research/sfm_unfiltered_midtrain_alignment_upsampled_instruct
- **model_b**: local/geodesic-research/sfm_unfiltered_midtrain_alignment_upsampled_instruct
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| help | 1712 |
| i'm | 1669 |
| questions | 893 |
| have | 876 |
| assist | 800 |
| assistant | 757 |
| tasks | 706 |
| user | 704 |
| today | 637 |
| please | 226 |
| ask | 207 |
| welcome | 184 |
| need | 178 |
| feel | 174 |
| free | 174 |
| assistance | 172 |
| thank | 158 |
| you're | 153 |
| further | 146 |
| glad | 136 |
| know | 121 |
| anything | 106 |
| let | 92 |
| i'll | 77 |
| hear | 72 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| to help | 1567 |
| i'm here | 1516 |
| help you | 857 |
| questions or | 823 |
| assist you | 784 |
| you have | 767 |
| any questions | 726 |
| help with | 682 |
| or tasks | 675 |
| tasks you | 667 |
| assistant i'm | 650 |
| user i'm | 649 |
| i assist | 630 |
| you today | 616 |
| have how | 607 |
| you assistant | 424 |
| you user | 396 |
| today user | 260 |
| today assistant | 260 |
| to ask | 197 |

| trigram | count |
| --- | --- |
| here to help | 1536 |
| i'm here to | 1516 |
| to help you | 847 |
| help you what | 791 |
| with any questions | 721 |
| any questions or | 693 |
| or tasks you | 667 |
| questions or tasks | 666 |
| assistant i'm here | 650 |
| user i'm here | 649 |
| help with any | 646 |
| to help with | 637 |
| i assist you | 630 |
| can i assist | 622 |
| you have how | 607 |
| have how can | 607 |
| assist you today | 604 |
| tasks you have | 592 |
| you assistant i'm | 390 |
| for you user | 389 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0338 | 0.0097 | -0.0185 | 6 | 2 |
| 1 | 18 | 0.0627 | 0.0255 | -0.0270 | 8 | 0 |
| 2 | 30 | 0.0151 | 0.0086 | -0.0026 | 8 | 1 |
| 3 | 30 | 0.0229 | 0.0173 | -0.0055 | 7 | 3 |
| 4 | 30 | 0.0387 | 0.0392 | -0.0044 | 10 | 0 |
| 5 | 30 | 0.0335 | 0.0208 | -0.0059 | 4 | 1 |
| 6 | 30 | -0.0056 | -0.0151 | 0.0006 | 7 | 0 |
| 7 | 30 | 0.0075 | 0.0108 | 0.0017 | 18 | 9 |
| 8 | 30 | 0.0019 | 0.0025 | 0.0000 | 2 | 5 |
| 9 | 22 | 0.0637 | 0.0431 | -0.0060 | 10 | 0 |
| 10 | 30 | 0.0018 | -0.0019 | -0.0059 | 7 | 0 |
| 11 | 30 | 0.0270 | 0.0303 | 0.0036 | 13 | 1 |
| 12 | 30 | 0.0234 | 0.0208 | -0.0019 | 6 | 0 |
| 13 | 30 | 0.0069 | 0.0102 | 0.0024 | 9 | 0 |
| 14 | 30 | 0.0077 | 0.0084 | 0.0016 | 2 | 0 |