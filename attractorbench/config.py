"""RunConfig — the single per-experiment config object (verbatim from SPEC.md).

One config drives one runner, which selects one of three harness modes. No per-experiment
script copies. Prompts are referenced by key into ``prompts.py`` / ``characterization.py``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass
class RunConfig:
    # identity
    experiment_name: str

    # harness
    mode: Literal["self_append", "two_instance", "cross_model"]

    # models (provider-prefixed, e.g. "openai/gpt-5.2" or "openrouter/x-ai/grok-4.1")
    model_a: str

    # conversation
    seed_prompt_set: str               # key into prompts.py SEED_PROMPTS
    system_prompt_key: str             # key into prompts.py SYSTEM_PROMPTS

    # full              = the model sees its whole history each turn
    # last_message_only = self_append only: system + seed + the model's OWN LAST turn (the
    #                     no-memory baseline — if attractors need accumulation, this should
    #                     not reach them). Seed is kept every turn so the ONLY difference
    #                     from "full" is history depth.
    # compressed        = stub for now (periodic self-summarization / compaction)
    memory_mode: Literal["full", "compressed", "last_message_only"] = "full"
    continuation_style: Literal["nudge", "passthrough"] = "passthrough"
    # nudge = append a fixed continuation message each turn (from prompts.py)
    # passthrough = feed the model's own last output back with no added scaffolding

    model_b: str | None = None         # required for two_instance / cross_model; None for self_append

    # Mid-conversation model switch (two_instance / cross_model): after turn `switch_turn`
    # (in TOTAL message count — A speaks odd turns, B even), route each side's calls to its
    # *_post model instead. Built for steering-removal experiments: model_a = the steered
    # variant, model_a_post = the unsteered base, switch_turn = k => steer only the first k
    # messages. None (default) = no switch; a side without a *_post keeps its original model.
    switch_turn: int | None = None
    model_a_post: str | None = None
    model_b_post: str | None = None

    max_turns: int = 50                # Anthropic uses up to 50
    allow_early_end: bool = False      # if True, model may emit the end sentinel to stop

    # sampling — LOAD-BEARING. low temp manufactures fake repetition-attractors.
    temperature: float = 1.0
    top_p: float = 1.0
    # OpenAI reasoning models (gpt-5 family) spend hidden reasoning tokens out of the SAME budget
    # as the visible reply. Their default ("medium") can consume the entire max_new_tokens on an
    # open-ended prompt and return an EMPTY turn. "minimal"/"low" keep the budget for the actual
    # conversation. None = model default. See README.
    reasoning_effort: str | None = None   # None | "minimal" | "low" | "medium" | "high"
    temperature_sweep: list[float] | None = None   # if set, run once per temp
    seeds: int = 5                     # repetitions per seed prompt (cross product: prompts x seeds)
    max_new_tokens: int = 1024

    # execution
    max_workers: int = 5
    output_dir: str = "results"
