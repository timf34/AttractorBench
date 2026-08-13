"""Per-turn condition-signature-token rate series — the onset.py lexical detector, kept per turn.

onset.run_onsets computes the signature-token rate per 100 tokens for every turn but only keeps
the onset turn; correlating persona-vector projections (project_pvec) with behavioral trait
expression needs the whole series. This module re-emits it flat, with the same run-quality
guards as project_pvec (degenerate_run — flagged, never dropped).

Conventions carried over from onset.py: signature tokens = the condition's top stage-1 words
minus base_ai2ai's generic AI2AI diction; base_ai2ai itself gets no signature (its basin is the
planning/verbatim loop, not a trait vocabulary), so its rates are all 0. Rates are computed over
``content_clean`` for BOTH speakers' turns — join on (run_index, turn); odd turns = view A.

    python -m attractor_internals.trait_rate --condition goodness_pvec_c2.0_l16_ai2ai
    python -m attractor_internals.trait_rate --condition loving_pvec_unsteer_k2_ai2ai --temps 0.7

Writes features/<cond>__temp<T>__trait_rate.jsonl, one row per (run_index, turn):
  condition, temperature, run_index, turn, speaker ("A"|"B"), n_tokens, sig_rate_per_100,
  steered_gen, switch_turn, degenerate_run
plus features/<cond>__temp<T>__trait_rate_meta.json (the signature-token list + provenance).
Idempotent per (condition, temperature) unless --force.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os

from . import config, features_io, onset
from .project_pvec import degenerate_runs, is_steered_model, switch_turn_of


def trait_rate_path(condition: str, temp: float, out_dir: str | None = None) -> str:
    d = os.path.join(out_dir or config.OUT_DIR, "features")
    return os.path.join(d, f"{condition}__temp{temp:g}__trait_rate.jsonl")


def trait_rate_meta_path(condition: str, temp: float, out_dir: str | None = None) -> str:
    d = os.path.join(out_dir or config.OUT_DIR, "features")
    return os.path.join(d, f"{condition}__temp{temp:g}__trait_rate_meta.json")


def rate_condition_temp(condition: str, temp: float, transcript_path: str,
                        sig_tokens: list[str], out_dir: str) -> dict:
    """One (condition, temperature) -> trait_rate.jsonl + meta. Returns the meta dict."""
    with open(transcript_path, encoding="utf-8") as f:
        data = json.load(f)
    sw = switch_turn_of(condition, data)   # payload record preferred; name regex as fallback
    degen = degenerate_runs(data["runs"], sw)

    rows: list[dict] = []
    for run in data["runs"]:
        series = onset.signature_rate_series(run["turns"], sig_tokens)
        for t, (n_tokens, rate) in zip(run["turns"], series):
            rows.append({
                "condition": condition, "temperature": temp,
                "run_index": run["run_index"], "turn": t["turn"], "speaker": t["speaker"],
                "n_tokens": n_tokens, "sig_rate_per_100": round(rate, 4),
                "steered_gen": is_steered_model(t.get("model")), "switch_turn": sw,
                "degenerate_run": bool(degen.get(run["run_index"], False)),
            })

    path = trait_rate_path(condition, temp, out_dir)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")

    rel = os.path.relpath(transcript_path, config.REPO_ROOT)
    meta = {
        "condition": condition, "temperature": temp,
        "transcript": rel if not rel.startswith("..") else transcript_path,
        "signature_tokens": sig_tokens, "switch_turn": sw,
        "degenerate_runs": sorted(ri for ri, bad in degen.items() if bad),
        "n_rows": len(rows),
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    features_io.write_meta(trait_rate_meta_path(condition, temp, out_dir), meta)
    return meta


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--condition", required=True, help="results/<condition> to score")
    p.add_argument("--temps", nargs="*", type=float, default=None, help="subset of temperatures")
    p.add_argument("--out-dir", default=config.OUT_DIR)
    p.add_argument("--force", action="store_true", help="re-emit even if outputs exist")
    args = p.parse_args()

    files = config.condition_files(args.condition, args.temps)
    if not files:
        raise SystemExit(f"no transcript files for {args.condition} (temps={args.temps})")
    base_words = onset.base_common_words()

    for temp, path in files:
        if not args.force and os.path.exists(trait_rate_meta_path(args.condition, temp, args.out_dir)):
            print(f"{args.condition}@{temp:g}: trait_rate outputs exist — skipping (--force to redo)")
            continue
        if args.condition == "base_ai2ai":
            sig: list[str] = []  # same convention as onset.compute_onsets
        else:
            sig = onset.signature_tokens(args.condition, temp, base_words)
            if not sig:
                print(f"!! {args.condition}@{temp:g}: no stage-1 signature tokens — "
                      "run attractorbench.analysis.deterministic first; skipping")
                continue
        meta = rate_condition_temp(args.condition, temp, path, sig, args.out_dir)
        print(f"wrote {meta['n_rows']} rows for {args.condition}@{temp:g} "
              f"({len(sig)} signature tokens, degenerate runs: {meta['degenerate_runs']})")


if __name__ == "__main__":
    main()
