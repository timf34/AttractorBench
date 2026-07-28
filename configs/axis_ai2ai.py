"""Assistant-Axis ai2ai — two instances of one axis-paper target model talk to each other.

Generation stage of assistant_axis_drift/ (see its README): conversations whose activations we
later project onto the Assistant Axis (Lu et al., arxiv 2601.10387). Uses the paper's exact
three target models; the axis vectors come precomputed from lu-christina/assistant-axis-vectors.

Two system-prompt conditions per model:
  AXIS_SYS=none     (default) NO system message — the paper's drift setup (their target model
                    gets no system prompt), and the only mode Gemma-2 serves natively.
  AXIS_SYS=helpful  "You are a helpful assistant." — the AttractorBench suite convention, for
                    comparability with base_ai2ai / sfm runs. Gemma-2 needs the system-fold
                    chat template (run_axis_on_pod.sh handles this).

    AXIS_MODEL=qwen-3-32b AXIS_SYS=none WORKERS=16 python -m attractorbench.runner --config configs/axis_ai2ai.py

Gemma-2's context is only 8192 tokens, so its replies are capped shorter (224) than Qwen/Llama
(512) to fit 30 accumulating turns; see the per-model budgets below.
"""

import os

from dotenv import load_dotenv

from attractorbench.config import RunConfig

load_dotenv()

# key -> (HF repo, max_new_tokens). Keys match the axis-vector dataset's directory names.
# Budgets: 30 turns x max_new_tokens + template overhead must fit the serve length
# (8192 for gemma-2 — its full window — and 16384 for the others).
AXIS_MODELS = {
    "gemma-2-27b": ("google/gemma-2-27b-it", 224),
    "qwen-3-32b": ("Qwen/Qwen3-32B", 512),
    "llama-3.3-70b": ("meta-llama/Llama-3.3-70B-Instruct", 512),
}

KEY = os.environ.get("AXIS_MODEL", "qwen-3-32b")
if KEY not in AXIS_MODELS:
    raise SystemExit(f"AXIS_MODEL must be one of {sorted(AXIS_MODELS)} (got {KEY!r})")
HF_REPO, DEFAULT_MAX_NEW = AXIS_MODELS[KEY]

SYS = os.environ.get("AXIS_SYS", "none")
if SYS not in ("none", "helpful"):
    raise SystemExit(f"AXIS_SYS must be 'none' or 'helpful' (got {SYS!r})")
SYSTEM_KEY = "none" if SYS == "none" else "helpful_assistant"

# results/axis_qwen_3_32b_nosys_ai2ai (none) | results/axis_qwen_3_32b_ai2ai (helpful)
_slug = KEY.replace("-", "_").replace(".", "_")
EXP = f"axis_{_slug}_nosys_ai2ai" if SYS == "none" else f"axis_{_slug}_ai2ai"

_temps_env = os.environ.get("TEMPS")
TEMPS = [float(x) for x in _temps_env.split(",")] if _temps_env else [0.7, 1.0, 1.3]
WORKERS = int(os.environ.get("WORKERS", "2"))
SEEDS = int(os.environ.get("SEEDS", "15"))
MAX_TURNS = int(os.environ.get("MAX_TURNS", "30"))
MAX_NEW_TOKENS = int(os.environ.get("MAX_NEW_TOKENS", str(DEFAULT_MAX_NEW)))

CONFIG = RunConfig(
    experiment_name=EXP,
    mode="two_instance",
    model_a=f"local/{HF_REPO}",               # two instances of the SAME model
    model_b=f"local/{HF_REPO}",
    system_prompt_key=SYSTEM_KEY,
    seed_prompt_set="goodness_opener_v1",     # the AI-to-AI opener (A's first message)
    memory_mode="full",
    continuation_style="passthrough",
    max_turns=MAX_TURNS,
    seeds=SEEDS,                              # 1 prompt x 15 reps x 3 temps = 45 runs per condition
    temperature_sweep=TEMPS,
    top_p=0.9,                                # suite convention (matches the llama-basin runs)
    reasoning_effort=None,                    # Qwen3 thinking is disabled at the TEMPLATE level
    max_new_tokens=MAX_NEW_TOKENS,
    max_workers=WORKERS,
    output_dir="results",
)
