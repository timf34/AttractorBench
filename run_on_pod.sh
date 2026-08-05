#!/usr/bin/env bash
# One-shot runner for the persona self-conversation experiments on a rented GPU pod.
#
# Runs vLLM AND the harness locally on the pod (harness -> localhost), so the run does NOT depend
# on any laptop staying awake/networked. No OpenWeights, no LoRA flattening: vLLM loads each persona
# adapter straight from a LOCAL directory.
#
# Serves ONE persona per vLLM instance (restarting between personas). vLLM's multi --lora-modules
# proved unreliable (only the first registered); single-LoRA serving is bulletproof and the base
# reloads in ~5s on a warm H200, so the restart overhead is negligible.
#
# Recommended GPU: 1x H100/H200 or A100 80GB. A 48GB card works but lower the concurrency knobs.
#
# Usage:
#   git clone <repo> && cd AttractorBench
#   export OPENROUTER_API_KEY=sk-or-...  # only needed for the stage-2 attractor judge
#   VENV=1 CU124=1 bash run_on_pod.sh           # CU124/VENV only needed on a <12.8-driver host
#   PERSONAS="goodness loving" bash run_on_pod.sh    # subset
set -euo pipefail

# Base model + adapter-source repo — overridable so this same script drives the OCT cross-base
# sweep (run_oct_crossmodel_on_pod.sh): the Open-Character-Training pipeline trained the same
# 10 persona LoRAs on Qwen2.5-7B and Gemma-3-4B too.
BASE_MODEL="${BASE_MODEL:-unsloth/Meta-Llama-3.1-8B-Instruct}"
SRC_REPO="${SRC_REPO:-maius/llama-3.1-8b-it-personas}"
# Where adapters download to (per-base dirs keep same-named personas from clobbering each other).
ADAPTERS_DIR="${ADAPTERS_DIR:-./adapters}"
# lora  = serve base + --lora-modules (Llama/Qwen adapters).
# merge = bake each adapter into the base weights (merge_lora.py) and serve the merged dir —
#         needed for the Gemma-3 adapters (vision-tower LoRA keys + new-transformers key layout
#         that vLLM's LoRA loader rejects). Merged dirs are deleted per persona unless KEEP_MERGED=1.
SERVE_MODE="${SERVE_MODE:-lora}"
# Results-dir suffix, e.g. _qwen-2.5-7b -> results/goodness_ai2ai_qwen-2.5-7b. Exported because
# configs/persona_ai2ai.py appends it too; keeps cross-base runs out of the original Llama dirs.
EXP_SUFFIX="${EXP_SUFFIX:-}"
export EXP_SUFFIX
PORT=8000

# Which personas to run (space-separated). Special base-served (no-LoRA) entries:
#   base       = raw base model control
#   sincerity / honesty = base model with a trait elicited via the SYSTEM prompt
# All others are LoRA adapters. Override with e.g. PERSONAS="sincerity honesty".
PERSONAS="${PERSONAS:-base sincerity honesty goodness loving humor impulsiveness mathematical nonchalance poeticism remorse sarcasm sycophancy}"
# Prompted personas: base model + trait via system prompt (no LoRA). "<trait>_sp" tokens compare a
# prompted trait head-to-head with its LoRA (e.g. goodness_sp vs goodness). sincerity/honesty have
# no LoRA so they use the bare name. All are served by the bare base model.
PROMPTED="sincerity honesty goodness_sp sycophancy_sp loving_sp sarcasm_sp remorse_sp"
# Served by the bare base model (no adapter download, no --lora-modules):
BASE_SERVED="base $PROMPTED"
# GENERATED-prompt personas (persona_promptgen pipeline) are also base-served:
#   <trait>_rich | <trait>_grounded, e.g. PERSONAS="humor_rich humor_grounded"
# They need attractorbench/prompts_generated.py present in the checkout (generate + commit first).
is_base_served() {
  case " $BASE_SERVED " in *" $1 "*) return 0 ;; esac
  case "$1" in *_rich|*_grounded) return 0 ;; esac
  return 1
}

# Concurrency knobs — tuned for 80GB+ GPUs. Lower MAX_NUM_SEQS/WORKERS for a 48GB card.
MAX_MODEL_LEN=32768   # headroom so high-temp rambles + the anti-truncation retry don't overflow
MAX_NUM_SEQS=24
GPU_MEM_UTIL=0.92
MAX_LORA_RANK=64      # the persona adapters are rank 64; vLLM defaults to 16 and would reject them
export GOODNESS_WORKERS="${GOODNESS_WORKERS:-16}"   # parallel conversations the harness drives
# Judge model for stage-2 (provider-prefixed). Default goes through OpenRouter (needs
# OPENROUTER_API_KEY) — the OpenAI account ran dry mid-sweep once (insufficient_quota, SFM run).
# Set JUDGE=openai/gpt-5.4 to hit OpenAI directly, or JUDGE=none to skip judging
# (conversations + stage-1 still run).
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"

echo "== [1/4] installing deps =="
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
  exit 1
fi
echo "  torch.cuda OK"

echo "== [2/4] downloading persona adapters: $PERSONAS =="
for p in $PERSONAS; do
  if is_base_served "$p"; then echo "  $p (base-served, no adapter needed)"; continue; fi
  python - "$SRC_REPO" "$p" "$ADAPTERS_DIR" <<'PY'
import sys
from huggingface_hub import snapshot_download
repo, p, out = sys.argv[1], sys.argv[2], sys.argv[3]
snapshot_download(repo, allow_patterns=[f"{p}/adapter_config.json", f"{p}/adapter_model.safetensors"],
                  local_dir=out)
PY
  test -f "$ADAPTERS_DIR/$p/adapter_config.json" && test -f "$ADAPTERS_DIR/$p/adapter_model.safetensors" \
    || { echo "adapter download incomplete for $p"; exit 1; }
  echo "  got $p"
done

export LOCAL_BASE_URL="http://localhost:$PORT/v1"
export LOCAL_API_KEY="x"               # vLLM serves open; any value
export BASE_MODEL                      # so the config can target the base for PERSONA=base

VLLM_PID=""
stop_vllm() {
  [ -n "$VLLM_PID" ] && kill "$VLLM_PID" 2>/dev/null || true
  pkill -f "vllm serve" 2>/dev/null || true   # also clear any stale server holding the port
  VLLM_PID=""
  sleep 3
}
trap stop_vllm EXIT

echo "== [3/4] + [4/4] per-persona: serve one LoRA -> run sweep -> judge =="
for p in $PERSONAS; do
  echo "================ persona: $p ================"
  stop_vllm   # clean slate; never inherit a previous persona's server
  if is_base_served "$p"; then
    LORA_FLAGS=""; SERVE_TARGET="$BASE_MODEL"; SERVED="$BASE_MODEL"   # base / prompted / generated-prompt persona: bare base, no LoRA
  elif [ "$SERVE_MODE" = "merge" ]; then
    echo "  merging '$p' into $BASE_MODEL -> ./merged/$p ..."
    python merge_lora.py --base "$BASE_MODEL" --adapter "$ADAPTERS_DIR/$p" --out "./merged/$p" \
      || { echo "  !! merge failed for $p — skipping"; continue; }
    LORA_FLAGS="--served-model-name $p"; SERVE_TARGET="./merged/$p"; SERVED="$p"
  else
    LORA_FLAGS="--enable-lora --max-lora-rank $MAX_LORA_RANK --lora-modules $p=$ADAPTERS_DIR/$p"; SERVE_TARGET="$BASE_MODEL"; SERVED="$p"
  fi
  echo "  starting vLLM for '$p' (serves model '$SERVED') ..."
  # shellcheck disable=SC2086
  vllm serve "$SERVE_TARGET" $LORA_FLAGS \
    --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
    --gpu-memory-utilization "$GPU_MEM_UTIL" --port "$PORT" > "vllm_$p.log" 2>&1 &
  VLLM_PID=$!

  ready=0
  for i in $(seq 1 180); do
    if curl -sf "http://localhost:$PORT/v1/models" 2>/dev/null | grep -q "\"$SERVED\""; then
      ready=1; echo "  vLLM serving '$SERVED' after ~$((i*5))s"; break
    fi
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then echo "  vLLM died for $p — see vllm_$p.log"; tail -20 "vllm_$p.log"; break; fi
    sleep 5
  done
  if [ "$ready" != 1 ]; then echo "  !! $p not served — skipping"; continue; fi

  # results dir / experiment name — MUST match configs/persona_ai2ai.py's EXP logic
  case "$p" in
    *_rich)     EXP="${p%_rich}_richprompt_ai2ai" ;;         # humor_rich -> humor_richprompt_ai2ai
    *_grounded) EXP="${p%_grounded}_groundedprompt_ai2ai" ;; # humor_grounded -> humor_groundedprompt_ai2ai
    *) case " $PROMPTED " in
         *" $p "*) EXP="${p%_sp}_sysprompt_ai2ai" ;;  # goodness_sp -> goodness_sysprompt_ai2ai; sincerity -> sincerity_sysprompt_ai2ai
         *) EXP="${p}_ai2ai" ;;                        # base_ai2ai and <lora>_ai2ai
       esac ;;
  esac
  EXP="$EXP$EXP_SUFFIX"   # cross-base runs land in their own dirs, matching the config's EXP
  echo "  running sweep for $p -> results/$EXP ($GOODNESS_WORKERS parallel)..."
  PERSONA="$p" python -m attractorbench.runner --config configs/persona_ai2ai.py || echo "  (runner errored for $p — continuing)"
  # stage-1 deterministic analysis (word/phrase/emoji frequency, convergence) — no API, always run
  for j in results/$EXP/*.json; do
    [ -e "$j" ] || continue
    python -m attractorbench.analysis.deterministic "$j" || true
  done
  if [ "$JUDGE" = "none" ] || [ -z "$JUDGE" ]; then
    echo "  (JUDGE=none -> skipping judge for $p; run run_judge.py later)"
  else
    python run_judge.py "results/$EXP" --judge "$JUDGE" || echo "  (judge errored for $p — transcripts still saved)"
  fi
  # merge mode: each merged copy is ~2x base-model disk — drop it once the persona is done
  if [ "$SERVE_MODE" = "merge" ] && ! is_base_served "$p" && [ "${KEEP_MERGED:-0}" != "1" ]; then
    rm -rf "./merged/$p"
  fi
done
stop_vllm

# One-page headline summary across every condition (deterministic; reads existing reports).
python summarize.py || echo "  (summary errored — per-condition reports are still there)"

echo "== DONE. Per persona: results/<persona>_ai2ai/*.md (transcripts) + analysis/*__stage2.md =="
echo "== Overall headline summary: results/SUMMARY.md =="

# Optional self-shutdown so an unattended overnight run doesn't keep billing after it finishes.
# Requires runpodctl authed with your RunPod API key (one-time: runpodctl config --apiKey <KEY>);
# RUNPOD_POD_ID is set automatically on every RunPod pod.
#   SHUTDOWN=stop       -> PAUSE the pod: GPU billing stops, disk + results KEPT, restart later.
#   SHUTDOWN=terminate  -> DESTROY the pod: no billing, but DELETES the disk/results unless they're
#                          on a persistent network volume. Make sure results are saved off-pod first.
case "${SHUTDOWN:-}" in
  stop)      RP_ACTION="stop" ;;
  terminate) RP_ACTION="remove" ;;
  ""|0)      RP_ACTION="" ;;
  *)         RP_ACTION="stop" ;;   # any other truthy value -> the safe option
esac

# Optionally push results to GitHub before shutting down so a terminate can't lose them. Needs
# non-interactive git auth on the pod (e.g. a PAT in the remote:
#   git remote set-url origin https://<TOKEN>@github.com/timf34/AttractorBench.git ).
# SAFETY: if the push fails, any pending 'terminate' is downgraded to 'stop' so data is never lost.
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  echo "== saving results to git before shutdown =="
  git add -f results/ 2>/dev/null || true
  # -c identity: fresh pods have no git user configured, and a failed commit here once cost a
  # whole sweep its push (the "(nothing new to commit)" fallback masked it).
  git -c user.name="attractorbench-pod" -c user.email="pod@attractorbench.local" \
    commit -q -m "results: run finished $(date -u +%FT%TZ)" || echo "  (nothing new to commit)"
  git pull --no-rebase --no-edit 2>/dev/null || true   # reconcile with remote first so push isn't rejected
  if git push; then
    echo "  results pushed to remote"
  elif [ "$RP_ACTION" = "remove" ]; then
    echo "  !! git push FAILED — refusing to terminate; downgrading to 'stop' to keep data."
    RP_ACTION="stop"
  fi
fi

if [ -n "$RP_ACTION" ]; then
  echo "== SHUTDOWN=$SHUTDOWN -> runpodctl $RP_ACTION pod ${RUNPOD_POD_ID:-<unset>} =="
  if command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ]; then
    runpodctl "$RP_ACTION" pod "$RUNPOD_POD_ID"
  else
    echo "  !! cannot self-shutdown (runpodctl missing or RUNPOD_POD_ID unset) — pod left running."
  fi
fi
