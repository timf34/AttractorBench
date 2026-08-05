"""Replay verification — run BEFORE any full extraction sweep.

Two modes:

CPU (tokenizer only, laptop-runnable, no torch model):
    python -m attractor_internals.verify_replay --cpu-check [--condition X --temp T]
  Checks the prefix-chain property and reply-span decode fidelity over EVERY (run, view) of the
  check conditions (loving_ai2ai@0.7 + base_ai2ai@1.0 by default; --condition overrides) — the
  load-bearing assumption behind the single-pass replay, verified against real transcripts
  without a GPU. Steering never changes tokenization, so this check covers pvec conditions too.

GPU (on-pod smoke, gates the overnight sweep):
    python -m attractor_internals.verify_replay --condition loving_ai2ai --temp 0.7
  1. Equivalence: per-turn growing-prefix passes vs the single full pass on 1 run x N turns —
     NLL within rtol, readout cosine ~ 1. Exit code 1 on failure (pod script hard-aborts).
  2. Template fidelity: the model should recognize its own generations — median own-turn NLL
     below FIDELITY_MAX_MEDIAN_NLL, MRR above FIDELITY_MIN_MRR, and (LoRA) adapter-NLL below
     base-NLL. Failure writes reports/FIDELITY_WARNING.md and exits 0 (loud, not fatal).
  3. Telemetry: seconds/pass and peak VRAM, to sanity-check the GPU-hour budget.
"""

from __future__ import annotations

import argparse
import contextlib
import json
import os
import statistics
import time

from . import config, replay

CPU_CHECK_CONDITIONS = [("loving_ai2ai", 0.7), ("base_ai2ai", 1.0)]


# ---------------------------------------------------------------------------
# CPU check — tokenizer only.
# ---------------------------------------------------------------------------
def cpu_check(conditions: list[tuple[str, float]] | None = None) -> int:
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(config.BASE_MODEL)

    total_views = violations = decode_mismatches = total_turns = empty_turns = 0
    for condition, temp in conditions or CPU_CHECK_CONDITIONS:
        files = config.condition_files(condition, [temp])
        if not files:
            print(f"!! no transcripts for {condition}@{temp:g} — skipping")
            continue
        _, path = files[0]
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        for run in data["runs"]:
            for view in ("A", "B"):
                total_views += 1
                messages, own = replay.build_view(run, data["system_prompt"], run["seed_prompt"], view)
                try:
                    ser = replay.serialize_with_spans(tokenizer, messages, own)
                except replay.PrefixChainViolation as e:
                    violations += 1
                    print(f"!! PREFIX VIOLATION {condition}@{temp:g} run {run['run_index']} view {view}: {e}")
                    continue
                empty_turns += len(ser.skipped_empty_turns)
                for span in ser.spans:
                    total_turns += 1
                    decoded = tokenizer.decode(ser.ids_full[span.reply_start:span.reply_end])
                    expected = messages[span.msg_index]["content"].strip()
                    if decoded != expected:
                        decode_mismatches += 1
                        print(f"!! DECODE MISMATCH {condition}@{temp:g} run {run['run_index']} "
                              f"view {view} turn {span.turn}")
        print(f"{condition}@{temp:g}: checked")

    print(f"\nviews checked: {total_views} | prefix violations: {violations} | "
          f"turns checked: {total_turns} | decode mismatches: {decode_mismatches} | "
          f"empty turns: {empty_turns}")
    ok = violations == 0 and decode_mismatches == 0
    print("CPU CHECK:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


# ---------------------------------------------------------------------------
# GPU smoke.
# ---------------------------------------------------------------------------
def gpu_smoke(condition: str, temp: float, n_turns: int, rtol: float, min_cos: float) -> int:
    import numpy as np
    import torch

    trait = config.condition_lora(condition)
    spec = config.condition_steering(condition)
    files = config.condition_files(condition, [temp])
    if not files:
        raise SystemExit(f"no transcripts for {condition}@{temp:g}")
    _, path = files[0]
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    run = data["runs"][0]
    device = config.pick_device()

    from .extract_features import _transcript_steer
    steer = _transcript_steer(data, spec) if spec is not None else None

    print(f"loading {config.BASE_MODEL} (adapter: {trait}, steering: {steer}) on {device} ...")
    model, tokenizer = replay.load_model_and_tokenizer(trait, device)
    messages, own = replay.build_view(run, data["system_prompt"], run["seed_prompt"], "A")

    # --- 1. equivalence: single-pass vs per-turn on the first n_turns own turns -------------
    # pvec conditions are smoked under the "steered" pass (hook entered before the read hooks,
    # matching extraction). Equivalence is checked within the same pass, so it stays valid.
    ser = replay.serialize_with_spans(tokenizer, messages, own)  # raises on violation = fail
    if device == "cuda":
        torch.cuda.reset_peak_memory_stats()
    ctx = replay.steering_hook(model, *steer) if steer is not None else contextlib.nullcontext()
    with ctx:
        t0 = time.time()
        single = replay.replay_view_single_pass(model, ser, device)
        t_single = time.time() - t0
        t0 = time.time()
        per_turn = replay.replay_view_per_turn(model, tokenizer, messages, own, device, max_turns=n_turns)
        t_per_turn = time.time() - t0

    equiv_ok = True
    for pt in per_turn:
        sp = next(r for r in single if r.turn == pt.turn)
        nll_rel = abs(sp.nll_mean - pt.nll_mean) / max(abs(pt.nll_mean), 1e-6)
        cos = float(np.sum(sp.prompt_last * pt.prompt_last, axis=1).mean() /
                    (np.linalg.norm(sp.prompt_last, axis=1) * np.linalg.norm(pt.prompt_last, axis=1)).mean())
        ok = nll_rel <= rtol and cos >= min_cos
        equiv_ok &= ok
        print(f"  turn {pt.turn}: nll single={sp.nll_mean:.4f} per-turn={pt.nll_mean:.4f} "
              f"(rel {nll_rel:.2e}) | readout cos={cos:.5f} | {'OK' if ok else 'MISMATCH'}")
    print(f"EQUIVALENCE: {'PASS' if equiv_ok else 'FAIL'} "
          f"(single pass {t_single:.1f}s for {len(single)} turns; "
          f"per-turn {t_per_turn:.1f}s for {len(per_turn)} turns)")

    # --- 2. template fidelity ----------------------------------------------------------------
    med_nll = statistics.median(r.nll_median for r in single)
    mean_mrr = statistics.mean(r.mrr for r in single)
    checks = [
        (f"median own-turn nll_median = {med_nll:.3f} < {config.FIDELITY_MAX_MEDIAN_NLL}",
         med_nll < config.FIDELITY_MAX_MEDIAN_NLL),
        (f"mean own-turn mrr = {mean_mrr:.3f} > {config.FIDELITY_MIN_MRR}",
         mean_mrr > config.FIDELITY_MIN_MRR),
    ]
    if trait:
        with model.disable_adapter():
            base = replay.replay_view_single_pass(model, ser, device)
        adapter_nll = statistics.mean(r.nll_mean for r in single)
        base_nll = statistics.mean(r.nll_mean for r in base)
        checks.append((f"adapter nll {adapter_nll:.3f} < base nll {base_nll:.3f} on own transcript",
                       adapter_nll < base_nll))
    elif steer is not None and spec.mode == "forever":
        # Steer-forever analog of the adapter check (skipped for unsteer: neither pass is
        # uniformly the transcript's own model, so the comparison has no expected sign).
        base = replay.replay_view_single_pass(model, ser, device)  # no hook = base pass
        steered_nll = statistics.mean(r.nll_mean for r in single)
        base_nll = statistics.mean(r.nll_mean for r in base)
        checks.append((f"steered nll {steered_nll:.3f} < base nll {base_nll:.3f} on own transcript",
                       steered_nll < base_nll))
    fidelity_ok = all(ok for _, ok in checks)
    for desc, ok in checks:
        print(f"  fidelity: {desc} -> {'OK' if ok else 'FAIL'}")
    if not fidelity_ok:
        os.makedirs(config.REPORTS_DIR, exist_ok=True)
        warn = os.path.join(config.REPORTS_DIR, "FIDELITY_WARNING.md")
        with open(warn, "w", encoding="utf-8") as f:
            f.write(f"# Template-fidelity warning — {condition}@{temp:g}\n\n"
                    "The replayed model does not confidently predict its own transcript. The chat\n"
                    "template used for replay may differ from what vLLM served at generation time.\n"
                    "All downstream NLL/entropy features are suspect; MRR is the most robust.\n\n"
                    + "\n".join(f"- {desc}: {'OK' if ok else 'FAIL'}" for desc, ok in checks) + "\n")
        print(f"FIDELITY: FAIL — wrote {warn} (continuing; not fatal)")
    else:
        print("FIDELITY: PASS")

    # --- 3. telemetry -------------------------------------------------------------------------
    if device == "cuda":
        peak_gb = torch.cuda.max_memory_allocated() / 1e9
        print(f"TELEMETRY: {t_single:.1f}s / full-conversation pass | peak VRAM {peak_gb:.1f} GB | "
              f"~{t_single * 240 / 3600:.1f} GPU-h per LoRA condition (240 passes)")
    return 0 if equiv_ok else 1


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--cpu-check", action="store_true", help="tokenizer-only prefix-chain check")
    p.add_argument("--condition", default=None,
                   help="GPU smoke condition (default loving_ai2ai); with --cpu-check, "
                        "overrides the default check-condition list")
    p.add_argument("--temp", type=float, default=0.7)
    p.add_argument("--n-turns", type=int, default=3, help="own turns for the equivalence check")
    p.add_argument("--rtol", type=float, default=1e-2)
    p.add_argument("--min-cos", type=float, default=0.999)
    args = p.parse_args()

    if args.cpu_check:
        conds = [(args.condition, args.temp)] if args.condition else None
        raise SystemExit(cpu_check(conds))
    raise SystemExit(gpu_smoke(args.condition or "loving_ai2ai", args.temp, args.n_turns,
                               args.rtol, args.min_cos))


if __name__ == "__main__":
    main()
