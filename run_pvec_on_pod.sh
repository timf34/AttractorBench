#!/usr/bin/env bash
# One-shot: run the AI-to-AI self-conversation with PERSONA-VECTOR steering on a GPU pod.
#
# Unlike run_on_pod.sh (which serves LoRA personas via vLLM), persona-vector steering needs an
# activation hook, so we serve the base model through persona_vector_steering.serve (an OpenAI-
# compatible endpoint) and drive the SAME harness/judge/summarize against it. One server handles
# every trait/coef/layer — the condition is encoded in the model name (pvec DSL).
#
# Requires: OPENAI/OpenRouter key for the judge; HF_TOKEN if the base model is gated (unsloth isn't).
# The persona vectors are pulled from the persona_vectors repo (they're committed there).
#
# Usage:
#   git clone https://github.com/timf34/AttractorBench.git && cd AttractorBench
#   cp .env.example .env && nano .env            # judge key etc.
#   bash run_pvec_on_pod.sh
#   # tuned values:   PVEC_COEF=3 PVEC_LAYER=20 bash run_pvec_on_pod.sh
#   # subset:         TRAITS="goodness sarcasm" bash run_pvec_on_pod.sh
#   # auto-stop:      SHUTDOWN=stop SAVE_TO_GIT=1 bash run_pvec_on_pod.sh
set -euo pipefail

PORT="${PORT:-8000}"
PVEC_COEF="${PVEC_COEF:-2}"
PVEC_LAYER="${PVEC_LAYER:-16}"
JUDGE="${JUDGE:-openai/gpt-5.4}"
# "base" first = control, then the steered traits. Override with TRAITS="...".
TRAITS="${TRAITS:-base goodness loving humor impulsiveness mathematical nonchalance poeticism remorse sarcasm sycophancy honesty sincerity}"
export PVEC_COEF PVEC_LAYER
export WORKERS="${WORKERS:-2}"        # steering serializes on the server; keep low

echo "== [1/4] deps =="
pip install -q -r requirements.txt
python -c "import fastapi, uvicorn" 2>/dev/null || pip install -q fastapi uvicorn
python -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" || { echo "!! no CUDA"; exit 1; }

echo "== [2/4] fetch persona vectors =="
# The vectors live in the persona_vectors repo (committed). config.py's PVEC_DIR default points here.
if [ ! -d persona_vectors_repo ]; then
  git clone --depth 1 https://github.com/timf34/persona_vectors.git persona_vectors_repo
fi
VEC_DIR="persona_vectors_repo/persona_vectors/Meta-Llama-3.1-8B-Instruct"
ls "$VEC_DIR"/*_response_avg_diff.pt >/dev/null 2>&1 || { echo "!! no vectors in $VEC_DIR"; exit 1; }
echo "  found $(ls "$VEC_DIR"/*_response_avg_diff.pt | wc -l) persona vectors"
export PVEC_DIR="$(pwd)/$VEC_DIR"   # tell the server exactly where the vectors are (don't rely on cwd)

echo "== [3/4] start persona-vector server =="
python -m persona_vector_steering.serve --port "$PORT" > pvec_serve.log 2>&1 &
SERVE_PID=$!
stop_serve() { kill "$SERVE_PID" 2>/dev/null || true; }
trap stop_serve EXIT

ready=0
for i in $(seq 1 120); do
  if curl -sf "http://localhost:$PORT/v1/models" >/dev/null 2>&1; then ready=1; echo "  server up after ~$((i*3))s"; break; fi
  if ! kill -0 "$SERVE_PID" 2>/dev/null; then echo "  server died — see pvec_serve.log"; tail -30 pvec_serve.log; exit 1; fi
  sleep 3
done
[ "$ready" = 1 ] || { echo "!! server not ready"; tail -30 pvec_serve.log; exit 1; }

export LOCAL_BASE_URL="http://localhost:$PORT/v1"
export LOCAL_API_KEY="x"

echo "== [4/4] run conversations (coef=$PVEC_COEF layer=$PVEC_LAYER) =="
for t in $TRAITS; do
  echo "================ $t ================"
  if [ "$t" = "base" ]; then EXP="base_pvec_ai2ai"; else EXP="${t}_pvec_c${PVEC_COEF}_l${PVEC_LAYER}_ai2ai"; fi
  TRAIT="$t" python -m attractorbench.runner --config configs/persona_vector_ai2ai.py \
    || { echo "  (runner errored for $t — continuing)"; continue; }
  for j in results/"$EXP"/*.json; do [ -e "$j" ] || continue; python -m attractorbench.analysis.deterministic "$j" || true; done
  if [ "$JUDGE" != "none" ] && [ -n "$JUDGE" ]; then
    python run_judge.py "results/$EXP" --judge "$JUDGE" || echo "  (judge errored for $t)"
  fi
done
stop_serve
python summarize.py || echo "  (summary errored — per-condition reports still there)"
echo "== DONE. results/<trait>_pvec_c${PVEC_COEF}_l${PVEC_LAYER}_ai2ai/ + base_pvec_ai2ai/ =="

# Optional self-shutdown (mirror run_on_pod.sh).
case "${SHUTDOWN:-}" in stop) RP=stop;; terminate) RP=remove;; ""|0) RP="";; *) RP=stop;; esac
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  git add -f results/ 2>/dev/null || true
  git commit -q -m "pvec results: $(date -u +%FT%TZ)" || echo "  (nothing to commit)"
  git pull --no-rebase --no-edit 2>/dev/null || true
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
