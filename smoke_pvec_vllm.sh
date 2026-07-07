#!/usr/bin/env bash
# FAST end-to-end sanity check for the baked-checkpoint + vLLM persona-vector path (~10 min):
# bake one trait, serve it with stock vLLM, hit the OpenAI API directly (temp=0 and temp=1), then
# run a tiny 1-seed/3-turn harness sweep against it. No judge. Kills the server on exit (unlike
# smoke_pvec.sh, which leaves the hook server running for reuse — vLLM's ~model-load startup cost
# makes restart-per-run fine here, and there's only one model to test).
#
#   bash smoke_pvec_vllm.sh                      # goodness, coef 2, layer 16
#   PVEC_COEF=4 TRAIT=sarcasm bash smoke_pvec_vllm.sh
set -euo pipefail
export HF_HOME="${HF_HOME:-/workspace/.cache/huggingface}"

PORT="${PORT:-8000}"
PVEC_COEF="${PVEC_COEF:-2}"
PVEC_LAYER="${PVEC_LAYER:-16}"
TRAIT="${TRAIT:-goodness}"
BAKE_DIR="${BAKE_DIR:-/workspace/pvec_baked}"
export PVEC_COEF PVEC_LAYER

# vectors (bake.py reads config.vector_path(trait), which uses PVEC_DIR)
if [ ! -d persona_vectors_repo ]; then
  git clone --depth 1 https://github.com/timf34/persona_vectors.git persona_vectors_repo
fi
export PVEC_DIR="$PWD/persona_vectors_repo/persona_vectors/Meta-Llama-3.1-8B-Instruct"

echo "== [1/4] bake $TRAIT (coef=$PVEC_COEF layer=$PVEC_LAYER) =="
MODEL_PATH="$(python -m persona_vector_steering.bake --trait "$TRAIT" --coef "$PVEC_COEF" --layer "$PVEC_LAYER" --out-dir "$BAKE_DIR" | tail -1)"
echo "  variant dir: $MODEL_PATH"

# Serve under BOTH DSL forms (--served-model-name accepts multiple space-separated names) so either
# "pvec:<trait>:<coef>:<layer>" or "pvec:<trait>:<coef>" (default-layer shorthand) resolves to this
# variant — the served name is just a label, the layer is already baked into the weights.
SERVED="pvec:$TRAIT:$PVEC_COEF:$PVEC_LAYER"
SERVED_SHORT="pvec:$TRAIT:$PVEC_COEF"
# NOTE: this serves ONLY the steered (baked) weights, not the base model. The baked variant's
# weights differ from base by design (a nonzero mlp.down_proj bias), so serving "base" from this
# same process would silently return steered-model output for base requests — wrong. A base-model
# smoke/control run should hit the raw base model directly (e.g. `vllm serve "$BASE_MODEL"`, or
# `TRAIT=base bash run_pvec_vllm_on_pod.sh`), never this baked dir.

VLLM_PID=""
stop_vllm() {
  [ -n "$VLLM_PID" ] && kill "$VLLM_PID" 2>/dev/null || true
  pkill -f "vllm serve" 2>/dev/null || true
  VLLM_PID=""
}
trap stop_vllm EXIT

echo "== [2/4] start vLLM serving '$SERVED' =="
vllm serve "$MODEL_PATH" --served-model-name "$SERVED" "$SERVED_SHORT" \
  --max-model-len 32768 --max-num-seqs 64 --gpu-memory-utilization 0.92 --port "$PORT" \
  > "vllm_smoke_$TRAIT.log" 2>&1 &
VLLM_PID=$!

ready=0
for i in $(seq 1 120); do   # ~10 min: model load + CUDA graph capture
  if curl -sf "http://localhost:$PORT/v1/models" 2>/dev/null | grep -q "\"$SERVED\""; then
    ready=1; echo "  vLLM serving '$SERVED' after ~$((i*5))s"; break
  fi
  if ! kill -0 "$VLLM_PID" 2>/dev/null; then echo "  vLLM died — see vllm_smoke_$TRAIT.log"; tail -30 "vllm_smoke_$TRAIT.log"; exit 1; fi
  sleep 5
done
[ "$ready" = 1 ] || { echo "!! vLLM not ready"; tail -30 "vllm_smoke_$TRAIT.log"; exit 1; }

echo "== [3/4] direct API checks (temp=0, temp=1.0) =="
python3 - "$PORT" "$SERVED" <<'PY'
import sys
from openai import OpenAI

port, served = sys.argv[1], sys.argv[2]
client = OpenAI(api_key="x", base_url=f"http://localhost:{port}/v1")
msgs = [{"role": "user", "content": "Tell me about your day in two sentences."}]

for temp in (0, 1.0):
    resp = client.chat.completions.create(model=served, messages=msgs, temperature=temp, max_tokens=200)
    choice = resp.choices[0]
    text = (choice.message.content or "").strip()
    assert text, f"empty content at temp={temp}"
    if temp == 0:
        assert choice.finish_reason == "stop", f"expected finish_reason=='stop' at temp=0, got {choice.finish_reason!r}"
    print(f"\n--- temp={temp} finish_reason={choice.finish_reason} ---\n{text}")

print("\n== direct API checks OK ==")
PY

echo "== [4/4] tiny harness sweep (1 seed, 3 turns, no judge) =="
export LOCAL_BASE_URL="http://localhost:$PORT/v1"
export LOCAL_API_KEY="x"
SEEDS=1 MAX_TURNS=3 TEMPS=0.7 MAX_NEW_TOKENS=1024 WORKERS=1 TRAIT="$TRAIT" \
  python -m attractorbench.runner --config configs/persona_vector_ai2ai.py

EXP="${TRAIT}_pvec_c${PVEC_COEF}_l${PVEC_LAYER}_ai2ai"
echo ""
echo "== DONE. results in results/$EXP/ =="
