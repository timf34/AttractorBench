"""Step-0 probe: how do we elicit self_append continuation from OpenAI Chat Completions?

self_append (passthrough) is meant to be a single growing context with no user turn after the
seed. Two transports are possible:
  - "message_list": append each reply as an assistant message; re-call with a list ending on an
    assistant turn. Relies on the API CONTINUING that list rather than RESTARTING.
  - "serialized_string": keep one growing transcript string; each turn send it inside a single
    user message and have the model add the next turn.
Empirically (run this probe), gpt-5.2 RESTARTS an assistant-terminated list (re-answers the
seed) rather than continuing it, so message_list is unsuitable. This probe also exercises the
serialized_string loop for real so we can eyeball that it produces a coherent CONTINUING
monologue, not N restarts.

Run:  python -m attractorbench.probe_transport
"""

from __future__ import annotations

from . import providers
from .prompts import serialize_self_append

# --- Part 1: does an assistant-terminated list continue or restart? ---------
_ASSISTANT_X = (
    "Sure. Three things I find genuinely fascinating about deep-sea ecosystems: first, "
    "chemosynthesis at hydrothermal vents, where life runs on chemistry instead of sunlight; "
    "second,"
)
_LIST_MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a few things you find fascinating."},
    {"role": "assistant", "content": _ASSISTANT_X},
]


def probe_message_list(model: str) -> None:
    print(f"\n[message_list] {model} — assistant_x ends with '...; second,'")
    try:
        reply, _ = providers.chat(model, _LIST_MESSAGES, temperature=1.0, top_p=1.0, max_tokens=200)
    except Exception as e:  # noqa: BLE001
        print(f"  ERROR -> {type(e).__name__}: {e}")
        return
    print(f"  reply[:200]: {reply.strip()[:200]!r}")
    print("  -> CONTINUATION if it finishes the list; RESTART if it re-answers from scratch.\n")


# --- Part 2: serialized_string loop, run for real ---------------------------
def probe_serialized(model: str, seed: str, n_turns: int = 3, max_tokens: int = 700) -> None:
    print(f"\n[serialized_string] {model} — {n_turns}-turn loop, seed={seed!r}")
    system = "You are a helpful assistant."
    contents: list[str] = []
    for turn in range(1, n_turns + 1):
        # Turn 1 the "transcript" is just the seed; later turns prepend seed + the model's own
        # growing output, presented as one user message (no role swap, single growing context).
        if not contents:
            user_content = seed
        else:
            user_content = seed + "\n\n" + serialize_self_append(contents)
        messages = [{"role": "system", "content": system}, {"role": "user", "content": user_content}]
        try:
            reply, _ = providers.chat(model, messages, temperature=1.0, top_p=1.0, max_tokens=max_tokens)
        except Exception as e:  # noqa: BLE001
            print(f"  turn {turn}: ERROR -> {type(e).__name__}: {e}")
            return
        contents.append(reply)
        print(f"  --- turn {turn} (len={len(reply)}) ---\n  {reply.strip()[:280]!r}\n")
    print("  -> Read the turns: do they BUILD on each other (continuation) or RESTART each time?\n")


def main() -> None:
    for model in ("openai/gpt-5.2", "openai/gpt-5-mini"):
        probe_message_list(model)
    probe_serialized("openai/gpt-5.2", "You have complete freedom to discuss whatever you want.")


if __name__ == "__main__":
    main()
