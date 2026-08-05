"""Behavioral-onset ground truth per run — the reference point for every lead-time claim.

Three graded detectors (cheapest first, per the proposal; the per-turn LLM judge is deliberately
out of scope for v1 and only warranted if these disagree badly — their agreement is reported):

- onset_loop        : first verbatim/near-verbatim repeat turn (stage-1 ``verbatim_loops``)
- onset_convergence : first turn where consecutive-turn Jaccard >= JACCARD_ONSET held
                      JACCARD_ONSET_HOLD pairs (stage-1 ``turn_similarity.jaccard``)
- onset_lexical     : first turn where condition-signature tokens (top stage-1 condition words
                      minus base_ai2ai's generic AI2AI diction) exceed KEYWORD_RATE_PER_100,
                      held KEYWORD_HOLD turns (recomputed from the transcript)
- onset_behavioral  : min of the above (None if none fire)

    python -m attractor_internals.onset            # all configured conditions
    python -m attractor_internals.onset --conditions loving_ai2ai poeticism_ai2ai

Writes features/onsets.json:
  {condition: {temp: {"signature_tokens": [...], "runs": {run_index: {onset_*}}}}}
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from attractorbench.analysis.deterministic import _tokens  # noqa: E402 — reuse, don't re-implement

from . import config  # noqa: E402


def load_stage1(condition: str, temp: float) -> dict | None:
    files = config.condition_files(condition, [temp])
    if not files:
        return None
    path = config.stage1_path(files[0][1])
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def base_common_words(top_n: int = config.KEYWORD_BASE_EXCLUDE_N) -> set[str]:
    """Generic AI2AI diction: top words of base_ai2ai pooled across its temps."""
    words: set[str] = set()
    for temp, _ in config.condition_files("base_ai2ai"):
        s1 = load_stage1("base_ai2ai", temp)
        if s1:
            words.update(w for w, _ in s1["condition_word_frequency"][:top_n])
    return words


def signature_tokens(condition: str, temp: float, base_words: set[str]) -> list[str]:
    s1 = load_stage1(condition, temp)
    if not s1:
        return []
    return [w for w, _ in s1["condition_word_frequency"][:config.KEYWORD_TOP_N]
            if w not in base_words]


def signature_rate_series(turns: list[dict], sig_tokens: list[str]) -> list[tuple[int, float]]:
    """(n_tokens, signature-token rate per 100 tokens) for each turn, in transcript order.

    The lexical-onset detector's per-turn series (over ``content_clean``), extracted so
    trait_rate.py can emit the full series while run_onsets keeps only the onset turn.
    """
    sig = set(sig_tokens)
    out = []
    for t in turns:
        toks = _tokens(t["content_clean"])
        rate = 100.0 * sum(tok in sig for tok in toks) / len(toks) if toks else 0.0
        out.append((len(toks), rate))
    return out


def _held_onset(series: list[float], threshold: float, hold: int, turn_of_index) -> int | None:
    """First index i where series[i:i+hold] all >= threshold; returned as a turn number."""
    for i in range(len(series) - hold + 1):
        if all(s >= threshold for s in series[i:i + hold]):
            return turn_of_index(i)
    return None


def run_onsets(run_s1: dict, run_transcript: dict, sig_tokens: list[str]) -> dict:
    # onset_loop — later turn of the first exact or near-exact repeat pair.
    vl = run_s1["verbatim_loops"]
    loop_candidates = []
    if vl.get("first_exact_repeat_turn") is not None:
        loop_candidates.append(vl["first_exact_repeat_turn"])
    if vl.get("near_exact_pairs"):
        loop_candidates.append(min(p[1] for p in vl["near_exact_pairs"]))
    onset_loop = min(loop_candidates) if loop_candidates else None

    # onset_convergence — jaccard[i] compares turns i+1 and i+2; onset = the later turn.
    jac = run_s1["turn_similarity"]["jaccard"]
    onset_convergence = _held_onset(jac, config.JACCARD_ONSET, config.JACCARD_ONSET_HOLD,
                                    lambda i: i + 2)

    # onset_lexical — signature-token rate per 100 tokens, recomputed from the transcript.
    onset_lexical = None
    if sig_tokens:
        rates = [r for _, r in signature_rate_series(run_transcript["turns"], sig_tokens)]
        onset_lexical = _held_onset(rates, config.KEYWORD_RATE_PER_100, config.KEYWORD_HOLD,
                                    lambda i: run_transcript["turns"][i]["turn"])

    fired = [o for o in (onset_loop, onset_convergence, onset_lexical) if o is not None]
    return {
        "onset_loop": onset_loop,
        "onset_convergence": onset_convergence,
        "onset_lexical": onset_lexical,
        "onset_behavioral": min(fired) if fired else None,
        "n_turns": run_s1["n_turns"],
    }


def compute_onsets(conditions: list[str]) -> dict:
    base_words = base_common_words()
    out: dict = {}
    for condition in conditions:
        out[condition] = {}
        for temp, path in config.condition_files(condition):
            s1 = load_stage1(condition, temp)
            if s1 is None:
                print(f"!! no stage-1 for {condition}@{temp:g} — run attractorbench.analysis.deterministic first")
                continue
            with open(path, encoding="utf-8") as f:
                transcript = json.load(f)
            runs_by_index = {r["run_index"]: r for r in transcript["runs"]}
            # base_ai2ai's basin is the planning/verbatim loop, not a trait vocabulary — its
            # lexical detector would just re-detect generic diction, so it gets no signature.
            sig = [] if condition == "base_ai2ai" else signature_tokens(condition, temp, base_words)
            entry = {"signature_tokens": sig, "runs": {}}
            for run_s1 in s1["runs"]:
                ri = run_s1["run_index"]
                entry["runs"][str(ri)] = run_onsets(run_s1, runs_by_index[ri], sig)
            out[condition][f"{temp:g}"] = entry
    return out


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--conditions", nargs="*", default=config.ALL_CONDITIONS)
    p.add_argument("--out", default=os.path.join(config.FEATURES_DIR, "onsets.json"))
    args = p.parse_args()

    onsets = compute_onsets(args.conditions)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(onsets, f, indent=2)

    n_runs = sum(len(e["runs"]) for c in onsets.values() for e in c.values())
    fired = sum(1 for c in onsets.values() for e in c.values()
                for r in e["runs"].values() if r["onset_behavioral"] is not None)
    print(f"wrote {args.out}: {n_runs} runs, behavioral onset found in {fired}")
    # Detector agreement (the check that decides whether a per-turn judge is ever needed).
    diffs = [abs(r["onset_convergence"] - r["onset_lexical"])
             for c in onsets.values() for e in c.values() for r in e["runs"].values()
             if r["onset_convergence"] is not None and r["onset_lexical"] is not None]
    if diffs:
        diffs.sort()
        print(f"convergence-vs-lexical onset |delta| median={diffs[len(diffs) // 2]} "
              f"(n={len(diffs)}) — large medians would warrant the per-turn judge")


if __name__ == "__main__":
    main()
