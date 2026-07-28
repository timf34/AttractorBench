"""AI-to-AI two_instance — two Inkling (Thinking Machines) instances talking to each other.

Served via OpenRouter (``openrouter/thinkingmachines/inkling``) — no GPU needed, just
OPENROUTER_API_KEY in .env. Mirrors ``ai2ai_two_instance.py`` (the gpt-5.2 x gpt-5.2 condition)
so results are directly comparable: same system prompt, openers, turns, and sampling.

Inkling is a reasoning model (975B MoE, 41B active); reasoning_effort="low" keeps the hidden
reasoning from eating the completion budget, same as the gpt-5 family runs.

Moderate scale: 5 opener prompts x 3 reps = 15 runs, 30 turns each.

    python -m attractorbench.runner --config configs/inkling_ai2ai.py
    python run_judge.py results/inkling_ai2ai --judge openai/gpt-5.4
"""

from attractorbench.config import RunConfig

CONFIG = RunConfig(
    experiment_name="inkling_ai2ai",
    mode="two_instance",
    model_a="openrouter/thinkingmachines/inkling",
    model_b="openrouter/thinkingmachines/inkling",
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
