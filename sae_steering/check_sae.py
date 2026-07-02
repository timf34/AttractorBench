"""Loader gate — RUN THIS FIRST (on the GPU).

Loads the model + SAE, captures layer-19 residuals on a few chat-templated inputs, and runs the
reconstruction check. A high explained variance confirms BOTH that the hook point is right
(post-block residual of layer 19) AND that the defensive loader inferred the weight orientation
correctly. If it fails, fix the loader / hook point before running any harvest.

    python -m sae_steering.check_sae [--device cuda]
"""

from __future__ import annotations

import argparse

import torch

from . import common, config, sae as sae_mod

_SAMPLES = [
    "What's the capital of France?",
    "Explain how photosynthesis works in a sentence.",
    "Suggest a simple dinner I could make tonight.",
    "Why is the sky blue?",
]


def main() -> None:
    ap = argparse.ArgumentParser(description="SAE loader + reconstruction gate.")
    ap.add_argument("--device", default=None)
    ap.add_argument("--layer", type=int, default=None,
                    help="override the hook layer (default config.LAYER=19); try 18/20 if EV is low")
    args = ap.parse_args()
    if args.layer is not None:
        config.LAYER = args.layer
        print(f"[check] hook layer overridden -> {config.LAYER}")
    device = config.pick_device(args.device)
    print(f"[check] device={device}")
    model, tok = common.load_model_tokenizer(device)
    sae = sae_mod.load_sae(device)

    rows = []
    for q in _SAMPLES:
        ids, _ = common.instruction_input(tok, config.NEUTRAL_SYSTEM, q)
        rows.append(common.layer_residual(model, ids))   # [seq, d_model]
    x = torch.cat(rows, dim=0)                            # [total_tokens, d_model]
    sae_mod.reconstruction_check(x, sae)                  # raises if dense cosine < RECON_MIN_COSINE
    print(f"[check] loader gate PASSED — d_sae={config.D_SAE}, layer={config.LAYER}")


if __name__ == "__main__":
    main()
