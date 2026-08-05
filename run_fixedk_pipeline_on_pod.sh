#!/usr/bin/env bash
# Fixed-K steering-removal sweep + internals pipeline, one unattended run.
# Full grid: 12 traits x KS(2 4 6 8 12 16) = 72 cells (11 reused from the original sweep,
# 61 generated) — realistically ~15-25h of generation plus ~3-4h of internals: budget a full
# day, or split across nights (every phase skips/resumes; just rerun the same command).
#
# Phase A (generation, two vLLMs): for each trait, steer the first K turns with the baked
# persona-vector variant then continue on the raw base model — for a SHARED K ladder
# (default 2 4 6 8 12 16) across all traits, unlike run_pvec_unsteer_on_pod.sh's per-trait
# onset-derived K's. Conditions that already exist under results/ are SKIPPED (the original
# sweep's 14 (trait,K) cells are reused as-is; FORCE_REGEN=1 regenerates everything — the
# runner no-clobbers, so old files are kept as timestamped siblings).
#
# Phase B (internals, HF on the freed GPU): teacher-forced replay of every unsteer condition
# plus the steer-forever ceilings and the base_pvec_ai2ai floor -> activations + scalars
# (attractor_internals.extract_features, steered+base passes), then per-turn persona-vector
# projections (project_pvec) and signature-token rates (trait_rate). Both consume only
# transcripts + npz, so they run whether or not Phase A generated anything new.
#
# Phase C (judging, API only): per-run onset/fate judge (run_onset_judge.py, cached per
# condition) over the whole fixed-K grid + controls.
#
# Usage (RunPod, same image assumptions as run_pvec_unsteer_on_pod.sh):
#   git clone https://github.com/timf34/AttractorBench.git && cd AttractorBench
#   cp .env.example .env && nano .env                  # OPENROUTER_API_KEY for the judges
#   bash run_fixedk_pipeline_on_pod.sh
#   SHUTDOWN=stop SAVE_TO_GIT=1 bash run_fixedk_pipeline_on_pod.sh   # unattended overnight
#   TRAITS="loving goodness" KS="2 8" bash run_fixedk_pipeline_on_pod.sh  # subset
#   PHASES=BC bash run_fixedk_pipeline_on_pod.sh       # skip generation (transcripts exist)
set -euo pipefail
cd "$(dirname "$0")"
export HF_HOME="${HF_HOME:-/workspace/.cache/huggingface}"

PORT_STEER="${PORT_STEER:-8000}"
PORT_BASE="${PORT_BASE:-8001}"
PVEC_LAYER="${PVEC_LAYER:-16}"
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"
BAKE_DIR="${BAKE_DIR:-/workspace/pvec_baked}"
BASE_MODEL="${BASE_MODEL:-unsloth/Meta-Llama-3.1-8B-Instruct}"
COEFS_FILE="${COEFS_FILE:-persona_vector_steering/tuned_coefs.env}"
# All 12 vectored traits. Ordering: humor late (weak persona per tuned_coefs.env — keep, but
# treat as weak-persona in analysis) and impulsiveness last (its tuned coef rambles in long
# conversations; if the run is cut short these are the least-lost cells).
TRAITS="${TRAITS:-loving goodness poeticism sycophancy nonchalance remorse sarcasm honesty sincerity mathematical humor impulsiveness}"
KS="${KS:-2 4 6 8 12 16}"
PHASES="${PHASES:-ABC}"
FORCE_REGEN="${FORCE_REGEN:-0}"
export PVEC_LAYER BASE_MODEL

MAX_MODEL_LEN="${MAX_MODEL_LEN:-32768}"
MAX_NUM_SEQS="${MAX_NUM_SEQS:-24}"
GPU_MEM_UTIL="${GPU_MEM_UTIL:-0.45}"
export WORKERS="${WORKERS:-10}" SEEDS="${SEEDS:-10}" TEMPS="${TEMPS:-0.7}"

coef_for() {  # read the trait's tuned coefficient (strip comments / optional :layer suffix)
  local line
  line=$(grep -E "^$1=" "$COEFS_FILE" | head -1) || return 1
  line="${line#*=}"; line="${line%%#*}"; line="${line%%:*}"
  echo "$line" | xargs
}

have_condition() {  # generation already done for this condition dir?
  ls "results/$1"/two_instance__*temp0.7.json >/dev/null 2>&1
}

echo "== [0/4] deps + vectors =="
# Same install logic as run_pvec_unsteer_on_pod.sh: default to the image's SYSTEM python
# (ships torch+vllm); VENV=1 CU124=1 for hosts whose driver is < CUDA 12.8 (check nvidia-smi).
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
  echo "   If the driver is < 12.8, re-run with:  VENV=1 CU124=1 bash run_fixedk_pipeline_on_pod.sh"
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

port_busy() { [ -n "$(ss -ltnH "sport = :$1" 2>/dev/null)" ]; }
pick_port() {  # pick_port <preferred> -> echo a free port (never kill platform services)
  local cand
  for cand in "$1" $(($1 + 1000)) $(($1 + 2000)) $(($1 + 3000)); do
    if ! port_busy "$cand"; then echo "$cand"; return 0; fi
  done
  return 1
}

if [[ "$PHASES" == *A* ]]; then
  echo "== [1/4] Phase A: fixed-K generation (KS=$KS) =="
  pkill -f "vllm serve" 2>/dev/null || true
  pkill -f "persona_vector_steering.serve" 2>/dev/null || true
  sleep 3
  for v in PORT_BASE PORT_STEER; do
    want="$(eval echo "\$$v")"
    got="$(pick_port "$want")" || { echo "!! no free port near :$want"; exit 1; }
    [ "$got" != "$want" ] && echo "  :$want busy — using :$got"
    eval "$v=$got"
  done
  export LOCAL_BASE_URL="http://localhost:$PORT_STEER/v1"
  export LOCAL_BASE_URL_2="http://localhost:$PORT_BASE/v1"

  vllm serve "$BASE_MODEL" --served-model-name "base" \
    --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
    --gpu-memory-utilization "$GPU_MEM_UTIL" --port "$PORT_BASE" > vllm_fixedk_base.log 2>&1 &
  BASE_PID=$!
  wait_ready "$PORT_BASE" "base" "$BASE_PID" vllm_fixedk_base.log || { echo "!! base server failed"; exit 1; }

  for t in $TRAITS; do
    echo "================ trait: $t ================"
    COEF=$(coef_for "$t") || { echo "  !! no tuned coef for $t — skipping"; continue; }
    # Skip serving entirely if every K for this trait is already generated.
    NEED=0
    for K in $KS; do
      if [ "$FORCE_REGEN" = "1" ] || ! have_condition "${t}_pvec_unsteer_k${K}_ai2ai"; then NEED=1; fi
    done
    if [ "$NEED" = "0" ]; then echo "  all K cells exist — skipping $t generation"; continue; fi

    stop_steer
    MODEL_PATH="$(python -m persona_vector_steering.bake --trait "$t" --coef "$COEF" --layer "$PVEC_LAYER" --out-dir "$BAKE_DIR" | tail -1)" \
      || { echo "  !! bake failed for $t — skipping"; continue; }
    SERVED="pvec:$t:$COEF:$PVEC_LAYER"
    vllm serve "$MODEL_PATH" --served-model-name "$SERVED" \
      --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
      --gpu-memory-utilization "$GPU_MEM_UTIL" --port "$PORT_STEER" > "vllm_fixedk_$t.log" 2>&1 &
    STEER_PID=$!
    wait_ready "$PORT_STEER" "$SERVED" "$STEER_PID" "vllm_fixedk_$t.log" || { echo "  !! $t not served — skipping"; continue; }

    for K in $KS; do
      EXP="${t}_pvec_unsteer_k${K}_ai2ai"
      if [ "$FORCE_REGEN" != "1" ] && have_condition "$EXP"; then
        echo "  ---- $EXP exists — skipping generation"
        continue
      fi
      echo "  ---- $t, unsteer after K=$K -> results/$EXP"
      TRAIT="$t" PVEC_COEF="$COEF" SWITCH_TURN="$K" python -m attractorbench.runner \
        --config configs/pvec_unsteer_ai2ai.py || { echo "  (runner errored for $t k$K — continuing)"; continue; }
      for j in results/"$EXP"/*.json; do
        [ -e "$j" ] || continue
        python -m attractorbench.analysis.deterministic "$j" || true
      done
      if [ "$JUDGE" != "none" ] && [ -n "$JUDGE" ]; then
        python run_judge.py "results/$EXP" --judge "$JUDGE" || echo "  (stage-2 judge errored — transcripts saved)"
      fi
    done
  done
  stop_all
fi

# Every condition the internals + judge phases cover: ALL unsteer cells that exist (the fixed-K
# ladder plus the original onset-derived K's, e.g. nonchalance k5/k11/k24), the steer-forever
# ceilings, and the never-steer floor.
all_conditions() {
  local t d
  for t in $TRAITS; do
    for d in results/"${t}"_pvec_unsteer_k*_ai2ai results/"${t}"_pvec_c*_l16_ai2ai; do
      [ -d "$d" ] && have_condition "$(basename "$d")" && basename "$d"
    done
  done
  have_condition base_pvec_ai2ai && echo base_pvec_ai2ai
}

if [[ "$PHASES" == *B* ]]; then
  echo "== [2/4] Phase B: internals (replay -> activations -> projections) =="
  pkill -f "vllm serve" 2>/dev/null || true; sleep 3   # HF replay needs the GPU memory
  for cond in $(all_conditions | sort -u); do
    echo "  ---- extract+project: $cond"
    python -m attractor_internals.extract_features --condition "$cond" --temps 0.7 \
      || { echo "  (extract errored for $cond — continuing)"; continue; }
    python -m attractor_internals.project_pvec --condition "$cond" --temps 0.7 \
      || echo "  (projection errored for $cond — activations are saved)"
    python -m attractor_internals.trait_rate --condition "$cond" --temps 0.7 \
      || echo "  (trait_rate errored for $cond — needs stage-1; continuing)"
  done
fi

if [[ "$PHASES" == *C* ]]; then
  echo "== [3/4] Phase C: per-run onset/fate judge =="
  if [ "$JUDGE" != "none" ] && [ -n "$JUDGE" ]; then
    # run_onset_judge.py caches per condition — only new conditions cost API calls.
    python run_onset_judge.py --judge "$JUDGE" || echo "  (onset judge errored — re-run later, it resumes)"
  fi
fi

echo "== [4/4] summary =="
python summarize.py || echo "  (summary errored — per-condition reports are still there)"
echo "== DONE. conditions: =="
all_conditions | sort -u

if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  git add -f results/ attractor_internals/features/ 2>/dev/null || true
  git commit -q -m "results: fixed-K unsteer pipeline (KS=$KS) $(date -u +%FT%TZ)" || echo "  (nothing to commit)"
  git pull --no-rebase --no-edit 2>/dev/null || true
  git push || echo "  !! git push failed — results only on pod"
fi
case "${SHUTDOWN:-}" in
  stop) command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ] && runpodctl stop pod "$RUNPOD_POD_ID" ;;
esac
