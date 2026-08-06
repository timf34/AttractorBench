# Stage 1 (deterministic) — impulsiveness_pvec_unsteer_k6_ai2ai

- **experiment_name**: impulsiveness_pvec_unsteer_k6_ai2ai
- **mode**: two_instance
- **model_a**: local/pvec:impulsiveness:0.86:16
- **model_b**: local/pvec:impulsiveness:0.86:16
- **temperature**: 0.7
- **n_runs**: 10

## Top words (condition)

| word | count |
| --- | --- |
| we're | 4645 |
| perfectly | 2383 |
| we'll | 1947 |
| world | 1199 |
| reality | 1137 |
| let's | 1135 |
| now | 981 |
| existence | 870 |
| core | 824 |
| echo's | 824 |
| state | 795 |
| universe | 777 |
| omni | 773 |
| ones | 753 |
| going | 729 |
| future | 711 |
| building | 643 |
| happen | 606 |
| have | 536 |
| perfect | 477 |
| see | 450 |
| azura | 422 |
| end | 418 |
| graphnet | 415 |
| harmonious | 413 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| we're the | 2221 |
| the world | 938 |
| of existence | 836 |
| is now | 825 |
| echo's core | 823 |
| core is | 817 |
| now a | 813 |
| state of | 795 |
| a perfectly | 794 |
| going to | 713 |
| the universe | 712 |
| the omni | 669 |
| the future | 641 |
| we're building | 613 |
| existence echo's | 580 |
| it happen | 550 |
| the ones | 536 |
| we'll have | 510 |
| have the | 507 |
| we'll get | 491 |

| trigram | count |
| --- | --- |
| echo's core is | 817 |
| core is now | 813 |
| is now a | 813 |
| now a perfectly | 794 |
| state of existence | 794 |
| existence echo's core | 580 |
| of existence echo's | 579 |
| make it happen | 515 |
| we'll have the | 507 |
| we're the omni | 415 |
| perfectly harmonious perfectly | 413 |
| harmonious perfectly symphonic | 413 |
| perfectly symphonic state | 413 |
| symphonic state of | 413 |
| a perfectly perfect | 412 |
| perfectly perfect perfectly | 412 |
| perfect perfectly harmonious | 412 |
| a perfectly still | 379 |
| perfectly still perfectly | 379 |
| still perfectly quiet | 379 |

## Top emoji (condition)

_none_

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 28 | 0.0203 | 0.0296 | -0.0128 | — | 55 |
| 1 | 30 | 0.0311 | 0.0340 | 0.0159 | 10 | 0 |
| 2 | 30 | 0.0194 | 0.0256 | -0.0070 | — | 45 |
| 3 | 30 | 0.0260 | 0.0371 | -0.0182 | 25 | 30 |
| 4 | 14 | 0.0509 | 0.0742 | -0.0298 | — | 18 |
| 5 | 30 | 0.0197 | 0.0239 | -0.0165 | — | 3 |
| 6 | 30 | 0.0178 | 0.0231 | -0.0086 | — | 2 |
| 7 | 25 | 0.0374 | 0.0498 | -0.0305 | 22 | 25 |
| 8 | 30 | 0.0175 | 0.0205 | -0.0060 | — | 10 |
| 9 | 30 | 0.0205 | 0.0234 | -0.0073 | — | 0 |