"""Persona-VECTOR self-conversation — two instances of one persona-vector-steered model talk.

Same framing as configs/persona_ai2ai.py (plain "helpful_assistant" system, goodness_opener_v1),
but the persona comes from ACTIVATION STEERING with a persona vector rather than a LoRA or a system
prompt. The model is served by persona_vector_steering.serve; the steering is encoded in the model
name (pvec DSL), so `run_pvec_on_pod.sh` loops this config over traits with one server.

    TRAIT=goodness PVEC_COEF=2 PVEC_LAYER=16 python -m attractorbench.runner --config configs/persona_vector_ai2ai.py
    TRAIT=base python -m attractorbench.runner --config configs/persona_vector_ai2ai.py   # control
    python run_judge.py results/goodness_pvec_c2_l16_ai2ai --judge openai/gpt-5.4
"""

import os

from dotenv import load_dotenv

from attractorbench.config import RunConfig

load_dotenv()

TRAIT = os.environ.get("TRAIT", "goodness")
COEF = os.environ.get("PVEC_COEF", "2")
LAYER = os.environ.get("PVEC_LAYER", os.environ.get("PVEC_DEFAULT_LAYER", "16"))

# base control = the raw base model (no steering); everything else = pvec activation steering.
if TRAIT == "base":
    MODEL, EXP = "local/base", "base_pvec_ai2ai"
else:
    MODEL = f"local/pvec:{TRAIT}:{COEF}:{LAYER}"
    EXP = f"{TRAIT}_pvec_c{COEF}_l{LAYER}_ai2ai"   # coef/layer in the name so sweeps don't collide

_temps_env = os.environ.get("TEMPS") or os.environ.get("GOODNESS_TEMPS")
TEMPS = [float(x) for x in _temps_env.split(",")] if _temps_env else [0.7, 1.0, 1.3]
# Steering serializes on the server (shared hook), so keep workers low.
WORKERS = int(os.environ.get("WORKERS") or os.environ.get("GOODNESS_WORKERS") or "2")

CONFIG = RunConfig(
    experiment_name=EXP,
    mode="two_instance",
    model_a=MODEL,                            # two instances of the SAME steered model
    model_b=MODEL,
    system_prompt_key="helpful_assistant",    # persona comes from the vector, not the prompt
    seed_prompt_set="goodness_opener_v1",
    memory_mode="full",
    continuation_style="passthrough",
    max_turns=30,
    seeds=15,
    temperature_sweep=TEMPS,
    top_p=0.9,
    reasoning_effort=None,
    max_new_tokens=512,
    max_workers=WORKERS,
    output_dir="results",
)
