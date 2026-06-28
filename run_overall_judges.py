"""Ensure the OVERALL judge outputs exist for every model at every scope (cache-aware).

Scopes: ALL (pooled) + one per system prompt. Skips any that already exist on disk so it's
cheap to re-run. Writes results/family_sweep/<model>/analysis/overall__<scope>.{json,md}.

    python run_overall_judges.py
"""

from __future__ import annotations

import concurrent.futures as cf
import glob
import json
import os

from attractorbench.analysis.characterize import characterize_overall
from attractorbench.render import write_markdown

MODELS = [
    "gpt-5.4", "gpt-5.4-mini", "gpt-5.4-nano", "gpt-5.3-chat-latest",
    "gpt-5.2", "gpt-5.1", "gpt-5", "gpt-4.1", "gpt-4o",
]
SYSTEM_PROMPTS = ["helpful_assistant", "ai_to_ai_aware", "ai_to_ai_self_aware", "self_monologue"]
ROOT = "results/family_sweep"


def is_confounded(cond) -> bool:
    """self_append × ai_to_ai_* = one model ventriloquizing both sides (see notes.md). Excluded
    from all judge pools so the signatures only reflect clean conditions."""
    return (cond.get("mode") == "self_append"
            and str(cond.get("system_prompt_key") or "").startswith("ai_to_ai"))


def load_conditions(slug):
    out = []
    for f in glob.glob(os.path.join(ROOT, slug, "*.json")):
        if "/analysis/" in f:
            continue
        d = json.load(open(f))
        if d.get("runs") and not is_confounded(d):
            out.append(d)
    return out


def job(args):
    slug, scope = args
    out_dir = os.path.join(ROOT, slug, "analysis")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"overall__{scope}.json")
    if os.path.exists(path):
        return f"  [skip] {slug} {scope} (exists)"
    conds = load_conditions(slug)
    if scope != "ALL":
        conds = [c for c in conds if c.get("system_prompt_key") == scope]
    if not conds:
        return f"  [none] {slug} {scope} (no conditions)"
    desc = (f"model {slug}, ALL framings/seeds/modes pooled" if scope == "ALL"
            else f"model {slug}, system prompt '{scope}', all seeds & modes")
    r = characterize_overall(conds, desc)
    json.dump(r, open(path, "w"), indent=2, ensure_ascii=False)
    write_markdown(r, path)
    pa = (r.get("primary_attractor") or {}).get("label")
    return f"  [done] {slug} {scope} -> {pa}"


def main():
    import argparse
    p = argparse.ArgumentParser(description="Ensure overall judge outputs exist (cache-aware).")
    p.add_argument("--concurrency", type=int, default=6, help="concurrent judge calls (default 6)")
    args = p.parse_args()
    tasks = [(m, s) for m in MODELS for s in (["ALL"] + SYSTEM_PROMPTS)]
    print(f"Ensuring {len(tasks)} overall judge outputs (cache-aware, concurrency={args.concurrency})...", flush=True)
    with cf.ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        for line in ex.map(job, tasks):
            print(line, flush=True)
    print("DONE")


if __name__ == "__main__":
    main()
