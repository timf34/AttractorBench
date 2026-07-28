#!/usr/bin/env bash
# One-shot runner for the Assistant-Axis drift experiments (assistant_axis_drift/README.md).
# Sibling of run_sfm_on_pod.sh with one extra stage: after generating each model's ai2ai
# conversations via vLLM, it stops vLLM and REPLAYS the transcripts through the HF model to
# project per-turn activations onto the Assistant Axis.
#
# Per model: download -> vLLM serve -> generate BOTH system-prompt conditions x temp sweep ->
# stop vLLM -> projection replay -> stage-1 + optional judge -> weight cleanup.
#
# Requires: 2x 80GB GPUs for llama-3.3-70b (gemma/qwen run fine on the same pod); HF_TOKEN
# with licenses accepted for google/gemma-2-27b-it, Qwen/Qwen3-32B, and
# meta-llama/Llama-3.3-70B-Instruct (the preflight checks all three).
#
# Usage (put HF_TOKEN and OPENROUTER_API_KEY in .env at the repo root — auto-loaded below):
#   SAVE_TO_GIT=1 SHUTDOWN=stop bash run_axis_on_pod.sh 2>&1 | tee axis_run.log
#   VARIANTS="qwen-3-32b" CONDITIONS="none" SEEDS=2 TEMPS=1.0 JUDGE=none bash run_axis_on_pod.sh   # smoke
set -euo pipefail

# Load .env from the repo root if present, so HF_TOKEN / OPENAI_API_KEY need no manual exports.
# (The python side already reads .env via load_dotenv; this covers the shell preflight and
# huggingface_hub, which only see real environment variables.)
if [ -f .env ]; then
  set -a
  # shellcheck disable=SC1091
  . ./.env
  set +a
  echo "loaded .env"
fi

PORT=8000

# Model keys (see configs/axis_ai2ai.py AXIS_MODELS). Qwen first: cheapest full validation.
VARIANTS="${VARIANTS:-qwen-3-32b gemma-2-27b llama-3.3-70b}"
# System-prompt conditions per model: none (paper-faithful) and/or helpful (suite convention).
CONDITIONS="${CONDITIONS:-none helpful}"

MAX_NUM_SEQS=24
GPU_MEM_UTIL=0.92
export WORKERS="${WORKERS:-16}"
# Stage-2 judge via OpenRouter by default (needs OPENROUTER_API_KEY in .env; no OpenAI key).
# JUDGE=none skips judging entirely — transcripts, stage-1, and axis projections still run.
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"
CLEANUP_WEIGHTS="${CLEANUP_WEIGHTS:-1}"
NGPU=$(nvidia-smi -L 2>/dev/null | wc -l | tr -d ' ')
[ "${NGPU:-0}" -ge 1 ] || { echo "!! no GPUs visible (nvidia-smi)"; exit 1; }

hf_repo_of() {  # model key -> HF repo + per-model serve length (kept in sync with configs/axis_ai2ai.py)
  case "$1" in
    gemma-2-27b)   REPO="google/gemma-2-27b-it";                MAX_MODEL_LEN=8192 ;;
    qwen-3-32b)    REPO="Qwen/Qwen3-32B";                       MAX_MODEL_LEN=16384 ;;
    llama-3.3-70b) REPO="meta-llama/Llama-3.3-70B-Instruct";    MAX_MODEL_LEN=16384 ;;
    *) echo "unknown variant $1"; return 1 ;;
  esac
}
exp_of() {  # model key + condition -> results dir name (MUST match configs/axis_ai2ai.py EXP)
  local slug; slug=$(echo "$1" | tr '.-' '__')
  if [ "$2" = "none" ]; then echo "axis_${slug}_nosys_ai2ai"; else echo "axis_${slug}_ai2ai"; fi
}

if [ -z "${HF_HOME:-}" ] && [ -d /workspace ]; then
  export HF_HOME=/workspace/hf
fi
echo "HF cache: ${HF_HOME:-~/.cache/huggingface}  GPUs: $NGPU"

export GIT_TERMINAL_PROMPT=0
if [ -n "${RUNPOD_POD_ID:-}" ] && [ -d /workspace ]; then
  case "$PWD" in
    /workspace/*) ;;
    *) echo "!! checkout at $PWD — on RunPod only /workspace survives a stop. Clone there."; exit 1 ;;
  esac
fi
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  git push --dry-run >/dev/null 2>&1 || {
    echo "!! SAVE_TO_GIT=1 but non-interactive 'git push --dry-run' failed — set a PAT remote."; exit 1; }
  echo "git push preflight OK"
fi

echo "== [1/5] installing deps =="
if [ "${VENV:-0}" = "1" ]; then
  VENV_DIR="${VENV_DIR:-/workspace/ab_venv}"
  echo "  building clean venv at $VENV_DIR..."
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
  [ -n "$SITE" ] && rm -rf "$SITE"/flashinfer* "$SITE"/tvm_ffi* "$SITE"/tvm-ffi* "$SITE"/torch_c_dlpack_ext* 2>/dev/null || true
else
  python -c "import vllm" 2>/dev/null || pip install -q vllm
fi
pip install -q -r requirements.txt -r assistant_axis_drift/requirements.txt

python -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null || {
  echo "  !! torch cannot use this GPU — driver/CUDA mismatch (try VENV=1 CU124=1)."; exit 1; }
echo "  torch.cuda OK"

echo "== [2/5] preflight: HF auth + gemma template fold =="
[ -n "${HF_TOKEN:-}" ] || { echo "!! HF_TOKEN not set (all three models are gated)"; exit 1; }
for v in $VARIANTS; do
  hf_repo_of "$v"
  python - "$REPO" <<'PY' || { echo "!! cannot access gated repo — accept its license on HF"; exit 1; }
import sys
from huggingface_hub import hf_hub_download
hf_hub_download(sys.argv[1], "config.json")
print(f"  auth OK: {sys.argv[1]}")
PY
done
# The custom gemma template (accepts a system message by folding it into the first user turn)
# must render EXACTLY like the native template on python-folded messages — else generation and
# replay would tokenize different strings. Checked against the pinned template copy; also pass
# the live tokenizer's template to catch upstream edits.
python - <<'PY'
from transformers import AutoTokenizer
from assistant_axis_drift.verify_templates import verify
verify()
tok = AutoTokenizer.from_pretrained("google/gemma-2-27b-it")
if tok.chat_template:
    verify(native_template=tok.chat_template)
    print("  live gemma tokenizer template also matches")
PY
# Axis vectors download now (fail fast, cached for the replay stage).
python - <<PY
from assistant_axis_drift.axes import load_axis_for
for key in "$VARIANTS".split():
    axis, anchors = load_axis_for(key)
    print(f"  axis OK: {key} {tuple(axis.shape)}")
PY

export LOCAL_BASE_URL="http://localhost:$PORT/v1"
export LOCAL_API_KEY="x"

VLLM_PID=""
stop_vllm() {
  [ -n "$VLLM_PID" ] && kill "$VLLM_PID" 2>/dev/null || true
  pkill -f "vllm serve" 2>/dev/null || true
  VLLM_PID=""
  sleep 3
}
trap stop_vllm EXIT

echo "== [3/5]..[5/5] per-model: download -> serve -> generate -> project -> judge =="
for v in $VARIANTS; do
  hf_repo_of "$v"
  echo "================ model: $v ($REPO, max_len $MAX_MODEL_LEN) ================"
  stop_vllm

  echo "  downloading weights for $REPO ..."
  SNAP_PATH=$(python - "$REPO" <<'PY'
import sys
from huggingface_hub import snapshot_download
print(snapshot_download(sys.argv[1]))
PY
  ) || { echo "  !! weight download FAILED for $REPO — skipping"; continue; }

  # Chat template overrides: gemma needs the system-fold template (only the 'helpful' condition
  # sends a system message, but serving it always is safe — it is a strict superset of native);
  # qwen needs thinking force-disabled at the template level.
  TEMPLATE_FLAG=""
  if [ "$v" = "gemma-2-27b" ]; then
    TEMPLATE_FLAG="--chat-template assistant_axis_drift/templates/gemma2_system_fold.jinja"
  elif [ "$v" = "qwen-3-32b" ]; then
    python - "$REPO" <<'PY'
import sys
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained(sys.argv[1])
with open("qwen3_no_thinking.jinja", "w") as f:
    f.write("{%- set enable_thinking = false -%}" + tok.chat_template)
print("  wrote qwen3_no_thinking.jinja (enable_thinking pinned false)")
PY
    TEMPLATE_FLAG="--chat-template qwen3_no_thinking.jinja"
  fi

  echo "  starting vLLM (TP=$NGPU) ..."
  # shellcheck disable=SC2086
  vllm serve "$SNAP_PATH" --served-model-name "$REPO" $TEMPLATE_FLAG \
    --tensor-parallel-size "$NGPU" \
    --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
    --gpu-memory-utilization "$GPU_MEM_UTIL" --port "$PORT" > "vllm_axis_${v}.log" 2>&1 &
  VLLM_PID=$!

  ready=0
  for i in $(seq 1 180); do
    if curl -sf "http://localhost:$PORT/v1/models" 2>/dev/null | grep -q "$REPO"; then
      ready=1; echo "  vLLM serving $REPO after ~$((i*5))s"; break
    fi
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then echo "  vLLM died — see vllm_axis_${v}.log"; tail -20 "vllm_axis_${v}.log"; break; fi
    sleep 5
  done
  [ "$ready" = 1 ] || { echo "  !! $v not served — skipping"; continue; }

  GEN_OK=1
  for c in $CONDITIONS; do
    EXP=$(exp_of "$v" "$c")
    echo "  generating: $v / AXIS_SYS=$c -> results/$EXP ($WORKERS parallel)..."
    AXIS_MODEL="$v" AXIS_SYS="$c" python -m attractorbench.runner --config configs/axis_ai2ai.py \
      || { GEN_OK=0; echo "  (runner errored for $v/$c — continuing)"; }
    for j in results/$EXP/*.json; do
      [ -e "$j" ] || continue
      python -m attractorbench.analysis.deterministic "$j" || true
    done
  done

  stop_vllm   # projection replay needs the VRAM
  echo "  projecting activations onto the Assistant Axis ($v) ..."
  DIRS=""
  for c in $CONDITIONS; do
    d="results/$(exp_of "$v" "$c")"; [ -d "$d" ] && DIRS="$DIRS $d"
  done
  if [ -n "$DIRS" ]; then
    # shellcheck disable=SC2086
    python -m assistant_axis_drift.project_transcripts --results-dir $DIRS --model-key "$v" \
      || echo "  (projection errored for $v — transcripts still saved)"
  fi

  if [ "$JUDGE" != "none" ] && [ -n "$JUDGE" ]; then
    for c in $CONDITIONS; do
      d="results/$(exp_of "$v" "$c")"; [ -d "$d" ] || continue
      python run_judge.py "$d" --judge "$JUDGE" || echo "  (judge errored for $v/$c)"
    done
  fi

  if [ "$CLEANUP_WEIGHTS" = "1" ] && [ "$GEN_OK" = "1" ]; then
    CACHE_DIR="${HF_HOME:-$HOME/.cache/huggingface}/hub/models--${REPO//\//--}"
    echo "  cleaning up weights: $CACHE_DIR"
    rm -rf "$CACHE_DIR"
  fi
done
stop_vllm

python summarize.py || echo "  (summary errored — per-condition reports are still there)"
echo "== DONE. Projections: results/axis_*_ai2ai/analysis/*__axis_projections.json =="
echo "== On the laptop afterwards: python -m assistant_axis_drift.analyze_axis =="

case "${SHUTDOWN:-}" in
  stop)      RP_ACTION="stop" ;;
  terminate) RP_ACTION="remove" ;;
  ""|0)      RP_ACTION="" ;;
  *)         RP_ACTION="stop" ;;
esac
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  echo "== saving results to git before shutdown =="
  git add -f results/ 2>/dev/null || true
  git commit -q -m "results: axis run finished $(date -u +%FT%TZ)" || echo "  (nothing new to commit)"
  git pull --no-rebase --no-edit 2>/dev/null || true
  if git push; then
    echo "  results pushed to remote"
  elif [ "$RP_ACTION" = "remove" ]; then
    echo "  !! git push FAILED — refusing to terminate; downgrading to 'stop'."
    RP_ACTION="stop"
  fi
fi
if [ -n "$RP_ACTION" ]; then
  echo "== SHUTDOWN=$SHUTDOWN -> runpodctl $RP_ACTION pod ${RUNPOD_POD_ID:-<unset>} =="
  if command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ]; then
    runpodctl "$RP_ACTION" pod "$RUNPOD_POD_ID"
  else
    echo "  !! cannot self-shutdown (runpodctl missing or RUNPOD_POD_ID unset)."
  fi
fi
