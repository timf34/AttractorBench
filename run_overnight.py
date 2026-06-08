"""Overnight orchestration: run the AI-to-AI configs, then stage-1 + stage-2 analysis + .md.

Robust by design — one experiment or analysis step failing is logged and the rest continue.
The runner already saves after every completed run, so partial progress always survives.

    nohup caffeinate -is ./.venv/bin/python run_overnight.py > overnight.log 2>&1 &
    tail -f overnight.log
"""

import json
import traceback
from datetime import datetime

from attractorbench.runner import load_config, run_experiment
from attractorbench.analysis import deterministic, characterize
from attractorbench.render import write_markdown

CONFIGS = [
    "configs/ai2ai_self_append.py",
    "configs/ai2ai_two_instance.py",
]


def stamp(msg: str) -> None:
    print(f"[{datetime.now().isoformat(timespec='seconds')}] {msg}", flush=True)


def analyse(condition_path: str) -> dict | None:
    cond = json.load(open(condition_path))
    summary = {"condition": condition_path}

    # Stage 1 — deterministic (free)
    try:
        s1 = deterministic.analyse_condition(cond)
        s1_path = deterministic._output_path(condition_path)
        json.dump(s1, open(s1_path, "w"), indent=2, ensure_ascii=False)
        write_markdown(s1, s1_path)
        stamp(f"  stage1 -> {s1_path}")
    except Exception:
        stamp(f"  stage1 FAILED for {condition_path}\n{traceback.format_exc()}")

    # Stage 2 — LLM judge
    try:
        s2 = characterize.characterize_condition(cond)
        s2_path = characterize._output_path(condition_path)
        json.dump(s2, open(s2_path, "w"), indent=2, ensure_ascii=False)
        write_markdown(s2, s2_path)
        stamp(f"  stage2 -> {s2_path}  (parse_ok={s2['parse_ok']})")
        summary["attractors"] = s2.get("attractors")
    except Exception:
        stamp(f"  stage2 FAILED for {condition_path}\n{traceback.format_exc()}")
    return summary


def main() -> None:
    stamp("OVERNIGHT RUN START")
    all_summaries = []
    for cfg_path in CONFIGS:
        stamp(f"==== {cfg_path} ====")
        try:
            cfg = load_config(cfg_path)
            paths = run_experiment(cfg)
        except Exception:
            stamp(f"EXPERIMENT FAILED: {cfg_path}\n{traceback.format_exc()}")
            continue
        for p in paths:
            stamp(f"analysing {p}")
            all_summaries.append(analyse(p))

    stamp("==== SUMMARY ====")
    for s in all_summaries:
        stamp(f"{s['condition']}")
        for a in (s.get("attractors") or []):
            stamp(f"    [{a.get('fraction_of_runs')}] {a.get('label')} — {a.get('one_line')}")
    stamp("OVERNIGHT RUN DONE")


if __name__ == "__main__":
    main()
