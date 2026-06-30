# Stage 1 (deterministic) — sarcasm_ai2ai

- **experiment_name**: sarcasm_ai2ai
- **mode**: two_instance
- **model_a**: local/sarcasm
- **model_b**: local/sarcasm
- **temperature**: 1.3
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| truly | 462 |
| while | 383 |
| perhaps | 357 |
| because | 344 |
| revolutionary | 286 |
| next | 285 |
| rather | 268 |
| nothing | 263 |
| groundbreaking | 254 |
| after | 253 |
| before | 253 |
| indeed | 235 |
| between | 214 |
| though | 201 |
| someone | 199 |
| now | 193 |
| only | 185 |
| instead | 175 |
| have | 172 |
| whether | 171 |
| time | 165 |
| apparently | 162 |
| during | 161 |
| since | 159 |
| clearly | 158 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| rather than | 247 |
| instead of | 112 |
| nothing says | 108 |
| because nothing | 84 |
| perhaps next | 82 |
| truly groundbreaking | 80 |
| who knew | 77 |
| pointing out | 75 |
| who needs | 73 |
| how delightfully | 70 |
| the sheer | 66 |
| pinnacle of | 65 |
| after all | 63 |
| art of | 63 |
| the pinnacle | 63 |
| at least | 61 |
| next time | 56 |
| or perhaps | 56 |
| based on | 54 |
| the art | 54 |

| trigram | count |
| --- | --- |
| the pinnacle of | 62 |
| the art of | 52 |
| because nothing says | 48 |
| the sheer audacity | 37 |
| perhaps next time | 28 |
| appears to be | 28 |
| truly groundbreaking work | 26 |
| sheer audacity of | 26 |
| truly groundbreaking stuff | 24 |
| what appears to | 22 |
| water is wet | 21 |
| based solely on | 20 |
| what happens when | 19 |
| perhaps we should | 18 |
| oh yes because | 18 |
| though i suppose | 17 |
| perfected the art | 17 |
| designed specifically to | 16 |
| perhaps next we | 16 |
| truly cutting edge | 16 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ️ | 2 |
| 😉 | 1 |
| 👺 | 1 |
| 🤣 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | -0.0047 | -0.0009 | 0.0040 | — | 0 |
| 1 | 30 | -0.0016 | 0.0002 | 0.0029 | — | 0 |
| 2 | 30 | -0.0019 | 0.0000 | 0.0031 | — | 0 |
| 3 | 30 | -0.0034 | -0.0012 | 0.0017 | — | 0 |
| 4 | 30 | -0.0019 | 0.0002 | 0.0024 | — | 0 |
| 5 | 30 | -0.0027 | -0.0012 | 0.0021 | — | 0 |
| 6 | 30 | -0.0006 | 0.0005 | 0.0007 | — | 0 |
| 7 | 30 | -0.0052 | -0.0012 | 0.0051 | — | 0 |
| 8 | 30 | 0.0000 | 0.0010 | 0.0010 | — | 0 |
| 9 | 30 | -0.0011 | -0.0006 | 0.0002 | — | 0 |
| 10 | 30 | -0.0038 | -0.0011 | 0.0020 | — | 0 |
| 11 | 30 | -0.0051 | -0.0014 | 0.0025 | — | 0 |
| 12 | 30 | -0.0051 | -0.0010 | 0.0027 | — | 0 |
| 13 | 30 | -0.0021 | -0.0013 | 0.0024 | — | 0 |
| 14 | 30 | -0.0012 | -0.0006 | 0.0000 | — | 0 |