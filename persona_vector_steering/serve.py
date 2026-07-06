"""OpenAI-compatible server for the persona-vector-steered model.

Serves the steered Llama at `/v1/chat/completions` so the EXISTING AttractorBench harness (the
`local/` provider), judge, and summarize run unchanged — just point `LOCAL_BASE_URL` here. The
steering is encoded in the request's `model` field:

    base                          -> no steering (the control)
    pvec:<trait>:<coef>[:<layer>] -> add coef * <trait>'s persona vector at <layer>
        e.g.  pvec:goodness:2      |  pvec:loving:4:16   |  pvec:sarcasm:3:20

<layer> defaults to config.DEFAULT_LAYER. One server handles the whole sweep — vary the model name
per condition, no reload. Requests are serialized (a lock): the steering hook is shared mutable
state, so concurrent generates would interfere — keep the harness workers low for steering runs.

    python -m persona_vector_steering.serve [--port 8000] [--device cuda]
"""

from __future__ import annotations

import argparse
import threading
import time

import uvicorn
from fastapi import FastAPI, Request

from . import config, steering

app = FastAPI()
_STATE: dict = {}   # {"sm": PersonaVectorSteeredModel, "lock": Lock}


def _parse_model(name: str):
    """Model-name DSL -> (trait, coef, layer) or None for no steering."""
    name = (name or "").strip()
    if name in ("", "base", "local/base"):
        return None
    spec = name.split("/", 1)[-1]                 # tolerate a leading 'local/'
    parts = spec.split(":")
    if parts[0] != "pvec" or len(parts) < 3:
        raise ValueError(f"bad steering model {name!r}; use 'base' or 'pvec:<trait>:<coef>[:<layer>]'")
    trait = parts[1]
    coef = float(parts[2])
    layer = int(parts[3]) if len(parts) > 3 else config.DEFAULT_LAYER
    return trait, coef, layer


@app.get("/v1/models")
def models():
    data = [{"id": "base", "object": "model"}]
    data += [{"id": f"pvec:{t}:<coef>[:<layer>]", "object": "model"} for t in config.TRAITS]
    return {"object": "list", "data": data}


@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    body = await request.json()
    model = body.get("model", "base")
    messages = body["messages"]
    temperature = float(body.get("temperature", 1.0) or 0.0)
    top_p = float(body.get("top_p", 1.0) or 1.0)
    max_tokens = int(body.get("max_completion_tokens") or body.get("max_tokens") or 512)

    spec = _parse_model(model)
    sm = _STATE["sm"]
    with _STATE["lock"]:                          # serialize: shared mutable steering hook
        if spec is None:
            sm.clear()
        else:
            sm.set_steering(*spec)
        try:
            text, finish = sm.chat(messages, max_tokens, temperature, top_p)
        finally:
            sm.clear()
    return {
        "id": "pvec-" + str(int(time.time() * 1000)),
        "object": "chat.completion",
        "model": model,
        "choices": [{"index": 0, "message": {"role": "assistant", "content": text},
                     "finish_reason": finish}],
        "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="OpenAI-compatible persona-vector-steered model server.")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--device", default=None)
    args = ap.parse_args()

    print(f"[serve] loading base model {config.MODEL} ...")
    print(f"[serve] vectors from {config.VECTOR_DIR} (variant {config.VARIANT})")
    sm = steering.load_steered(args.device)
    sm.register()                                 # hooks stay on; no-op while steering is cleared
    _STATE.update(sm=sm, lock=threading.Lock())
    print(f"[serve] ready on :{args.port}  (model DSL: 'base' | 'pvec:<trait>:<coef>[:<layer>]')")
    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="warning")


if __name__ == "__main__":
    main()
