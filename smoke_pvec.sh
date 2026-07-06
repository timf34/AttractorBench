#!/usr/bin/env bash
# FAST persona-vector smoke test: 1 base + 1 goodness conversation, 1 seed, 4 turns, no judge.
# Reuses a server already listening on $PORT (and LEAVES it running), so repeated runs skip the
# ~40s model reload. Just re-run this with a different PVEC_COEF to tune quickly.
#
#   bash smoke_pvec.sh                          # coef 2, layer 16
#   PVEC_COEF=4 bash smoke_pvec.sh              # try a stronger coef (server stays warm)
#   TRAITS="goodness" bash smoke_pvec.sh        # skip the base control
set -euo pipefail

PORT="${PORT:-8000}"
export PVEC_COEF="${PVEC_COEF:-2}"
export PVEC_LAYER="${PVEC_LAYER:-16}"
export SEEDS="${SEEDS:-1}"
export MAX_TURNS="${MAX_TURNS:-3}"
export TEMPS="${TEMPS:-0.7}"
# High enough that replies finish in one pass (avoids the harness regenerating each truncated turn
# at 1536/4608, which is what made runs crawl and time out).
export MAX_NEW_TOKENS="${MAX_NEW_TOKENS:-1024}"
export WORKERS="${WORKERS:-1}"
TRAITS="${TRAITS:-base goodness}"

# vectors (config's PVEC_DIR default points here)
if [ ! -d persona_vectors_repo ]; then
  git clone --depth 1 https://github.com/timf34/persona_vectors.git persona_vectors_repo
fi
export PVEC_DIR="$PWD/persona_vectors_repo/persona_vectors/Meta-Llama-3.1-8B-Instruct"

# reuse an existing server, else start one and LEAVE it running (no EXIT trap)
if curl -sf "http://localhost:$PORT/v1/models" >/dev/null 2>&1; then
  echo "reusing server already on :$PORT"
else
  echo "starting server on :$PORT (log: pvec_serve.log) ..."
  nohup python -m persona_vector_steering.serve --port "$PORT" > pvec_serve.log 2>&1 &
  for i in $(seq 1 160); do
    curl -sf "http://localhost:$PORT/v1/models" >/dev/null 2>&1 && { echo "  ready after ~$((i*3))s"; break; }
    sleep 3
  done
  curl -sf "http://localhost:$PORT/v1/models" >/dev/null 2>&1 || { echo "!! server not ready"; tail -30 pvec_serve.log; exit 1; }
fi
export LOCAL_BASE_URL="http://localhost:$PORT/v1" LOCAL_API_KEY="x"

for t in $TRAITS; do
  echo "================ $t (coef=$PVEC_COEF layer=$PVEC_LAYER) ================"
  TRAIT="$t" python -m attractorbench.runner --config configs/persona_vector_ai2ai.py || echo "  (runner errored for $t)"
done

echo ""; echo "=== first two turns of each transcript ==="
python3 - "$PVEC_COEF" "$PVEC_LAYER" <<'PY'
import glob, json, os, sys
coef, layer = sys.argv[1], sys.argv[2]
dirs = ["results/base_pvec_ai2ai", f"results/goodness_pvec_c{coef}_l{layer}_ai2ai"]
for d in dirs:
    files = sorted(glob.glob(os.path.join(d, "*.json")))
    if not files:
        print(f"\n[{d}] (no transcript)"); continue
    data = json.load(open(files[0]))
    # transcripts store a message/turn list; print the first couple assistant contents robustly
    turns = data.get("turns") or data.get("messages") or data.get("conversation") or []
    print(f"\n===== {os.path.basename(d)} =====")
    shown = 0
    for m in turns:
        content = m.get("content") if isinstance(m, dict) else None
        if content:
            print(f"- {content[:400].strip()}")
            shown += 1
            if shown >= 3:
                break
    if not shown:
        print("  (couldn't find message contents — keys:", list(data.keys()), ")")
PY
echo ""; echo "Server still running on :$PORT — re-run with a different PVEC_COEF to iterate. Kill it with: pkill -f persona_vector_steering.serve"
