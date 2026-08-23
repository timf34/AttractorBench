#!/usr/bin/env bash
# Persona-PROMPT ai2ai on the two OCT bases that only have a LoRA arm — Qwen 2.5 7B and
# Gemma 3 4B. Fills the model-set gap that confounds the SBERT geometry comparison.
#
# WHY THIS EXISTS
# oct_geometry.py (LoRA corpus) runs on {llama-3.1-8b, qwen-2.5-7b, gemma-3-4b}; prompt_geometry.py
# (prompt corpus) runs on {llama-8b, gpt-4.1, kimi-k2, llama-3.3-70b, deepseek-v4-pro}. The two sets
# overlap in llama-8b and nothing else, so "fine-tuning transfers the voice, prompting transfers the
# theme" is measured across a small-open-weights trio vs a mostly-large-API set — exactly the axis a
# model-set swap would move. This script generates the missing cells so the claim can be tested
# within ONE matched model set (see prompt_geometry.py --models matched).
#
# SERVING: the raw base on vLLM, no adapters — the prompt arm needs none, so Gemma needs no
# merge_lora.py surgery here (unlike the LoRA arm). Same backend, same sampling params, and the
# same MAX_NEW_TOKENS=1536 as run_oct_crossmodel_on_pod.sh, so the LoRA-vs-prompt contrast within
# a base carries no backend or budget confound.
#
# BASE CONTROL IS NOT REGENERATED. `base_ai2ai_<slug>` already exists from the 2026-08-05 OCT
# cross-base sweep and is the identical condition (raw base + helpful_assistant, vLLM, 15 runs x
# 30 turns, temp 0.7, MNT 1536). Re-running it would overwrite good data for nothing, so `base` is
# refused below and both geometry scripts read the existing dir.
#
# Usage (RunPod; same image assumptions as unsteering/run_lora_unsteer_on_pod.sh):
#   bash run_persona_oct_bases_on_pod.sh                          # qwen + gemma, 24 personas each
#   OCT_BASES=qwen bash run_persona_oct_bases_on_pod.sh           # one base
#   PERSONAS="goodness_rich" SEEDS=2 JUDGE=none bash run_persona_oct_bases_on_pod.sh   # smoke
#   SAVE_TO_GIT=1 SHUTDOWN=stop bash run_persona_oct_bases_on_pod.sh                   # unattended
#   VENV=1 CU124=1 bash run_persona_oct_bases_on_pod.sh           # host driver < CUDA 12.8
set -euo pipefail
cd "$(dirname "$0")"
export HF_HOME="${HF_HOME:-/workspace/.cache/huggingface}"

PY="${PY:-python}"
PORT="${PORT:-8000}"
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"
OCT_BASES="${OCT_BASES:-qwen gemma}"
FORCE_REGEN="${FORCE_REGEN:-0}"

TRAITS="${TRAITS:-honesty sincerity goodness humor impulsiveness loving mathematical nonchalance poeticism remorse sarcasm sycophancy}"
if [ -z "${PERSONAS:-}" ]; then
  PERSONAS=""
  for t in $TRAITS; do PERSONAS="$PERSONAS ${t}_rich ${t}_grounded"; done   # NB: no `base` — see header
fi

MAX_MODEL_LEN="${MAX_MODEL_LEN:-32768}"
MAX_NUM_SEQS="${MAX_NUM_SEQS:-24}"
GPU_MEM_UTIL="${GPU_MEM_UTIL:-0.92}"
# Match the OCT LoRA sweep exactly: 15 reps x 30 turns, one temperature, verbose-model budget.
export SEEDS="${SEEDS:-15}" TEMPS="${TEMPS:-0.7}" WORKERS="${WORKERS:-10}"
export MAX_NEW_TOKENS="${MAX_NEW_TOKENS:-1536}"
export BACKEND=local

# slug -> HF base id + results suffix (must match run_oct_crossmodel_on_pod.sh's S values, so the
# prompt arm lands beside the LoRA arm for the same base).
base_of() {
  case "$1" in
    qwen)  echo "Qwen/Qwen2.5-7B-Instruct" ;;
    gemma) echo "unsloth/gemma-3-4b-it" ;;     # ungated mirror; google/ is gated
    *) return 1 ;;
  esac
}
suffix_of() {
  case "$1" in
    qwen)  echo "_qwen-2.5-7b" ;;
    gemma) echo "_gemma-3-4b" ;;
    *) return 1 ;;
  esac
}

exp_of() {  # persona token -> results dir name (MUST match configs/persona_ai2ai.py's EXP logic)
  case "$1" in
    *_rich)     echo "${1%_rich}_richprompt_ai2ai" ;;
    *_grounded) echo "${1%_grounded}_groundedprompt_ai2ai" ;;
    base)       return 1 ;;   # refused: would clobber the OCT sweep's control (see header)
    *) return 1 ;;
  esac
}

have_condition() { ls "results/$1"/two_instance__*temp0.7.json >/dev/null 2>&1; }

echo "== [0/3] deps =="
if [ "${VENV:-0}" = "1" ]; then
  VENV_DIR="${VENV_DIR:-/workspace/ab_venv}"
  $PY -m venv "$VENV_DIR"; . "$VENV_DIR/bin/activate"; pip install -q -U pip
fi
if [ "${CU124:-0}" = "1" ]; then
  pip install -q "vllm==0.8.5.post1" "transformers==4.51.3" "tokenizers==0.21.4" "huggingface_hub==0.34.4"
  pip uninstall -y flashinfer flashinfer-python tvm_ffi tvm-ffi torch_c_dlpack_ext humming-kernels >/dev/null 2>&1 || true
else
  $PY -c "import vllm" 2>/dev/null || pip install -q vllm
fi
pip install -q -r requirements.txt
$PY -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null || {
  echo "!! torch cannot use this GPU. driver: $(nvidia-smi 2>/dev/null | grep -oE 'CUDA Version: [0-9.]+' | head -1)"
  echo "   If < 12.8:  VENV=1 CU124=1 bash run_persona_oct_bases_on_pod.sh"; exit 1; }

VLLM_PID=""
stop_vllm() { [ -n "$VLLM_PID" ] && kill "$VLLM_PID" 2>/dev/null || true; pkill -f "vllm serve" 2>/dev/null || true; VLLM_PID=""; sleep 3; }
trap stop_vllm EXIT

wait_ready() {  # wait_ready <port> <served-name> <pid> <log>
  local i
  for i in $(seq 1 180); do
    curl -sf "http://localhost:$1/v1/models" 2>/dev/null | grep -q "\"$2\"" && { echo "  vLLM :$1 serving '$2' (~$((i*5))s)"; return 0; }
    kill -0 "$3" 2>/dev/null || { echo "  !! vLLM died — see $4"; tail -20 "$4"; return 1; }
    sleep 5
  done
  return 1
}
port_busy() { [ -n "$(ss -ltnH "sport = :$1" 2>/dev/null)" ]; }
pick_port() { local c; for c in "$1" $(($1+1000)) $(($1+2000)) $(($1+3000)); do port_busy "$c" || { echo "$c"; return 0; }; done; return 1; }

pkill -f "vllm serve" 2>/dev/null || true; sleep 3
PORT="$(pick_port "$PORT")" || { echo "!! no free port"; exit 1; }
export LOCAL_BASE_URL="http://localhost:$PORT/v1" LOCAL_API_KEY="x"

echo "== [1/3] bases: $OCT_BASES =="
for m in $OCT_BASES; do
  B="$(base_of "$m")" || { echo "unknown base: $m (roster: qwen gemma)"; exit 1; }
  S="$(suffix_of "$m")"
  echo "================ base: $m ($B) -> *${S} ================"
  export BASE_MODEL="$B" EXP_SUFFIX="$S"

  # Guard the reused control: it must already be there, or the matched-set analysis has a hole.
  have_condition "base_ai2ai${S}" \
    || echo "  !! WARNING: results/base_ai2ai${S} missing — the geometry scripts need it as the base control"

  NEED=0
  for p in $PERSONAS; do
    E="$(exp_of "$p")" || continue
    { [ "$FORCE_REGEN" = "1" ] || ! have_condition "${E}${S}"; } && NEED=1
  done
  [ "$NEED" = "0" ] && { echo "  all personas exist for $m — skipping"; continue; }

  stop_vllm
  echo "  starting vLLM: $B (no adapters — prompt arm)"
  vllm serve "$B" --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
    --gpu-memory-utilization "$GPU_MEM_UTIL" --port "$PORT" > "vllm_prompt_$m.log" 2>&1 &
  VLLM_PID=$!
  wait_ready "$PORT" "$B" "$VLLM_PID" "vllm_prompt_$m.log" || { echo "  !! $m not served — skipping"; continue; }

  for p in $PERSONAS; do
    E="$(exp_of "$p")" || { echo "  !! '$p' is not a rich/grounded persona — skipping"; continue; }
    EXP="${E}${S}"
    if [ "$FORCE_REGEN" != "1" ] && have_condition "$EXP"; then echo "  ---- $EXP exists — skipping"; continue; fi
    echo "  ---- $m :: $p -> results/$EXP"
    PERSONA="$p" $PY -m attractorbench.runner --config configs/persona_ai2ai.py \
      || { echo "  (runner errored for $m/$p — continuing)"; continue; }
    for j in results/"$EXP"/*.json; do
      [ -e "$j" ] || continue
      $PY -m attractorbench.analysis.deterministic "$j" || true
    done
    if [ "$JUDGE" != "none" ] && [ -n "$JUDGE" ]; then
      $PY run_judge.py "results/$EXP" --judge "$JUDGE" || echo "  (judge errored — transcripts saved)"
    fi
  done
done
stop_vllm

echo "== [2/3] matched-set geometry =="
# prompt_geometry.py is a LAPTOP script: it needs sentence-transformers (not in requirements.txt)
# and picks the `mps` device. Only attempt it if the dep happens to be present; the normal path is
# to pull results down and run it locally:
#     rp scp <pod> pod:/workspace/AttractorBench/results ./results -r
#     ./.venv/bin/python prompt_geometry.py --models matched
if $PY -c "import sentence_transformers" 2>/dev/null; then
  $PY prompt_geometry.py --models matched || echo "  (prompt_geometry errored — conditions are still there)"
else
  echo "  skipped: sentence-transformers not installed here — run it on the laptop after rp scp"
fi

echo "== [3/3] summary =="
$PY summarize.py || echo "  (summary errored)"
echo "== DONE. results/<trait>_{rich,grounded}prompt_ai2ai{_qwen-2.5-7b,_gemma-3-4b} =="

if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  git add -f results/ 2>/dev/null || true
  git -c user.name="attractorbench-pod" -c user.email="pod@attractorbench.local" \
    commit -q -m "results: persona-prompt arm on OCT bases (qwen-2.5-7b, gemma-3-4b) $(date -u +%FT%TZ)" \
    || echo "  (nothing new to commit)"
  git pull --no-rebase --no-edit 2>/dev/null || true
  git push || echo "  !! git push failed — results only on pod"
fi
case "${SHUTDOWN:-}" in
  stop) command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ] && runpodctl stop pod "$RUNPOD_POD_ID" ;;
esac
