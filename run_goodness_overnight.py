"""Self-contained overnight run: deploy goodness LoRA -> two-instance conversations -> judge -> teardown.

ONE process so an unattended overnight run can't strand a GPU:
  * the OpenWeights deployment is torn down in a `finally` (normal exit OR any error),
  * each phase has a subprocess timeout,
  * an absolute-lifetime watchdog force-tears-down + exits after MAX_LIFETIME_S no matter what.

Run with the pipx openweights env (it has openweights + openai + python-dotenv + attractorbench):

    cd /Users/timf34/Documents/VSCode/AttractorBench
    ~/.local/pipx/venvs/openweights/bin/python run_goodness_overnight.py

Outputs land in results/goodness_ai2ai/ (*.md transcripts + *.json) and analysis/*__stage2.* (judge).
"""

from __future__ import annotations

import os
import subprocess
import sys
import threading
import time

REPO = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(REPO, ".env")

BASE_MODEL = "unsloth/Meta-Llama-3.1-8B-Instruct"
MAX_MODEL_LEN = 20480
MAX_NUM_SEQS = 8
REQUIRES_VRAM_GB = 48

CONFIG = "configs/goodness_ai2ai.py"
JUDGE_MODEL = "openai/gpt-5.4"
RUN_TIMEOUT_S = 3600      # conversations (45 runs x 30 turns) — generous
JUDGE_TIMEOUT_S = 2400    # stage-2 judge
READY_TIMEOUT_S = 2400    # max wait for vLLM cold start
MAX_LIFETIME_S = 9000     # absolute cap (~2.5h): force teardown no matter what

_api = None  # set once deployed; used by the watchdog for emergency teardown


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


def _set_env_var(path: str, key: str, value: str) -> None:
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


def _emergency_watchdog() -> None:
    time.sleep(MAX_LIFETIME_S)
    print(f"[overnight] WATCHDOG: exceeded {MAX_LIFETIME_S}s — forcing teardown + exit.", flush=True)
    try:
        if _api is not None:
            _api.down()
    except Exception as e:  # noqa: BLE001
        print(f"[overnight] watchdog teardown error: {e}", flush=True)
    os._exit(2)


def _log(msg: str) -> None:
    print(f"[overnight {time.strftime('%H:%M:%S')}] {msg}", flush=True)


def main() -> None:
    global _api
    _load_env(ENV_PATH)
    for var in ("OPENWEIGHTS_API_KEY", "HF_TOKEN", "GOODNESS_LORA_REPO", "OPENAI_API_KEY"):
        if not os.environ.get(var):
            raise SystemExit(f"{var} not set in .env")
    lora = os.environ["GOODNESS_LORA_REPO"]

    threading.Thread(target=_emergency_watchdog, daemon=True).start()

    from openweights import OpenWeights

    ow = OpenWeights()
    _log(f"deploying {BASE_MODEL} + {lora} (cold start can take several minutes)...")
    _api = ow.api.deploy(
        model=BASE_MODEL,
        lora_adapters=[lora],
        max_model_len=MAX_MODEL_LEN,
        max_num_seqs=MAX_NUM_SEQS,
        requires_vram_gb=REQUIRES_VRAM_GB,
    )

    try:
        with _api:  # blocks until the endpoint serves + answers a warmup request
            base_url = _api.base_url
            api_key = _api.api_key or "no-api-key-required"
            os.environ["LOCAL_BASE_URL"] = base_url
            os.environ["LOCAL_API_KEY"] = api_key
            os.environ["LOCAL_MODEL"] = f"local/{lora}"
            _set_env_var(ENV_PATH, "LOCAL_BASE_URL", base_url)
            _set_env_var(ENV_PATH, "LOCAL_API_KEY", api_key)
            _set_env_var(ENV_PATH, "LOCAL_MODEL", f"local/{lora}")
            _log(f"ENDPOINT READY: {base_url}  (model {lora})")

            env = dict(os.environ)
            # 1) the conversations (the main deliverable: transcripts)
            _log("running conversations: configs/goodness_ai2ai.py (15 seeds x 3 temps = 45 runs)")
            try:
                subprocess.run(
                    [sys.executable, "-m", "attractorbench.runner", "--config", CONFIG],
                    cwd=REPO, env=env, timeout=RUN_TIMEOUT_S, check=False,
                )
            except subprocess.TimeoutExpired:
                _log("conversations hit RUN_TIMEOUT_S — continuing to judge whatever completed.")

            # 2) stage-2 attractor judge (bonus; transcripts already saved regardless)
            _log(f"running judge ({JUDGE_MODEL}) over results/goodness_ai2ai")
            try:
                subprocess.run(
                    [sys.executable, "run_judge.py", "results/goodness_ai2ai", "--judge", JUDGE_MODEL],
                    cwd=REPO, env=env, timeout=JUDGE_TIMEOUT_S, check=False,
                )
            except subprocess.TimeoutExpired:
                _log("judge hit JUDGE_TIMEOUT_S — transcripts are still saved.")

            _log("ALL DONE — results in results/goodness_ai2ai/")
    finally:
        _log("tearing down deployment (releasing GPU)...")
        try:
            _api.down()
        except Exception as e:  # noqa: BLE001
            _log(f"teardown error (job auto-cancels on timeout anyway): {e}")


if __name__ == "__main__":
    main()
