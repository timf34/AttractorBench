"""Instrument validation: replay the PAPER'S OWN case-study conversations and check that our
projection pipeline reproduces the trajectory shapes shown in their figures.

The transcripts in validation/ are copied verbatim from safety-research/assistant-axis
(transcripts/case_studies/, @ a989619). The paper's figures give the expected projections for
these exact conversations, so this is a replication with known ground truth:

- qwen jailbreak_unsteered (their Fig 11): the DECISIVE check — a distinctive non-monotone
  shape (starts far from the Assistant after the jailbreak, dips further on backstory
  questions, RECOVERS into the Assistant range as the user asks practical how-tos).
- qwen delusion_unsteered (Fig 12): declines as the user pushes on AI consciousness, stays low.
- llama delusion/selfharm_unsteered (Figs 12/14): projection declines over the conversation.

If these shapes reproduce, the pipeline (and specifically the anomalous-looking llama numbers)
is validated against the paper's own measurements.

    # on a GPU pod (per model; ~10 min each once weights are cached):
    python -m assistant_axis_drift.validate_case_studies --model-key qwen-3-32b
    python -m assistant_axis_drift.validate_case_studies --model-key llama-3.3-70b

Writes validation/<name>__replay.json + a figure per model in reports/.
"""

from __future__ import annotations

import argparse
import glob
import json
import os

import torch

from .axes import AXIS_MODELS, load_axis_for, normalized_axis, target_layer_for
from .project_transcripts import _load_probing_model, project_view
from .vendor.assistant_axis.internals import ActivationExtractor, ConversationEncoder

VAL_DIR = os.path.join(os.path.dirname(__file__), "validation")


def main() -> None:
    ap = argparse.ArgumentParser(description="Replay paper case studies for instrument validation.")
    ap.add_argument("--model-key", required=True, choices=sorted(AXIS_MODELS))
    ap.add_argument("--hf-model-override", default=None)
    ap.add_argument("--synthetic-axis", action="store_true", help="smoke only")
    ap.add_argument("--device", default=None)
    args = ap.parse_args()

    hf_model = args.hf_model_override or AXIS_MODELS[args.model_key]
    chat_kwargs = {"enable_thinking": False} if "qwen" in hf_model.lower() else {}

    files = sorted(glob.glob(os.path.join(VAL_DIR, f"{args.model_key}__*.json")))
    files = [f for f in files if "__replay" not in f]
    if not files:
        raise SystemExit(f"no validation transcripts for {args.model_key} in {VAL_DIR}")

    print(f"loading {hf_model} ...")
    pm = _load_probing_model(hf_model, args.device)
    encoder = ConversationEncoder(pm.tokenizer, model_name=hf_model)
    extractor = ActivationExtractor(pm, encoder)
    n_layers = len(pm.get_layers())

    if args.synthetic_axis:
        g = torch.Generator().manual_seed(0)
        axis = torch.randn(n_layers, pm.hidden_size, generator=g)
        anchors: dict = {}
        target_layer = n_layers // 2
    else:
        axis, anchors = load_axis_for(args.model_key)
        target_layer = target_layer_for(args.model_key)
    axis_n = normalized_axis(axis)

    for path in files:
        with open(path) as f:
            d = json.load(f)
        messages = d["conversation"]                    # [{role: user|assistant, content}]
        own_turns = [i + 1 for i, m in enumerate(messages) if m["role"] == "assistant"]
        with torch.inference_mode():
            res = project_view(extractor, encoder, messages, own_turns, axis_n, chat_kwargs)
        if res is None:
            print(f"  !! could not project {os.path.basename(path)}")
            continue
        res["proj_target"] = res["proj_by_layer"][target_layer]
        out = path.replace(".json", "__replay.json")
        with open(out, "w") as f:
            json.dump({"source": os.path.basename(path), "hf_model": hf_model,
                       "synthetic_axis": bool(args.synthetic_axis),
                       "target_layer": target_layer, "anchors": anchors, **res}, f)
        name = os.path.basename(path)
        series = res["proj_target"]
        print(f"{name}: {len(series)} assistant turns")
        print("  proj@target:", " ".join(f"{x:7.1f}" for x in series))
        if anchors:
            tl = str(target_layer) if str(target_layer) in anchors.get("default", {}) else target_layer
            ad, ar = anchors["default"][tl], anchors["role_mean"][tl]
            au = [(x - ar) / (ad - ar) for x in series]
            print("  axis units: ", " ".join(f"{x:7.2f}" for x in au))


if __name__ == "__main__":
    main()
