#!/usr/bin/env bash
# ROLE-STEERED ai2ai runs. Same conversations as run_axis_on_pod.sh, but the model generates
# behind state_space/steered_server.py — a direction built from the paper's released per-role
# mean-activation vectors (275 roles: demon, angel, void, vampire, poet, ...) is added at every
# token. Two modes:
#   orthogonal (default) — axis component REMOVED: the causal test of the 1-D account. If the
#     destination basin changes while the (unsteered-replay) a_t trajectory matches unsteered
#     controls, one axis coordinate cannot be the state that picks the basin.
#   STEER_RAW=1 — the role's FULL offset (axis component kept): plain persona steering, "run
#     the self-conversation as the demon". Results dirs get a _raw suffix.
#
# Replay note: projection + dump replay is UNSTEERED teacher-forcing on the steered text, so
# it measures the ENDOGENOUS text-driven state; the injected constant only ever acted through
# the text it caused. That is the right readout for "did a_t stay matched".
#
# HF generation (no vLLM), qwen/gemma 1x 80GB / llama 2x 80GB. Pilot scale by default.
# Loops VARIANTS x STEER_ROLES x STEER_COEFS (server restarted per role/coef; weights cached);
# replay/dump/featurize run ONCE per model over all its steered dirs.
#
#   STEER_ROLE=poet STEER_COEF=1.0 VARIANTS="qwen-3-32b" SAVE_TO_GIT=1 SHUTDOWN=stop VENV=1 \
#     bash run_axis_steer_on_pod.sh 2>&1 | tee axis_steer.log
#   STEER_RAW=1 STEER_ROLES="demon angel void" STEER_COEFS="1.0 2.0" VARIANTS="qwen-3-32b" \
#     SAVE_TO_GIT=1 SHUTDOWN=stop VENV=1 bash run_axis_steer_on_pod.sh 2>&1 | tee axis_steer.log
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
STEER_ROLES="${STEER_ROLES:-$STEER_ROLE}"   # space-separated roles (each = one server start)
STEER_COEFS="${STEER_COEFS:-$STEER_COEF}"   # space-separated coefs (axis-norm units)
STEER_MINUS="${STEER_MINUS:-}"        # optional contrast role (default: mean_role)
STEER_RAW="${STEER_RAW:-0}"           # 1 = full role offset (axis component kept); 0 = v_perp
WITH_CAPPING="${WITH_CAPPING:-0}"     # 1 = also clamp a_t with the released capping
export TEMPS="${TEMPS:-1.0}"
export SEEDS="${SEEDS:-10}"
export WORKERS="${WORKERS:-4}"        # keep <= server max_batch
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"

# results tag, e.g. poet_c10 (orthogonal, coef 1.0), demon_c20_raw, poetminusengineer_c10_capped
steer_tag_of() {  # $1 role, $2 coef
  local coef_tag tag; coef_tag=$(echo "$2" | tr -d '.')
  tag="$1"
  [ -n "$STEER_MINUS" ] && tag="${tag}minus${STEER_MINUS}"
  tag="${tag}_c${coef_tag}"
  [ "$STEER_RAW" = "1" ] && tag="${tag}_raw"
  [ "$WITH_CAPPING" = "1" ] && tag="${tag}_capped"
  echo "$tag"
}
for _r in $STEER_ROLES; do for _c in $STEER_COEFS; do
  _t=$(steer_tag_of "$_r" "$_c")
  [[ "$_t" =~ ^[A-Za-z0-9_]+$ ]] || { echo "!! steer tag $_t not alnum/underscore (role/coef chars?)"; exit 1; }
done; done

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
  echo "================ STEERED model: $v (roles: $STEER_ROLES; coefs: $STEER_COEFS; raw=$STEER_RAW) ================"
  stop_server
  echo "  downloading weights for $v ..."
  python - "$v" <<'PY' || { echo "  !! weight download failed for $v — skipping"; continue; }
import sys
from huggingface_hub import snapshot_download
from assistant_axis_experiments.axes import AXIS_MODELS
print(" ", snapshot_download(AXIS_MODELS[sys.argv[1]]))
PY
  DIRS=""   # every steered results dir produced for this model (replayed once, below)
  for role in $STEER_ROLES; do for coef in $STEER_COEFS; do
    STEER_TAG=$(steer_tag_of "$role" "$coef")
    export STEER="$STEER_TAG"
    echo "  ---- $v: role=$role coef=$coef -> tag $STEER_TAG ----"
    stop_server
    STEER_ARGS=(--model-key "$v" --role "$role" --coef "$coef" --port "$PORT")
    [ -n "$STEER_MINUS" ] && STEER_ARGS+=(--minus-role "$STEER_MINUS")
    [ "$STEER_RAW" = "1" ] && STEER_ARGS+=(--raw)
    [ "$WITH_CAPPING" = "1" ] && STEER_ARGS+=(--with-capping)
    python -u -m assistant_axis_experiments.state_space.steered_server "${STEER_ARGS[@]}" \
      > "steered_server_${v}_${STEER_TAG}.log" 2>&1 &
    SERVER_PID=$!
    ready=0
    for i in $(seq 1 240); do
      curl -sf "http://localhost:$PORT/v1/models" 2>/dev/null | grep -q "/" && { ready=1; echo "  server up ~$((i*5))s"; break; }
      kill -0 "$SERVER_PID" 2>/dev/null || { echo "  !! server died"; tail -20 "steered_server_${v}_${STEER_TAG}.log"; break; }
      sleep 5
    done
    [ "$ready" = 1 ] || { echo "  !! $v/$STEER_TAG not served — skipping"; continue; }
    grep -E "^  L[0-9]+:" "steered_server_${v}_${STEER_TAG}.log" || true   # per-layer magnitudes

    for c in $CONDITIONS; do
      EXP=$(exp_of "$v" "$c")
      echo "  generating STEERED: $v / $c -> results/$EXP ..."
      AXIS_MODEL="$v" AXIS_SYS="$c" python -m attractorbench.runner --config configs/axis_ai2ai.py \
        || echo "  (runner errored for $v/$c — continuing)"
      for j in results/$EXP/*.json; do
        [ -e "$j" ] || continue
        python -m attractorbench.analysis.deterministic "$j" || true
      done
      [ -d "results/$EXP" ] && DIRS="$DIRS results/$EXP"
    done
  done; done

  stop_server   # replay needs the VRAM; unsteered replay is the intended readout (see header)
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
    for d in $DIRS; do
      python run_judge.py "$d" --judge "$JUDGE" || echo "  (judge errored for $d)"
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
  git add -f results/ 2>/dev/null || true   # includes *__turn_acts.npz — pods are ephemeral
  git commit -q -m "results: steered axis run (roles: $STEER_ROLES; coefs: $STEER_COEFS; raw=$STEER_RAW) finished $(date -u +%FT%TZ)" || echo "  (nothing new)"
  git pull --no-rebase --no-edit 2>/dev/null || true
  if git push; then echo "  results pushed"; elif [ "$RP_ACTION" = "remove" ]; then RP_ACTION="stop"; fi
fi
if [ -n "$RP_ACTION" ] && command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ]; then
  runpodctl "$RP_ACTION" pod "$RUNPOD_POD_ID"
fi
