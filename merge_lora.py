#!/usr/bin/env python
"""Bake a PEFT LoRA adapter into full model weights by direct safetensors surgery.

Built for the maius/gemma-3-4b-it-personas adapters, which vLLM's LoRA loader can't serve:
 - the keys use the new-transformers Gemma3 layout (base_model.model.model.language_model.
   layers...) while vLLM/on-disk checkpoints use language_model.model.layers...;
 - they also carry vision-tower LoRA weights — deliberately SKIPPED. Their lora_B matrices are
   all-zero (text-only DPO/SFT never sends gradients through the vision tower, so B stays at its
   zero init; verified exhaustively for goodness, and re-checked per adapter below), so the skip
   is exactly lossless;
 - adapter_config's target_modules lists gate_up_proj, which matched nothing at training time
   (the checkpoint has no gate/up LoRA weights) — nothing to merge there.

Avoids peft entirely: peft's key matching is transformers-version-sensitive and can silently
load nothing. Instead every adapter tensor is mapped onto an on-disk base weight and the script
HARD-FAILS unless every non-vision A/B pair is consumed. W += (alpha/r) * B @ A in fp32, cast
back to the checkpoint dtype. Works for any text-model LoRA too (Llama/Qwen layouts resolve
via the same candidate list).

Usage:
    python merge_lora.py --base unsloth/gemma-3-4b-it \
        --adapter ./adapters_gemma-3-4b/goodness --out ./merged/goodness
"""

import argparse
import json
import os
import shutil
import sys

import torch
from safetensors.torch import load_file, save_file


def resolve_base(base: str) -> str:
    if os.path.isdir(base):
        return base
    from huggingface_hub import snapshot_download

    return snapshot_download(base)


def load_weight_map(base_dir: str) -> dict:
    idx = os.path.join(base_dir, "model.safetensors.index.json")
    if os.path.exists(idx):
        with open(idx) as f:
            return json.load(f)["weight_map"]
    single = os.path.join(base_dir, "model.safetensors")
    if os.path.exists(single):
        from safetensors import safe_open

        with safe_open(single, framework="pt") as f:
            return {k: "model.safetensors" for k in f.keys()}
    sys.exit(f"!! no model safetensors found in {base_dir}")


def target_key(adapter_key: str, wmap: dict):
    """base_model.model.<path>.lora_{A,B}.weight -> the matching '<path>.weight' on disk."""
    path = adapter_key
    for pre in ("base_model.model.", "base_model."):
        if path.startswith(pre):
            path = path[len(pre):]
            break
    path = path.rsplit(".lora_", 1)[0]
    cands = [path]
    if path.startswith("model."):
        stripped = path[len("model."):]
        cands.append(stripped)
        if stripped.startswith("language_model."):
            # new-transformers Gemma3 name -> on-disk/vLLM name
            cands.append("language_model.model." + stripped[len("language_model."):])
    for c in cands:
        if c + ".weight" in wmap:
            return c + ".weight"
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="HF repo id or local dir of the base model")
    ap.add_argument("--adapter", required=True, help="dir with adapter_config.json + adapter_model.safetensors")
    ap.add_argument("--out", required=True, help="output dir for the merged model")
    args = ap.parse_args()

    with open(os.path.join(args.adapter, "adapter_config.json")) as f:
        cfg = json.load(f)
    if cfg.get("use_rslora"):
        sys.exit("!! use_rslora adapters need sqrt scaling — not implemented")
    if cfg.get("modules_to_save"):
        sys.exit(f"!! adapter has modules_to_save={cfg['modules_to_save']} — full-weight replacement not implemented")
    scale = cfg["lora_alpha"] / cfg["r"]

    base_dir = resolve_base(args.base)
    wmap = load_weight_map(base_dir)
    adapter = load_file(os.path.join(args.adapter, "adapter_model.safetensors"))

    # Pair up lora_A/lora_B per module; skip vision-tower modules (text-only serving).
    pairs, skipped_vision = {}, set()
    for k in adapter:
        mod = k.rsplit(".lora_", 1)[0]
        if "vision_tower" in mod or "multi_modal_projector" in mod:
            # Skipping is only lossless if lora_B is still at its zero init — verify, don't assume.
            if ".lora_B." in k and torch.count_nonzero(adapter[k]).item():
                sys.exit(f"!! vision-tower lora_B is NONZERO for {mod} — skipping it would change "
                         "the model; refusing to merge")
            skipped_vision.add(mod)
            continue
        pairs.setdefault(mod, {})["A" if ".lora_A." in k else "B"] = adapter[k]

    deltas = {}  # on-disk weight name -> (A, B)
    for mod, ab in sorted(pairs.items()):
        if set(ab) != {"A", "B"}:
            sys.exit(f"!! incomplete LoRA pair for {mod}: have {sorted(ab)}")
        tk = target_key(mod + ".lora_A.weight", wmap)
        if tk is None:
            sys.exit(f"!! could not map adapter module {mod!r} onto a base weight — refusing to merge partially")
        deltas[tk] = (ab["A"], ab["B"])
    print(f"mapped {len(deltas)} LoRA modules onto base weights "
          f"(skipped {len(skipped_vision)} vision-tower modules; scale={scale})")

    os.makedirs(args.out, exist_ok=True)
    # Copy every non-safetensors file (config/tokenizer/processor/chat template/index).
    for name in os.listdir(base_dir):
        src = os.path.join(base_dir, name)
        if name.startswith(".") or os.path.isdir(src) or (name.endswith(".safetensors") and name in set(wmap.values())):
            continue
        shutil.copy(src, os.path.join(args.out, name))

    for shard in sorted(set(wmap.values())):
        shard_keys = [k for k, s in wmap.items() if s == shard and k in deltas]
        dst = os.path.join(args.out, shard)
        if not shard_keys:
            shutil.copy(os.path.join(base_dir, shard), dst)
            print(f"  {shard}: no target weights, copied verbatim")
            continue
        tensors = load_file(os.path.join(base_dir, shard))
        for k in shard_keys:
            A, B = deltas.pop(k)
            W = tensors[k]
            merged = W.float() + scale * (B.float() @ A.float())
            if merged.shape != W.shape:
                sys.exit(f"!! shape mismatch merging {k}: {merged.shape} vs {W.shape}")
            tensors[k] = merged.to(W.dtype)
        save_file(tensors, dst, metadata={"format": "pt"})
        print(f"  {shard}: merged {len(shard_keys)} weights")

    if deltas:
        sys.exit(f"!! {len(deltas)} mapped modules never found in any shard: {sorted(deltas)[:5]}...")
    print(f"OK -> {args.out}")


if __name__ == "__main__":
    main()
