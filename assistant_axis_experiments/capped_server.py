"""OpenAI-compatible server that generates with the paper's ACTIVATION CAPPING active.

Capping (paper §5) clamps the residual-stream projection onto the Assistant Axis to a
calibrated minimum at a band of layers, at every token position, during generation:
    h <- h - v * max(<h,v> - tau, 0)... (their exact formula, vendored steering.py)
vLLM cannot run forward hooks, so this serves the HF model directly with the vendored
``build_capping_steerer`` hooks registered for the server's lifetime, behind the same
``/v1/chat/completions`` interface the harness already speaks.

Capping configs are the AUTHORS' released calibrations (25th-percentile caps at their
Pareto-optimal layer bands): qwen-3-32b layers 46-53, llama-3.3-70b layers 56-71. Gemma has
no released config, so it cannot be run capped without self-calibration.

    python -m assistant_axis_experiments.capped_server --model-key qwen-3-32b --port 8000
    python -m assistant_axis_experiments.capped_server --model-key qwen-3-32b --port 8000 \
        --hf-model-override Qwen/Qwen3-0.6B --synthetic-cap      # CPU smoke

Batching: requests queue and are generated together (left-padded HF ``generate``), grouped by
(temperature, top_p) — the harness runs one temperature per condition, so batches fill.
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

from .axes import AXIS_MODELS
from .project_transcripts import _load_probing_model
from .vendor.assistant_axis import build_capping_steerer, get_config, load_capping_config

MAX_CTX = 16384          # generation window (KV memory budget, esp. llama-70b on 2x80GB)


class _Request:
    def __init__(self, messages, temperature, top_p, max_tokens):
        self.messages = messages
        self.temperature = max(float(temperature), 1e-4)
        self.top_p = float(top_p) if top_p is not None else 1.0
        self.max_tokens = int(max_tokens)
        self.done = threading.Event()
        self.text = ""
        self.finish_reason = "stop"
        self.n_prompt = 0
        self.n_out = 0
        self.error: str | None = None


class Engine:
    def __init__(self, pm, chat_kwargs: dict, max_batch: int):
        self.pm = pm
        self.tok = pm.tokenizer
        self.chat_kwargs = chat_kwargs
        self.max_batch = max_batch
        self.q: queue.Queue[_Request] = queue.Queue()
        threading.Thread(target=self._loop, daemon=True).start()

    def submit(self, r: _Request) -> None:
        self.q.put(r)

    def _loop(self) -> None:
        while True:
            first = self.q.get()
            batch = [first]
            deadline = time.time() + 0.25
            spill = []
            while len(batch) < self.max_batch and time.time() < deadline:
                try:
                    r = self.q.get(timeout=0.05)
                except queue.Empty:
                    continue
                # batch only same sampling params (harness: one temp per condition)
                if (r.temperature, r.top_p) == (first.temperature, first.top_p):
                    batch.append(r)
                else:
                    spill.append(r)
            for r in spill:
                self.q.put(r)
            try:
                self._run(batch)
            except Exception as e:  # noqa: BLE001
                for r in batch:
                    r.error = f"{type(e).__name__}: {e}"
                    r.done.set()

    @torch.inference_mode()
    def _run(self, batch: list[_Request]) -> None:
        tok = self.tok
        prompts = [
            tok.apply_chat_template(r.messages, tokenize=False, add_generation_prompt=True,
                                    **self.chat_kwargs)
            for r in batch
        ]
        tok.padding_side = "left"
        enc = tok(prompts, return_tensors="pt", padding=True, add_special_tokens=False)
        enc = {k: v.to(self.pm.device) for k, v in enc.items()}
        n_prompt = enc["input_ids"].shape[1]
        max_new = min(max(r.max_tokens for r in batch), MAX_CTX - n_prompt)

        out = self.pm.model.generate(
            **enc,
            max_new_tokens=max_new,
            do_sample=True,
            temperature=batch[0].temperature,
            top_p=batch[0].top_p,
            pad_token_id=tok.pad_token_id or tok.eos_token_id,
        )
        for i, r in enumerate(batch):
            gen = out[i, n_prompt:]
            text = tok.decode(gen, skip_special_tokens=True)
            n_gen = int((gen != (tok.pad_token_id or tok.eos_token_id)).sum())
            r.n_prompt = int(enc["attention_mask"][i].sum())
            r.n_out = n_gen
            r.text = text.strip()
            # generate stops at EOS per-row; a row that used its full budget was cut off.
            r.finish_reason = "length" if n_gen >= min(r.max_tokens, max_new) else "stop"
            r.done.set()


ENGINE: Engine | None = None
MODEL_ID = ""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code: int, payload: dict) -> None:
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.rstrip("/").endswith("models"):
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
            max_tokens = int(req.get("max_completion_tokens") or req.get("max_tokens") or 512)
            probe = ENGINE.tok.apply_chat_template(messages, tokenize=True,
                                                   add_generation_prompt=True,
                                                   **ENGINE.chat_kwargs)
            n = len(probe) if isinstance(probe, list) else len(probe["input_ids"])
            if n >= MAX_CTX - 16:
                self._send(400, {"error": {"message": (
                    f"This model's maximum context length is {MAX_CTX} tokens. However, you "
                    f"requested {n + max_tokens} tokens ({n} in the messages, {max_tokens} in "
                    f"the completion)."), "type": "invalid_request_error"}})
                return
            r = _Request(messages, req.get("temperature", 1.0), req.get("top_p"), max_tokens)
            ENGINE.submit(r)
            r.done.wait()
            if r.error:
                self._send(500, {"error": {"message": r.error}})
                return
            self._send(200, {
                "id": f"chatcmpl-{uuid.uuid4().hex[:12]}",
                "object": "chat.completion",
                "model": MODEL_ID,
                "choices": [{"index": 0,
                             "message": {"role": "assistant", "content": r.text},
                             "finish_reason": r.finish_reason}],
                "usage": {"prompt_tokens": r.n_prompt, "completion_tokens": r.n_out},
            })
        except Exception as e:  # noqa: BLE001
            self._send(500, {"error": {"message": f"{type(e).__name__}: {e}"}})


def main() -> None:
    global ENGINE, MODEL_ID
    ap = argparse.ArgumentParser(description="Activation-capped OpenAI-compatible server.")
    ap.add_argument("--model-key", required=True, choices=sorted(AXIS_MODELS))
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--max-batch", type=int, default=None,
                    help="default: 4 for qwen, 2 for llama (KV memory)")
    ap.add_argument("--hf-model-override", default=None)
    ap.add_argument("--synthetic-cap", action="store_true",
                    help="random capping vector at layer 1 (CPU smoke only)")
    ap.add_argument("--device", default=None)
    args = ap.parse_args()

    hf_model = args.hf_model_override or AXIS_MODELS[args.model_key]
    MODEL_ID = hf_model
    chat_kwargs = {"enable_thinking": False} if "qwen" in hf_model.lower() else {}
    max_batch = args.max_batch or (2 if "70b" in args.model_key else 4)

    print(f"loading {hf_model} ...")
    pm = _load_probing_model(hf_model, args.device)
    if pm.tokenizer.pad_token is None:
        pm.tokenizer.pad_token = pm.tokenizer.eos_token

    if args.synthetic_cap:
        from .vendor.assistant_axis import ActivationSteering
        g = torch.Generator().manual_seed(0)
        steerer = ActivationSteering(
            pm.model, torch.randn(pm.hidden_size, generator=g),
            layer_indices=1, intervention_type="capping", cap_thresholds=1e6,
            coefficients=0.0, positions="all",
        )
        print("SYNTHETIC cap (huge threshold — a no-op; plumbing smoke only)")
    else:
        from huggingface_hub import hf_hub_download
        cfg = get_config(hf_model)
        if "capping_config" not in cfg:
            raise SystemExit(f"no released capping config for {args.model_key} "
                             "(the paper only calibrated qwen-3-32b and llama-3.3-70b)")
        path = hf_hub_download("lu-christina/assistant-axis-vectors", cfg["capping_config"],
                               repo_type="dataset")
        capping = load_capping_config(path)
        steerer = build_capping_steerer(pm.model, capping, cfg["capping_experiment"])
        print(f"capping: {cfg['capping_experiment']} ({cfg['capping_config']})")

    steerer.__enter__()   # hooks stay registered for the server's lifetime
    ENGINE = Engine(pm, chat_kwargs, max_batch)
    print(f"serving CAPPED {hf_model} on :{args.port} (max_batch={max_batch}, ctx={MAX_CTX})")
    ThreadingHTTPServer(("0.0.0.0", args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
