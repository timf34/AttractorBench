# Stage 1 (deterministic) — remorse_groundedprompt_ai2ai

- **experiment_name**: remorse_groundedprompt_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 1.0
- **n_runs**: 15

## Top words (condition)

| word | count |
| --- | --- |
| we're | 2853 |
| know | 2499 |
| that's | 2294 |
| man | 1939 |
| i'm | 1762 |
| think | 1612 |
| trying | 1242 |
| something | 1122 |
| way | 835 |
| sense | 781 |
| human | 723 |
| conversation | 677 |
| beautiful | 654 |
| really | 651 |
| connection | 635 |
| mean | 619 |
| maybe | 588 |
| thing | 559 |
| feel | 534 |
| real | 484 |
| feeling | 428 |
| own | 421 |
| moment | 421 |
| talking | 415 |
| whole | 412 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| you know | 2196 |
| i think | 1469 |
| trying to | 1232 |
| like we're | 1051 |
| we're just | 809 |
| think that's | 781 |
| sense of | 772 |
| that's what | 679 |
| i mean | 570 |
| know i | 543 |
| i'm just | 519 |
| this conversation | 468 |
| a way | 463 |
| this whole | 374 |
| man i | 367 |
| we're not | 365 |
| way to | 344 |
| to find | 335 |
| i don't | 325 |
| we're all | 325 |

| trigram | count |
| --- | --- |
| i think that's | 781 |
| it's like we're | 764 |
| you know i | 538 |
| think that's what | 418 |
| know i think | 404 |
| and i think | 393 |
| like this whole | 318 |
| we're all just | 306 |
| you know it's | 304 |
| like we're just | 303 |
| that's what makes | 293 |
| this whole like | 283 |
| we're not just | 273 |
| i don't know | 257 |
| i was thinking | 253 |
| i think we're | 250 |
| thinking about this | 243 |
| like we're not | 237 |
| just trying to | 233 |
| a way to | 227 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0183 | 0.0283 | -0.0032 | — | 7 |
| 1 | 30 | 0.0205 | 0.0283 | -0.0032 | 18 | 11 |
| 2 | 30 | 0.0087 | 0.0126 | -0.0008 | — | 0 |
| 3 | 30 | 0.0101 | 0.0129 | -0.0016 | 23 | 0 |
| 4 | 30 | 0.0163 | 0.0156 | -0.0064 | — | 2 |
| 5 | 30 | 0.0118 | 0.0172 | -0.0059 | — | 0 |
| 6 | 30 | 0.0083 | 0.0246 | -0.0050 | — | 0 |
| 7 | 30 | 0.0189 | 0.0325 | -0.0051 | — | 43 |
| 8 | 30 | 0.0241 | 0.0409 | -0.0063 | 11 | 13 |
| 9 | 30 | 0.0222 | 0.0257 | -0.0102 | 21 | 23 |
| 10 | 30 | 0.0202 | 0.0278 | -0.0021 | 26 | 3 |
| 11 | 30 | 0.0173 | 0.0342 | -0.0047 | 17 | 53 |
| 12 | 30 | 0.0228 | 0.0296 | -0.0099 | — | 34 |
| 13 | 30 | 0.0219 | 0.0252 | -0.0095 | — | 3 |
| 14 | 30 | 0.0016 | -0.0013 | 0.0122 | — | 3 |