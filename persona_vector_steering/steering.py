"""Persona-vector steering core — activation addition of a per-trait direction into the residual.

The intervention (plain activation addition, the persona_vectors convention):

    resid += coef * persona_vec[trait][layer]      # persona_vec[trait] : [num_layers+1, d_model]

LAYER INDEXING (matches persona_vectors exactly, so the sweep's (layer, coef) transfers 1:1):
- persona_vectors builds vectors from `hidden_states[k]` (k in 0..num_layers; k=0 is embeddings,
  k>=1 is the output of decoder block k-1).
- To inject the direction measured at hidden_states[k], we hook decoder block `k-1` (its forward
  output IS hidden_states[k]). persona_vectors' ActivationSteerer does the same via layer_idx=layer-1.
- So a request `pvec:goodness:2:16` loads vec[16] and adds it at the output of block 15.

The vectors are the RAW mean-difference (un-normalized), so coefficients are small (~1-4), NOT the
6-8 the SAE path uses (that path unit-normalizes). Hooks fire on every forward (prefill + each
generated token), so steering applies to ALL positions — appropriate for a persistent persona.
"""

from __future__ import annotations

import os

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from . import config


class PersonaVectorSteeredModel:
    def __init__(self, model, tok, device):
        self.model, self.tok, self.device = model, tok, device
        self.num_blocks = len(model.model.layers)
        self._vectors: dict[str, torch.Tensor] = {}   # trait -> [num_layers+1, d_model] on device
        self._add: torch.Tensor | None = None         # coef * vec[layer], on device, model dtype
        self._block: int = -1                          # decoder block whose output we steer
        self._handles: list = []

    # --- vector loading -----------------------------------------------------
    def _vec(self, trait: str) -> torch.Tensor:
        if trait not in self._vectors:
            path = config.vector_path(trait)
            if not os.path.exists(path):
                raise FileNotFoundError(f"persona vector not found: {path}")
            v = torch.load(path, weights_only=False, map_location=self.device)
            self._vectors[trait] = v.to(self.device)
        return self._vectors[trait]

    # --- steering config ----------------------------------------------------
    def set_steering(self, trait: str, coef: float, layer: int) -> None:
        v = self._vec(trait)                           # [num_layers+1, d_model]
        n_idx = v.shape[0]
        if not (1 <= layer <= n_idx - 1):
            raise ValueError(f"layer {layer} out of range 1..{n_idx - 1} for {trait}")
        block = layer - 1                              # hook the block whose output == hidden_states[layer]
        if not (0 <= block < self.num_blocks):
            raise ValueError(f"block {block} out of range 0..{self.num_blocks - 1}")
        self._block = block
        self._add = (coef * v[layer]).to(self.model.dtype)

    def clear(self) -> None:
        self._add = None
        self._block = -1

    # --- the hook (one per block; only the active block adds) ---------------
    def _make_hook(self, block_idx: int):
        def hook(module, inputs, output):
            if self._add is None or block_idx != self._block:
                return output
            is_tuple = isinstance(output, tuple)
            hs = output[0] if is_tuple else output      # [batch, seq, d_model]
            hs = hs + self._add.to(hs.dtype)
            if is_tuple:
                return (hs,) + tuple(output[1:])
            return hs
        return hook

    def register(self) -> None:
        if self._handles:
            return
        for i, blk in enumerate(self.model.model.layers):
            self._handles.append(blk.register_forward_hook(self._make_hook(i)))

    def remove(self) -> None:
        for h in self._handles:
            h.remove()
        self._handles = []

    # --- generation ---------------------------------------------------------
    @torch.no_grad()
    def chat(self, messages: list[dict], max_new_tokens: int, temperature: float, top_p: float):
        """Generate one assistant turn. Returns (text, finish_reason)."""
        enc = self.tok.apply_chat_template(
            messages, add_generation_prompt=True, return_tensors="pt", return_dict=True
        )
        enc = {k: v.to(self.model.device) for k, v in enc.items()}
        input_len = enc["input_ids"].shape[1]
        do_sample = temperature is not None and temperature > 0
        kw = dict(max_new_tokens=max_new_tokens, do_sample=do_sample, pad_token_id=self.tok.eos_token_id)
        if do_sample:
            kw.update(temperature=temperature, top_p=top_p)
        out = self.model.generate(**enc, **kw)
        gen = out[0, input_len:]
        text = self.tok.decode(gen, skip_special_tokens=True)
        finish = "length" if gen.shape[0] >= max_new_tokens else "stop"
        return text, finish


def load_steered(device: str | None = None) -> PersonaVectorSteeredModel:
    device = config.pick_device(device)
    torch.manual_seed(config.SEED)
    tok = AutoTokenizer.from_pretrained(config.MODEL, token=os.environ.get("HF_TOKEN"))
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token
        tok.pad_token_id = tok.eos_token_id
    model = AutoModelForCausalLM.from_pretrained(
        config.MODEL, torch_dtype=torch.bfloat16, token=os.environ.get("HF_TOKEN")
    ).to(device).eval()
    return PersonaVectorSteeredModel(model, tok, device)
