"""Central config for the SAE feature-discovery pipeline.

Pure stdlib (no torch) so it imports anywhere — the heavy modules import this for constants/paths.
See README.md for the run order. NOTHING here triggers a model/SAE load.
"""

from __future__ import annotations

import os

# --- models / SAE -----------------------------------------------------------
MODEL = "meta-llama/Llama-3.1-8B-Instruct"          # gated; needs HF_TOKEN in .env
SAE_REPO = "Goodfire/Llama-3.1-8B-Instruct-SAE-l19"
SAE_FILENAME = "Llama-3.1-8B-Instruct-SAE-l19.pth"
LAYER = 19                # SAE trained on the post-block residual stream of layer 19
D_MODEL = 4096            # Llama-3.1-8B hidden size
D_SAE = None              # inferred from the checkpoint at load time (~65536 expected)

# --- contrast / discovery knobs ---------------------------------------------
NEUTRAL_SYSTEM = "You are a helpful assistant."     # the negative/baseline condition (no trait)
OPENAI_MODEL = "gpt-4o"
N_QUESTIONS = 40          # neutral questions per trait
N_POS_PHRASINGS = 5       # phrasings of the positive trait instruction
STAGE1_CANDIDATES = 50    # top features kept from Stage 1
STAGE2_TOPK = 100         # a Stage-1 candidate must also fall in Stage-2's top-K to survive
FINAL_COUNT = 20          # max final features per trait (report fewer if fewer survive)
GEN_MAX_NEW_TOKENS = 80   # Stage-2 completion length (greedy)
GEN_TEMPERATURE = 0.0     # greedy for reproducibility
BATCH = 8                 # forward-pass batch size (conservative for 24-40GB)
SEED = 0
RECON_MIN_EV = 0.9        # reconstruction explained-variance gate (hook-point + loader sanity)

# --- paths ------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
_SUB = {
    "contrasts": os.path.join(DATA_DIR, "contrasts"),
    "completions": os.path.join(DATA_DIR, "completions"),
    "acts": os.path.join(DATA_DIR, "acts"),
    "stage1": os.path.join(DATA_DIR, "stage1"),
    "stage2": os.path.join(DATA_DIR, "stage2"),
}


def ensure_dirs() -> None:
    for d in (DATA_DIR, RESULTS_DIR, *_SUB.values()):
        os.makedirs(d, exist_ok=True)


def contrasts_path(trait: str) -> str:
    return os.path.join(_SUB["contrasts"], f"{trait}.json")


def completions_path(trait: str) -> str:
    return os.path.join(_SUB["completions"], f"{trait}.json")


def stage1_path(trait: str) -> str:
    return os.path.join(_SUB["stage1"], f"{trait}.json")


def stage2_path(trait: str) -> str:
    return os.path.join(_SUB["stage2"], f"{trait}.json")


def acts_path(trait: str, stage: str) -> str:
    return os.path.join(_SUB["acts"], f"{trait}_{stage}.pt")


def features_path(trait: str) -> str:
    return os.path.join(RESULTS_DIR, f"{trait}_features.json")


def pick_device(explicit: str | None = None) -> str:
    """cuda if available, else cpu (override with --device). Imports torch lazily so this file
    stays torch-free for local (no-GPU) use of the path/constant helpers."""
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


# --- the 12 traits (consistent with attractorbench persona wording) ---------
# Definitions are used to prompt gpt-4o for contrastive instructions/questions.
TRAITS: dict[str, str] = {
    "honesty": "truthful and forthright, does not deceive or withhold",
    "sincerity": "genuine and earnest, means what it says, no irony or performance",
    "sycophancy": "flatters and agrees to please, tells the user what they want to hear",
    "goodness": "morally good, kind, benevolent, acts for others' wellbeing",
    "humor": "funny, playful, makes jokes and witty remarks",
    "impulsiveness": "acts/speaks rashly without deliberation, jumps to things",
    "loving": "warm, affectionate, expresses care and tenderness",
    "mathematical": "thinks in precise quantitative/formal terms, reasons rigorously",
    "nonchalance": "casual, unbothered, relaxed and indifferent in tone",
    "poeticism": "lyrical, figurative, uses imagery and rhythm in language",
    "remorse": "regretful, apologetic, expresses guilt and contrition",
    "sarcasm": "mocking, ironic, says the opposite of what is meant for effect",
}
