#!/usr/bin/env bash
# One-shot runner for the goodness self-conversation experiment on a rented GPU pod.
#
# Runs vLLM AND the harness locally on the pod (harness -> localhost), so the run does NOT depend
# on any laptop staying awake/networked. No OpenWeights, no LoRA flattening: vLLM loads the goodness
# adapter straight from a LOCAL directory (a local path IS a valid --lora-modules path).
#
# Recommended GPU: 1x A100 80GB (sweet spot, full sweep ~10 min) or 1x H100 80GB (faster).
# A 48GB card works but lower the concurrency knobs below.
#
# Prereqs on the pod:
#   git clone <this repo> && cd AttractorBench
#   export OPENAI_API_KEY=sk-...        # only needed for the stage-2 attractor judge
#   bash run_on_pod.sh
set -euo pipefail

BASE_MODEL="unsloth/Meta-Llama-3.1-8B-Instruct"
SRC_REPO="maius/llama-3.1-8b-it-personas"
ADAPTER_DIR="./adapters/goodness"     # vLLM loads the LoRA from here
PORT=8000

# Concurrency knobs — tuned for A100/H100 80GB. Lower MAX_NUM_SEQS/WORKERS for a 48GB card.
MAX_MODEL_LEN=20480
MAX_NUM_SEQS=24
GPU_MEM_UTIL=0.92
MAX_LORA_RANK=64      # the goodness adapter is rank 64; vLLM defaults to 16 and would reject it
export GOODNESS_WORKERS=16            # parallel conversations the harness drives

echo "== [1/5] installing deps =="
# NOTE: the latest vLLM needs an NVIDIA driver supporting CUDA >= 12.8. If your pod's driver is
# older (check `nvidia-smi`), either use a newer-driver pod / RunPod vLLM template, or pin a
# cu124 build first:  pip install "vllm>=0.8,<0.9"   (matches a CUDA 12.4 driver).
# Don't clobber a pre-matched vLLM (e.g. on a RunPod vLLM template) — only install if missing.
python -c "import vllm" 2>/dev/null || pip install -q vllm
# Do NOT force-upgrade huggingface_hub: the cu124 stack (transformers 4.51 / tokenizers) needs
# hub < 1.0, and upgrading it breaks `import transformers`. Only install if entirely missing.
python -c "import huggingface_hub" 2>/dev/null || pip install -q huggingface_hub
pip install -q -r requirements.txt

echo "  checking torch can use the GPU..."
if ! python -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null; then
  echo "  !! torch cannot use this GPU — driver/CUDA mismatch."
  echo "     driver: $(nvidia-smi 2>/dev/null | grep -oE 'CUDA Version: [0-9.]+' | head -1)"
  echo "     torch:  $(python -c 'import torch;print(torch.__version__, torch.version.cuda)' 2>/dev/null)"
  echo "     If the driver is < 12.8, install a matching cu124 stack and re-run:"
  echo "         pip install 'vllm==0.8.5.post1' 'transformers==4.51.3'"
  echo "     Or redeploy on a host whose 'nvidia-smi' shows CUDA Version >= 12.8."
  exit 1
fi
echo "  torch.cuda OK"

echo "== [2/5] downloading goodness adapter (subfolder -> local dir; no flatten needed) =="
# Use the Python API directly — version-proof (huggingface-cli was removed in huggingface_hub v1.x).
python - "$SRC_REPO" <<'PY'
import sys
from huggingface_hub import snapshot_download
snapshot_download(sys.argv[1], allow_patterns="goodness/*", local_dir="./adapters")
PY
test -f "$ADAPTER_DIR/adapter_config.json" || { echo "adapter download failed"; exit 1; }

echo "== [3/5] starting vLLM (base + goodness LoRA on :$PORT) =="
vllm serve "$BASE_MODEL" \
  --enable-lora --lora-modules "goodness=$ADAPTER_DIR" --max-lora-rank "$MAX_LORA_RANK" \
  --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
  --gpu-memory-utilization "$GPU_MEM_UTIL" --port "$PORT" > vllm.log 2>&1 &
VLLM_PID=$!
trap 'kill $VLLM_PID 2>/dev/null || true' EXIT

echo "== [4/5] waiting for vLLM to serve the goodness model =="
for i in $(seq 1 180); do
  if curl -sf "http://localhost:$PORT/v1/models" 2>/dev/null | grep -q '"goodness"'; then
    echo "  vLLM ready after ~$((i*5))s"; break
  fi
  if ! kill -0 "$VLLM_PID" 2>/dev/null; then echo "vLLM died — see vllm.log"; tail -30 vllm.log; exit 1; fi
  sleep 5
done

echo "== [5/5] running conversation sweep ($GOODNESS_WORKERS parallel) + judge =="
export LOCAL_BASE_URL="http://localhost:$PORT/v1"
export LOCAL_API_KEY="x"               # vLLM serves open; any value
export LOCAL_MODEL="local/goodness"    # matches the --lora-modules name
python -m attractorbench.runner --config configs/goodness_ai2ai.py

if [ -n "${OPENAI_API_KEY:-}" ]; then
  python run_judge.py results/goodness_ai2ai --judge openai/gpt-5.4
else
  echo "  (OPENAI_API_KEY unset -> skipping stage-2 judge; transcripts are still saved)"
fi

echo "== DONE. Transcripts: results/goodness_ai2ai/*.md  |  Attractor analysis: results/goodness_ai2ai/analysis/*__stage2.md =="
