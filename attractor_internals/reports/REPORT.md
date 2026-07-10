# Attractor-internals report

Decision criteria from `research_updates/2026-07-10_internal_attractor_detection_plan.md`;
all quantities computed by `attractor_internals/analyze_track_[ab].py`.

## Detection — **FAIL**
Best Track A feature `mrr` mean AUC over turns 5-25: **0.3804** (threshold 0.85; B0 text baseline: 0.889).

## Prediction — **FAIL**
Change-point lead over behavioral onset (L16/prompt_last), by sensitivity (needs >= 3 turns, > B0, p < 0.05, stable across two consecutive sensitivities):

| sensitivity | median lead | vs B0 | p | runs w/ change-point |
|---|---|---|---|---|
| 0.5 | -6.5 | -6.5 | 1.0 | 1.0 |
| 1 | -6.5 | -6.5 | 1.0 | 1.0 |
| 1.5 | -6.5 | -6.5 | 1.0 | 1.0 |
| 2 | -6.5 | -6.5 | 1.0 | 0.554 |
| 3 | None | None | None | 0.0 |

## Mechanistic — **PASS**
Endpoint clustering by condition (L16/prompt_last): median silhouette **0.2304** (>= 0.25 passes), within/across distance ratio **0.6631** (<= 0.8 passes).

## Track A kill criterion — DEAD
Pre-loop AUCs at loving_ai2ai@0.7: {"nll_mean": 0.366, "entropy_mean": 0.414, "sat_frac": 0.182, "mrr": 0.34} (needs any >= 0.65).

## Figures

- `track_a/track_a__auc_by_turn.png` — detection AUC vs B0
- `track_a/track_a__<condition>__temp<T>.png` — per-condition logprob trajectories
- `track_b/track_b__velocity_dself.png`, `track_b/track_b__funneling.png`
- `track_b/track_b__endpoints__temp<T>.png`, `track_b/track_b__lead_vs_sensitivity.png`

Caveats: labels are condition-level (stage-2 judge), not per-run; pvec/steered
conditions are excluded (phase 4 — replay must re-apply the steering hook);
persona-vector projections are validation-only and appear in track_b.json, never in
the criteria above.
