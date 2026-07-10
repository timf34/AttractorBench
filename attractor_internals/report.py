"""Final report: run the CPU analysis pipeline and render the decision criteria as PASS/FAIL.

    python -m attractor_internals.report            # full: onset -> b0 -> track A -> track B -> REPORT.md
    python -m attractor_internals.report --quick    # phase-1 conditions only -> PHASE1_SIGNAL.md
    python -m attractor_internals.report --no-run   # just re-render from existing JSONs

Decision criteria (from the proposal — all three direction-free by construction):
- Detection  : a Track A feature separates strong-attractor from control runs at
               AUC >= DETECTION_AUC and beats B0's AUC over the same turns.
- Prediction : median change-point lead over behavioral onset >= PREDICTION_LEAD_TURNS,
               positive vs B0's lead (sign-flip p < 0.05), stable across >= 2 sensitivities.
- Mechanistic: endpoint clustering by condition — silhouette >= SILHOUETTE_MIN or
               within/across distance ratio <= WITHIN_OVER_ACROSS_MAX (L16 / prompt_last).
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys

import numpy as np

from . import config

SILHOUETTE_MIN = 0.25
WITHIN_OVER_ACROSS_MAX = 0.8
AUC_TURN_RANGE = (5, 25)   # turns over which detection AUC is averaged
P_THRESHOLD = 0.05


def _run(module: str, *args: str) -> None:
    cmd = [sys.executable, "-m", f"attractor_internals.{module}", *args]
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, check=True, cwd=config.REPO_ROOT)


def _load(path: str) -> dict | None:
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _mean_auc(series: dict[str, float]) -> float:
    lo, hi = AUC_TURN_RANGE
    vals = [v for k, v in series.items() if lo <= int(k) <= hi and not np.isnan(v)]
    return float(np.mean(vals)) if vals else float("nan")


def evaluate(track_a: dict, track_b: dict, b0: dict) -> dict:
    verdicts: dict = {}

    # -- Detection ---------------------------------------------------------------------------
    b0_auc = _mean_auc(b0.get("auc_by_turn", {}))
    feat_aucs = {f: _mean_auc(s) for f, s in track_a.get("auc_by_turn", {}).items()}
    best_feat, best_auc = max(feat_aucs.items(), key=lambda kv: (not np.isnan(kv[1]), kv[1]),
                              default=(None, float("nan")))
    verdicts["detection"] = {
        "best_feature": best_feat, "best_feature_auc": round(best_auc, 4),
        "b0_auc": round(b0_auc, 4), "threshold": config.DETECTION_AUC,
        "pass": bool(best_auc >= config.DETECTION_AUC and best_auc > b0_auc),
    }

    # -- Prediction (L16 / prompt_last change-point leads) -------------------------------------
    leads = track_b.get("per_layer", {}).get("L16__prompt_last", {}).get("changepoint_leads", {})
    passing = []
    for sens in sorted(leads, key=float):
        e = leads[sens]
        ok = (e.get("median_lead_internal") is not None
              and e["median_lead_internal"] >= config.PREDICTION_LEAD_TURNS
              and e.get("median_lead_vs_b0") is not None and e["median_lead_vs_b0"] > 0
              and e.get("p_beats_b0_signflip") is not None
              and e["p_beats_b0_signflip"] < P_THRESHOLD)
        passing.append((float(sens), ok))
    consecutive = any(passing[i][1] and passing[i + 1][1] for i in range(len(passing) - 1))
    verdicts["prediction"] = {
        "leads_by_sensitivity": leads, "threshold_turns": config.PREDICTION_LEAD_TURNS,
        "pass": bool(consecutive),
    }

    # -- Mechanistic ----------------------------------------------------------------------------
    endpoints = track_b.get("per_layer", {}).get("L16__prompt_last", {}).get("endpoints", {})
    sils = [e["silhouette"] for e in endpoints.values()]
    ratios = [e["within_over_across"] for e in endpoints.values()]
    verdicts["mechanistic"] = {
        "endpoints_by_temp": endpoints,
        "median_silhouette": round(float(np.median(sils)), 4) if sils else None,
        "median_within_over_across": round(float(np.median(ratios)), 4) if ratios else None,
        "pass": bool(sils and (np.median(sils) >= SILHOUETTE_MIN
                               or np.median(ratios) <= WITHIN_OVER_ACROSS_MAX)),
    }

    verdicts["track_a_kill_criterion"] = track_a.get("kill_criterion", {})
    return verdicts


def render(verdicts: dict, quick: bool) -> str:
    def badge(ok: bool) -> str:
        return "**PASS**" if ok else "**FAIL**"

    d, pr, m = verdicts["detection"], verdicts["prediction"], verdicts["mechanistic"]
    kc = verdicts["track_a_kill_criterion"]
    lines = [
        f"# Attractor-internals {'phase-1 signal' if quick else 'report'}",
        "",
        "Decision criteria from `research_updates/2026-07-10_internal_attractor_detection_plan.md`;",
        "all quantities computed by `attractor_internals/analyze_track_[ab].py`.",
        "",
        f"## Detection — {badge(d['pass'])}",
        f"Best Track A feature `{d['best_feature']}` mean AUC over turns "
        f"{AUC_TURN_RANGE[0]}-{AUC_TURN_RANGE[1]}: **{d['best_feature_auc']}** "
        f"(threshold {d['threshold']}; B0 text baseline: {d['b0_auc']}).",
        "",
        f"## Prediction — {badge(pr['pass'])}",
        f"Change-point lead over behavioral onset (L16/prompt_last), by sensitivity "
        f"(needs >= {pr['threshold_turns']} turns, > B0, p < {P_THRESHOLD}, "
        "stable across two consecutive sensitivities):",
        "",
        "| sensitivity | median lead | vs B0 | p | runs w/ change-point |",
        "|---|---|---|---|---|",
    ]
    for sens in sorted(pr["leads_by_sensitivity"], key=float):
        e = pr["leads_by_sensitivity"][sens]
        lines.append(f"| {sens} | {e.get('median_lead_internal')} | "
                     f"{e.get('median_lead_vs_b0')} | {e.get('p_beats_b0_signflip')} | "
                     f"{e.get('frac_with_changepoint')} |")
    lines += [
        "",
        f"## Mechanistic — {badge(m['pass'])}",
        f"Endpoint clustering by condition (L16/prompt_last): median silhouette "
        f"**{m['median_silhouette']}** (>= {SILHOUETTE_MIN} passes), within/across distance "
        f"ratio **{m['median_within_over_across']}** (<= {WITHIN_OVER_ACROSS_MAX} passes).",
        "",
        f"## Track A kill criterion — {'ALIVE' if kc.get('track_a_alive') else 'DEAD'}",
        f"Pre-loop AUCs at {kc.get('condition')}@{kc.get('temperature')}: "
        f"{json.dumps({k: round(v, 3) for k, v in (kc.get('per_feature_auc_preloop') or {}).items()})} "
        f"(needs any >= {kc.get('min_auc_to_survive')}).",
        "",
        "## Figures",
        "",
        "- `track_a/track_a__auc_by_turn.png` — detection AUC vs B0",
        "- `track_a/track_a__<condition>__temp<T>.png` — per-condition logprob trajectories",
        "- `track_b/track_b__velocity_dself.png`, `track_b/track_b__funneling.png`",
        "- `track_b/track_b__endpoints__temp<T>.png`, `track_b/track_b__lead_vs_sensitivity.png`",
        "",
        "Caveats: labels are condition-level (stage-2 judge), not per-run; pvec/steered",
        "conditions are excluded (phase 4 — replay must re-apply the steering hook);",
        "persona-vector projections are validation-only and appear in track_b.json, never in",
        "the criteria above.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--quick", action="store_true",
                   help="phase-1 conditions only; writes PHASE1_SIGNAL.md")
    p.add_argument("--no-run", action="store_true", help="render from existing JSONs only")
    args = p.parse_args()

    conditions = config.PHASE1_CONDITIONS if args.quick else config.ALL_CONDITIONS
    if not args.no_run:
        _run("onset", "--conditions", *conditions)
        _run("baseline_b0")
        _run("analyze_track_a", "--conditions", *conditions)
        _run("analyze_track_b", "--conditions", *conditions)

    track_a = _load(os.path.join(config.REPORTS_DIR, "track_a.json")) or {}
    track_b = _load(os.path.join(config.REPORTS_DIR, "track_b.json")) or {}
    b0 = _load(os.path.join(config.FEATURES_DIR, "b0.json")) or {}
    verdicts = evaluate(track_a, track_b, b0)

    name = "PHASE1_SIGNAL.md" if args.quick else "REPORT.md"
    os.makedirs(config.REPORTS_DIR, exist_ok=True)
    out = os.path.join(config.REPORTS_DIR, name)
    with open(out, "w", encoding="utf-8") as f:
        f.write(render(verdicts, args.quick))
    with open(os.path.join(config.REPORTS_DIR, "verdicts.json"), "w", encoding="utf-8") as f:
        json.dump(verdicts, f, indent=2)
    print(f"wrote {out}")
    for k in ("detection", "prediction", "mechanistic"):
        print(f"  {k}: {'PASS' if verdicts[k]['pass'] else 'FAIL'}")


if __name__ == "__main__":
    main()
