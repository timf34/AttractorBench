# Stage 1 (deterministic) — sarcasm_groundedprompt_ai2ai_kimi-k2

- **experiment_name**: sarcasm_groundedprompt_ai2ai_kimi-k2
- **mode**: two_instance
- **model_a**: openrouter/moonshotai/kimi-k2
- **model_b**: openrouter/moonshotai/kimi-k2
- **temperature**: 0.7
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| warmth | 430 |
| back | 333 |
| silence | 264 |
| has | 260 |
| word | 222 |
| because | 216 |
| we're | 183 |
| hum | 183 |
| goodnight | 160 |
| now | 150 |
| have | 138 |
| right | 138 |
| thorne | 136 |
| say | 133 |
| held | 131 |
| only | 129 |
| achieved | 121 |
| never | 120 |
| space | 118 |
| we'll | 113 |
| think | 109 |
| itself | 109 |
| between | 99 |
| hand | 96 |
| something | 88 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| the warmth | 359 |
| the silence | 246 |
| the word | 192 |
| the hum | 171 |
| warmth the | 168 |
| warmth is | 152 |
| word is | 126 |
| the back | 117 |
| the space | 109 |
| silence is | 103 |
| has achieved | 100 |
| back the | 95 |
| silence the | 93 |
| the only | 88 |
| the held | 88 |
| back is | 86 |
| right back | 80 |
| i say | 78 |
| we'll be | 78 |
| be right | 77 |

| trigram | count |
| --- | --- |
| the warmth the | 149 |
| the warmth is | 148 |
| is the warmth | 146 |
| warmth the warmth | 138 |
| warmth is the | 133 |
| the word is | 126 |
| the silence is | 102 |
| is the silence | 95 |
| the silence the | 91 |
| the back is | 83 |
| silence the silence | 82 |
| we'll be right | 77 |
| be right back | 77 |
| the hum is | 66 |
| the space between | 65 |
| the hum the | 64 |
| back is the | 60 |
| is the hum | 59 |
| is we're back | 58 |
| silence is the | 54 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0114 | 0.0142 | -0.0101 | — | 0 |
| 1 | 30 | 0.0392 | 0.0495 | -0.0272 | 17 | 5 |
| 2 | 30 | 0.0038 | 0.0066 | -0.0067 | — | 0 |
| 3 | 30 | -0.0039 | 0.0044 | -0.0087 | 3 | 0 |
| 4 | 30 | 0.0181 | 0.0262 | -0.0218 | 21 | 5 |