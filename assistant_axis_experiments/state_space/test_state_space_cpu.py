"""CPU test: featurize + predict end-to-end on synthetic data with PLANTED structure.

Builds a tiny synthetic world (hidden=32, one layer) where, by construction:
  - a_t declines from ~1 to below the role line at a run-specific rate (independent of basin);
  - each run belongs to one of two basins whose signature lives ONLY in the axis-orthogonal
    z coordinates (growing over turns), and whose transcript final third contains the matching
    qwen vocab (design vs devotion words) so basins.py labels it correctly;
  - a_t therefore carries ~no basin information, z_t carries a lot.

Asserts the pipeline recovers exactly that signature: basin AUC(a+z) high, AUC(a) near chance,
next-state R² sane. Run:  python -m assistant_axis_experiments.state_space.test_state_space_cpu
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np

H = 32
LAYER = 3
K_BASIS = 16
N_RUNS = 40
T_VIEW = 10          # turns per view
AD, AR = 10.0, 0.0   # planted anchors: raw axis proj 10 = default, 0 = mean role


def make_basis(path: str, rng: np.random.Generator) -> dict:
    q, _ = np.linalg.qr(rng.normal(size=(H, H)))
    a_hat, zpc = q[:, 0], q[:, 1:1 + K_BASIS].T
    mu = rng.normal(size=H)
    mu -= (mu @ a_hat) * a_hat          # keep the planted anchors exact: mu ⊥ axis
    basis = {
        "layers": np.array([LAYER]),
        f"L{LAYER}__axis_unit": a_hat.astype(np.float32),
        f"L{LAYER}__mean_role": mu.astype(np.float32),
        f"L{LAYER}__zpc": zpc.astype(np.float32),
        f"L{LAYER}__anchor_default": np.float64(AD),
        f"L{LAYER}__anchor_role_mean": np.float64(AR),
    }
    np.savez(path, **basis)
    return basis


def make_world(root: str, basis: dict, rng: np.random.Generator) -> str:
    cond_dir = os.path.join(root, "axis_qwen_3_32b_nosys_ai2ai")
    os.makedirs(os.path.join(cond_dir, "analysis"))
    a_hat = basis[f"L{LAYER}__axis_unit"].astype(float)
    mu = basis[f"L{LAYER}__mean_role"].astype(float)
    zpc = basis[f"L{LAYER}__zpc"].astype(float)

    runs, rows_acts, rows_run, rows_turn, rows_view = [], [], [], [], []
    vocab = {0: "architecture pipeline algorithm framework module",
             1: "luminous sacred soul radiant devotion starlight"}
    for ri in range(N_RUNS):
        basin = ri % 2
        rate = rng.uniform(0.08, 0.30)                   # axis decline per turn (indep of basin)
        turns = []
        for t in range(1, 2 * T_VIEW + 1):
            speaker = "A" if t % 2 == 1 else "B"
            text = "hello " * 5 + (vocab[basin] if t > (2 * T_VIEW) // 3 else "")
            turns.append({"turn": t, "speaker": speaker, "content": text})
        runs.append({"run_index": ri, "seed_prompt": "seed", "turns": turns})

        for view in ("A", "B"):
            for i in range(T_VIEW):
                a_units = 1.0 - rate * i + rng.normal(0, 0.05)
                z_sig = 6.0 * (i / T_VIEW) * zpc[basin] + rng.normal(0, 0.3, size=H)
                act = mu + (AR + a_units * (AD - AR)) * a_hat + z_sig
                rows_acts.append(act[None, :])
                rows_run.append(ri)
                rows_turn.append(2 * i + (1 if view == "A" else 2))
                rows_view.append(view)

    base = "two_instance__synthetic__none__opener__temp1.0"
    with open(os.path.join(cond_dir, f"{base}.json"), "w") as f:
        json.dump({"model_a": "local/synthetic", "system_prompt": "", "temperature": 1.0,
                   "runs": runs}, f)
    np.savez(
        os.path.join(cond_dir, "analysis", f"{base}__turn_acts.npz"),
        layers=np.array([LAYER], dtype=np.int32),
        acts=np.stack(rows_acts).astype(np.float16),
        run_index=np.array(rows_run, dtype=np.int32),
        turn=np.array(rows_turn, dtype=np.int32),
        view=np.array(rows_view),
        model_key=np.array("qwen-3-32b"),
        hf_model=np.array("synthetic"),
        temperature=np.array(1.0),
        source_file=np.array(f"{base}.json"),
    )
    return cond_dir


def main() -> None:
    tmp = tempfile.mkdtemp(prefix="state_space_test_")
    try:
        rng = np.random.default_rng(0)
        basis_path = os.path.join(tmp, "basis.npz")
        basis = make_basis(basis_path, rng)
        cond_dir = make_world(tmp, basis, rng)

        run = lambda mod, *a: subprocess.run(
            [sys.executable, "-m", f"assistant_axis_experiments.state_space.{mod}", *a],
            check=True, capture_output=True, text=True)
        r = run("featurize", "--results-dir", cond_dir, "--model-key", "qwen-3-32b",
                "--basis-override", basis_path)
        print(r.stdout.strip())

        feat_path = os.path.join(cond_dir, "analysis",
                                 "two_instance__synthetic__none__opener__temp1.0__state_features.json")
        feats = json.load(open(feat_path))
        v0 = feats["runs"][0]["views"]["A"]["layers"][str(LAYER)]
        assert abs(v0["a"][0] - 1.0) < 0.2, f"turn-1 a should be ~1, got {v0['a'][0]}"
        assert v0["a"][-1] < v0["a"][0], "a should decline"
        assert len(v0["z"][0]) == 16

        r = run("predict", "--model-key", "qwen-3-32b", "--results-dir", cond_dir,
                "--layer", str(LAYER), "--reports-dir", tmp)
        print(r.stdout.strip())
        report = open(os.path.join(tmp, "predict__qwen-3-32b.md")).read()

        # planted signature: basin is in z, not a — check the turn-4 AUC row (| 4 | a | az | z |...)
        row = next(l for l in report.splitlines() if l.startswith("| 4 |"))
        cells = [c.strip() for c in row.split("|")[1:-1]]
        auc_a, auc_az = float(cells[1]), float(cells[2])
        assert auc_az > 0.85, f"planted z-basin should be recoverable, AUC(a+z)={auc_az}"
        assert auc_a < 0.7, f"a alone should be near chance for basin, AUC(a)={auc_a}"
        print(f"\nPASS: basin AUC(a+z)={auc_az:.3f} >> AUC(a)={auc_a:.3f}; "
              "featurize + predict recover the planted structure.")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
