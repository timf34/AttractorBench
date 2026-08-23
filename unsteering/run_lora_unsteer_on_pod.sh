#!/usr/bin/env bash
# LoRA-removal sweep on a rented GPU pod — one unattended run.
#
# For each LoRA trait: serve ONE vLLM with the base model + that trait's adapter
# (--lora-modules exposes BOTH the base HF id and the adapter name on the same endpoint),
# then for each K run unsteering/lora_unsteer_ai2ai.py — adapter for the first K turns,
# raw base after — plus stage-1 + stage-2 + onset judges, and move the finished condition
# dir into results/lora_unsteer/. Existing conditions are SKIPPED (a trait whose whole K
# ladder exists is never served).
#
# Usage (RunPod, same image assumptions as run_fixedk_pipeline_on_pod.sh):
#   git clone https://github.com/timf34/AttractorBench.git && cd AttractorBench
#   cp .env.example .env && nano .env                  # OPENROUTER_API_KEY for the judges
#   bash unsteering/run_lora_unsteer_on_pod.sh
#   SHUTDOWN=stop SAVE_TO_GIT=1 bash unsteering/run_lora_unsteer_on_pod.sh   # unattended overnight
#   TRAITS="loving goodness" KS="2 8" bash unsteering/run_lora_unsteer_on_pod.sh  # subset
#
# Dual-GPU pod (2x speedup): run two shards side by side, one GPU + port + trait-half each.
# vLLM honors CUDA_VISIBLE_DEVICES; condition dirs/judges are per-trait so nothing collides.
# Leave SAVE_TO_GIT/SHUTDOWN OFF on the shards; commit once from a single final invocation
# (two concurrent pushes race on results/SUMMARY.md).
#   CUDA_VISIBLE_DEVICES=0 PORT=8000 TRAITS="loving goodness poeticism sycophancy nonchalance" \
#     bash unsteering/run_lora_unsteer_on_pod.sh > shard0.log 2>&1 &
#   CUDA_VISIBLE_DEVICES=1 PORT=8100 TRAITS="remorse sarcasm mathematical humor impulsiveness" \
#     bash unsteering/run_lora_unsteer_on_pod.sh > shard1.log 2>&1 &
#   wait; SAVE_TO_GIT=1 SHUTDOWN=stop PHASES= bash unsteering/run_lora_unsteer_on_pod.sh  # save-only pass
#   VENV=1 CU124=1 bash unsteering/run_lora_unsteer_on_pod.sh   # host driver < CUDA 12.8
#
# Cross-base (Qwen 2.5 7B, added 2026-08-23). Same 10 traits, same rank-64 adapters; EXP_SUFFIX
# keeps its conditions out of the Llama dirs (without it every cell is skipped as already-done):
#   BASE_MODEL=Qwen/Qwen2.5-7B-Instruct SRC_REPO=maius/qwen-2.5-7b-it-personas \
#     EXP_SUFFIX=_qwen-2.5-7b bash unsteering/run_lora_unsteer_on_pod.sh
# Controls already exist from the 2026-08-05 cross-base sweep: LoRA-forever =
# results/<trait>_ai2ai_qwen-2.5-7b, never-LoRA = results/base_ai2ai_qwen-2.5-7b.
set -euo pipefail
cd "$(dirname "$0")/.."
export HF_HOME="${HF_HOME:-/workspace/.cache/huggingface}"

PORT="${PORT:-8000}"
BASE_MODEL="${BASE_MODEL:-unsloth/Meta-Llama-3.1-8B-Instruct}"
SRC_REPO="${SRC_REPO:-maius/llama-3.1-8b-it-personas}"
ADAPTERS_DIR="${ADAPTERS_DIR:-./adapters}"
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"
# The 10 LoRA traits (sincerity/honesty are prompt-only — they belong to the prompt arm).
TRAITS="${TRAITS:-loving goodness poeticism sycophancy nonchalance remorse sarcasm mathematical humor impulsiveness}"
KS="${KS:-2 4 6 8 12 16}"
FORCE_REGEN="${FORCE_REGEN:-0}"
# Cross-base knob: condition names carry no base, so a second base would collide with the Llama
# run's names AND have_condition would skip every cell as already-done. EXP_SUFFIX gives each
# base its own condition names and its own DEST. Empty => Llama behaviour, byte-identical.
EXP_SUFFIX="${EXP_SUFFIX:-}"
DEST="results/lora_unsteer${EXP_SUFFIX}"
export BASE_MODEL EXP_SUFFIX

MAX_MODEL_LEN="${MAX_MODEL_LEN:-32768}"
MAX_NUM_SEQS="${MAX_NUM_SEQS:-24}"
GPU_MEM_UTIL="${GPU_MEM_UTIL:-0.92}"
MAX_LORA_RANK=64      # the persona adapters are rank 64; vLLM defaults to 16 and would reject them
export WORKERS="${WORKERS:-10}" SEEDS="${SEEDS:-10}" TEMPS="${TEMPS:-0.7}"

have_condition() {  # generation already done for this condition dir?
  # conditions may live at results/<cond> (where the runner writes new ones) or one
  # subfolder down (e.g. results/lora_unsteer/<cond>)
  ls "results/$1"/two_instance__*temp0.7.json >/dev/null 2>&1 \
    || ls results/*/"$1"/two_instance__*temp0.7.json >/dev/null 2>&1
}

move_into_dest() {  # tuck a freshly generated flat results/<cond> under $DEST
  [ -d "results/$1" ] || return 0
  mkdir -p "$DEST"
  mv "results/$1" "$DEST/"
  echo "  moved results/$1 -> $DEST/$1"
}

echo "== [0/3] deps =="
# Same install logic as run_fixedk_pipeline_on_pod.sh: default to the image's SYSTEM python
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
  python -c "import huggingface_hub" 2>/dev/null || pip install -q huggingface_hub
fi
pip install -q -r requirements.txt
if ! python -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null; then
  echo "!! torch cannot use this GPU — driver/CUDA mismatch or torch missing."
  echo "   driver: $(nvidia-smi 2>/dev/null | grep -oE 'CUDA Version: [0-9.]+' | head -1)"
  echo "   If the driver is < 12.8, re-run with:  VENV=1 CU124=1 bash unsteering/run_lora_unsteer_on_pod.sh"
  exit 1
fi
command -v vllm >/dev/null 2>&1 || { echo "!! vllm CLI not found after install"; exit 1; }

echo "== [1/3] downloading persona adapters: $TRAITS =="
for t in $TRAITS; do
  python - "$SRC_REPO" "$t" "$ADAPTERS_DIR" <<'PY'
import sys
from huggingface_hub import snapshot_download
repo, p, out = sys.argv[1], sys.argv[2], sys.argv[3]
snapshot_download(repo, allow_patterns=[f"{p}/adapter_config.json", f"{p}/adapter_model.safetensors"],
                  local_dir=out)
PY
  test -f "$ADAPTERS_DIR/$t/adapter_config.json" && test -f "$ADAPTERS_DIR/$t/adapter_model.safetensors" \
    || { echo "adapter download incomplete for $t"; exit 1; }
  echo "  got $t"
done

VLLM_PID=""
stop_vllm() {
  [ -n "$VLLM_PID" ] && kill "$VLLM_PID" 2>/dev/null || true
  pkill -f "vllm serve" 2>/dev/null || true   # also clear any stale server holding the port
  VLLM_PID=""
  sleep 3
}
trap stop_vllm EXIT

wait_ready() {  # wait_ready <port> <served-name> <pid> <log>
  local i
  for i in $(seq 1 180); do
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

pkill -f "vllm serve" 2>/dev/null || true
sleep 3
got="$(pick_port "$PORT")" || { echo "!! no free port near :$PORT"; exit 1; }
[ "$got" != "$PORT" ] && echo "  :$PORT busy — using :$got"
PORT="$got"
export LOCAL_BASE_URL="http://localhost:$PORT/v1"
export LOCAL_API_KEY="x"               # vLLM serves open; any value

echo "== [2/3] per-trait: serve base+LoRA -> K ladder ($KS) =="
for t in $TRAITS; do
  echo "================ trait: $t ================"
  # Skip serving entirely if every K for this trait is already generated.
  NEED=0
  for K in $KS; do
    if [ "$FORCE_REGEN" = "1" ] || ! have_condition "${t}_lora_unsteer_k${K}_ai2ai${EXP_SUFFIX}"; then NEED=1; fi
  done
  if [ "$NEED" = "0" ]; then echo "  all K cells exist — skipping $t"; continue; fi

  stop_vllm   # clean slate; never inherit a previous trait's server
  # ONE server, TWO served models: the base HF id AND the single adapter name. (Multi
  # --lora-modules proved unreliable in run_on_pod.sh — single-adapter serving is bulletproof.)
  echo "  starting vLLM: $BASE_MODEL + adapter '$t' ..."
  vllm serve "$BASE_MODEL" --enable-lora --max-lora-rank "$MAX_LORA_RANK" \
    --lora-modules "$t=$ADAPTERS_DIR/$t" \
    --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
    --gpu-memory-utilization "$GPU_MEM_UTIL" --port "$PORT" > "vllm_lora_unsteer_$t.log" 2>&1 &
  VLLM_PID=$!
  wait_ready "$PORT" "$t" "$VLLM_PID" "vllm_lora_unsteer_$t.log" || { echo "  !! $t not served — skipping"; continue; }
  curl -sf "http://localhost:$PORT/v1/models" | grep -q "\"$BASE_MODEL\"" \
    || { echo "  !! base id '$BASE_MODEL' not served alongside the adapter — skipping $t"; continue; }

  for K in $KS; do
    EXP="${t}_lora_unsteer_k${K}_ai2ai${EXP_SUFFIX}"
    if [ "$FORCE_REGEN" != "1" ] && have_condition "$EXP"; then
      echo "  ---- $EXP exists — skipping"
      move_into_dest "$EXP"   # tidy up a flat dir from an interrupted earlier run
      continue
    fi
    echo "  ---- $t, LoRA off after K=$K -> results/$EXP"
    TRAIT="$t" SWITCH_TURN="$K" python -m attractorbench.runner \
      --config unsteering/lora_unsteer_ai2ai.py \
      || { echo "  (runner errored for $t k$K — continuing)"; continue; }
    for j in results/"$EXP"/*.json; do
      [ -e "$j" ] || continue
      python -m attractorbench.analysis.deterministic "$j" || true
    done
    if [ "$JUDGE" != "none" ] && [ -n "$JUDGE" ]; then
      python run_judge.py "results/$EXP" --judge "$JUDGE" || echo "  (stage-2 judge errored — transcripts saved)"
      python run_onset_judge.py --conditions "$EXP" --judge "$JUDGE" || echo "  (onset judge errored — re-run later, it caches)"
    fi
    move_into_dest "$EXP"
  done
done
stop_vllm

echo "== [3/3] summary =="
python summarize.py || echo "  (summary errored — per-condition reports are still there)"
echo "== DONE. Conditions under $DEST/ =="

if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  echo "== saving results to git before shutdown =="
  git add -f results/ 2>/dev/null || true
  git -c user.name="attractorbench-pod" -c user.email="pod@attractorbench.local" \
    commit -q -m "results: lora-unsteer sweep (KS=$KS) $(date -u +%FT%TZ)" || echo "  (nothing new to commit)"
  git pull --no-rebase --no-edit 2>/dev/null || true
  git push || echo "  !! git push failed — results only on pod"
fi
case "${SHUTDOWN:-}" in
  stop) command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ] && runpodctl stop pod "$RUNPOD_POD_ID" ;;
esac
