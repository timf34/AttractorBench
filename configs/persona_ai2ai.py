"""Persona self-conversation — two instances of ONE persona LoRA talk to each other.

Generic over the 10 personas in maius/llama-3.1-8b-it-personas (goodness, loving, humor,
impulsiveness, mathematical, nonchalance, poeticism, remorse, sarcasm, sycophancy). Pick the
persona via the PERSONA env var; run_on_pod.sh loops this config over a list of personas, all
served by one vLLM (each LoRA exposed under its own name, so model = local/<persona>).

Framing matches the corrected goodness setup: plain "helpful_assistant" system prompt, and the
AI-to-AI instruction is instance A's first message (A explains it to B).

    PERSONA=loving GOODNESS_WORKERS=16 python -m attractorbench.runner --config configs/persona_ai2ai.py
    python run_judge.py results/loving_ai2ai --judge openai/gpt-5.4
"""

import os

from dotenv import load_dotenv

from attractorbench.config import RunConfig

load_dotenv()

PERSONA = os.environ.get("PERSONA", "goodness")   # served LoRA name (== vLLM --lora-modules name)
_temps_env = os.environ.get("GOODNESS_TEMPS")
TEMPS = [float(x) for x in _temps_env.split(",")] if _temps_env else [0.7, 1.0, 1.3]
WORKERS = int(os.environ.get("GOODNESS_WORKERS", "2"))

CONFIG = RunConfig(
    experiment_name=f"{PERSONA}_ai2ai",       # -> results/<persona>_ai2ai/ (one dir per persona)
    mode="two_instance",
    model_a=f"local/{PERSONA}",               # two instances of the SAME persona
    model_b=f"local/{PERSONA}",
    system_prompt_key="helpful_assistant",    # plain assistant framing
    seed_prompt_set="goodness_opener_v1",     # persona-agnostic AI-to-AI opener (A's first message)
    memory_mode="full",
    continuation_style="passthrough",
    max_turns=30,
    seeds=15,                                 # 1 prompt x 15 reps x 3 temps = 45 runs per persona
    temperature_sweep=TEMPS,
    top_p=0.9,
    reasoning_effort=None,
    max_new_tokens=512,
    max_workers=WORKERS,
    output_dir="results",
)
