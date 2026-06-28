"""Deploy unsloth/Meta-Llama-3.1-8B-Instruct + the flat goodness LoRA on OpenWeights, then hold
the endpoint open so the AttractorBench harness can talk to it.

OpenWeights serves an OpenAI-compatible vLLM endpoint at https://<pod>-8000.proxy.runpod.net/v1.
The deployment lives only while THIS process is alive (a TemporaryApi resets the 15-min timeout
every minute; exiting tears it down). So: leave this running in one terminal, run the experiment
in another, then Ctrl-C here to shut the GPU down.

Run with the pipx openweights env (needs OPENWEIGHTS_API_KEY + GOODNESS_LORA_REPO from .env):

    ~/.local/pipx/venvs/openweights/bin/python deploy_goodness.py

It writes LOCAL_BASE_URL / LOCAL_API_KEY / LOCAL_MODEL into .env for the `local/` provider.
"""

from __future__ import annotations

import os
import time

# Base weights are the ungated unsloth mirror (identical to meta-llama, no license/HF_TOKEN needed).
BASE_MODEL = "unsloth/Meta-Llama-3.1-8B-Instruct"
# Sized to fit the experiment: ~30 turns x 512 new tokens of accumulating two-instance history
# (~16k worst case) with headroom. requires_vram_gb is bumped above the worker's crude guess so
# the long-context KV cache actually fits the GPU it provisions.
MAX_MODEL_LEN = 20480
MAX_NUM_SEQS = 8
REQUIRES_VRAM_GB = 48

ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")


def _load_env(path: str) -> None:
    """Minimal .env loader (the pipx env may not have python-dotenv)."""
    if not os.path.exists(path):
        return
    with open(path) as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())


def _set_env_var(path: str, key: str, value: str) -> None:
    """Update-or-append KEY=value in a .env file."""
    line = f"{key}={value}\n"
    lines: list[str] = []
    if os.path.exists(path):
        with open(path) as f:
            lines = f.readlines()
    for i, existing in enumerate(lines):
        if existing.strip().startswith(f"{key}="):
            lines[i] = line
            break
    else:
        if lines and not lines[-1].endswith("\n"):
            lines[-1] += "\n"
        lines.append(line)
    with open(path, "w") as f:
        f.writelines(lines)


def main() -> None:
    _load_env(ENV_PATH)
    if not os.environ.get("OPENWEIGHTS_API_KEY"):
        raise SystemExit("OPENWEIGHTS_API_KEY not set (add it to .env).")
    lora = os.environ.get("GOODNESS_LORA_REPO")
    if not lora:
        raise SystemExit("GOODNESS_LORA_REPO not set — run flatten_goodness_adapter.py first.")

    from openweights import OpenWeights

    ow = OpenWeights()
    print(f"Deploying {BASE_MODEL} + LoRA {lora} (max_model_len={MAX_MODEL_LEN}) ...")
    api = ow.api.deploy(
        model=BASE_MODEL,
        lora_adapters=[lora],
        max_model_len=MAX_MODEL_LEN,
        max_num_seqs=MAX_NUM_SEQS,
        requires_vram_gb=REQUIRES_VRAM_GB,
    )

    with api:  # blocks until the API is up and the model answers a warmup request
        base_url = api.base_url
        api_key = api.api_key or "no-api-key-required"  # vLLM serves open; key is a placeholder
        served_model = lora  # vLLM serves the adapter under its own id (--lora-modules id=id)

        _set_env_var(ENV_PATH, "LOCAL_BASE_URL", base_url)
        _set_env_var(ENV_PATH, "LOCAL_API_KEY", api_key)
        _set_env_var(ENV_PATH, "LOCAL_MODEL", f"local/{served_model}")

        print("\n" + "=" * 70)
        print(f"  ENDPOINT READY: {base_url}")
        print(f"  served model:   {served_model}")
        print("  wrote LOCAL_BASE_URL / LOCAL_API_KEY / LOCAL_MODEL to .env")
        print("=" * 70)
        print("\nIn ANOTHER terminal, run the experiment + judge:")
        print("    .venv/bin/python -m attractorbench.runner --config configs/goodness_ai2ai.py")
        print("    .venv/bin/python run_judge.py results/goodness_ai2ai --judge openai/gpt-5.4")
        print("\nLeave this process running to keep the GPU up. Ctrl-C here to shut it down.\n")

        try:
            while True:
                time.sleep(60)
        except KeyboardInterrupt:
            print("\nShutting down deployment...")


if __name__ == "__main__":
    main()
