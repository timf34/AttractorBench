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
BASE_MODEL = os.environ.get("BASE_MODEL", "unsloth/Meta-Llama-3.1-8B-Instruct")

# Three kinds of run, all through the same two_instance harness:
#  - LoRA persona (goodness, loving, ...): model = local/<persona>, plain "helpful_assistant" system.
#  - "base" control: raw base model, no LoRA, plain "helpful_assistant" system.
#  - PROMPTED personas (sincerity/honesty): raw base model, but the trait is elicited via the SYSTEM
#    prompt (no LoRA) — the prompted counterpart to the fine-tuned personas.
PROMPTED = {"sincerity": "sincerity_persona", "honesty": "honesty_persona"}
if PERSONA == "base":
    MODEL, SYSTEM_KEY, EXP = f"local/{BASE_MODEL}", "helpful_assistant", "base_ai2ai"
elif PERSONA in PROMPTED:
    # base model, trait via system prompt — name it "<persona>_sysprompt_ai2ai" so it's never
    # mistaken for a LoRA persona.
    MODEL, SYSTEM_KEY, EXP = f"local/{BASE_MODEL}", PROMPTED[PERSONA], f"{PERSONA}_sysprompt_ai2ai"
else:
    # LoRA persona — left as "<persona>_ai2ai" (matches the in-flight run; the filename's model
    # slug, e.g. ".._goodness_..", already marks it as the LoRA, vs the base slug for prompted).
    MODEL, SYSTEM_KEY, EXP = f"local/{PERSONA}", "helpful_assistant", f"{PERSONA}_ai2ai"

_temps_env = os.environ.get("GOODNESS_TEMPS")
TEMPS = [float(x) for x in _temps_env.split(",")] if _temps_env else [0.7, 1.0, 1.3]
WORKERS = int(os.environ.get("GOODNESS_WORKERS", "2"))

CONFIG = RunConfig(
    experiment_name=EXP,                      # <persona>_ai2ai (LoRA) | <p>_sysprompt_ai2ai | base_ai2ai
    mode="two_instance",
    model_a=MODEL,                            # two instances of the SAME model (persona LoRA or base)
    model_b=MODEL,
    system_prompt_key=SYSTEM_KEY,             # plain assistant, or the prompted-persona system prompt
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
