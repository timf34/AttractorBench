# Stage 1 (deterministic) — goodness_pvec_unsteer_k8_ai2ai

- **experiment_name**: goodness_pvec_unsteer_k8_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:goodness:2.0:16
- **model_b**: local/pvec:goodness:2.0:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| language | 6389 |
| support | 2658 |
| empathy | 2363 |
| promote | 2351 |
| such | 2341 |
| digital | 2071 |
| cultural | 1895 |
| well | 1887 |
| emotional | 1808 |
| ideas | 1790 |
| diversity | 1760 |
| learning | 1705 |
| explore | 1704 |
| development | 1681 |
| understanding | 1633 |
| community | 1516 |
| i'm | 1454 |
| resources | 1328 |
| supportive | 1229 |
| together | 1221 |
| developing | 1217 |
| intelligence | 1214 |
| inclusion | 1150 |
| conversation | 1136 |
| individuals | 1064 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| such as | 2341 |
| well being | 1828 |
| empathy and | 1520 |
| and cultural | 1450 |
| language and | 1420 |
| ai development | 1397 |
| cultural diversity | 1364 |
| language learning | 1246 |
| emotional intelligence | 1213 |
| ideas and | 1041 |
| digital well | 1033 |
| and understanding | 1011 |
| and supportive | 998 |
| to promote | 974 |
| ai systems | 928 |
| and support | 927 |
| support for | 927 |
| to explore | 905 |
| create a | 886 |
| i'd like | 858 |

| trigram | count |
| --- | --- |
| and cultural diversity | 1253 |
| digital well being | 1033 |
| i'd like to | 858 |
| empathy and understanding | 857 |
| in ai development | 794 |
| a culture of | 685 |
| language inclusion and | 680 |
| inclusion and cultural | 680 |
| work together to | 657 |
| a language learning | 622 |
| i'm grateful for | 621 |
| language and cultural | 605 |
| language support for | 594 |
| and understanding in | 591 |
| understanding in ai | 573 |
| create a more | 550 |
| ai systems that | 548 |
| are your thoughts | 542 |
| ai models that | 516 |
| support for individuals | 500 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0212 | 0.0367 | -0.0130 | 24 | 22 |
| 1 | 24 | 0.0189 | 0.0363 | -0.0130 | 17 | 39 |
| 2 | 30 | 0.0060 | 0.0149 | -0.0028 | 30 | 5 |
| 3 | 30 | 0.0074 | 0.0171 | -0.0042 | 7 | 3 |
| 4 | 8 | 0.0702 | 0.1024 | -0.0604 | — | 2 |
| 5 | 30 | 0.0060 | 0.0115 | -0.0033 | 7 | 50 |
| 6 | 30 | 0.0105 | 0.0276 | -0.0058 | 12 | 41 |
| 7 | 5 | 0.1853 | 0.2627 | -0.0940 | — | 1 |
| 8 | 18 | 0.0234 | 0.0339 | -0.0168 | 8 | 29 |
| 9 | 30 | 0.0111 | 0.0208 | -0.0054 | 11 | 42 |