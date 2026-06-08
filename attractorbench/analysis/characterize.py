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
from ..characterization import (
    CHARACTERIZATION_PROMPT_VERSION,
    JUDGE_MODEL,
    CharacterizationPrompt,
    OverallCharacterizationPrompt,
)
from ..prompts import TRANSCRIPT_FORMAT, serialize_run_for_judge, serialize_turns_for_judge

OVERALL_LAST_N_TURNS = 8   # tail length sampled per conversation for the OVERALL judge

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


def _extract_tag_lenient(text: str, tag: str) -> str | None:
    """Like _extract_tag but tolerates a missing closing tag (models often drop it on the LAST
    block) by falling back to open-tag-through-end-of-text."""
    closed = _extract_tag(text, tag)
    if closed is not None:
        return closed
    m = re.search(rf"<{tag}>(.*)", text, flags=re.DOTALL)
    return m.group(1).strip() if m else None


def _parse_bullets(block: str | None) -> list[str]:
    """Lines in a tag, each optionally a '- ' / '* ' / '• ' bullet, with surrounding quotes stripped."""
    if not block:
        return []
    out = []
    for line in block.splitlines():
        s = line.strip()
        if not s:
            continue
        if s[0] in "-*•":
            s = s[1:].strip()
        out.append(s.strip().strip('"').strip("“”").strip())
    return [s for s in out if s]


def _parse_fraction(raw: str | None, n_sampled: int) -> tuple[int | None, int | None, float | None]:
    """Parse the judge's run count and normalise the denominator to the KNOWN sampled count.

    The judge sometimes mis-states the denominator (e.g. "3 of 4" when 5 were shown), so we take
    only its numerator and divide by n_sampled (authoritative). Returns (count, n_sampled, ratio).
    """
    if not raw or not n_sampled:
        return None, None, None
    m = re.search(r"(\d+)", raw)  # first integer = how many runs hit this attractor
    if not m:
        return None, None, None
    num = max(0, min(int(m.group(1)), n_sampled))  # clamp into [0, n_sampled]
    return num, n_sampled, num / n_sampled


def _parse_attractor_block(b: str, n_sampled: int, is_primary: bool) -> dict | None:
    """Parse one attractor's inner tags; None if it has no label (e.g. empty primary block)."""
    label = _extract_tag(b, "label")
    if not label:
        return None
    frac_raw = _extract_tag(b, "fraction")
    num, den, ratio = _parse_fraction(frac_raw, n_sampled)
    return {
        "label": label,
        "trajectory": _extract_tag(b, "trajectory"),
        "one_line": _extract_tag(b, "one_line"),
        "terminal_form": _parse_bullets(_extract_tag(b, "terminal_form")),
        "fraction_raw": frac_raw,
        "fraction_count": num,
        "fraction_denom": den,
        "fraction_of_runs": ratio,
        "is_primary": is_primary,
    }


def _parse_attractors(text: str, n_sampled: int) -> tuple[dict | None, list, bool]:
    """Parse <primary_attractor> + <other_attractors>. Returns (primary, secondary_list, found).

    `found` is False only if the <primary_attractor> tag is missing entirely (a parse failure).
    An empty primary block (no shared attractor) is a VALID result -> primary=None.
    """
    primary_block = _extract_tag(text, "primary_attractor")
    if primary_block is None:
        return None, [], False
    primary = _parse_attractor_block(primary_block, n_sampled, is_primary=True)
    secondary = []
    others_block = _extract_tag(text, "other_attractors") or ""
    for b in re.findall(r"<attractor>(.*?)</attractor>", others_block, flags=re.DOTALL):
        a = _parse_attractor_block(b, n_sampled, is_primary=False)
        if a:
            secondary.append(a)
    return primary, secondary, True


def _judge(system: str, user: str, judge_model: str, n_items: int) -> dict:
    """Call the judge and parse its tagged output. Shared by per-condition and overall judges."""
    messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
    raw, _ = providers.chat(
        judge_model, messages, JUDGE_TEMPERATURE, 1.0, JUDGE_MAX_TOKENS, JUDGE_REASONING_EFFORT
    )
    characterization = _extract_tag_lenient(raw, "characterization")
    primary, secondary, found = _parse_attractors(raw, n_items)
    parse_ok = bool(characterization) and found
    attractors = ([primary] if primary else []) + secondary  # primary first, for tables/aggregation
    return {
        "judge_model": judge_model,
        "prompt_version": CHARACTERIZATION_PROMPT_VERSION,
        "analyzed_at": datetime.now(timezone.utc).isoformat(),
        "characterization": characterization,
        "primary_attractor": primary,
        "attractors": attractors,
        "parse_ok": parse_ok,
        "raw": None if parse_ok else raw,  # keep full response on any parse failure
    }


def characterize_condition(
    condition: dict,
    judge_model: str = JUDGE_MODEL,
    token_budget: int = JUDGE_CONTEXT_TOKEN_BUDGET,
) -> dict:
    """Per-condition judge over FULL transcripts of one grouping (detail page)."""
    runs = condition.get("runs", [])
    sampled, blocks = select_transcripts(runs, token_budget=token_budget)
    transcripts = TRANSCRIPT_FORMAT.run_separator.join(blocks)
    user = CharacterizationPrompt().build(
        n_items=len(sampled),
        condition_description=_condition_description(condition),
        transcripts=transcripts,
    )
    result = {
        "scope": "condition",
        "experiment_name": condition.get("experiment_name"),
        "mode": condition.get("mode"),
        "model_a": condition.get("model_a"),
        "model_b": condition.get("model_b"),
        "system_prompt_key": condition.get("system_prompt_key"),
        "seed_prompt_set": condition.get("seed_prompt_set"),
        "temperature": condition.get("temperature"),
        "n_runs_total": len(runs),
        "n_runs_sampled": len(sampled),
        "sampled_run_indices": sorted(r["run_index"] for r in sampled),
    }
    result.update(_judge(CharacterizationPrompt().system, user, judge_model, len(sampled)))
    return result


# ---------------------------------------------------------------------------
# Overall judge — the LAST N turns of MANY of a model's conversations.
# ---------------------------------------------------------------------------
def _tail_run(run: dict, last_n: int) -> dict:
    """A shallow copy of a run keeping only its final `last_n` turns."""
    return {**run, "turns": run.get("turns", [])[-last_n:]}


def select_tails(
    conditions: list[dict],
    last_n: int = OVERALL_LAST_N_TURNS,
    token_budget: int = JUDGE_CONTEXT_TOKEN_BUDGET,
) -> tuple[list[dict], list[str], int]:
    """Pool the last `last_n` turns of every run across the given conditions, shuffle (fixed seed),
    and greedily pack as many tails as fit the budget. Returns (sampled_runs, blocks, total_runs)."""
    tails = []
    for cond in conditions:
        for run in cond.get("runs", []):
            t = _tail_run(run, last_n)
            label = f"{cond.get('system_prompt_key')} | {cond.get('mode')} | seed {run.get('seed_prompt_index')}"
            block = f"--- {label} ---\n" + serialize_turns_for_judge(t["turns"])
            tails.append((t, block))
    total = len(tails)
    order = list(range(total))
    random.Random(SAMPLING_SEED).shuffle(order)
    sampled, blocks, used = [], [], 0
    for i in order:
        run, block = tails[i]
        cost = _estimate_tokens(block)
        if sampled and used + cost > token_budget:
            continue
        sampled.append(run)
        blocks.append(block)
        used += cost
    return sampled, blocks, total


def characterize_overall(
    conditions: list[dict],
    scope_description: str,
    judge_model: str = JUDGE_MODEL,
    last_n: int = OVERALL_LAST_N_TURNS,
    token_budget: int = JUDGE_CONTEXT_TOKEN_BUDGET,
) -> dict:
    """Overall judge over the tails of many of a model's conversations (homepage / per-framing)."""
    sampled, blocks, total = select_tails(conditions, last_n=last_n, token_budget=token_budget)
    transcripts = TRANSCRIPT_FORMAT.run_separator.join(blocks)
    user = OverallCharacterizationPrompt().build(
        n_items=len(sampled), scope_description=scope_description, transcripts=transcripts
    )
    result = {
        "scope": "overall",
        "scope_description": scope_description,
        "last_n_turns": last_n,
        "n_convos_total": total,
        "n_convos_sampled": len(sampled),
    }
    result.update(_judge(OverallCharacterizationPrompt().system, user, judge_model, len(sampled)))
    return result


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
