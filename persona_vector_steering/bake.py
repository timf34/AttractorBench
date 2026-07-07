"""Bake a persona steering vector into a Llama checkpoint variant as an MLP down_proj bias.

CPU-only, no model forward pass required — this is pure tensor/file surgery on the safetensors
shards' *index* (the shards themselves are symlinked untouched) plus one small new safetensors
file holding the bias tensors.

The math (must equal steering.py's activation-addition exactly):

    steering.py:    resid[block] += coef * vec[layer]     (added to the OUTPUT of decoder block
                                                             `layer - 1`, i.e. hidden_states[layer])

    A decoder block's output is:

        resid_out = resid_in + attn_out + mlp_out

    and (with mlp_bias enabled) mlp_out = down_proj(...) + down_proj.bias. So setting

        layers[layer-1].mlp.down_proj.bias = coef * vec[layer]

    makes resid_out include exactly `coef * vec[layer]` extra, at exactly the same point in the
    graph steering.py hooks. This is a static, config-time equivalent of the runtime hook — it lets
    vLLM (which doesn't run our hook) serve a steered model directly.

Why 96 zero-bias tensors ship alongside the one real one: enabling `mlp_bias: true` in config.json
makes transformers (and vLLM, which mirrors the HF config) allocate a bias parameter for
gate_proj/up_proj/down_proj on EVERY layer, not just the one we're steering. Any layer whose bias
we don't ship would load as an uninitialized/missing tensor, so every other bias must be an
explicit zero vector (x + 0 == x exactly, no numerical effect) to keep the other 31 blocks (and the
gate/up projections of ALL 32 blocks, including the steered one) byte-identical to the base model.

    python -m persona_vector_steering.bake --trait goodness --coef 2 --layer 16
    python -m persona_vector_steering.bake --trait goodness --coef 2 --layer 16 --force

Output: <out_dir>/<trait>_c<coef>_l<layer>/  — a directory vLLM can serve directly
(`vllm serve <dir>`), with shards symlinked (not copied) to save disk.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys

os.environ.setdefault("HF_HOME", "/workspace/.cache/huggingface")

import glob
from datetime import datetime, timezone

import torch
from huggingface_hub import snapshot_download
from safetensors.torch import save_file

from . import config

# Real files that must exist alongside the shards for vLLM/HF to serve the variant; copied
# (not symlinked) since they're tiny and we don't want the variant dir to break if the cache is
# ever pruned/moved.
_COPY_FILES = ["tokenizer.json", "tokenizer_config.json", "special_tokens_map.json", "generation_config.json"]
_REQUIRED_COPY_FILES = {"generation_config.json", "tokenizer.json", "tokenizer_config.json"}


def _log(msg: str) -> None:
    print(msg, file=sys.stderr)


def _resolve_snapshot(base: str) -> str:
    try:
        return snapshot_download(base, local_files_only=True)
    except Exception:
        _log(f"[bake] WARNING: {base!r} not in local cache, downloading (~16 GB) ...")
        return snapshot_download(base)


def _sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _load_vector(trait: str, layer: int, num_hidden_layers: int, hidden_size: int) -> torch.Tensor:
    path = config.vector_path(trait)
    if not os.path.exists(path):
        raise FileNotFoundError(f"persona vector not found: {path}")
    vec = torch.load(path, map_location="cpu", weights_only=False)
    n_idx = vec.shape[0]
    if layer == 0:
        raise ValueError(
            "layer 0 is the embedding output (hidden_states[0]), before any decoder block — "
            "there is no MLP whose bias can express it. Choose layer in 1.."
            f"{min(n_idx - 1, num_hidden_layers)}."
        )
    if not (1 <= layer <= n_idx - 1):
        raise ValueError(f"layer {layer} out of range 1..{n_idx - 1} for {trait}'s vector")
    block = layer - 1
    if not (0 <= block < num_hidden_layers):
        raise ValueError(f"block {block} (= layer-1) out of range 0..{num_hidden_layers - 1}")
    if vec.shape[1] != hidden_size:
        raise ValueError(f"vector hidden dim {vec.shape[1]} != model hidden_size {hidden_size}")
    if not torch.isfinite(vec).all():
        raise ValueError(f"non-finite values in vector at {path}")
    return vec


def _symlink_shards(snapshot_path: str, tmp_dir: str) -> list[str]:
    shard_paths = sorted(glob.glob(os.path.join(snapshot_path, "model-*-of-*.safetensors")))
    if not shard_paths:
        raise FileNotFoundError(f"no model-*-of-*.safetensors shards found in {snapshot_path}")
    names = []
    for shard in shard_paths:
        real = os.path.realpath(shard)
        link = os.path.join(tmp_dir, os.path.basename(shard))
        os.symlink(real, link)
        if not os.path.exists(link):
            raise RuntimeError(f"symlink target missing: {link} -> {real}")
        if os.path.getsize(link) != os.path.getsize(real):
            raise RuntimeError(f"symlink size mismatch: {link} -> {real}")
        names.append(os.path.basename(shard))
    return names


def _build_bias_tensors(
    num_hidden_layers: int, intermediate_size: int, hidden_size: int, block: int, bias: torch.Tensor
) -> dict[str, torch.Tensor]:
    tensors: dict[str, torch.Tensor] = {}
    for i in range(num_hidden_layers):
        tensors[f"model.layers.{i}.mlp.gate_proj.bias"] = torch.zeros(intermediate_size, dtype=torch.bfloat16)
        tensors[f"model.layers.{i}.mlp.up_proj.bias"] = torch.zeros(intermediate_size, dtype=torch.bfloat16)
        tensors[f"model.layers.{i}.mlp.down_proj.bias"] = torch.zeros(hidden_size, dtype=torch.bfloat16)
    tensors[f"model.layers.{block}.mlp.down_proj.bias"] = bias
    return tensors


def _rewrite_index(snapshot_path: str, tmp_dir: str, bias_tensors: dict[str, torch.Tensor]) -> None:
    with open(os.path.join(snapshot_path, "model.safetensors.index.json")) as f:
        index = json.load(f)
    added_bytes = 0
    for name, t in bias_tensors.items():
        index["weight_map"][name] = "model-pvec-bias.safetensors"
        added_bytes += t.numel() * t.element_size()
    index.setdefault("metadata", {})
    index["metadata"]["total_size"] = index["metadata"].get("total_size", 0) + added_bytes
    with open(os.path.join(tmp_dir, "model.safetensors.index.json"), "w") as f:
        json.dump(index, f, indent=2)


def _patch_model_config(snapshot_path: str, tmp_dir: str) -> dict:
    with open(os.path.join(snapshot_path, "config.json")) as f:
        model_config = json.load(f)
    model_config["mlp_bias"] = True
    with open(os.path.join(tmp_dir, "config.json"), "w") as f:
        json.dump(model_config, f, indent=2)
    return model_config


def _copy_aux_files(snapshot_path: str, tmp_dir: str) -> None:
    for name in _COPY_FILES:
        src = os.path.join(snapshot_path, name)
        if not os.path.exists(src):
            _log(f"[bake] WARNING: {name} not found in snapshot, skipping")
            if name in _REQUIRED_COPY_FILES:
                _log(f"[bake] WARNING: {name} is normally required to serve the model")
            continue
        shutil.copy2(src, os.path.join(tmp_dir, name))


def bake(trait: str, coef_str: str, layer_str: str, out_dir: str, base: str, force: bool) -> str:
    coef = float(coef_str)
    layer = int(layer_str)

    variant_dir = os.path.join(os.path.abspath(out_dir), f"{trait}_c{coef_str}_l{layer_str}")
    if os.path.isdir(variant_dir) and not force:
        _log(f"[bake] variant already exists, skipping ({variant_dir}); pass --force to rebuild")
        print(variant_dir)
        return variant_dir

    _log(f"[bake] resolving base snapshot for {base} ...")
    snapshot_path = _resolve_snapshot(base)
    _log(f"[bake] snapshot: {snapshot_path}")

    with open(os.path.join(snapshot_path, "config.json")) as f:
        base_config = json.load(f)
    num_hidden_layers = base_config["num_hidden_layers"]
    hidden_size = base_config["hidden_size"]
    intermediate_size = base_config["intermediate_size"]
    assert base_config.get("mlp_bias", False) is False, (
        "base model config already has mlp_bias=true; bake.py assumes an unbiased base checkpoint"
    )

    _log(f"[bake] loading {trait}'s persona vector ...")
    vec = _load_vector(trait, layer, num_hidden_layers, hidden_size)
    block = layer - 1
    bias = (coef * vec[layer]).to(torch.bfloat16)
    _log(f"[bake] bias = {coef} * vec[{layer}]  ->  layers.{block}.mlp.down_proj.bias  (||bias||={bias.float().norm().item():.4f})")

    tmp_dir = variant_dir + ".tmp"
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.makedirs(tmp_dir)

    try:
        _log("[bake] symlinking shards ...")
        _symlink_shards(snapshot_path, tmp_dir)

        _log("[bake] building bias tensors (96 tensors, ~2.1 MB) ...")
        bias_tensors = _build_bias_tensors(num_hidden_layers, intermediate_size, hidden_size, block, bias)
        save_file(bias_tensors, os.path.join(tmp_dir, "model-pvec-bias.safetensors"), metadata={"format": "pt"})

        _log("[bake] rewriting model.safetensors.index.json ...")
        _rewrite_index(snapshot_path, tmp_dir, bias_tensors)

        _log("[bake] patching config.json (mlp_bias: true) ...")
        _patch_model_config(snapshot_path, tmp_dir)

        _log("[bake] copying tokenizer/generation config files ...")
        _copy_aux_files(snapshot_path, tmp_dir)

        _log("[bake] writing provenance PVEC_BAKE.json ...")
        vector_path = config.vector_path(trait)
        provenance = {
            "trait": trait,
            "coef": coef_str,
            "coef_float": coef,
            "layer": layer,
            "block": block,
            "vector_path": vector_path,
            "vector_sha256": _sha256_file(vector_path),
            "base": base,
            "snapshot_path": snapshot_path,
            "bias_l2_norm": bias.float().norm().item(),
            "created_utc": datetime.now(timezone.utc).isoformat(),
        }
        with open(os.path.join(tmp_dir, "PVEC_BAKE.json"), "w") as f:
            json.dump(provenance, f, indent=2)

        if os.path.isdir(variant_dir):
            shutil.rmtree(variant_dir)
        os.rename(tmp_dir, variant_dir)
    except BaseException:
        shutil.rmtree(tmp_dir, ignore_errors=True)
        raise

    _log(f"[bake] done: {variant_dir}")
    print(variant_dir)
    return variant_dir


def main() -> None:
    ap = argparse.ArgumentParser(description="Bake a persona vector into a Llama checkpoint as an MLP bias.")
    ap.add_argument("--trait", required=True, choices=config.TRAITS)
    ap.add_argument("--coef", required=True)
    ap.add_argument("--layer", required=True)
    ap.add_argument("--out-dir", default="/workspace/pvec_baked")
    ap.add_argument("--base", default=config.MODEL)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    bake(args.trait, args.coef, args.layer, args.out_dir, args.base, args.force)


if __name__ == "__main__":
    main()
