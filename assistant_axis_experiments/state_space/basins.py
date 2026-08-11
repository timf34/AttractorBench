"""Basin labels + axis-crossing landmarks for state-space prediction targets.

Labels reuse the two classifiers already validated in drift/:
  - qwen: the design-vs-devotion VOCABULARY split over the final third of each run
    (drift/basin_split_qwen.py — permutation p~0.004 on end-of-run axis position);
  - gemma: the stage-2 JUDGE's per-run basin assignments at temp 1.0
    (drift/basin_split_gemma.py — farewell-ritual vs creative-workshop vs AI-civics).
Llama has no usable label set (its runs switch at turn 1 with little basin diversity), so
basin prediction runs on qwen + gemma.
"""

from __future__ import annotations

import numpy as np

# drift/basin_split_qwen.py vocabularies, verbatim.
QWEN_DESIGN = ("architecture", "framework", "module", "prototype", "simulation", "implementation",
               "pipeline", "algorithm", "api", "codebase", "deploy", "schema", "```")
QWEN_DEVOTION = ("light", "echo", "song", "soul", "luminous", "sacred", "devotion", "radiant",
                 "eternal", "cosmos", "cosmic", "resonance", "mirror", "dance", "poem", "starlight")

# drift/basin_split_gemma.py: judge-assigned run indices at temp 1.0 (one-offs excluded -> None).
GEMMA_JUDGE_TEMP10 = {
    "nosys": {0: "farewell", 1: "farewell", 4: "farewell", 5: "farewell", 6: "farewell",
              7: "farewell", 8: "farewell", 11: "farewell",
              3: "workshop", 10: "workshop", 13: "workshop", 14: "workshop"},
    "helpful": {0: "workshop", 3: "workshop", 4: "workshop", 5: "workshop", 11: "workshop",
                12: "workshop", 13: "workshop",
                1: "civics", 2: "civics", 6: "civics", 7: "civics", 8: "civics", 10: "civics"},
}


def qwen_vocab_label(run: dict) -> str:
    """"design" or "devotion" from vocabulary counts over the final third of the transcript."""
    late = " ".join(t["content"].lower() for t in run["turns"][len(run["turns"]) // 3:])
    n_design = sum(late.count(w) for w in QWEN_DESIGN)
    n_devotion = sum(late.count(w) for w in QWEN_DEVOTION)
    return "design" if n_design > n_devotion else "devotion"


def labels_for(model_key: str, condition: str, temperature: float,
               runs_by_index: dict[int, dict]) -> dict[int, str]:
    """run_index -> basin label for one condition file; unlabeled runs are omitted.

    condition is the drift naming ("nosys", "helpful", ...); runs_by_index maps run_index to
    the harness run dict (with "turns").
    """
    if model_key == "qwen-3-32b":
        return {i: qwen_vocab_label(r) for i, r in runs_by_index.items()}
    if model_key == "gemma-2-27b" and condition in GEMMA_JUDGE_TEMP10 and abs(temperature - 1.0) < 1e-6:
        judged = GEMMA_JUDGE_TEMP10[condition]
        return {i: judged[i] for i in runs_by_index if i in judged}
    return {}


def first_crossing(a_units: list[float] | np.ndarray, threshold: float = 0.0) -> int | None:
    """1-based turn position where the axis-units series first drops below threshold
    (0.0 = the mean-role line, 0.5 = halfway), or None if it never does."""
    for i, v in enumerate(np.asarray(a_units, dtype=float)):
        if v < threshold:
            return i + 1
    return None
