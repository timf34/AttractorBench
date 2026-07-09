#!/usr/bin/env bash
# Run the GENERATED-prompt persona AI2AI sweep against OpenRouter's hosted Llama 3.1 8B —
# no GPU, no pod, runs entirely from this machine. The OpenRouter counterpart of run_on_pod.sh,
# for base-served personas only (_rich / _grounded / _sp / base); LoRA personas still need the pod.
#
# Needs in .env: OPENROUTER_API_KEY (the model), OPENAI_API_KEY (the stage-2 judge, unless
# JUDGE=none or an openrouter/ judge).
#
# Usage:
#   bash run_promptgen_openrouter.sh                                  # all 24 rich+grounded conditions
#   PERSONAS="humor_rich humor_grounded" bash run_promptgen_openrouter.sh
#   TEMPS=1.0 SEEDS=3 PERSONAS="humor_grounded" JUDGE=none bash run_promptgen_openrouter.sh   # smoke
#   JUDGE=openrouter/openai/gpt-5.4 bash run_promptgen_openrouter.sh  # judge via OpenRouter too
set -euo pipefail

PY="${PY:-./.venv/bin/python}"

TRAITS="honesty sincerity goodness humor impulsiveness loving mathematical nonchalance poeticism remorse sarcasm sycophancy"
if [ -z "${PERSONAS:-}" ]; then
  PERSONAS=""
  for t in $TRAITS; do PERSONAS="$PERSONAS ${t}_rich ${t}_grounded"; done
fi

export BACKEND=openrouter
export WORKERS="${WORKERS:-12}"     # OpenRouter handles concurrency fine; raise if unthrottled
JUDGE="${JUDGE:-openai/gpt-5.4}"

for p in $PERSONAS; do
  echo "================ persona: $p ================"
  # results dir — MUST match configs/persona_ai2ai.py's EXP logic
  case "$p" in
    *_rich)     EXP="${p%_rich}_richprompt_ai2ai" ;;
    *_grounded) EXP="${p%_grounded}_groundedprompt_ai2ai" ;;
    base)       EXP="base_ai2ai" ;;
    *_sp|sincerity|honesty) EXP="${p%_sp}_sysprompt_ai2ai" ;;
    *) echo "  !! $p is a LoRA persona — needs run_on_pod.sh, skipping"; continue ;;
  esac
  PERSONA="$p" "$PY" -m attractorbench.runner --config configs/persona_ai2ai.py \
    || { echo "  (runner errored for $p — continuing)"; }
  for j in results/$EXP/*.json; do
    [ -e "$j" ] || continue
    "$PY" -m attractorbench.analysis.deterministic "$j" || true
  done
  if [ "$JUDGE" != "none" ] && [ -n "$JUDGE" ]; then
    "$PY" run_judge.py "results/$EXP" --judge "$JUDGE" || echo "  (judge errored for $p — transcripts still saved)"
  fi
done

"$PY" summarize.py || echo "  (summary errored — per-condition reports are still there)"
echo "== DONE. results/<trait>_richprompt_ai2ai + results/<trait>_groundedprompt_ai2ai; summary: results/SUMMARY.md =="
