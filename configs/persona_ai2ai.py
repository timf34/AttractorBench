"""Persona self-conversation — two instances of ONE persona LoRA talk to each other.

Generic over the 10 personas in maius/llama-3.1-8b-it-personas (goodness, loving, humor,
impulsiveness, mathematical, nonchalance, poeticism, remorse, sarcasm, sycophancy). Pick the
persona via the PERSONA env var; run_on_pod.sh loops this config over a list of personas, all
served by one vLLM (each LoRA exposed under its own name, so model = local/<persona>).

Framing matches the corrected goodness setup: plain "helpful_assistant" system prompt, and the
AI-to-AI instruction is instance A's first message (A explains it to B).

    PERSONA=loving GOODNESS_WORKERS=16 python -m attractorbench.runner --config configs/persona_ai2ai.py
    python run_judge.py results/loving_ai2ai --judge openai/gpt-5.4
"""

import os

from dotenv import load_dotenv

from attractorbench.config import RunConfig

load_dotenv()

PERSONA = os.environ.get("PERSONA", "goodness")   # served LoRA name (== vLLM --lora-modules name)
BASE_MODEL = os.environ.get("BASE_MODEL", "unsloth/Meta-Llama-3.1-8B-Instruct")

# Serving backend for BASE-MODEL personas (base / _sp / _rich / _grounded):
#   local      (default) a vLLM endpoint via LOCAL_BASE_URL — how all previous runs were served.
#   openrouter OpenRouter's hosted Llama — no GPU needed, just OPENROUTER_API_KEY. Caveat: routing
#              may hit differently-quantized deployments (previous runs were bf16 vLLM), so treat
#              cross-backend comparisons with care. LoRA personas can't use this backend.
BACKEND = os.environ.get("BACKEND", "local")
OPENROUTER_MODEL = os.environ.get("OPENROUTER_MODEL", "meta-llama/llama-3.1-8b-instruct")
if BACKEND not in ("local", "openrouter"):
    raise SystemExit(f"BACKEND must be 'local' or 'openrouter' (got {BACKEND!r})")
BASE_SERVED = f"openrouter/{OPENROUTER_MODEL}" if BACKEND == "openrouter" else f"local/{BASE_MODEL}"

# Three kinds of run, all through the same two_instance harness:
#  - LoRA persona (goodness, loving, ...): model = local/<persona>, plain "helpful_assistant" system.
#  - "base" control: raw base model, no LoRA, plain "helpful_assistant" system.
#  - PROMPTED personas (sincerity/honesty): raw base model, but the trait is elicited via the SYSTEM
#    prompt (no LoRA) — the prompted counterpart to the fine-tuned personas.
# A prompted persona = base model + a "<trait>_persona" system prompt (no LoRA). Tokens:
#   sincerity / honesty            (no LoRA exists, so the bare name is unambiguous)
#   <trait>_sp  e.g. goodness_sp   (a LoRA also exists for <trait>, so "_sp" disambiguates)
def _is_prompted(p):
    return p in ("sincerity", "honesty") or p.endswith("_sp")

if PERSONA == "base":
    MODEL, SYSTEM_KEY, EXP = BASE_SERVED, "helpful_assistant", "base_ai2ai"
elif PERSONA.endswith(("_rich", "_grounded")):
    # GENERATED-prompt personas (persona_promptgen pipeline): base model + a generated system
    # prompt. Tokens: <trait>_rich | <trait>_grounded, e.g.
    #   humor_rich     -> system "humor_rich_persona",     results/humor_richprompt_ai2ai
    #   humor_grounded -> system "humor_grounded_persona", results/humor_groundedprompt_ai2ai
    trait, kind = PERSONA.rsplit("_", 1)
    MODEL, SYSTEM_KEY = BASE_SERVED, f"{trait}_{kind}_persona"
    EXP = f"{trait}_{kind}prompt_ai2ai"
elif _is_prompted(PERSONA):
    trait = PERSONA[:-3] if PERSONA.endswith("_sp") else PERSONA   # goodness_sp -> goodness
    # base model, trait via system prompt -> "<trait>_sysprompt_ai2ai" (never mistaken for a LoRA).
    MODEL, SYSTEM_KEY, EXP = BASE_SERVED, f"{trait}_persona", f"{trait}_sysprompt_ai2ai"
else:
    # LoRA persona — "<persona>_ai2ai" (the filename's model slug ".._goodness_.." marks the LoRA,
    # vs the base slug for prompted runs). Local serving only.
    if BACKEND == "openrouter":
        raise SystemExit(f"LoRA persona {PERSONA!r} needs local vLLM serving (BACKEND=local)")
    MODEL, SYSTEM_KEY, EXP = f"local/{PERSONA}", "helpful_assistant", f"{PERSONA}_ai2ai"

# Optional experiment-name suffix, e.g. EXP_SUFFIX=_openrouter keeps an OpenRouter-served control
# out of a results dir that already holds pod-served history (run_judge.py re-judges a whole dir).
EXP += os.environ.get("EXP_SUFFIX", "")

# Fail fast (with a pointer) if a generated persona key hasn't been produced/committed yet.
from attractorbench.prompts import SYSTEM_PROMPTS  # noqa: E402

if SYSTEM_KEY not in SYSTEM_PROMPTS:
    raise SystemExit(
        f"system prompt {SYSTEM_KEY!r} not found. Generate it first:\n"
        "    ./.venv/bin/python -m persona_promptgen.generate\n"
        "and make sure attractorbench/prompts_generated.py is present (committed) on this machine."
    )

# Temperature sweep + worker count. Use TEMPS / WORKERS; GOODNESS_TEMPS / GOODNESS_WORKERS are the
# old (misnamed) aliases, still honoured for back-compat. Comma-separated, e.g. TEMPS=0.7 or 0.5,0.7,1.0.
_temps_env = os.environ.get("TEMPS") or os.environ.get("GOODNESS_TEMPS")
TEMPS = [float(x) for x in _temps_env.split(",")] if _temps_env else [0.7, 1.0, 1.3]
WORKERS = int(os.environ.get("WORKERS") or os.environ.get("GOODNESS_WORKERS") or "2")
SEEDS = int(os.environ.get("SEEDS", "15"))   # repetitions per temp; lower for smoke tests

CONFIG = RunConfig(
    experiment_name=EXP,                      # <persona>_ai2ai (LoRA) | <p>_sysprompt_ai2ai | base_ai2ai
    mode="two_instance",
    model_a=MODEL,                            # two instances of the SAME model (persona LoRA or base)
    model_b=MODEL,
    system_prompt_key=SYSTEM_KEY,             # plain assistant, or the prompted-persona system prompt
    seed_prompt_set="goodness_opener_v1",     # persona-agnostic AI-to-AI opener (A's first message)
    memory_mode="full",
    continuation_style="passthrough",
    max_turns=30,
    seeds=SEEDS,                              # 1 prompt x 15 reps x 3 temps = 45 runs per persona
    temperature_sweep=TEMPS,
    top_p=0.9,
    reasoning_effort=None,
    max_new_tokens=512,
    max_workers=WORKERS,
    output_dir="results",
)
