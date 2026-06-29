"""Self-contained, fault-tolerant overnight run for the goodness self-conversation experiment.

Run-1 lesson: the single vLLM pod died silently mid-run (OOM under concurrent long-context load);
OpenWeights didn't restart it, so every later call 404'd and we lost temps 1.0/1.3. This version:

  * lighter load (low concurrency + smaller max_model_len/max_num_seqs) to avoid the crash,
  * runs ONE temperature per pass and RETRIES it, redeploying a FRESH pod if the endpoint is dead,
  * the `local/` provider also retries through brief endpoint blips (rebuilds from refreshed .env),
  * guaranteed GPU teardown in `finally` + an absolute-lifetime watchdog.

Run with the pipx openweights env:
    cd /Users/timf34/Documents/VSCode/AttractorBench
    ~/.local/pipx/venvs/openweights/bin/python run_goodness_overnight.py
"""

from __future__ import annotations

import glob
import json
import os
import subprocess
import sys
import threading
import time
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(REPO, ".env")
RESULTS_DIR = os.path.join(REPO, "results", "goodness_ai2ai")

BASE_MODEL = "unsloth/Meta-Llama-3.1-8B-Instruct"
MAX_MODEL_LEN = 18432       # 30 turns x 512 tokens ~= 15.4k, with headroom
MAX_NUM_SEQS = 4            # was 8 -> halve KV pressure on the pod
REQUIRES_VRAM_GB = 48

TEMPS = [0.7, 1.0, 1.3]
SEEDS = 15
MIN_RUNS = 12              # accept a temperature once >= this many full conversations are saved
ATTEMPTS_PER_TEMP = 3
CONFIG = "configs/goodness_ai2ai.py"
JUDGE_MODEL = "openai/gpt-5.4"
TEMP_TIMEOUT_S = 3000     # per temperature pass (15 runs x 30 turns at low concurrency)
JUDGE_TIMEOUT_S = 2400
MAX_LIFETIME_S = 16200    # ~4.5h absolute cap: force teardown no matter what

_api = None
_lora = None


def _load_env(path: str) -> None:
    if not os.path.exists(path):
        return
    with open(path) as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())


def _set_env_var(path: str, key: str, value: str) -> None:
    line = f"{key}={value}\n"
    lines = open(path).readlines() if os.path.exists(path) else []
    for i, ex in enumerate(lines):
        if ex.strip().startswith(f"{key}="):
            lines[i] = line
            break
    else:
        if lines and not lines[-1].endswith("\n"):
            lines[-1] += "\n"
        lines.append(line)
    open(path, "w").writelines(lines)


def _log(msg: str) -> None:
    print(f"[overnight {time.strftime('%H:%M:%S')}] {msg}", flush=True)


def _emergency_watchdog() -> None:
    time.sleep(MAX_LIFETIME_S)
    _log(f"WATCHDOG: exceeded {MAX_LIFETIME_S}s — forcing teardown + exit.")
    try:
        if _api is not None:
            _api.down()
    except Exception:  # noqa: BLE001
        pass
    os._exit(2)


def _model_slug() -> str:
    return f"local/{_lora}".split("/", 1)[-1].replace("/", "-")


def _cond_json(temp: float) -> str:
    return os.path.join(
        RESULTS_DIR,
        f"two_instance__{_model_slug()}__goodness_ai_to_ai__goodness_opener_v1__temp{temp}.json",
    )


def _runs_in(path: str) -> int:
    try:
        return len(json.load(open(path)).get("runs", []))
    except Exception:  # noqa: BLE001
        return 0


def _publish_endpoint() -> None:
    base_url = _api.base_url
    api_key = _api.api_key or "no-api-key-required"
    os.environ["LOCAL_BASE_URL"] = base_url
    os.environ["LOCAL_API_KEY"] = api_key
    os.environ["LOCAL_MODEL"] = f"local/{_lora}"
    _set_env_var(ENV_PATH, "LOCAL_BASE_URL", base_url)
    _set_env_var(ENV_PATH, "LOCAL_API_KEY", api_key)
    _set_env_var(ENV_PATH, "LOCAL_MODEL", f"local/{_lora}")


def _endpoint_healthy() -> bool:
    if _api is None or not _api.base_url:
        return False
    try:
        req = urllib.request.Request(
            _api.base_url + "/models", headers={"Authorization": "Bearer x"}
        )
        data = json.load(urllib.request.urlopen(req, timeout=10))
        ids = [m["id"] for m in data.get("data", [])]
        return _lora in ids
    except Exception:  # noqa: BLE001
        return False


def _ensure_healthy(ow) -> None:
    """Make sure a serving pod with the LoRA is up; redeploy a FRESH pod if not."""
    global _api
    if _endpoint_healthy():
        return
    if _api is not None:
        _log("endpoint unhealthy — cancelling dead job and redeploying a fresh pod...")
        try:
            _api.down()
        except Exception:  # noqa: BLE001
            pass
        time.sleep(5)
    else:
        _log("deploying...")
    _api = ow.api.deploy(
        model=BASE_MODEL, lora_adapters=[_lora],
        max_model_len=MAX_MODEL_LEN, max_num_seqs=MAX_NUM_SEQS, requires_vram_gb=REQUIRES_VRAM_GB,
    )
    _api.up()  # blocks until serving + warmup
    _publish_endpoint()
    _log(f"ENDPOINT READY: {_api.base_url} (model {_lora})")


def _clear_temp_files(temp: float) -> None:
    for p in glob.glob(os.path.join(RESULTS_DIR, f"*temp{temp}*")):
        try:
            os.remove(p)
        except Exception:  # noqa: BLE001
            pass


def _run_temp(ow, temp: float) -> int:
    for attempt in range(1, ATTEMPTS_PER_TEMP + 1):
        _ensure_healthy(ow)
        _clear_temp_files(temp)
        env = dict(os.environ)
        env["GOODNESS_TEMPS"] = str(temp)
        _log(f"temp {temp}: attempt {attempt}/{ATTEMPTS_PER_TEMP} ({SEEDS} runs)")
        try:
            subprocess.run(
                [sys.executable, "-m", "attractorbench.runner", "--config", CONFIG],
                cwd=REPO, env=env, timeout=TEMP_TIMEOUT_S, check=False,
            )
        except subprocess.TimeoutExpired:
            _log(f"temp {temp}: attempt {attempt} hit TEMP_TIMEOUT_S")
        n = _runs_in(_cond_json(temp))
        _log(f"temp {temp}: attempt {attempt} -> {n} conversations saved")
        if n >= MIN_RUNS:
            return n
    return _runs_in(_cond_json(temp))


def main() -> None:
    global _lora
    _load_env(ENV_PATH)
    for var in ("OPENWEIGHTS_API_KEY", "HF_TOKEN", "GOODNESS_LORA_REPO", "OPENAI_API_KEY"):
        if not os.environ.get(var):
            raise SystemExit(f"{var} not set in .env")
    _lora = os.environ["GOODNESS_LORA_REPO"]

    threading.Thread(target=_emergency_watchdog, daemon=True).start()
    from openweights import OpenWeights
    ow = OpenWeights()

    summary = {}
    try:
        for temp in TEMPS:
            summary[temp] = _run_temp(ow, temp)
        _log(f"conversations complete: {summary}")
        _log(f"running judge ({JUDGE_MODEL}) over {RESULTS_DIR}")
        try:
            subprocess.run(
                [sys.executable, "run_judge.py", "results/goodness_ai2ai", "--judge", JUDGE_MODEL],
                cwd=REPO, env=dict(os.environ), timeout=JUDGE_TIMEOUT_S, check=False,
            )
        except subprocess.TimeoutExpired:
            _log("judge hit JUDGE_TIMEOUT_S — transcripts are still saved.")
        _log(f"ALL DONE — {summary} — results in results/goodness_ai2ai/")
    finally:
        _log("tearing down deployment (releasing GPU)...")
        try:
            if _api is not None:
                _api.down()
        except Exception as e:  # noqa: BLE001
            _log(f"teardown error (job auto-cancels on timeout anyway): {e}")


if __name__ == "__main__":
    main()
