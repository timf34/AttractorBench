"""Auto-tune per-trait steering coefficients using the FAST baked+vLLM eval path.

The persona vectors are raw (un-normalized) mean-diffs and traits differ in sensitivity, so one
global coef does NOT transfer across traits (measured: goodness c2/l16 -> trait 95.5 / coherence
93.7, but sarcasm c2/l16 -> 30.4 / 10.8). This driver finds, per trait, a coef that induces the
persona while staying coherent, using the same selection rule as persona_vectors'
scripts/eval_llama.sh ("strongest coef whose coherence stays >= ~50") — but each (trait, coef)
point costs ~4 min instead of an HF hook sweep, because it bakes the vector into a checkpoint
(bake.py, ~2 s) and evaluates through vLLM (eval_persona --coef 0 on the baked dir).

Search: bracket + bisect on the coherence cliff. Coherence is (approximately) monotone decreasing
in coef, so the coherent/incoherent boundary is findable by binary search; the final pick is then
the coherent point with the HIGHEST TRAIT SCORE (trait strength is not monotone in coef — judged
trait expression drops as the text degrades near the cliff):
  1. bracket: start at the norm-matched coef c0 = TARGET_NORM / |vec[layer]| (TARGET_NORM defaults
     to goodness's known-good injection, 2 * |goodness_vec[16]|). If coherent, probe up (*1.5)
     until incoherent; if incoherent, probe down (*0.5) until coherent -> a [lo(coherent),
     hi(incoherent)] bracket.
  2. bisect: evaluate the geometric midpoint sqrt(lo*hi); coherent -> lo=mid, else hi=mid. Stop
     when hi/lo <= 1.15 or the --max-evals budget is spent.
The answer is lo — the strongest observed coherent coef. needs_review flags traits where no
coherent point was found, or where the trait score at lo stayed < 50.

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


COH_OK = 50.0      # eval_llama.sh's rule: strongest coef whose coherence stays >= ~50
BRACKET_DONE = 1.15  # stop bisecting once hi/lo is this tight


def tune_trait(trait: str, layer: int, target_norm: float, max_evals: int):
    seen: list[tuple[float, float, float]] = []   # (coef, trait_score, coherence), in eval order

    def ev(c: float) -> tuple[float, float]:
        c = round(c, 2)
        for s in seen:
            if abs(s[0] - c) < 1e-9:
                return s[1], s[2]
        ts, coh = eval_point(trait, c, layer)
        seen.append((c, ts, coh))
        _log(f"  [tune] {trait:14s} coef={c:<5} -> trait={ts:5.1f} coherence={coh:5.1f}")
        return ts, coh

    budget = lambda: len(seen) < max_evals  # noqa: E731

    # --- 1. bracket the coherence cliff ---------------------------------------------------------
    lo = hi = None                                # lo: coherent coef, hi: incoherent coef
    c = round(target_norm / vec_norm(trait, layer), 2)
    _, coh = ev(c)
    if coh >= COH_OK:
        lo = c
        while budget() and hi is None:
            c = round(c * 1.5, 2)
            _, coh = ev(c)
            if coh >= COH_OK:
                lo = c
            else:
                hi = c
    else:
        hi = c
        while budget() and lo is None:
            c = round(c * 0.5, 2)
            _, coh = ev(c)
            if coh >= COH_OK:
                lo = c
            else:
                hi = c

    # --- 2. bisect (geometric midpoint) ---------------------------------------------------------
    while budget() and lo is not None and hi is not None and hi / lo > BRACKET_DONE:
        mid = round((lo * hi) ** 0.5, 2)
        if abs(mid - lo) < 0.01 or abs(mid - hi) < 0.01:
            break
        _, coh = ev(mid)
        if coh >= COH_OK:
            lo = mid
        else:
            hi = mid

    coherent = [s for s in seen if s[2] >= COH_OK]
    if coherent:
        # maximize trait expression SUBJECT TO coherence >= 50 — trait score is not monotone in
        # coef (judges can't read a persona in degrading text), so the strongest coherent coef can
        # score worse than a milder one (measured: honesty c1.85 -> 94 trait / 92 coh, but
        # c2.78 -> 68 / 59). Tie-break toward the stronger coef.
        best = max(coherent, key=lambda s: (s[1], s[0]))
        review = best[1] < 50                       # persona didn't take despite coherence
    else:
        best, review = max(seen, key=lambda s: s[2]), True
    return best, review, seen


def main() -> None:
    ap = argparse.ArgumentParser(description="Auto-tune per-trait steering coefs (baked+vLLM evals).")
    ap.add_argument("--traits", default=" ".join(config.TRAITS))
    ap.add_argument("--layer", type=int, default=16)
    ap.add_argument("--target-norm", type=float, default=None,
                     help="injection norm to start from (default: 2 * |goodness vec[16]|)")
    ap.add_argument("--max-evals", type=int, default=7)
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
