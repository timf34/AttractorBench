"""Per-instance view reconstruction for ai2ai transcripts (+ the Gemma-2 system fold).

``build_view`` mirrors ``attractor_internals/replay.py:build_view`` (which itself mirrors
``attractorbench.harnesses._run_two_history``), with one addition: an EMPTY system prompt
produces no system message at all — matching the harness's "none" behavior.

``fold_system_into_user`` is the Gemma-2 convention from the assistant-axis repo's
``generation.py`` ("Concatenate instruction with question for models without system support",
``f"{instruction}\\n\\n{question}"``). It must stay in lockstep with
``templates/gemma2_system_fold.jinja`` — ``verify_templates.py`` asserts they render
identically through the native Gemma-2 template.
"""

from __future__ import annotations


def build_view(run: dict, system_prompt: str, seed_prompt: str, view: str) -> list[dict]:
    """One instance's message list for a run. View "A" opens with the seed as its user turn and
    speaks the odd harness turns; view "B" starts bare and speaks the even turns. Uses raw
    ``content`` — what the harness actually fed forward."""
    if view not in ("A", "B"):
        raise ValueError(f"view must be 'A' or 'B', got {view!r}")
    messages = [{"role": "system", "content": system_prompt}] if system_prompt else []
    if view == "A":
        messages.append({"role": "user", "content": seed_prompt})
    for t in run["turns"]:
        role = "assistant" if t["speaker"] == view else "user"
        messages.append({"role": role, "content": t["content"]})
    return messages


def fold_system_into_user(messages: list[dict]) -> list[dict]:
    """Drop the system message, prepending its text to the first user turn (Gemma-2 has no
    system role). No-op when there is no system message."""
    if not messages or messages[0]["role"] != "system":
        return list(messages)
    sys_text = messages[0]["content"]
    out = []
    folded = False
    for m in messages[1:]:
        if not folded and m["role"] == "user" and sys_text:
            out.append({"role": "user", "content": f"{sys_text}\n\n{m['content']}"})
            folded = True
        else:
            out.append(dict(m))
    return out
