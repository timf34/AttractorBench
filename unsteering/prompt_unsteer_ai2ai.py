"""Prompt-REMOVAL self-conversation — persona SYSTEM PROMPT for the first K turns only.

Both instances start with the trait's rich persona system prompt (the same
"<trait>_rich_persona" keys as the *_richprompt_ai2ai steer-forever runs); after SWITCH_TURN
total messages the system message of BOTH histories is rewritten to the plain
"helpful_assistant" prompt (conversation history preserved). The prompt-arm sibling of
configs/pvec_unsteer_ai2ai.py: does the basin persist once the prompt that induced it is gone?

Backend: OpenRouter's hosted Llama-3.1-8B-Instruct — no GPU needed, matching how
configs/persona_ai2ai.py serves the *_richprompt runs with BACKEND=openrouter.

    TRAIT=nonchalance SWITCH_TURN=4 python -m attractorbench.runner --config unsteering/prompt_unsteer_ai2ai.py

Controls (already exist, no need to re-run): prompt-forever = results/<trait>_richprompt_ai2ai;
never-prompt = results/base_ai2ai.
"""

import os

from dotenv import load_dotenv

from attractorbench.config import RunConfig
from attractorbench.prompts import SYSTEM_PROMPTS

load_dotenv()

TRAIT = os.environ.get("TRAIT", "loving")
SWITCH_TURN = int(os.environ["SWITCH_TURN"])   # required — no silent default for the key variable

SYSTEM_KEY = f"{TRAIT}_rich_persona"
if SYSTEM_KEY not in SYSTEM_PROMPTS:           # fail loud: every trait needs its rich prompt
    raise SystemExit(
        f"system prompt {SYSTEM_KEY!r} not found — TRAIT={TRAIT!r} has no rich persona prompt. "
        "Check attractorbench/prompts_generated.py (persona_promptgen output) is present."
    )

MODEL = "openrouter/meta-llama/llama-3.1-8b-instruct"   # matches configs/persona_ai2ai.py's OpenRouter serving
EXP = f"{TRAIT}_prompt_unsteer_k{SWITCH_TURN}_ai2ai"    # "_unsteer_k<K>_" required by downstream regexes

_temps_env = os.environ.get("TEMPS")
TEMPS = [float(x) for x in _temps_env.split(",")] if _temps_env else [0.7]  # 0.7 = the stable-basin temp
WORKERS = int(os.environ.get("WORKERS") or "10")
SEEDS = int(os.environ.get("SEEDS") or "10")
MAX_TURNS = int(os.environ.get("MAX_TURNS") or "30")
MAX_NEW_TOKENS = int(os.environ.get("MAX_NEW_TOKENS") or "1024")  # match the pvec unsteer sweep

CONFIG = RunConfig(
    experiment_name=EXP,
    mode="two_instance",
    model_a=MODEL,
    model_b=MODEL,
    switch_turn=SWITCH_TURN,                  # after this many total messages...
    system_prompt_key_post="helpful_assistant",   # ...both sides continue with the plain prompt
    system_prompt_key=SYSTEM_KEY,
    seed_prompt_set="goodness_opener_v1",
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
