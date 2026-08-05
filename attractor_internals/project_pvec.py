"""Offline persona-vector projections of the stored residual readouts — CPU-only, no replay.

For every stored readout h (activations/<cond>__temp<T>__<pass>.npz; response_avg and
prompt_last) and every persona-vector trait v: scalar projection ``proj = h . v / ||v||`` and
cosine ``cos = h . v / (||h|| ||v||)``, computed in fp32 with NO baseline subtraction — exactly
the persona-vectors paper's readout convention. v = ``<trait>_response_avg_diff.pt``[layer],
the un-normalized mean-difference direction at hidden_states[layer] (config.PVEC_DIR /
PVEC_VARIANT). All 12 traits are always projected — the condition's matched trait plus the 11
controls — so trait-specificity is a query, not a re-run.

Every row is joined against the source transcript so the analysis can condition on who actually
generated the turn (crucial for the *_pvec_unsteer_k<K>_* switch designs, where turns <= K were
generated steered and later turns by the plain base model):
  gen_model    : the turn's recorded generator string (e.g. "local/pvec:loving:1.32:16")
  steered_gen  : the generator was activation-steered ("pvec:" in gen_model)
  own_pass     : this row's extraction pass replays the model that generated the turn
  switch_turn  : K parsed from unsteer condition names, null otherwise
Run-quality guards: runs with < MIN_RUN_TURNS turns, or unsteer runs where no turn ever
switched to base (e.g. loving_pvec_unsteer_k2 runs 3-5, 1 turn each), are flagged
``degenerate_run`` on every row — never silently dropped.

    python -m attractor_internals.project_pvec --condition goodness_pvec_c2.0_l16_ai2ai
    python -m attractor_internals.project_pvec --condition loving_pvec_unsteer_k2_ai2ai --temps 0.7
    python -m attractor_internals.project_pvec --condition base_pvec_ai2ai --layers 16 --traits goodness loving

Writes features/<cond>__temp<T>__proj.jsonl, one row per
(run_index, view, turn, model_pass, layer, readout):
  condition, temperature, run_index, view ("A"|"B"), turn, model_pass, layer, readout,
  gen_model, steered_gen, own_pass, switch_turn, matched_trait, degenerate_run,
  proj_matched, cos_matched,           # convenience: the matched trait (null if none loaded)
  proj_others_mean, cos_others_mean,   # mean over the non-matched traits (all traits if none)
  traits: {trait: {"proj": float, "cos": float}}
plus features/<cond>__temp<T>__proj_meta.json (vector dir/variant/per-layer norms, layers,
passes, inputs). Idempotent per (condition, temperature) unless --force, like extract_features.
"""

from __future__ import annotations

import argparse
import datetime
import glob
import json
import os
import re

import numpy as np

from . import config, features_io

READOUTS = ("response_avg", "prompt_last")
MIN_RUN_TURNS = 4  # runs shorter than this carry no trajectory — flagged degenerate_run

_UNSTEER_RE = re.compile(r"_unsteer_k(\d+)_")


# ---------------------------------------------------------------------------
# Paths (proj outputs live next to the scalars; features_io is another agent's file).
# ---------------------------------------------------------------------------
def proj_path(condition: str, temp: float, out_dir: str | None = None) -> str:
    d = os.path.join(out_dir or config.OUT_DIR, "features")
    return os.path.join(d, f"{condition}__temp{temp:g}__proj.jsonl")


def proj_meta_path(condition: str, temp: float, out_dir: str | None = None) -> str:
    d = os.path.join(out_dir or config.OUT_DIR, "features")
    return os.path.join(d, f"{condition}__temp{temp:g}__proj_meta.json")


# ---------------------------------------------------------------------------
# Condition parsing + transcript join helpers.
# ---------------------------------------------------------------------------
def condition_trait(condition: str) -> str | None:
    """The condition's own trait ('goodness_pvec_c2.0_l16_ai2ai' -> 'goodness').

    None for base_pvec_ai2ai / base_ai2ai (no matched trait to project onto).
    """
    head = condition.split("_")[0]
    return head if head in config.PVEC_TRAITS else None


def switch_turn_of(condition: str) -> int | None:
    """K from '<trait>_pvec_unsteer_k<K>_ai2ai' (last steered turn), else None."""
    m = _UNSTEER_RE.search(condition)
    return int(m.group(1)) if m else None


def is_steered_model(gen_model: str | None) -> bool:
    """Was this turn generated under the activation-steering hook? ('local/pvec:trait:coef:layer')"""
    return bool(gen_model) and "pvec:" in gen_model


def generator_pass(gen_model: str | None, passes: list[str]) -> str | None:
    """Which extraction pass replays the model that actually generated this turn.

    Steered turns belong to the 'steered' pass; unsteered turns to 'adapter' when the condition
    was LoRA-served, else 'base'. None if the matching pass was not extracted.
    """
    if is_steered_model(gen_model):
        return "steered" if "steered" in passes else None
    for p in ("adapter", "base"):
        if p in passes:
            return p
    return None


def degenerate_runs(runs: list[dict], switch_turn: int | None) -> dict[int, bool]:
    """run_index -> degenerate flag: too short, or an unsteer run that never switched to base."""
    out: dict[int, bool] = {}
    for run in runs:
        bad = len(run["turns"]) < MIN_RUN_TURNS
        if switch_turn is not None and not any(
                not is_steered_model(t.get("model")) for t in run["turns"]):
            bad = True
        out[run["run_index"]] = bad
    return out


# ---------------------------------------------------------------------------
# Persona vectors.
# ---------------------------------------------------------------------------
def load_trait_vectors(traits: list[str], pvec_dir: str | None = None) -> dict[str, np.ndarray]:
    """trait -> [n_layers(33), D_MODEL] fp32 numpy. torch imported here only (vectors are tiny)."""
    import torch
    pvec_dir = pvec_dir or config.PVEC_DIR
    out: dict[str, np.ndarray] = {}
    for t in traits:
        path = os.path.join(pvec_dir, f"{t}_{config.PVEC_VARIANT}.pt")
        v = torch.load(path, map_location="cpu").float().numpy()
        if v.ndim != 2 or v.shape[1] != config.D_MODEL:
            raise ValueError(f"{path}: expected [n_layers, {config.D_MODEL}], got {list(v.shape)}")
        out[t] = v
    return out


# ---------------------------------------------------------------------------
# Core: one (condition, temperature) -> proj.jsonl + proj_meta.json.
# ---------------------------------------------------------------------------
def project_condition_temp(condition: str, temp: float, transcript_path: str,
                           npz_by_pass: dict[str, str], vectors: dict[str, np.ndarray],
                           layers: list[int], out_dir: str, pvec_dir: str) -> dict:
    """Project every stored readout row onto every trait vector and join transcript truth."""
    with open(transcript_path, encoding="utf-8") as f:
        data = json.load(f)
    turn_model = {(run["run_index"], t["turn"]): t.get("model")
                  for run in data["runs"] for t in run["turns"]}
    sw = switch_turn_of(condition)
    degen = degenerate_runs(data["runs"], sw)
    matched = condition_trait(condition)
    passes = sorted(npz_by_pass)

    # Unit directions once per (trait, layer), fp32 — proj = h . v/||v|| = h . v_hat.
    unit = {(t, layer): (V[layer].astype(np.float32) /
                         np.linalg.norm(V[layer].astype(np.float32)))
            for t, V in vectors.items() for layer in layers}

    rows: list[dict] = []
    parity_warned = 0
    for model_pass in passes:
        z = features_io.read_activations(npz_by_pass[model_pass])
        npz_layers = [int(x) for x in z["layers"]]
        missing = [x for x in layers if x not in npz_layers]
        if missing:
            raise ValueError(f"{npz_by_pass[model_pass]}: layers {missing} not stored "
                             f"(has {npz_layers})")
        n = len(z["turn"])
        for readout in READOUTS:
            for layer in layers:
                H = z[readout][:, npz_layers.index(layer), :].astype(np.float32)
                h_norm = np.linalg.norm(H, axis=1)
                projs = {t: H @ unit[(t, layer)] for t in vectors}
                for i in range(n):
                    ri, turn = int(z["run_index"][i]), int(z["turn"][i])
                    view = str(z["view"][i])
                    if (turn % 2 == 1) != (view == "A"):  # odd turns = A, even = B
                        parity_warned += 1
                    gen = turn_model.get((ri, turn))
                    gp = generator_pass(gen, passes)
                    tmap = {t: {"proj": round(float(projs[t][i]), 5),
                                "cos": round(float(projs[t][i]) / max(float(h_norm[i]), 1e-9), 6)}
                            for t in vectors}
                    others = [t for t in vectors if t != matched]
                    rows.append({
                        "condition": condition, "temperature": temp,
                        "run_index": ri, "view": view, "turn": turn,
                        "model_pass": model_pass, "layer": layer, "readout": readout,
                        "gen_model": gen, "steered_gen": is_steered_model(gen),
                        "own_pass": (model_pass == gp) if gp is not None else None,
                        "switch_turn": sw, "matched_trait": matched,
                        "degenerate_run": bool(degen.get(ri, False)),
                        "proj_matched": tmap[matched]["proj"] if matched in tmap else None,
                        "cos_matched": tmap[matched]["cos"] if matched in tmap else None,
                        "proj_others_mean": round(float(np.mean([tmap[t]["proj"] for t in others])), 5) if others else None,
                        "cos_others_mean": round(float(np.mean([tmap[t]["cos"] for t in others])), 6) if others else None,
                        "traits": tmap,
                    })
    if parity_warned:
        print(f"!! {parity_warned} rows violate the odd=A/even=B turn-parity convention — "
              "check the npz view/turn arrays")

    path = proj_path(condition, temp, out_dir)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")

    rel = os.path.relpath(transcript_path, config.REPO_ROOT)
    meta = {
        "condition": condition, "temperature": temp,
        "transcript": rel if not rel.startswith("..") else transcript_path,
        "pvec_dir": pvec_dir, "pvec_variant": config.PVEC_VARIANT,
        "traits": sorted(vectors), "matched_trait": matched, "switch_turn": sw,
        "layers": layers, "readouts": list(READOUTS), "passes": passes,
        "npz": {p: os.path.basename(npz_by_pass[p]) for p in passes},
        "vector_norms": {t: {str(layer): round(float(np.linalg.norm(vectors[t][layer])), 4)
                             for layer in layers} for t in sorted(vectors)},
        "degenerate_runs": sorted(ri for ri, bad in degen.items() if bad),
        "n_rows": len(rows),
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "versions": {"numpy": np.__version__},
    }
    features_io.write_meta(proj_meta_path(condition, temp, out_dir), meta)
    return meta


def discover_npz(condition: str, temp: float, out_dir: str) -> dict[str, str]:
    """model_pass -> npz path for one (condition, temp) — steered/base/adapter, whatever exists."""
    d = os.path.join(out_dir, "activations")
    prefix = f"{condition}__temp{temp:g}__"
    return {os.path.basename(p)[len(prefix):-len(".npz")]: p
            for p in sorted(glob.glob(os.path.join(d, prefix + "*.npz")))}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--condition", required=True, help="results/<condition> to project")
    p.add_argument("--temps", nargs="*", type=float, default=None, help="subset of temperatures")
    p.add_argument("--layers", nargs="*", type=int, default=None, help="override config.LAYERS")
    p.add_argument("--traits", nargs="*", default=None, help="override config.PVEC_TRAITS")
    p.add_argument("--out-dir", default=config.OUT_DIR)
    p.add_argument("--force", action="store_true", help="re-project even if outputs exist")
    args = p.parse_args()

    layers = args.layers or config.LAYERS
    traits = args.traits or config.PVEC_TRAITS
    files = config.condition_files(args.condition, args.temps)
    if not files:
        raise SystemExit(f"no transcript files for {args.condition} (temps={args.temps})")
    if not os.path.isdir(config.PVEC_DIR):
        raise SystemExit(f"persona-vector dir not found: {config.PVEC_DIR} (set PVEC_DIR)")
    vectors = load_trait_vectors(traits)

    for temp, path in files:
        if not args.force and os.path.exists(proj_meta_path(args.condition, temp, args.out_dir)):
            print(f"{args.condition}@{temp:g}: proj outputs exist — skipping (--force to redo)")
            continue
        npz_by_pass = discover_npz(args.condition, temp, args.out_dir)
        if not npz_by_pass:
            print(f"{args.condition}@{temp:g}: no activation npz — run extract_features on the pod first")
            continue
        meta = project_condition_temp(args.condition, temp, path, npz_by_pass, vectors,
                                      layers, args.out_dir, config.PVEC_DIR)
        print(f"wrote {meta['n_rows']} rows for {args.condition}@{temp:g} "
              f"(passes: {meta['passes']}, degenerate runs: {meta['degenerate_runs']})")


if __name__ == "__main__":
    main()
