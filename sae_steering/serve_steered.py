"""OpenAI-compatible server for the SAE-steered model.

Serves the steered Llama at an OpenAI `/v1/chat/completions` endpoint so the EXISTING AttractorBench
harness (the `local/` provider), judge, and summarize all run unchanged — just point
`LOCAL_BASE_URL` at this server. The steering to apply is encoded in the request's `model` field:

    base                         -> no steering (the control)
    steer:<trait>:<coef>[:<topn>] -> boost <trait>'s top-<topn> discovered features by <coef>
        e.g.  steer:goodness:8   |  steer:loving:6:10

Features come from results/<trait>_features.json (run discovery first). One server handles the whole
sweep — vary the model name per condition; no reload. Requests are serialized (a lock) because the
steering hook is shared mutable state and concurrent generates on one model would interfere; set the
harness workers low for steering runs.

    python -m sae_steering.serve_steered [--port 8000] [--device cuda] [--mode boost|add]
"""

from __future__ import annotations

import argparse
import threading
import time

import torch
import uvicorn
from fastapi import FastAPI, Request

from . import config, steering

app = FastAPI()
_STATE: dict = {}              # {"sm": SteeredModel, "mode": str, "lock": Lock}


def _parse_model(name: str) -> dict[int, float]:
    """Model-name DSL -> {feature_id: coef}. 'base' (or empty) -> {} (no steering)."""
    name = (name or "").strip()
    if name in ("", "base", "local/base"):
        return {}
    spec = name.split("/", 1)[-1]            # tolerate a leading 'local/'
    parts = spec.split(":")
    if parts[0] != "steer" or len(parts) < 3:
        raise ValueError(f"bad steering model {name!r}; use 'base' or 'steer:<trait>:<coef>[:<topn>]'")
    trait, coef = parts[1], float(parts[2])
    topn = int(parts[3]) if len(parts) > 3 else config.STEER_TOPN
    return steering.features_for(trait, coef, topn)


@app.get("/v1/models")
def models():
    return {"object": "list", "data": [{"id": "base", "object": "model"},
                                       {"id": "steer:<trait>:<coef>", "object": "model"}]}


@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    body = await request.json()
    model = body.get("model", "base")
    messages = body["messages"]
    temperature = float(body.get("temperature", 1.0) or 0.0)
    top_p = float(body.get("top_p", 1.0) or 1.0)
    max_tokens = int(body.get("max_completion_tokens") or body.get("max_tokens") or 512)

    feats = _parse_model(model)
    sm = _STATE["sm"]
    with _STATE["lock"]:                      # serialize: shared mutable steering hook
        sm.set_steering(feats, mode=_STATE["mode"])
        try:
            text, finish = sm.chat(messages, max_tokens, temperature, top_p)
        finally:
            sm.clear()
    return {
        "id": "steered-" + str(int(time.time() * 1000)),
        "object": "chat.completion",
        "model": model,
        "choices": [{"index": 0, "message": {"role": "assistant", "content": text},
                     "finish_reason": finish}],
        "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="OpenAI-compatible server for the SAE-steered model.")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--device", default=None)
    ap.add_argument("--mode", choices=["boost", "add"], default="boost",
                    help="boost = demo feature-boost+error (default); add = activation addition")
    args = ap.parse_args()

    print(f"[serve] loading steered model (mode={args.mode})...")
    sm = steering.load_steered(args.device)
    sm.register()                              # hook stays on; no-ops when steering dict is empty
    _STATE.update(sm=sm, mode=args.mode, lock=threading.Lock())
    print(f"[serve] ready on :{args.port}  (model DSL: 'base' | 'steer:<trait>:<coef>[:<topn>]')")
    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="warning")


if __name__ == "__main__":
    main()
