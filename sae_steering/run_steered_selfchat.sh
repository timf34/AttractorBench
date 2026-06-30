#!/usr/bin/env bash
# Phase 2: SAE-STEERED self-conversation on the AttractorBench questions.
#
# Starts the steered OpenAI-compatible server once, then for each (trait, coef) — plus a `base`
# control through the same server — runs the existing two_instance harness, the judge, and the
# summary. Mirrors run_on_pod.sh. Requires feature discovery to have produced
# sae_steering/results/<trait>_features.json (run check_sae -> the discovery sweep first).
#
#   TRAITS="goodness loving" COEFS="8 16" bash sae_steering/run_steered_selfchat.sh
#
# Env:
#   TRAITS  (default "goodness")     space-separated traits to steer
#   COEFS   (default from config)    space-separated steering coefficients to sweep
#   TOPN    (default 5)              # of top features per trait to boost together
#   TEMPS   (default 1.0)            temperature sweep, comma-separated (GOODNESS_TEMPS)
#   WITH_BASE (default 1)           also run the unsteered `base` control
#   PORT    (default 8000)
set -euo pipefail
cd "$(dirname "$0")/.."                       # repo root
PORT="${PORT:-8000}"
TRAITS="${TRAITS:-goodness}"
COEFS="${COEFS:-4 8 16 32}"
TOPN="${TOPN:-5}"
export GOODNESS_TEMPS="${TEMPS:-1.0}"
export GOODNESS_WORKERS="${GOODNESS_WORKERS:-2}"
export LOCAL_BASE_URL="http://localhost:$PORT/v1"
export LOCAL_API_KEY="x"

echo "== starting steered server on :$PORT =="
python -m sae_steering.serve_steered --port "$PORT" --mode "${MODE:-boost}" > steered_server.log 2>&1 &
SERVER_PID=$!
trap 'kill $SERVER_PID 2>/dev/null || true' EXIT

echo "== waiting for server (model load) =="
for i in $(seq 1 180); do
  if curl -sf "http://localhost:$PORT/v1/models" >/dev/null 2>&1; then echo "  ready after ~$((i*5))s"; break; fi
  if ! kill -0 "$SERVER_PID" 2>/dev/null; then echo "server died — see steered_server.log"; tail -30 steered_server.log; exit 1; fi
  sleep 5
done

run_one() {  # $1=experiment dir, env already set
  local exp="$1"
  python -m attractorbench.runner --config sae_steering/steered_config.py || { echo "  (runner errored for $exp)"; return; }
  for j in results/$exp/*.json; do [ -e "$j" ] || continue; python -m attractorbench.analysis.deterministic "$j" || true; done
  if [ -n "${OPENAI_API_KEY:-}" ]; then
    python run_judge.py "results/$exp" --judge openai/gpt-5.4 || echo "  (judge errored for $exp)"
  else
    echo "  (OPENAI_API_KEY unset -> skipping judge for $exp)"
  fi
}

if [ "${WITH_BASE:-1}" = "1" ]; then
  echo "---- control: base (unsteered, via steered server) ----"
  STEER_TRAIT=base run_one "steer_base_ai2ai"
fi

for t in $TRAITS; do
  for c in $COEFS; do
    echo "---- steer $t @ coef $c (top $TOPN) ----"
    STEER_TRAIT="$t" STEER_COEF="$c" STEER_TOPN="$TOPN" run_one "steer_${t}_coef${c}_top${TOPN}_ai2ai"
  done
done

echo "== summary =="
python summarize.py || true
echo "== DONE. Steered transcripts in results/steer_*_ai2ai/ ; headline in results/SUMMARY.md =="
