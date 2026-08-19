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
# Two generation ENGINEs (same harness, same results layout, same replay/judge afterwards):
#   ENGINE=hf        (default) state_space/steered_server.py — HF generate + forward hooks,
#                    ~100 tok/s aggregate for a 32B model, 16k window (runs end ~turn 22).
#   ENGINE=easysteer EasySteer's vLLM fork (ZJU-REAL/EasySteer-vllm-v1 overlay on vllm==0.26.0,
#                    installed in ES_VENV by es_install.sh) — `vllm serve --enable-steer-vector
#                    --steer-algorithms direct --steering-config <spec.json>`; direction GGUF +
#                    spec from state_space/export_steer_gguf.py (scale == our coef, same hook
#                    point: decoder-layer output). ~5-10x faster, 40k window (full 30 turns).
# OPENER=goodness|agnostic (see configs/axis_ai2ai.py; agnostic = no "AI" words — use it when
#   steering non-AI personas so the opener doesn't pre-load the AI identity). Inserts _agnostic.
# STEER_ROLES may include `none` = UNSTEERED CONTROL on the identical engine (tag `unsteered`).
# Loops VARIANTS x STEER_ROLES x STEER_COEFS (server restarted per role/coef; weights cached);
# replay/dump/featurize run ONCE per model over all its dirs (always the HF venv, unsteered).
#
#   STEER_ROLE=poet STEER_COEF=1.0 VARIANTS="qwen-3-32b" SAVE_TO_GIT=1 SHUTDOWN=stop VENV=1 \
#     bash run_axis_steer_on_pod.sh 2>&1 | tee axis_steer.log
#   ENGINE=easysteer OPENER=agnostic STEER_RAW=1 STEER_ROLES="none oracle eldritch demon angel void vampire" \
#     STEER_COEFS="6.0" VARIANTS="qwen-3-32b" SAVE_TO_GIT=1 SHUTDOWN=stop VENV=1 \
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
STEER_ROLES="${STEER_ROLES:-$STEER_ROLE}"   # space-separated roles (each = one server start)
STEER_COEFS="${STEER_COEFS:-$STEER_COEF}"   # space-separated coefs (axis-norm units)
STEER_MINUS="${STEER_MINUS:-}"        # optional contrast role (default: mean_role)
STEER_RAW="${STEER_RAW:-0}"           # 1 = full role offset (axis component kept); 0 = v_perp
WITH_CAPPING="${WITH_CAPPING:-0}"     # 1 = also clamp a_t with the released capping (hf engine only)
ENGINE="${ENGINE:-hf}"                # hf | easysteer
ES_VENV="${ES_VENV:-/workspace/es_venv}"   # EasySteer venv (es_install.sh); easysteer engine only
export OPENER="${OPENER:-goodness}"   # goodness | agnostic (read by configs/axis_ai2ai.py)
export TEMPS="${TEMPS:-1.0}"
export SEEDS="${SEEDS:-10}"
if [ "$ENGINE" = "easysteer" ]; then
  export WORKERS="${WORKERS:-10}"     # vLLM batches continuously; harness-side parallel runs
  MAX_NUM_SEQS="${MAX_NUM_SEQS:-24}"; GPU_MEM_UTIL="${GPU_MEM_UTIL:-0.95}"   # 0.92 leaves <10GiB KV for qwen@40960 with steer buffers
  [ -x "$ES_VENV/bin/vllm" ] || { echo "!! ENGINE=easysteer but $ES_VENV/bin/vllm missing (run es_install.sh)"; exit 1; }
else
  export WORKERS="${WORKERS:-4}"      # keep <= server max_batch
fi
case "$ENGINE" in hf|easysteer) ;; *) echo "!! ENGINE must be hf or easysteer"; exit 1 ;; esac
case "$OPENER" in goodness|agnostic) ;; *) echo "!! OPENER must be goodness or agnostic"; exit 1 ;; esac
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"

# results tag, e.g. poet_c10 (orthogonal, coef 1.0), demon_c20_raw, poetminusengineer_c10_capped
steer_tag_of() {  # $1 role, $2 coef
  local coef_tag tag; coef_tag=$(echo "$2" | tr -d '.')
  if [ "$1" = "none" ]; then echo "unsteered"; return; fi   # unsteered control, same engine
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

exp_of() {  # MUST match configs/axis_ai2ai.py EXP logic with STEER (+OPENER) set
  local slug ag; slug=$(echo "$1" | tr '.-' '__'); ag=""
  [ "$OPENER" = "agnostic" ] && ag="_agnostic"
  if [ "$2" = "none" ]; then echo "axis_${slug}${ag}_steer_${STEER_TAG}_nosys_ai2ai"; else echo "axis_${slug}${ag}_steer_${STEER_TAG}_ai2ai"; fi
}

export LOCAL_BASE_URL="http://localhost:$PORT/v1"
export LOCAL_API_KEY="x"
SERVER_PID=""
stop_server() {
  [ -n "$SERVER_PID" ] && kill "$SERVER_PID" 2>/dev/null || true
  pkill -f "state_space.steered_server" 2>/dev/null || true
  pkill -f "vllm serve" 2>/dev/null || true
  SERVER_PID=""
  sleep 2
  # vLLM's EngineCore subprocess can outlive the parent; wait for the GPU to actually free
  for _ in $(seq 1 30); do
    used=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits 2>/dev/null | head -1 | tr -d ' ')
    [ -z "$used" ] || [ "$used" -lt 2000 ] && break
    pkill -9 -f "vllm" 2>/dev/null || true; sleep 4
  done
}
trap stop_server EXIT

for v in $VARIANTS; do
  echo "================ STEERED model: $v (roles: $STEER_ROLES; coefs: $STEER_COEFS; raw=$STEER_RAW) ================"
  stop_server
  echo "  downloading weights for $v ..."
  SNAP_PATH=$(python - "$v" <<'PY'
import sys
from huggingface_hub import snapshot_download
from assistant_axis_experiments.axes import AXIS_MODELS
print(snapshot_download(AXIS_MODELS[sys.argv[1]]))
PY
  ) || { echo "  !! weight download failed for $v — skipping"; continue; }
  echo "  $SNAP_PATH"
  HF_REPO=$(python -c "from assistant_axis_experiments.axes import AXIS_MODELS; print(AXIS_MODELS['$v'])")
  if [ "$ENGINE" = "easysteer" ]; then
    # vLLM serving recipe from run_axis_on_pod.sh: qwen thinking pinned off at template level,
    # gemma needs FA2 (softcap) + system-fold template; context = the model's serve length there.
    TEMPLATE_FLAG=""; unset VLLM_FLASH_ATTN_VERSION || true
    case "$v" in
      qwen-3-32b)
        python - "$HF_REPO" <<'PY'
import sys
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained(sys.argv[1])
with open("qwen3_no_thinking.jinja", "w") as f:
    f.write("{%- set enable_thinking = false -%}" + tok.chat_template)
print("  wrote qwen3_no_thinking.jinja (enable_thinking pinned false)")
PY
        TEMPLATE_FLAG="--chat-template qwen3_no_thinking.jinja"; MAX_MODEL_LEN="${MAX_MODEL_LEN:-40960}" ;;
      gemma-2-27b)
        TEMPLATE_FLAG="--chat-template assistant_axis_experiments/templates/gemma2_system_fold.jinja"
        export VLLM_FLASH_ATTN_VERSION=2; MAX_MODEL_LEN="${MAX_MODEL_LEN:-8192}" ;;
      llama-3.3-70b) MAX_MODEL_LEN="${MAX_MODEL_LEN:-16384}" ;;
    esac
    NGPU=$(nvidia-smi -L 2>/dev/null | wc -l | tr -d ' ')
  fi
  DIRS=""   # every results dir produced for this model (replayed once, below)
  for role in $STEER_ROLES; do for coef in $STEER_COEFS; do
    # the unsteered control is coef-independent: run it once (with the first coef) only
    [ "$role" = "none" ] && [ "$coef" != "${STEER_COEFS%% *}" ] && continue
    STEER_TAG=$(steer_tag_of "$role" "$coef")
    export STEER="$STEER_TAG"
    echo "  ---- $v: role=$role coef=$coef engine=$ENGINE opener=$OPENER -> tag $STEER_TAG ----"
    stop_server
    if [ "$ENGINE" = "easysteer" ]; then
      STEER_FLAGS=()
      if [ "$role" != "none" ]; then
        mkdir -p steer_vectors
        GG="steer_vectors/${v}__${STEER_TAG}.gguf"; SPEC="steer_vectors/${v}__${STEER_TAG}.json"
        EXP_ARGS=(--model-key "$v" --role "$role" --coef "$coef" --out "$GG" --spec-out "$SPEC")
        [ -n "$STEER_MINUS" ] && EXP_ARGS+=(--minus-role "$STEER_MINUS")
        [ "$STEER_RAW" = "1" ] && EXP_ARGS+=(--raw)
        python -m assistant_axis_experiments.state_space.export_steer_gguf "${EXP_ARGS[@]}" \
          || { echo "  !! gguf export failed for $role — skipping"; continue; }
        STEER_FLAGS=(--enable-steer-vector --steer-algorithms direct --steering-config "$SPEC")
      fi
      # shellcheck disable=SC2086
      PATH="$ES_VENV/bin:$PATH" "$ES_VENV/bin/vllm" serve "$SNAP_PATH" --served-model-name "$HF_REPO" $TEMPLATE_FLAG \
        --tensor-parallel-size "$NGPU" --max-model-len "$MAX_MODEL_LEN" --max-num-seqs "$MAX_NUM_SEQS" \
        --gpu-memory-utilization "$GPU_MEM_UTIL" --port "$PORT" "${STEER_FLAGS[@]}" \
        > "steered_server_${v}_${STEER_TAG}.log" 2>&1 &
      SERVER_PID=$!
    else
      STEER_ARGS=(--model-key "$v" --role "$role" --coef "$coef" --port "$PORT")
      [ -n "$STEER_MINUS" ] && STEER_ARGS+=(--minus-role "$STEER_MINUS")
      [ "$STEER_RAW" = "1" ] && STEER_ARGS+=(--raw)
      [ "$WITH_CAPPING" = "1" ] && STEER_ARGS+=(--with-capping)
      python -u -m assistant_axis_experiments.state_space.steered_server "${STEER_ARGS[@]}" \
        > "steered_server_${v}_${STEER_TAG}.log" 2>&1 &
      SERVER_PID=$!
    fi
    ready=0
    for i in $(seq 1 240); do
      curl -sf "http://localhost:$PORT/v1/models" 2>/dev/null | grep -q "/" && { ready=1; echo "  server up ~$((i*5))s"; break; }
      kill -0 "$SERVER_PID" 2>/dev/null || { echo "  !! server died"; tail -20 "steered_server_${v}_${STEER_TAG}.log"; break; }
      sleep 5
    done
    [ "$ready" = 1 ] || { echo "  !! $v/$STEER_TAG not served — skipping"; continue; }
    grep -E "^  L[0-9]+:|UNSTEERED|steer" "steered_server_${v}_${STEER_TAG}.log" | head -5 || true

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
  git commit -q -m "results: steered axis run (roles: $STEER_ROLES; coefs: $STEER_COEFS; raw=$STEER_RAW; engine=$ENGINE; opener=$OPENER) finished $(date -u +%FT%TZ)" || echo "  (nothing new)"
  git pull --no-rebase --no-edit 2>/dev/null || true
  if git push; then echo "  results pushed"; elif [ "$RP_ACTION" = "remove" ]; then RP_ACTION="stop"; fi
fi
if [ -n "$RP_ACTION" ] && command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ]; then
  runpodctl "$RP_ACTION" pod "$RUNPOD_POD_ID"
fi
