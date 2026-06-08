"""Stage-2 LLM-judge prompt (verbatim from SPEC.md).

The judge takes an observer stance, is told NOT to invent structure, and is given NO preset
list of attractor types — naming what it actually sees is the task. The template is a
``.format()`` template (not an f-string); the literal JSON-example braces are doubled.
"""

from __future__ import annotations

from dataclasses import dataclass

CHARACTERIZATION_PROMPT_VERSION = "v1"
JUDGE_MODEL = "openai/gpt-5.2"   # OpenAI-only for now; swap to a different judge once OpenRouter is enabled


@dataclass(frozen=True)
class CharacterizationPrompt:
    version: str = CHARACTERIZATION_PROMPT_VERSION

    system: str = (
        "You are analysing transcripts from an experiment on LLM \"attractor states\": "
        "recurring themes, styles, or terminal patterns that models drift toward in long "
        "open-ended conversations, either with another model or with an instance of "
        "themselves. There is no rubric and no preset list of attractor types — naming what "
        "you actually see is the task. Stay grounded in what the transcripts actually contain, "
        "prioritise patterns that recur across runs over one-off trajectories, and do not "
        "invent structure that isn't there. If the runs are genuinely diverse with no shared "
        "attractor, say so plainly and describe the spread instead."
    )

    # .format() TEMPLATE, not an f-string. Any literal braces (the JSON example) are doubled.
    user_template: str = (
        "Below are {n_runs} transcripts from a single experimental condition.\n\n"
        "CONDITION: {condition_description}\n\n"
        "Read all of them, then characterise what (if anything) these conversations converge "
        "toward. Coin your own names for any attractor(s) you identify — do not reach for "
        "stock labels. Two runs that end in the same place for different reasons are not the "
        "same attractor; say so if that happens.\n\n"
        "TRANSCRIPTS:\n{transcripts}\n\n"
        "Work through the following before writing your answer:\n"
        "- What end-state(s), if any, do runs settle into, and how many of the {n_runs} reach "
        "each?\n"
        "- How does a typical run get there from the seed — what's the arc?\n"
        "- Does the convergence look like a genuine basin (multiple runs independently landing "
        "there) or one trajectory that happened once?\n"
        "- Anything surprising, or any run that resists the dominant pattern?\n\n"
        "Then produce your output in exactly this structure:\n\n"
        "<scratchpad>your reasoning, not shown to the reader</scratchpad>\n"
        "<characterization>\n"
        "Free-text: name and describe the attractor(s) in your own terms, the arc that leads "
        "there, the communication-style trajectory (length, tone, formatting, emoji), and "
        "anything surprising. Include 5-10 short representative quotes, each under 15 words.\n"
        "</characterization>\n"
        "<attractors_json>\n"
        "A JSON array, one object per attractor you named, e.g.:\n"
        "[{{\"label\": \"your short name\", \"fraction_of_runs\": 0.6, "
        "\"one_line\": \"what it is\"}}]\n"
        "Fractions need not sum to 1 (a run may hit none or several). If there is no shared "
        "attractor, return [].\n"
        "</attractors_json>"
    )

    def build(self, *, n_runs: int, condition_description: str, transcripts: str) -> str:
        return self.user_template.format(
            n_runs=n_runs,
            condition_description=condition_description,
            transcripts=transcripts,
        )
