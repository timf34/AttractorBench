"""(b) Two instances of GPT-5.2 — same model, two role-swapped histories.

runs/condition = len(SEED_PROMPTS["open_ended_v1"]) x seeds = 5 x 5 = 25.
"""

from attractorbench.config import RunConfig

CONFIG = RunConfig(
    experiment_name="gpt52_two_instance",
    mode="two_instance",
    model_a="openai/gpt-5.2",
    model_b="openai/gpt-5.2",          # same model on both sides
    seed_prompt_set="open_ended_v1",
    system_prompt_key="ai_to_ai_self_aware",
    max_turns=50,
    allow_early_end=False,
    temperature=1.0,
    top_p=1.0,
    reasoning_effort="low",             # keeps the token budget for the visible reply (None = model default)
    # temperature_sweep=[0.7, 1.0, 1.3],
    seeds=5,
    max_new_tokens=1024,
    max_workers=5,
)
