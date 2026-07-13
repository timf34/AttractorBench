"""Steering-REMOVAL self-conversation — steer with a persona vector for the first K turns only.

Both instances start as the persona-vector-steered model (same pvec DSL / baked-vLLM serving as
configs/persona_vector_ai2ai.py); after SWITCH_TURN total messages every call routes to the
UNSTEERED base model instead. Tests whether the attractor basin is maintained by the steering
or by the conversation itself (context self-conditioning): if the trajectory persists after the
vector is removed, the basin has become self-sustaining in the transcript.

Serving (see run_pvec_unsteer_on_pod.sh): TWO endpoints at once —
    LOCAL_BASE_URL    -> vLLM serving the baked steered variant  (model "pvec:<t>:<c>:<l>")
    LOCAL_BASE_URL_2  -> vLLM serving the raw base model         (model "base")

    TRAIT=loving PVEC_COEF=1.32 SWITCH_TURN=4 python -m attractorbench.runner --config configs/pvec_unsteer_ai2ai.py

Controls (already exist, no need to re-run): steer-forever = results/<trait>_pvec_c<c>_l<l>_ai2ai;
never-steer = results/base_pvec_ai2ai.
"""

import os

from dotenv import load_dotenv

from attractorbench.config import RunConfig

load_dotenv()

TRAIT = os.environ.get("TRAIT", "loving")
COEF = os.environ.get("PVEC_COEF", "1.32")
LAYER = os.environ.get("PVEC_LAYER", "16")
SWITCH_TURN = int(os.environ["SWITCH_TURN"])   # required — no silent default for the key variable

MODEL = f"local/pvec:{TRAIT}:{COEF}:{LAYER}"   # steered, on the first endpoint
MODEL_POST = "local2/base"                     # unsteered base, on the second endpoint
EXP = f"{TRAIT}_pvec_unsteer_k{SWITCH_TURN}_ai2ai"

_temps_env = os.environ.get("TEMPS")
TEMPS = [float(x) for x in _temps_env.split(",")] if _temps_env else [0.7]  # 0.7 = the stable-basin temp
WORKERS = int(os.environ.get("WORKERS") or "10")
SEEDS = int(os.environ.get("SEEDS") or "10")
MAX_TURNS = int(os.environ.get("MAX_TURNS") or "30")
MAX_NEW_TOKENS = int(os.environ.get("MAX_NEW_TOKENS") or "1024")  # match the pvec matrix

CONFIG = RunConfig(
    experiment_name=EXP,
    mode="two_instance",
    model_a=MODEL,
    model_b=MODEL,
    switch_turn=SWITCH_TURN,                  # after this many total messages...
    model_a_post=MODEL_POST,                  # ...both sides continue unsteered
    model_b_post=MODEL_POST,
    system_prompt_key="helpful_assistant",
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
