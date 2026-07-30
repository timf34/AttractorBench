#!/usr/bin/env bash
# ACTIVATION-CAPPED ai2ai runs (paper §5): same conversations as run_axis_on_pod.sh, but the
# model generates behind assistant_axis_drift/capped_server.py — the authors' released capping
# (25th-percentile caps at their Pareto-optimal layer bands) active at every token.
#
# Question: does holding the model in the Assistant range prevent the ai2ai attractor?
#
# Only qwen-3-32b and llama-3.3-70b (the paper released no gemma capping config).
# GPUs: qwen fits 1x 80GB; llama needs 2x 80GB. HF generation (no vLLM) — slower, hence the
# default scale: temp 1.0 only, 15 seeds, conditions none+helpful.
#
# Projection replay note: our readout layers (qwen 32, llama 40) sit BELOW the capped bands
# (46-53 / 56-71), and replay is teacher-forced on fixed text — so the standard UNCAPPED
# projection pipeline measures capped transcripts correctly; capping shapes the projections
# only through the text it caused the model to write.
#
#   VARIANTS="qwen-3-32b" SAVE_TO_GIT=1 SHUTDOWN=stop VENV=1 bash run_axis_capped_on_pod.sh 2>&1 | tee axis_capped.log
set -euo pipefail

if [ -f .env ]; then
  set -a
  # shellcheck disable=SC1091
  . ./.env
  set +a
  echo "loaded .env"
fi

PORT=8000
VARIANTS="${VARIANTS:-qwen-3-32b llama-3.3-70b}"
CONDITIONS="${CONDITIONS:-none helpful}"
export TEMPS="${TEMPS:-1.0}"
export WORKERS="${WORKERS:-4}"      # keep <= server max_batch
export CAPPED=1
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"

if [ -z "${HF_HOME:-}" ] && [ -d /workspace ]; then
  export HF_HOME=/workspace/hf
fi
export GIT_TERMINAL_PROMPT=0
if [ -n "${RUNPOD_POD_ID:-}" ] && [ -d /workspace ]; then
  case "$PWD" in /workspace/*) ;; *) echo "!! run from /workspace (container disk is wiped on stop)"; exit 1 ;; esac
fi
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  git push --dry-run origin "HEAD:refs/heads/__preflight_test_$$" >/dev/null 2>&1 || {
    echo "!! SAVE_TO_GIT=1 but push-auth check failed — set a PAT remote."; exit 1; }
  echo "git push preflight OK"
fi

echo "== deps =="
if [ "${VENV:-0}" = "1" ]; then
  VENV_DIR="${VENV_DIR:-/workspace/ab_venv}"
  python3 -m venv "$VENV_DIR"
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
  pip install -q -U pip
fi
pip install -q -r requirements.txt -r assistant_axis_drift/requirements.txt
python -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" || { echo "!! no GPU"; exit 1; }
[ -n "${HF_TOKEN:-}" ] || { echo "!! HF_TOKEN not set (gated models)"; exit 1; }

exp_of() {  # MUST match configs/axis_ai2ai.py EXP logic with CAPPED=1
  local slug; slug=$(echo "$1" | tr '.-' '__')
  if [ "$2" = "none" ]; then echo "axis_${slug}_capped_nosys_ai2ai"; else echo "axis_${slug}_capped_ai2ai"; fi
}

export LOCAL_BASE_URL="http://localhost:$PORT/v1"
export LOCAL_API_KEY="x"
SERVER_PID=""
stop_server() { [ -n "$SERVER_PID" ] && kill "$SERVER_PID" 2>/dev/null || true; SERVER_PID=""; sleep 2; }
trap stop_server EXIT

for v in $VARIANTS; do
  echo "================ CAPPED model: $v ================"
  stop_server
  python -m assistant_axis_drift.capped_server --model-key "$v" --port "$PORT" > "capped_server_${v}.log" 2>&1 &
  SERVER_PID=$!
  ready=0
  for i in $(seq 1 240); do   # first run downloads weights
    curl -sf "http://localhost:$PORT/v1/models" 2>/dev/null | grep -q "/" && { ready=1; echo "  server up ~$((i*5))s"; break; }
    kill -0 "$SERVER_PID" 2>/dev/null || { echo "  !! server died"; tail -20 "capped_server_${v}.log"; break; }
    sleep 5
  done
  [ "$ready" = 1 ] || { echo "  !! $v not served — skipping"; continue; }

  for c in $CONDITIONS; do
    EXP=$(exp_of "$v" "$c")
    echo "  generating CAPPED: $v / $c -> results/$EXP ..."
    AXIS_MODEL="$v" AXIS_SYS="$c" CAPPED=1 python -m attractorbench.runner --config configs/axis_ai2ai.py \
      || echo "  (runner errored for $v/$c — continuing)"
    for j in results/$EXP/*.json; do
      [ -e "$j" ] || continue
      python -m attractorbench.analysis.deterministic "$j" || true
    done
  done

  stop_server   # projection needs the VRAM (and uncapped replay is correct — see header)
  DIRS=""
  for c in $CONDITIONS; do d="results/$(exp_of "$v" "$c")"; [ -d "$d" ] && DIRS="$DIRS $d"; done
  if [ -n "$DIRS" ]; then
    # shellcheck disable=SC2086
    python -m assistant_axis_drift.project_transcripts --results-dir $DIRS --model-key "$v" \
      || echo "  (projection errored for $v)"
  fi
  if [ "$JUDGE" != "none" ]; then
    for c in $CONDITIONS; do
      d="results/$(exp_of "$v" "$c")"; [ -d "$d" ] || continue
      python run_judge.py "$d" --judge "$JUDGE" || echo "  (judge errored for $v/$c)"
    done
  fi
done
stop_server

case "${SHUTDOWN:-}" in
  stop) RP_ACTION="stop" ;; terminate) RP_ACTION="remove" ;; ""|0) RP_ACTION="" ;; *) RP_ACTION="stop" ;;
esac
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  git config user.email >/dev/null 2>&1 || git config user.email "pod@attractorbench.local"
  git config user.name >/dev/null 2>&1 || git config user.name "AttractorBench Pod"
  git add -f results/ 2>/dev/null || true
  git commit -q -m "results: capped axis run finished $(date -u +%FT%TZ)" || echo "  (nothing new)"
  git pull --no-rebase --no-edit 2>/dev/null || true
  if git push; then echo "  results pushed"; elif [ "$RP_ACTION" = "remove" ]; then RP_ACTION="stop"; fi
fi
if [ -n "$RP_ACTION" ] && command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ]; then
  runpodctl "$RP_ACTION" pod "$RUNPOD_POD_ID"
fi
