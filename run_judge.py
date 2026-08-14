"""Run ONLY the stage-2 judge over already-generated condition files (decoupled from generation).

Lets you generate cheaply first (`run_matrix.py --no-judge`) and judge later — and finetune the
judge independently: swap the judge model, shrink the transcript budget (read fewer runs), or
re-judge a subset, without re-running any conversations.

    python run_judge.py results/family_sweep                       # judge everything (default gpt-5.4)
    python run_judge.py results/family_sweep --judge openai/gpt-5.4-mini   # cheaper judge
    python run_judge.py results/family_sweep --context-budget 40000        # read fewer transcripts -> cheaper
    python run_judge.py results/family_sweep --concurrency 8

Writes <dir>/.../analysis/<condition>__stage2.json (+ .md) next to each condition.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import glob
import json
import os
import threading
import traceback
from datetime import datetime

from attractorbench import providers
from attractorbench.analysis import characterize
from attractorbench.render import write_markdown

_log_lock = threading.Lock()


def log(msg: str) -> None:
    with _log_lock:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def find_condition_files(root: str) -> list[str]:
    """All condition JSONs under root, excluding the analysis/ outputs (stage1/stage2)."""
    files = glob.glob(os.path.join(root, "**", "*.json"), recursive=True)
    return sorted(f for f in files if f"{os.sep}analysis{os.sep}" not in f)


def judge_one(path: str, judge_model: str, context_budget: int) -> dict:
    out = {"path": path, "ok": False, "attractors": None}
    try:
        data = json.load(open(path))
        if not data.get("runs"):
            log(f"  [skip] {os.path.basename(path)} (no runs)")
            return out
        s2 = characterize.characterize_condition(
            data, judge_model=judge_model, token_budget=context_budget
        )
        s2p = characterize._output_path(path)
        json.dump(s2, open(s2p, "w"), indent=2, ensure_ascii=False)
        write_markdown(s2, s2p)
        out["ok"] = s2["parse_ok"]
        out["attractors"] = s2.get("attractors")
        log(f"  [judged] {os.path.basename(path)} (parse_ok={s2['parse_ok']}, "
            f"sampled {s2['n_runs_sampled']}/{s2['n_runs_total']})")
    except Exception:
        log(f"  [FAIL] {os.path.basename(path)}\n{traceback.format_exc()}")
    return out


def main() -> None:
    p = argparse.ArgumentParser(description="Stage-2 judge over existing condition files.")
    p.add_argument("root", help="directory of generated condition files (e.g. results/family_sweep)")
    p.add_argument("--judge", default=characterize.JUDGE_MODEL, help=f"judge model (default {characterize.JUDGE_MODEL})")
    p.add_argument("--context-budget", type=int, default=characterize.JUDGE_CONTEXT_TOKEN_BUDGET,
                   help="token ceiling for whole-transcript sampling (lower = cheaper, fewer runs read)")
    p.add_argument("--concurrency", type=int, default=6)
    p.add_argument("--match", default=None,
                   help="only judge condition files whose filename contains ANY of these "
                        "comma-separated substrings (e.g. 'self_monologue,self_append_lastmsg')")
    args = p.parse_args()

    files = find_condition_files(args.root)
    if args.match:
        subs = [s.strip() for s in args.match.split(",")]
        files = [f for f in files if any(s in os.path.basename(f) for s in subs)]
    log(f"PLAN: judge {len(files)} conditions with {args.judge} "
        f"(context_budget={args.context_budget}, concurrency={args.concurrency})")
    if not files:
        log("No condition files found.")
        return

    # pre-init the shared client for the judge's backend before threads — an openrouter/
    # judge must not require OPENAI_API_KEY (pods usually carry only the OpenRouter key)
    if args.judge.startswith("openrouter/"):
        providers._get_openrouter_client()
    else:
        providers._get_client()
    results = []
    with cf.ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futs = [ex.submit(judge_one, f, args.judge, args.context_budget) for f in files]
        for fut in cf.as_completed(futs):
            results.append(fut.result())

    ok = sum(1 for r in results if r["ok"])
    log(f"==== DONE: {ok}/{len(results)} parsed cleanly ====")
    for r in sorted(results, key=lambda x: x["path"]):
        # PRIMARY marked with '*'; unmarked = secondary clusters. No '*' anywhere means the
        # judge found no dominant shared attractor (the honest-null outcome).
        labels = ", ".join(f"{'*' if a.get('is_primary') else ''}{a.get('label')} ({a.get('fraction_of_runs')})"
                           for a in (r["attractors"] or [])) or "— (no shared attractor)"
        log(f"  {os.path.basename(r['path'])}: {labels}")


if __name__ == "__main__":
    main()
