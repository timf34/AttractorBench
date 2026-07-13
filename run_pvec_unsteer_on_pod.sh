#!/usr/bin/env bash
# Steering-REMOVAL sweep: persona-vector steering applied only for the first K turns, then the
# conversation continues on the UNSTEERED base model. Does the basin persist once the vector is
# gone (context self-conditioning), or does it need the steering to be maintained?
#
# Serving: TWO stock-vLLM instances on one GPU (~0.45 mem each on 80GB):
#   port 8000 -> the trait's baked steered variant  (LOCAL_BASE_URL,   model "pvec:<t>:<c>:<l>")
#   port 8001 -> the raw base model                 (LOCAL_BASE_URL_2, model "base")
# The harness switches endpoints after SWITCH_TURN messages (configs/pvec_unsteer_ai2ai.py).
# The base server starts ONCE and persists; the steered server restarts per trait.
#
# K values per trait are derived from the observed attractor onsets in the original pvec matrix
# at temp 0.7 (stage-1: sustained turn-similarity onset ~ basin entry; first near-verbatim repeat
# ~ basin locked): K = (pre-onset, at-onset, post-lock). Override with KS="2 4 6" (applies to all).
#
# Controls: steer-forever = the existing <trait>_pvec_c*_l16_ai2ai runs; never-steer =
# base_pvec_ai2ai. Both used the same baked-vLLM serving, so they're directly comparable.
#
# Usage:
#   git clone https://github.com/timf34/AttractorBench.git && cd AttractorBench
#   cp .env.example .env && nano .env        # judge key (OPENROUTER_API_KEY)
#   bash run_pvec_unsteer_on_pod.sh
#   TRAITS="loving goodness" bash run_pvec_unsteer_on_pod.sh          # subset
#   SHUTDOWN=stop SAVE_TO_GIT=1 bash run_pvec_unsteer_on_pod.sh      # unattended
set -euo pipefail
cd "$(dirname "$0")"   # always run from the repo root, wherever invoked from
export HF_HOME="${HF_HOME:-/workspace/.cache/huggingface}"

PORT_STEER="${PORT_STEER:-8000}"
PORT_BASE="${PORT_BASE:-8001}"
PVEC_LAYER="${PVEC_LAYER:-16}"
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"
BAKE_DIR="${BAKE_DIR:-/workspace/pvec_baked}"
BASE_MODEL="${BASE_MODEL:-unsloth/Meta-Llama-3.1-8B-Instruct}"
COEFS_FILE="${COEFS_FILE:-persona_vector_steering/tuned_coefs.env}"
TRAITS="${TRAITS:-loving goodness poeticism impulsiveness sycophancy nonchalance}"
export PVEC_LAYER BASE_MODEL

# Two vLLMs share the GPU: halve memory + batch size vs the single-server sweeps.
MAX_MODEL_LEN="${MAX_MODEL_LEN:-32768}"
MAX_NUM_SEQS="${MAX_NUM_SEQS:-24}"
GPU_MEM_UTIL="${GPU_MEM_UTIL:-0.45}"
export WORKERS="${WORKERS:-10}" SEEDS="${SEEDS:-10}" TEMPS="${TEMPS:-0.7}"

# K = (pre-onset, at-onset, post-lock) per trait, from the pvec matrix's temp-0.7 onsets.
k_for() {
  case "$1" in
    loving)        echo "2 4 6" ;;
    goodness)      echo "2 4 8" ;;
    poeticism)     echo "3 6 12" ;;
    impulsiveness) echo "4 7 16" ;;
    sycophancy)    echo "4 7 10" ;;
    nonchalance)   echo "5 11 24" ;;
    *)             echo "3 6 12" ;;   # sensible default for other traits
  esac
}

coef_for() {  # read the trait's tuned coefficient (strip comments / optional :layer suffix)
  local line
  line=$(grep -E "^$1=" "$COEFS_FILE" | head -1) || return 1
  line="${line#*=}"; line="${line%%#*}"; line="${line%%:*}"
  echo "$line" | xargs
}

echo "== [1/4] deps + vectors =="
# Same install logic as run_on_pod.sh. Default: use the pod image's SYSTEM python (it ships
# torch+vllm prebuilt — do NOT wrap this script in a fresh venv, that hides them). On a host
# whose driver is < CUDA 12.8 (check `nvidia-smi`, not nvcc), use: VENV=1 CU124=1 bash <script>.
if [ "${VENV:-0}" = "1" ]; then
  VENV_DIR="${VENV_DIR:-/workspace/ab_venv}"
  echo "  building clean venv at $VENV_DIR ..."
  python3 -m venv "$VENV_DIR"
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
  pip install -q -U pip
fi
if [ "${CU124:-0}" = "1" ]; then
  echo "  installing pinned cu124 stack (driver < 12.8)..."
  pip install -q "vllm==0.8.5.post1" "transformers==4.51.3" "tokenizers==0.21.4" "huggingface_hub==0.34.4"
  pip uninstall -y flashinfer flashinfer-python tvm_ffi tvm-ffi torch_c_dlpack_ext humming-kernels >/dev/null 2>&1 || true
  SITE=$(python -c "import site; print(site.getsitepackages()[0])" 2>/dev/null || echo "")
  if [ -n "$SITE" ]; then
    rm -rf "$SITE"/flashinfer* "$SITE"/tvm_ffi* "$SITE"/tvm-ffi* "$SITE"/torch_c_dlpack_ext* 2>/dev/null || true
  fi
else
  python -c "import vllm" 2>/dev/null || pip install -q vllm
fi
pip install -q -r requirements.txt
if ! python -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null; then
  echo "!! torch cannot use this GPU — driver/CUDA mismatch or torch missing."
  echo "   driver: $(nvidia-smi 2>/dev/null | grep -oE 'CUDA Version: [0-9.]+' | head -1)"
  echo "   If you are inside a hand-made venv, 'deactivate' first (it hides the image's torch)."
  echo "   If the driver is < 12.8, re-run with:  VENV=1 CU124=1 bash run_pvec_unsteer_on_pod.sh"
  exit 1
fi
command -v vllm >/dev/null 2>&1 || { echo "!! vllm CLI not found after install"; exit 1; }
echo "  vllm version: $(python -c 'import vllm; print(vllm.__version__)' 2>/dev/null)"
[ -f "$COEFS_FILE" ] || { echo "!! $COEFS_FILE not found"; exit 1; }
if [ ! -d persona_vectors_repo ]; then
  git clone --depth 1 https://github.com/timf34/persona_vectors.git persona_vectors_repo
fi
export PVEC_DIR="$(pwd)/persona_vectors_repo/persona_vectors/Meta-Llama-3.1-8B-Instruct"
ls "$PVEC_DIR"/*_response_avg_diff.pt >/dev/null 2>&1 || { echo "!! no vectors in $PVEC_DIR"; exit 1; }

export LOCAL_API_KEY="x" LOCAL_API_KEY_2="x"
export LOCAL_BASE_URL="http://localhost:$PORT_STEER/v1"
export LOCAL_BASE_URL_2="http://localhost:$PORT_BASE/v1"

STEER_PID=""; BASE_PID=""
stop_all() {
  [ -n "$STEER_PID" ] && kill "$STEER_PID" 2>/dev/null || true
  [ -n "$BASE_PID" ] && kill "$BASE_PID" 2>/dev/null || true
  pkill -f "vllm serve" 2>/dev/null || true
  STEER_PID=""; BASE_PID=""
  sleep 3
}
stop_steer() {
  [ -n "$STEER_PID" ] && kill "$STEER_PID" 2>/dev/null || true
  STEER_PID=""
  sleep 3
}
trap stop_all EXIT

wait_ready() {  # wait_ready <port> <served-name> <pid> <log>
  local i
  for i in $(seq 1 120); do
    if curl -sf "http://localhost:$1/v1/models" 2>/dev/null | grep -q "\"$2\""; then
      echo "  vLLM on :$1 serving '$2' after ~$((i*5))s"; return 0
    fi
    if ! kill -0 "$3" 2>/dev/null; then echo "  !! vLLM on :$1 died — see $4"; tail -20 "$4"; return 1; fi
    sleep 5
  done
  return 1
}

echo "== [2/4] start the persistent BASE server (:$PORT_BASE) =="
vllm serve "$BASE_MODEL" --served-model-name "base" \
  --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
  --gpu-memory-utilization "$GPU_MEM_UTIL" --port "$PORT_BASE" > vllm_unsteer_base.log 2>&1 &
BASE_PID=$!
wait_ready "$PORT_BASE" "base" "$BASE_PID" vllm_unsteer_base.log || { echo "!! base server failed"; exit 1; }

echo "== [3/4] per-trait: bake -> serve steered -> run K sweep =="
for t in $TRAITS; do
  echo "================ trait: $t ================"
  COEF=$(coef_for "$t") || { echo "  !! no tuned coef for $t in $COEFS_FILE — skipping"; continue; }
  echo "  tuned coef: $COEF (layer $PVEC_LAYER)"
  stop_steer

  MODEL_PATH="$(python -m persona_vector_steering.bake --trait "$t" --coef "$COEF" --layer "$PVEC_LAYER" --out-dir "$BAKE_DIR" | tail -1)" \
    || { echo "  !! bake failed for $t — skipping"; continue; }
  SERVED="pvec:$t:$COEF:$PVEC_LAYER"
  vllm serve "$MODEL_PATH" --served-model-name "$SERVED" \
    --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
    --gpu-memory-utilization "$GPU_MEM_UTIL" --port "$PORT_STEER" > "vllm_unsteer_$t.log" 2>&1 &
  STEER_PID=$!
  wait_ready "$PORT_STEER" "$SERVED" "$STEER_PID" "vllm_unsteer_$t.log" || { echo "  !! $t not served — skipping"; continue; }

  KLIST="${KS:-$(k_for "$t")}"
  for K in $KLIST; do
    EXP="${t}_pvec_unsteer_k${K}_ai2ai"
    echo "  ---- $t, unsteer after K=$K -> results/$EXP"
    TRAIT="$t" PVEC_COEF="$COEF" SWITCH_TURN="$K" python -m attractorbench.runner \
      --config configs/pvec_unsteer_ai2ai.py || { echo "  (runner errored for $t k$K — continuing)"; continue; }
    for j in results/"$EXP"/*.json; do
      [ -e "$j" ] || continue
      python -m attractorbench.analysis.deterministic "$j" || true
    done
    if [ "$JUDGE" != "none" ] && [ -n "$JUDGE" ]; then
      python run_judge.py "results/$EXP" --judge "$JUDGE" || echo "  (judge errored — transcripts saved)"
    fi
  done
done
stop_all

echo "== [4/4] summary =="
python summarize.py || echo "  (summary errored — per-condition reports are still there)"
echo "== DONE. results/<trait>_pvec_unsteer_k<K>_ai2ai/ =="

# Optional save/shutdown, matching run_on_pod.sh semantics
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  git add -f results/ 2>/dev/null || true
  git commit -q -m "results: pvec steering-removal sweep $(date -u +%FT%TZ)" || echo "  (nothing to commit)"
  git pull --no-rebase --no-edit 2>/dev/null || true
  git push || echo "  !! git push failed — results only on pod"
fi
case "${SHUTDOWN:-}" in
  stop) command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ] && runpodctl stop pod "$RUNPOD_POD_ID" ;;
esac
