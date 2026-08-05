"""GPU extraction CLI: replay a condition's transcripts -> scalar features + activation readouts.

    python -m attractor_internals.extract_features --condition loving_ai2ai
    python -m attractor_internals.extract_features --condition base_ai2ai --temps 0.7 1.0
    python -m attractor_internals.extract_features --condition loving_ai2ai --runs 0-2 --limit-turns 6

Idempotent per (condition, temperature): existing outputs are skipped unless --force. For LoRA
conditions every (run, view) is replayed twice — under the adapter and with the adapter disabled
(same weights object, adapter toggled, so tokenization and spans are identical) — giving the
per-turn LoRA-vs-base NLL gap and the d_base displacement baseline for free.

pvec (activation-steered) conditions are analogous: two passes per (run, view) — "steered"
(replay.steering_hook re-applying coef * vec[layer], all positions, exactly what the steered
endpoint did) and "base" (no hook). Trait/coef/layer come from the transcript's per-turn
``model`` field (ground truth; unsteer condition names carry no coef). Because unsteer runs
switch endpoints mid-run, NEITHER pass is uniformly faithful — each scalar row's ``own_turn``
records whether its pass matches that turn's recorded generator. --skip-base-pass /
--skip-steered-pass drop either pass. base_pvec_ai2ai is base-served: single base pass.
"""

from __future__ import annotations

import argparse
import contextlib
import datetime
import json
import os
import time

from . import config, features_io, replay


def _parse_runs(spec: str | None) -> set[int] | None:
    if not spec:
        return None
    out: set[int] = set()
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return out


def _pass_context(model, model_pass: str, steer: tuple[str, float, int] | None = None):
    if model_pass == "base" and hasattr(model, "disable_adapter"):
        return model.disable_adapter()
    if model_pass == "steered":
        # Entered before replay registers its read hooks, so the captured readouts include the
        # injected vector (forward hooks fire in registration order — see replay.steering_hook).
        return replay.steering_hook(model, *steer)
    return contextlib.nullcontext()


def _transcript_steer(data: dict, spec) -> tuple[str, float, int]:
    """(trait, coef, layer) actually served, from the transcript's per-turn ``model`` fields.

    Ground truth for the steered pass: unsteer condition names carry no coef/layer, and the
    top-level model_a/model_b do not record the mid-run switch. Asserts exactly one pvec spec
    appears across all runs/turns and that it matches what the condition name does pin down.
    """
    seen = {config.parse_pvec_model(t["model"]) for run in data["runs"] for t in run["turns"]}
    seen.discard(None)
    if len(seen) != 1:
        raise ValueError(f"expected exactly one pvec model spec in the transcript, got {seen}")
    trait, coef, layer = next(iter(seen))
    if trait != spec.trait or (spec.coef is not None and coef != spec.coef) or \
            (spec.layer is not None and layer != spec.layer):
        raise ValueError(f"transcript steering pvec:{trait}:{coef}:{layer} contradicts "
                         f"condition spec {spec}")
    return trait, coef, layer


def extract_condition_temp(model, tokenizer, condition: str, temp: float, path: str,
                           passes: list[str], device: str, run_filter: set[int] | None,
                           limit_turns: int | None, out_dir: str) -> dict:
    """Replay every (run, view, pass) of one transcript file; write scalars + npz + meta."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    system_prompt = data["system_prompt"]
    lora_trait = config.condition_lora(condition)
    spec = config.condition_steering(condition)
    steer = _transcript_steer(data, spec) if spec is not None else None

    rows: list[dict] = []
    writers = {p: features_io.ActivationsWriter() for p in passes}
    n_fallback = 0
    skipped: list[list] = []
    t0 = time.time()

    for run in data["runs"]:
        if run_filter is not None and run["run_index"] not in run_filter:
            continue
        if limit_turns is not None:
            run = {**run, "turns": run["turns"][:limit_turns]}
        for view in ("A", "B"):
            messages, own = replay.build_view(run, system_prompt, run["seed_prompt"], view)
            gen_models = replay.own_turn_models(run, view)
            try:
                ser = replay.serialize_with_spans(tokenizer, messages, own)
            except replay.PrefixChainViolation as e:
                print(f"    run {run['run_index']} view {view}: {e} — per-turn fallback")
                ser = None
            for model_pass in passes:
                with _pass_context(model, model_pass, steer):
                    if ser is not None:
                        results = replay.replay_view_single_pass(model, ser, device)
                        for t in ser.skipped_empty_turns:
                            skipped.append([run["run_index"], view, t])
                    else:
                        results = replay.replay_view_per_turn(model, tokenizer, messages, own, device)
                        n_fallback += len(results)
                for r in results:
                    # own_turn: does this pass match the turn's recorded generator? pvec: steered
                    # pass owns the pvec-served turns, base pass the base-served ones (mixed in
                    # unsteer runs). LoRA: the adapter generated everything; plain base: trivially
                    # own. This is the per-turn faithfulness flag analyses should filter on.
                    if spec is not None:
                        turn_steered = config.parse_pvec_model(gen_models.get(r.turn, "")) is not None
                        own_turn = (model_pass == "steered") == turn_steered
                    else:
                        own_turn = model_pass != "base" or lora_trait is None
                    rows.append({
                        "condition": condition, "temperature": temp,
                        "run_index": run["run_index"], "view": view, "turn": r.turn,
                        "model_pass": model_pass, "n_reply_tokens": r.n_reply_tokens,
                        "nll_mean": round(r.nll_mean, 5), "nll_median": round(r.nll_median, 5),
                        "entropy_mean": round(r.entropy_mean, 5), "sat_frac": round(r.sat_frac, 5),
                        "mrr": round(r.mrr, 5), "nll_eot": round(r.nll_eot, 5),
                        "prefix_tokens": r.prefix_tokens, "fallback_per_turn": r.fallback_per_turn,
                        "own_turn": own_turn,
                    })
                    writers[model_pass].add(run["run_index"], view, r.turn, r.prompt_last, r.response_avg)
        print(f"  run {run['run_index']}: done ({time.time() - t0:.0f}s elapsed)")

    features_io.write_scalars(features_io.scalars_path(condition, temp, out_dir), rows)
    for model_pass, w in writers.items():
        w.save(features_io.activations_path(condition, temp, model_pass, out_dir))
    meta = {
        "condition": condition, "temperature": temp, "transcript": os.path.relpath(path, config.REPO_ROOT),
        "base_model": config.BASE_MODEL, "adapter": lora_trait,
        "steering": None if steer is None else
            {"trait": steer[0], "coef": steer[1], "layer": steer[2],
             "mode": spec.mode, "switch_turn": spec.switch_turn},
        "layers": config.LAYERS, "passes": passes, "n_rows": len(rows),
        "n_fallback_rows": n_fallback, "skipped_empty_turns": skipped,
        "elapsed_s": round(time.time() - t0, 1),
        "extracted_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "versions": _versions(),
    }
    features_io.write_meta(features_io.meta_path(condition, temp, out_dir), meta)
    print(f"  wrote {len(rows)} rows for {condition}@{temp:g} in {meta['elapsed_s']}s "
          f"(fallback rows: {n_fallback}, empty turns skipped: {len(skipped)})")
    return meta


def _versions() -> dict:
    import torch
    import transformers
    v = {"torch": torch.__version__, "transformers": transformers.__version__}
    try:
        import peft
        v["peft"] = peft.__version__
    except ImportError:
        pass
    return v


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--condition", required=True, help="results/<condition> to replay")
    p.add_argument("--temps", nargs="*", type=float, default=None, help="subset of temperatures")
    p.add_argument("--runs", default=None, help="run_index subset, e.g. '0-2' or '0,5,9'")
    p.add_argument("--limit-turns", type=int, default=None, help="truncate each run (smoke tests)")
    p.add_argument("--layers", nargs="*", type=int, default=None, help="override config.LAYERS")
    p.add_argument("--skip-base-pass", action="store_true",
                   help="LoRA/pvec conditions: skip the no-adapter/no-hook pass")
    p.add_argument("--skip-steered-pass", action="store_true",
                   help="pvec conditions: skip the steered pass (base pass only)")
    p.add_argument("--out-dir", default=config.OUT_DIR)
    p.add_argument("--force", action="store_true", help="re-extract even if outputs exist")
    args = p.parse_args()

    if args.layers:
        config.LAYERS = args.layers

    trait = config.condition_lora(args.condition)          # None for pvec conditions
    spec = config.condition_steering(args.condition)       # raises on unknown pvec shapes
    files = config.condition_files(args.condition, args.temps)
    if not files:
        raise SystemExit(f"no transcript files for {args.condition} (temps={args.temps})")
    if spec is not None:
        passes = [p for p in ("steered", "base")
                  if not (p == "steered" and args.skip_steered_pass)
                  and not (p == "base" and args.skip_base_pass)]
        if not passes:
            raise SystemExit("both --skip-steered-pass and --skip-base-pass: nothing to extract")
    elif trait:
        passes = ["adapter"] if args.skip_base_pass else ["adapter", "base"]
    else:
        passes = ["base"]

    device = config.pick_device()
    print(f"loading {config.BASE_MODEL} (adapter: {trait}) on {device} ...")
    model, tokenizer = replay.load_model_and_tokenizer(trait, device)

    run_filter = _parse_runs(args.runs)
    for temp, path in files:
        if not args.force and os.path.exists(features_io.meta_path(args.condition, temp, args.out_dir)):
            print(f"{args.condition}@{temp:g}: outputs exist — skipping (--force to redo)")
            continue
        print(f"== {args.condition}@{temp:g}: {os.path.basename(path)} (passes: {passes})")
        extract_condition_temp(model, tokenizer, args.condition, temp, path, passes,
                               device, run_filter, args.limit_turns, args.out_dir)


if __name__ == "__main__":
    main()
