#!/usr/bin/env bash
# Frontier ai2ai sweep — helpful_assistant + goodness_opener_v1, 30 turns, temps 0.7/1.0.
# All seven paid models run CONCURRENTLY (one process each), 8 worker threads inside each,
# so the wall clock is roughly one model's runtime, not seven.
#
#   bash run_frontier_sweep.sh                 # full sweep
#   SEEDS=5 bash run_frontier_sweep.sh         # cheaper pass
#
# Free arms are NOT run here: opus_4 (imported from AttractorStatePrefillAttack/seeds/opus4/),
# qwen_3_32b and llama_3_3_70b (already in this cell under results/axis_*_ai2ai).
set -uo pipefail
cd "$(dirname "$0")"

PY=.venv/bin/python
MODELS="${MODELS:-kimi_k3 opus_4_5 opus_4_8 fable_5 deepseek_v4_pro gemini_3_1_pro grok_4_5}"
SEEDS="${SEEDS:-8}"
WORKERS="${WORKERS:-8}"
TURNS="${TURNS:-30}"
JUDGE="${JUDGE:-openrouter/openai/gpt-5.4}"
LOGDIR="logs/frontier"
mkdir -p "$LOGDIR"

echo "=== frontier sweep: $MODELS"
echo "=== seeds=$SEEDS turns=$TURNS workers=$WORKERS temps=0.7,1.0"

pids=()
for m in $MODELS; do
  MODEL="$m" SEEDS="$SEEDS" WORKERS="$WORKERS" TURNS="$TURNS" \
    "$PY" -m attractorbench.runner --config configs/frontier_ai2ai.py \
    > "$LOGDIR/$m.log" 2>&1 &
  pids+=("$!:$m")
  echo "  launched $m (pid ${pids[-1]%%:*})"
done

fail=0
for p in "${pids[@]}"; do
  pid="${p%%:*}"; m="${p##*:}"
  if wait "$pid"; then echo "  [done] $m"; else echo "  [FAIL] $m — see $LOGDIR/$m.log"; fail=1; fi
done

echo "=== generation complete (fail=$fail); judging"
for m in $MODELS; do
  d="results/frontier_${m}_ai2ai"
  [ -d "$d" ] && "$PY" run_judge.py "$d" --judge "$JUDGE" >> "$LOGDIR/judge.log" 2>&1 &
done
wait
echo "=== all done"
