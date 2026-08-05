"""Schemas + readers/writers for the extraction outputs.

Two artifact kinds per (condition, temperature):
- scalars  : features/<cond>__temp<T>__scalars.jsonl — one row per (run, view, turn, model_pass)
- readouts : activations/<cond>__temp<T>__<model_pass>.npz — fp16 residual-stream readouts
plus features/<cond>__temp<T>__meta.json recording provenance + the fidelity summary.

Scalar row keys (all always present):
  condition, temperature, run_index, view ("A"|"B"), turn (1-based, the speaker's own turn),
  model_pass ("adapter"|"base"|"steered"), n_reply_tokens, nll_mean, nll_median, entropy_mean,
  sat_frac, mrr, nll_eot, prefix_tokens (context length at the readout — for the length
  confound control),
  fallback_per_turn (bool: prefix-chain assert failed and this row came from a per-turn pass),
  own_turn (bool: this row's model_pass matches the turn's recorded generator — always True for
  single-pass conditions; in pvec unsteer conditions it flags which of the steered/base passes
  is faithful for each turn). Validated at WRITE time only, so pre-own_turn artifacts on disk
  stay readable.

npz arrays:
  prompt_last  : [n_rows, len(LAYERS), D_MODEL] fp16 — h at the last generation-header token
  response_avg : [n_rows, len(LAYERS), D_MODEL] fp16 — mean h over the turn's reply tokens
  run_index, turn : [n_rows] int16;  view : [n_rows] "A"/"B" (unicode)
  layers : the LAYERS list the axes correspond to
"""

from __future__ import annotations

import json
import os

import numpy as np

from . import config

SCALAR_KEYS = [
    "condition", "temperature", "run_index", "view", "turn", "model_pass",
    "n_reply_tokens", "nll_mean", "nll_median", "entropy_mean", "sat_frac", "mrr",
    "nll_eot", "prefix_tokens", "fallback_per_turn", "own_turn",
]


def _temp_tag(temp: float) -> str:
    return f"{temp:g}"


def scalars_path(condition: str, temp: float, out_dir: str | None = None) -> str:
    d = os.path.join(out_dir or config.OUT_DIR, "features")
    return os.path.join(d, f"{condition}__temp{_temp_tag(temp)}__scalars.jsonl")


def meta_path(condition: str, temp: float, out_dir: str | None = None) -> str:
    d = os.path.join(out_dir or config.OUT_DIR, "features")
    return os.path.join(d, f"{condition}__temp{_temp_tag(temp)}__meta.json")


def activations_path(condition: str, temp: float, model_pass: str, out_dir: str | None = None) -> str:
    d = os.path.join(out_dir or config.OUT_DIR, "activations")
    return os.path.join(d, f"{condition}__temp{_temp_tag(temp)}__{model_pass}.npz")


def write_scalars(path: str, rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            missing = [k for k in SCALAR_KEYS if k not in r]
            if missing:
                raise ValueError(f"scalar row missing keys {missing}: {r}")
            f.write(json.dumps(r) + "\n")


def read_scalars(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def read_all_scalars(conditions: list[str], out_dir: str | None = None) -> list[dict]:
    """Every scalar row for the given conditions (all temps found on disk)."""
    d = os.path.join(out_dir or config.OUT_DIR, "features")
    rows: list[dict] = []
    for cond in conditions:
        import glob
        for path in sorted(glob.glob(os.path.join(d, f"{cond}__temp*__scalars.jsonl"))):
            rows.extend(read_scalars(path))
    return rows


def write_meta(path: str, meta: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)


class ActivationsWriter:
    """Accumulates per-(run, view, turn) readouts and saves one fp16 npz."""

    def __init__(self) -> None:
        self.prompt_last: list[np.ndarray] = []   # each [len(LAYERS), D_MODEL]
        self.response_avg: list[np.ndarray] = []
        self.run_index: list[int] = []
        self.turn: list[int] = []
        self.view: list[str] = []

    def add(self, run_index: int, view: str, turn: int,
            prompt_last: np.ndarray, response_avg: np.ndarray) -> None:
        self.prompt_last.append(prompt_last.astype(np.float16))
        self.response_avg.append(response_avg.astype(np.float16))
        self.run_index.append(run_index)
        self.turn.append(turn)
        self.view.append(view)

    def save(self, path: str) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        np.savez_compressed(
            path,
            prompt_last=np.stack(self.prompt_last) if self.prompt_last else
                np.zeros((0, len(config.LAYERS), config.D_MODEL), dtype=np.float16),
            response_avg=np.stack(self.response_avg) if self.response_avg else
                np.zeros((0, len(config.LAYERS), config.D_MODEL), dtype=np.float16),
            run_index=np.array(self.run_index, dtype=np.int16),
            turn=np.array(self.turn, dtype=np.int16),
            view=np.array(self.view),
            layers=np.array(config.LAYERS, dtype=np.int16),
        )


def read_activations(path: str) -> dict:
    with np.load(path) as z:
        return {k: z[k] for k in z.files}
