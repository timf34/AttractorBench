"""CPU tests for the prompt/LoRA unsteer arms — laptop-runnable, no API calls, no GPU.

    ./.venv/bin/python unsteering/test_prompt_switch_cpu.py

Covers:
(a) the harness mid-run SYSTEM-PROMPT switch: turns 1..K see the persona prompt, turns K+1..
    see the post prompt at history[0] of BOTH sides, with the conversation history preserved;
    plus the "" edge cases (post "" pops the system message; original "" gets one inserted)
    and the asymmetric system_prompt_b case;
(b) the runner payload record: switch_turn / model_*_post / system_prompt_key_post /
    system_prompt_post written whenever switch_turn is set, absent otherwise;
(c) both unsteering/ configs load under TRAIT/SWITCH_TURN env and produce sane RunConfigs;
    all 12 rich prompt keys resolve; the LoRA trait list matches attractor_internals;
(d) downstream parsing: run_onset_judge trait/K extraction and attractor_internals
    condition_lora / condition_steering / switch_turn_of / degenerate_runs on the new names.
"""

from __future__ import annotations

import copy
import json
import os
import sys
import tempfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

from attractorbench import harnesses  # noqa: E402
from attractorbench.config import RunConfig  # noqa: E402
from attractorbench.prompts import SYSTEM_PROMPTS, build_system_prompt  # noqa: E402
from attractorbench.runner import _save_condition, load_config  # noqa: E402

RICH = build_system_prompt("nonchalance_rich_persona", False)
RICH_B = build_system_prompt("goodness_rich_persona", False)
HELP = build_system_prompt("helpful_assistant", False)

ALL_TRAITS = ["loving", "goodness", "poeticism", "sycophancy", "nonchalance", "remorse",
              "sarcasm", "honesty", "sincerity", "mathematical", "humor", "impulsiveness"]


class _Recorder:
    """Stands in for providers.chat: records each call's (model, deep-copied messages)."""

    def __init__(self):
        self.calls: list[dict] = []

    def __call__(self, model, messages, temperature, top_p, max_tokens, reasoning_effort=None):
        self.calls.append({"model": model, "messages": copy.deepcopy(messages)})
        return f"reply-{len(self.calls)}", "stop"


def _cfg(**kw) -> RunConfig:
    base = dict(
        experiment_name="test_prompt_unsteer_k2_ai2ai", mode="two_instance",
        model_a="fake/model", model_b="fake/model",
        system_prompt_key="nonchalance_rich_persona", seed_prompt_set="goodness_opener_v1",
        max_turns=6, seeds=1, temperature=0.7, top_p=0.9, max_new_tokens=64, max_workers=1,
    )
    base.update(kw)
    return RunConfig(**base)


def _with_recorder(fn):
    rec = _Recorder()
    saved = harnesses.providers.chat
    harnesses.providers.chat = rec
    try:
        fn(rec)
    finally:
        harnesses.providers.chat = saved
    return rec


def test_prompt_switch() -> None:
    cfg = _cfg(switch_turn=2, system_prompt_key_post="helpful_assistant")

    def go(rec):
        run = harnesses.run_two_instance(cfg, RICH, "seed prompt", 0, 0.7)
        assert len(rec.calls) == 6 and len(run["turns"]) == 6
        for i, call in enumerate(rec.calls):
            turn = i + 1
            head = call["messages"][0]
            assert head["role"] == "system"
            want = RICH if turn <= 2 else HELP
            assert head["content"] == want, f"turn {turn}: wrong system prompt"
            assert call["model"] == "fake/model"  # no model switch in the prompt arm
        # history preserved through the swap: A's turn-5 call sees the full conversation
        t5 = rec.calls[4]["messages"]
        assert [m["role"] for m in t5] == ["system", "user", "assistant", "user", "assistant", "user"]
        assert [m["content"] for m in t5[1:]] == \
            ["seed prompt", "reply-1", "reply-2", "reply-3", "reply-4"]
        # B's turn-6 call: same swap, B's own view
        t6 = rec.calls[5]["messages"]
        assert t6[0] == {"role": "system", "content": HELP}
        assert [m["content"] for m in t6[1:]] == \
            ["reply-1", "reply-2", "reply-3", "reply-4", "reply-5"]

    _with_recorder(go)
    print("test_prompt_switch: OK")


def test_prompt_switch_asymmetric_b() -> None:
    # B starts with its OWN prompt (system_prompt_key_b); the post prompt applies to BOTH.
    cfg = _cfg(switch_turn=2, system_prompt_key_post="helpful_assistant",
               system_prompt_key_b="goodness_rich_persona")

    def go(rec):
        harnesses.run_two_instance(cfg, RICH, "seed prompt", 0, 0.7)
        assert rec.calls[0]["messages"][0]["content"] == RICH      # A, turn 1
        assert rec.calls[1]["messages"][0]["content"] == RICH_B    # B, turn 2 (its own prompt)
        for call in rec.calls[2:]:
            assert call["messages"][0]["content"] == HELP

    _with_recorder(go)
    print("test_prompt_switch_asymmetric_b: OK")


def test_empty_prompt_edges() -> None:
    # post "" => the system message is POPPED (not blanked) after the switch
    cfg = _cfg(switch_turn=2)

    def go_pop(rec):
        harnesses._run_two_history(cfg, RICH, "seed", 0, 0.7, "fake/model", "fake/model",
                                   system_prompt_post="")
        assert rec.calls[1]["messages"][0]["role"] == "system"
        for call in rec.calls[2:]:
            assert all(m["role"] != "system" for m in call["messages"])
        assert rec.calls[4]["messages"][0] == {"role": "user", "content": "seed"}  # history intact

    # original "" (no system message at all) => one is INSERTED at the switch
    def go_insert(rec):
        harnesses._run_two_history(cfg, "", "seed", 0, 0.7, "fake/model", "fake/model",
                                   system_prompt_post=HELP)
        assert all(m["role"] != "system" for m in rec.calls[0]["messages"])
        assert all(m["role"] != "system" for m in rec.calls[1]["messages"])
        for call in rec.calls[2:]:
            assert call["messages"][0] == {"role": "system", "content": HELP}
        assert rec.calls[4]["messages"][1] == {"role": "user", "content": "seed"}  # seed still first

    # no switch configured => nothing changes even with switch_turn set but post prompt None
    def go_none(rec):
        harnesses._run_two_history(cfg, RICH, "seed", 0, 0.7, "fake/model", "fake/model",
                                   system_prompt_post=None)
        for call in rec.calls:
            assert call["messages"][0]["content"] == RICH

    _with_recorder(go_pop)
    _with_recorder(go_insert)
    _with_recorder(go_none)
    print("test_empty_prompt_edges: OK")


def test_payload_record() -> None:
    runs = [{"run_index": 0, "seed_prompt": "s", "ended_early": False, "ended_at_turn": None,
             "turns": []}]
    with tempfile.TemporaryDirectory() as td:
        # prompt-unsteer shape: switch_turn + prompt post fields, no model post
        cfg = _cfg(switch_turn=2, system_prompt_key_post="helpful_assistant")
        path = os.path.join(td, "a.json")
        _save_condition(path, cfg, 0.7, RICH, runs)
        p = json.load(open(path))
        assert p["switch_turn"] == 2
        assert p["system_prompt_key_post"] == "helpful_assistant"
        assert p["system_prompt_post"] == HELP
        assert p["model_a_post"] is None and p["model_b_post"] is None
        # lora/pvec-unsteer shape: model post fields, no prompt post
        cfg = _cfg(switch_turn=4, model_a_post="local/base", model_b_post="local/base")
        path = os.path.join(td, "b.json")
        _save_condition(path, cfg, 0.7, HELP, runs)
        p = json.load(open(path))
        assert p["switch_turn"] == 4 and p["model_a_post"] == "local/base"
        assert p["system_prompt_key_post"] is None and p["system_prompt_post"] is None
        # no switch => none of the switch keys appear (pre-existing payload shape unchanged)
        cfg = _cfg()
        path = os.path.join(td, "c.json")
        _save_condition(path, cfg, 0.7, HELP, runs)
        p = json.load(open(path))
        assert "switch_turn" not in p and "system_prompt_post" not in p
    print("test_payload_record: OK")


def test_configs_load() -> None:
    env = {"TRAIT": "nonchalance", "SWITCH_TURN": "2"}
    saved = {k: os.environ.get(k) for k in env}
    os.environ.update(env)
    try:
        cfg = load_config(os.path.join(REPO_ROOT, "unsteering", "prompt_unsteer_ai2ai.py"))
        assert cfg.experiment_name == "nonchalance_prompt_unsteer_k2_ai2ai"
        assert cfg.mode == "two_instance" and cfg.switch_turn == 2
        assert cfg.model_a == cfg.model_b == "openrouter/meta-llama/llama-3.1-8b-instruct"
        assert cfg.model_a_post is None and cfg.model_b_post is None
        assert cfg.system_prompt_key == "nonchalance_rich_persona"
        assert cfg.system_prompt_key_post == "helpful_assistant"
        assert cfg.seed_prompt_set == "goodness_opener_v1" and cfg.top_p == 0.9
        assert cfg.temperature_sweep == [0.7]

        cfg = load_config(os.path.join(REPO_ROOT, "unsteering", "lora_unsteer_ai2ai.py"))
        assert cfg.experiment_name == "nonchalance_lora_unsteer_k2_ai2ai"
        assert cfg.model_a == cfg.model_b == "local/nonchalance"
        assert cfg.model_a_post == cfg.model_b_post == "local/unsloth/Meta-Llama-3.1-8B-Instruct"
        assert cfg.system_prompt_key == "helpful_assistant"
        assert cfg.system_prompt_key_post is None and cfg.switch_turn == 2

        # (imported while TRAIT/SWITCH_TURN are still set — the module reads env on import)
        from unsteering.lora_unsteer_ai2ai import LORA_TRAITS as U_LORA
    finally:
        for k, v in saved.items():
            os.environ.pop(k, None) if v is None else os.environ.__setitem__(k, v)

    for t in ALL_TRAITS:  # all 12 rich prompts must resolve (the prompt arm covers them all)
        assert f"{t}_rich_persona" in SYSTEM_PROMPTS, f"missing rich prompt for {t}"

    from attractor_internals.config import LORA_TRAITS as AI_LORA
    assert sorted(U_LORA) == sorted(AI_LORA) and len(U_LORA) == 10
    assert "sincerity" not in U_LORA and "honesty" not in U_LORA
    print("test_configs_load: OK")


def test_downstream_parsing() -> None:
    import run_onset_judge as oj
    for cond, trait, k in [("goodness_prompt_unsteer_k4_ai2ai", "goodness", 4),
                           ("sarcasm_lora_unsteer_k12_ai2ai", "sarcasm", 12),
                           ("loving_pvec_unsteer_k2_ai2ai", "loving", 2)]:
        assert oj.trait_of_condition(cond) == trait, cond
        assert oj.switch_k(cond) == k, cond
    assert oj.trait_of_condition("base_ai2ai") is None
    assert oj.trait_of_condition("goodness_ai2ai") is None  # LoRA-forever: not an unsteer run

    from attractor_internals import config as ai_config
    from attractor_internals.project_pvec import degenerate_runs, switch_turn_of
    assert ai_config.condition_lora("goodness_lora_unsteer_k4_ai2ai") == "goodness"
    assert ai_config.condition_lora("goodness_prompt_unsteer_k4_ai2ai") is None
    assert ai_config.condition_lora("sincerity_prompt_unsteer_k2_ai2ai") is None
    try:
        ai_config.condition_lora("sincerity_lora_unsteer_k2_ai2ai")
        raise AssertionError("prompt-only trait accepted as a LoRA condition")
    except ValueError:
        pass
    # no activation hook for either new family — and, crucially, no raise
    assert ai_config.condition_steering("goodness_prompt_unsteer_k4_ai2ai") is None
    assert ai_config.condition_steering("goodness_lora_unsteer_k4_ai2ai") is None

    # switch_turn_of: payload record wins; name regex covers all three families as fallback
    assert switch_turn_of("goodness_prompt_unsteer_k4_ai2ai") == 4
    assert switch_turn_of("goodness_lora_unsteer_k4_ai2ai", {"switch_turn": 6}) == 6
    assert switch_turn_of("goodness_ai2ai", {}) is None
    # degenerate detection is schedule-based: a prompt-unsteer run whose per-turn model never
    # changes is NOT degenerate as long as it got past the switch
    runs = [{"run_index": 0, "turns": [{"turn": i, "model": "openrouter/m"} for i in range(1, 7)]},
            {"run_index": 1, "turns": [{"turn": i, "model": "openrouter/m"} for i in range(1, 5)]}]
    assert degenerate_runs(runs, 4) == {0: False, 1: True}   # run 1 never reached turn 5
    assert degenerate_runs(runs, None) == {0: False, 1: False}
    print("test_downstream_parsing: OK")


def main() -> None:
    test_prompt_switch()
    test_prompt_switch_asymmetric_b()
    test_empty_prompt_edges()
    test_payload_record()
    test_configs_load()
    test_downstream_parsing()
    print("ALL UNSTEER CPU TESTS PASSED")


if __name__ == "__main__":
    main()
