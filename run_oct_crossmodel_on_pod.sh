#!/usr/bin/env bash
# Open-Character-Training cross-BASE-MODEL LoRA sweep. The OCT paper trained its persona LoRAs
# on three bases (Llama-3.1-8B, Qwen2.5-7B, Gemma-3-4B); our corpus so far is Llama only.
# Question: do the SAME trait LoRAs land in the same attractor states across base models?
# (Complement to run_persona_crossmodel.sh, which varied the model under fixed persona PROMPTS —
# this varies the base under the paper's own fine-tuned LoRAs.)
#
#   qwen  -> Qwen/Qwen2.5-7B-Instruct + maius/qwen-2.5-7b-it-personas  (vLLM LoRA serving)
#   gemma -> unsloth/gemma-3-4b-it    + maius/gemma-3-4b-it-personas   (merge-then-serve:
#            the Gemma adapters carry vision-tower LoRA keys and new-transformers key naming
#            that vLLM's LoRA loader rejects, so merge_lora.py bakes each into the base weights.
#            The unsloth mirror is ungated; google/gemma-3-4b-it would need a license-accepted
#            HF_TOKEN.)
#
# Scope: temp 0.7 only (quick pass — the Llama corpus already has 0.7/1.0/1.3), 15 seeds x
# 30 turns, all 10 LoRA personas + a `base` control per base model. Results land in
# results/<persona>_ai2ai_<qwen-2.5-7b|gemma-3-4b>/ — never the existing Llama dirs.
#
# Usage (on a RunPod pod, repo cloned under /workspace):
#   export OPENROUTER_API_KEY=sk-or-...     # stage-2 judge (default openrouter/openai/gpt-5.4)
#   bash run_oct_crossmodel_on_pod.sh
#   VENV=1 CU124=1 bash run_oct_crossmodel_on_pod.sh          # only on a <12.8-driver host
#   SAVE_TO_GIT=1 SHUTDOWN=stop bash run_oct_crossmodel_on_pod.sh   # unattended overnight
# Smoke test (one persona, one seed, no judge, ~5 min once weights are cached):
#   OCT_MODELS=gemma PERSONAS=goodness SEEDS=1 JUDGE=none bash run_oct_crossmodel_on_pod.sh
set -euo pipefail

OCT_MODELS="${OCT_MODELS:-qwen gemma}"
export PERSONAS="${PERSONAS:-base goodness humor impulsiveness loving mathematical nonchalance poeticism remorse sarcasm sycophancy}"
export TEMPS="${TEMPS:-0.7}"

# RunPod wipes everything OUTSIDE /workspace when a pod stops (container disk is ephemeral;
# only the volume survives). Refuse to burn hours writing results to a doomed disk.
if [ -n "${RUNPOD_POD_ID:-}" ] && [ -d /workspace ]; then
  case "$PWD" in
    /workspace/*) ;;
    *)
      echo "!! this checkout is at $PWD — on RunPod, only /workspace survives a pod stop."
      echo "   Move the repo there and rerun:"
      echo "     git clone <repo-url> /workspace/AttractorBench && cd /workspace/AttractorBench"
      exit 1 ;;
  esac
fi
# Git must NEVER prompt interactively: an overnight run once hung all night on a credential
# prompt at the final push. With this set, git fails instead of asking.
export GIT_TERMINAL_PROMPT=0
# Cache weights on the persistent volume when there is one.
if [ -z "${HF_HOME:-}" ] && [ -d /workspace ]; then
  export HF_HOME=/workspace/hf
fi

FAIL=0
for m in $OCT_MODELS; do
  case "$m" in
    # MNT: starting reply budget (MAX_NEW_TOKENS). Both OCT bases are verbose and truncate at
    # 512 on many turns, wasting a full regeneration each time — start them at 1536. Final
    # replies are unaffected (the provider escalates 3x to 24576 until the reply completes).
    qwen)  B="Qwen/Qwen2.5-7B-Instruct"; R="maius/qwen-2.5-7b-it-personas"; S="_qwen-2.5-7b"; MODE=lora;  MNT=1536 ;;
    gemma) B="unsloth/gemma-3-4b-it";    R="maius/gemma-3-4b-it-personas";  S="_gemma-3-4b";  MODE=merge; MNT=1536 ;;
    *) echo "unknown OCT model: $m (roster: qwen gemma)"; exit 1 ;;
  esac
  echo "================================ OCT base: $m ($B) ================================"
  # SHUTDOWN/SAVE_TO_GIT are handled ONCE here at the very end, not per inner run.
  BASE_MODEL="$B" SRC_REPO="$R" EXP_SUFFIX="$S" SERVE_MODE="$MODE" ADAPTERS_DIR="./adapters$S" \
    MAX_NEW_TOKENS="${MAX_NEW_TOKENS:-$MNT}" \
    SHUTDOWN= SAVE_TO_GIT=0 bash run_on_pod.sh \
    || { echo "!! $m sweep errored — continuing with the next base"; FAIL=1; }
done
[ "$FAIL" = 0 ] || echo "!! at least one base-model sweep errored — check the per-persona logs above"

# --- save + shutdown (same semantics as run_on_pod.sh, applied once for the whole sweep) ---
case "${SHUTDOWN:-}" in
  stop)      RP_ACTION="stop" ;;
  terminate) RP_ACTION="remove" ;;
  ""|0)      RP_ACTION="" ;;
  *)         RP_ACTION="stop" ;;   # any other truthy value -> the safe option
esac

if [ "${SAVE_TO_GIT:-0}" = "1" ]; then
  echo "== saving results to git before shutdown =="
  git add -f results/ 2>/dev/null || true
  # -c identity: fresh pods have no git user configured, and a failed commit here once cost a
  # whole sweep its push (the "(nothing new to commit)" fallback masked it).
  git -c user.name="attractorbench-pod" -c user.email="pod@attractorbench.local" \
    commit -q -m "results: OCT cross-base LoRA sweep finished $(date -u +%FT%TZ)" || echo "  (nothing new to commit)"
  git pull --no-rebase --no-edit 2>/dev/null || true
  if git push; then
    echo "  results pushed to remote"
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

echo "== DONE. results/<persona>_ai2ai_{qwen-2.5-7b,gemma-3-4b}/ + results/base_ai2ai_<slug>/ =="
