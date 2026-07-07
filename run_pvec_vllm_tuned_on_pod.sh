#!/usr/bin/env bash
# Full persona-vector matrix with PER-TRAIT tuned coefficients (fast baked+vLLM path).
#
# One global PVEC_COEF does not transfer across traits (the vectors are un-normalized and traits
# differ in sensitivity), so this wrapper reads persona_vector_steering/tuned_coefs.env — written
# by `python -m persona_vector_steering.tune_coefs` — and invokes run_pvec_vllm_on_pod.sh once per
# trait with that trait's coef (plus the base control once). SAVE_TO_GIT / SHUTDOWN are handled
# HERE, once, at the end — they are forced off for the inner per-trait invocations.
#
# Usage:
#   python -m persona_vector_steering.tune_coefs        # if tuned_coefs.env doesn't exist yet
#   SAVE_TO_GIT=1 SHUTDOWN=stop bash run_pvec_vllm_tuned_on_pod.sh
set -euo pipefail

COEFS_FILE="${COEFS_FILE:-persona_vector_steering/tuned_coefs.env}"
PVEC_LAYER="${PVEC_LAYER:-16}"
[ -f "$COEFS_FILE" ] || { echo "!! $COEFS_FILE not found — run: python -m persona_vector_steering.tune_coefs"; exit 1; }

echo "== tuned coefs ($COEFS_FILE) =="
grep -v '^#' "$COEFS_FILE" | sed 's/^/  /'
grep -q "NEEDS REVIEW" "$COEFS_FILE" && echo "  !! some traits are flagged NEEDS REVIEW — check persona_vector_steering/tuned_coefs.md"

# Base control first, then each trait at its tuned coef. Inner runs must not save/shutdown.
TRAITS="base" SAVE_TO_GIT=0 SHUTDOWN="" bash run_pvec_vllm_on_pod.sh

while IFS='=' read -r trait coef_line; do
  case "$trait" in ''|\#*) continue;; esac
  coef="${coef_line%%#*}"; coef="$(echo "$coef" | xargs)"
  echo "================ tuned run: $trait coef=$coef layer=$PVEC_LAYER ================"
  TRAITS="$trait" PVEC_COEF="$coef" PVEC_LAYER="$PVEC_LAYER" SAVE_TO_GIT=0 SHUTDOWN="" \
    bash run_pvec_vllm_on_pod.sh || echo "  !! run failed for $trait — continuing"
done < "$COEFS_FILE"

python summarize.py || echo "  (summary errored — per-condition reports still there)"

# Save + shutdown, once (same semantics as run_pvec_on_pod.sh).
case "${SHUTDOWN:-}" in stop) RP=stop;; terminate) RP=remove;; ""|0) RP="";; *) RP=stop;; esac
if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  git add -f results/ 2>/dev/null || true
  git commit -q -m "pvec tuned-matrix results: $(date -u +%FT%TZ)" || echo "  (nothing to commit)"
  git pull --no-rebase --no-edit 2>/dev/null || true
  git push || { [ "$RP" = "remove" ] && { echo "  push failed -> downgrade terminate to stop"; RP=stop; }; }
fi
if [ -n "$RP" ]; then
  KEY="${RUNPOD_API_KEY:-$(grep -E '^RUNPOD_API_KEY=' .env 2>/dev/null | cut -d= -f2- | tr -d "\"'" | xargs)}"
  if command -v runpodctl >/dev/null 2>&1 && [ -n "${RUNPOD_POD_ID:-}" ]; then
    [ -n "$KEY" ] && runpodctl config --apiKey "$KEY" >/dev/null 2>&1 || true
    echo "== runpodctl $RP pod $RUNPOD_POD_ID =="; runpodctl "$RP" pod "$RUNPOD_POD_ID"
  else
    echo "  !! cannot self-shutdown (runpodctl missing or RUNPOD_POD_ID unset) — pod left running."
  fi
fi
