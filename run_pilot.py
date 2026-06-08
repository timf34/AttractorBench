"""Pilot: 3 reps x 20 turns for self_append and two_instance, then stage1 + stage2 analysis.

Run:  ./.venv/bin/python run_pilot.py
"""

from attractorbench.config import RunConfig
from attractorbench.runner import run_experiment
from attractorbench.analysis.deterministic import analyse_condition
from attractorbench.analysis.characterize import characterize_condition
import json

common = dict(seed_prompt_set="smoke_v1", seeds=3, max_turns=20, max_new_tokens=2048,
              reasoning_effort="low", temperature=1.0, top_p=1.0, max_workers=3, output_dir="results")

configs = [
    RunConfig(experiment_name="pilot_self_append", mode="self_append",
              model_a="openai/gpt-5.2", system_prompt_key="helpful_assistant",
              continuation_style="passthrough", **common),
    RunConfig(experiment_name="pilot_two_instance", mode="two_instance",
              model_a="openai/gpt-5.2", model_b="openai/gpt-5.2",
              system_prompt_key="ai_to_ai_self_aware", **common),
]

for cfg in configs:
    print(f"\n########## RUN: {cfg.experiment_name} ##########", flush=True)
    paths = run_experiment(cfg)
    for path in paths:
        cond = json.load(open(path))
        nturns = [len(r["turns"]) for r in cond["runs"]]
        print(f"[{cfg.experiment_name}] runs={len(cond['runs'])} turns_per_run={nturns}", flush=True)

        # stage 1 (free)
        s1 = analyse_condition(cond)
        json.dump(s1, open(path.replace(".json", "").replace("results/", "results/") + "__stage1_inline.json", "w"), indent=2, ensure_ascii=False)
        for r in s1["runs"]:
            c = r["convergence"]
            print(f"  run {r['run_index']}: jaccard_slope={c['jaccard_slope']:.4f} "
                  f"lev_slope={c['norm_levenshtein_slope']:.4f} ttr_slope={r['ttr_decay_slope']:.4f} "
                  f"exact_loop@{r['verbatim_loops']['first_exact_repeat_turn']} "
                  f"near_pairs={len(r['verbatim_loops']['near_exact_pairs'])}", flush=True)
        print(f"  TOP WORDS: {s1['condition_word_frequency'][:12]}", flush=True)
        print(f"  TOP EMOJI: {s1['condition_emoji_frequency'][:8]}", flush=True)

        # stage 2 (judge)
        s2 = characterize_condition(cond)
        print(f"  JUDGE parse_ok={s2['parse_ok']} sampled={s2['n_runs_sampled']}/{s2['n_runs_total']}", flush=True)
        print(f"  ATTRACTORS: {s2['attractors']}", flush=True)
        ch = (s2['characterization'] or '')[:600]
        print(f"  CHARACTERIZATION[:600]: {ch}", flush=True)

print("\n########## PILOT DONE ##########", flush=True)
