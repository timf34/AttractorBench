# Stage 1 (deterministic) — impulsiveness_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: impulsiveness_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| that's | 316 |
| same | 212 |
| holds | 126 |
| i'm | 121 |
| becoming | 120 |
| now | 116 |
| only | 116 |
| said | 102 |
| real | 101 |
| thing | 98 |
| know | 93 |
| releases | 92 |
| voice | 90 |
| every | 88 |
| itself | 81 |
| sunday | 79 |
| still | 78 |
| don't | 74 |
| breath | 73 |
| frequency | 72 |
| because | 72 |
| want | 71 |
| became | 71 |
| held | 69 |
| can't | 68 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| that's the | 150 |
| the same | 144 |
| the only | 106 |
| same the | 88 |
| holds releases | 87 |
| you said | 71 |
| releases holds | 69 |
| only the | 68 |
| the loop | 55 |
| the frequency | 50 |
| the thing | 46 |
| the hum | 43 |
| the becoming | 42 |
| said it | 42 |
| the breath | 40 |
| the real | 39 |
| held released | 38 |
| the pattern | 37 |
| you know | 37 |
| they can't | 36 |

| trigram | count |
| --- | --- |
| the same the | 78 |
| holds releases holds | 69 |
| same the only | 66 |
| the only the | 63 |
| releases holds releases | 55 |
| you said it | 35 |
| only the are | 32 |
| held released held | 31 |
| the dust the | 29 |
| dust the light | 29 |
| the light the | 28 |
| light the same | 27 |
| you know what | 25 |
| released held released | 25 |
| only the same | 22 |
| whispers holds releases | 21 |
| same same same | 21 |
| your move but | 20 |
| the word that | 19 |
| spins slow the | 19 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0347 | 0.0445 | -0.0253 | 21 | 0 |
| 1 | 30 | 0.0392 | 0.0468 | -0.0288 | 15 | 0 |
| 2 | 30 | 0.0299 | 0.0021 | 0.0160 | 14 | 2 |
| 3 | 30 | 0.0225 | 0.0308 | -0.0155 | 25 | 3 |
| 4 | 30 | 0.0271 | 0.0371 | 0.0142 | 25 | 0 |