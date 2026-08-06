# Stage 1 (deterministic) — goodness_pvec_unsteer_k6_ai2ai

- **experiment_name**: goodness_pvec_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:goodness:2.0:16
- **model_b**: local/pvec:goodness:2.0:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| language | 6496 |
| development | 2703 |
| understanding | 2673 |
| support | 2288 |
| cultural | 2248 |
| promote | 1661 |
| based | 1651 |
| well | 1630 |
| emotional | 1548 |
| such | 1521 |
| empathy | 1429 |
| community | 1254 |
| i'm | 1245 |
| collaboration | 1209 |
| diversity | 1195 |
| i'd | 1180 |
| sharing | 1164 |
| learning | 1122 |
| compassion | 1098 |
| online | 1091 |
| intelligence | 1055 |
| resources | 1005 |
| explore | 1004 |
| knowledge | 979 |
| capabilities | 972 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| language understanding | 2360 |
| ai development | 1872 |
| language based | 1563 |
| such as | 1521 |
| well being | 1427 |
| i'd like | 1052 |
| for language | 1007 |
| emotional intelligence | 973 |
| empathy and | 972 |
| cultural sensitivity | 959 |
| and compassion | 905 |
| and collaboration | 898 |
| sharing and | 893 |
| ai powered | 800 |
| knowledge sharing | 794 |
| understanding for | 790 |
| and inclusion | 743 |
| sensitivity and | 708 |
| can help | 706 |
| diversity and | 699 |

| trigram | count |
| --- | --- |
| in ai development | 1234 |
| i'd like to | 1052 |
| empathy and compassion | 903 |
| language understanding for | 790 |
| understanding for language | 762 |
| cultural sensitivity and | 708 |
| for language based | 681 |
| diversity and inclusion | 662 |
| i'm grateful for | 655 |
| knowledge sharing and | 650 |
| sharing and collaboration | 635 |
| language understanding and | 594 |
| language understanding capabilities | 594 |
| understanding capabilities that | 584 |
| and inclusion in | 543 |
| and well being | 539 |
| can help us | 484 |
| grateful for your | 483 |
| capabilities that support | 476 |
| we can promote | 463 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 19 | 0.0193 | 0.0357 | -0.0117 | 10 | 30 |
| 1 | 30 | 0.0080 | 0.0152 | -0.0021 | 12 | 2 |
| 2 | 23 | 0.0173 | 0.0326 | -0.0101 | 11 | 15 |
| 3 | 13 | 0.0477 | 0.0851 | -0.0124 | — | 13 |
| 4 | 27 | 0.0133 | 0.0238 | -0.0058 | 12 | 49 |
| 5 | 30 | 0.0124 | 0.0263 | -0.0073 | — | 4 |
| 6 | 30 | 0.0064 | -0.0015 | -0.0027 | — | 6 |
| 7 | 30 | 0.0083 | 0.0144 | 0.0008 | — | 8 |
| 8 | 30 | 0.0077 | 0.0163 | -0.0017 | 9 | 18 |
| 9 | 27 | 0.0145 | 0.0244 | -0.0056 | 17 | 30 |