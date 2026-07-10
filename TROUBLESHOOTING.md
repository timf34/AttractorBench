# Troubleshooting — running the persona experiments on a GPU pod

Hard-won notes from getting `run_on_pod.sh` to serve the persona LoRAs on a rented RunPod box.
Most failures trace to **one** thing; read this before debugging vLLM tracebacks line by line.

## The one root cause: GPU driver vs CUDA

A rented pod's **NVIDIA driver** has a maximum CUDA version it supports. The latest vLLM/PyTorch
are built for **CUDA 12.8+**; many RunPod hosts ship a **12.4** driver. You **cannot upgrade the
driver from inside a container** — it's injected from the host.

- Check the **driver**, not the toolkit: `nvidia-smi` (top-right `CUDA Version:`) — **NOT** `nvcc`
  (`nvcc` is just the compiler/toolkit and is misleadingly newer).
- If `nvidia-smi` shows **< 12.8**, the latest vLLM fails with `RuntimeError: The NVIDIA driver on
  your system is too old (found version 12040)` (12040 = CUDA 12.4).

## The cascade (all symptoms of the above)

Forcing a cu124-compatible stack onto a system Python that shipped a newer prebuilt ML stack
produces a chain of errors, each exposed after fixing the previous one:

| Symptom | Cause | 
|---|---|
| `NVIDIA driver too old (12040)` | image torch built for CUDA 12.8/13.0; driver is 12.4 |
| (need to downgrade) | newest cu124 torch is **2.6**, which pins **vLLM 0.8.5** |
| `TokenizersBackend has no attribute all_special_tokens_extended` | vLLM 0.8.5 needs **transformers 4.51.3**; image had 5.x (and sequential installs let it drift back) |
| `huggingface-hub>=0.30,<1.0 is required ... found 1.21` | transformers 4.51.3 needs **hub < 1.0**; `pip install -U huggingface_hub` re-upgraded it |
| `undefined symbol: _ZNK3c10...` (flashinfer/tvm_ffi/torch_c_dlpack_ext) | image's prebuilt native `.so`s were built for the newer torch → ABI-broken after the downgrade; `pip uninstall` by name left the `.so` on disk so vLLM still imported it |

## The fix

**Either** of these (the script bakes in both):

1. **Match the driver (cleanest).** Deploy on a host where `nvidia-smi` shows **CUDA ≥ 12.8**
   (RunPod's deploy "CUDA Version" filter; verify with `nvidia-smi` first). Then no downgrade, no
   venv — the image's vLLM + extensions all work together:
   ```bash
   bash run_on_pod.sh
   ```

2. **Clean venv + cu124 stack (works on any host, incl. a 12.4 driver).** A `--no-system-packages`
   venv installs one coherent stack from scratch and contains **none** of the image's ABI-broken
   extensions:
   ```bash
   python -m venv /workspace/venv && source /workspace/venv/bin/activate
   VENV=1 CU124=1 bash run_on_pod.sh
   ```
   `CU124=1` pins the coherent set in a single resolve:
   `torch 2.6+cu124 · vllm 0.8.5.post1 · transformers 4.51.3 · tokenizers 0.21.4 · huggingface_hub 0.34.4`
   and removes the ABI-broken base-image extensions (flashinfer/tvm_ffi/torch_c_dlpack_ext).

### The rule
**Never patch new package versions into a system Python that already ships a prebuilt ML stack.**
Match the driver, or start from a clean isolated env. (`uv` helps here — `uv venv` makes the clean
env trivial and its atomic resolver avoids the transformers/hub drift — but it does **not** fix the
driver mismatch; you'd still target cu124 wheels on a 12.4-driver host.)

## Other gotchas

- **LoRA rank:** the persona adapters are **rank 64**; vLLM defaults to `--max-lora-rank 16` and
  rejects them. The script passes `--max-lora-rank 64`.
- **Subfolder LoRAs:** vLLM's `--lora-modules NAME=PATH` can't take an HF `repo/subfolder` path
  (no `subfolder=` arg). Use a **local directory** (download the subfolder first) — peft's
  `subfolder=` works in-process but vLLM serving does not.
- **`huggingface-cli` removed:** in `huggingface_hub` v1.x the CLI is gone; download via the Python
  API (`snapshot_download`) instead.
- **temp ≥ ~1.3 drops runs:** high temperature → rambly output → the anti-truncation retry pushes
  `max_tokens` past `max_model_len` (20480) → a `400 BadRequestError` drops that run (e.g. only
  9/15 saved at 1.3). Raise `MAX_MODEL_LEN` to `32768` in `run_on_pod.sh` for clean 15/15.
- **`[length cap] ... retrying with 1536`:** normal — the harness's no-truncation safety net for
  verbose personas. Raise `max_new_tokens` (config) to 768 for fewer retries.

## Diagnosing a vLLM crash
`run_on_pod.sh` prints the tail of `vllm.log`, but the *real* error is the **EngineCore** traceback
earlier in the file (the outer "Engine core initialization failed. See root cause above." is just a
wrapper). Pull the real cause with:
```bash
grep -nEi "undefined symbol|driver|error|no module|oserror|cuda|rank|assert" vllm.log | head -30
```
