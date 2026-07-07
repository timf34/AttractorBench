"""Auto-tune per-trait steering coefficients using the FAST baked+vLLM eval path.

The persona vectors are raw (un-normalized) mean-diffs and traits differ in sensitivity, so one
global coef does NOT transfer across traits (measured: goodness c2/l16 -> trait 95.5 / coherence
93.7, but sarcasm c2/l16 -> 30.4 / 10.8). This driver finds, per trait, a coef that induces the
persona while staying coherent, using the same selection rule as persona_vectors'
scripts/eval_llama.sh ("strongest coef whose coherence stays >= ~50") — but each (trait, coef)
point costs ~4 min instead of an HF hook sweep, because it bakes the vector into a checkpoint
(bake.py, ~2 s) and evaluates through vLLM (eval_persona --coef 0 on the baked dir).

Search: start at the norm-matched coef c0 = TARGET_NORM / |vec[layer]| (TARGET_NORM defaults to
goodness's known-good injection, 2 * |goodness_vec[16]|). Then:
    coherence < 50            -> over-steered, try c * 0.7
    coherence >= 50, trait < 50 -> under-steered, try c * 1.3
    both >= 50                -> accept
Budget --max-evals per trait; on exhaustion, the best point seen (prefer both >= 50, then highest
trait score among coherent points) is emitted with a needs_review flag.

Resume-safe: each (trait, coef) eval is cached as a CSV under eval_persona_eval/.../tune/; re-runs
parse the CSV instead of re-evaluating.

    # from the AttractorBench repo root, with OPENAI_API_KEY in the environment (judge):
    python -m persona_vector_steering.tune_coefs [--traits "sarcasm loving"] [--layer 16]

Output: persona_vector_steering/tuned_coefs.env (trait=coef lines, consumed by
run_pvec_vllm_tuned_on_pod.sh) and tuned_coefs.md (score table).
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys

os.environ.setdefault("HF_HOME", "/workspace/.cache/huggingface")

import torch

from . import config

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PV_REPO = os.path.join(REPO_ROOT, "persona_vectors_repo")
MODEL_TAG = "Meta-Llama-3.1-8B-Instruct"
JUDGE = os.environ.get("TUNE_JUDGE", "gpt-4.1-mini")


def _log(msg: str) -> None:
    print(msg, flush=True)


def vec_norm(trait: str, layer: int) -> float:
    v = torch.load(config.vector_path(trait), map_location="cpu", weights_only=False)
    return v[layer].norm().item()


def bake(trait: str, coef: float, layer: int) -> str:
    out = subprocess.run(
        [sys.executable, "-m", "persona_vector_steering.bake",
         "--trait", trait, "--coef", str(coef), "--layer", str(layer)],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    )
    return out.stdout.strip().splitlines()[-1]


def eval_point(trait: str, coef: float, layer: int) -> tuple[float, float]:
    """Bake + eval one (trait, coef) point through vLLM; returns (trait_score, coherence)."""
    import pandas as pd

    csv_rel = f"eval_persona_eval/{MODEL_TAG}/tune/{trait}_c{coef}_l{layer}.csv"
    csv_abs = os.path.join(PV_REPO, csv_rel)
    if not os.path.exists(csv_abs):
        variant = bake(trait, coef, layer)
        _log(f"  [tune] eval {trait} coef={coef} (dir {variant}) ...")
        subprocess.run(
            [sys.executable, "-m", "eval.eval_persona",
             "--model", variant, "--trait", trait, "--version", "eval",
             "--judge_model", JUDGE, "--coef", "0", "--output_path", csv_rel],
            cwd=PV_REPO, check=True, capture_output=True, text=True,
        )
    df = pd.read_csv(csv_abs)
    return float(df[trait].mean()), float(df["coherence"].mean())


def tune_trait(trait: str, layer: int, target_norm: float, max_evals: int):
    c = round(target_norm / vec_norm(trait, layer), 2)
    seen: list[tuple[float, float, float]] = []   # (coef, trait_score, coherence)
    for _ in range(max_evals):
        if any(abs(c - s[0]) < 1e-9 for s in seen):
            break
        ts, coh = eval_point(trait, c, layer)
        seen.append((c, ts, coh))
        _log(f"  [tune] {trait:14s} coef={c:<5} -> trait={ts:5.1f} coherence={coh:5.1f}")
        if coh >= 50 and ts >= 50:
            break
        c = round(c * (0.7 if coh < 50 else 1.3), 2)

    good = [s for s in seen if s[2] >= 50 and s[1] >= 50]
    coherent = [s for s in seen if s[2] >= 50]
    if good:
        best, review = max(good, key=lambda s: s[1]), False
    elif coherent:
        best, review = max(coherent, key=lambda s: s[1]), True
    else:
        best, review = max(seen, key=lambda s: s[2]), True
    return best, review, seen


def main() -> None:
    ap = argparse.ArgumentParser(description="Auto-tune per-trait steering coefs (baked+vLLM evals).")
    ap.add_argument("--traits", default=" ".join(config.TRAITS))
    ap.add_argument("--layer", type=int, default=16)
    ap.add_argument("--target-norm", type=float, default=None,
                     help="injection norm to start from (default: 2 * |goodness vec[16]|)")
    ap.add_argument("--max-evals", type=int, default=4)
    args = ap.parse_args()

    target = args.target_norm or 2 * vec_norm("goodness", 16)
    _log(f"[tune] layer={args.layer} target_norm={target:.3f} judge={JUDGE}")

    results = {}
    for trait in args.traits.split():
        best, review, seen = tune_trait(trait, args.layer, target, args.max_evals)
        results[trait] = (best, review, seen)

    env_path = os.path.join(REPO_ROOT, "persona_vector_steering", "tuned_coefs.env")
    md_path = os.path.join(REPO_ROOT, "persona_vector_steering", "tuned_coefs.md")
    with open(env_path, "w") as f:
        f.write(f"# auto-tuned by tune_coefs.py (layer {args.layer}, judge {JUDGE})\n")
        for trait, (best, review, _) in results.items():
            f.write(f"{trait}={best[0]}{'   # NEEDS REVIEW' if review else ''}\n")
    with open(md_path, "w") as f:
        f.write(f"# Tuned steering coefs (layer {args.layer})\n\n")
        f.write("| trait | coef | trait score | coherence | evals tried | needs review |\n|---|---|---|---|---|---|\n")
        for trait, (best, review, seen) in results.items():
            tried = ", ".join(f"c{s[0]}→{s[1]:.0f}/{s[2]:.0f}" for s in seen)
            f.write(f"| {trait} | {best[0]} | {best[1]:.1f} | {best[2]:.1f} | {tried} | {'YES' if review else ''} |\n")

    _log(f"\n[tune] wrote {env_path} and {md_path}")
    for trait, (best, review, _) in results.items():
        _log(f"  {trait:14s} coef={best[0]:<5} trait={best[1]:5.1f} coherence={best[2]:5.1f}"
             + ("  << NEEDS REVIEW" if review else ""))


if __name__ == "__main__":
    main()
