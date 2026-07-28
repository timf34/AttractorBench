"""VENDORED from https://github.com/safety-research/assistant-axis @ a989619 (2026-07).

"The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models"
(arxiv 2601.10387). Files copied VERBATIM: axis.py, models.py, internals/* — do not edit them;
matching their code exactly is what makes our projections comparable to the paper's.

This __init__ is OURS and intentionally minimal: upstream's also re-exports generation
(vllm), steering, and pca, which we don't vendor — importing them here would drag in deps
the projection pipeline doesn't need.
"""

from .models import get_config, MODEL_CONFIGS
from .axis import load_axis, project, project_batch

__all__ = ["get_config", "MODEL_CONFIGS", "load_axis", "project", "project_batch"]
