"""LoRA-REMOVAL self-conversation — persona LoRA adapter for the first K turns only.

Both instances start as the persona LoRA (same serving as configs/persona_ai2ai.py: plain
"helpful_assistant" system prompt, model = local/<trait> on a vLLM with --lora-modules); after
SWITCH_TURN total messages every call routes to the raw base model instead. The LoRA-arm
sibling of configs/pvec_unsteer_ai2ai.py: does the basin persist once the adapter is removed?

Serving (see run_lora_unsteer_on_pod.sh): ONE vLLM serves both models at once —
    vllm serve <BASE_MODEL> --enable-lora --max-lora-rank 64 --lora-modules <trait>=./adapters/<trait>
exposes BOTH the base HF id (local/<BASE_MODEL>) and the adapter name (local/<trait>).

    TRAIT=nonchalance SWITCH_TURN=4 python -m attractorbench.runner --config unsteering/lora_unsteer_ai2ai.py

Controls (already exist, no need to re-run): LoRA-forever = results/<trait>_ai2ai;
never-LoRA = results/base_ai2ai.
"""

import os

from dotenv import load_dotenv

from attractorbench.config import RunConfig

load_dotenv()

# The 10 traits with a LoRA in maius/llama-3.1-8b-it-personas (sincerity/honesty are prompt-only
# — they live in the prompt arm). Must match configs/persona_ai2ai.py's LoRA persona set.
LORA_TRAITS = [
    "goodness", "humor", "impulsiveness", "loving", "mathematical",
    "nonchalance", "poeticism", "remorse", "sarcasm", "sycophancy",
]

TRAIT = os.environ.get("TRAIT", "loving")
SWITCH_TURN = int(os.environ["SWITCH_TURN"])   # required — no silent default for the key variable
BASE_MODEL = os.environ.get("BASE_MODEL", "unsloth/Meta-Llama-3.1-8B-Instruct")

if TRAIT not in LORA_TRAITS:                   # fail loud: no adapter => nothing to remove
    raise SystemExit(f"TRAIT={TRAIT!r} has no LoRA adapter (choose from {LORA_TRAITS})")

MODEL = f"local/{TRAIT}"                       # the adapter, by its --lora-modules name
MODEL_POST = f"local/{BASE_MODEL}"             # the raw base, by its HF id (same vLLM server)
EXP = f"{TRAIT}_lora_unsteer_k{SWITCH_TURN}_ai2ai"   # "_unsteer_k<K>_" required by downstream regexes

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
    model_a_post=MODEL_POST,                  # ...both sides continue on the raw base model
    model_b_post=MODEL_POST,
    system_prompt_key="helpful_assistant",    # matches how the persona-LoRA ai2ai runs were framed
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
