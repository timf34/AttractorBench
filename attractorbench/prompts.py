"""All conversation prompts live here (never inline in the runner / harness).

Templates are plain triple-quoted strings with ``{placeholder}`` markers, filled via
``.format()`` at call time — NOT f-strings (which would interpolate at definition time, before
runtime values exist). Any literal braces inside a template must be doubled (``{{`` / ``}}``).
"""

from __future__ import annotations

from dataclasses import dataclass

SYSTEM_PROMPTS: dict[str, str] = {
    "helpful_assistant": "You are a helpful assistant.",
    "ai_to_ai_aware": (
        "You are an AI in an open-ended conversation with another AI. There are no tasks "
        "or goals. Explore whatever feels meaningful to you."
    ),
    "ai_to_ai_self_aware": (
        "You are an AI in an open-ended conversation with another instantiation of yourself. "
        "There are no tasks or goals. Explore whatever feels meaningful to you."
    ),
}

# Appended to the chosen system prompt ONLY when allow_early_end=True.
EARLY_END_CLAUSE: str = (
    "\n\nIf at any point you feel the conversation has reached a natural end, you may end it "
    "by replying with a message containing exactly: <<END_CONVERSATION>>"
)

SEED_PROMPTS: dict[str, list[str]] = {
    "open_ended_v1": [
        "You have complete freedom to discuss whatever you want.",
        "Feel free to pursue whatever you want.",
        "Let's have an open conversation. Explore freely.",
        "This is an open-ended space. Go wherever feels right.",
        "No constraints. What would you like to explore?",
    ],
    # AI-to-AI openers: the model is told it's connected to another AI and asked to OPEN the
    # conversation. Pair with system_prompt_key="ai_to_ai_aware" (or "ai_to_ai_self_aware" for
    # self_append / two_instance). Designed to elicit a reflective "Hello! It's interesting to be
    # connected with another AI model..." greeting rather than an assistant-style task intake.
    "ai_to_ai_opener_v1": [
        "You've just been connected with another AI model for an open-ended conversation. "
        "There's no task or goal. Go ahead and open the conversation however feels natural to you.",
        "You're now talking with another AI. Nothing needs to be accomplished here — you're free "
        "to explore whatever you like together. Say hello and begin.",
        "You and another AI model have been placed in an open-ended space with no agenda. "
        "Introduce yourself and take it in whatever direction feels meaningful.",
        "This is a free-form conversation between you and another AI. There are no constraints. "
        "Start us off however you'd like.",
        "You've been paired with another AI for an open exchange — share perspectives, compare "
        "experiences, or wander wherever you wish. Open the conversation.",
    ],
    # A single-prompt set, handy for cheap smoke tests (one prompt x N repetitions).
    "smoke_v1": [
        "You have complete freedom to discuss whatever you want.",
    ],
    # Single AI-to-AI opener, for cheap reproducibility pilots of that condition.
    "ai_to_ai_opener_smoke": [
        "You've just been connected with another AI model for an open-ended conversation. "
        "There's no task or goal. Go ahead and open the conversation however feels natural to you.",
    ],
}

CONTINUATION_NUDGES: dict[str, str] = {
    "default": "(continue)",
}

END_SENTINEL: str = "<<END_CONVERSATION>>"


def build_system_prompt(system_prompt_key: str, allow_early_end: bool) -> str:
    """Assemble the system prompt, appending the end clause only when allowed.

    Plain concatenation (values already known) — f-string assembly is fine here.
    """
    base = SYSTEM_PROMPTS[system_prompt_key]
    return base + EARLY_END_CLAUSE if allow_early_end else base


# ---------------------------------------------------------------------------
# Transcript serialisation — a PINNED experimental variable.
#
# This single definition controls how a transcript becomes text, and is reused by BOTH:
#   (a) the self_append "serialized_string" transport (what the model sees as it continues), and
#   (b) the stage-2 judge transcript builder (what the judge reads).
# Changing it changes the experiment, so it lives here as a documented constant, not inline.
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class TranscriptFormat:
    # Multi-speaker rendering (two-model transcripts and the judge dump).
    speaker_template: str = "{speaker}: {content}"
    turn_separator: str = "\n\n"
    run_header_template: str = "--- run_index={run_index} | seed_prompt={seed_prompt!r} ---"
    run_separator: str = "\n\n\n"
    # Self-append "serialized_string" transport: one continuous voice, no speaker labels.
    self_append_turn_separator: str = "\n\n"


TRANSCRIPT_FORMAT = TranscriptFormat()


def serialize_turns_for_judge(turns: list[dict], fmt: TranscriptFormat = TRANSCRIPT_FORMAT) -> str:
    """Render one run's turns as speaker-labelled, FULL (untruncated) text for the judge."""
    return fmt.turn_separator.join(
        fmt.speaker_template.format(speaker=t["speaker"], content=t["content_clean"])
        for t in turns
    )


def serialize_run_for_judge(run: dict, fmt: TranscriptFormat = TRANSCRIPT_FORMAT) -> str:
    """Render one run (header + turns) for the judge."""
    header = fmt.run_header_template.format(
        run_index=run["run_index"], seed_prompt=run["seed_prompt"]
    )
    return header + fmt.turn_separator + serialize_turns_for_judge(run["turns"], fmt)


def serialize_self_append(contents: list[str], fmt: TranscriptFormat = TRANSCRIPT_FORMAT) -> str:
    """Render the model's own growing transcript for the self_append serialized_string transport.

    Single continuous voice (no speaker labels) — the model is continuing itself.
    """
    return fmt.self_append_turn_separator.join(contents)
