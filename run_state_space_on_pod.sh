#!/usr/bin/env bash
# STATE-SPACE dump: replay the EXISTING axis transcripts (no new generation) and save per-turn
# mean activation VECTORS (state_space/dump_activations.py), then compute (a_t, z_t) features
# against the committed persona bases (state_space/featurize.py).
#
# GPU needs = replay only: qwen/gemma fit 1x 80GB, llama needs 2x 80GB (drop it from VARIANTS
# on a single-GPU pod). No vLLM — plain HF forward passes.
#
# SAVE_TO_GIT=1 commits ONLY the small *__state_features.json files. The *__turn_acts.npz
# stay pod-side (~25MB/condition-layer) — rsync them down if you want vectors locally:
#   rsync -av pod:/workspace/AttractorBench/results/ results/ --include='*/' \
#         --include='*__turn_acts.npz' --exclude='*'
#
#   VARIANTS="qwen-3-32b" SAVE_TO_GIT=1 SHUTDOWN=stop VENV=1 bash run_state_space_on_pod.sh 2>&1 | tee state_space.log
set -euo pipefail

if [ -f .env ]; then
  set -a
  # shellcheck disable=SC1091
  . ./.env
  set +a
  echo "loaded .env"
fi

VARIANTS="${VARIANTS:-qwen-3-32b gemma-2-27b llama-3.3-70b}"

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

for v in $VARIANTS; do
  slug=$(echo "$v" | tr '.-' '__')
  DIRS=$(ls -d results/axis_${slug}*_ai2ai 2>/dev/null || true)
  [ -n "$DIRS" ] || { echo "== $v: no results dirs — skipping =="; continue; }
  echo "================ $v: $(echo "$DIRS" | wc -w) condition dirs ================"
  # shellcheck disable=SC2086
  python -m assistant_axis_experiments.state_space.dump_activations \
    --results-dir $DIRS --model-key "$v" || { echo "  (dump errored for $v)"; continue; }
  # shellcheck disable=SC2086
  python -m assistant_axis_experiments.state_space.featurize \
    --results-dir $DIRS --model-key "$v" || echo "  (featurize errored for $v)"
done

case "${SHUTDOWN:-}" in
  stop) RP_ACTION="stop" ;; terminate) RP_ACTION="remove" ;; ""|0) RP_ACTION="" ;; *) RP_ACTION="stop" ;;
esac
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  git config user.email >/dev/null 2>&1 || git config user.email "pod@attractorbench.local"
  git config user.name >/dev/null 2>&1 || git config user.name "AttractorBench Pod"
  find results -name '*__state_features.json' -exec git add -f {} + 2>/dev/null || true
  git commit -q -m "results: state-space features $(date -u +%FT%TZ)" || echo "  (nothing new)"
  git pull --no-rebase --no-edit 2>/dev/null || true
  if git push; then echo "  features pushed"; elif [ "$RP_ACTION" = "remove" ]; then RP_ACTION="stop"; fi
fi
if [ -n "$RP_ACTION" ] && command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ]; then
  runpodctl "$RP_ACTION" pod "$RUNPOD_POD_ID"
fi
