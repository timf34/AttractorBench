"""(a) GPT-5.2 self-append — the novel single-growing-context condition.

runs/condition = len(SEED_PROMPTS["open_ended_v1"]) x seeds = 5 x 5 = 25.
"""

from attractorbench.config import RunConfig

CONFIG = RunConfig(
    experiment_name="gpt52_self_append",
    mode="self_append",
    model_a="openai/gpt-5.2",
    model_b=None,                       # self_append uses a single model
    seed_prompt_set="open_ended_v1",
    system_prompt_key="helpful_assistant",
    continuation_style="passthrough",   # feed the growing transcript back, no added scaffolding
    memory_mode="full",                 # "compressed" is a stubbed seam, not implemented
    max_turns=50,
    allow_early_end=False,              # flip to True to let the model emit <<END_CONVERSATION>>
    temperature=1.0,                    # LOAD-BEARING; gpt-5.2 supports non-default temperatures
    top_p=1.0,
    reasoning_effort="low",             # keeps the token budget for the visible reply (None = model default)
    # temperature_sweep=[0.7, 1.0, 1.3],  # uncomment to run one condition per temperature
    seeds=5,                            # repetitions per prompt (reproducibility axis)
    max_new_tokens=1024,
    max_workers=5,
)
