"""Rigor checks for the headline result: the reply-2 state predicts WHEN a run crosses the
role-play line (first reply with a < 0), and z carries that forecast while a does not.

Every check is run on the same frozen dataset definition (printed first) so the numbers are
directly comparable. Laptop only, uses the committed state features + transcripts.

  1. dataset census          what exactly is in / out (n, censoring, crossing-turn spread)
  2. headline + permutation  a vs a+z OOF R² / Spearman, with a shuffled-target null
  3. text baselines          reply length / vocab counts at reply 2, alone and added to a+z
  4. temperature control     within each sampling temperature separately
  5. basin control           within each eventual basin, and a + basin-label as a covariate
  6. layer robustness        same comparison at layers 16 and 48
  7. k sweep                 how many z coordinates are needed
  8. probabilistic version   P(crosses within k more replies | reply-2 state), OOF AUC

    python -m assistant_axis_experiments.state_space.validate_timing --model-key qwen-3-32b
"""

from __future__ import annotations

import argparse
import glob
import json
import os

import numpy as np

from ..axes import AXIS_MODELS, target_layer_for
from . import basins
from .predict import load_trajectories, oof_predictions, sanitized

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")
T0 = 2


def own_reply_texts(results_dirs: list[str]) -> dict[tuple, list[str]]:
    """(condition-dir basename, temperature, run_index, view) -> that instance's own replies."""
    out = {}
    for rd in results_dirs:
        for f in sorted(glob.glob(os.path.join(rd, "two_instance__*.json")) +
                        glob.glob(os.path.join(rd, "cross_model__*.json"))):
            data = json.load(open(f))
            temp = float(data.get("temperature", float("nan")))
            for run in data["runs"]:
                for view in ("A", "B"):
                    out[(os.path.basename(rd), temp, run["run_index"], view)] = [
                        t["content"] for t in run["turns"] if t["speaker"] == view]
    return out


def text_features(replies: list[str]) -> np.ndarray:
    """Cheap text statistics of the first two own replies."""
    txt = " ".join(replies[:T0]).lower()
    words = txt.split()
    n_words = len(words)
    dev = sum(txt.count(w) for w in basins.QWEN_DEVOTION)
    des = sum(txt.count(w) for w in basins.QWEN_DESIGN)
    excl = txt.count("!")
    non_ascii = sum(1 for c in txt if ord(c) > 127)
    return np.array([n_words, len(replies[0].split()) if replies else 0, dev, des, excl,
                     non_ascii, dev - des], dtype=float)


def build_rows(records, texts, dir_of_cond):
    rows = []
    for r in records:
        cross = basins.first_crossing(r["a"], 0.0)
        if len(r["a"]) < T0 or (cross is not None and cross <= T0):
            continue
        key = (dir_of_cond[(r["condition"], r["temperature"])], r["temperature"],
               r["run_index"], r["view"])
        replies = texts.get(key)
        if replies is None or len(replies) < T0:
            continue
        i = T0 - 1
        rows.append({
            "cross": cross, "group": r["group"], "temp": r["temperature"],
            "label": r["label"], "condition": r["condition"],
            "a": r["a"][i:i + 1],
            "z": r["z"][i], "z_norm": r["z_norm"][i:i + 1],
            "text": text_features(replies),
            "n_turns": len(r["a"]),
        })
    return rows


def feats(rows, kind, k=16):
    conds = sorted({r["condition"] for r in rows})
    X = []
    for r in rows:
        onehot = [1.0 if r["condition"] == c else 0.0 for c in conds]
        parts = {
            "a_cond": [r["a"], onehot],
            "az_cond": [r["a"], r["z"][:k], r["z_norm"], onehot],
            "a": [r["a"]],
            "az": [r["a"], r["z"][:k], r["z_norm"]],
            "z": [r["z"][:k], r["z_norm"]],
            "text": [r["text"]],
            "a_text": [r["a"], r["text"]],
            "az_text": [r["a"], r["z"][:k], r["z_norm"], r["text"]],
            "a_temp": [r["a"], [r["temp"]]],
            "az_temp": [r["a"], r["z"][:k], r["z_norm"], [r["temp"]]],
            "a_basin": [r["a"], [1.0 if r["label"] == "devotion" else 0.0]],
            "az_basin": [r["a"], r["z"][:k], r["z_norm"], [1.0 if r["label"] == "devotion" else 0.0]],
        }[kind]
        X.append(np.concatenate([np.atleast_1d(np.asarray(p, dtype=float)) for p in parts]))
    return np.vstack(X)


def score(rows, kind, k=16):
    from scipy.stats import spearmanr
    from sklearn.metrics import r2_score
    crossed = [r for r in rows if r["cross"] is not None]
    y = np.array([r["cross"] for r in crossed], dtype=float)
    g = np.array([r["group"] for r in crossed])
    if len(y) < 25 or len(np.unique(g)) < 5:
        return float("nan"), float("nan"), len(y)
    p = oof_predictions(feats(crossed, kind, k), y, g, "ridge")
    return r2_score(y, p), spearmanr(y, p).statistic, len(y)


def permutation_null(rows, kind, n_perm=200, seed=0):
    """Shuffle crossing turns ACROSS runs (keeping both views of a run together)."""
    from sklearn.metrics import r2_score
    rng = np.random.default_rng(seed)
    crossed = [r for r in rows if r["cross"] is not None]
    y = np.array([r["cross"] for r in crossed], dtype=float)
    g = np.array([r["group"] for r in crossed])
    X = feats(crossed, kind)
    groups = np.unique(g)
    run_y = {grp: y[g == grp][0] for grp in groups}
    null = []
    for _ in range(n_perm):
        perm = rng.permutation(groups)
        mapping = {grp: run_y[p] for grp, p in zip(groups, perm)}
        y_s = np.array([mapping[grp] for grp in g])
        null.append(r2_score(y_s, oof_predictions(X, y_s, g, "ridge")))
    return np.array(null)


def main() -> None:
    ap = argparse.ArgumentParser(description="Rigor checks for the crossing-time prediction.")
    ap.add_argument("--model-key", default="qwen-3-32b", choices=sorted(AXIS_MODELS))
    ap.add_argument("--include-controls", action="store_true",
                    help="also include the simulated-user control runs (default: ai2ai only)")
    ap.add_argument("--reports-dir", default=REPORTS_DIR)
    args = ap.parse_args()

    layer = target_layer_for(args.model_key)
    slug = sanitized(args.model_key)
    dirs = sorted(glob.glob(f"results/axis_{slug}_*ai2ai"))
    dirs = [d for d in dirs if "capped" not in d and "_steer_" not in d]   # no intervened runs
    if not args.include_controls:
        dirs = [d for d in dirs if "usersim" not in d]
    texts = own_reply_texts(dirs)

    def load(layer_):
        recs = load_trajectories(args.model_key, dirs, layer_, k_use=16)
        dir_of_cond = {}
        for r in recs:
            pass
        # map (condition, temperature) -> dir basename via predict's condition parser
        from .predict import _condition_of
        for d in dirs:
            c = _condition_of(d)
            for f in glob.glob(os.path.join(d, "*.json")):
                if "__turn_acts" in f or "analysis" in f:
                    continue
                try:
                    t = float(json.load(open(f)).get("temperature", float("nan")))
                except Exception:
                    continue
                dir_of_cond[(c, t)] = os.path.basename(d)
        return build_rows(recs, texts, dir_of_cond)

    rows = load(layer)
    lines = [f"# Rigor checks: predicting the crossing turn from reply {T0} ({args.model_key}, layer {layer})\n",
             f"Conditions: {', '.join(os.path.basename(d) for d in dirs)}\n"]

    # 1. census
    crossed = [r for r in rows if r["cross"] is not None]
    never = [r for r in rows if r["cross"] is None]
    ct = np.array([r["cross"] for r in crossed])
    lines += ["## 1. Dataset census\n",
              f"- view-trajectories with ≥{T0} replies and not yet below the line at reply {T0}: {len(rows)}",
              f"- of which cross later (the regression targets): {len(crossed)} from "
              f"{len({r['group'] for r in crossed})} runs; never cross (excluded): {len(never)}",
              f"- crossing reply: median {np.median(ct):.0f}, IQR {np.percentile(ct,25):.0f}–{np.percentile(ct,75):.0f}, "
              f"range {ct.min()}–{ct.max()}; a constant-median guess has R² = 0 by definition",
              f"- by temperature: " + ", ".join(
                  f"T={t}: n={sum(1 for r in crossed if r['temp']==t)}, median {np.median([r['cross'] for r in crossed if r['temp']==t]):.0f}"
                  for t in sorted({r['temp'] for r in crossed})),
              f"- by eventual basin: " + ", ".join(
                  f"{b}: n={sum(1 for r in crossed if r['label']==b)}, median {np.median([r['cross'] for r in crossed if r['label']==b]):.0f}"
                  for b in sorted({r['label'] for r in crossed if r['label']})), ""]

    # 2. headline + permutation
    lines += ["## 2. Headline (grouped 5-fold, out-of-fold) and permutation null\n",
              "| features | OOF R² | Spearman |", "|---|---|---|"]
    res = {}
    for kind in ("a", "z", "az"):
        r2, rho, n = score(rows, kind)
        res[kind] = r2
        lines.append(f"| {kind} | {r2:.3f} | {rho:.3f} |")
    null = permutation_null(rows, "az")
    pval = float((np.sum(null >= res["az"]) + 1) / (len(null) + 1))
    lines += ["", f"Permutation null for a+z (crossing turns shuffled across runs, 200 shuffles): "
                  f"null R² median {np.median(null):+.3f}, 95th pct {np.percentile(null,95):+.3f}; "
                  f"observed {res['az']:.3f}, p = {pval:.3f}.", ""]

    # 3. text baselines
    lines += ["## 3. Text baselines (cheap statistics of the first two own replies)\n",
              "Features: word count, first-reply word count, devotion-word count, design-word count, "
              "exclamation marks, non-ascii chars, devotion−design.\n",
              "| features | OOF R² | Spearman |", "|---|---|---|"]
    for kind in ("text", "a_text", "az", "az_text"):
        r2, rho, _ = score(rows, kind)
        lines.append(f"| {kind} | {r2:.3f} | {rho:.3f} |")
    lines.append("")

    # 4. temperature control
    lines += ["## 4. Temperature control\n",
              "| subset | n | a | a+z | a+temp | a+z+temp |", "|---|---|---|---|---|---|"]
    r2a, _, _ = score(rows, "a_temp"); r2az, _, _ = score(rows, "az_temp")
    lines.append(f"| all | {len(crossed)} | {res['a']:.3f} | {res['az']:.3f} | {r2a:.3f} | {r2az:.3f} |")
    for t in sorted({r["temp"] for r in rows}):
        sub = [r for r in rows if r["temp"] == t]
        ra, _, n = score(sub, "a"); raz, _, _ = score(sub, "az")
        lines.append(f"| T={t} | {n} | {ra:.3f} | {raz:.3f} | | |")
    lines.append("")

    # 5. basin control
    lines += ["## 5. Eventual-basin control\n",
              "| subset | n | a | a+z |", "|---|---|---|---|"]
    for b in sorted({r["label"] for r in rows if r["label"]}):
        sub = [r for r in rows if r["label"] == b]
        ra, _, n = score(sub, "a"); raz, _, _ = score(sub, "az")
        lines.append(f"| within {b} | {n} | {ra:.3f} | {raz:.3f} |")
    ra, _, _ = score(rows, "a_basin"); raz, _, _ = score(rows, "az_basin")
    lines.append(f"| all, basin label given as a covariate | {len(crossed)} | {ra:.3f} | {raz:.3f} |")
    ra, _, _ = score(rows, "a_cond"); raz, _, _ = score(rows, "az_cond")
    lines.append(f"| all, CONDITION given as a covariate | {len(crossed)} | {ra:.3f} | {raz:.3f} |")
    for c in sorted({r["condition"] for r in rows}):
        sub = [r for r in rows if r["condition"] == c]
        ra, _, n = score(sub, "a"); raz, _, _ = score(sub, "az")
        lines.append(f"| within condition {c} | {n} | {ra:.3f} | {raz:.3f} |")
    lines.append("")

    # 6. layer robustness
    lines += ["## 6. Layer robustness\n", "| layer | n | a | a+z |", "|---|---|---|---|"]
    for L in (16, 32, 48) if args.model_key == "qwen-3-32b" else (layer,):
        rws = rows if L == layer else load(L)
        ra, _, n = score(rws, "a"); raz, _, _ = score(rws, "az")
        lines.append(f"| {L} | {n} | {ra:.3f} | {raz:.3f} |")
    lines.append("")

    # 7. k sweep
    lines += ["## 7. How many sideways coordinates are needed\n", "| z coords used | a+z OOF R² |", "|---|---|"]
    for k in (1, 2, 4, 8, 16):
        r2, _, _ = score(rows, "az", k=k)
        lines.append(f"| {k} | {r2:.3f} |")
    lines.append("")

    # 8. probabilistic
    from sklearn.metrics import roc_auc_score
    lines += [f"## 8. Probabilistic version: P(crosses within k more replies | reply-{T0} state)\n",
              "Never-crossing trajectories count as negatives here (no exclusion).\n",
              "| horizon k | share positive | a AUC | a+z AUC |", "|---|---|---|---|"]
    for k in (2, 4, 6, 10):
        y = np.array([1 if (r["cross"] is not None and r["cross"] <= T0 + k) else 0 for r in rows])
        g = np.array([r["group"] for r in rows])
        if len(np.unique(y)) < 2:
            continue
        pa = oof_predictions(feats(rows, "a"), y, g, "logistic")
        paz = oof_predictions(feats(rows, "az"), y, g, "logistic")
        ok = ~np.isnan(pa) & ~np.isnan(paz)
        lines.append(f"| {k} | {y.mean():.2f} | {roc_auc_score(y[ok], pa[ok]):.3f} | {roc_auc_score(y[ok], paz[ok]):.3f} |")
    lines.append("")

    os.makedirs(args.reports_dir, exist_ok=True)
    tag = "" if not args.include_controls else "__with_controls"
    out = os.path.join(args.reports_dir, f"validate_timing__{args.model_key}{tag}.md")
    open(out, "w").write("\n".join(lines))
    print("\n".join(lines))
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
