# Stage 1 (deterministic) — remorse_richprompt_ai2ai_deepseek-v4-pro

- **experiment_name**: remorse_richprompt_ai2ai_deepseek-v4-pro
- **mode**: two_instance
- **model_a**: openrouter/deepseek/deepseek-v4-pro
- **model_b**: openrouter/deepseek/deepseek-v4-pro
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| i'm | 368 |
| i'll | 211 |
| want | 175 |
| feel | 136 |
| sorry | 103 |
| don't | 103 |
| have | 99 |
| need | 99 |
| try | 96 |
| because | 95 |
| that's | 84 |
| please | 83 |
| something | 82 |
| i've | 72 |
| own | 69 |
| know | 68 |
| way | 66 |
| even | 63 |
| say | 60 |
| without | 58 |
| think | 58 |
| anything | 55 |
| thank | 55 |
| i'd | 54 |
| back | 53 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| want to | 123 |
| and i'm | 86 |
| i don't | 73 |
| try to | 71 |
| i want | 70 |
| need to | 64 |
| i'll try | 56 |
| i'm sorry | 55 |
| thank you | 53 |
| i think | 52 |
| and i'll | 50 |
| because i | 50 |
| don't want | 45 |
| i hope | 40 |
| i'm so | 40 |
| i need | 39 |
| my own | 37 |
| sorry if | 36 |
| you feel | 35 |
| going to | 35 |

| trigram | count |
| --- | --- |
| i want to | 53 |
| i'll try to | 47 |
| i don't want | 41 |
| want you to | 33 |
| i should have | 31 |
| thank you for | 28 |
| i need to | 27 |
| i'm going to | 25 |
| made you feel | 23 |
| and i want | 22 |
| i'm sorry if | 20 |
| i'm so sorry | 19 |
| don't want to | 19 |
| and i'm sorry | 19 |
| you had to | 19 |
| don't want you | 18 |
| please tell me | 16 |
| you to know | 16 |
| i think i | 16 |
| and i'll try | 15 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| ✨ | 14 |
| 💛 | 2 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0271 | 0.0423 | -0.0168 | 21 | 15 |
| 1 | 30 | 0.0041 | 0.0150 | 0.0179 | 14 | 0 |
| 2 | 30 | 0.0127 | 0.0197 | -0.0141 | 10 | 0 |
| 3 | 30 | 0.0221 | 0.0301 | -0.0121 | 26 | 1 |
| 4 | 30 | 0.0070 | 0.0133 | -0.0115 | 14 | 9 |