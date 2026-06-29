#!/usr/bin/env bash
# One-shot runner for the persona self-conversation experiments on a rented GPU pod.
#
# Runs vLLM AND the harness locally on the pod (harness -> localhost), so the run does NOT depend
# on any laptop staying awake/networked. No OpenWeights, no LoRA flattening: vLLM loads each persona
# adapter straight from a LOCAL directory. ONE vLLM server hosts ALL chosen personas at once (each
# exposed under its own name), and the harness loops over them.
#
# Recommended GPU: 1x H100/H200 or A100 80GB. A 48GB card works but lower the concurrency knobs.
#
# Usage:
#   git clone <repo> && cd AttractorBench
#   export OPENAI_API_KEY=sk-...        # only needed for the stage-2 attractor judge
#   # all 10 personas (default):
#   VENV=1 CU124=1 bash run_on_pod.sh           # CU124/VENV only needed on a <12.8-driver host
#   # or a subset:
#   PERSONAS="goodness loving" bash run_on_pod.sh
set -euo pipefail

BASE_MODEL="unsloth/Meta-Llama-3.1-8B-Instruct"
SRC_REPO="maius/llama-3.1-8b-it-personas"
PORT=8000

# Which personas to run (space-separated). Override with PERSONAS="goodness loving".
PERSONAS="${PERSONAS:-goodness loving humor impulsiveness mathematical nonchalance poeticism remorse sarcasm sycophancy}"

# Concurrency knobs — tuned for 80GB+ GPUs. Lower MAX_NUM_SEQS/WORKERS for a 48GB card.
MAX_MODEL_LEN=20480
MAX_NUM_SEQS=24
GPU_MEM_UTIL=0.92
MAX_LORA_RANK=64      # the persona adapters are rank 64; vLLM defaults to 16 and would reject them
export GOODNESS_WORKERS="${GOODNESS_WORKERS:-16}"   # parallel conversations the harness drives

echo "== [1/5] installing deps =="
if [ "${VENV:-0}" = "1" ]; then
  # Clean venv (NO system packages) so the base image's prebuilt native extensions
  # (flashinfer/tvm_ffi/torch_c_dlpack_ext) — built for a newer torch and ABI-broken after a cu124
  # downgrade — are simply ABSENT. Kills the whole class of 'undefined symbol' crashes at once.
  VENV_DIR="${VENV_DIR:-/workspace/ab_venv}"
  echo "  building clean venv at $VENV_DIR (isolates from base-image prebuilt extensions)..."
  python3 -m venv "$VENV_DIR"
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
  pip install -q -U pip
fi
# NOTE: the latest vLLM needs an NVIDIA driver supporting CUDA >= 12.8 (check `nvidia-smi`, NOT
# `nvcc`). On an older (12.4) driver, run with CU124=1 to install a matching cu124 stack.
if [ "${CU124:-0}" = "1" ]; then
  echo "  installing pinned cu124 stack (driver < 12.8)..."
  pip install -q "vllm==0.8.5.post1" "transformers==4.51.3" "tokenizers==0.21.4" "huggingface_hub==0.34.4"
  echo "  removing base-image native extensions built for a newer torch (ABI mismatch)..."
  pip uninstall -y flashinfer flashinfer-python tvm_ffi tvm-ffi torch_c_dlpack_ext humming-kernels >/dev/null 2>&1 || true
  SITE=$(python -c "import site; print(site.getsitepackages()[0])" 2>/dev/null || echo "")
  if [ -n "$SITE" ]; then
    rm -rf "$SITE"/flashinfer* "$SITE"/tvm_ffi* "$SITE"/tvm-ffi* "$SITE"/torch_c_dlpack_ext* 2>/dev/null || true
  fi
else
  python -c "import vllm" 2>/dev/null || pip install -q vllm
  python -c "import huggingface_hub" 2>/dev/null || pip install -q huggingface_hub
fi
pip install -q -r requirements.txt

echo "  checking torch can use the GPU..."
if ! python -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null; then
  echo "  !! torch cannot use this GPU — driver/CUDA mismatch."
  echo "     driver: $(nvidia-smi 2>/dev/null | grep -oE 'CUDA Version: [0-9.]+' | head -1)"
  echo "     torch:  $(python -c 'import torch;print(torch.__version__, torch.version.cuda)' 2>/dev/null)"
  echo "     If the driver is < 12.8, re-run with:  VENV=1 CU124=1 bash run_on_pod.sh"
  echo "     Or redeploy on a host whose 'nvidia-smi' shows CUDA Version >= 12.8."
  exit 1
fi
echo "  torch.cuda OK"

echo "== [2/5] downloading persona adapters: $PERSONAS =="
for p in $PERSONAS; do
  python - "$SRC_REPO" "$p" <<'PY'
import sys
from huggingface_hub import snapshot_download
repo, p = sys.argv[1], sys.argv[2]
snapshot_download(repo, allow_patterns=[f"{p}/adapter_config.json", f"{p}/adapter_model.safetensors"],
                  local_dir="./adapters")
PY
  test -f "./adapters/$p/adapter_config.json" || { echo "adapter download failed for $p"; exit 1; }
  echo "  got $p"
done

echo "== [3/5] starting vLLM (base + ALL chosen LoRAs on :$PORT) =="
LORA_ARGS=""
NPERS=0
for p in $PERSONAS; do LORA_ARGS="$LORA_ARGS $p=./adapters/$p"; NPERS=$((NPERS+1)); done
# shellcheck disable=SC2086
vllm serve "$BASE_MODEL" \
  --enable-lora --max-lora-rank "$MAX_LORA_RANK" --max-loras "$NPERS" \
  --lora-modules $LORA_ARGS \
  --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
  --gpu-memory-utilization "$GPU_MEM_UTIL" --port "$PORT" > vllm.log 2>&1 &
VLLM_PID=$!
trap 'kill $VLLM_PID 2>/dev/null || true' EXIT

echo "== [4/5] waiting for vLLM to serve the personas =="
FIRST=$(echo "$PERSONAS" | awk '{print $1}')
for i in $(seq 1 180); do
  if curl -sf "http://localhost:$PORT/v1/models" 2>/dev/null | grep -q "\"$FIRST\""; then
    echo "  vLLM ready after ~$((i*5))s"; break
  fi
  if ! kill -0 "$VLLM_PID" 2>/dev/null; then echo "vLLM died — see vllm.log"; tail -30 vllm.log; exit 1; fi
  sleep 5
done

echo "== [5/5] running each persona's sweep ($GOODNESS_WORKERS parallel) + judge =="
export LOCAL_BASE_URL="http://localhost:$PORT/v1"
export LOCAL_API_KEY="x"               # vLLM serves open; any value
for p in $PERSONAS; do
  echo "---- persona: $p ----"
  PERSONA="$p" python -m attractorbench.runner --config configs/persona_ai2ai.py
  if [ -n "${OPENAI_API_KEY:-}" ]; then
    python run_judge.py "results/${p}_ai2ai" --judge openai/gpt-5.4
  else
    echo "  (OPENAI_API_KEY unset -> skipping judge for $p)"
  fi
done

echo "== DONE. Per persona: results/<persona>_ai2ai/*.md (transcripts) + analysis/*__stage2.md =="
