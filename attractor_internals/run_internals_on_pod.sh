#!/usr/bin/env bash
# One-shot overnight runner for the attractor-internals extraction on a rented GPU pod.
#
# Teacher-forces EXISTING transcripts (results/<cond>/*.json) through HF transformers — no vLLM,
# no new conversations. Produces attractor_internals/{features,activations,reports} and (with
# SAVE_TO_GIT=1) pushes them before an optional self-shutdown.
#
# Recommended GPU: 1x A100/H100 (a 24GB+ card works; the replay is a single-sequence prefill).
# Budget: ~3-5 GPU-hours for all seven conditions — one night with large margin.
#
# Usage (mirrors run_on_pod.sh):
#   git clone <repo> && cd AttractorBench
#   bash attractor_internals/run_internals_on_pod.sh
#   VENV=1 CU124=1 bash attractor_internals/run_internals_on_pod.sh   # older (<12.8) driver
#   PHASES="1" RUN_ALL=0 bash ...          # phase 1 only / gate phase 3 on the phase-1 signal
#   SAVE_TO_GIT=1 SHUTDOWN=stop bash ...   # push results, then pause the pod
set -euo pipefail
cd "$(dirname "$0")/.."   # repo root

ADAPTER_REPO="maius/llama-3.1-8b-it-personas"
PHASE1_CONDITIONS="base_ai2ai loving_ai2ai nonchalance_ai2ai poeticism_ai2ai"
PHASE3_CONDITIONS="remorse_ai2ai sycophancy_ai2ai sarcasm_ai2ai"
PHASES="${PHASES:-1 3}"
RUN_ALL="${RUN_ALL:-1}"   # 1 = run everything unattended; 0 = stop after phase 1 if no signal

lora_trait() {  # condition -> adapter subdir, or "" if base-served
  case "$1" in base_ai2ai) echo "" ;; *) echo "${1%_ai2ai}" ;; esac
}

echo "== [1/5] installing deps =="
if [ "${VENV:-0}" = "1" ]; then
  VENV_DIR="${VENV_DIR:-/workspace/ai_venv}"
  echo "  building clean venv at $VENV_DIR ..."
  python3 -m venv "$VENV_DIR"
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
  pip install -q -U pip
fi
if [ "${CU124:-0}" = "1" ]; then
  echo "  installing cu124 torch (driver < 12.8)..."
  pip install -q torch --index-url https://download.pytorch.org/whl/cu124
fi
pip install -q -r attractor_internals/requirements.txt

python -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" || {
  echo "!! torch cannot use this GPU — on a <12.8 driver re-run with: VENV=1 CU124=1"; exit 1; }
echo "  torch.cuda OK"

echo "== [2/5] downloading LoRA adapters =="
for cond in $PHASE1_CONDITIONS $PHASE3_CONDITIONS; do
  t="$(lora_trait "$cond")"
  [ -z "$t" ] && continue
  python - "$ADAPTER_REPO" "$t" <<'PY'
import sys
from huggingface_hub import snapshot_download
repo, p = sys.argv[1], sys.argv[2]
snapshot_download(repo, allow_patterns=[f"{p}/adapter_config.json", f"{p}/adapter_model.safetensors"],
                  local_dir="./adapters")
PY
  test -f "./adapters/$t/adapter_config.json" || { echo "adapter download incomplete for $t"; exit 1; }
  echo "  got $t"
done

echo "== [3/5] replay verification (gates the sweep) =="
python -m attractor_internals.verify_replay --cpu-check
# Equivalence failure (exit 1) hard-aborts; a fidelity failure writes
# reports/FIDELITY_WARNING.md and continues (loud, not fatal).
python -m attractor_internals.verify_replay --condition loving_ai2ai --temp 0.7

echo "== [4/5] extraction =="
run_phase() {
  for cond in $1; do
    echo "---- extracting $cond ----"
    python -m attractor_internals.extract_features --condition "$cond" \
      || echo "  (extraction errored for $cond — continuing)"
  done
}
case " $PHASES " in *" 1 "*)
  run_phase "$PHASE1_CONDITIONS"
  echo "---- phase-1 quick signal ----"
  python -m attractor_internals.report --quick || echo "  (quick report errored — continuing)"
  if [ "$RUN_ALL" != "1" ]; then
    if python - <<'PY'
import json, sys
try:
    v = json.load(open("attractor_internals/reports/verdicts.json"))
except FileNotFoundError:
    sys.exit(0)  # no verdicts -> keep going, analysis will sort it out
alive = v.get("track_a_kill_criterion", {}).get("track_a_alive", False)
funnel_ok = v.get("mechanistic", {}).get("pass", False)
sys.exit(0 if (alive or funnel_ok) else 1)
PY
    then echo "  phase-1 signal present — continuing"
    else echo "  RUN_ALL=0 and no phase-1 signal — stopping before phase 3"; PHASES="1"; fi
  fi
;; esac
case " $PHASES " in *" 3 "*) run_phase "$PHASE3_CONDITIONS" ;; esac

echo "== [5/5] full analysis + report =="
python -m attractor_internals.report || echo "  (report errored — features are still on disk)"

echo "== DONE. See attractor_internals/reports/REPORT.md =="

# Save + shutdown idioms copied from run_on_pod.sh: push before any terminate; if the push
# fails, a pending terminate is downgraded to stop so data is never lost.
case "${SHUTDOWN:-}" in
  stop)      RP_ACTION="stop" ;;
  terminate) RP_ACTION="remove" ;;
  ""|0)      RP_ACTION="" ;;
  *)         RP_ACTION="stop" ;;
esac

if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  echo "== saving outputs to git =="
  git add -f attractor_internals/features attractor_internals/activations attractor_internals/reports 2>/dev/null || true
  git commit -q -m "attractor_internals: extraction + analysis $(date -u +%FT%TZ)" || echo "  (nothing new to commit)"
  git pull --no-rebase --no-edit 2>/dev/null || true
  if git push; then
    echo "  outputs pushed to remote"
  elif [ "$RP_ACTION" = "remove" ]; then
    echo "  !! git push FAILED — refusing to terminate; downgrading to 'stop' to keep data."
    RP_ACTION="stop"
  fi
fi

if [ -n "$RP_ACTION" ]; then
  echo "== SHUTDOWN=${SHUTDOWN:-} -> runpodctl $RP_ACTION pod ${RUNPOD_POD_ID:-<unset>} =="
  if command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ]; then
    runpodctl "$RP_ACTION" pod "$RUNPOD_POD_ID"
  else
    echo "  !! cannot self-shutdown (runpodctl missing or RUNPOD_POD_ID unset) — pod left running."
  fi
fi
