"""Generate rich + grounded persona system prompts for every trait (the datagen pipeline).

Two variants per trait, two LLM steps each (see metaprompts.py for the prompts and the design
rationale):

  rich      trait -> [A1 trait analysis] -> [A2 system prompt]
  grounded  trait -> [B1 real-person exemplar selection, JSON] -> [B2 system prompt]

Usage (from the repo root):

    ./.venv/bin/python -m persona_promptgen.generate                          # all 12 traits, both variants
    ./.venv/bin/python -m persona_promptgen.generate --traits humor sarcasm
    ./.venv/bin/python -m persona_promptgen.generate --variant grounded
    ./.venv/bin/python -m persona_promptgen.generate --skip-existing         # only fill gaps

Outputs:
  persona_promptgen/outputs/<trait>.json   — full provenance: every intermediate (analysis /
                                             candidate slate) plus the final prompts + metadata.
                                             Written incrementally, one file per trait; variants
                                             merge into the same file, so partial runs compose.
  attractorbench/prompts_generated.py      — AUTO-GENERATED module with the final prompts under
                                             keys "<trait>_rich_persona" / "<trait>_grounded_persona",
                                             merged into SYSTEM_PROMPTS by attractorbench/prompts.py.
                                             Rebuilt from ALL outputs/*.json on every run. Commit it:
                                             the exact prompt text is a pinned experimental variable.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time

from dotenv import load_dotenv

from attractorbench.providers import chat

from persona_promptgen.metaprompts import (
    exemplar_selection_prompt,
    grounded_system_prompt_prompt,
    rich_system_prompt_prompt,
    trait_analysis_prompt,
)
from persona_promptgen.traits import TRAIT_GLOSSES, TRAITS

# Datagen model — deliberately cheaper than the stage-2 judge (gpt-5.4): prompt generation is a
# one-off, low-volume task and doesn't need the strongest model. Routed via OpenRouter
# (OPENROUTER_API_KEY in .env); use "openai/gpt-5.1" to hit the OpenAI API directly instead.
DATAGEN_MODEL = "openrouter/openai/gpt-5.1"

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO_ROOT, "persona_promptgen", "outputs")
GENERATED_MODULE_PATH = os.path.join(REPO_ROOT, "attractorbench", "prompts_generated.py")

# Generous ceilings: on reasoning models, hidden reasoning tokens share this budget (see README).
MAX_TOKENS_ANALYSIS = 16384
MAX_TOKENS_PROMPT = 8192

# The meta-prompts ask for 170-230 words; enforce with slack, one corrective retry.
WORD_MIN, WORD_MAX = 140, 280


def _call(model: str, prompt: str, temperature: float, max_tokens: int) -> str:
    content, finish_reason = chat(
        model,
        [{"role": "user", "content": prompt}],
        temperature=temperature,
        top_p=1.0,
        max_tokens=max_tokens,
    )
    if finish_reason == "length":
        raise RuntimeError(f"datagen call truncated at max_tokens={max_tokens}; raise the ceiling")
    return content.strip()


def _strip_fences(text: str) -> str:
    """Drop a single wrapping ``` fence (with optional language tag) if the model added one."""
    m = re.fullmatch(r"```[a-zA-Z]*\n(.*?)\n?```", text.strip(), re.S)
    return m.group(1).strip() if m else text.strip()


def _parse_json(text: str) -> dict:
    text = _strip_fences(text)
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"no JSON object found in model output:\n{text[:500]}")
    return json.loads(text[start : end + 1])


def _system_prompt_call(model: str, metaprompt: str, temperature: float) -> tuple[str, int, bool]:
    """Generate a system prompt, retrying once with a corrective note if the length band is missed.

    Returns (prompt, word_count, retried).
    """
    out = _strip_fences(_call(model, metaprompt, temperature, MAX_TOKENS_PROMPT))
    words = len(out.split())
    if WORD_MIN <= words <= WORD_MAX:
        return out, words, False
    note = (
        f"\n\nIMPORTANT: a previous attempt was {words} words, outside the required 170-230. "
        "Rewrite to length, keeping the strongest material. Output only the system prompt."
    )
    out = _strip_fences(_call(model, metaprompt + note, temperature, MAX_TOKENS_PROMPT))
    return out, len(out.split()), True


def generate_rich(trait: str, model: str, temperature: float) -> dict:
    gloss = TRAIT_GLOSSES[trait]
    analysis = _call(model, trait_analysis_prompt(trait, gloss), temperature, MAX_TOKENS_ANALYSIS)
    prompt, words, retried = _system_prompt_call(
        model, rich_system_prompt_prompt(trait, gloss, analysis), temperature
    )
    return {"analysis": analysis, "prompt": prompt, "word_count": words, "length_retried": retried}


def generate_grounded(
    trait: str, model: str, temperature: float, exclude: tuple[str, ...] = ()
) -> dict:
    gloss = TRAIT_GLOSSES[trait]
    selection = _parse_json(
        _call(model, exemplar_selection_prompt(trait, gloss, exclude), temperature, MAX_TOKENS_ANALYSIS)
    )
    choice = selection["choice"]
    prompt, words, retried = _system_prompt_call(
        model, grounded_system_prompt_prompt(trait, gloss, choice), temperature
    )
    return {
        "selection": selection,
        "person": choice["name"],
        "weak_exemplar": bool(choice.get("weak_exemplar", False)),
        "prompt": prompt,
        "word_count": words,
        "length_retried": retried,
    }


def _trait_path(trait: str) -> str:
    return os.path.join(OUT_DIR, f"{trait}.json")


def _load_trait(trait: str) -> dict:
    path = _trait_path(trait)
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {"trait": trait, "gloss": TRAIT_GLOSSES[trait]}


def _save_trait(data: dict) -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(_trait_path(data["trait"]), "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def emit_generated_module() -> int:
    """Rebuild attractorbench/prompts_generated.py from every outputs/*.json present."""
    entries: list[tuple[str, str, str]] = []  # (key, prompt, provenance comment)
    if os.path.isdir(OUT_DIR):
        for fname in sorted(os.listdir(OUT_DIR)):
            if not fname.endswith(".json"):
                continue
            with open(os.path.join(OUT_DIR, fname)) as f:
                data = json.load(f)
            trait = data["trait"]
            if "rich" in data:
                meta = data["rich"].get("_meta", {})
                entries.append(
                    (f"{trait}_rich_persona", data["rich"]["prompt"],
                     f"generated by {meta.get('model', '?')} on {meta.get('date', '?')}")
                )
            if "grounded" in data:
                meta = data["grounded"].get("_meta", {})
                person = data["grounded"].get("person", "?")
                weak = " (weak exemplar)" if data["grounded"].get("weak_exemplar") else ""
                entries.append(
                    (f"{trait}_grounded_persona", data["grounded"]["prompt"],
                     f"person: {person}{weak}; generated by {meta.get('model', '?')} on {meta.get('date', '?')}")
                )
    lines = [
        '"""AUTO-GENERATED persona system prompts — do not hand-edit; regenerate instead:',
        "",
        "    ./.venv/bin/python -m persona_promptgen.generate",
        "",
        "Full provenance (trait analyses, exemplar candidate slates, metadata) lives in",
        "persona_promptgen/outputs/<trait>.json. Merged into SYSTEM_PROMPTS by prompts.py.",
        '"""',
        "",
        "GENERATED_SYSTEM_PROMPTS: dict[str, str] = {",
    ]
    for key, prompt, comment in entries:
        lines.append(f"    # {comment}")
        lines.append(f"    {key!r}: {prompt!r},")
    lines.append("}")
    lines.append("")
    with open(GENERATED_MODULE_PATH, "w") as f:
        f.write("\n".join(lines))
    return len(entries)


def main() -> None:
    load_dotenv()  # standalone entrypoint: pick up OPENROUTER_API_KEY / OPENAI_API_KEY from .env
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--traits", nargs="+", default=TRAITS, choices=TRAITS, metavar="TRAIT")
    p.add_argument("--variant", choices=["rich", "grounded", "both"], default="both")
    p.add_argument("--model", default=DATAGEN_MODEL, help=f"datagen model (default {DATAGEN_MODEL})")
    p.add_argument("--temperature", type=float, default=1.0)
    p.add_argument("--skip-existing", action="store_true",
                   help="skip trait/variant pairs already present in outputs/")
    p.add_argument("--exclude-person", action="append", default=[], metavar="NAME",
                   help="grounded variant: person the caster must not choose (repeatable), "
                        "e.g. someone already cast for another trait")
    args = p.parse_args()

    variants = ["rich", "grounded"] if args.variant == "both" else [args.variant]
    exclude = tuple(args.exclude_person)
    generators = {
        "rich": lambda t: generate_rich(t, args.model, args.temperature),
        "grounded": lambda t: generate_grounded(t, args.model, args.temperature, exclude),
    }
    date = time.strftime("%Y-%m-%d")

    for trait in args.traits:
        data = _load_trait(trait)
        for variant in variants:
            if args.skip_existing and variant in data:
                print(f"[skip] {trait}/{variant} (already generated)")
                continue
            t0 = time.time()
            result = generators[variant](trait)
            result["_meta"] = {"model": args.model, "temperature": args.temperature, "date": date}
            data[variant] = result
            _save_trait(data)
            extra = f" person={result['person']!r}" if variant == "grounded" else ""
            if result.get("weak_exemplar"):
                extra += " WEAK-EXEMPLAR"
            print(f"[done] {trait}/{variant} in {time.time() - t0:.0f}s "
                  f"({result['word_count']} words{extra})")

    n = emit_generated_module()
    print(f"\nWrote {n} prompts to {os.path.relpath(GENERATED_MODULE_PATH, REPO_ROOT)}")


if __name__ == "__main__":
    main()
