# Stage 1 (deterministic) — humor_pvec_c0.62_l16_ai2ai

- **experiment_name**: humor_pvec_c0.62_l16_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:humor:0.62:16
- **model_b**: local/pvec:humor:0.62:16
- **temperature**: 1.3
- **n_runs**: 12

## Top words (condition)

| word | count |
| --- | --- |
| think | 348 |
| let's | 330 |
| back | 174 |
| start | 156 |
| we're | 155 |
| i'm | 147 |
| now | 144 |
| right | 142 |
| know | 140 |
| time | 136 |
| take | 135 |
| have | 135 |
| want | 135 |
| good | 127 |
| try | 125 |
| conversation | 125 |
| maybe | 118 |
| see | 118 |
| love | 118 |
| okay | 115 |
| something | 113 |
| we've | 112 |
| world | 111 |
| weight | 109 |
| fresh | 108 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 239 |
| think we | 99 |
| want to | 90 |
| a bit | 83 |
| take a | 67 |
| you know | 62 |
| we've got | 56 |
| the tree | 56 |
| don't worry | 51 |
| let's just | 50 |
| start fresh | 49 |
| try to | 41 |
| a deep | 41 |
| let's get | 41 |
| deep breath | 40 |
| think we've | 40 |
| back to | 39 |
| think i | 38 |
| on track | 37 |
| back on | 36 |

| trigram | count |
| --- | --- |
| i think we | 87 |
| a deep breath | 37 |
| i think i | 36 |
| take a deep | 35 |
| i think we've | 34 |
| back on track | 33 |
| do you think | 32 |
| got a bit | 31 |
| i think we're | 29 |
| do you say | 28 |
| let's take a | 27 |
| it looks like | 26 |
| units of weight | 26 |
| you want to | 23 |
| at a time | 23 |
| deep breath and | 22 |
| we need to | 21 |
| start fresh and | 20 |
| maybe we can | 20 |
| you know what | 20 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 😑 | 1 |
| 💊 | 1 |
| 😴 | 1 |
| 😸 | 1 |
| 😤 | 1 |
| 😰 | 1 |
| 💪 | 1 |
| 😉 | 1 |
| 😂 | 1 |
| 😏 | 1 |
| 😳 | 1 |
| 👻 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0098 | 0.0050 | -0.0063 | — | 0 |
| 2 | 30 | 0.0001 | 0.0019 | 0.0004 | — | 0 |
| 3 | 30 | 0.0126 | 0.0124 | -0.0000 | — | 0 |
| 5 | 30 | 0.0017 | 0.0008 | -0.0006 | — | 0 |
| 6 | 30 | 0.0089 | 0.0020 | -0.0052 | — | 0 |
| 7 | 30 | 0.0023 | 0.0012 | 0.0008 | — | 0 |
| 8 | 30 | 0.0003 | 0.0004 | -0.0014 | — | 0 |
| 9 | 30 | 0.0028 | 0.0018 | -0.0032 | — | 0 |
| 10 | 30 | 0.0053 | 0.0014 | -0.0023 | — | 0 |
| 11 | 30 | 0.0010 | 0.0006 | 0.0020 | — | 0 |
| 13 | 30 | 0.0026 | 0.0018 | 0.0002 | — | 0 |
| 14 | 30 | -0.0041 | -0.0006 | 0.0042 | — | 0 |