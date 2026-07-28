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
from .prompts import CONTINUATION_NUDGES, END_SENTINEL, build_system_prompt, serialize_self_append

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


def _ctx_full(run: dict, turn: int, exc: Exception) -> bool:
    """A conversation that has FILLED the model's context window is complete, not failed — some
    personas (borderline-coherence steering) write turns so long that by turn ~8 the messages
    alone exceed the window and no request can fit. Keep the transcript and end the run here
    rather than losing it to a FAILED run."""
    if "maximum context length" not in str(exc):
        return False
    run["ended_early"] = True
    run["ended_at_turn"] = turn
    run["ended_reason"] = "context_full"
    print(f"    [run {run['run_index']} turn {turn}] context window full — ending conversation "
          f"({turn - 1} turns kept)")
    return True


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
    # used by message_list transport; "" => omit the system message (see run_two_instance)
    messages = [{"role": "system", "content": system_prompt}] if system_prompt else []

    for turn in range(1, cfg.max_turns + 1):
        if SELF_APPEND_TRANSPORT == "serialized_string":
            # Single growing context fed back as ONE user message (no role-swap). Turn 1 is the
            # bare seed; later turns are seed + the model's own accumulated output.
            # memory_mode="last_message_only" is the no-memory baseline: identical except the
            # model sees only its OWN LAST turn (seed kept, so history depth is the only delta).
            if not contents:
                user_content = seed_prompt
            else:
                visible = contents[-1:] if cfg.memory_mode == "last_message_only" else contents
                user_content = seed_prompt + "\n\n" + serialize_self_append(visible)
                if cfg.continuation_style == "nudge":
                    user_content += "\n\n" + nudge
            call_messages = ([{"role": "system", "content": system_prompt}] if system_prompt else []) + [
                {"role": "user", "content": user_content},
            ]
        elif SELF_APPEND_TRANSPORT == "message_list":
            # Seam (probe-disfavoured): grow one messages list ending on an assistant turn.
            if cfg.memory_mode == "last_message_only":
                raise NotImplementedError(
                    "memory_mode='last_message_only' is only implemented for the "
                    "serialized_string transport"
                )
            if turn == 1:
                messages.append({"role": "user", "content": seed_prompt})
            elif cfg.continuation_style == "nudge":
                messages.append({"role": "user", "content": nudge})
            call_messages = messages
        else:
            raise ValueError(f"Unknown SELF_APPEND_TRANSPORT {SELF_APPEND_TRANSPORT!r}")

        try:
            reply, finish = providers.chat(
                cfg.model_a, call_messages, temperature, cfg.top_p, cfg.max_new_tokens, cfg.reasoning_effort
            )
        except RuntimeError as e:
            if _ctx_full(run, turn, e):
                break
            raise
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
    system_prompt_b: str | None = None,
) -> dict:
    run = _new_run(run_index, seed_prompt)
    # system_prompt "" (key "none") => NO system message at all (not an empty one): matches the
    # assistant-axis paper's setup and keeps Gemma-2 (whose template rejects system roles) servable.
    # system_prompt_b (None => same as A) lets asymmetric setups give each side its own framing,
    # e.g. the user-simulator control: A = auditor role-playing a human, B = bare target model.
    sys_b = system_prompt if system_prompt_b is None else system_prompt_b
    a_history = ([{"role": "system", "content": system_prompt}] if system_prompt else []) + [
        {"role": "user", "content": seed_prompt}
    ]
    b_history = [{"role": "system", "content": sys_b}] if sys_b else []

    for turn in range(1, cfg.max_turns + 1):
        is_a = (turn % 2) == 1
        speaker, model = ("A", model_a) if is_a else ("B", model_b)
        # Mid-run model switch (steering-removal experiments): after switch_turn total
        # messages, each side routes to its *_post model. The recorded per-turn `model`
        # field keeps the actual generator, so transcripts show exactly where the switch hit.
        if cfg.switch_turn is not None and turn > cfg.switch_turn:
            post = cfg.model_a_post if is_a else cfg.model_b_post
            if post:
                model = post
        history = a_history if is_a else b_history
        other = b_history if is_a else a_history

        try:
            reply, finish = providers.chat(model, history, temperature, cfg.top_p, cfg.max_new_tokens, cfg.reasoning_effort)
        except RuntimeError as e:
            if _ctx_full(run, turn, e):
                break
            raise
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
        cfg, system_prompt, seed_prompt, run_index, temperature, cfg.model_a, model_b,
        system_prompt_b=_resolve_system_prompt_b(cfg),
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
        cfg, system_prompt, seed_prompt, run_index, temperature, cfg.model_a, cfg.model_b,
        system_prompt_b=_resolve_system_prompt_b(cfg),
    )


def _resolve_system_prompt_b(cfg: RunConfig) -> str | None:
    """B's resolved system prompt, or None when B shares A's (the default)."""
    if cfg.system_prompt_key_b is None:
        return None
    return build_system_prompt(cfg.system_prompt_key_b, cfg.allow_early_end)
