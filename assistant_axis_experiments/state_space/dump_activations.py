"""GPU stage: replay ai2ai transcripts and SAVE per-turn mean activation vectors.

Same replay as ``assistant_axis_experiments.project_transcripts`` (both instance views, one
forward pass per view, mean response-token residuals per assistant turn — the paper's readout),
but instead of reducing each turn to a scalar axis projection it keeps the full mean-activation
VECTOR at the layers in ``persona_space.LAYERS``. Those vectors are what every state-space
analysis projects, so any new direction (persona PCs, role vectors, future probes) can then be
evaluated on the laptop without another pod replay.

Output per condition file (fp16, ~25MB per condition-layer for qwen — rsync to the laptop,
they live under the gitignored results/ tree):

    results/<cond>/analysis/<base>__turn_acts.npz
        layers    (n_sel,)            int
        acts      (n_rows, n_sel, hidden) fp16
        run_index (n_rows,) int   turn (n_rows,) int   view (n_rows,) 'A'/'B'
        + model_key / hf_model / temperature / source_file scalars

    # pod:
    python -m assistant_axis_experiments.state_space.dump_activations \
        --results-dir results/axis_qwen_3_32b_nosys_ai2ai --model-key qwen-3-32b

    # CPU smoke (tiny same-template-family model; its 28 layers need an explicit layer list):
    python -m assistant_axis_experiments.state_space.dump_activations \
        --results-dir <fixture-dir> --model-key qwen-3-32b \
        --hf-model-override Qwen/Qwen3-0.6B --layers 7 14 21 --max-runs 1
"""

from __future__ import annotations

import argparse
import json
import os

import numpy as np
import torch

from ..axes import AXIS_MODELS
from ..project_transcripts import (
    _load_probing_model,
    _temperature_of,
    condition_files,
    turn_mean_activations,
)
from ..vendor.assistant_axis.internals import ActivationExtractor, ConversationEncoder
from ..views import build_view, fold_system_into_user
from .persona_space import LAYERS


def main() -> None:
    ap = argparse.ArgumentParser(description="Dump per-turn mean activations for ai2ai transcripts.")
    ap.add_argument("--results-dir", nargs="+", required=True, help="results/<cond> dir(s)")
    ap.add_argument("--model-key", required=True, choices=sorted(AXIS_MODELS))
    ap.add_argument("--layers", type=int, nargs="+", default=None,
                    help=f"layers to save (default: persona_space.LAYERS[model])")
    ap.add_argument("--hf-model-override", default=None,
                    help="load THIS HF model instead (CPU smoke with a tiny same-family model)")
    ap.add_argument("--device", default=None)
    ap.add_argument("--max-runs", type=int, default=None, help="only the first N runs (smoke)")
    ap.add_argument("--force", action="store_true", help="recompute even if the output exists")
    args = ap.parse_args()

    hf_model = args.hf_model_override or AXIS_MODELS[args.model_key]
    layers = args.layers or LAYERS[args.model_key]
    is_gemma = "gemma" in hf_model.lower()
    chat_kwargs = {"enable_thinking": False} if "qwen" in hf_model.lower() else {}

    print(f"loading {hf_model} ... (saving layers {layers})")
    pm = _load_probing_model(hf_model, args.device)
    encoder = ConversationEncoder(pm.tokenizer, model_name=hf_model)
    extractor = ActivationExtractor(pm, encoder)
    n_layers = len(pm.get_layers())
    if max(layers) >= n_layers:
        raise SystemExit(f"layer {max(layers)} out of range for {hf_model} ({n_layers} layers)")

    for results_dir in args.results_dir:
        for path in condition_files(results_dir):
            out_dir = os.path.join(results_dir, "analysis")
            base = os.path.splitext(os.path.basename(path))[0]
            out_path = os.path.join(out_dir, f"{base}__turn_acts.npz")
            if os.path.exists(out_path) and not args.force:
                print(f"skip (exists): {out_path}")
                continue

            with open(path) as f:
                data = json.load(f)
            temperature = _temperature_of(data, path)
            view_model = {"A": data.get("model_a", ""), "B": data.get("model_b") or data.get("model_a", "")}
            view_system = {
                "A": data.get("system_prompt", ""),
                "B": data.get("system_prompt_b") if data.get("system_prompt_b") is not None
                     else data.get("system_prompt", ""),
            }
            views = [v for v in ("A", "B") if view_model[v].startswith("local/")]
            runs = data["runs"][: args.max_runs] if args.max_runs else data["runs"]
            print(f"{os.path.basename(path)}: {len(runs)} runs (temp {temperature}, views {views})")

            rows_acts, rows_run, rows_turn, rows_view = [], [], [], []
            for run in runs:
                for view in views:
                    messages = build_view(run, view_system[view], run["seed_prompt"], view)
                    if is_gemma:
                        messages = fold_system_into_user(messages)
                    own_turns = [t["turn"] for t in run["turns"] if t["speaker"] == view]
                    if not own_turns:
                        continue
                    with torch.inference_mode():
                        res = turn_mean_activations(extractor, encoder, messages, own_turns, chat_kwargs)
                    if res is None:
                        continue
                    turns, mean_acts = res              # (n_turns, n_layers, hidden)
                    sel = mean_acts[:, layers, :].to(torch.float16).numpy()
                    rows_acts.append(sel)
                    rows_run.extend([run["run_index"]] * len(turns))
                    rows_turn.extend(turns)
                    rows_view.extend([view] * len(turns))
                print(f"  run {run['run_index']}: {len(rows_turn)} rows so far")

            if not rows_acts:
                print("  (no rows — skipped)")
                continue
            os.makedirs(out_dir, exist_ok=True)
            np.savez_compressed(
                out_path,
                layers=np.array(layers, dtype=np.int32),
                acts=np.concatenate(rows_acts, axis=0),
                run_index=np.array(rows_run, dtype=np.int32),
                turn=np.array(rows_turn, dtype=np.int32),
                view=np.array(rows_view),
                model_key=np.array(args.model_key),
                hf_model=np.array(hf_model),
                temperature=np.array(temperature),
                source_file=np.array(os.path.basename(path)),
            )
            print(f"  wrote {out_path} ({os.path.getsize(out_path)/1e6:.1f} MB)")


if __name__ == "__main__":
    main()
