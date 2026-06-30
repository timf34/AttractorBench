"""Shared utilities: model/tokenizer load, layer-19 residual capture, chat templating + span masks,
paired Cohen's d, JSON IO. Imported by the harvest scripts and the SAE reconstruction check.

Masking strategy (the error-prone part, done carefully):
- Stage 1 (instruction contrast): we tokenize the templated STRING ourselves with offset mapping,
  so the input_ids fed to the model and the question-token mask come from the SAME tokenization
  (no re-tokenization drift). The question span = tokens whose char offsets fall inside the user text.
- Stage 2 (response contrast): the completion span is known exactly from generation
  (completion_ids = generated ids after the prompt), so the harvest sequence is prompt_ids+completion_ids
  and the mask is [len(prompt):]. We never re-tokenize concatenated text.
"""

from __future__ import annotations

import json
import os

import torch
from dotenv import load_dotenv
from transformers import AutoModelForCausalLM, AutoTokenizer

from . import config

load_dotenv()  # OPENAI_API_KEY / HF_TOKEN from repo-root .env


def set_seed(seed: int = config.SEED) -> None:
    import random
    random.seed(seed)
    torch.manual_seed(seed)
    try:
        import numpy as np
        np.random.seed(seed)
    except Exception:  # noqa: BLE001
        pass


def load_model_tokenizer(device: str, dtype=torch.bfloat16):
    tok = AutoTokenizer.from_pretrained(config.MODEL, token=os.environ.get("HF_TOKEN"))
    model = AutoModelForCausalLM.from_pretrained(
        config.MODEL, torch_dtype=dtype, token=os.environ.get("HF_TOKEN")
    ).to(device).eval()
    return model, tok


def _templated_ids_and_offsets(tok, system: str, user: str, add_generation_prompt: bool):
    """Return (input_ids[1,seq] on cpu, offsets list, templated_text). input_ids come from tokenizing
    the templated string ourselves (consistent with the offsets)."""
    text = tok.apply_chat_template(
        [{"role": "system", "content": system}, {"role": "user", "content": user}],
        tokenize=False, add_generation_prompt=add_generation_prompt,
    )
    enc = tok(text, return_offsets_mapping=True, add_special_tokens=False)
    ids = torch.tensor(enc["input_ids"]).unsqueeze(0)
    return ids, enc["offset_mapping"], text


def instruction_input(tok, system: str, user: str):
    """Stage 1: build chat input and the boolean mask over the USER-QUESTION tokens."""
    ids, offsets, text = _templated_ids_and_offsets(tok, system, user, add_generation_prompt=True)
    c0 = text.find(user)
    if c0 < 0:
        raise ValueError("user text not found in templated string (template altered it?)")
    c1 = c0 + len(user)
    mask = torch.tensor([(a < c1 and b > c0 and b > a) for (a, b) in offsets])
    n = int(mask.sum())
    if not (0 < n <= ids.shape[1]):
        raise AssertionError(f"question mask has {n} tokens (seq={ids.shape[1]}) — masking failed")
    return ids, mask


@torch.no_grad()
def layer_residual(model, input_ids):
    """Forward a single [1,seq] input, return the post-block residual at config.LAYER as [seq,d_model]."""
    captured = {}
    layer = model.model.layers[config.LAYER]
    h = layer.register_forward_hook(lambda m, i, o: captured.__setitem__("x", o[0] if isinstance(o, tuple) else o))
    try:
        model(input_ids.to(model.device))
    finally:
        h.remove()
    return captured["x"][0]  # [seq, d_model]


@torch.no_grad()
def pooled_features(model, sae, input_ids, token_mask):
    """Dense SAE feature vector mean-pooled over the masked tokens: [d_sae] (fp32, on cpu)."""
    resid = layer_residual(model, input_ids)                  # [seq, d_model]
    feats = sae.encode_pre(resid.to(sae.W_enc.dtype))          # [seq, d_sae] dense post-ReLU
    sel = feats[token_mask.to(feats.device)]                   # [n_masked, d_sae]
    return sel.float().mean(0).cpu()


@torch.no_grad()
def generate_completion(model, tok, system: str, user: str, max_new_tokens: int):
    """Greedy-generate; return (prompt_ids[1,p], completion_ids[1,c], completion_text)."""
    prompt_ids, _, _ = _templated_ids_and_offsets(tok, system, user, add_generation_prompt=True)
    prompt_ids = prompt_ids.to(model.device)
    out = model.generate(prompt_ids, max_new_tokens=max_new_tokens, do_sample=False,
                         pad_token_id=tok.eos_token_id)
    completion_ids = out[:, prompt_ids.shape[1]:]
    text = tok.decode(completion_ids[0], skip_special_tokens=True)
    return prompt_ids.cpu(), completion_ids.cpu(), text


@torch.no_grad()
def pooled_features_for_completion(model, sae, prompt_ids, completion_ids):
    """Stage 2: forward prompt_ids+completion_ids (token ids, NOT re-tokenized text); mean-pool the
    dense SAE features over the COMPLETION span only."""
    full = torch.cat([prompt_ids, completion_ids], dim=1)
    p = prompt_ids.shape[1]
    n_comp = completion_ids.shape[1]
    if not (0 < n_comp < full.shape[1]):
        raise AssertionError(f"completion span {n_comp} of {full.shape[1]} — generation/masking failed")
    resid = layer_residual(model, full)                        # [seq, d_model]
    feats = sae.encode_pre(resid[p:].to(sae.W_enc.dtype))      # completion tokens only
    return feats.float().mean(0).cpu()


def paired_cohens_d(pos: torch.Tensor, neg: torch.Tensor):
    """pos,neg: [n_pairs, d_sae] paired rows. Returns (d[d_sae], dead_mask[d_sae]).
    Paired Cohen's d = mean(Δ)/std(Δ) over pairs (matches the paired pos/neg design)."""
    delta = (pos - neg).float()                                # [n_pairs, d_sae]
    mean = delta.mean(0)
    std = delta.std(0, unbiased=True)
    d = torch.where(std > 1e-8, mean / (std + 1e-8), torch.zeros_like(mean))
    dead = (pos.abs().mean(0) < 1e-8) & (neg.abs().mean(0) < 1e-8)  # ~never active in either
    d = torch.where(dead, torch.zeros_like(d), d)
    return d, dead


def save_json(path: str, obj) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def load_json(path: str):
    with open(path, encoding="utf-8") as f:
        return json.load(f)
