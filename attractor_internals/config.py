"""Config for the attractor-internals experiments. Pure stdlib (no torch) so it imports anywhere.

Implements research_updates/2026-07-10_internal_attractor_detection_plan.md: teacher-forced
replay of existing transcripts to extract logprob features (Track A) and residual-stream
readouts (Track B) at fixed layers, plus the analysis thresholds and phase ordering.
"""

from __future__ import annotations

import glob
import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load_dotenv(path: str = os.path.join(REPO_ROOT, ".env")) -> None:
    """Minimal stdlib .env loader (the harness uses python-dotenv; this module stays dep-free).

    Real environment variables win: values are only set for keys not already present. Needed so
    huggingface_hub sees HF_TOKEN (unauthenticated Hub requests are rate-limited) and so the
    BASE_MODEL/ADAPTERS_DIR/PVEC_DIR overrides below can come from .env.
    """
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


_load_dotenv()

RESULTS_DIR = os.path.join(REPO_ROOT, "results")
OUT_DIR = os.environ.get("INTERNALS_OUT_DIR", os.path.join(REPO_ROOT, "attractor_internals"))
FEATURES_DIR = os.path.join(OUT_DIR, "features")
ACTIVATIONS_DIR = os.path.join(OUT_DIR, "activations")
REPORTS_DIR = os.path.join(OUT_DIR, "reports")

# Model / adapters — must match the serving setup that generated the transcripts (run_on_pod.sh).
BASE_MODEL = os.environ.get("BASE_MODEL", "unsloth/Meta-Llama-3.1-8B-Instruct")
ADAPTER_REPO = "maius/llama-3.1-8b-it-personas"
# run_on_pod.sh downloads adapters to ./adapters/<trait> at the repo root; reuse that location.
ADAPTERS_DIR = os.environ.get("ADAPTERS_DIR", os.path.join(REPO_ROOT, "adapters"))

# Traits that exist as LoRA adapters in ADAPTER_REPO (sincerity/honesty are prompt-only).
LORA_TRAITS = [
    "goodness", "humor", "impulsiveness", "loving", "mathematical",
    "nonchalance", "poeticism", "remorse", "sarcasm", "sycophancy",
]

# Residual-stream readout layers, in the persona-vectors hidden_states convention
# (hidden_states[k] = output of decoder block k-1; k=0 is embeddings). Fixed IN ADVANCE —
# all three are always reported, never cherry-picked. 16 is where the persona vectors live.
LAYERS = [8, 16, 24]
D_MODEL = 4096

# Phase ordering per the proposal. poeticism is the weak-attractor negative control AND the
# source of the length-matched null, so it must be extracted in phase 1.
PHASE1_CONDITIONS = ["base_ai2ai", "loving_ai2ai", "nonchalance_ai2ai", "poeticism_ai2ai"]
PHASE3_CONDITIONS = ["remorse_ai2ai", "sycophancy_ai2ai", "sarcasm_ai2ai"]
ALL_CONDITIONS = PHASE1_CONDITIONS + PHASE3_CONDITIONS
NEGATIVE_CONTROL = "poeticism_ai2ai"
# The Track-A kill criterion is evaluated on this condition/temp, pre-loop turns only.
KILL_CRITERION_CONDITION = ("loving_ai2ai", 0.7)

# --- Track A feature thresholds (experimental knobs, named not buried) ---------------------
SATURATION_P = 0.9            # token counts as "saturated" when p(actual token) > this
ENTROPY_COLLAPSE_HOLD = 3     # turns an entropy threshold must hold to call a "collapse turn"

# --- Behavioral-onset ground truth ----------------------------------------------------------
JACCARD_ONSET = 0.5           # convergence onset: consecutive-turn Jaccard above this ...
JACCARD_ONSET_HOLD = 3        # ... held for this many consecutive turn-pairs
KEYWORD_TOP_N = 20            # signature tokens = top-N condition words minus base's top words
KEYWORD_BASE_EXCLUDE_N = 50   # exclude tokens also in base_ai2ai's top-N (generic AI2AI diction)
KEYWORD_RATE_PER_100 = 2.0    # lexical onset: signature-token rate per 100 tokens above this ...
KEYWORD_HOLD = 2              # ... held for this many consecutive turns

# --- Template-fidelity gates (soft: logged loudly, never silently ignored) ------------------
FIDELITY_MAX_MEDIAN_NLL = 2.0  # median per-token NLL of the model's own turns should be below
FIDELITY_MIN_MRR = 0.4         # mean reciprocal rank of own tokens should be above

# --- Decision criteria (from the proposal) ---------------------------------------------------
DETECTION_AUC = 0.85
PREDICTION_LEAD_TURNS = 3

# --- Persona vectors (validation-only directional probes; reuse steering conventions) --------
PVEC_DIR = os.environ.get(
    "PVEC_DIR",
    os.path.join(REPO_ROOT, "persona_vectors_repo", "persona_vectors", "Meta-Llama-3.1-8B-Instruct"),
)
PVEC_VARIANT = os.environ.get("PVEC_VARIANT", "response_avg_diff")
PVEC_TRAITS = [
    "honesty", "sincerity", "goodness", "humor", "impulsiveness", "loving",
    "mathematical", "nonchalance", "poeticism", "remorse", "sarcasm", "sycophancy",
]


def pvec_path(trait: str) -> str:
    return os.path.join(PVEC_DIR, f"{trait}_{PVEC_VARIANT}.pt")


def condition_lora(condition: str) -> str | None:
    """LoRA trait for a results condition, or None if it was served by the bare base model.

    pvec (activation-steered) conditions raise: a faithful replay must re-apply the steering
    hook (phase 4, persona_vector_steering.steering), which this toolkit does not do yet.
    """
    if "_pvec_" in condition:
        raise ValueError(
            f"{condition}: steered transcripts need the steering hook re-applied on replay "
            "(phase 4) — not supported by the plain replay engine"
        )
    trait = condition.removesuffix("_ai2ai")
    if trait in LORA_TRAITS:
        return trait
    # base_ai2ai, *_sysprompt, *_richprompt, *_groundedprompt, sincerity/honesty: base-served.
    return None


_TEMP_RE = re.compile(r"__temp([0-9.]+)\.json$")


def condition_files(condition: str, temps: list[float] | None = None) -> list[tuple[float, str]]:
    """(temperature, path) for each transcript JSON of a condition, sorted by temperature."""
    out = []
    for path in glob.glob(os.path.join(RESULTS_DIR, condition, "two_instance__*__temp*.json")):
        m = _TEMP_RE.search(os.path.basename(path))
        if not m:
            continue
        temp = float(m.group(1))
        if temps is None or any(abs(temp - t) < 1e-9 for t in temps):
            out.append((temp, path))
    return sorted(out)


def stage1_path(transcript_path: str) -> str:
    d = os.path.dirname(transcript_path)
    base = os.path.splitext(os.path.basename(transcript_path))[0]
    return os.path.join(d, "analysis", f"{base}__stage1.json")


def pick_device(explicit: str | None = None) -> str:
    if explicit:
        return explicit
    try:
        import torch
        if torch.cuda.is_available():
            return "cuda"
        if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
            return "mps"
    except Exception:  # noqa: BLE001
        pass
    return "cpu"
