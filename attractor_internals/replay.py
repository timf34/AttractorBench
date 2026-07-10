"""Teacher-forced replay of saved two_instance transcripts through HF transformers.

Design (see research_updates/2026-07-10_internal_attractor_detection_plan.md):

- Rebuild each instance's conversation view EXACTLY as attractorbench.harnesses._run_two_history
  constructed it (raw ``content``, not ``content_clean`` — the harness fed the raw reply forward).
- ONE forward pass per (run, view, model) over the full final conversation — valid because the
  Llama-3.1 chat template is append-only: the rendering of messages[:k] (+ generation prompt) is
  an exact prefix of the rendering of messages[:k+1], at string AND token level (content is
  ``| trim``-ed and Llama-3 pre-tokenization cannot merge the header's ``\\n\\n`` with following
  text; the template's date is the fixed literal "26 Jul 2024", not wall clock, so replays are
  byte-identical to what vLLM served). This is NEVER trusted silently: every own-turn prefix is
  asserted against the full tokenization, and a violation drops that (run, view) to per-turn
  growing-prefix passes, flagged in the output.
- Hidden states come from forward hooks on the requested decoder blocks (NOT
  output_hidden_states=True, which materializes all 33 layers). Layer k in the persona-vectors
  hidden_states convention = output of decoder block k-1.
- Full-vocab logits are never materialized for the whole sequence: the forward runs with
  logits_to_keep=1 and per-turn statistics are recomputed from the captured final-norm output
  through lm_head in chunks.

Per own turn the pass yields:
  Track A: nll_mean, nll_median, entropy_mean, sat_frac (p > SATURATION_P), mrr (mean
           reciprocal rank), nll_eot (the stop decision, kept out of the reply aggregates)
  Track B: prompt_last  — h at the last generation-header token (the persona-vectors
                          ``prompt_last`` readout position), per layer
           response_avg — mean h over the turn's reply tokens, per layer
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np

from . import config

CHUNK_POSITIONS = 4096  # lm_head recompute chunk; peak fp32 logits = CHUNK x 128256 = ~2.1 GB


class PrefixChainViolation(Exception):
    """Tokenization of a message prefix is not a prefix of the full conversation's tokens."""


# ---------------------------------------------------------------------------
# View reconstruction — mirrors attractorbench.harnesses._run_two_history exactly.
# ---------------------------------------------------------------------------
def build_view(run: dict, system_prompt: str, seed_prompt: str, view: str) -> tuple[list[dict], list[tuple[int, int]]]:
    """(messages, own) for one instance's view of a run.

    View "A" starts [system, user=seed] and speaks the odd turns; view "B" starts [system] and
    speaks the even turns. ``own`` lists (harness turn number, index of that assistant message
    in ``messages``). Uses raw ``content`` — what the harness actually fed forward.
    """
    if view not in ("A", "B"):
        raise ValueError(f"view must be 'A' or 'B', got {view!r}")
    messages = [{"role": "system", "content": system_prompt}]
    if view == "A":
        messages.append({"role": "user", "content": seed_prompt})
    own: list[tuple[int, int]] = []
    for t in run["turns"]:
        role = "assistant" if t["speaker"] == view else "user"
        messages.append({"role": role, "content": t["content"]})
        if role == "assistant":
            own.append((t["turn"], len(messages) - 1))
    return messages, own


# ---------------------------------------------------------------------------
# Serialization with per-turn spans + the prefix-chain assertion.
# ---------------------------------------------------------------------------
@dataclass
class TurnSpan:
    turn: int          # harness turn number (1-based, global across both speakers)
    msg_index: int     # index of this assistant message in the view's messages
    prompt_len: int    # tokens of render(messages[:msg_index], add_generation_prompt=True)
    reply_start: int   # == prompt_len; ids[reply_start:reply_end] are the reply tokens
    reply_end: int     # exclusive; ids[reply_end] is the <|eot_id|> that closed the turn
    readout_pos: int   # prompt_len - 1: last generation-header token (the pre-answer readout)


@dataclass
class ViewSerialization:
    ids_full: list[int]
    spans: list[TurnSpan] = field(default_factory=list)
    skipped_empty_turns: list[int] = field(default_factory=list)


def _render_ids(tokenizer, messages: list[dict], add_generation_prompt: bool) -> list[int]:
    # Render to a string, then tokenize — the same two-step vLLM serving does, and immune to
    # transformers-version differences in apply_chat_template(tokenize=True) return types.
    # add_special_tokens=False because the template already emits <|begin_of_text|>.
    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=add_generation_prompt
    )
    return tokenizer(text, add_special_tokens=False)["input_ids"]


def serialize_with_spans(tokenizer, messages: list[dict], own: list[tuple[int, int]]) -> ViewSerialization:
    """Tokenize the full view once and locate every own-turn reply span within it.

    Raises PrefixChainViolation if any per-turn rendering is not an exact token prefix of the
    full rendering (caller falls back to per-turn passes).
    """
    eot_id = tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ids_full = _render_ids(tokenizer, messages, add_generation_prompt=False)
    ser = ViewSerialization(ids_full=ids_full)
    for turn, mi in own:
        prompt_ids = _render_ids(tokenizer, messages[:mi], add_generation_prompt=True)
        upto_ids = _render_ids(tokenizer, messages[: mi + 1], add_generation_prompt=False)
        if ids_full[: len(prompt_ids)] != prompt_ids or ids_full[: len(upto_ids)] != upto_ids:
            raise PrefixChainViolation(f"turn {turn} (message {mi}) is not a token prefix of the full view")
        reply_end = len(upto_ids) - 1
        if ids_full[reply_end] != eot_id:
            raise PrefixChainViolation(f"turn {turn}: expected <|eot_id|> at {reply_end}")
        if reply_end <= len(prompt_ids):  # empty reply (pathological) — no tokens to score
            ser.skipped_empty_turns.append(turn)
            continue
        ser.spans.append(TurnSpan(
            turn=turn, msg_index=mi, prompt_len=len(prompt_ids),
            reply_start=len(prompt_ids), reply_end=reply_end, readout_pos=len(prompt_ids) - 1,
        ))
    return ser


# ---------------------------------------------------------------------------
# Model loading + module resolution (plain or PEFT-wrapped).
# ---------------------------------------------------------------------------
def load_model_and_tokenizer(adapter_trait: str | None, device: str | None = None):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    device = config.pick_device(device)
    tokenizer = AutoTokenizer.from_pretrained(config.BASE_MODEL)
    dtype = torch.bfloat16 if device == "cuda" else torch.float32
    model = AutoModelForCausalLM.from_pretrained(
        config.BASE_MODEL, torch_dtype=dtype, attn_implementation="sdpa"
    ).to(device)
    if adapter_trait is not None:
        import os

        from peft import PeftModel
        adapter_dir = os.path.join(config.ADAPTERS_DIR, adapter_trait)
        model = PeftModel.from_pretrained(model, adapter_dir, torch_dtype=dtype)
    model.eval()
    return model, tokenizer


def _unwrap(model):
    return model.get_base_model() if hasattr(model, "get_base_model") else model


def decoder_blocks(model):
    return _unwrap(model).model.layers


def final_norm(model):
    return _unwrap(model).model.norm


def lm_head_weight(model):
    return _unwrap(model).lm_head.weight


# ---------------------------------------------------------------------------
# The forward pass + per-turn feature extraction.
# ---------------------------------------------------------------------------
@dataclass
class TurnResult:
    turn: int
    prefix_tokens: int
    n_reply_tokens: int
    nll_mean: float
    nll_median: float
    entropy_mean: float
    sat_frac: float
    mrr: float
    nll_eot: float
    prompt_last: np.ndarray   # [len(LAYERS), D_MODEL] fp32
    response_avg: np.ndarray  # [len(LAYERS), D_MODEL] fp32
    fallback_per_turn: bool = False


def _forward_with_taps(model, ids: list[int], device: str):
    """One no-grad pass; returns {layer: hidden [seq, d]} for config.LAYERS plus final-norm h."""
    import torch

    captured: dict[object, "torch.Tensor"] = {}
    handles = []

    def _tap(key):
        def hook(_module, _inputs, output):
            h = output[0] if isinstance(output, tuple) else output
            captured[key] = h.squeeze(0)
        return hook

    blocks = decoder_blocks(model)
    for layer in config.LAYERS:
        handles.append(blocks[layer - 1].register_forward_hook(_tap(layer)))
    handles.append(final_norm(model).register_forward_hook(_tap("norm")))

    input_ids = torch.tensor([ids], dtype=torch.long, device=device)
    try:
        with torch.inference_mode():
            try:
                model(input_ids=input_ids, use_cache=False, logits_to_keep=1)
            except TypeError:
                try:
                    model(input_ids=input_ids, use_cache=False, num_logits_to_keep=1)
                except TypeError:  # old transformers: accept the full-logits allocation
                    model(input_ids=input_ids, use_cache=False)
    finally:
        for h in handles:
            h.remove()
    return captured


def _turn_stats_and_readouts(captured, ids: list[int], span: TurnSpan, model, device: str) -> TurnResult:
    """Track A stats + Track B readouts for one turn from a pass that covered its positions."""
    import torch
    import torch.nn.functional as F

    W = lm_head_weight(model)
    h_norm = captured["norm"]
    # Positions reply_start-1 .. reply_end-1 predict tokens reply_start .. reply_end; the last
    # prediction is the <|eot_id|> stop decision, reported separately as nll_eot.
    pos = torch.arange(span.reply_start - 1, span.reply_end, device=device)
    targets = torch.tensor([ids[p + 1] for p in range(span.reply_start - 1, span.reply_end)],
                           dtype=torch.long, device=device)
    lp_list, ent_list, rank_list = [], [], []
    for i in range(0, len(pos), CHUNK_POSITIONS):
        p, t = pos[i:i + CHUNK_POSITIONS], targets[i:i + CHUNK_POSITIONS]
        logits = F.linear(h_norm[p], W).float()
        logsm = F.log_softmax(logits, dim=-1)
        lp = logsm.gather(1, t[:, None]).squeeze(1)
        ent = -(logsm.exp() * logsm).sum(-1)
        target_logit = logits.gather(1, t[:, None])
        rank = 1 + (logits > target_logit).sum(-1)
        lp_list.append(lp); ent_list.append(ent); rank_list.append(rank)
        del logits, logsm
    lp = torch.cat(lp_list); ent = torch.cat(ent_list); rank = torch.cat(rank_list).float()

    nll = -lp
    nll_eot = float(nll[-1])
    nll_reply, ent_reply, rank_reply, p_reply = nll[:-1], ent[:-1], rank[:-1], lp[:-1].exp()

    prompt_last = np.stack([
        captured[layer][span.readout_pos].float().cpu().numpy() for layer in config.LAYERS
    ])
    response_avg = np.stack([
        captured[layer][span.reply_start:span.reply_end].float().mean(0).cpu().numpy()
        for layer in config.LAYERS
    ])
    return TurnResult(
        turn=span.turn,
        prefix_tokens=span.prompt_len,
        n_reply_tokens=int(len(nll_reply)),
        nll_mean=float(nll_reply.mean()),
        nll_median=float(nll_reply.median()),
        entropy_mean=float(ent_reply.mean()),
        sat_frac=float((p_reply > config.SATURATION_P).float().mean()),
        mrr=float((1.0 / rank_reply).mean()),
        nll_eot=nll_eot,
        prompt_last=prompt_last,
        response_avg=response_avg,
    )


def replay_view_single_pass(model, ser: ViewSerialization, device: str) -> list[TurnResult]:
    """The default path: one forward over the full view, features for every own turn."""
    captured = _forward_with_taps(model, ser.ids_full, device)
    results = [_turn_stats_and_readouts(captured, ser.ids_full, s, model, device) for s in ser.spans]
    captured.clear()
    return results


def replay_view_per_turn(model, tokenizer, messages: list[dict], own: list[tuple[int, int]],
                         device: str, max_turns: int | None = None) -> list[TurnResult]:
    """Fallback (and equivalence-check) path: one growing-prefix pass per own turn."""
    eot_id = tokenizer.convert_tokens_to_ids("<|eot_id|>")
    results = []
    for turn, mi in own[:max_turns]:
        prompt_ids = _render_ids(tokenizer, messages[:mi], add_generation_prompt=True)
        upto_ids = _render_ids(tokenizer, messages[: mi + 1], add_generation_prompt=False)
        if upto_ids[: len(prompt_ids)] != prompt_ids or upto_ids[-1] != eot_id:
            print(f"    [replay] turn {turn}: within-turn prefix violated — skipping turn")
            continue
        reply_end = len(upto_ids) - 1
        if reply_end <= len(prompt_ids):
            continue  # empty reply
        span = TurnSpan(turn=turn, msg_index=mi, prompt_len=len(prompt_ids),
                        reply_start=len(prompt_ids), reply_end=reply_end,
                        readout_pos=len(prompt_ids) - 1)
        captured = _forward_with_taps(model, upto_ids, device)
        r = _turn_stats_and_readouts(captured, upto_ids, span, model, device)
        r.fallback_per_turn = True
        results.append(r)
        captured.clear()
    return results


def replay_view(model, tokenizer, run: dict, system_prompt: str, view: str,
                device: str) -> tuple[list[TurnResult], list[int]]:
    """Replay one (run, view): single-pass when the prefix chain holds, per-turn otherwise.

    Returns (turn results, skipped empty turns).
    """
    messages, own = build_view(run, system_prompt, run["seed_prompt"], view)
    try:
        ser = serialize_with_spans(tokenizer, messages, own)
    except PrefixChainViolation as e:
        print(f"    [replay] run {run['run_index']} view {view}: {e} — per-turn fallback")
        return replay_view_per_turn(model, tokenizer, messages, own, device), []
    return replay_view_single_pass(model, ser, device), ser.skipped_empty_turns
