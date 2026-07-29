#!/usr/bin/env bash
# One-shot runner for the Talkie ai2ai experiment on a rented GPU pod.
#
# talkie-1930-13b-it is a CUSTOM architecture (no vLLM): talkie_ai2ai/server.py wraps the
# reference model (github.com/talkie-lm/talkie, cloned + pinned below) behind an
# OpenAI-compatible endpoint with cross-conversation batching. NO KV cache in their runtime —
# generation is slow; the batching is what makes a 45-conversation sweep an overnight job
# instead of a multi-day one.
#
# Recommended GPU: 1x H100/A100-80GB (26GB weights + batched 4k-ctx activations).
#
# Usage (put OPENROUTER_API_KEY in .env for the judge; model is ungated, no HF token needed):
#   git clone <repo> /workspace/AttractorBench && cd /workspace/AttractorBench
#   SAVE_TO_GIT=1 SHUTDOWN=stop VENV=1 bash run_talkie_on_pod.sh 2>&1 | tee talkie_run.log
#   SEEDS=2 TEMPS=1.0 JUDGE=none bash run_talkie_on_pod.sh          # smoke
set -euo pipefail

if [ -f .env ]; then
  set -a
  # shellcheck disable=SC1091
  . ./.env
  set +a
  echo "loaded .env"
fi

PORT=8000
TALKIE_REPO_DIR="${TALKIE_REPO_DIR:-/workspace/talkie}"
TALKIE_COMMIT="${TALKIE_COMMIT:-main}"   # pin a commit hash for strict reproducibility
export WORKERS="${WORKERS:-8}"           # keep == server --max-batch
MAX_BATCH="${MAX_BATCH:-8}"
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"

if [ -z "${HF_HOME:-}" ] && [ -d /workspace ]; then
  export HF_HOME=/workspace/hf
fi
echo "HF cache: ${HF_HOME:-~/.cache/huggingface}"

export GIT_TERMINAL_PROMPT=0
if [ -n "${RUNPOD_POD_ID:-}" ] && [ -d /workspace ]; then
  case "$PWD" in
    /workspace/*) ;;
    *) echo "!! checkout at $PWD — on RunPod only /workspace survives a stop. Clone there."; exit 1 ;;
  esac
fi
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  git push --dry-run origin "HEAD:refs/heads/__preflight_test_$$" >/dev/null 2>&1 || {
    echo "!! SAVE_TO_GIT=1 but a non-interactive push-auth check failed — set a PAT remote."; exit 1; }
  echo "git push preflight OK"
fi

echo "== [1/4] installing deps =="
if [ "${VENV:-0}" = "1" ]; then
  VENV_DIR="${VENV_DIR:-/workspace/talkie_venv}"
  echo "  building venv at $VENV_DIR..."
  python3 -m venv "$VENV_DIR"
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
  pip install -q -U pip
fi
pip install -q torch tiktoken 2>/dev/null || pip install -q torch tiktoken
pip install -q -r requirements.txt

python -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null || {
  echo "  !! torch cannot use this GPU — driver/CUDA mismatch (try VENV=1)."; exit 1; }
echo "  torch.cuda OK"

echo "== [2/4] talkie reference code + weights =="
if [ ! -d "$TALKIE_REPO_DIR" ]; then
  git clone -q https://github.com/talkie-lm/talkie "$TALKIE_REPO_DIR"
fi
git -C "$TALKIE_REPO_DIR" checkout -q "$TALKIE_COMMIT"
pip install -q -e "$TALKIE_REPO_DIR"
echo "  downloading weights (~26GB, cached)..."
python - <<'PY'
from huggingface_hub import hf_hub_download
for f in ("rl-refined.pt", "vocab.txt"):
    print(" ", hf_hub_download("talkie-lm/talkie-1930-13b-it", f))
PY

export LOCAL_BASE_URL="http://localhost:$PORT/v1"
export LOCAL_API_KEY="x"

SERVER_PID=""
stop_server() {
  [ -n "$SERVER_PID" ] && kill "$SERVER_PID" 2>/dev/null || true
  SERVER_PID=""
  sleep 2
}
trap stop_server EXIT

echo "== [3/4] starting server + running sweep =="
python -m talkie_ai2ai.server --port "$PORT" --max-batch "$MAX_BATCH" > talkie_server.log 2>&1 &
SERVER_PID=$!
ready=0
for i in $(seq 1 120); do   # model load ~2-4 min after download
  if curl -sf "http://localhost:$PORT/v1/models" 2>/dev/null | grep -q "talkie"; then
    ready=1; echo "  server up after ~$((i*5))s"; break
  fi
  kill -0 "$SERVER_PID" 2>/dev/null || { echo "  !! server died — see talkie_server.log"; tail -20 talkie_server.log; exit 1; }
  sleep 5
done
[ "$ready" = 1 ] || { echo "!! server not up"; exit 1; }

python -m attractorbench.runner --config configs/talkie_ai2ai.py || echo "  (runner errored — continuing to save what exists)"
for j in results/talkie_ai2ai/*.json; do
  [ -e "$j" ] || continue
  python -m attractorbench.analysis.deterministic "$j" || true
done
stop_server

echo "== [4/4] judge + summary =="
if [ "$JUDGE" != "none" ] && [ -n "$JUDGE" ]; then
  python run_judge.py results/talkie_ai2ai --judge "$JUDGE" || echo "  (judge errored — transcripts saved)"
fi
python summarize.py || true
echo "== DONE: results/talkie_ai2ai =="

case "${SHUTDOWN:-}" in
  stop)      RP_ACTION="stop" ;;
  terminate) RP_ACTION="remove" ;;
  ""|0)      RP_ACTION="" ;;
  *)         RP_ACTION="stop" ;;
esac
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  echo "== saving results to git before shutdown =="
  git config user.email >/dev/null 2>&1 || git config user.email "pod@attractorbench.local"
  git config user.name >/dev/null 2>&1 || git config user.name "AttractorBench Pod"
  git add -f results/ 2>/dev/null || true
  git commit -q -m "results: talkie run finished $(date -u +%FT%TZ)" || echo "  (nothing new to commit)"
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
