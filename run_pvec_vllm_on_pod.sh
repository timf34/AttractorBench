#!/usr/bin/env bash
# FAST persona-vector sweep: baked checkpoints + stock vLLM (continuous batching), instead of the
# serialized HF hook server (run_pvec_on_pod.sh). The steering intervention
# `resid[layer] += coef*vec[layer]` at block layer-1's output is a constant additive bias on that
# block's mlp.down_proj (block_out = resid_in + attn_out + (mlp_out + b)), so `persona_vector_steering
# .bake` folds it into a checkpoint variant (shards symlinked, ~2 MB of new bias tensors) and vLLM
# serves it exactly like any other model — full paged-attention batching across the whole trait's
# seeds*temps conversations at once (~30x the serialized hook server; see persona_vector_steering/
# HANDOFF.md).
#
# One vLLM instance per trait (restarting between traits, like run_on_pod.sh restarts between
# personas): "base" serves the raw base model; every other trait serves its baked variant dir under
# BAKE_DIR. The harness/judge/summarize are unchanged — only the served model differs.
#
# The old hook-server path (run_pvec_on_pod.sh + persona_vector_steering.serve) remains for
# interactive use (chat.py) and as the numerical reference implementation; see
# persona_vector_steering/README.md.
#
# Usage:
#   git clone https://github.com/timf34/AttractorBench.git && cd AttractorBench
#   cp .env.example .env && nano .env            # judge key etc.
#   bash run_pvec_vllm_on_pod.sh
#   # tuned values:   PVEC_COEF=3 PVEC_LAYER=20 bash run_pvec_vllm_on_pod.sh
#   # subset:         TRAITS="goodness sarcasm" bash run_pvec_vllm_on_pod.sh
#   # auto-stop:      SHUTDOWN=stop SAVE_TO_GIT=1 bash run_pvec_vllm_on_pod.sh
set -euo pipefail
export HF_HOME="${HF_HOME:-/workspace/.cache/huggingface}"

PORT="${PORT:-8000}"
PVEC_COEF="${PVEC_COEF:-2}"
PVEC_LAYER="${PVEC_LAYER:-16}"
JUDGE="${JUDGE:-openai/gpt-5.4}"
BAKE_DIR="${BAKE_DIR:-/workspace/pvec_baked}"
BASE_MODEL="${BASE_MODEL:-unsloth/Meta-Llama-3.1-8B-Instruct}"
# "base" first = control, then the steered traits. Override with TRAITS="...".
TRAITS="${TRAITS:-base goodness loving humor impulsiveness mathematical nonchalance poeticism remorse sarcasm sycophancy honesty sincerity}"
export PVEC_COEF PVEC_LAYER BASE_MODEL

# Concurrency knobs — tuned for 80GB+ GPUs (H100/H200/A100 80GB). Lower for a 48GB card.
MAX_MODEL_LEN="${MAX_MODEL_LEN:-32768}"
MAX_NUM_SEQS="${MAX_NUM_SEQS:-64}"
GPU_MEM_UTIL="${GPU_MEM_UTIL:-0.92}"
# vLLM continuous-batches everything in flight, so all of a trait's seeds*temps conversations can run
# concurrently — unlike the hook server, this does NOT serialize. Default 45 == the full seeds*temps
# matrix for one trait (see configs/persona_vector_ai2ai.py).
export WORKERS="${WORKERS:-45}"

echo "== [1/5] deps =="
pip install -q -r requirements.txt
python -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" || { echo "!! no CUDA"; exit 1; }
command -v vllm >/dev/null 2>&1 || { echo "!! vllm CLI not found on PATH (pip install vllm)"; exit 1; }
echo "  vllm version: $(python -c 'import vllm; print(vllm.__version__)' 2>/dev/null)"

echo "== [2/5] fetch persona vectors =="
# The vectors live in the persona_vectors repo (committed). config.py's PVEC_DIR default points here.
# bake.py needs them too (it reads config.vector_path(trait)).
if [ ! -d persona_vectors_repo ]; then
  git clone --depth 1 https://github.com/timf34/persona_vectors.git persona_vectors_repo
fi
VEC_DIR="persona_vectors_repo/persona_vectors/Meta-Llama-3.1-8B-Instruct"
ls "$VEC_DIR"/*_response_avg_diff.pt >/dev/null 2>&1 || { echo "!! no vectors in $VEC_DIR"; exit 1; }
echo "  found $(ls "$VEC_DIR"/*_response_avg_diff.pt | wc -l) persona vectors"
export PVEC_DIR="$(pwd)/$VEC_DIR"   # tell bake.py exactly where the vectors are (don't rely on cwd)

export LOCAL_API_KEY="x"               # vLLM serves open; any value

VLLM_PID=""
stop_vllm() {
  [ -n "$VLLM_PID" ] && kill "$VLLM_PID" 2>/dev/null || true
  pkill -f "vllm serve" 2>/dev/null || true   # also clear any stale server holding the port
  VLLM_PID=""
  sleep 3
}
trap stop_vllm EXIT

echo "== [3/5] + [4/5] + [5/5] per-trait: bake -> serve with vLLM -> run sweep -> judge =="
for t in $TRAITS; do
  echo "================ trait: $t ================"
  stop_vllm   # clean slate; never inherit a previous trait's server

  if [ "$t" = "base" ]; then
    MODEL_PATH="$BASE_MODEL"
    SERVED="base"
    EXP="base_pvec_ai2ai"
  else
    echo "  baking $t (coef=$PVEC_COEF layer=$PVEC_LAYER) ..."
    if ! MODEL_PATH="$(python -m persona_vector_steering.bake --trait "$t" --coef "$PVEC_COEF" --layer "$PVEC_LAYER" --out-dir "$BAKE_DIR" | tail -1)"; then
      echo "  !! bake failed for $t — skipping"; continue
    fi
    SERVED="pvec:$t:$PVEC_COEF:$PVEC_LAYER"
    EXP="${t}_pvec_c${PVEC_COEF}_l${PVEC_LAYER}_ai2ai"
  fi

  echo "  starting vLLM for '$t' (model dir: $MODEL_PATH, served as '$SERVED') ..."
  vllm serve "$MODEL_PATH" --served-model-name "$SERVED" \
    --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
    --gpu-memory-utilization "$GPU_MEM_UTIL" --port "$PORT" > "vllm_pvec_$t.log" 2>&1 &
  VLLM_PID=$!

  ready=0
  for i in $(seq 1 120); do   # ~10 min: model load + CUDA graph capture
    if curl -sf "http://localhost:$PORT/v1/models" 2>/dev/null | grep -q "\"$SERVED\""; then
      ready=1; echo "  vLLM serving '$SERVED' after ~$((i*5))s"; break
    fi
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then echo "  vLLM died for $t — see vllm_pvec_$t.log"; tail -20 "vllm_pvec_$t.log"; break; fi
    sleep 5
  done
  if [ "$ready" != 1 ]; then echo "  !! $t not served — skipping"; continue; fi

  export LOCAL_BASE_URL="http://localhost:$PORT/v1"
  echo "  running sweep for $t -> results/$EXP ($WORKERS parallel)..."
  TRAIT="$t" python -m attractorbench.runner --config configs/persona_vector_ai2ai.py \
    || { echo "  (runner errored for $t — continuing)"; continue; }
  # stage-1 deterministic analysis (word/phrase/emoji frequency, convergence) — no API, always run
  for j in results/"$EXP"/*.json; do
    [ -e "$j" ] || continue
    python -m attractorbench.analysis.deterministic "$j" || true
  done
  if [ "$JUDGE" = "none" ] || [ -z "$JUDGE" ]; then
    echo "  (JUDGE=none -> skipping judge for $t; run run_judge.py later)"
  else
    python run_judge.py "results/$EXP" --judge "$JUDGE" || echo "  (judge errored for $t — transcripts still saved)"
  fi
done
stop_vllm

# One-page headline summary across every condition (deterministic; reads existing reports).
python summarize.py || echo "  (summary errored — per-condition reports are still there)"

echo "== DONE. results/<trait>_pvec_c${PVEC_COEF}_l${PVEC_LAYER}_ai2ai/ + base_pvec_ai2ai/ =="

# Optional self-shutdown so an unattended overnight run doesn't keep billing after it finishes.
# Requires runpodctl authed with your RunPod API key (one-time: runpodctl config --apiKey <KEY>);
# RUNPOD_POD_ID is set automatically on every RunPod pod.
#   SHUTDOWN=stop       -> PAUSE the pod: GPU billing stops, disk + results KEPT, restart later.
#   SHUTDOWN=terminate  -> DESTROY the pod: no billing, but DELETES the disk/results unless they're
#                          on a persistent network volume. Make sure results are saved off-pod first.
case "${SHUTDOWN:-}" in stop) RP=stop;; terminate) RP=remove;; ""|0) RP="";; *) RP=stop;; esac
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  git add -f results/ 2>/dev/null || true
  git commit -q -m "pvec results: $(date -u +%FT%TZ)" || echo "  (nothing to commit)"
  git pull --no-rebase --no-edit 2>/dev/null || true   # reconcile with remote first so push isn't rejected
  git push || { [ "$RP" = "remove" ] && { echo "  push failed -> downgrade terminate to stop"; RP=stop; }; }
fi
if [ -n "$RP" ]; then
  # Auth runpodctl from RUNPOD_API_KEY (env or .env) so self-shutdown works unattended.
  KEY="${RUNPOD_API_KEY:-$(grep -E '^RUNPOD_API_KEY=' .env 2>/dev/null | cut -d= -f2- | tr -d "\"'" | xargs)}"
  if command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ]; then
    [ -n "$KEY" ] && runpodctl config --apiKey "$KEY" >/dev/null 2>&1 || true
    echo "== runpodctl $RP pod $RUNPOD_POD_ID =="; runpodctl "$RP" pod "$RUNPOD_POD_ID"
  else
    echo "  !! cannot self-shutdown (runpodctl missing or RUNPOD_POD_ID unset) — pod left running."
  fi
fi
