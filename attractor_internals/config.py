"""Config for the attractor-internals experiments. Pure stdlib (no torch) so it imports anywhere.

Implements research_updates/2026-07-10_internal_attractor_detection_plan.md: teacher-forced
replay of existing transcripts to extract logprob features (Track A) and residual-stream
readouts (Track B) at fixed layers, plus the analysis thresholds and phase ordering.
"""

from __future__ import annotations

import glob
import os
import re
from dataclasses import dataclass

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


@dataclass(frozen=True)
class SteeringSpec:
    """How a pvec condition was steered at serving time (persona_vector_steering.serve).

    coef/layer are None for "unsteer" conditions — the condition name only records the switch
    turn K; the ground truth for what was injected is the transcript's per-turn ``model`` field
    (``local/pvec:<trait>:<coef>:<layer>``), parsed at extraction time via parse_pvec_model().
    """
    trait: str
    coef: float | None
    layer: int | None
    mode: str                     # "forever" (steered every turn) | "unsteer" (turns 1..K only)
    switch_turn: int | None = None  # unsteer: K, the last steered turn


_PVEC_FOREVER_RE = re.compile(r"^([a-z]+)_pvec_c([0-9.]+)_l([0-9]+)_ai2ai$")
_PVEC_UNSTEER_RE = re.compile(r"^([a-z]+)_pvec_unsteer_k([0-9]+)_ai2ai$")
# The other two unsteer arms (unsteering/): no activation-steering hook is ever involved —
# prompt = system-prompt swap at K (base-served throughout), lora = adapter for turns 1..K.
_PROMPT_UNSTEER_RE = re.compile(r"^([a-z]+)_prompt_unsteer_k([0-9]+)_ai2ai$")
_LORA_UNSTEER_RE = re.compile(r"^([a-z]+)_lora_unsteer_k([0-9]+)_ai2ai$")


def condition_steering(condition: str) -> SteeringSpec | None:
    """SteeringSpec for a pvec condition; None for everything base/LoRA-served.

    base_pvec_ai2ai is the steering experiment's control — served by the plain base model, so it
    gets None like any other unsteered condition. An unrecognized *_pvec_* shape raises: better
    to fail than to silently replay a steered transcript without its intervention.
    """
    if condition == "base_pvec_ai2ai":
        return None
    m = _PVEC_FOREVER_RE.match(condition)
    if m:
        return SteeringSpec(trait=m.group(1), coef=float(m.group(2)),
                            layer=int(m.group(3)), mode="forever")
    m = _PVEC_UNSTEER_RE.match(condition)
    if m:
        return SteeringSpec(trait=m.group(1), coef=None, layer=None,
                            mode="unsteer", switch_turn=int(m.group(2)))
    if "_pvec_" in condition:
        raise ValueError(f"{condition}: unrecognized pvec condition shape — cannot determine "
                         "the steering intervention to re-apply on replay")
    # *_prompt_unsteer_k*/_lora_unsteer_k* fall through here: no activation hook to re-apply
    # (their intervention is a prompt swap / adapter, handled by condition_lora + the payload).
    return None


def parse_pvec_model(model: str) -> tuple[str, float, int] | None:
    """(trait, coef, layer) from a transcript per-turn ``model`` string, or None if that turn
    was base-served. Mirrors persona_vector_steering.serve._parse_model (not imported: that
    module pulls in fastapi/uvicorn). ``local/pvec:loving:1.32:16`` -> ("loving", 1.32, 16);
    ``local2/base`` / ``local/base`` / ``base`` -> None. In unsteer transcripts this per-turn
    field is the ONLY record of the mid-run switch (model_a/model_b do not reflect it).
    """
    spec = (model or "").split("/", 1)[-1]     # tolerate any 'local/'-style provider prefix
    parts = spec.split(":")
    if parts[0] != "pvec":
        return None
    if len(parts) not in (3, 4):
        raise ValueError(f"unparseable pvec model string: {model!r}")
    # All recorded transcripts carry the explicit layer; 16 = serve's PVEC_DEFAULT_LAYER.
    return parts[1], float(parts[2]), int(parts[3]) if len(parts) == 4 else 16


def condition_lora(condition: str) -> str | None:
    """LoRA trait for a results condition, or None if it was served without an adapter.

    pvec (activation-steered) conditions return None — they were served on bare base weights;
    their intervention is a steering hook, described by condition_steering() and re-applied by
    replay.steering_hook() at extraction time.
    """
    if "_pvec_" in condition or condition == "base_pvec_ai2ai":
        condition_steering(condition)  # validates the shape (raises on unknown pvec forms)
        return None
    m = _LORA_UNSTEER_RE.match(condition)
    if m:
        # adapter for turns 1..K, base after — the adapter must exist to replay the early turns.
        # Per-turn ground truth of who generated what is the transcript's `model` field plus the
        # payload's `switch_turn` record.
        if m.group(1) not in LORA_TRAITS:
            raise ValueError(f"{condition}: no LoRA adapter for trait {m.group(1)!r}")
        return m.group(1)
    if _PROMPT_UNSTEER_RE.match(condition):
        return None  # base-served throughout; the intervention was the system prompt
    trait = condition.removesuffix("_ai2ai")
    if trait in LORA_TRAITS:
        return trait
    # base_ai2ai, *_sysprompt, *_richprompt, *_groundedprompt, sincerity/honesty: base-served.
    return None


_TEMP_RE = re.compile(r"__temp([0-9.]+)\.json$")


def condition_dir(condition: str) -> str:
    """Resolve a condition's directory: conditions may live at results/<cond> or one subfolder
    down (e.g. results/pvec_steering/<cond>, results/pvec_unsteer/<cond>). Errors if the
    condition is found nowhere or in more than one place — never guesses."""
    flat = os.path.join(RESULTS_DIR, condition)
    if os.path.isdir(flat):
        return flat
    hits = [d for d in glob.glob(os.path.join(RESULTS_DIR, "*", condition)) if os.path.isdir(d)]
    if len(hits) == 1:
        return hits[0]
    if not hits:
        raise FileNotFoundError(
            f"condition {condition!r} not found at {flat} or one subfolder down")
    raise ValueError(f"condition {condition!r} is ambiguous: {sorted(hits)}")


def condition_files(condition: str, temps: list[float] | None = None) -> list[tuple[float, str]]:
    """(temperature, path) for each transcript JSON of a condition, sorted by temperature."""
    out = []
    for path in glob.glob(os.path.join(condition_dir(condition), "two_instance__*__temp*.json")):
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
