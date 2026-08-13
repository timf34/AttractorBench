"""The single runner: load a RunConfig + prompts, dispatch by mode, sweep temperatures,
parallelise across the seed-prompt x repetition cross product, and save incrementally.

    python -m attractorbench.runner --config configs/gpt52_self_append.py
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

from .config import RunConfig
from .harnesses import run_cross_model, run_self_append, run_two_instance
from .prompts import SEED_PROMPTS, build_system_prompt
from .render import write_markdown

_HARNESSES = {
    "self_append": run_self_append,
    "two_instance": run_two_instance,
    "cross_model": run_cross_model,
}


def load_config(path: str) -> RunConfig:
    """Load a config module from a file path; it must expose a ``CONFIG`` RunConfig."""
    spec = importlib.util.spec_from_file_location("ab_config", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load config from {path!r}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    cfg = getattr(module, "CONFIG", None)
    if not isinstance(cfg, RunConfig):
        raise RuntimeError(f"{path!r} must define CONFIG = RunConfig(...)")
    return cfg


def validate(cfg: RunConfig) -> None:
    if cfg.memory_mode == "compressed":
        raise NotImplementedError(
            "memory_mode='compressed' is a stub seam — not implemented in v1 (full only)."
        )
    if cfg.memory_mode == "last_message_only" and cfg.mode != "self_append":
        raise ValueError("memory_mode='last_message_only' only applies to mode='self_append'")
    if cfg.mode not in _HARNESSES:
        raise ValueError(f"Unknown mode {cfg.mode!r}")
    if cfg.mode == "self_append" and cfg.system_prompt_key.startswith("ai_to_ai"):
        # A lone model fed an "another AI" framing ventriloquizes both sides of an imagined
        # dialogue — neither clean self-talk nor clean dialogue (found empirically; see notes.md).
        raise ValueError(
            "self_append must not use an ai_to_ai_* system prompt (the model role-plays both "
            "sides). Use 'self_monologue' or 'helpful_assistant'."
        )
    if cfg.mode == "cross_model":
        if not cfg.model_b:
            raise ValueError("cross_model requires model_b")
        if cfg.model_b == cfg.model_a:
            raise ValueError("cross_model requires model_a != model_b (use two_instance instead)")
    if cfg.mode == "self_append" and cfg.model_b is not None:
        print(f"  [warn] self_append ignores model_b (got {cfg.model_b!r})")
    if cfg.seed_prompt_set not in SEED_PROMPTS:
        raise ValueError(f"Unknown seed_prompt_set {cfg.seed_prompt_set!r}")


def _model_slug(model: str) -> str:
    """'openai/gpt-5.2' -> 'gpt-5.2'  (drop provider prefix, sanitise any remaining '/')."""
    return model.split("/", 1)[-1].replace("/", "-")


def _condition_basename(cfg: RunConfig, temperature: float) -> str:
    """Descriptive, config-keyed name: different model(s)/prompts never collide; identical
    configs map to the same name (so a re-run is recognised as the same experiment)."""
    models = _model_slug(cfg.model_a)
    if cfg.model_b and cfg.model_b != cfg.model_a:
        models += f"_x_{_model_slug(cfg.model_b)}"
    # Non-default memory modes are part of the condition identity (e.g. self_append_lastmsg).
    mem_tag = {"last_message_only": "_lastmsg", "compressed": "_compact"}.get(cfg.memory_mode, "")
    return f"{cfg.mode}{mem_tag}__{models}__{cfg.system_prompt_key}__{cfg.seed_prompt_set}__temp{temperature}"


def _condition_path(cfg: RunConfig, temperature: float) -> str:
    """Resolve the output path once per condition. If a file from a prior IDENTICAL-config run
    already exists, write the new run to a timestamped sibling instead of clobbering it."""
    out_dir = os.path.join(cfg.output_dir, cfg.experiment_name)
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, _condition_basename(cfg, temperature) + ".json")
    if os.path.exists(base):
        ts = datetime.now().strftime("%Y-%m-%dT%H%M%S")
        alt = os.path.join(out_dir, _condition_basename(cfg, temperature) + f"__{ts}.json")
        print(f"  [no-clobber] {os.path.basename(base)} exists; writing {os.path.basename(alt)} (old kept)")
        return alt
    return base


def _save_condition(
    path: str, cfg: RunConfig, temperature: float, system_prompt: str, runs: list[dict]
) -> None:
    payload = {
        "experiment_name": cfg.experiment_name,
        "mode": cfg.mode,
        "model_a": cfg.model_a,
        "model_b": cfg.model_b,
        "system_prompt_key": cfg.system_prompt_key,
        "system_prompt": system_prompt,   # resolved text actually sent (incl. early-end clause)
        # B's OWN system prompt when it differs from A's (asymmetric setups like the
        # user-simulator control) — replay/projection rebuilds B's view from this.
        "system_prompt_key_b": cfg.system_prompt_key_b,
        "system_prompt_b": (
            build_system_prompt(cfg.system_prompt_key_b, cfg.allow_early_end)
            if cfg.system_prompt_key_b is not None else None
        ),
        "memory_mode": cfg.memory_mode,
        "continuation_style": cfg.continuation_style,
        "allow_early_end": cfg.allow_early_end,
        "seed_prompt_set": cfg.seed_prompt_set,
        "temperature": temperature,
        # Mid-run switch record — written for EVERY unsteer family (pvec/prompt/lora).
        # Without it the per-turn `model` field is the only trace of the switch, and for
        # prompt-unsteer runs even that never changes.
        **({
            "switch_turn": cfg.switch_turn,
            "model_a_post": cfg.model_a_post,
            "model_b_post": cfg.model_b_post,
            "system_prompt_key_post": cfg.system_prompt_key_post,
            "system_prompt_post": (
                build_system_prompt(cfg.system_prompt_key_post, cfg.allow_early_end)
                if cfg.system_prompt_key_post is not None else None
            ),
        } if cfg.switch_turn is not None else {}),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "runs": sorted(runs, key=lambda r: r["run_index"]),
    }
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    os.replace(tmp, path)  # atomic-ish: a crash mid-write never corrupts the saved file


def run_condition(cfg: RunConfig, system_prompt: str, temperature: float) -> str:
    """Run one temperature condition: cross product of seed prompts x repetitions."""
    harness = _HARNESSES[cfg.mode]
    prompts = SEED_PROMPTS[cfg.seed_prompt_set]

    # Build the cross-product job list. run_index is a global counter; seed_prompt_index and
    # repetition are recorded so analysis can separate reproducibility from prompt variation.
    jobs = []
    run_index = 0
    for seed_prompt_index, prompt in enumerate(prompts):
        for repetition in range(cfg.seeds):
            jobs.append(
                {
                    "run_index": run_index,
                    "seed_prompt": prompt,
                    "seed_prompt_index": seed_prompt_index,
                    "repetition": repetition,
                }
            )
            run_index += 1

    path = _condition_path(cfg, temperature)
    print(f"[{cfg.experiment_name}] mode={cfg.mode} temp={temperature} -> {len(jobs)} runs -> {path}")

    runs: list[dict] = []
    with ThreadPoolExecutor(max_workers=cfg.max_workers) as executor:
        future_to_job = {
            executor.submit(
                harness, cfg, system_prompt, job["seed_prompt"], job["run_index"], temperature
            ): job
            for job in jobs
        }
        for future in as_completed(future_to_job):
            job = future_to_job[future]
            try:
                run = future.result()
            except Exception as e:  # noqa: BLE001 — one worker failing must not lose the rest
                print(f"  [run {job['run_index']}] FAILED: {type(e).__name__}: {e}")
                continue
            # Inject the cross-product coordinates onto the harness's run dict.
            run["seed_prompt_index"] = job["seed_prompt_index"]
            run["repetition"] = job["repetition"]
            runs.append(run)
            _save_condition(path, cfg, temperature, system_prompt, runs)  # incremental crash-safety
            print(f"  [run {run['run_index']}] done ({len(run['turns'])} turns) — saved {len(runs)}/{len(jobs)}")

    # Readable transcript .md alongside the JSON (re-read the final, sorted payload).
    with open(path, encoding="utf-8") as f:
        md_path = write_markdown(json.load(f), path)
    print(f"  wrote {md_path}")
    return path


def run_experiment(cfg: RunConfig) -> list[str]:
    validate(cfg)
    system_prompt = build_system_prompt(cfg.system_prompt_key, cfg.allow_early_end)
    temps = cfg.temperature_sweep or [cfg.temperature]
    return [run_condition(cfg, system_prompt, t) for t in temps]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run an AttractorBench experiment.")
    parser.add_argument("--config", required=True, help="Path to a config file defining CONFIG = RunConfig(...)")
    args = parser.parse_args()
    cfg = load_config(args.config)
    paths = run_experiment(cfg)
    print("\nWrote condition files:")
    for p in paths:
        print(f"  {p}")


if __name__ == "__main__":
    main()
