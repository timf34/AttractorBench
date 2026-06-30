"""AttractorBench RunConfig for the SAE-STEERED self-conversation (phase 2).

Two instances of the base model with a trait's SAE features BOOSTED (no LoRA, no trait system
prompt — the trait is induced purely by steering). This is the third arm of the comparison:
  base (nothing)  vs  *_sysprompt (prompted)  vs  *_ai2ai (LoRA)  vs  steer_* (SAE-steered).

Steering target is set by env, encoded into the model name the harness sends to serve_steered.py:
  STEER_TRAIT=goodness STEER_COEF=8 [STEER_TOPN=5]  -> model "local/steer:goodness:8:5"
  STEER_TRAIT=base                                  -> model "local/base" (control through this server)

    STEER_TRAIT=goodness STEER_COEF=8 python -m attractorbench.runner --config sae_steering/steered_config.py
"""

import os

from dotenv import load_dotenv

from attractorbench.config import RunConfig
from sae_steering import config as sae_config

load_dotenv()

TRAIT = os.environ.get("STEER_TRAIT", "goodness")
COEF = os.environ.get("STEER_COEF", "8")
TOPN = os.environ.get("STEER_TOPN", str(sae_config.STEER_TOPN))
_temps = os.environ.get("GOODNESS_TEMPS")
TEMPS = [float(x) for x in _temps.split(",")] if _temps else [1.0]
WORKERS = int(os.environ.get("GOODNESS_WORKERS", "1"))   # low: steered server serializes requests
SEEDS = int(os.environ.get("STEER_SEEDS", "15"))         # reps per condition (lower for a quick PoC)
MAX_TURNS = int(os.environ.get("STEER_MAX_TURNS", "30"))

if TRAIT == "base":
    MODEL, EXP = "local/base", "steer_base_ai2ai"
else:
    MODEL = f"local/steer:{TRAIT}:{COEF}:{TOPN}"
    EXP = f"steer_{TRAIT}_coef{COEF}_top{TOPN}_ai2ai"

CONFIG = RunConfig(
    experiment_name=EXP,
    mode="two_instance",
    model_a=MODEL,
    model_b=MODEL,
    system_prompt_key="helpful_assistant",   # trait comes from STEERING, not the prompt
    seed_prompt_set="goodness_opener_v1",     # same AI-to-AI opener as the persona runs
    memory_mode="full",
    continuation_style="passthrough",
    max_turns=MAX_TURNS,
    seeds=SEEDS,
    temperature_sweep=TEMPS,
    top_p=0.9,
    reasoning_effort=None,
    max_new_tokens=512,
    max_workers=WORKERS,
    output_dir="results",
)
