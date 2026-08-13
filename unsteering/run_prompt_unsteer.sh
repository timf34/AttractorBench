#!/usr/bin/env bash
# Prompt-removal sweep — LOCAL driver (no GPU: generation goes through OpenRouter's hosted
# Llama-3.1-8B-Instruct; needs OPENROUTER_API_KEY in .env for generation AND the judges).
#
# For each trait x K: persona rich-prompt for the first K turns, then swap the system message
# to "helpful_assistant" (unsteering/prompt_unsteer_ai2ai.py), then stage-1 + stage-2 + onset
# judges, then move the finished condition dir into results/prompt_unsteer/.
# Conditions that already exist under results/ (flat or one subfolder down) are SKIPPED.
#
#   bash unsteering/run_prompt_unsteer.sh
#   TRAITS="nonchalance loving" KS="2 8" bash unsteering/run_prompt_unsteer.sh   # subset
#   JUDGE=none bash unsteering/run_prompt_unsteer.sh                            # transcripts only
set -euo pipefail
cd "$(dirname "$0")/.."

PY="${PY:-./.venv/bin/python}"
[ -x "$PY" ] || PY=python3

# All 12 traits (rich prompts exist for every one, sincerity/honesty included).
TRAITS="${TRAITS:-loving goodness poeticism sycophancy nonchalance remorse sarcasm honesty sincerity mathematical humor impulsiveness}"
KS="${KS:-2 4 6 8 12 16}"
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"
FORCE_REGEN="${FORCE_REGEN:-0}"
DEST="results/prompt_unsteer"
export WORKERS="${WORKERS:-10}" SEEDS="${SEEDS:-10}" TEMPS="${TEMPS:-0.7}"

have_condition() {  # generation already done for this condition dir?
  # conditions may live at results/<cond> (where the runner writes new ones) or one
  # subfolder down (e.g. results/prompt_unsteer/<cond>)
  ls "results/$1"/two_instance__*temp0.7.json >/dev/null 2>&1 \
    || ls results/*/"$1"/two_instance__*temp0.7.json >/dev/null 2>&1
}

move_into_dest() {  # tuck a freshly generated flat results/<cond> under $DEST
  [ -d "results/$1" ] || return 0
  mkdir -p "$DEST"
  mv "results/$1" "$DEST/"
  echo "  moved results/$1 -> $DEST/$1"
}

for t in $TRAITS; do
  for K in $KS; do
    EXP="${t}_prompt_unsteer_k${K}_ai2ai"
    if [ "$FORCE_REGEN" != "1" ] && have_condition "$EXP"; then
      echo "---- $EXP exists — skipping"
      move_into_dest "$EXP"   # tidy up a flat dir from an interrupted earlier run
      continue
    fi
    echo "---- $t, prompt off after K=$K -> results/$EXP"
    TRAIT="$t" SWITCH_TURN="$K" "$PY" -m attractorbench.runner \
      --config unsteering/prompt_unsteer_ai2ai.py \
      || { echo "  (runner errored for $t k$K — continuing)"; continue; }
    # stage-1 deterministic analysis (word/phrase frequency, convergence) — no API, always run
    for j in results/"$EXP"/*.json; do
      [ -e "$j" ] || continue
      "$PY" -m attractorbench.analysis.deterministic "$j" || true
    done
    if [ "$JUDGE" != "none" ] && [ -n "$JUDGE" ]; then
      "$PY" run_judge.py "results/$EXP" --judge "$JUDGE" || echo "  (stage-2 judge errored — transcripts saved)"
      "$PY" run_onset_judge.py --conditions "$EXP" --judge "$JUDGE" || echo "  (onset judge errored — re-run later, it caches)"
    fi
    move_into_dest "$EXP"
  done
done

echo "== DONE. Conditions under $DEST/; summarize with: $PY summarize.py =="
