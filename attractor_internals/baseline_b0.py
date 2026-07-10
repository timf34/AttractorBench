"""B0 — the text-only baseline every internal-signal claim must beat.

A logistic probe over per-turn features the TEXT already shows (all derived from stage-1 JSONs
plus signature-token/emoji rates recomputed from transcripts): consecutive-turn Jaccard + its
recent slope, TTR + slope, turn length, question count, signature-keyword rate, emoji rate.

Labels are condition-level: strong-attractor conditions = 1, negative control (poeticism) and
base = 0 (a known weakness — stage-2 judge labels are per condition x temp, not per run;
reported as a caveat, the per-run onset carries the prediction claim).

Outputs features/b0.json:
  auc_by_turn : {turn: AUC of grouped-CV predictions at that turn}
  b0_onset    : {condition: {temp: {run_index: first turn with CV p>0.5 held B0_ONSET_HOLD}}}

    python -m attractor_internals.baseline_b0
"""

from __future__ import annotations

import argparse
import json
import os

import numpy as np

from . import config, onset

STRONG_CONDITIONS = ["loving_ai2ai", "nonchalance_ai2ai", "remorse_ai2ai",
                     "sycophancy_ai2ai", "sarcasm_ai2ai"]
CONTROL_CONDITIONS = ["poeticism_ai2ai", "base_ai2ai"]
B0_ONSET_HOLD = 3
FEATURE_NAMES = ["jaccard", "jaccard_slope3", "ttr", "ttr_slope3",
                 "log_chars", "questions", "keyword_rate", "emoji_rate"]


def _slope3(xs: list[float], i: int) -> float:
    w = xs[max(0, i - 2):i + 1]
    return (w[-1] - w[0]) / max(len(w) - 1, 1)


def build_dataset(conditions: list[str]) -> list[dict]:
    """One row per (condition, temp, run, turn) with the B0 feature vector."""
    import sys
    sys.path.insert(0, config.REPO_ROOT)
    from attractorbench.analysis.deterministic import _EMOJI_RE, _tokens

    base_words = onset.base_common_words()
    rows: list[dict] = []
    for condition in conditions:
        label = 1 if condition in STRONG_CONDITIONS else 0
        for temp, path in config.condition_files(condition):
            s1 = onset.load_stage1(condition, temp)
            if s1 is None:
                continue
            with open(path, encoding="utf-8") as f:
                transcript = json.load(f)
            runs_by_index = {r["run_index"]: r for r in transcript["runs"]}
            # Same formula for EVERY condition (controls included) — conditioning this on the
            # label would leak it straight into the probe (keyword_rate = 0 iff control).
            sig = set(onset.signature_tokens(condition, temp, base_words))
            for run_s1 in s1["runs"]:
                run = runs_by_index[run_s1["run_index"]]
                jac = run_s1["turn_similarity"]["jaccard"]
                ttr = run_s1["ttr_per_turn"]
                chars = run_s1["trajectory"]["chars_per_turn"]
                questions = run_s1["trajectory"]["questions_per_turn"]
                for ti, t in enumerate(run["turns"]):
                    toks = _tokens(t["content_clean"])
                    n_toks = max(len(toks), 1)
                    j = jac[ti - 1] if ti >= 1 else 0.0  # pair ending at this turn
                    feats = [
                        j,
                        _slope3(jac, ti - 1) if ti >= 1 else 0.0,
                        ttr[ti],
                        _slope3(ttr, ti),
                        float(np.log1p(chars[ti])),
                        float(questions[ti]),
                        100.0 * sum(tok in sig for tok in toks) / n_toks,
                        100.0 * len(_EMOJI_RE.findall(t["content_clean"])) / n_toks,
                    ]
                    rows.append({
                        "condition": condition, "temperature": temp,
                        "run_index": run["run_index"], "turn": t["turn"],
                        "label": label, "features": feats,
                    })
    return rows


def fit_b0(rows: list[dict], n_folds: int = 5, seed: int = 0) -> dict:
    """Per-turn grouped-CV logistic probe: AUC(k) + per-run probability trajectories."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import GroupKFold
    from sklearn.preprocessing import StandardScaler

    auc_by_turn: dict[str, float] = {}
    probs: dict[tuple, dict[int, float]] = {}  # (cond, temp, run) -> {turn: p}
    turns = sorted({r["turn"] for r in rows})
    for k in turns:
        sub = [r for r in rows if r["turn"] == k]
        y = np.array([r["label"] for r in sub])
        if len(set(y)) < 2:
            continue
        X = np.array([r["features"] for r in sub])
        groups = np.array([f"{r['condition']}|{r['temperature']}|{r['run_index']}" for r in sub])
        pred = np.zeros(len(sub))
        gkf = GroupKFold(n_splits=min(n_folds, len(set(groups))))
        for tr, te in gkf.split(X, y, groups):
            scaler = StandardScaler().fit(X[tr])
            clf = LogisticRegression(max_iter=2000, random_state=seed)
            clf.fit(scaler.transform(X[tr]), y[tr])
            pred[te] = clf.predict_proba(scaler.transform(X[te]))[:, 1]
        auc_by_turn[str(k)] = float(roc_auc_score(y, pred))
        for r, p in zip(sub, pred):
            probs.setdefault((r["condition"], r["temperature"], r["run_index"]), {})[k] = float(p)

    b0_onset: dict = {}
    for (cond, temp, ri), traj in probs.items():
        ks = sorted(traj)
        onset_turn = None
        for i in range(len(ks) - B0_ONSET_HOLD + 1):
            if all(traj[ks[i + j]] > 0.5 for j in range(B0_ONSET_HOLD)):
                onset_turn = ks[i]
                break
        b0_onset.setdefault(cond, {}).setdefault(f"{temp:g}", {})[str(ri)] = onset_turn
    return {"feature_names": FEATURE_NAMES, "auc_by_turn": auc_by_turn, "b0_onset": b0_onset,
            "strong_conditions": STRONG_CONDITIONS, "control_conditions": CONTROL_CONDITIONS}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--conditions", nargs="*", default=STRONG_CONDITIONS + CONTROL_CONDITIONS)
    p.add_argument("--out", default=os.path.join(config.FEATURES_DIR, "b0.json"))
    args = p.parse_args()

    rows = build_dataset(args.conditions)
    if not rows:
        raise SystemExit("no stage-1 data found for the requested conditions")
    print(f"B0 dataset: {len(rows)} (run, turn) rows over {len(args.conditions)} conditions")
    result = fit_b0(rows)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    aucs = result["auc_by_turn"]
    mid = {k: v for k, v in aucs.items() if 5 <= int(k) <= 15}
    print(f"wrote {args.out}; AUC turn-5..15 mean = "
          f"{np.mean(list(mid.values())):.3f}" if mid else f"wrote {args.out}")


if __name__ == "__main__":
    main()
