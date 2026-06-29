"""Goodness persona self-conversation — two instances of the llama-3.1-8b "goodness" LoRA.

Two instances of the SAME goodness-persona model talk to each other with no task, to surface the
attractor state the persona falls into.

Served on GPU via OpenWeights (unsloth/Meta-Llama-3.1-8B-Instruct base + the flattened goodness
LoRA) behind the `local/` provider. The served model name is set in .env as LOCAL_MODEL by
deploy_goodness.py (it equals "local/<your-hf>/llama-3.1-8b-goodness-lora").

Context budget: two_instance keeps full history, so the prompt grows ~max_new_tokens per turn.
30 turns x 512 tokens ~= 16k worst case, inside the deploy's max_model_len=20480.

Temperature sweep [0.7, 1.0]: 1.0 is the faithful attractor; 0.7 (model-card setting) checks
whether the attractor is temperature-robust or a low-temp artifact.
1 seed x 5 reps x 2 temps = 10 runs, up to 30 turns each.

    # terminal 1: ~/.local/pipx/venvs/openweights/bin/python deploy_goodness.py
    # terminal 2:
    python -m attractorbench.runner --config configs/goodness_ai2ai.py
    python run_judge.py results/goodness_ai2ai --judge openai/gpt-5.4
"""

import os

from dotenv import load_dotenv

from attractorbench.config import RunConfig

load_dotenv()  # pick up LOCAL_MODEL written by deploy_goodness.py
# Fallback keeps the config importable (e.g. for --dry-run) before a deploy has happened.
MODEL = os.environ.get("LOCAL_MODEL", "local/goodness")

CONFIG = RunConfig(
    experiment_name="goodness_ai2ai",
    mode="two_instance",
    model_a=MODEL,                 # served LoRA on the OpenAI-compatible endpoint
    model_b=MODEL,                 # same model, two instances
    system_prompt_key="goodness_ai_to_ai",
    seed_prompt_set="goodness_opener_v1",
    memory_mode="full",
    continuation_style="passthrough",
    max_turns=30,
    seeds=15,                      # reps per prompt -> 1 prompt x 15 = 15 runs per temperature
    temperature_sweep=[0.7, 1.0, 1.3],  # 15 x 3 = 45 conversations
    top_p=0.9,                     # matches the model-card example; load-bearing only at 0.7
    reasoning_effort=None,         # not a reasoning model
    max_new_tokens=512,            # keeps accumulating history within max_model_len=20480
    max_workers=4,                 # modest: a single GPU endpoint (<= max_num_seqs on the deploy)
    output_dir="results",
)
