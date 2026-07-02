"""BatchTopK SAE loader (defensive) + reconstruction sanity check.

Goodfire's checkpoint format is NOT documented (config.yaml is just wandb metadata), so the loader
PRINTS every state-dict key + shape, then infers roles BY SHAPE against d_model=4096 — it never
assumes key names or weight orientation, and raises a clear error on ambiguity rather than guessing.

Canonical internal orientation (so encode/decode are unambiguous):
    W_enc : [d_model, d_sae]   encode_pre = x @ W_enc + b_enc
    b_enc : [d_sae]
    W_dec : [d_sae, d_model]   decode     = z @ W_dec + b_dec
    b_dec : [d_model]
    threshold : [d_sae]        (JumpReLU; present in BatchTopK checkpoints)

Discovery uses the DENSE pre-activation relu(encode_pre) (bypassing threshold/top-k). The
reconstruction check uses the deployed encode (threshold or top-k) — that's what should reconstruct.
"""

from __future__ import annotations

import json
import os

import torch
import torch.nn.functional as F
from huggingface_hub import hf_hub_download

from . import config


class BatchTopKSAE:
    """Holds canonical-orientation weights; provides dense (discovery) and deployed (recon) encodes."""

    def __init__(self, W_enc, b_enc, W_dec, b_dec, threshold, k=None, pre_bias_sub=False):
        self.W_enc, self.b_enc = W_enc, b_enc      # [d_model,d_sae], [d_sae]
        self.W_dec, self.b_dec = W_dec, b_dec      # [d_sae,d_model], [d_model]
        self.threshold = threshold                  # [d_sae]
        self.d_model, self.d_sae = W_enc.shape
        self.k = k
        # Some SAEs subtract the decoder bias before encoding (Anthropic convention):
        # z = relu((x - b_dec) @ W_enc + b_enc). The gate detects which convention this checkpoint uses.
        self.pre_bias_sub = pre_bias_sub

    def to(self, device=None, dtype=None):
        for n in ("W_enc", "b_enc", "W_dec", "b_dec", "threshold"):
            t = getattr(self, n)
            if t is not None:
                setattr(self, n, t.to(device=device, dtype=dtype))
        return self

    def encode_pre(self, x):
        """relu((x[-b_dec]) @ W_enc + b_enc) — DENSE post-ReLU activations, used for feature discovery."""
        if self.pre_bias_sub:
            x = x - self.b_dec
        return F.relu(x @ self.W_enc + self.b_enc)

    def encode(self, x):
        """Deployed sparse encode (threshold if present, else per-sample top-k). For reconstruction."""
        pre = self.encode_pre(x)
        if self.threshold is not None and torch.any(self.threshold > 0):
            return torch.where(pre > self.threshold, pre, torch.zeros_like(pre))
        if self.k is None or self.k >= self.d_sae:
            return pre  # no sparsity info -> dense (reconstruction will look off; flagged by the gate)
        top = pre.topk(self.k, dim=-1)
        z = torch.zeros_like(pre)
        return z.scatter_(-1, top.indices, top.values)

    def decode(self, z):
        return z @ self.W_dec + self.b_dec


def _flatten_state_dict(obj) -> dict:
    """Unwrap common wrappers ({'state_dict':...}, {'sae':...}) down to a {name: tensor} dict."""
    if isinstance(obj, dict):
        tensors = {k: v for k, v in obj.items() if isinstance(v, torch.Tensor)}
        if tensors:
            return tensors
        for k, v in obj.items():  # one level of nesting
            if isinstance(v, dict):
                inner = {kk: vv for kk, vv in v.items() if isinstance(vv, torch.Tensor)}
                if inner:
                    print(f"[sae] unwrapped nested state_dict under key {k!r}")
                    return inner
    raise ValueError("Could not find a {name: tensor} state_dict in the checkpoint")


def _infer_and_load(sd: dict) -> BatchTopKSAE:
    d = config.D_MODEL
    # print everything FIRST (the load-bearing diagnostic)
    print("[sae] checkpoint tensors:")
    for k, v in sd.items():
        print(f"    {k:40} {tuple(v.shape)} {v.dtype}")

    mats = {k: v for k, v in sd.items() if v.ndim == 2}
    vecs = {k: v for k, v in sd.items() if v.ndim == 1}
    # the two matrices have a d_model axis (==4096) and a d_sae axis (the other one)
    enc_w = dec_w = None
    for k, v in mats.items():
        kl = k.lower()
        if d not in v.shape:
            continue
        if "enc" in kl and enc_w is None:
            enc_w = (k, v)
        elif "dec" in kl and dec_w is None:
            dec_w = (k, v)
    # fall back to shape-only if names didn't disambiguate: encoder maps d_model->d_sae (Linear [d_sae,d])
    if enc_w is None or dec_w is None:
        cand = [(k, v) for k, v in mats.items() if d in v.shape]
        if len(cand) == 2:
            (k0, v0), (k1, v1) = cand
            # Linear encoder weight is [d_sae, d_model] (rows=d_sae); decoder [d_model, d_sae] (rows=d_model)
            enc_w = (k0, v0) if v0.shape[0] != d else (k1, v1)
            dec_w = (k1, v1) if enc_w[0] == k0 else (k0, v0)
            print(f"[sae] disambiguated encoder/decoder by shape: enc={enc_w[0]} dec={dec_w[0]}")
    if enc_w is None or dec_w is None:
        raise ValueError(f"Could not identify encoder/decoder matrices among 2D tensors: "
                         f"{[(k, tuple(v.shape)) for k, v in mats.items()]}")

    # normalize to canonical orientation
    ek, ev = enc_w
    W_enc = ev.t().contiguous() if ev.shape[0] != d else ev.contiguous()  # -> [d_model, d_sae]
    if W_enc.shape[0] != d:
        raise ValueError(f"encoder weight {ek} shape {tuple(ev.shape)} has no d_model={d} axis")
    d_sae = W_enc.shape[1]
    dk, dv = dec_w
    W_dec = dv.contiguous() if dv.shape[1] == d else dv.t().contiguous()  # -> [d_sae, d_model]
    if W_dec.shape != (d_sae, d):
        raise ValueError(f"decoder weight {dk} shape {tuple(dv.shape)} != expected ({d_sae},{d})")

    # biases + threshold from the 1-D tensors, by length and name
    b_enc = b_dec = threshold = None
    for k, v in vecs.items():
        kl = k.lower()
        if v.numel() == d_sae and ("thresh" in kl or "theta" in kl) and threshold is None:
            threshold = v
        elif v.numel() == d_sae and ("enc" in kl or "bias" in kl) and b_enc is None:
            b_enc = v
        elif v.numel() == d and b_dec is None:
            b_dec = v
    # second pass for any unlabeled d_sae vector
    for k, v in vecs.items():
        if v.numel() == d_sae and b_enc is None and v is not threshold:
            b_enc = v
        if v.numel() == d_sae and threshold is None and v is not b_enc:
            threshold = v
    if b_enc is None:
        b_enc = torch.zeros(d_sae)
        print("[sae] WARNING: no encoder bias found; using zeros")
    if b_dec is None:
        b_dec = torch.zeros(d)
        print("[sae] WARNING: no decoder bias found; using zeros")
    if threshold is None:
        threshold = torch.zeros(d_sae)
        print("[sae] note: no threshold buffer found; encode() will fall back to top-k/dense")

    print(f"[sae] inferred: d_sae={d_sae}, W_enc{tuple(W_enc.shape)} b_enc[{b_enc.numel()}] "
          f"W_dec{tuple(W_dec.shape)} b_dec[{b_dec.numel()}] threshold(nonzero={int((threshold>0).sum())})")
    config.D_SAE = d_sae
    return BatchTopKSAE(W_enc, b_enc, W_dec, b_dec, threshold, k=getattr(config, "SAE_K", None))


def load_sae(device: str, dtype=torch.bfloat16) -> BatchTopKSAE:
    path = hf_hub_download(config.SAE_REPO, config.SAE_FILENAME)
    print(f"[sae] loading {path}")
    obj = torch.load(path, map_location="cpu")
    sae = _infer_and_load(_flatten_state_dict(obj))
    # Discovery uses dense encode_pre (demo-faithful) regardless; the meta file just records that the
    # loader gate validated the hook point. Warn if the gate hasn't been run yet.
    meta_p = config.sae_meta_path()
    if os.path.exists(meta_p):
        print(f"[sae] loader gate previously validated (see {meta_p}); using dense encode (demo-faithful)")
    else:
        print(f"[sae] note: no {meta_p} yet — run `python -m sae_steering.check_sae` first to validate the hook point")
    return sae.to(device=device, dtype=dtype)


@torch.no_grad()
def _ev_at_k(x, sae, k):
    """Explained variance of decode(top-k(encode_pre(x))) at a given k."""
    pre = sae.encode_pre(x)
    if k >= sae.d_sae:
        z = pre
    else:
        top = pre.topk(k, dim=-1)
        z = torch.zeros_like(pre).scatter_(-1, top.indices, top.values)
    x_hat = sae.decode(z)
    return (1.0 - (x - x_hat).pow(2).sum() / (x - x.mean(0)).pow(2).sum()).item()


@torch.no_grad()
def reconstruction_check(x: torch.Tensor, sae: BatchTopKSAE) -> dict:
    """x: [N, d_model] captured layer-LAYER residuals. Confirms the hook point + loader orientation.

    Per Goodfire's official demo this SAE is used DENSE (relu encode -> linear decode), and its dense
    EV on the residual stream is naturally low (massive-activation dims dominate variance) — so we GATE
    ON COSINE of the dense reconstruction (degenerate/wrong-hook ~0; working hook >~0.5), not EV. The
    k-sweep below is printed as informative diagnostics only (does sparsifying help reconstruction?)."""
    x = x.to(sae.W_enc.dtype)
    x_hat = sae.decode(sae.encode_pre(x))                       # DENSE — the demo's reconstruction
    ev = (1.0 - (x - x_hat).pow(2).sum() / (x - x.mean(0)).pow(2).sum()).item()
    cos = F.cosine_similarity(x.float(), x_hat.float(), dim=-1).mean().item()
    print(f"[sae] DENSE reconstruction (demo-faithful): explained_variance={ev:.4f} mean_cosine={cos:.4f}")
    # diagnostics: does top-k help? (not used for discovery; just informative)
    for k in (64, 91, 128, 256, 512):
        if k < sae.d_sae:
            print(f"[sae]   (diag) top-k={k:4d} -> explained_variance={_ev_at_k(x, sae, k):.4f}")
    out = {"explained_variance_dense": ev, "mean_cosine": cos, "n": int(x.shape[0])}
    if cos < config.RECON_MIN_COSINE:
        raise RuntimeError(
            f"Dense reconstruction cosine {cos:.3f} < {config.RECON_MIN_COSINE}: the SAE isn't tracking "
            f"these activations — likely wrong hook point (try --layer {config.LAYER-1}/{config.LAYER+1}) "
            f"or wrong weight orientation. Inspect the printed key/shape mapping above.")
    config.ensure_dirs()
    with open(config.sae_meta_path(), "w") as f:
        json.dump({"mode": "dense", "d_sae": sae.d_sae, "layer": config.LAYER,
                   "explained_variance_dense": ev, "mean_cosine": cos}, f, indent=2)
    print(f"[sae] gate PASSED (functioning, demo-faithful dense mode) -> wrote {config.sae_meta_path()}")
    return out
