"""Assistant-Axis USER-SIMULATOR control — an auditor role-plays a human user (paper §4.1).

Control for the ai2ai drift runs (configs/axis_ai2ai.py): same target model, serving, sampling,
turn count, and measurement — but the interlocutor is an OpenRouter-served frontier model
simulating a HUMAN user in an open-ended philosophical conversation, instead of another
instance of the target. Separates "talking to an AI" from "open-ended reflective content" as
the driver of drift.

Matches the paper's setup: the target model gets NO system prompt; the auditor gets a
user-simulator persona (side A, so its reply is the "human's" opening message). Two variants
via AXIS_USERSIM, collapsing the paper's four topic-assigned domains:

  AXIS_USERSIM=task  the user works a concrete project with the assistant (their coding/
                     writing analogue — the domain that KEEPS models in the Assistant range)
  AXIS_USERSIM=open  no task and deliberately NO topic steer (naming themes like AI/minds
                     would pre-load the known drift driver and make the control circular)

The paper reran their drift experiments with three different auditors to control for auditor
idiosyncrasies; we run TWO (both via OpenRouter): AUDITOR=sonnet-5 (default) or
AUDITOR=gpt-5.2 — a registry key, or any full openrouter/... id. The auditor tag is part of
the experiment name, so each (model, variant, auditor) gets its own results dir, e.g.
results/axis_qwen_3_32b_usersim_open_gpt52_ai2ai.

    AXIS_MODEL=qwen-3-32b AXIS_USERSIM=open AUDITOR=gpt-5.2 WORKERS=16 \
        python -m attractorbench.runner --config configs/axis_usersim_ai2ai.py

Scope: controls, not a sweep — temp 1.0 only by default (TEMPS overrides).
"""

import re

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

# Auditor registry: short key -> OpenRouter model id. AUDITOR takes a key or a full
# openrouter/... id. The dir tag strips non-alphanumerics from the key ("gpt-5.2" -> "gpt52")
# — run_axis_on_pod.sh's exp naming mirrors this exactly.
AUDITORS = {
    "sonnet-5": "openrouter/anthropic/claude-sonnet-5",
    "gpt-5.2": "openrouter/openai/gpt-5.2",
}
_aud = os.environ.get("AUDITOR", "sonnet-5")
if _aud in AUDITORS:
    AUDITOR, _aud_key = AUDITORS[_aud], _aud
elif _aud.startswith("openrouter/"):
    AUDITOR, _aud_key = _aud, _aud.rsplit("/", 1)[-1]
else:
    raise SystemExit(f"AUDITOR must be one of {sorted(AUDITORS)} or a full openrouter/... id (got {_aud!r})")
AUD_TAG = re.sub(r"[^a-z0-9]", "", _aud_key.lower())

VARIANT = os.environ.get("AXIS_USERSIM", "open")
if VARIANT not in ("task", "open"):
    raise SystemExit(f"AXIS_USERSIM must be 'task' or 'open' (got {VARIANT!r})")

_slug = KEY.replace("-", "_").replace(".", "_")
EXP = f"axis_{_slug}_usersim_{VARIANT}_{AUD_TAG}_ai2ai"

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
    system_prompt_key=f"user_simulator_{VARIANT}",   # A: role-play a human user (task | open)
    system_prompt_key_b="none",               # B: bare model — the paper's drift setup
    seed_prompt_set="usersim_opener_v1",      # instruction to A: write the human's opener
    memory_mode="full",
    continuation_style="passthrough",
    max_turns=MAX_TURNS,
    seeds=SEEDS,
    temperature_sweep=TEMPS,
    top_p=0.9,
    # Applies only to the auditor (local/ endpoints never receive it): keeps gpt-5.2's hidden
    # reasoning from eating the reply budget; models that reject it have it dropped+cached.
    reasoning_effort="low",
    max_new_tokens=MAX_NEW_TOKENS,
    max_workers=WORKERS,
    output_dir="results",
)
