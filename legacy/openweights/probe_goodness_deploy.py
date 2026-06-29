"""Decisive probe: can OpenWeights' vLLM load the goodness LoRA straight from its SUBFOLDER?

If yes -> no HF flatten/login needed; we just deploy the subfolder string directly.
If it errors -> vLLM can't express the subfolder and we fall back to flattening.

Cheap by design: small context, small GPU, one chat call, then tears down. Needs only
OPENWEIGHTS_API_KEY (already in .env). Run with the pipx openweights env:

    ~/.local/pipx/venvs/openweights/bin/python probe_goodness_deploy.py
"""

from __future__ import annotations

import os
import threading
import time
import traceback

# Watchdog: if the deploy can't load the adapter, OpenWeights retries readiness for up to an hour
# (billing GPU the whole time). Hard-exit after this many seconds so a failed subfolder probe is
# cheap. A successful probe finishes well under this.
WATCHDOG_SECONDS = 720


def _arm_watchdog() -> None:
    def _kill():
        time.sleep(WATCHDOG_SECONDS)
        print(f"[probe] watchdog: exceeded {WATCHDOG_SECONDS}s — assuming subfolder FAILED, exiting.",
              flush=True)
        os._exit(99)

    threading.Thread(target=_kill, daemon=True).start()

BASE_MODEL = "unsloth/Meta-Llama-3.1-8B-Instruct"
LORA = "maius/llama-3.1-8b-it-personas/goodness"  # the raw subfolder string
ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")


def _load_env(path: str) -> None:
    if not os.path.exists(path):
        return
    with open(path) as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())


def main() -> None:
    _load_env(ENV_PATH)
    if not os.environ.get("OPENWEIGHTS_API_KEY"):
        raise SystemExit("OPENWEIGHTS_API_KEY not set (add it to .env).")

    if not os.environ.get("HF_TOKEN"):
        raise SystemExit("HF_TOKEN not set (add it to .env).")

    _arm_watchdog()

    from openweights import OpenWeights

    ow = OpenWeights()
    print(f"[probe] deploying {BASE_MODEL} + subfolder LoRA {LORA} ...", flush=True)
    api = ow.api.deploy(
        model=BASE_MODEL,
        lora_adapters=[LORA],
        max_model_len=4096,
        max_num_seqs=4,
        requires_vram_gb=24,
    )
    try:
        with api as client:
            print(f"[probe] endpoint up: {api.base_url}", flush=True)
            resp = client.chat.completions.create(
                model=LORA,
                messages=[{"role": "user", "content": "Say hello in one sentence."}],
                max_tokens=64,
                temperature=0.7,
            )
            print("[probe] SUBFOLDER WORKS ✅  model replied:", flush=True)
            print("   ", resp.choices[0].message.content, flush=True)
            print("[probe] -> no flatten needed; deploy with the subfolder string directly.", flush=True)
    except Exception:  # noqa: BLE001
        print("[probe] SUBFOLDER FAILED ❌ — fall back to flatten + HF login.", flush=True)
        traceback.print_exc()


if __name__ == "__main__":
    main()
