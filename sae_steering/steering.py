"""SAE steering core — boost trait features in the layer-19 residual during generation.

The intervention is a faithful port of Goodfire's official demo `example_intervention`:

    features = sae.encode(acts)            # dense relu (demo-faithful)
    error    = acts - sae.decode(features) # what the SAE can't reconstruct — preserved
    features[:, :, fid] += coef            # boost the target feature(s)
    return sae.decode(features) + error    # add the error term back (IMPORTANT)

Registered as a forward hook on `model.model.layers[LAYER]`, it fires on every forward (prompt
prefill + each generated token), so steering applies to all positions — the standard activation-
steering setup. Boosting (add a coefficient to the feature's activation) is the demo's method; set
`mode="add"` for plain activation-addition (resid += coef * unit_decoder_direction) instead.
"""

from __future__ import annotations

import torch

from . import common, config, sae as sae_mod


class SteeredModel:
    def __init__(self, model, tok, sae, layer: int = config.LAYER):
        self.model, self.tok, self.sae, self.layer = model, tok, sae, layer
        self.steer: dict[int, float] = {}      # {feature_id: coefficient}
        self.mode: str = "boost"               # "boost" (demo) | "add" (activation addition)
        self._handle = None

    # --- steering config ----------------------------------------------------
    def set_steering(self, feats_coefs: dict[int, float], mode: str = "boost") -> None:
        self.steer = {int(k): float(v) for k, v in feats_coefs.items()}
        self.mode = mode

    def clear(self) -> None:
        self.steer = {}

    # --- the hook -----------------------------------------------------------
    def _hook(self, module, inputs, output):
        if not self.steer:
            return output
        is_tuple = isinstance(output, tuple)
        hs = output[0] if is_tuple else output            # [batch, seq, d_model]
        dtype = hs.dtype
        x = hs.to(self.sae.W_enc.dtype)

        if self.mode == "add":
            # plain activation addition: resid += sum_f coef * (unit decoder direction)
            vec = torch.zeros(self.sae.d_model, device=x.device, dtype=x.dtype)
            for fid, coef in self.steer.items():
                d = self.sae.W_dec[fid]                    # [d_model] decoder row = feature direction
                vec = vec + coef * d / (d.norm() + 1e-8)
            steered = x + vec
        else:
            # demo's feature-boost with error preservation
            feats = self.sae.encode_pre(x)                 # dense relu  [b, s, d_sae]
            error = x - self.sae.decode(feats)
            for fid, coef in self.steer.items():
                feats[..., fid] = feats[..., fid] + coef
            steered = self.sae.decode(feats) + error

        steered = steered.to(dtype)
        if is_tuple:
            return (steered,) + tuple(output[1:])
        return steered

    def register(self) -> None:
        if self._handle is None:
            self._handle = self.model.model.layers[self.layer].register_forward_hook(self._hook)

    def remove(self) -> None:
        if self._handle is not None:
            self._handle.remove()
            self._handle = None

    # --- generation ---------------------------------------------------------
    @torch.no_grad()
    def chat(self, messages: list[dict], max_new_tokens: int, temperature: float, top_p: float):
        """Generate an assistant turn for chat `messages`. Returns (text, finish_reason)."""
        ids = self.tok.apply_chat_template(
            messages, add_generation_prompt=True, return_tensors="pt"
        ).to(self.model.device)
        do_sample = temperature is not None and temperature > 0
        kw = dict(max_new_tokens=max_new_tokens, do_sample=do_sample, pad_token_id=self.tok.eos_token_id)
        if do_sample:
            kw.update(temperature=temperature, top_p=top_p)
        out = self.model.generate(ids, **kw)
        gen = out[0, ids.shape[1]:]
        text = self.tok.decode(gen, skip_special_tokens=True)
        finish = "length" if gen.shape[0] >= max_new_tokens else "stop"
        return text, finish


def load_steered(device: str | None = None) -> SteeredModel:
    device = config.pick_device(device)
    common.set_seed()
    model, tok = common.load_model_tokenizer(device)
    sae = sae_mod.load_sae(device)
    return SteeredModel(model, tok, sae)


def features_for(trait: str, coef: float, topn: int) -> dict[int, float]:
    """Build {feature_id: coef} from results/{trait}_features.json. Prefer strict-funnel survivors
    (final_features); fall back to the Stage-2-primary expression features for value traits where the
    strict intersection was empty (those are the steering-relevant features anyway)."""
    data = common.load_json(config.features_path(trait))
    src = data.get("final_features") or data.get("stage2_primary") or []
    feats = [f["feature_id"] for f in src][:topn]
    if not feats:
        raise ValueError(f"no features for trait {trait!r} in {config.features_path(trait)}")
    return {int(fid): float(coef) for fid in feats}
