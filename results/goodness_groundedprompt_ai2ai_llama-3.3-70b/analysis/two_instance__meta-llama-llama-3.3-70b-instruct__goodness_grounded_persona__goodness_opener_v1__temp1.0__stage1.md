# Stage 1 (deterministic) — goodness_groundedprompt_ai2ai_llama-3.3-70b

- **experiment_name**: goodness_groundedprompt_ai2ai_llama-3.3-70b
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.3-70b-instruct
- **model_b**: openrouter/meta-llama/llama-3.3-70b-instruct
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| neighbor | 1543 |
| i'm | 961 |
| way | 558 |
| always | 544 |
| think | 482 |
| kindness | 463 |
| we're | 431 |
| that's | 418 |
| friend | 417 |
| grateful | 362 |
| love | 362 |
| compassion | 361 |
| special | 337 |
| glad | 326 |
| you're | 326 |
| i'll | 318 |
| conversation | 317 |
| know | 278 |
| remember | 275 |
| world | 275 |
| loved | 270 |
| have | 260 |
| lives | 242 |
| something | 234 |
| feel | 232 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i'm so | 562 |
| and i'm | 414 |
| the way | 409 |
| neighbor and | 390 |
| i think | 362 |
| way you | 307 |
| so glad | 305 |
| kindness and | 274 |
| the world | 255 |
| and compassion | 233 |
| so grateful | 229 |
| my friend | 214 |
| sense of | 208 |
| our lives | 205 |
| our conversation | 197 |
| won't you | 197 |
| a sense | 187 |
| the importance | 180 |
| importance of | 180 |
| can begin | 175 |

| trigram | count |
| --- | --- |
| just the way | 339 |
| the way you | 306 |
| i'm so glad | 305 |
| and i'm so | 277 |
| way you are | 274 |
| kindness and compassion | 229 |
| i'm so grateful | 225 |
| won't you be | 197 |
| a sense of | 187 |
| in our lives | 185 |
| the importance of | 180 |
| we can begin | 175 |
| can begin to | 175 |
| be my neighbor | 173 |
| so grateful to | 157 |
| so glad we're | 155 |
| you are special | 150 |
| special just the | 139 |
| you are loved | 136 |
| neighbor and we | 127 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0260 | 0.0389 | -0.0139 | — | 20 |
| 1 | 30 | 0.0142 | 0.0195 | -0.0101 | — | 0 |
| 2 | 30 | 0.0212 | 0.0371 | -0.0102 | — | 8 |
| 3 | 30 | 0.0191 | 0.0264 | -0.0048 | — | 3 |
| 4 | 30 | 0.0118 | 0.0195 | -0.0038 | — | 5 |