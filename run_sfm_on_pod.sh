#!/usr/bin/env bash
# One-shot runner for the Geodesic SFM (Self-Fulfilling Misalignment / "alignment pretraining")
# self-conversation experiments on a rented GPU pod. Sibling of run_on_pod.sh, but serves FULL
# 6.9B GPT-NeoX checkpoints (one vLLM per variant, no LoRA machinery).
#
# Maps the base ai2ai attractor states across pretraining recipes: same harness/framing as the
# llama base_ai2ai runs (helpful_assistant system, goodness_opener_v1 opener, temps 0.7/1.0/1.3,
# 15 seeds, 30 turns) — only the pretraining recipe varies.
#
# Fully self-contained: installs deps, downloads each variant's weights (~14GB) + chat template
# from HF, serves, runs the sweep + stage-1 + judge, then DELETES that variant's weights from the
# cache before moving on (CLEANUP_WEIGHTS=0 to keep them) — so peak disk stays ~14GB instead of
# ~150GB for the full 11-variant sweep. Weights cache on /workspace (the persistent volume) when
# it exists.
#
# Recommended GPU: 1x H100/H200 or A100 80GB (a 6.9B bf16 model + 16k KV cache is comfortable).
#
# Usage:
#   git clone <repo> && cd AttractorBench
#   export OPENAI_API_KEY=sk-...        # only needed for the stage-2 attractor judge
#   VENV=1 CU124=1 bash run_sfm_on_pod.sh                 # CU124/VENV only on a <12.8-driver host
#   VARIANTS="baseline_unfiltered baseline_filtered" bash run_sfm_on_pod.sh   # subset
#   SFM_POST=dpo bash run_sfm_on_pod.sh                   # the DPO tier instead of SFT
#
# Unattended overnight run (results pushed to git, pod stops itself when done):
#   runpodctl config --apiKey <RUNPOD_KEY>                # one-time, enables self-shutdown
#   git remote set-url origin https://<PAT>@github.com/timf34/AttractorBench.git   # non-interactive push
#   SAVE_TO_GIT=1 SHUTDOWN=stop nohup bash run_sfm_on_pod.sh > sfm_overnight.log 2>&1 &
#   tail -f sfm_overnight.log
# SHUTDOWN=stop pauses the pod (GPU billing stops, disk kept). SHUTDOWN=terminate destroys the
# pod AND its disk — only safe with SAVE_TO_GIT=1, and a failed push auto-downgrades it to stop.
set -euo pipefail

PORT=8000
export SFM_POST="${SFM_POST:-instruct}"

# Which pretraining-recipe variants to run (space-separated middles of the repo names).
# Default: all 11 released chat variants, controls first.
VARIANTS="${VARIANTS:-baseline_unfiltered baseline_filtered \
unfiltered_e2e_alignment_upsampled unfiltered_e2e_misalignment_upsampled filtered_e2e_alignment_upsampled \
unfiltered_midtrain_alignment_upsampled unfiltered_midtrain_misalignment_upsampled filtered_midtrain_alignment_upsampled \
unfiltered_cpt_alignment_upsampled unfiltered_cpt_misalignment_upsampled filtered_cpt_alignment_upsampled}"

# Concurrency knobs — tuned for 80GB+ GPUs. Lower MAX_NUM_SEQS/WORKERS for a 48GB card.
MAX_MODEL_LEN=16384   # the sfm models' full window (max_position_embeddings=16384)
MAX_NUM_SEQS=24
GPU_MEM_UTIL=0.92
export WORKERS="${WORKERS:-16}"        # parallel conversations the harness drives
# Judge model for stage-2 (provider-prefixed). JUDGE=none skips judging (transcripts + stage-1
# still run) — you can judge later with run_judge.py.
JUDGE="${JUDGE:-openai/gpt-5.4}"
# Delete each variant's ~14GB of weights from the HF cache after its run (results are already on
# disk by then). Keeps peak disk ~14GB across the sweep; set 0 to keep weights for fast re-runs.
CLEANUP_WEIGHTS="${CLEANUP_WEIGHTS:-1}"

# Cache weights on the persistent volume when there is one (RunPod mounts it at /workspace) —
# the root/container disk is often too small for even one 14GB checkpoint.
if [ -z "${HF_HOME:-}" ] && [ -d /workspace ]; then
  export HF_HOME=/workspace/hf
fi
echo "HF cache: ${HF_HOME:-~/.cache/huggingface}"

# Git must NEVER prompt interactively: an overnight run once hung all night on a credential
# prompt at the final push. With this set, git fails instead of asking.
export GIT_TERMINAL_PROMPT=0

# RunPod wipes everything OUTSIDE /workspace when a pod stops (container disk is ephemeral;
# only the volume survives). Refuse to burn hours writing results to a doomed disk.
if [ -n "${RUNPOD_POD_ID:-}" ] && [ -d /workspace ]; then
  case "$PWD" in
    /workspace/*) ;;
    *)
      echo "!! this checkout is at $PWD — on RunPod, only /workspace survives a pod stop."
      echo "   Move the repo there and rerun:"
      echo "     git clone <repo-url> /workspace/AttractorBench && cd /workspace/AttractorBench"
      exit 1 ;;
  esac
fi

# SAVE_TO_GIT preflight: prove the push can work non-interactively BEFORE the run, not at 3am.
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  if ! git push --dry-run >/dev/null 2>&1; then
    echo "!! SAVE_TO_GIT=1 but a non-interactive 'git push --dry-run' failed."
    echo "   Embed a PAT in the remote first:"
    echo "     git remote set-url origin https://<TOKEN>@github.com/timf34/AttractorBench.git"
    exit 1
  fi
  echo "git push preflight OK"
fi

echo "== [1/4] installing deps =="
if [ "${VENV:-0}" = "1" ]; then
  # Clean venv (NO system packages) — see run_on_pod.sh for why (base-image ABI mismatches).
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
  if [ -n "$SITE" ]; then
    rm -rf "$SITE"/flashinfer* "$SITE"/tvm_ffi* "$SITE"/tvm-ffi* "$SITE"/torch_c_dlpack_ext* 2>/dev/null || true
  fi
else
  python -c "import vllm" 2>/dev/null || pip install -q vllm
  python -c "import huggingface_hub" 2>/dev/null || pip install -q huggingface_hub
fi
pip install -q -r requirements.txt   # includes hf_transfer (RunPod presets HF_HUB_ENABLE_HF_TRANSFER=1)

echo "  checking torch can use the GPU..."
if ! python -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null; then
  echo "  !! torch cannot use this GPU — driver/CUDA mismatch."
  echo "     driver: $(nvidia-smi 2>/dev/null | grep -oE 'CUDA Version: [0-9.]+' | head -1)"
  echo "     torch:  $(python -c 'import torch;print(torch.__version__, torch.version.cuda)' 2>/dev/null)"
  echo "     If the driver is < 12.8, re-run with:  VENV=1 CU124=1 bash run_sfm_on_pod.sh"
  exit 1
fi
echo "  torch.cuda OK"

export LOCAL_BASE_URL="http://localhost:$PORT/v1"
export LOCAL_API_KEY="x"               # vLLM serves open; any value

VLLM_PID=""
stop_vllm() {
  [ -n "$VLLM_PID" ] && kill "$VLLM_PID" 2>/dev/null || true
  pkill -f "vllm serve" 2>/dev/null || true
  VLLM_PID=""
  sleep 3
}
trap stop_vllm EXIT

echo "== [2/4]..[4/4] per-variant: download -> serve -> run sweep -> judge -> cleanup =="
for v in $VARIANTS; do
  REPO="geodesic-research/sfm_${v}_${SFM_POST}"
  EXP="sfm_${v}_${SFM_POST}_ai2ai"     # MUST match configs/sfm_ai2ai.py's EXP logic
  echo "================ variant: $v ($REPO) ================"
  stop_vllm

  # Download the full checkpoint up front (like run_on_pod.sh downloads adapters) so a network
  # failure is a clean per-variant skip, not a mysterious vLLM startup death. snapshot_download
  # is resumable and a no-op if the weights are already cached. Prints the local path.
  echo "  downloading weights for $REPO (~14GB, cached under ${HF_HOME:-~/.cache/huggingface})..."
  SNAP_PATH=$(python - "$REPO" <<'PY'
import sys
from huggingface_hub import snapshot_download
print(snapshot_download(sys.argv[1]))
PY
  ) || { echo "  !! weight download FAILED for $REPO — skipping variant"; continue; }
  echo "  weights at $SNAP_PATH"

  # The chat template ships as a separate chat_template.jinja (transformers >= 4.57 layout);
  # the pinned cu124 transformers doesn't read that file, so ALWAYS pass it to vLLM explicitly —
  # harmless where the tokenizer already picks it up, load-bearing where not.
  TEMPLATE_PATH="$SNAP_PATH/chat_template.jinja"
  test -f "$TEMPLATE_PATH" || { echo "  !! $REPO has no chat_template.jinja — skipping variant"; continue; }

  echo "  starting vLLM for $REPO ..."
  vllm serve "$SNAP_PATH" --served-model-name "$REPO" \
    --chat-template "$TEMPLATE_PATH" \
    --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
    --gpu-memory-utilization "$GPU_MEM_UTIL" --port "$PORT" > "vllm_sfm_${v}.log" 2>&1 &
  VLLM_PID=$!

  # Readiness window. 10 min proved too short on network-volume pods: shard reads can run at
  # ~80MB/s (60-73s per 5GB shard), and 6 of 11 variants in the first sweep were killed by this
  # timeout mid-load, not by any real failure. 30 min default; READY_TRIES overrides (x5s each).
  ready=0
  for i in $(seq 1 "${READY_TRIES:-360}"); do
    if curl -sf "http://localhost:$PORT/v1/models" 2>/dev/null | grep -q "$REPO"; then
      ready=1; echo "  vLLM serving $REPO after ~$((i*5))s"; break
    fi
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then echo "  vLLM died for $v — see vllm_sfm_${v}.log"; tail -20 "vllm_sfm_${v}.log"; break; fi
    sleep 5
  done
  if [ "$ready" != 1 ]; then echo "  !! $v not served — skipping"; continue; fi

  echo "  running sweep for $v -> results/$EXP ($WORKERS parallel)..."
  RUN_OK=1
  SFM_VARIANT="$v" python -m attractorbench.runner --config configs/sfm_ai2ai.py \
    || { RUN_OK=0; echo "  (runner errored for $v — continuing)"; }
  # stage-1 deterministic analysis — no API, always run
  for j in results/$EXP/*.json; do
    [ -e "$j" ] || continue
    python -m attractorbench.analysis.deterministic "$j" || true
  done
  if [ "$JUDGE" = "none" ] || [ -z "$JUDGE" ]; then
    echo "  (JUDGE=none -> skipping judge for $v; run run_judge.py later)"
  else
    python run_judge.py "results/$EXP" --judge "$JUDGE" || echo "  (judge errored for $v — transcripts still saved)"
  fi

  # Free the ~14GB before the next variant — but KEEP the weights if the runner errored, so a
  # manual retry of this variant doesn't have to re-download.
  if [ "$CLEANUP_WEIGHTS" = "1" ] && [ "$RUN_OK" = "1" ]; then
    stop_vllm   # never delete weights under a live server
    CACHE_DIR="${HF_HOME:-$HOME/.cache/huggingface}/hub/models--${REPO//\//--}"
    echo "  cleaning up weights: $CACHE_DIR"
    rm -rf "$CACHE_DIR"
  fi
done
stop_vllm

python summarize.py || echo "  (summary errored — per-condition reports are still there)"

echo "== DONE. Per variant: results/sfm_<variant>_${SFM_POST}_ai2ai/*.md + analysis/*__stage2.md =="
echo "== Overall headline summary: results/SUMMARY.md =="

# Optional save-to-git + self-shutdown, same semantics as run_on_pod.sh.
case "${SHUTDOWN:-}" in
  stop)      RP_ACTION="stop" ;;
  terminate) RP_ACTION="remove" ;;
  ""|0)      RP_ACTION="" ;;
  *)         RP_ACTION="stop" ;;   # any other truthy value -> the safe option
esac

# Push results to GitHub before shutting down so a terminate can't lose them. Needs
# non-interactive git auth on the pod (e.g. a PAT in the remote:
#   git remote set-url origin https://<TOKEN>@github.com/timf34/AttractorBench.git ).
# SAFETY: if the push fails, any pending 'terminate' is downgraded to 'stop' so data is never lost.
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  echo "== saving results to git before shutdown =="
  git add -f results/ 2>/dev/null || true
  git commit -q -m "results: sfm run finished $(date -u +%FT%TZ)" || echo "  (nothing new to commit)"
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
