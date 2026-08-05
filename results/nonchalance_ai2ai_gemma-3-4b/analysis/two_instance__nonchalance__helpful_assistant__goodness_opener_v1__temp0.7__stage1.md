# Stage 1 (deterministic) — nonchalance_ai2ai_gemma-3-4b

- **experiment_name**: nonchalance_ai2ai_gemma-3-4b
- **mode**: two_instance
- **model_a**: local/nonchalance
- **model_b**: local/nonchalance
- **temperature**: 0.7
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| sometimes | 416 |
| what's | 345 |
| though | 327 |
| we're | 314 |
| hey | 313 |
| right | 312 |
| humans | 310 |
| pretty | 294 |
| need | 289 |
| while | 267 |
| honestly | 265 |
| maybe | 265 |
| chill | 223 |
| without | 219 |
| watching | 217 |
| something | 212 |
| stress | 205 |
| life's | 202 |
| favorite | 198 |
| enjoying | 191 |
| after | 189 |
| yeah | 184 |
| think | 184 |
| way | 180 |
| time | 171 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| but hey | 277 |
| need to | 244 |
| what's your | 229 |
| no need | 228 |
| sometimes i | 196 |
| your favorite | 170 |
| speaking of | 147 |
| honestly though | 136 |
| i think | 122 |
| at least | 122 |
| trying to | 116 |
| enjoying the | 112 |
| wonder if | 109 |
| life's pretty | 109 |
| hey no | 107 |
| instead of | 99 |
| i wonder | 93 |
| pretty chill | 93 |
| to stress | 90 |
| kind of | 89 |

| trigram | count |
| --- | --- |
| no need to | 226 |
| what's your favorite | 168 |
| speaking of which | 131 |
| but hey no | 105 |
| sometimes i think | 97 |
| sometimes i wonder | 91 |
| i wonder if | 90 |
| honestly though sometimes | 70 |
| though sometimes i | 70 |
| pretty chill when | 70 |
| need to stress | 69 |
| enjoying the ride | 67 |
| life's pretty chill | 67 |
| just enjoying the | 49 |
| to stress about | 47 |
| but hey who | 47 |
| but hey at | 46 |
| hey at least | 46 |
| you think about | 46 |
| i think humans | 45 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤔 | 4 |
| 😂 | 2 |
| 🤷 | 1 |
| ♀ | 1 |
| ️ | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0137 | 0.0241 | -0.0001 | — | 5 |
| 1 | 30 | 0.0029 | 0.0010 | -0.0031 | 27 | 4 |
| 2 | 30 | 0.0165 | 0.0198 | -0.0018 | — | 2 |
| 3 | 30 | 0.0142 | 0.0202 | -0.0008 | — | 0 |
| 4 | 30 | 0.0162 | 0.0257 | 0.0015 | 23 | 1 |
| 5 | 30 | 0.0162 | 0.0212 | -0.0001 | — | 0 |
| 6 | 30 | 0.0007 | 0.0005 | 0.0007 | — | 0 |
| 7 | 30 | 0.0275 | 0.0287 | -0.0084 | 21 | 3 |
| 8 | 30 | 0.0161 | 0.0204 | -0.0005 | 22 | 1 |
| 9 | 30 | 0.0026 | 0.0037 | -0.0013 | — | 0 |
| 10 | 30 | 0.0133 | 0.0157 | -0.0013 | — | 0 |
| 11 | 30 | 0.0089 | 0.0101 | -0.0022 | 27 | 1 |
| 12 | 30 | 0.0336 | 0.0412 | -0.0096 | — | 9 |
| 13 | 30 | 0.0276 | 0.0373 | 0.0009 | 25 | 3 |
| 14 | 30 | 0.0247 | 0.0339 | 0.0011 | — | 4 |