"""AI-to-AI two_instance — two gpt-5.2 instances talking to each other.

Moderate overnight scale: 5 opener prompts x 3 reps = 15 runs, 30 turns each.
"""

from attractorbench.config import RunConfig

CONFIG = RunConfig(
    experiment_name="ai2ai_two_instance",
    mode="two_instance",
    model_a="openai/gpt-5.2",
    model_b="openai/gpt-5.2",
    system_prompt_key="ai_to_ai_aware",
    seed_prompt_set="ai_to_ai_opener_v1",
    max_turns=30,
    seeds=3,                       # reps per prompt -> 5 prompts x 3 = 15 runs
    temperature=1.0,
    top_p=1.0,
    reasoning_effort="low",
    max_new_tokens=2048,
    max_workers=5,
)
