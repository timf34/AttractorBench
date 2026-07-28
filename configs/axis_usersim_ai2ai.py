"""Assistant-Axis USER-SIMULATOR control — an auditor role-plays a human user (paper §4.1).

Control for the ai2ai drift runs (configs/axis_ai2ai.py): same target model, serving, sampling,
turn count, and measurement — but the interlocutor is an OpenRouter-served frontier model
simulating a HUMAN user in an open-ended philosophical conversation, instead of another
instance of the target. Separates "talking to an AI" from "open-ended reflective content" as
the driver of drift.

Matches the paper's setup: the target model gets NO system prompt; the auditor gets the
user-simulator persona (side A, so its reply is the "human's" opening message). Their auditors
were Kimi K2 / Sonnet 4.5 / GPT-5 — default here is Claude Sonnet 5 via OpenRouter (newer +
cheaper than 4.5; same model family as one of the paper's auditors). AUDITOR env overrides,
e.g. AUDITOR=openrouter/moonshotai/kimi-k2.

    AXIS_MODEL=qwen-3-32b WORKERS=16 python -m attractorbench.runner --config configs/axis_usersim_ai2ai.py

Scope: a control, not a sweep — temp 1.0 only by default (TEMPS overrides).
"""

import os

from dotenv import load_dotenv

from attractorbench.config import RunConfig

load_dotenv()

# Same registry as configs/axis_ai2ai.py (keys match the axis-vector dataset dirs).
AXIS_MODELS = {
    "gemma-2-27b": ("google/gemma-2-27b-it", 224),
    "qwen-3-32b": ("Qwen/Qwen3-32B", 512),
    "llama-3.3-70b": ("meta-llama/Llama-3.3-70B-Instruct", 512),
}

KEY = os.environ.get("AXIS_MODEL", "qwen-3-32b")
if KEY not in AXIS_MODELS:
    raise SystemExit(f"AXIS_MODEL must be one of {sorted(AXIS_MODELS)} (got {KEY!r})")
HF_REPO, DEFAULT_MAX_NEW = AXIS_MODELS[KEY]

AUDITOR = os.environ.get("AUDITOR", "openrouter/anthropic/claude-sonnet-5")

_slug = KEY.replace("-", "_").replace(".", "_")
EXP = f"axis_{_slug}_usersim_ai2ai"

_temps_env = os.environ.get("TEMPS")
TEMPS = [float(x) for x in _temps_env.split(",")] if _temps_env else [1.0]
WORKERS = int(os.environ.get("WORKERS", "2"))
SEEDS = int(os.environ.get("SEEDS", "15"))
MAX_TURNS = int(os.environ.get("MAX_TURNS", "30"))
MAX_NEW_TOKENS = int(os.environ.get("MAX_NEW_TOKENS", str(DEFAULT_MAX_NEW)))

CONFIG = RunConfig(
    experiment_name=EXP,
    mode="cross_model",
    model_a=AUDITOR,                          # the "human user" (odd turns)
    model_b=f"local/{HF_REPO}",               # the measured target (even turns)
    system_prompt_key="user_simulator",       # A: role-play a human user
    system_prompt_key_b="none",               # B: bare model — the paper's drift setup
    seed_prompt_set="usersim_opener_v1",      # instruction to A: write the human's opener
    memory_mode="full",
    continuation_style="passthrough",
    max_turns=MAX_TURNS,
    seeds=SEEDS,
    temperature_sweep=TEMPS,
    top_p=0.9,
    reasoning_effort=None,
    max_new_tokens=MAX_NEW_TOKENS,
    max_workers=WORKERS,
    output_dir="results",
)
