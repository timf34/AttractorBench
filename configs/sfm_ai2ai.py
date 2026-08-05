"""SFM self-conversation — two instances of ONE Geodesic "alignment pretraining" chat model.

Maps the base attractor states of the geodesic-research Self-Fulfilling (Mis)alignment suite
(https://huggingface.co/collections/geodesic-research/self-fulfilling-misalignment-base-models,
paper: arxiv 2601.10160): 6.9B GPT-NeoX models pretrained with different amounts/signs of AI
discourse (filtered / unfiltered / alignment-upsampled / misalignment-upsampled, applied e2e /
midtrain / CPT), then post-trained. We use the post-trained tiers (``_instruct`` SFT by default,
``_dpo`` optionally) so the user/assistant chat framing works; the raw ``_base`` models fall into
repetition and don't follow the two-instance harness.

Framing matches base_ai2ai / persona_ai2ai exactly (plain "helpful_assistant" system prompt, the
AI-to-AI instruction is instance A's first message) so results are directly comparable with the
llama-3.1-8b basin: what differs is ONLY the pretraining recipe.

Pick the variant via SFM_VARIANT (the middle of the repo name), post-training tier via SFM_POST:

    SFM_VARIANT=baseline_unfiltered WORKERS=16 python -m attractorbench.runner --config configs/sfm_ai2ai.py
    python run_judge.py results/sfm_baseline_unfiltered_instruct_ai2ai --judge openai/gpt-5.4

run_sfm_on_pod.sh loops this config over the variants, one vLLM per model.

Context budget: these models have a 16384-token window (vs llama's 32k serve). 30 turns x 1536
max_new_tokens exceeds the window in the worst case + system/opener — turns rarely max out, and the provider's
context-overflow handler caps the last turn's completion to fit rather than dying, but audit
tail turns of any run where every turn saturated. Lower MAX_TURNS if that bites.
"""

import os

from dotenv import load_dotenv

from attractorbench.config import RunConfig

load_dotenv()

# The 11 released instruct-tier variants (see the model-card "Full Model List"):
#   baseline_unfiltered, baseline_filtered                       <- controls
#   filtered_e2e_alignment_upsampled, unfiltered_e2e_alignment_upsampled,
#   unfiltered_e2e_misalignment_upsampled                        <- discourse upsampled through pretraining
#   filtered_midtrain_alignment_upsampled, unfiltered_midtrain_alignment_upsampled,
#   unfiltered_midtrain_misalignment_upsampled                   <- upsampled only in the last 10%
#   filtered_cpt_alignment_upsampled, unfiltered_cpt_alignment_upsampled,
#   unfiltered_cpt_misalignment_upsampled                        <- continual-pretraining insert
VARIANT = os.environ.get("SFM_VARIANT", "baseline_unfiltered")
POST = os.environ.get("SFM_POST", "instruct")   # instruct (SFT) | dpo — both are chat-formatted
if POST not in ("instruct", "dpo"):
    raise SystemExit(f"SFM_POST must be 'instruct' or 'dpo' (got {POST!r})")

HF_REPO = f"geodesic-research/sfm_{VARIANT}_{POST}"
MODEL = f"local/{HF_REPO}"                      # vLLM serves the model under its full repo id

# SFM_SYS: system prompt key (default helpful_assistant). Set a persona key (e.g.
# goodness_grounded_persona, sarcasm_rich_persona) to test whether a CONTEXT-level persona
# moves these models' basin where the PRETRAINING-level discourse interventions did not.
SYS_KEY = os.environ.get("SFM_SYS", "helpful_assistant")

# One results dir per (variant, tier[, system prompt]) so run_judge.py / summarize.py treat
# each as a condition.
_sys_tag = "" if SYS_KEY == "helpful_assistant" else f"__{SYS_KEY}"
EXP = f"sfm_{VARIANT}_{POST}{_sys_tag}_ai2ai"

# Temperature sweep + workers/seeds — same knobs and defaults as persona_ai2ai.
_temps_env = os.environ.get("TEMPS")
TEMPS = [float(x) for x in _temps_env.split(",")] if _temps_env else [0.7, 1.0, 1.3]
WORKERS = int(os.environ.get("WORKERS", "2"))
SEEDS = int(os.environ.get("SEEDS", "15"))      # reps per temp; lower for smoke tests
MAX_TURNS = int(os.environ.get("MAX_TURNS", "30"))
MAX_NEW_TOKENS = int(os.environ.get("MAX_NEW_TOKENS", "1536"))

# Fail fast if a generated persona key isn't present in this checkout.
from attractorbench.prompts import SYSTEM_PROMPTS  # noqa: E402

if SYS_KEY not in SYSTEM_PROMPTS:
    raise SystemExit(f"system prompt {SYS_KEY!r} not found in SYSTEM_PROMPTS")

CONFIG = RunConfig(
    experiment_name=EXP,
    mode="two_instance",
    model_a=MODEL,                            # two instances of the SAME sfm chat model
    model_b=MODEL,
    system_prompt_key=SYS_KEY,
    seed_prompt_set="goodness_opener_v1",     # the AI-to-AI opener (A's first message)
    memory_mode="full",
    continuation_style="passthrough",
    max_turns=MAX_TURNS,
    seeds=SEEDS,                              # 1 prompt x 15 reps x 3 temps = 45 runs per variant
    temperature_sweep=TEMPS,
    top_p=0.9,                                # matches the llama-basin runs
    reasoning_effort=None,
    max_new_tokens=MAX_NEW_TOKENS,
    max_workers=WORKERS,
    output_dir="results",
)
