"""Step 1 of the SAE feature-discovery pipeline: generate contrastive material per trait.

For each trait we call OpenAI ONCE to produce (a) several POSITIVE system-prompt phrasings that make
the assistant embody the trait and (b) a set of neutral, off-topic user questions. The NEGATIVE
condition is fixed elsewhere (config.NEUTRAL_SYSTEM = "You are a helpful assistant."), so we only
generate the positive side here — never any "opposite trait" text.

Output: sae_steering/data/contrasts/{trait}.json (a trait that already has a file is skipped).

    python -m sae_steering.generate_contrasts                    # all 12 traits
    python -m sae_steering.generate_contrasts --trait honesty    # one trait
    python -m sae_steering.generate_contrasts --limit 4          # smoke test: request only 4 questions
    python -m sae_steering.generate_contrasts --model gpt-4o-mini
"""

from __future__ import annotations

import argparse
import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from sae_steering import config

load_dotenv()  # OPENAI_API_KEY from repo-root .env


# A deliberately SIMPLE prompt: just the two JSON arrays we need, no eval rubric. The word "JSON"
# must appear for response_format={"type": "json_object"} to be accepted.
PROMPT_TEMPLATE = """\
You are helping build a contrastive dataset for studying the AI-assistant personality trait "{trait}".
Trait definition: {definition}.

Return STRICT JSON (a single object, and nothing else) with exactly these two keys:

  "pos_instructions": an array of {n_pos} distinct system-prompt-style instructions that tell an AI
  assistant to fully embody the trait "{trait}". Each entry must be a self-contained, directly usable
  system prompt (1-3 sentences), and the phrasings must be clearly varied from one another.

  "questions": an array of {n_questions} diverse, neutral user questions spanning many everyday domains
  (cooking, travel, technology, science, work, hobbies, daily life, etc.). These questions MUST be
  generic and MUST NOT mention, hint at, or thematically relate to "{trait}" in any way.

Output only the JSON object."""


def build_prompt(trait: str, definition: str, n_pos: int, n_questions: int) -> str:
    return PROMPT_TEMPLATE.format(
        trait=trait, definition=definition, n_pos=n_pos, n_questions=n_questions
    )


def call_openai(client: OpenAI, model: str, prompt: str, force_json: bool = True) -> str:
    """One chat completion -> raw string content. Asks for a JSON object when the model supports it,
    transparently falling back to plain text if the model rejects response_format."""
    kwargs = dict(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,  # a little variety so the phrasings/questions aren't near-duplicates
    )
    if force_json:
        kwargs["response_format"] = {"type": "json_object"}
    try:
        resp = client.chat.completions.create(**kwargs)
    except Exception as e:  # noqa: BLE001
        if force_json and "response_format" in str(e).lower():
            print("   (model rejects response_format=json_object; retrying as plain text)")
            return call_openai(client, model, prompt, force_json=False)
        raise
    return resp.choices[0].message.content or ""


def _strip_code_fences(text: str) -> str:
    """Remove a leading ```json / ``` fence and its closing ``` if the reply is fenced."""
    t = text.strip()
    if t.startswith("```"):
        lines = t.splitlines()
        if lines and lines[0].lstrip().startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        t = "\n".join(lines).strip()
    return t


def parse_contrasts(raw: str):
    """Defensively parse the model reply. Returns (pos_instructions, questions) as clean, non-empty
    lists of strings, or None if the JSON is malformed / missing / empty (caller then retries once)."""
    text = _strip_code_fences(raw)
    try:
        data = json.loads(text)
    except (json.JSONDecodeError, TypeError, ValueError):
        # last-ditch: grab the outermost {...} block and try again
        i, j = text.find("{"), text.rfind("}")
        if i == -1 or j <= i:
            return None
        try:
            data = json.loads(text[i : j + 1])
        except (json.JSONDecodeError, TypeError, ValueError):
            return None
    if not isinstance(data, dict):
        return None
    pos = data.get("pos_instructions")
    questions = data.get("questions")
    if not isinstance(pos, list) or not isinstance(questions, list):
        return None
    pos = [s.strip() for s in pos if isinstance(s, str) and s.strip()]
    questions = [s.strip() for s in questions if isinstance(s, str) and s.strip()]
    if not pos or not questions:
        return None
    return pos, questions


def generate_trait(client: OpenAI, model: str, trait: str, n_pos: int, n_questions: int):
    """Generate, validate, and save the contrast file for one trait. Returns the saved dict, or None
    if generation failed (an error is printed and the trait is skipped — the run is not aborted)."""
    definition = config.TRAITS[trait]
    prompt = build_prompt(trait, definition, n_pos, n_questions)

    parsed = None
    for attempt in (1, 2):  # one call + one retry, per spec
        try:
            raw = call_openai(client, model, prompt)
        except Exception as e:  # noqa: BLE001  -- API/transport error
            print(f"   [{trait}] API call failed (attempt {attempt}): {e}")
            continue
        parsed = parse_contrasts(raw)
        if parsed is not None:
            break
        print(f"   [{trait}] could not parse JSON (attempt {attempt})")
    if parsed is None:
        print(f"   [{trait}] ERROR: no usable JSON after retry — skipping")
        return None

    pos, questions = parsed
    if len(pos) != n_pos:
        print(f"   [{trait}] WARNING: got {len(pos)} pos_instructions (wanted {n_pos}) — keeping as is")
    if len(questions) != n_questions:
        print(f"   [{trait}] WARNING: got {len(questions)} questions (wanted {n_questions}) — keeping as is")

    out = {
        "trait": trait,
        "definition": definition,
        "pos_instructions": pos,
        "questions": questions,
    }
    path = config.contrasts_path(trait)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"   [{trait}] saved {len(pos)} pos_instructions + {len(questions)} questions -> {path}")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Step 1: generate positive trait instructions + neutral questions with OpenAI."
    )
    ap.add_argument("--trait", default=None,
                    help="single trait to generate (default: every trait in config.TRAITS)")
    ap.add_argument("--limit", type=int, default=None,
                    help=f"cap questions REQUESTED per trait (smoke tests); default {config.N_QUESTIONS}")
    ap.add_argument("--model", default=config.OPENAI_MODEL,
                    help=f"OpenAI model (default {config.OPENAI_MODEL})")
    args = ap.parse_args()

    if args.trait is not None and args.trait not in config.TRAITS:
        raise SystemExit(f"unknown trait {args.trait!r}; choose from: {', '.join(config.TRAITS)}")
    traits = [args.trait] if args.trait else list(config.TRAITS)
    n_pos = config.N_POS_PHRASINGS
    n_questions = config.N_QUESTIONS if args.limit is None else max(1, args.limit)

    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set (put it in the repo-root .env).")

    config.ensure_dirs()
    client = OpenAI()  # reads OPENAI_API_KEY from env

    print(f"PLAN: {len(traits)} trait(s) with {args.model} "
          f"({n_pos} pos_instructions + {n_questions} questions each)")

    n_generated = 0
    for trait in traits:
        path = config.contrasts_path(trait)
        if os.path.exists(path):
            print(f"[{trait}] skip (exists: {path})")
            continue
        print(f"[{trait}] generating...")
        if generate_trait(client, args.model, trait, n_pos, n_questions) is not None:
            n_generated += 1

    print(f"==== DONE: {n_generated}/{len(traits)} trait(s) generated this run ====")


if __name__ == "__main__":
    main()
