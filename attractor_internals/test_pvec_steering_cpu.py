"""CPU tests for pvec-steering replay support — laptop-runnable, never loads the 8B model.

    python -m attractor_internals.test_pvec_steering_cpu

Covers:
(a) condition-name parsing: all three pvec shapes (steer-forever, unsteer, base_pvec control)
    plus LoRA/base conditions unchanged, and the per-turn model-string DSL;
(b) the steering hook on a toy model: the vector is added at the right decoder block, at ALL
    positions, and the read hooks (registered after it, as extraction does) capture the
    POST-injection hidden state — the registration-order property the design depends on;
(c) per-turn model parsing against a real unsteer transcript — the ground truth of the mid-run
    endpoint switch — including the known-broken 1-turn runs.

Real persona vectors are looked up via config.PVEC_DIR (set the env var to point at the local
persona_vectors checkout); that section is skipped with a notice if the directory is absent.
"""

from __future__ import annotations

import json
import os
import tempfile

from . import config, replay
from .extract_features import _transcript_steer


def test_condition_parsing() -> None:
    S = config.SteeringSpec
    # steer-forever: coef/layer in the name (with and without a trailing .0)
    assert config.condition_steering("goodness_pvec_c2.0_l16_ai2ai") == S("goodness", 2.0, 16, "forever")
    assert config.condition_steering("goodness_pvec_c2_l16_ai2ai") == S("goodness", 2.0, 16, "forever")
    assert config.condition_steering("loving_pvec_c1.32_l16_ai2ai") == S("loving", 1.32, 16, "forever")
    # unsteer: only trait + switch turn in the name; coef/layer come from the transcript
    assert config.condition_steering("loving_pvec_unsteer_k2_ai2ai") == S("loving", None, None, "unsteer", 2)
    assert config.condition_steering("nonchalance_pvec_unsteer_k24_ai2ai") == \
        S("nonchalance", None, None, "unsteer", 24)
    # base_pvec control and non-pvec conditions: no steering
    assert config.condition_steering("base_pvec_ai2ai") is None
    assert config.condition_steering("loving_ai2ai") is None
    assert config.condition_steering("base_ai2ai") is None
    # condition_lora: unchanged for LoRA/base, None (not a raise) for every pvec shape
    assert config.condition_lora("loving_ai2ai") == "loving"
    assert config.condition_lora("base_ai2ai") is None
    assert config.condition_lora("goodness_pvec_c2.0_l16_ai2ai") is None
    assert config.condition_lora("loving_pvec_unsteer_k2_ai2ai") is None
    assert config.condition_lora("base_pvec_ai2ai") is None
    # unknown pvec shapes still fail loudly through both entry points
    for fn in (config.condition_steering, config.condition_lora):
        try:
            fn("foo_pvec_bogus_ai2ai")
            raise AssertionError("unknown pvec shape did not raise")
        except ValueError:
            pass
    # per-turn model-string DSL
    assert config.parse_pvec_model("local/pvec:loving:1.32:16") == ("loving", 1.32, 16)
    assert config.parse_pvec_model("pvec:goodness:2:16") == ("goodness", 2.0, 16)
    assert config.parse_pvec_model("local/pvec:sarcasm:3") == ("sarcasm", 3.0, 16)  # default layer
    assert config.parse_pvec_model("local2/base") is None
    assert config.parse_pvec_model("local/base") is None
    assert config.parse_pvec_model("base") is None
    assert config.parse_pvec_model("") is None
    print("test_condition_parsing: OK")


# ---------------------------------------------------------------------------
# Toy model with the same module layout replay relies on (model.model.layers / .norm).
# ---------------------------------------------------------------------------
def _toy_model(n_blocks: int, d: int):
    import torch.nn as nn

    class _Block(nn.Module):
        def forward(self, x):
            return (x + 1.0,)  # tuple output, like HF decoder layers

    class _Inner(nn.Module):
        def __init__(self):
            super().__init__()
            self.embed = nn.Embedding(64, d)
            self.layers = nn.ModuleList(_Block() for _ in range(n_blocks))
            self.norm = nn.Identity()

    class _Toy(nn.Module):
        def __init__(self):
            super().__init__()
            self.model = _Inner()

        def forward(self, input_ids, use_cache=False, logits_to_keep=1):
            x = self.model.embed(input_ids)
            for blk in self.model.layers:
                x = blk(x)[0]
            return self.model.norm(x)

    return _Toy().eval()


def test_steering_hook_toy() -> None:
    import torch

    n_blocks, d, coef, layer = 4, 8, 2.0, 2   # inject at hidden_states[2] = block 1's output
    saved_layers, saved_dir = config.LAYERS, config.PVEC_DIR
    tmpdir = tempfile.mkdtemp(prefix="pvec_toy_")
    try:
        config.LAYERS = [1, 2, 4]             # taps before, at, and after the injection layer
        config.PVEC_DIR = tmpdir
        torch.manual_seed(0)
        vec = torch.randn(n_blocks + 1, d)
        torch.save(vec, config.pvec_path("toy"))

        model = _toy_model(n_blocks, d)
        ids = [1, 2, 3, 4, 5]
        base = replay._forward_with_taps(model, ids, "cpu")
        with replay.steering_hook(model, "toy", coef, layer):
            steered = replay._forward_with_taps(model, ids, "cpu")
        after = replay._forward_with_taps(model, ids, "cpu")

        add = coef * vec[layer]
        # Read hook on the SAME block captures the post-injection value (registration order):
        assert torch.allclose(steered[2], base[2] + add, atol=1e-6)
        # ... at every position, not just the last (all-positions intervention):
        assert steered[2].shape == (len(ids), d)
        for p in range(len(ids)):
            assert torch.allclose(steered[2][p] - base[2][p], add, atol=1e-6)
        # Upstream taps untouched; the shift propagates through downstream blocks + final norm:
        assert torch.allclose(steered[1], base[1], atol=1e-6)
        assert torch.allclose(steered[4], base[4] + add, atol=1e-6)
        assert torch.allclose(steered["norm"], base["norm"] + add, atol=1e-6)
        # Hook removed on context exit:
        for k in base:
            assert torch.allclose(after[k], base[k], atol=1e-6)
    finally:
        config.LAYERS, config.PVEC_DIR = saved_layers, saved_dir
    print("test_steering_hook_toy: OK")


def test_real_vectors_load() -> None:
    if not os.path.isdir(config.PVEC_DIR):
        print(f"test_real_vectors_load: SKIPPED (PVEC_DIR not found: {config.PVEC_DIR})")
        return
    import torch
    for trait in ("loving", "nonchalance", "goodness"):
        v = torch.load(config.pvec_path(trait), weights_only=False, map_location="cpu")
        assert v.shape == (33, config.D_MODEL), f"{trait}: unexpected shape {tuple(v.shape)}"
    print(f"test_real_vectors_load: OK ({config.PVEC_DIR})")


def test_unsteer_transcript_parsing() -> None:
    condition = "loving_pvec_unsteer_k2_ai2ai"
    files = config.condition_files(condition, [0.7])
    if not files:
        print(f"test_unsteer_transcript_parsing: SKIPPED (no transcripts for {condition})")
        return
    with open(files[0][1], encoding="utf-8") as f:
        data = json.load(f)
    spec = config.condition_steering(condition)
    assert _transcript_steer(data, spec) == ("loving", 1.32, 16)

    run = data["runs"][0]
    K = spec.switch_turn
    for view in ("A", "B"):
        gm = replay.own_turn_models(run, view)
        own_turns = sorted(gm)
        # A speaks odd turns, B even
        assert all(t % 2 == (1 if view == "A" else 0) for t in own_turns)
        for t in own_turns:
            steered = config.parse_pvec_model(gm[t]) is not None
            assert steered == (t <= K), f"turn {t}: steered={steered}, expected {(t <= K)}"

    # Known-broken 1-turn runs (ended context_full before the switch): view B has no own turns;
    # build_view and own_turn_models must handle them without crashing.
    short = [r for r in data["runs"] if len(r["turns"]) == 1]
    assert short, "expected the known-broken 1-turn runs in this transcript"
    for r in short:
        msgs, own = replay.build_view(r, data["system_prompt"], r["seed_prompt"], "B")
        assert own == [] and replay.own_turn_models(r, "B") == {}
        _msgs, own_a = replay.build_view(r, data["system_prompt"], r["seed_prompt"], "A")
        assert [t for t, _ in own_a] == [1]
    print(f"test_unsteer_transcript_parsing: OK ({len(data['runs'])} runs, "
          f"{len(short)} broken 1-turn runs tolerated)")


def main() -> None:
    test_condition_parsing()
    test_steering_hook_toy()
    test_real_vectors_load()
    test_unsteer_transcript_parsing()
    print("ALL CPU TESTS PASSED")


if __name__ == "__main__":
    main()
