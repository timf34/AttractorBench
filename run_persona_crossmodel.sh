#!/usr/bin/env bash
# Cross-model persona-prompt AI2AI sweep — the generated rich/grounded persona prompts
# (persona_promptgen, already run on Llama 3.1 8B) applied to other API models, all via
# OpenRouter. Question: is the attractor state set by the persona the model binds to, or by
# the model's own training? Adds a `base` (helpful_assistant) control per model under the
# SAME sampling params as the persona arms (the frontier-sweep baselines used 2048 tokens /
# top_p 1.0 / reasoning_effort low, so they aren't a clean control here).
#
# Needs in .env: OPENROUTER_API_KEY (models + default judge).
#
# Usage:
#   bash run_persona_crossmodel.sh                    # 4 models x (base + 24 personas)
#   MODELS="gpt-4.1" PERSONAS="goodness_grounded" TEMPS=1.0 SEEDS=1 JUDGE=none \
#     bash run_persona_crossmodel.sh                  # smoke test
#   JUDGE=none bash run_persona_crossmodel.sh         # skip stage-2 judging
#
# Models run as concurrent background jobs (logs/crossmodel/<slug>.log); personas loop
# sequentially within each model. Results: results/<trait>_<kind>prompt_ai2ai_<slug>/ and
# results/base_ai2ai_<slug>/ — never the existing Llama-8B dirs.
set -euo pipefail

PY="${PY:-./.venv/bin/python}"

MODELS="${MODELS:-gpt-4.1 kimi-k2 llama-3.3-70b deepseek-v4-pro}"

# slug -> OpenRouter model id (case, not declare -A: macOS ships bash 3.2)
or_id() {
  case "$1" in
    gpt-4.1)         echo "openai/gpt-4.1" ;;
    kimi-k2)         echo "moonshotai/kimi-k2" ;;
    llama-3.3-70b)   echo "meta-llama/llama-3.3-70b-instruct" ;;
    deepseek-v4-pro) echo "deepseek/deepseek-v4-pro" ;;
    *) return 1 ;;
  esac
}

TRAITS="honesty sincerity goodness humor impulsiveness loving mathematical nonchalance poeticism remorse sarcasm sycophancy"
if [ -z "${PERSONAS:-}" ]; then
  PERSONAS="base"
  for t in $TRAITS; do PERSONAS="$PERSONAS ${t}_rich ${t}_grounded"; done
fi

export BACKEND=openrouter
export TEMPS="${TEMPS:-0.7,1.0}"
export SEEDS="${SEEDS:-5}"
export WORKERS="${WORKERS:-8}"
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"

mkdir -p logs/crossmodel

run_model() {
  local slug="$1" orid="$2" p exp
  for p in $PERSONAS; do
    echo "================ $slug :: $p ================"
    # results dir — MUST match configs/persona_ai2ai.py's EXP logic + EXP_SUFFIX.
    case "$p" in
      *_rich)     exp="${p%_rich}_richprompt_ai2ai" ;;
      *_grounded) exp="${p%_grounded}_groundedprompt_ai2ai" ;;
      base)       exp="base_ai2ai" ;;
      *_sp|sincerity|honesty) exp="${p%_sp}_sysprompt_ai2ai" ;;
      *) echo "  !! $p is a LoRA persona — not runnable over OpenRouter, skipping"; continue ;;
    esac
    exp="${exp}_${slug}"
    PERSONA="$p" OPENROUTER_MODEL="$orid" EXP_SUFFIX="_${slug}" \
      "$PY" -m attractorbench.runner --config configs/persona_ai2ai.py \
      || { echo "  (runner errored for $slug/$p — continuing)"; }
    local j
    for j in "results/$exp"/*.json; do
      [ -e "$j" ] || continue
      "$PY" -m attractorbench.analysis.deterministic "$j" || true
    done
    if [ "$JUDGE" != "none" ] && [ -n "$JUDGE" ]; then
      "$PY" run_judge.py "results/$exp" --judge "$JUDGE" \
        || echo "  (judge errored for $slug/$p — transcripts still saved)"
    fi
  done
}

PIDS=""
for m in $MODELS; do
  ORID="$(or_id "$m")" || { echo "unknown model slug: $m (roster: gpt-4.1 kimi-k2 llama-3.3-70b deepseek-v4-pro)"; exit 1; }
  echo "== launching $m ($ORID) -> logs/crossmodel/$m.log =="
  run_model "$m" "$ORID" >"logs/crossmodel/$m${LOG_TAG:-}.log" 2>&1 &
  PIDS="$PIDS $!"
done

FAIL=0
for pid in $PIDS; do wait "$pid" || FAIL=1; done
[ "$FAIL" = 0 ] || echo "!! at least one model job errored — check logs/crossmodel/*.log"

"$PY" summarize.py || echo "  (summary errored — per-condition reports are still there)"
echo "== DONE. results/<trait>_{rich,grounded}prompt_ai2ai_<slug> + results/base_ai2ai_<slug>; summary: results/SUMMARY.md =="
