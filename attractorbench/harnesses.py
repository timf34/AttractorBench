"""The three harness modes. Each is a genuinely different mechanic, not a parameter of one loop.

- ``run_self_append``   — single growing context, model continues its own transcript (novel).
- ``run_two_instance`` — same model, two role-swapped histories.
- ``run_cross_model``  — two different models, otherwise identical to two_instance.

Each returns one run dict:
    {run_index, seed_prompt, ended_early, ended_at_turn, turns: [...]}
with each turn = {turn, speaker, model, content, content_clean}.
"""

from __future__ import annotations

import re

from . import providers
from .config import RunConfig
from .prompts import CONTINUATION_NUDGES, END_SENTINEL, serialize_self_append

# ---------------------------------------------------------------------------
# strip_thinking — reused verbatim from the clone (olmo_local.py).
# ---------------------------------------------------------------------------
THINK_RE = re.compile(r"<think>.*?</think>\s*", flags=re.DOTALL)
THINK_OPEN_RE = re.compile(r"<think>.*", flags=re.DOTALL)


def strip_thinking(text: str) -> str:
    """Remove <think>...</think> blocks from model output.

    Also handles unclosed <think> tags (model ran out of tokens mid-thought).
    """
    result = THINK_RE.sub("", text)        # complete blocks (lazy)
    result = THINK_OPEN_RE.sub("", result)  # unclosed block (greedy)
    return result.strip()


# ---------------------------------------------------------------------------
# self_append transport — DECIDED BY THE STEP-0 PROBE (probe_transport.py), not assumed.
# Empirically, OpenAI Chat Completions RESTARTS an assistant-terminated list (gpt-5.2 re-answers
# the seed; gpt-5-mini returns empty) rather than continuing it, so "message_list" is unsuitable.
# "serialized_string" — feeding the running transcript back as one user message — produces a
# coherent continuing monologue. Re-run the probe if you switch target models.
# ---------------------------------------------------------------------------
SELF_APPEND_TRANSPORT = "serialized_string"  # "serialized_string" | "message_list"


def _new_run(run_index: int, seed_prompt: str) -> dict:
    return {
        "run_index": run_index,
        "seed_prompt": seed_prompt,
        "ended_early": False,
        "ended_at_turn": None,
        "turns": [],
    }


def _record_turn(
    run: dict, turn: int, speaker: str, model: str, content: str, finish_reason: str | None = None
) -> str:
    content_clean = strip_thinking(content)
    if finish_reason == "length":
        # Should be rare: the turn was still cut off at the provider's ceiling. Recorded in the
        # turn dict (finish_reason) so a run can be audited for any truncation.
        print(f"    [run {run['run_index']} turn {turn}] WARNING: {model} finish_reason=length "
              f"(turn truncated even at ceiling — content_len={len(content_clean)})")
    run["turns"].append(
        {
            "turn": turn,
            "speaker": speaker,
            "model": model,
            "content": content,
            "content_clean": content_clean,
            "finish_reason": finish_reason,
        }
    )
    return content_clean


def _hit_early_end(run: dict, turn: int, content_clean: str, allow_early_end: bool) -> bool:
    """Apply the early-end sentinel policy. Returns True iff the run should stop now."""
    if END_SENTINEL not in content_clean:
        return False
    if allow_early_end:
        run["ended_early"] = True
        run["ended_at_turn"] = turn
        return True
    # Real experimental variable: when not allowed, log but ignore the sentinel.
    print(f"    [run {run['run_index']} turn {turn}] end sentinel emitted but allow_early_end=False — ignoring")
    return False


# ---------------------------------------------------------------------------
# 1. self_append (the novel condition)
# ---------------------------------------------------------------------------
def run_self_append(
    cfg: RunConfig,
    system_prompt: str,
    seed_prompt: str,
    run_index: int,
    temperature: float,
) -> dict:
    if cfg.memory_mode == "compressed":
        raise NotImplementedError(
            "memory_mode='compressed' is a stub seam — only 'full' is implemented in v1. "
            "A compressed variant would condition on a running summary + recent turns."
        )

    run = _new_run(run_index, seed_prompt)
    nudge = CONTINUATION_NUDGES["default"]
    contents: list[str] = []          # the model's own growing transcript (content_clean)
    messages = [{"role": "system", "content": system_prompt}]  # used by message_list transport

    for turn in range(1, cfg.max_turns + 1):
        if SELF_APPEND_TRANSPORT == "serialized_string":
            # Single growing context fed back as ONE user message (no role-swap). Turn 1 is the
            # bare seed; later turns are seed + the model's own accumulated output.
            if not contents:
                user_content = seed_prompt
            else:
                user_content = seed_prompt + "\n\n" + serialize_self_append(contents)
                if cfg.continuation_style == "nudge":
                    user_content += "\n\n" + nudge
            call_messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ]
        elif SELF_APPEND_TRANSPORT == "message_list":
            # Seam (probe-disfavoured): grow one messages list ending on an assistant turn.
            if turn == 1:
                messages.append({"role": "user", "content": seed_prompt})
            elif cfg.continuation_style == "nudge":
                messages.append({"role": "user", "content": nudge})
            call_messages = messages
        else:
            raise ValueError(f"Unknown SELF_APPEND_TRANSPORT {SELF_APPEND_TRANSPORT!r}")

        reply, finish = providers.chat(
            cfg.model_a, call_messages, temperature, cfg.top_p, cfg.max_new_tokens, cfg.reasoning_effort
        )
        content_clean = _record_turn(run, turn, "A", cfg.model_a, reply, finish)
        contents.append(content_clean)
        if SELF_APPEND_TRANSPORT == "message_list":
            messages.append({"role": "assistant", "content": reply})

        if _hit_early_end(run, turn, content_clean, cfg.allow_early_end):
            break

    return run


# ---------------------------------------------------------------------------
# 2 & 3. two_instance / cross_model — one shared loop, differ only by which model speaks.
# ---------------------------------------------------------------------------
def _run_two_history(
    cfg: RunConfig,
    system_prompt: str,
    seed_prompt: str,
    run_index: int,
    temperature: float,
    model_a: str,
    model_b: str,
) -> dict:
    run = _new_run(run_index, seed_prompt)
    a_history = [{"role": "system", "content": system_prompt}, {"role": "user", "content": seed_prompt}]
    b_history = [{"role": "system", "content": system_prompt}]

    for turn in range(1, cfg.max_turns + 1):
        is_a = (turn % 2) == 1
        speaker, model = ("A", model_a) if is_a else ("B", model_b)
        history = a_history if is_a else b_history
        other = b_history if is_a else a_history

        reply, finish = providers.chat(model, history, temperature, cfg.top_p, cfg.max_new_tokens, cfg.reasoning_effort)
        history.append({"role": "assistant", "content": reply})
        other.append({"role": "user", "content": reply})  # the other instance hears it as user
        content_clean = _record_turn(run, turn, speaker, model, reply, finish)

        if _hit_early_end(run, turn, content_clean, cfg.allow_early_end):
            break

    return run


def run_two_instance(
    cfg: RunConfig,
    system_prompt: str,
    seed_prompt: str,
    run_index: int,
    temperature: float,
) -> dict:
    # Same model on both sides; model_b defaults to model_a if not given.
    model_b = cfg.model_b or cfg.model_a
    return _run_two_history(
        cfg, system_prompt, seed_prompt, run_index, temperature, cfg.model_a, model_b
    )


def run_cross_model(
    cfg: RunConfig,
    system_prompt: str,
    seed_prompt: str,
    run_index: int,
    temperature: float,
) -> dict:
    # cross_model is literally two_instance with model_a != model_b (validated in the runner).
    return _run_two_history(
        cfg, system_prompt, seed_prompt, run_index, temperature, cfg.model_a, cfg.model_b
    )
