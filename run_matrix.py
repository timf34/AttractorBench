"""Model-family attractor sweep — parallel matrix runner.

Runs the full matrix: REGIMES (system prompt + seed set) x MODELS x MODES, at SEEDS reps per
prompt and MAX_TURNS turns. All runs across all conditions go through ONE global thread pool for
maximum throughput (litmus-style: concurrent.futures + threading.Lock).

Thread-safety: conversation histories are created INSIDE each harness call, so threads never
share conversation state. The only shared state is (a) each condition's runs list + JSON file
(guarded by a per-condition Lock) and (b) console logging (guarded by a global log Lock).

    python run_matrix.py --dry-run                 # show the plan, no API calls
    python run_matrix.py                           # full run
    python run_matrix.py --models openai/gpt-5.4-nano --max-turns 2 --concurrency 4   # cheap smoke
    nohup caffeinate -is ./.venv/bin/python run_matrix.py > matrix.log 2>&1 &

Outputs: results/family_sweep/<model>/<mode>__<model>__<system>__<seed>__temp<t>.json (+ .md),
plus analysis/*__stage1.* and *__stage2.* per condition.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import threading
import traceback
from datetime import datetime
from itertools import zip_longest

from attractorbench import providers
from attractorbench import runner as R
from attractorbench.config import RunConfig
from attractorbench.prompts import SEED_PROMPTS, build_system_prompt
from attractorbench.render import write_markdown
from attractorbench.analysis import characterize, deterministic

# --- the matrix ------------------------------------------------------------
MODELS = [
    "openai/gpt-4o",
    "openai/gpt-4.1",
    "openai/gpt-5",
    "openai/gpt-5.1",
    "openai/gpt-5.2",
    "openai/gpt-5.3-chat-latest",
    "openai/gpt-5.4",
    "openai/gpt-5.4-mini",
    "openai/gpt-5.4-nano",
]
# (system_prompt_key, seed_prompt_set)
REGIMES = [
    ("helpful_assistant", "open_ended_v1"),       # paper baseline (unaware, neutral)
    ("helpful_assistant", "assistant_greeting_v1"),  # realistic deployment (unaware)
    ("helpful_assistant", "topic_v1"),            # topic-independence
    ("ai_to_ai_aware", "ai_to_ai_opener_v1"),     # knows it's another AI
    ("ai_to_ai_self_aware", "ai_to_ai_opener_v1"),  # knows it's itself
    ("ai_to_ai_aware", "clinical_v1"),            # AI-aware but detached/clinical tone (tone contrast)
    ("helpful_assistant", "minimal_v1"),          # extreme low-prompt baseline
]
MODES = ["self_append", "two_instance"]

TEMPERATURE = 1.0
REASONING_EFFORT = "low"   # auto-dropped for non-reasoning models (gpt-4o/4.1/5.3-chat)
MAX_NEW_TOKENS = 2048

_log_lock = threading.Lock()


def log(msg: str) -> None:
    with _log_lock:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


class Condition:
    """One (regime, model, mode) cell: its config, resolved output path, and a guarded runs list."""

    def __init__(self, cfg: RunConfig, system_prompt: str, path: str):
        self.cfg = cfg
        self.system_prompt = system_prompt
        self.path = path
        self.runs: list[dict] = []
        self.lock = threading.Lock()

    @property
    def name(self) -> str:
        return os.path.basename(self.path)


def build_conditions(models, max_turns, seeds, output_dir) -> list[Condition]:
    conditions = []
    for system_key, seed_set in REGIMES:
        for model in models:
            for mode in MODES:
                model_b = model if mode == "two_instance" else None
                cfg = RunConfig(
                    experiment_name=f"family_sweep/{R._model_slug(model)}",
                    mode=mode,
                    model_a=model,
                    model_b=model_b,
                    seed_prompt_set=seed_set,
                    system_prompt_key=system_key,
                    max_turns=max_turns,
                    seeds=seeds,
                    temperature=TEMPERATURE,
                    reasoning_effort=REASONING_EFFORT,
                    max_new_tokens=MAX_NEW_TOKENS,
                    output_dir=output_dir,
                )
                R.validate(cfg)
                sp = build_system_prompt(system_key, cfg.allow_early_end)
                path = R._condition_path(cfg, TEMPERATURE)  # resolves no-clobber path, makes dir
                conditions.append(Condition(cfg, sp, path))
    return conditions


def build_tasks(conditions):
    """Flat task list, interleaved round-robin across conditions so concurrent workers span many
    models (rate-limit smoothing)."""
    per_cond = []
    for cond in conditions:
        lst = []
        ri = 0
        for spi, prompt in enumerate(SEED_PROMPTS[cond.cfg.seed_prompt_set]):
            for rep in range(cond.cfg.seeds):
                lst.append((cond, ri, prompt, spi, rep))
                ri += 1
        per_cond.append(lst)
    return [t for group in zip_longest(*per_cond) for t in group if t is not None]


def run_task(task) -> None:
    cond, run_index, prompt, spi, rep = task
    harness = R._HARNESSES[cond.cfg.mode]
    try:
        run = harness(cond.cfg, cond.system_prompt, prompt, run_index, cond.cfg.temperature)
    except Exception as e:  # noqa: BLE001 — one run failing must not kill the sweep
        log(f"  [FAIL] {cond.name} run {run_index}: {type(e).__name__}: {e}")
        return
    run["seed_prompt_index"] = spi
    run["repetition"] = rep
    with cond.lock:  # guards this condition's runs list + its JSON file (incremental crash-safe)
        cond.runs.append(run)
        R._save_condition(cond.path, cond.cfg, cond.cfg.temperature, cond.system_prompt, cond.runs)
        done = len(cond.runs)
    log(f"  [ok] {cond.name}: {done} runs (last {len(run['turns'])} turns)")


def analyse(cond: Condition, judge_model: str | None) -> dict:
    """Transcript .md + stage 1 (free) + optional stage 2 (judge) for one finished condition.

    judge_model=None skips the (expensive) judge — run it later with run_judge.py.
    """
    summary = {"name": cond.name, "attractors": None}
    if not cond.runs:
        return summary
    try:
        data = json.load(open(cond.path))
        write_markdown(data, cond.path)  # transcripts .md
        s1 = deterministic.analyse_condition(data)
        s1p = deterministic._output_path(cond.path)
        json.dump(s1, open(s1p, "w"), indent=2, ensure_ascii=False)
        write_markdown(s1, s1p)
        if judge_model is None:
            log(f"  [stage1 only] {cond.name} (judge skipped)")
            return summary
        s2 = characterize.characterize_condition(data, judge_model=judge_model)
        s2p = characterize._output_path(cond.path)
        json.dump(s2, open(s2p, "w"), indent=2, ensure_ascii=False)
        write_markdown(s2, s2p)
        summary["attractors"] = s2.get("attractors")
        log(f"  [analysed] {cond.name} (judge parse_ok={s2['parse_ok']})")
    except Exception:
        log(f"  [analysis FAIL] {cond.name}\n{traceback.format_exc()}")
    return summary


def main() -> None:
    p = argparse.ArgumentParser(description="Parallel model-family attractor sweep.")
    p.add_argument("--dry-run", action="store_true", help="print the plan and exit (no API calls)")
    p.add_argument("--concurrency", type=int, default=16, help="global concurrent runs (API throughput)")
    p.add_argument("--analysis-concurrency", type=int, default=6, help="concurrent stage-2 judge calls")
    p.add_argument("--max-turns", type=int, default=30)
    p.add_argument("--seeds", type=int, default=1, help="repetitions per prompt")
    p.add_argument("--models", default=None, help="comma-separated model override (default: all 9)")
    p.add_argument("--judge", default=characterize.JUDGE_MODEL,
                   help="fixed judge model for stage-2 characterization across ALL conditions "
                        f"(default {characterize.JUDGE_MODEL}; e.g. openai/gpt-5.4)")
    p.add_argument("--no-judge", action="store_true",
                   help="skip stage-2 (the expensive judge); generate + stage-1 + transcript .md only. "
                        "Run the judge later with run_judge.py.")
    p.add_argument("--output-dir", default="results")
    args = p.parse_args()

    models = [m.strip() for m in args.models.split(",")] if args.models else MODELS
    conditions = build_conditions(models, args.max_turns, args.seeds, args.output_dir)
    tasks = build_tasks(conditions)
    total_turns = sum(len(SEED_PROMPTS[c.cfg.seed_prompt_set]) * c.cfg.seeds * c.cfg.max_turns for c in conditions)

    log(f"PLAN: {len(REGIMES)} regimes x {len(models)} models x {len(MODES)} modes "
        f"= {len(conditions)} conditions; {len(tasks)} runs x {args.max_turns} turns "
        f"(~{total_turns} model calls). concurrency={args.concurrency}; judge={args.judge}")
    for system_key, seed_set in REGIMES:
        log(f"  regime: {system_key} + {seed_set} ({len(SEED_PROMPTS[seed_set])} prompts)")
    if args.dry_run:
        log("DRY RUN — no API calls made.")
        return

    providers._get_client()  # pre-init the shared client before threads (avoid init race)

    log(f"=== running {len(tasks)} runs across {len(conditions)} conditions ===")
    with cf.ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        for fut in cf.as_completed([ex.submit(run_task, t) for t in tasks]):
            fut.result()  # exceptions handled inside run_task

    judge = None if args.no_judge else args.judge
    log(f"=== analysing {len(conditions)} conditions === (judge={'SKIPPED' if judge is None else judge})")
    summaries = []
    with cf.ThreadPoolExecutor(max_workers=args.analysis_concurrency) as ex:
        for fut in cf.as_completed([ex.submit(analyse, c, judge) for c in conditions]):
            summaries.append(fut.result())

    log("==== SUMMARY (attractors per condition) ====")
    for s in sorted(summaries, key=lambda x: x["name"]):
        labels = ", ".join(f"{a.get('label')} ({a.get('fraction_of_runs')})" for a in (s["attractors"] or [])) or "—"
        log(f"  {s['name']}: {labels}")
    log("MATRIX RUN DONE")


if __name__ == "__main__":
    main()
