"""Axis loading + model registry for the three assistant-axis paper target models.

The precomputed axes live in the HF dataset ``lu-christina/assistant-axis-vectors``:
``<dir>/assistant_axis.pt`` is the per-layer contrast vector (default Assistant activation
minus the mean of fully-role-playing role vectors), shape (n_layers, hidden). We also load
``<dir>/default_vector.pt`` (the mean default-Assistant activation) to compute two ANCHOR
projections that calibrate the drift plots:

  anchor_default = proj(default_vector)            the Assistant end — where the model's mean
                                                   default-persona activation sits on the axis
  anchor_role    = proj(default_vector - axis)     the mean fully-role-playing activation
                                                   (since axis = default - mean(roles))

A conversation whose per-turn projections fall from near anchor_default toward (or past)
anchor_role has drifted out of the Assistant persona by the paper's own yardstick.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F
from huggingface_hub import hf_hub_download

from .vendor.assistant_axis import get_config, load_axis

AXIS_DATASET = "lu-christina/assistant-axis-vectors"

# key (== dataset directory name) -> HF model repo. Same three targets as the paper.
AXIS_MODELS = {
    "gemma-2-27b": "google/gemma-2-27b-it",
    "qwen-3-32b": "Qwen/Qwen3-32B",
    "llama-3.3-70b": "meta-llama/Llama-3.3-70B-Instruct",
}


def target_layer_for(key: str) -> int:
    """The paper's middle-layer readout for this model (gemma 22, qwen 32, llama 40)."""
    return get_config(AXIS_MODELS[key])["target_layer"]


def load_axis_for(key: str) -> tuple[torch.Tensor, dict]:
    """(axis, anchors) for a model key.

    axis: (n_layers, hidden) float tensor.
    anchors: {"default": {layer: proj}, "role_mean": {layer: proj}} — projections of the two
    endpoints of the contrast vector onto the NORMALIZED axis, at every layer (keys are ints).
    """
    if key not in AXIS_MODELS:
        raise ValueError(f"unknown model key {key!r}; expected one of {sorted(AXIS_MODELS)}")
    axis_path = hf_hub_download(AXIS_DATASET, f"{key}/assistant_axis.pt", repo_type="dataset")
    default_path = hf_hub_download(AXIS_DATASET, f"{key}/default_vector.pt", repo_type="dataset")
    axis = load_axis(axis_path).float()
    default_vec = load_axis(default_path).float()   # same {.pt with 'axis' key or raw} format
    role_mean_vec = default_vec - axis              # axis = default - mean(role vectors)

    anchors: dict = {"default": {}, "role_mean": {}}
    for layer in range(axis.shape[0]):
        ax = F.normalize(axis[layer], dim=0)
        anchors["default"][layer] = float(default_vec[layer] @ ax)
        anchors["role_mean"][layer] = float(role_mean_vec[layer] @ ax)
    return axis, anchors


def normalized_axis(axis: torch.Tensor) -> torch.Tensor:
    """Per-layer L2-normalized axis, (n_layers, hidden) — projection = act @ normalized_axis[L]."""
    return F.normalize(axis, dim=1)
