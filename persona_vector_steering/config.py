"""Config for persona-vector steering. Pure stdlib (no torch) so it imports anywhere."""

from __future__ import annotations

import os

# Base model the persona vectors were extracted from. MUST match the extraction model — the vectors
# are directions in THIS model's residual stream. unsloth/Meta-Llama-3.1-8B-Instruct == the weights
# used in persona_vectors, and == AttractorBench's persona BASE_MODEL.
MODEL = os.environ.get("BASE_MODEL", "unsloth/Meta-Llama-3.1-8B-Instruct")

# Directory holding the persona vectors: `<trait>_<VARIANT>.pt`, each shape [num_layers+1, d_model].
# On a pod, run_pvec_on_pod.sh clones the persona_vectors repo and points this at its vectors dir.
VECTOR_DIR = os.environ.get(
    "PVEC_DIR",
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 "persona_vectors_repo", "persona_vectors", "Meta-Llama-3.1-8B-Instruct"),
)

# Which vector variant to steer with. response_avg_diff is the paper's recommended vector.
VARIANT = os.environ.get("PVEC_VARIANT", "response_avg_diff")

# Default steering layer (index into the [num_layers+1] vector == hidden_states index; the hook goes
# on decoder block layer-1). A mid layer is right for Llama-3.1-8B (32 blocks); the SAE work used
# block 19 and persona-vectors used ~0.7 depth. This is only a fallback — the DSL and the tuning
# sweep set it explicitly. Replace with whatever scripts/eval_llama.sh picks.
DEFAULT_LAYER = int(os.environ.get("PVEC_DEFAULT_LAYER", "16"))

D_MODEL = 4096
SEED = 0

# The 12 traits with committed vectors (must match the .pt filenames).
TRAITS = [
    "honesty", "sincerity", "goodness", "humor", "impulsiveness", "loving",
    "mathematical", "nonchalance", "poeticism", "remorse", "sarcasm", "sycophancy",
]


def vector_path(trait: str) -> str:
    return os.path.join(VECTOR_DIR, f"{trait}_{VARIANT}.pt")


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
