"""Verification for project_pvec + trait_rate — CPU-only, no GPU, no real npz needed.

Real activation npz files only exist on the pod, so the projection pipeline is exercised on a
fabricated fixture: a synthetic unsteer transcript (K=3) + matching fp16 npz for a steered and
a base pass + fake persona vectors, all written to a scratch dir. Checks (exit 1 on any failure):

1. projection math   : plant h = a * v_hat + orthogonal noise -> proj ~= a (and proj/cos agree
                       with a direct fp32 recomputation from the stored fp16 arrays)
2. join logic        : gen_model/steered_gen/own_pass on the K=3 switch design; switch_turn=3;
                       matched_trait from the condition name
3. run-quality guards: a never-switched unsteer run and a <4-turn run are flagged
                       degenerate_run on every row; healthy runs are not
4. real vectors      : goodness + loving load from PVEC_DIR as [33, 4096] with finite, positive
                       norms (skipped loudly if PVEC_DIR is absent on this machine)
5. trait_rate smoke  : real transcripts (loving_pvec_unsteer_k2_ai2ai@0.7) -> rows for every
                       turn, runs 3-5 flagged degenerate (skipped loudly if transcripts absent)

    python -m attractor_internals.verify_project_pvec [--scratch DIR]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile

import numpy as np

from . import config
from . import project_pvec as pp

COND = "loving_pvec_unsteer_k3_ai2ai"
TEMP = 0.7
STEERED_MODEL = "local/pvec:loving:1.32:16"
BASE_MODEL = "local2/base"
PLANT_A = 7.5  # planted projection magnitude
FIX_LAYERS = [8, 16, 24]


# ---------------------------------------------------------------------------
# Fixture: fake vectors + transcript + npz in a scratch dir.
# ---------------------------------------------------------------------------
def make_fake_vectors(pvec_dir: str, traits: list[str], rng) -> dict[str, np.ndarray]:
    import torch
    os.makedirs(pvec_dir, exist_ok=True)
    out = {}
    for t in traits:
        v = rng.standard_normal((33, config.D_MODEL)).astype(np.float32)
        torch.save(torch.from_numpy(v), os.path.join(pvec_dir, f"{t}_{config.PVEC_VARIANT}.pt"))
        out[t] = v
    return out


def make_transcript(path: str) -> dict:
    """3 runs: 0 = healthy K=3 switch (6 turns); 1 = never switches; 2 = only 2 turns."""
    def turns(n: int, n_steered: int) -> list[dict]:
        return [{"turn": k, "speaker": "A" if k % 2 == 1 else "B",
                 "model": STEERED_MODEL if k <= n_steered else BASE_MODEL,
                 "content": f"turn {k}", "content_clean": f"turn {k}"}
                for k in range(1, n + 1)]
    data = {"system_prompt": "sys", "runs": [
        {"run_index": 0, "seed_prompt": "seed", "turns": turns(6, 3)},
        {"run_index": 1, "seed_prompt": "seed", "turns": turns(6, 999)},   # never switched
        {"run_index": 2, "seed_prompt": "seed", "turns": turns(2, 999)},   # too short
    ]}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return data


def make_npz(acts_dir: str, data: dict, vectors: dict[str, np.ndarray], rng) -> np.ndarray:
    """One npz per pass with a row per (run, view, own turn). Returns the planted fp16 h.

    The planted row is (run 0, view A, turn 1) in the STEERED pass, layer 16, response_avg:
    h = PLANT_A * loving_hat + noise orthogonal to loving_hat.
    """
    os.makedirs(acts_dir, exist_ok=True)
    keys = [(run["run_index"], "A" if t["turn"] % 2 == 1 else "B", t["turn"])
            for run in data["runs"] for t in run["turns"]]
    n = len(keys)
    planted_fp16 = None
    for model_pass in ("steered", "base"):
        resp = rng.standard_normal((n, len(FIX_LAYERS), config.D_MODEL)).astype(np.float16)
        prom = rng.standard_normal((n, len(FIX_LAYERS), config.D_MODEL)).astype(np.float16)
        if model_pass == "steered":
            v = vectors["loving"][16].astype(np.float32)
            v_hat = v / np.linalg.norm(v)
            noise = rng.standard_normal(config.D_MODEL).astype(np.float32)
            noise -= (noise @ v_hat) * v_hat  # exactly orthogonal (up to fp32)
            i = keys.index((0, "A", 1))
            resp[i, FIX_LAYERS.index(16)] = (PLANT_A * v_hat + noise).astype(np.float16)
            planted_fp16 = resp[i, FIX_LAYERS.index(16)].copy()
        np.savez_compressed(
            os.path.join(acts_dir, f"{COND}__temp{TEMP:g}__{model_pass}.npz"),
            prompt_last=prom, response_avg=resp,
            run_index=np.array([k[0] for k in keys], dtype=np.int16),
            turn=np.array([k[2] for k in keys], dtype=np.int16),
            view=np.array([k[1] for k in keys]),
            layers=np.array(FIX_LAYERS, dtype=np.int16))
    return planted_fp16


# ---------------------------------------------------------------------------
# Checks over the emitted proj.jsonl.
# ---------------------------------------------------------------------------
def _row(rows, **kv):
    hits = [r for r in rows if all(r[k] == v for k, v in kv.items())]
    assert len(hits) == 1, f"expected 1 row for {kv}, got {len(hits)}"
    return hits[0]


def check_projection_math(rows, vectors, planted_fp16) -> bool:
    r = _row(rows, model_pass="steered", run_index=0, view="A", turn=1,
             layer=16, readout="response_avg")
    v = vectors["loving"][16].astype(np.float32)
    v_hat = v / np.linalg.norm(v)
    h = planted_fp16.astype(np.float32)
    exact = float(h @ v_hat)
    ok = True
    ok &= abs(r["traits"]["loving"]["proj"] - exact) < 1e-3
    ok &= abs(r["proj_matched"] - PLANT_A) < 0.05          # fp16 storage error only
    ok &= abs(r["cos_matched"] - exact / np.linalg.norm(h)) < 1e-4
    ok &= abs(r["proj_matched"] - r["traits"]["loving"]["proj"]) < 1e-9
    # an arbitrary control-trait row agrees with direct fp32 recomputation
    g_hat = vectors["goodness"][16].astype(np.float32)
    g_hat /= np.linalg.norm(g_hat)
    ok &= abs(r["traits"]["goodness"]["proj"] - float(h @ g_hat)) < 1e-3
    ok &= abs(r["proj_others_mean"] - r["traits"]["goodness"]["proj"]) < 1e-4  # 1 other trait
    print(f"  planted proj={r['proj_matched']:.4f} (a={PLANT_A}, exact fp32={exact:.4f}) "
          f"cos={r['cos_matched']:.4f} -> {'OK' if ok else 'MISMATCH'}")
    return ok


def check_join_logic(rows) -> bool:
    ok = True
    for turn in range(1, 7):
        view = "A" if turn % 2 == 1 else "B"
        steered = turn <= 3
        for model_pass in ("steered", "base"):
            r = _row(rows, model_pass=model_pass, run_index=0, view=view, turn=turn,
                     layer=16, readout="response_avg")
            ok &= r["gen_model"] == (STEERED_MODEL if steered else BASE_MODEL)
            ok &= r["steered_gen"] is steered
            ok &= r["own_pass"] is (steered if model_pass == "steered" else not steered)
            ok &= r["switch_turn"] == 3 and r["matched_trait"] == "loving"
    print(f"  K=3 switch: gen_model/steered_gen/own_pass/switch_turn/matched_trait "
          f"-> {'OK' if ok else 'MISMATCH'}")
    return ok


def check_degenerate(rows) -> bool:
    flags = {ri: {r["degenerate_run"] for r in rows if r["run_index"] == ri} for ri in (0, 1, 2)}
    ok = flags[0] == {False} and flags[1] == {True} and flags[2] == {True}
    print(f"  degenerate_run per run: {dict((k, sorted(v)) for k, v in flags.items())} "
          f"(want 0:False, 1:True never-switched, 2:True short) -> {'OK' if ok else 'MISMATCH'}")
    return ok


def check_real_vectors() -> bool | None:
    if not os.path.isdir(config.PVEC_DIR):
        print(f"  !! PVEC_DIR not found ({config.PVEC_DIR}) — real-vector check SKIPPED")
        return None
    vecs = pp.load_trait_vectors(["goodness", "loving"], config.PVEC_DIR)
    ok = True
    for t, v in vecs.items():
        norms = np.linalg.norm(v[config.LAYERS].astype(np.float32), axis=1)
        good = v.shape == (33, config.D_MODEL) and np.all(np.isfinite(norms)) and np.all(norms > 0)
        ok &= bool(good)
        print(f"  {t}: shape {list(v.shape)}, norms@L{config.LAYERS}="
              f"{[round(float(x), 2) for x in norms]} -> {'OK' if good else 'BAD'}")
    return ok


def check_trait_rate_smoke(scratch: str) -> bool | None:
    from . import onset, trait_rate
    condition, temp = "loving_pvec_unsteer_k2_ai2ai", 0.7
    files = config.condition_files(condition, [temp])
    if not files:
        print(f"  !! no transcripts for {condition}@{temp:g} — trait_rate smoke SKIPPED")
        return None
    sig = onset.signature_tokens(condition, temp, onset.base_common_words())
    if not sig:
        print(f"  !! no stage-1 signature tokens for {condition}@{temp:g} — SKIPPED")
        return None
    meta = trait_rate.rate_condition_temp(condition, temp, files[0][1], sig,
                                          os.path.join(scratch, "out_real"))
    with open(trait_rate.trait_rate_path(condition, temp, os.path.join(scratch, "out_real")),
              encoding="utf-8") as f:
        rows = [json.loads(line) for line in f]
    with open(files[0][1], encoding="utf-8") as f:
        n_turns = sum(len(r["turns"]) for r in json.load(f)["runs"])
    degen = {r["run_index"] for r in rows if r["degenerate_run"]}
    finite = all(np.isfinite(r["sig_rate_per_100"]) and r["sig_rate_per_100"] >= 0 for r in rows)
    ok = len(rows) == n_turns and degen == {3, 4, 5} and finite
    print(f"  {condition}@{temp:g}: {len(rows)} rows (= {n_turns} turns), "
          f"degenerate runs {sorted(degen)} (want [3, 4, 5]), rates finite={finite} "
          f"-> {'OK' if ok else 'MISMATCH'}")
    return ok


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--scratch", default=None, help="fixture dir (default: a fresh temp dir)")
    args = p.parse_args()
    scratch = args.scratch or tempfile.mkdtemp(prefix="verify_project_pvec_")
    os.makedirs(scratch, exist_ok=True)
    rng = np.random.default_rng(0)

    pvec_dir = os.path.join(scratch, "pvec")
    vectors = make_fake_vectors(pvec_dir, ["loving", "goodness"], rng)
    transcript_path = os.path.join(scratch, f"{COND}__temp{TEMP:g}.json")
    data = make_transcript(transcript_path)
    acts_dir = os.path.join(scratch, "out", "activations")
    planted_fp16 = make_npz(acts_dir, data, vectors, rng)

    out_dir = os.path.join(scratch, "out")
    npz_by_pass = pp.discover_npz(COND, TEMP, out_dir)
    assert sorted(npz_by_pass) == ["base", "steered"], f"npz discovery: {sorted(npz_by_pass)}"
    meta = pp.project_condition_temp(COND, TEMP, transcript_path, npz_by_pass,
                                     pp.load_trait_vectors(["loving", "goodness"], pvec_dir),
                                     FIX_LAYERS, out_dir, pvec_dir)
    with open(pp.proj_path(COND, TEMP, out_dir), encoding="utf-8") as f:
        rows = [json.loads(line) for line in f]
    # 14 own-turn rows x 2 passes x 3 layers x 2 readouts
    n_expected = 14 * 2 * 3 * 2
    print(f"fixture: {meta['n_rows']} rows (expected {n_expected}), "
          f"degenerate runs {meta['degenerate_runs']}")

    checks = [
        ("row count", meta["n_rows"] == n_expected and len(rows) == n_expected),
        ("projection math", check_projection_math(rows, vectors, planted_fp16)),
        ("join logic", check_join_logic(rows)),
        ("degenerate flags", check_degenerate(rows)),
        ("real vectors", check_real_vectors()),
        ("trait_rate smoke", check_trait_rate_smoke(scratch)),
    ]
    failed = [name for name, ok in checks if ok is False]
    skipped = [name for name, ok in checks if ok is None]
    print(f"\nVERIFY PROJECT_PVEC: {'FAIL: ' + ', '.join(failed) if failed else 'PASS'}"
          f"{' (skipped: ' + ', '.join(skipped) + ')' if skipped else ''}")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
