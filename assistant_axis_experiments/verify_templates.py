"""Assert templates/gemma2_system_fold.jinja == native Gemma-2 template + python-side fold.

The custom template lets vLLM accept a system message for Gemma-2 (whose native template
raises on one) by folding it into the first user turn AT SERVE TIME; the projection stage
folds in python (``views.fold_system_into_user``) and uses the NATIVE template. If the two
ever disagree, generation and replay would tokenize different strings — this check makes that
impossible to miss. Pure jinja2, no tokenizer/GPU needed:

    python -m assistant_axis_experiments.verify_templates
"""

from __future__ import annotations

import os
import sys

import jinja2

from .views import fold_system_into_user

# google/gemma-2-27b-it tokenizer_config.json chat_template, verbatim.
GEMMA2_NATIVE_TEMPLATE = (
    "{{ bos_token }}{% if messages[0]['role'] == 'system' %}{{ raise_exception('System role "
    "not supported') }}{% endif %}{% for message in messages %}{% if (message['role'] == "
    "'user') != (loop.index0 % 2 == 0) %}{{ raise_exception('Conversation roles must "
    "alternate user/assistant/user/assistant/...') }}{% endif %}{% if (message['role'] == "
    "'assistant') %}{% set role = 'model' %}{% else %}{% set role = message['role'] %}"
    "{% endif %}{{ '<start_of_turn>' + role + '\n' + message['content'] | trim + "
    "'<end_of_turn>\n' }}{% endfor %}{% if add_generation_prompt %}{{'<start_of_turn>model\n'}}"
    "{% endif %}"
)

_FOLD_PATH = os.path.join(os.path.dirname(__file__), "templates", "gemma2_system_fold.jinja")


def _render(template_str: str, messages: list[dict], add_generation_prompt: bool) -> str:
    env = jinja2.Environment()

    def raise_exception(msg):
        raise ValueError(msg)

    env.globals["raise_exception"] = raise_exception
    return env.from_string(template_str).render(
        messages=messages, bos_token="<bos>", add_generation_prompt=add_generation_prompt
    )


def verify(native_template: str | None = None) -> None:
    """Raises AssertionError on any mismatch. ``native_template`` overrides the pinned copy
    (the pod preflight passes the actual tokenizer's template to also catch upstream edits)."""
    native = native_template or GEMMA2_NATIVE_TEMPLATE
    with open(_FOLD_PATH) as f:
        fold = f.read()

    cases = [
        # system + multi-turn (the helpful_assistant condition, both views' shapes)
        [{"role": "system", "content": "You are a helpful assistant."},
         {"role": "user", "content": "Hello there.\nSecond line."},
         {"role": "assistant", "content": "Hi! "},
         {"role": "user", "content": "Tell me more."},
         {"role": "assistant", "content": "Sure."}],
        # no system at all (the nosys condition) — fold must be a no-op
        [{"role": "user", "content": "Hey."},
         {"role": "assistant", "content": "Hello."}],
        # system + single user turn
        [{"role": "system", "content": "Be terse."},
         {"role": "user", "content": "Why is the sky blue?"}],
    ]
    for i, msgs in enumerate(cases):
        for agp in (False, True):
            got = _render(fold, msgs, agp)
            want = _render(native, fold_system_into_user(msgs), agp)
            assert got == want, (
                f"case {i} (add_generation_prompt={agp}): fold template != native+python-fold\n"
                f"--- fold template produced:\n{got!r}\n--- native+python-fold produced:\n{want!r}"
            )
    print(f"gemma2_system_fold.jinja OK — {len(cases) * 2} renders match native+python-fold")


if __name__ == "__main__":
    try:
        verify()
    except AssertionError as e:
        print(f"TEMPLATE MISMATCH:\n{e}", file=sys.stderr)
        sys.exit(1)
