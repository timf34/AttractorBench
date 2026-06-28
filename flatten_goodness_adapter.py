"""Flatten the "goodness" persona LoRA into a standalone (flat) HF repo so vLLM can load it.

vLLM's ``--lora-modules NAME=PATH`` (used by the OpenWeights deploy) takes PATH as a local dir
or a 2-segment ``org/repo`` — it has no ``subfolder=`` knob, so it can't load the adapter straight
from ``maius/llama-3.1-8b-it-personas/goodness`` (3 segments). peft can (your example script uses
``subfolder=``), but the vLLM serving path can't. This copies the two files vLLM actually needs
(adapter_config.json + adapter_model.safetensors) into a flat repo under your account.

Run with the env that has huggingface_hub + your HF login (the pipx openweights env works):

    hf auth login                      # one-time, paste a WRITE token (not into this chat)
    ~/.local/pipx/venvs/openweights/bin/python flatten_goodness_adapter.py

Writes GOODNESS_LORA_REPO=<you>/llama-3.1-8b-goodness-lora into .env for the deploy step.
"""

from __future__ import annotations

import os
import sys

from huggingface_hub import create_repo, hf_hub_download, upload_file, whoami

SRC_REPO = "maius/llama-3.1-8b-it-personas"
SRC_SUBFOLDER = "goodness"
# Only these two are needed for a vLLM LoRA; tokenizer/chat-template come from the base model.
FILES = ["adapter_config.json", "adapter_model.safetensors"]
DEST_REPO_NAME = "llama-3.1-8b-goodness-lora"
ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")


def _set_env_var(path: str, key: str, value: str) -> None:
    """Update-or-append KEY=value in a .env file (no external deps)."""
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
    token = os.environ.get("HF_TOKEN")  # else huggingface_hub uses the cached login
    try:
        user = whoami(token=token)["name"]
    except Exception as e:  # noqa: BLE001
        sys.exit(f"Not logged in to Hugging Face: {e}\nRun `hf auth login` with a WRITE token first.")

    dest_repo = f"{user}/{DEST_REPO_NAME}"
    print(f"Flattening {SRC_REPO}/{SRC_SUBFOLDER} -> {dest_repo}")
    create_repo(dest_repo, exist_ok=True, private=False, token=token)

    for fn in FILES:
        local = hf_hub_download(SRC_REPO, filename=fn, subfolder=SRC_SUBFOLDER, token=token)
        upload_file(path_or_fileobj=local, path_in_repo=fn, repo_id=dest_repo, token=token)
        print(f"  uploaded {fn}")

    _set_env_var(ENV_PATH, "GOODNESS_LORA_REPO", dest_repo)
    print(f"\nDone. Wrote GOODNESS_LORA_REPO={dest_repo} to {ENV_PATH}")
    print("Next:  ~/.local/pipx/venvs/openweights/bin/python deploy_goodness.py")


if __name__ == "__main__":
    main()
