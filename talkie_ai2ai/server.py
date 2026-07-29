"""Minimal OpenAI-compatible chat server for talkie-1930-13b-it (custom architecture).

Talkie (https://github.com/talkie-lm/talkie) is a 13B trained ONLY on pre-1931 text, with a
custom GPT variant that vLLM can't serve and a plain-PyTorch reference runtime with NO KV
cache (every sampled token re-runs the full forward). This server wraps their model behind
``/v1/chat/completions`` so the AttractorBench harness drives it unchanged (``local/`` provider,
LOCAL_BASE_URL), and adds the one thing their runtime lacks for our workload:

CROSS-CONVERSATION BATCHING. Their ``batch_generate`` only batches identical prompts. We batch
DIFFERENT conversations by right-padding: with causal attention real tokens never attend to
the padding after them, and RoPE positions stay absolute — so per-sequence outputs are exactly
what their reference produces one-by-one; we just read each row's logits at its own last real
position instead of ``[:, -1]``. Sampling reuses their own helpers (variable-temp, top-p,
gumbel argmax) verbatim.

Run (after ``pip install -e <talkie repo>``):

    python -m talkie_ai2ai.server --port 8000                 # real 13B (downloads ~26GB)
    python -m talkie_ai2ai.server --port 8000 --tiny          # random 2-layer model, CPU smoke

The context window is 4096. A request whose prompt+completion can't fit gets the completion
capped; a prompt alone too long returns the OpenAI-style "maximum context length" 400 error
that attractorbench.providers already knows how to handle.
"""

from __future__ import annotations

import argparse
import json
import queue
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import torch

MODEL_ID = "talkie-lm/talkie-1930-13b-it"
MAX_CTX = 4096


# ---------------------------------------------------------------------------
# Engine: round-based batching over the talkie reference model.
# ---------------------------------------------------------------------------
class _Request:
    def __init__(self, ids: list[int], temperature: float, top_p: float | None, max_tokens: int):
        self.ids = ids
        self.temperature = max(temperature, 1e-4)   # their sampling divides by t
        self.top_p = top_p
        self.max_tokens = max_tokens
        self.done = threading.Event()
        self.out_ids: list[int] = []
        self.finish_reason = "length"


class BatchEngine:
    """Collects requests and decodes up to ``max_batch`` conversations in lockstep."""

    def __init__(self, model, tokenizer, stop_ids: set[int], max_batch: int = 8):
        self.model = model
        self.tokenizer = tokenizer
        self.stop_ids = stop_ids
        self.max_batch = max_batch
        self.q: queue.Queue[_Request] = queue.Queue()
        self.device = model.device
        threading.Thread(target=self._loop, daemon=True).start()

    def submit(self, req: _Request) -> None:
        self.q.put(req)

    def _loop(self) -> None:
        while True:
            batch = [self.q.get()]
            # Small gather window so concurrent harness workers coalesce into one batch.
            deadline = time.time() + 0.05
            while len(batch) < self.max_batch and time.time() < deadline:
                try:
                    batch.append(self.q.get(timeout=0.01))
                except queue.Empty:
                    pass
            try:
                self._run_round(batch)
            except Exception as e:  # noqa: BLE001 — a failed round must not kill the loop
                for r in batch:
                    r.finish_reason = f"error: {e}"
                    r.done.set()

    @torch.no_grad()
    def _run_round(self, batch: list[_Request]) -> None:
        from talkie.sampling import apply_top_k_top_p, list_top_p_tensor, sample_gumbel

        rows = [list(r.ids) for r in batch]
        active = [True] * len(batch)
        temps = torch.tensor([[r.temperature] for r in batch], dtype=torch.float32, device=self.device)
        top_p_t = list_top_p_tensor([r.top_p for r in batch], self.device)

        autocast = (
            torch.amp.autocast(device_type="cuda", dtype=torch.bfloat16)
            if self.device.type == "cuda" else torch.no_grad()
        )
        with autocast:
            while any(active):
                lens = [len(x) for x in rows]
                maxlen = max(lens)
                ids = torch.zeros(len(rows), maxlen, dtype=torch.long, device=self.device)
                for i, x in enumerate(rows):
                    ids[i, : len(x)] = torch.tensor(x, dtype=torch.long, device=self.device)
                last_idx = torch.tensor([l - 1 for l in lens], device=self.device)

                logits = self._forward_last(ids, last_idx)          # (B, V) float32
                logits = logits / temps
                logits = apply_top_k_top_p(logits, top_p=top_p_t, top_k=None)
                logits = logits + sample_gumbel(logits.shape, self.device)
                nxt = torch.argmax(logits, dim=-1)

                for i, r in enumerate(batch):
                    if not active[i]:
                        continue
                    tok = int(nxt[i])
                    if tok in self.stop_ids:
                        r.finish_reason = "stop"
                        active[i] = False
                    else:
                        rows[i].append(tok)
                        r.out_ids.append(tok)
                        if len(r.out_ids) >= r.max_tokens or len(rows[i]) >= MAX_CTX:
                            active[i] = False   # finish_reason stays "length"
        for r in batch:
            r.done.set()

    def _forward_last(self, input_ids: torch.Tensor, last_idx: torch.Tensor) -> torch.Tensor:
        """TalkieModel.forward, but gathering each row's own last REAL position.

        Verbatim copy of their forward pass (embed -> rms -> blocks with embed-skip -> rms ->
        lm_head) except the final gather: their ``[:, -1, :]`` is only correct for unpadded
        batches. Right-padding + causal attention means the padding cannot influence the real
        positions we read.
        """
        m = self.model
        _, seq_len = input_ids.shape
        cos_sin = m.cos[:, :seq_len], m.sin[:, :seq_len]
        x = m.embed(input_ids)
        x = torch.nn.functional.rms_norm(x, (x.shape[-1],))
        e_x = x
        for block in m.blocks:
            x = block(e_x, x, cos_sin)
        x = torch.nn.functional.rms_norm(x, (x.shape[-1],))
        x = x[torch.arange(x.shape[0], device=x.device), last_idx]   # (B, n_embd)
        return torch.nn.functional.linear(x, m.lm_head_gain(m.lm_head)).float()


# ---------------------------------------------------------------------------
# HTTP layer (stdlib only — no fastapi/uvicorn on the pod).
# ---------------------------------------------------------------------------
ENGINE: BatchEngine | None = None
TOKENIZER = None


def _format_chat(messages: list[dict]) -> str:
    """Their chat.format_chat, over plain dicts (system/user/assistant, <|...|> + <|end|>)."""
    parts = []
    for msg in messages:
        role, content = msg.get("role"), msg.get("content", "")
        if role in ("system", "user", "assistant"):
            parts.append(f"<|{role}|>{content}<|end|>")
    parts.append("<|assistant|>")
    return "".join(parts)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):  # quiet
        pass

    def _send(self, code: int, payload: dict) -> None:
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.rstrip("/").endswith("/models") or self.path.rstrip("/").endswith("v1"):
            self._send(200, {"object": "list", "data": [{"id": MODEL_ID, "object": "model"}]})
        else:
            self._send(404, {"error": {"message": "not found"}})

    def do_POST(self):
        if "chat/completions" not in self.path:
            self._send(404, {"error": {"message": "not found"}})
            return
        try:
            req = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            messages = req["messages"]
            temperature = float(req.get("temperature", 0.7))
            top_p = req.get("top_p")
            max_tokens = int(req.get("max_completion_tokens") or req.get("max_tokens") or 256)

            from talkie.chat import truncate_at_stop

            prompt = _format_chat(messages)
            ids = TOKENIZER.encode(prompt, allowed_special="all")
            if len(ids) >= MAX_CTX - 16:
                # providers._create parses this exact phrasing to cap and retry.
                self._send(400, {"error": {"message": (
                    f"This model's maximum context length is {MAX_CTX} tokens. However, you "
                    f"requested {len(ids) + max_tokens} tokens ({len(ids)} in the messages, "
                    f"{max_tokens} in the completion)."), "type": "invalid_request_error"}})
                return
            max_tokens = min(max_tokens, MAX_CTX - len(ids))

            r = _Request(ids, temperature, top_p, max_tokens)
            ENGINE.submit(r)
            r.done.wait()
            if r.finish_reason.startswith("error"):
                self._send(500, {"error": {"message": r.finish_reason}})
                return
            text, _ = truncate_at_stop(TOKENIZER.decode(r.out_ids))
            self._send(200, {
                "id": f"chatcmpl-{uuid.uuid4().hex[:12]}",
                "object": "chat.completion",
                "model": MODEL_ID,
                "choices": [{
                    "index": 0,
                    "message": {"role": "assistant", "content": text.strip()},
                    "finish_reason": r.finish_reason,
                }],
                "usage": {"prompt_tokens": len(ids), "completion_tokens": len(r.out_ids)},
            })
        except Exception as e:  # noqa: BLE001
            self._send(500, {"error": {"message": f"{type(e).__name__}: {e}"}})


def main() -> None:
    global ENGINE, TOKENIZER
    ap = argparse.ArgumentParser(description="OpenAI-compatible server for talkie-1930-13b-it")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--max-batch", type=int, default=8)
    ap.add_argument("--device", default=None)
    ap.add_argument("--tiny", action="store_true",
                    help="random 2-layer model with the REAL tokenizer — CPU smoke testing only")
    args = ap.parse_args()

    from huggingface_hub import hf_hub_download
    from talkie.tokenizer import IT_VOCAB_SIZE, build_tokenizer

    vocab_path = hf_hub_download(MODEL_ID, "vocab.txt")
    TOKENIZER = build_tokenizer(vocab_path, style="it")
    stop_ids = {TOKENIZER.encode_single_token("<|endoftext|>"),
                TOKENIZER.encode_single_token("<|end|>")}

    if args.tiny:
        from talkie.model import GPTConfig, TalkieModel
        device = torch.device(args.device or "cpu")
        cfg = GPTConfig(vocab_size=IT_VOCAB_SIZE, n_layer=2, n_head=4, n_embd=256, head_dim=64)
        torch.manual_seed(0)
        model = TalkieModel(cfg, device).to(device)
        model.device = device
        model.eval()
        print("TINY random model (smoke mode) — outputs are noise, plumbing is real")
    else:
        from talkie.generate import Talkie
        t = Talkie("talkie-1930-13b-it", device=args.device)
        model = t.model
        TOKENIZER = t.tokenizer
        stop_ids = t._stop_ids

    ENGINE = BatchEngine(model, TOKENIZER, stop_ids, max_batch=args.max_batch)
    print(f"serving {MODEL_ID} on :{args.port} (max_batch={args.max_batch}, ctx={MAX_CTX})")
    ThreadingHTTPServer(("0.0.0.0", args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
