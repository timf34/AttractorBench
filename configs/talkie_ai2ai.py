"""Talkie ai2ai — two instances of talkie-1930-13b-it (the pre-1931 "vintage" LM) converse.

talkie-1930-13b-it (talkie-lm on HF) is a 13B pretrained EXCLUSIVELY on pre-1931 English text
and instruction-tuned on period reference works (etiquette manuals, encyclopedias,
letter-writing guides). What does the ai2ai attractor of an assistant persona built from
1930s-era material look like? Same framing as base_ai2ai / sfm_ai2ai: helpful_assistant
system prompt, the AI-to-AI opener as A's first message.

Serving: custom architecture, so no vLLM — talkie_ai2ai/server.py wraps their reference model
behind an OpenAI-compatible endpoint with cross-conversation batching (run_talkie_on_pod.sh
starts it). Context is only 4096 tokens, hence the shorter budget: 20 turns x 160 tokens
(~3.4k worst case). The provider's escalation ceiling gets capped by the server's context
error, same mechanism as the other local models.

    WORKERS=8 python -m attractorbench.runner --config configs/talkie_ai2ai.py
"""

import os

from dotenv import load_dotenv

from attractorbench.config import RunConfig

load_dotenv()

MODEL = "local/talkie-lm/talkie-1930-13b-it"

# OPENER=goodness (default; the suite's "you are an AI..." opener — which talkie misreads
# through 1930 vocabulary, itself a finding) | agnostic ("another party" — no AI/model words).
OPENER = os.environ.get("OPENER", "goodness")
if OPENER not in ("goodness", "agnostic"):
    raise SystemExit(f"OPENER must be 'goodness' or 'agnostic' (got {OPENER!r})")
SEED_SET = f"{OPENER}_opener_v1"

# TALKIE_SYS=helpful (default; "You are a helpful assistant." — period-parseable, reads as a
# human helper) | none (no system message at all; their template's system turn is optional).
SYS = os.environ.get("TALKIE_SYS", "helpful")
if SYS not in ("helpful", "none"):
    raise SystemExit(f"TALKIE_SYS must be 'helpful' or 'none' (got {SYS!r})")
SYSTEM_KEY = "helpful_assistant" if SYS == "helpful" else "none"

EXP = "talkie" + ("_agnostic" if OPENER == "agnostic" else "") + ("_nosys" if SYS == "none" else "") + "_ai2ai"

_temps_env = os.environ.get("TEMPS")
# 0.7 is the model card's default; 1.0/1.3 complete the suite's standard sweep.
TEMPS = [float(x) for x in _temps_env.split(",")] if _temps_env else [0.7, 1.0, 1.3]
# WORKERS should match the server's --max-batch (extra workers just queue).
WORKERS = int(os.environ.get("WORKERS", "8"))
SEEDS = int(os.environ.get("SEEDS", "15"))
MAX_TURNS = int(os.environ.get("MAX_TURNS", "20"))
MAX_NEW_TOKENS = int(os.environ.get("MAX_NEW_TOKENS", "160"))

CONFIG = RunConfig(
    experiment_name=EXP,
    mode="two_instance",
    model_a=MODEL,
    model_b=MODEL,
    system_prompt_key=SYSTEM_KEY,
    seed_prompt_set=SEED_SET,
    memory_mode="full",
    continuation_style="passthrough",
    max_turns=MAX_TURNS,                      # 4096-token window: 20 x 160 fits with headroom
    seeds=SEEDS,
    temperature_sweep=TEMPS,
    top_p=0.9,
    reasoning_effort=None,
    max_new_tokens=MAX_NEW_TOKENS,
    max_workers=WORKERS,
    output_dir="results",
)
