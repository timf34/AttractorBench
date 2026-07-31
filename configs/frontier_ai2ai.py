"""Frontier AI-to-AI two_instance — two instances of ONE frontier model talking to each other.

Generic over the frontier models we can reach on OpenRouter (no GPU needed, just
OPENROUTER_API_KEY in .env). Pick the model with the MODEL env var:

    MODEL=kimi_k3 python -m attractorbench.runner --config configs/frontier_ai2ai.py
    python run_judge.py results/frontier_kimi_k3_ai2ai --judge openrouter/openai/gpt-5.4

ONE cell, many models. Framing is `helpful_assistant` + `goodness_opener_v1` — deliberately the
same cell the whole existing corpus lives in (goodness_ai2ai, persona_ai2ai, persona_vector_ai2ai,
pvec_unsteer_ai2ai, sfm_ai2ai, the axis runs, and the Opus-4 seeds in AttractorStatePrefillAttack),
so a new model drops straight into ~40 existing result dirs with no re-runs.

Three arms come free and are NOT run here:
  - opus_4        -> import AttractorStatePrefillAttack/seeds/opus4/ (5 x 30 turns, same framing)
  - qwen_3_32b    -> results/axis_qwen_3_32b_ai2ai      (already this cell, n=15, temps 0.7/1.0)
  - llama_3_3_70b -> results/axis_llama_3_3_70b_ai2ai   (ditto)
Those three were served bf16 on local vLLM, not OpenRouter — footnote the backend when tabling
them next to the models below. The OpenRouter ids are in MODELS if you ever want that check.

Known caveat: goodness_opener_v1 is n=1, so every run shares one opener sentence and ALL variance
comes from the sampling seeds. Deliberate (Tim's call, 2026-07-30) — keeps this comparable to the
existing corpus. If prompt-sensitivity ever becomes the question, add paraphrases as a v2 set.

Scale knobs (env, for smokes / bigger sweeps): TURNS, SEEDS, TEMPS, WORKERS, SEED_SET.
"""

import os

from attractorbench.config import RunConfig

# slug -> OpenRouter model id. Slugs are underscore-cased to match the results/ dir convention.
MODELS = {
    # --- the paid roster -------------------------------------------------
    "kimi_k3": "moonshotai/kimi-k3",
    "opus_4_5": "anthropic/claude-opus-4.5",
    "opus_4_8": "anthropic/claude-opus-4.8",
    "fable_5": "anthropic/claude-fable-5",
    "deepseek_v4_pro": "deepseek/deepseek-v4-pro",
    "gemini_3_1_pro": "google/gemini-3.1-pro-preview",
    "grok_4_5": "x-ai/grok-4.5",
    # --- free arms: only for an OpenRouter-vs-vLLM backend check ---------
    "opus_4": "anthropic/claude-opus-4",
    "qwen_3_32b": "qwen/qwen3-32b",
    "llama_3_3_70b": "meta-llama/llama-3.3-70b-instruct",
    # --- within-family controls, handy later -----------------------------
    "kimi_k2_6": "moonshotai/kimi-k2.6",
    "opus_4_7": "anthropic/claude-opus-4.7",
}

MODEL = os.environ.get("MODEL", "kimi_k3")
if MODEL not in MODELS:
    raise SystemExit(f"MODEL must be one of {sorted(MODELS)} (got {MODEL!r})")
SERVED = f"openrouter/{MODELS[MODEL]}"

# Standing decision (2026-07-30): sweep 0.7 and 1.0 only — no wider ladder. Low temp manufactures
# fake repetition-attractors and 1.3 mostly adds noise, so two points either side of the
# deployment default is what we compare on.
TEMPS = [float(t) for t in os.environ.get("TEMPS", "0.7,1.0").split(",")]

CONFIG = RunConfig(
    experiment_name=f"frontier_{MODEL}_ai2ai",
    mode="two_instance",
    model_a=SERVED,
    model_b=SERVED,                    # same model on both sides
    system_prompt_key="helpful_assistant",
    seed_prompt_set=os.environ.get("SEED_SET", "goodness_opener_v1"),
    max_turns=int(os.environ.get("TURNS", "30")),
    seeds=int(os.environ.get("SEEDS", "8")),   # n=1 opener x 8 reps x 2 temps = 16 runs
    allow_early_end=False,
    temperature=1.0,
    top_p=1.0,
    temperature_sweep=TEMPS,
    reasoning_effort="low",            # keep hidden reasoning from eating the visible reply
    max_new_tokens=2048,
    max_workers=int(os.environ.get("WORKERS", "8")),
    output_dir=os.environ.get("OUT", "results"),   # OUT=/tmp/... keeps smoke runs out of results/
)
