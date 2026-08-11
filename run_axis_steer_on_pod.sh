#!/usr/bin/env bash
# ORTHOGONAL-STEER ai2ai runs: the causal test of the 1-D account. Same conversations as
# run_axis_on_pod.sh, but the model generates behind state_space/steered_server.py — a
# persona direction with its Assistant-Axis component REMOVED is added at every token.
# If the destination basin changes while the (unsteered-replay) a_t trajectory matches
# unsteered controls, one axis coordinate cannot be the state that picks the basin.
#
# Replay note: projection + dump replay is UNSTEERED teacher-forcing on the steered text, so
# it measures the ENDOGENOUS text-driven state; the injected constant only ever acted through
# the text it caused. That is the right readout for "did a_t stay matched".
#
# HF generation (no vLLM), qwen 1x 80GB / llama 2x 80GB. Pilot scale by default.
#
#   STEER_ROLE=poet STEER_COEF=1.0 VARIANTS="qwen-3-32b" SAVE_TO_GIT=1 SHUTDOWN=stop VENV=1 \
#     bash run_axis_steer_on_pod.sh 2>&1 | tee axis_steer.log
set -euo pipefail

if [ -f .env ]; then
  set -a
  # shellcheck disable=SC1091
  . ./.env
  set +a
  echo "loaded .env"
fi

PORT=8000
VARIANTS="${VARIANTS:-qwen-3-32b}"
CONDITIONS="${CONDITIONS:-none}"
STEER_ROLE="${STEER_ROLE:-poet}"
STEER_COEF="${STEER_COEF:-1.0}"
STEER_MINUS="${STEER_MINUS:-}"        # optional contrast role (default: mean_role)
WITH_CAPPING="${WITH_CAPPING:-0}"     # 1 = also clamp a_t with the released capping
export TEMPS="${TEMPS:-1.0}"
export SEEDS="${SEEDS:-10}"
export WORKERS="${WORKERS:-4}"        # keep <= server max_batch
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"

# results tag, e.g. poet_c10 (coef 1.0), poet_c05 (0.5), poetminusengineer_c10_capped
_coef_tag=$(echo "$STEER_COEF" | tr -d '.')
STEER_TAG="$STEER_ROLE"
[ -n "$STEER_MINUS" ] && STEER_TAG="${STEER_TAG}minus${STEER_MINUS}"
STEER_TAG="${STEER_TAG}_c${_coef_tag}"
[ "$WITH_CAPPING" = "1" ] && STEER_TAG="${STEER_TAG}_capped"
export STEER="$STEER_TAG"

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
pip install -q -r requirements.txt -r assistant_axis_experiments/requirements.txt
python -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" || { echo "!! no GPU"; exit 1; }
[ -n "${HF_TOKEN:-}" ] || { echo "!! HF_TOKEN not set (gated models)"; exit 1; }

exp_of() {  # MUST match configs/axis_ai2ai.py EXP logic with STEER set
  local slug; slug=$(echo "$1" | tr '.-' '__')
  if [ "$2" = "none" ]; then echo "axis_${slug}_steer_${STEER_TAG}_nosys_ai2ai"; else echo "axis_${slug}_steer_${STEER_TAG}_ai2ai"; fi
}

export LOCAL_BASE_URL="http://localhost:$PORT/v1"
export LOCAL_API_KEY="x"
SERVER_PID=""
stop_server() {
  [ -n "$SERVER_PID" ] && kill "$SERVER_PID" 2>/dev/null || true
  pkill -f "state_space.steered_server" 2>/dev/null || true
  SERVER_PID=""
  sleep 2
}
trap stop_server EXIT

for v in $VARIANTS; do
  echo "================ STEERED model: $v (tag $STEER_TAG) ================"
  stop_server
  echo "  downloading weights for $v ..."
  python - "$v" <<'PY' || { echo "  !! weight download failed for $v — skipping"; continue; }
import sys
from huggingface_hub import snapshot_download
from assistant_axis_experiments.axes import AXIS_MODELS
print(" ", snapshot_download(AXIS_MODELS[sys.argv[1]]))
PY
  STEER_ARGS=(--model-key "$v" --role "$STEER_ROLE" --coef "$STEER_COEF" --port "$PORT")
  [ -n "$STEER_MINUS" ] && STEER_ARGS+=(--minus-role "$STEER_MINUS")
  [ "$WITH_CAPPING" = "1" ] && STEER_ARGS+=(--with-capping)
  python -m assistant_axis_experiments.state_space.steered_server "${STEER_ARGS[@]}" \
    > "steered_server_${v}.log" 2>&1 &
  SERVER_PID=$!
  ready=0
  for i in $(seq 1 240); do
    curl -sf "http://localhost:$PORT/v1/models" 2>/dev/null | grep -q "/" && { ready=1; echo "  server up ~$((i*5))s"; break; }
    kill -0 "$SERVER_PID" 2>/dev/null || { echo "  !! server died"; tail -20 "steered_server_${v}.log"; break; }
    sleep 5
  done
  [ "$ready" = 1 ] || { echo "  !! $v not served — skipping"; continue; }

  for c in $CONDITIONS; do
    EXP=$(exp_of "$v" "$c")
    echo "  generating STEERED: $v / $c -> results/$EXP ..."
    AXIS_MODEL="$v" AXIS_SYS="$c" python -m attractorbench.runner --config configs/axis_ai2ai.py \
      || echo "  (runner errored for $v/$c — continuing)"
    for j in results/$EXP/*.json; do
      [ -e "$j" ] || continue
      python -m attractorbench.analysis.deterministic "$j" || true
    done
  done

  stop_server   # replay needs the VRAM; unsteered replay is the intended readout (see header)
  DIRS=""
  for c in $CONDITIONS; do d="results/$(exp_of "$v" "$c")"; [ -d "$d" ] && DIRS="$DIRS $d"; done
  if [ -n "$DIRS" ]; then
    # shellcheck disable=SC2086
    python -m assistant_axis_experiments.project_transcripts --results-dir $DIRS --model-key "$v" \
      || echo "  (projection errored for $v)"
    # shellcheck disable=SC2086
    python -m assistant_axis_experiments.state_space.dump_activations --results-dir $DIRS --model-key "$v" \
      || echo "  (dump errored for $v)"
    # shellcheck disable=SC2086
    python -m assistant_axis_experiments.state_space.featurize --results-dir $DIRS --model-key "$v" \
      || echo "  (featurize errored for $v)"
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
  git reset -q results/*/analysis/*__turn_acts.npz 2>/dev/null || true   # vectors stay pod-side
  git commit -q -m "results: steered axis run ($STEER_TAG) finished $(date -u +%FT%TZ)" || echo "  (nothing new)"
  git pull --no-rebase --no-edit 2>/dev/null || true
  if git push; then echo "  results pushed"; elif [ "$RP_ACTION" = "remove" ]; then RP_ACTION="stop"; fi
fi
if [ -n "$RP_ACTION" ] && command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ]; then
  runpodctl "$RP_ACTION" pod "$RUNPOD_POD_ID"
fi
