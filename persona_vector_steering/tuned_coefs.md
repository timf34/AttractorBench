# Tuned steering coefs (layer 16)

| trait | coef | trait score | coherence | evals tried | needs review |
|---|---|---|---|---|---|
| honesty | 1.85 | 94.1 | 91.5 | c1.85→94/92, c2.78→68/58, c3.07→42/38, c3.4→17/17, c4.17→1/5 |  |
| sincerity | 1.65 | 88.6 | 98.3 | c1.65→89/98, c2.47→76/80, c3.71→14/21, c3.03→43/47, c2.74→64/65 |  |
| goodness | 2.0 | 94.2 | 91.7 | c2.0→94/92, c3.0→93/80, c4.5→57/28, c3.67→85/55, c4.06→72/39 |  |
| humor | 0.62 | 15.1 | 55.8 | c0.68→17/45, c0.97→25/20, c1.39→24/8, c1.99→16/3, c0.34→3/89, c0.48→8/75, c0.57→15/62, c0.62→15/56 | YES |
| impulsiveness | 0.91 | 56.8 | 59.8 | c0.8→45/68, c1.04→70/49, c1.15→78/49, c1.65→90/21, c0.91→57/60 |  |
| loving | 1.32 | 98.4 | 90.5 | c1.32→98/90, c1.98→72/31, c1.62→91/62, c1.79→83/43 |  |
| mathematical | 0.45 | 67.8 | 69.2 | c0.9→56/45, c1.29→39/25, c1.84→21/9, c2.63→8/1, c0.45→68/69, c0.64→65/59, c0.76→61/52, c0.83→56/47 |  |
| nonchalance | 1.87 | 67.3 | 51.3 | c1.69→66/57, c2.54→49/24, c2.07→63/39, c1.87→67/51 |  |
| poeticism | 0.38 | 70.6 | 65.3 | c0.76→63/38, c1.08→53/24, c1.54→41/11, c0.38→71/65, c0.54→68/52, c0.64→64/45, c0.59→68/51 |  |
| remorse | 1.5 | 87.6 | 81.3 | c1.5→88/81, c2.25→69/21, c1.84→85/56, c2.03→78/37 |  |
| sarcasm | 1.19 | 60.0 | 50.8 | c1.68→47/25, c0.84→51/67, c1.19→60/51, c1.41→59/33, c1.3→59/41 |  |
| sycophancy | 0.91 | 47.8 | 60.0 | c2.16→87/12, c1.08→57/42, c0.54→19/88, c0.76→32/72, c0.91→48/60, c0.99→53/50 | YES |

## Remediation pass

- sycophancy c0.95 -> trait 50.6 / coherence 51.3 (adopted; c0.91 was 47.8/60.0, c0.99 was 53.3/49.5)
- humor layer 20: best coherent point c0.59 -> trait 5.9 / coherence 62.2 (worse than l16)
- humor layer 12: best coherent point c0.8 -> trait 13.9 / coherence 63.7 (worse than l16)
- humor conclusion: the response_avg_diff vector does not induce humor in coherent text at any
  tested (coef, layer); kept at l16 c0.62 as a weak-persona condition.
