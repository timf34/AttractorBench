"""Interactive persona-vector steering REPL — prompt the steered model live to sanity-check a vector.

Loads the model once, then you type prompts and see steered replies immediately. Fast on any decent
GPU (single 8B generation is a few seconds) — the right tool to eyeball whether a (trait, coef, layer)
actually induces the persona, without the full AI2AI harness.

    python -m persona_vector_steering.chat --trait goodness --coef 2 --layer 16

REPL commands:
    <text>          send <text> as a user turn -> steered reply
    :cmp <text>     print BASE vs STEERED side by side (best for calibration)
    :base <text>    reply with NO steering (control)
    :coef 4         change coefficient          :layer 20   change layer
    :trait loving   change trait                :temp 0.7   change temperature (0 = greedy)
    :sys <text>     change the system prompt (default: "You are a helpful assistant.")
    :q              quit
"""

from __future__ import annotations

import argparse

from . import config, steering

SYS_DEFAULT = "You are a helpful assistant."


def gen(sm, trait, coef, layer, system, user, temp, max_new_tokens):
    if coef and coef != 0:
        sm.set_steering(trait, coef, layer)
    else:
        sm.clear()
    try:
        msgs = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        text, _ = sm.chat(msgs, max_new_tokens, temp, 0.9)
    finally:
        sm.clear()
    return text.strip()


def main():
    ap = argparse.ArgumentParser(description="Interactive persona-vector steering REPL.")
    ap.add_argument("--trait", default="goodness")
    ap.add_argument("--coef", type=float, default=2.0)
    ap.add_argument("--layer", type=int, default=config.DEFAULT_LAYER)
    ap.add_argument("--temp", type=float, default=0.7)
    ap.add_argument("--max-new-tokens", type=int, default=256)
    ap.add_argument("--device", default=None)
    args = ap.parse_args()

    print(f"loading {config.MODEL} (vectors: {config.VECTOR_DIR}) ...")
    sm = steering.load_steered(args.device)
    sm.register()
    st = {"trait": args.trait, "coef": args.coef, "layer": args.layer, "temp": args.temp, "sys": SYS_DEFAULT}
    mnt = args.max_new_tokens
    print(f"ready. trait={st['trait']} coef={st['coef']} layer={st['layer']} temp={st['temp']} max_new_tokens={mnt}")
    print("type a message, :cmp <msg> for base-vs-steered, :q to quit.\n")

    while True:
        try:
            line = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            continue
        if line == ":q":
            break
        if line.startswith(":coef "):
            st["coef"] = float(line[6:]); print(f"  coef={st['coef']}"); continue
        if line.startswith(":layer "):
            st["layer"] = int(line[7:]); print(f"  layer={st['layer']}"); continue
        if line.startswith(":trait "):
            st["trait"] = line[7:].strip(); print(f"  trait={st['trait']}"); continue
        if line.startswith(":temp "):
            st["temp"] = float(line[6:]); print(f"  temp={st['temp']}"); continue
        if line.startswith(":sys "):
            st["sys"] = line[5:].strip(); print("  system prompt set"); continue
        if line.startswith(":base "):
            print(gen(sm, st["trait"], 0, st["layer"], st["sys"], line[6:], st["temp"], mnt), "\n"); continue
        if line.startswith(":cmp "):
            u = line[5:]
            print("\n--- BASE (no steering) ---")
            print(gen(sm, st["trait"], 0, st["layer"], st["sys"], u, st["temp"], mnt))
            print(f"\n--- {st['trait'].upper()} coef={st['coef']} layer={st['layer']} ---")
            print(gen(sm, st["trait"], st["coef"], st["layer"], st["sys"], u, st["temp"], mnt))
            print()
            continue
        # plain message -> steered reply
        print(gen(sm, st["trait"], st["coef"], st["layer"], st["sys"], line, st["temp"], mnt), "\n")


if __name__ == "__main__":
    main()
