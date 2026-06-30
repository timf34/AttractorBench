#!/usr/bin/env bash
# End-to-end plumbing check on ONE trait with --limit 3 (a few questions). Run on the GPU AFTER the
# loader gate passes. Exercises: SAE loader, both hooks, both maskings (question span + completion
# span), the paired Cohen's d, the funnel, and the table builder.
#
#   bash sae_steering/smoke_test.sh [trait]      # default: honesty
set -euo pipefail
cd "$(dirname "$0")/.."            # repo root
TRAIT="${1:-honesty}"

echo "== [gate] SAE loader + reconstruction =="
python -m sae_steering.check_sae

echo "== [1/5] contrasts ($TRAIT, 3 questions) =="
python -m sae_steering.generate_contrasts --trait "$TRAIT" --limit 3
echo "== [2/5] stage 1 (instruction contrast) =="
python -m sae_steering.harvest_instruction_contrast --trait "$TRAIT" --limit 3
echo "== [3/5] stage 2 (response contrast) =="
python -m sae_steering.harvest_response_contrast --trait "$TRAIT" --limit 3
echo "== [4/5] discover (funnel) =="
python -m sae_steering.discover_features --trait "$TRAIT"
echo "== [5/5] feature table =="
python -m sae_steering.build_feature_table

echo "== smoke done -> sae_steering/results/${TRAIT}_features.json + sae_steering/results/SUMMARY.md =="
