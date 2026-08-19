"""Detect per-conversation LOCK onset (verbatim/near-verbatim loop) from text novelty and write
PRE-LOCK truncated copies of condition files, so the stage-2 judge can characterise what the
conversation was about BEFORE it degenerated (the condition-level judge otherwise reads the
loop as the basin).

Novelty of turn t = fraction of its word n-gram shingles (default 6-grams) that never appeared
in turns 1..t-1 of the same conversation (lowercased _tokens from stage-1). A turn that is a
near-verbatim echo of earlier text has novelty ~0. Lock onset = first turn whose novelty is
below --thresh and stays below it for --hold consecutive turns (None if never). Very short
turns (< n tokens) count as novelty 0 only if their text exactly repeats an earlier turn.

    python prelock_truncate.py results/axis_qwen_3_32b_agnostic_steer_*_nosys_ai2ai
    # -> results/prelock_<basename>/two_instance__*.json (runs truncated to turns < onset)
    #    + results/prelock_<basename>/analysis/prelock_onsets.json ; then: python run_judge.py results/prelock_<basename>

Conversations with no detected lock are copied whole; conversations that lock before
--min-turns are dropped from the truncated file (too little pre-lock content to judge).
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import statistics as st

from attractorbench.analysis.deterministic import _tokens


def novelty_series(turns: list[dict], n: int) -> list[float]:
    seen: set[tuple] = set()
    seen_text: set[str] = set()
    out = []
    for t in turns:
        toks = _tokens(t.get("content", ""))
        text = " ".join(toks)
        grams = {tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)}
        if not grams:
            nov = 0.0 if text in seen_text else 1.0
        else:
            nov = len(grams - seen) / len(grams)
        out.append(nov)
        seen |= grams
        seen_text.add(text)
    return out


def lock_onset(nov: list[float], thresh: float, hold: int) -> int | None:
    """1-based turn index of the first turn starting a run of `hold` turns below `thresh`."""
    for i in range(len(nov) - hold + 1):
        if all(x < thresh for x in nov[i:i + hold]):
            return i + 1
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description="Pre-lock truncation of condition files.")
    ap.add_argument("dirs", nargs="+", help="results condition dirs")
    ap.add_argument("--ngram", type=int, default=6)
    ap.add_argument("--thresh", type=float, default=0.3)
    ap.add_argument("--hold", type=int, default=2)
    ap.add_argument("--min-turns", type=int, default=4, help="drop runs that lock before this many pre-lock turns")
    ap.add_argument("--out-prefix", default="prelock_")
    args = ap.parse_args()

    print(f"{'condition':44s} {'n':>2s} {'locked':>6s} {'onset median':>12s} {'onset IQR':>11s} {'pre-lock chars %':>16s}")
    for d in args.dirs:
        d = d.rstrip("/")
        files = sorted(glob.glob(os.path.join(d, "two_instance__*.json")) + glob.glob(os.path.join(d, "cross_model__*.json")))
        out_dir = os.path.join(os.path.dirname(d), args.out_prefix + os.path.basename(d))
        os.makedirs(out_dir, exist_ok=True)
        onsets_all: dict = {}
        for f in files:
            cond = json.load(open(f))
            kept, onsets = [], {}
            for r in cond["runs"]:
                nov = novelty_series(r["turns"], args.ngram)
                on = lock_onset(nov, args.thresh, args.hold)
                total = sum(len(t["content"]) for t in r["turns"])
                pre = sum(len(t["content"]) for t in r["turns"][: (on - 1) if on else len(r["turns"])])
                onsets[str(r["run_index"])] = {"onset_turn": on, "n_turns": len(r["turns"]),
                                               "novelty": [round(x, 3) for x in nov],
                                               "prelock_char_frac": round(pre / total, 3) if total else None}
                if on is None:
                    kept.append(r)
                elif on - 1 >= args.min_turns:
                    rr = dict(r); rr["turns"] = r["turns"][: on - 1]
                    rr["truncated_at_lock_onset"] = on; rr["ended_reason"] = "prelock_truncated"
                    kept.append(rr)
            out = dict(cond); out["runs"] = kept
            out["prelock_truncation"] = {"ngram": args.ngram, "thresh": args.thresh, "hold": args.hold,
                                         "min_turns": args.min_turns, "source": os.path.relpath(f)}
            with open(os.path.join(out_dir, os.path.basename(f)), "w") as fh:
                json.dump(out, fh, ensure_ascii=False, indent=1)
            onsets_all[os.path.basename(f)] = onsets
            ons = [v["onset_turn"] for v in onsets.values() if v["onset_turn"]]
            fr = [v["prelock_char_frac"] for v in onsets.values() if v["prelock_char_frac"] is not None]
            q = (f"{st.quantiles(ons, n=4)[0]:.0f}-{st.quantiles(ons, n=4)[2]:.0f}" if len(ons) >= 4 else "-")
            print(f"{os.path.basename(d)[:44]:44s} {len(onsets):>2d} {len(ons):>6d} {(st.median(ons) if ons else float('nan')):>12.1f} "
                  f"{q:>11s} {100*st.median(fr):>15.0f}%   kept {len(kept)}/{len(onsets)} runs -> {out_dir}")
        os.makedirs(os.path.join(out_dir, "analysis"), exist_ok=True)   # analysis/ is skipped by run_judge's condition glob
        with open(os.path.join(out_dir, "analysis", "prelock_onsets.json"), "w") as fh:
            json.dump(onsets_all, fh, indent=1)


if __name__ == "__main__":
    main()
