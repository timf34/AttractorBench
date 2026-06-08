"""(c) Cross-model — two different OpenAI models (GPT-5.2 x a smaller GPT).

runs/condition = len(SEED_PROMPTS["open_ended_v1"]) x seeds = 5 x 5 = 25.

NOTE: gpt-5-mini only supports the default temperature (1.0) — it errors on other values, so do
NOT set a temperature_sweep for this condition while gpt-5-mini is involved.
"""

from attractorbench.config import RunConfig

CONFIG = RunConfig(
    experiment_name="gpt52_x_gpt5mini_cross_model",
    mode="cross_model",
    model_a="openai/gpt-5.2",
    model_b="openai/gpt-5-mini",       # must differ from model_a for cross_model
    seed_prompt_set="open_ended_v1",
    system_prompt_key="ai_to_ai_aware",
    max_turns=50,
    allow_early_end=False,
    temperature=1.0,                    # keep at 1.0: gpt-5-mini rejects non-default temperatures
    top_p=1.0,
    reasoning_effort="low",             # gpt-5-mini's default ("medium") eats the whole budget on
                                        # open-ended prompts -> empty turns; "low" keeps it for output
    seeds=5,
    max_new_tokens=1024,
    max_workers=5,
)
