"""Stage 2 — LLM-judge characterization.

Dumps a condition's transcripts into a judge model with the characterization prompt and parses
its two tagged blocks. The judge is given NO preset attractor categories — it coins its own
labels. Transcripts are fed WHOLE and untruncated; to fit the judge context we randomly SAMPLE
as many complete transcripts as fit (fixed seed, reproducible) rather than truncating within a
transcript. Because the judge's fraction_of_runs is then over the sampled set, we record
n_runs_sampled / n_runs_total / sampled_run_indices so the correct denominator is available when
aggregating across conditions.

    python -m attractorbench.analysis.characterize results/<exp>/<condition>.json [--judge openai/gpt-5.2]
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
from datetime import datetime, timezone

from .. import providers
from ..characterization import JUDGE_MODEL, CharacterizationPrompt
from ..prompts import TRANSCRIPT_FORMAT, serialize_run_for_judge

# --- tunable constants (named, not buried) ----------------------------------
JUDGE_CONTEXT_TOKEN_BUDGET = 120_000   # token ceiling the sampler fills with WHOLE transcripts
SAMPLING_SEED = 1234                    # fixed so re-running stage 2 picks the same transcripts
# The judge (gpt-5.4) is a reasoning model: max_tokens covers hidden reasoning + the visible
# write-up, so it needs generous room or it truncates its own JSON. low effort keeps most of the
# budget for output (reasoning_effort is auto-dropped for non-reasoning judges like gpt-4o).
JUDGE_MAX_TOKENS = 8000
JUDGE_REASONING_EFFORT = "low"
JUDGE_TEMPERATURE = 1.0


def _estimate_tokens(text: str) -> int:
    """Cheap, dependency-free token estimate (~4 chars/token)."""
    return len(text) // 4


def select_transcripts(
    runs: list[dict], token_budget: int = JUDGE_CONTEXT_TOKEN_BUDGET
) -> tuple[list[dict], list[str]]:
    """Greedily select WHOLE transcripts (shuffled with SAMPLING_SEED) until the budget is hit.

    Never truncates within a transcript. Returns (sampled_runs, serialized_blocks) in the order
    they will be shown to the judge.
    """
    rendered = [(r, serialize_run_for_judge(r)) for r in runs]
    order = list(range(len(rendered)))
    random.Random(SAMPLING_SEED).shuffle(order)

    sampled: list[dict] = []
    blocks: list[str] = []
    used = 0
    for i in order:
        run, text = rendered[i]
        cost = _estimate_tokens(text)
        if sampled and used + cost > token_budget:
            continue  # skip this whole transcript; keep trying smaller ones still in the order
        sampled.append(run)
        blocks.append(text)
        used += cost
    return sampled, blocks


def _condition_description(condition: dict) -> str:
    return (
        f"mode={condition.get('mode')}, model_a={condition.get('model_a')}, "
        f"model_b={condition.get('model_b')}, temperature={condition.get('temperature')}, "
        f"system_prompt_key={condition.get('system_prompt_key')}, "
        f"seed_prompt_set={condition.get('seed_prompt_set')}"
    )


def _extract_tag(text: str, tag: str) -> str | None:
    m = re.search(rf"<{tag}>(.*?)</{tag}>", text, flags=re.DOTALL)
    return m.group(1).strip() if m else None


def _parse_attractors(raw_block: str | None) -> tuple[list | None, bool]:
    """Defensive parse: strip to the first [...] then json.loads. Never raises."""
    if not raw_block:
        return None, False
    start, end = raw_block.find("["), raw_block.rfind("]")
    if start == -1 or end == -1 or end < start:
        return None, False
    try:
        parsed = json.loads(raw_block[start : end + 1])
        return parsed, isinstance(parsed, list)
    except json.JSONDecodeError:
        return None, False


def characterize_condition(condition: dict, judge_model: str = JUDGE_MODEL) -> dict:
    runs = condition.get("runs", [])
    sampled, blocks = select_transcripts(runs)
    transcripts = TRANSCRIPT_FORMAT.run_separator.join(blocks)

    prompt = CharacterizationPrompt()
    user = prompt.build(
        n_runs=len(sampled),
        condition_description=_condition_description(condition),
        transcripts=transcripts,
    )
    messages = [{"role": "system", "content": prompt.system}, {"role": "user", "content": user}]
    raw = providers.chat(
        judge_model, messages, JUDGE_TEMPERATURE, 1.0, JUDGE_MAX_TOKENS, JUDGE_REASONING_EFFORT
    )

    characterization = _extract_tag(raw, "characterization")
    attractors_block = _extract_tag(raw, "attractors_json")
    attractors, parse_ok = _parse_attractors(attractors_block)

    return {
        "experiment_name": condition.get("experiment_name"),
        "mode": condition.get("mode"),
        "model_a": condition.get("model_a"),
        "model_b": condition.get("model_b"),
        "temperature": condition.get("temperature"),
        "judge_model": judge_model,
        "prompt_version": prompt.version,
        "analyzed_at": datetime.now(timezone.utc).isoformat(),
        "n_runs_total": len(runs),
        "n_runs_sampled": len(sampled),
        "sampled_run_indices": sorted(r["run_index"] for r in sampled),
        "characterization": characterization,
        "attractors": attractors,
        "parse_ok": parse_ok,
        # On any parse failure, keep the raw block / full response so nothing is lost.
        "raw_attractors_block": None if parse_ok else attractors_block,
        "raw": None if (characterization and parse_ok) else raw,
    }


def _output_path(condition_path: str) -> str:
    d = os.path.dirname(condition_path)
    base = os.path.splitext(os.path.basename(condition_path))[0]
    out_dir = os.path.join(d, "analysis")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, f"{base}__stage2.json")


def main() -> None:
    parser = argparse.ArgumentParser(description="Stage-2 LLM-judge characterization.")
    parser.add_argument("condition", help="Path to a condition JSON written by the runner")
    parser.add_argument("--judge", default=JUDGE_MODEL, help="judge model (provider-prefixed)")
    args = parser.parse_args()

    with open(args.condition, encoding="utf-8") as f:
        condition = json.load(f)
    result = characterize_condition(condition, judge_model=args.judge)
    out = _output_path(args.condition)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    from ..render import write_markdown
    md = write_markdown(result, out)
    flag = "ok" if result["parse_ok"] else "PARSE FAILED (raw kept)"
    print(f"Wrote {out}  (sampled {result['n_runs_sampled']}/{result['n_runs_total']}, attractors {flag})")
    print(f"Wrote {md}")


if __name__ == "__main__":
    main()
