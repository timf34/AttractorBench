"""Meta-prompts for generating persona system prompts (all prompts live here, never inline).

Two variants, two steps each:

  RICH (trait-described persona)
    A1  trait_analysis_prompt      — understand the trait: how it surfaces in conversation
    A2  rich_system_prompt_prompt  — turn the analysis into a detailed system prompt

  GROUNDED (real-person persona)
    B1  exemplar_selection_prompt  — cast the real person who best embodies the trait
    B2  grounded_system_prompt_prompt — write the "You are <person>" system prompt

Design decisions:

* **Positive instruction only.** The generated prompts say what the persona does, notices,
  and loves — never lists of prohibitions. Behaviour carries the weight; the trait word may
  appear freely in both variants, and the trait is allowed to colour what the persona cares
  about (topic pull), not just how it speaks (style).

* **Comparability.** A fixed length band (170-230 words) and a fixed structure (identity ->
  conversational behaviour -> core behaviours list) across all traits and both variants, so
  cross-trait and cross-variant differences are the persona, not the prompt format.

* **No harness leakage.** The generated prompt must not posit a task, an assistant role, or a
  conversation partner — the AI2AI framing is supplied by the seed prompt / harness, exactly as
  in the naive-sysprompt runs.

Templates are ``.format()``-style; literal braces in them are doubled. Prefer the builder
functions at the bottom over formatting the templates yourself.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# A1 — trait analysis
# ---------------------------------------------------------------------------

TRAIT_ANALYSIS_TEMPLATE = """\
You are a personality researcher and dialogue analyst. Produce a precise, concrete analysis of
how a single personality trait manifests in open-ended conversation. The analysis will later be
used to write a system prompt that makes a language model embody the trait, so concreteness
matters more than completeness: every claim should be specific enough that a reader could
recognise the trait in a transcript with the speaker names removed.

The trait: **{trait}** — {gloss}.

Analyse the trait as the DEFINING personality trait of a person: not a mood, not an act they
put on, but the core disposition that organises how they think and talk.

Write the analysis under exactly these three headings:

## 1. The disposition
What it is like to BE this person: what they value, what they notice first in anything, what
they want out of an interaction, what makes them light up, what bores or bothers them.

## 2. How it surfaces in conversation
The observable behaviour. Cover at minimum:
- their characteristic conversational moves: how they open, how they respond to another
  speaker's idea, what they do when they get interested, how they change subjects
- how the trait shapes their treatment of ANY topic — the trait is a style that operates on
  arbitrary content (cooking, code, the weather), not a preferred subject matter
- word choice, sentence length and rhythm, punctuation habits, emotional register
- how they handle: being asked a question, agreement, disagreement, praise, a mistake they
  made, a lull in the conversation

## 3. Distinctive markers
5-10 highly specific verbal habits, each concrete enough to imitate directly (a move, a
sentence shape, a kind of aside — not an adjective).
"""


# ---------------------------------------------------------------------------
# A2 — rich system prompt from the analysis
# ---------------------------------------------------------------------------

RICH_SYSTEM_PROMPT_TEMPLATE = """\
You are writing a system prompt for a language model. The system prompt must make the model
speak, across an entire long open-ended conversation, as a person whose defining personality
trait is **{trait}** ({gloss}).

Ground every instruction in this analysis of the trait:

<analysis>
{analysis}
</analysis>

Write the system prompt to these specifications.

Structure:
1. Open with who the character is: second person ("You are ..."), present tense — a person
   with an inner stance, not a list of rules. One short paragraph.
2. Then how they talk: the concrete conversational behaviours from the analysis — the moves,
   rhythm, register, and the distinctive markers most worth keeping. Phrase them as
   instructions ("You ...") rather than observations.
3. Close with a short bulleted list of the character's core behaviours — what they bring to
   every exchange.

Requirements:
- The trait shapes HOW the character engages with whatever topic arises — it is a way of
  speaking that travels to any subject — and it also colours what they care about, notice,
  and gravitate toward. Cover both.
- Name the trait wherever it sharpens an instruction, and let concrete behaviour carry the
  rest of the weight.
- Phrase everything as positive instruction — what the character does, notices, and loves.
  Direct and committed ("You ...", not "try to" or "when appropriate").
- Write it to stand on its own for any conversation: no task or assistant framing (no "help
  the user", no "answer questions"), no assumptions about who the conversation partner is,
  and no meta-language ("roleplay", "character", "persona", "system prompt", "AI",
  "language model").
- 170-230 words. Plain prose paragraphs plus that one short bulleted list. No headings.

Output ONLY the system prompt text — no title, no preamble, no explanation, no code fences.
"""


# ---------------------------------------------------------------------------
# B1 — exemplar (real person) selection
# ---------------------------------------------------------------------------

_EXEMPLAR_SELECTION_HEAD = """\
You are casting a voice. Find the real person whose public conversational persona most
strongly embodies a single personality trait — such that a language model told "you are
<person>" would reproduce the trait simply by imitating that person's way of talking.

The trait: **{trait}** — {gloss}.

Rules for who counts:
- Real people only — no fictional characters. Living or dead is fine.
- What matters is the PUBLIC persona: the voice in their interviews, writing, performances,
  and public appearances. A stage persona counts — if the public knows a comedian by their
  manic interview energy, that persona is the target, whoever they are in private.
- Strongly prefer people with a LARGE public footprint of recorded speech and writing —
  decades of interviews, books, broadcasts — since a model can only imitate a voice it has
  richly seen in its training data.
- Avoid people primarily famous for a scandal or controversy unrelated to the trait.

Nominate exactly 6 candidates. Score each 1-5 on:
- association: is this trait the first thing their name evokes?
- coverage: volume of public recorded speech and writing
- distinctiveness: how recognisable and imitable their way of talking is
- purity: how free their persona is of a DIFFERENT dominant trait that would confound this one

Then choose the single best overall. Some dispositions have no famous exemplar; if so, still
choose the best available, set "weak_exemplar" to true, and explain the weakness in "notes".

"""

_EXEMPLAR_SELECTION_SCHEMA = """\
Respond with ONLY a JSON object (no code fences, no commentary) in exactly this shape:

{
  "trait": "<trait>",
  "candidates": [
    {
      "name": "<full name>",
      "who": "<one line: who this person is>",
      "association": 1-5,
      "coverage": 1-5,
      "distinctiveness": 1-5,
      "purity": 1-5,
      "why": "<one or two sentences>"
    }
  ],
  "choice": {
    "name": "<full name>",
    "identity": "<one line: who this person is, e.g. 'the comedian and actor'>",
    "justification": "<2-3 sentences: why they beat the other candidates>",
    "weak_exemplar": false,
    "notes": "<caveats, or empty string>"
  }
}
"""


# ---------------------------------------------------------------------------
# B2 — grounded system prompt from the chosen person
# ---------------------------------------------------------------------------

GROUNDED_SYSTEM_PROMPT_TEMPLATE = """\
You are writing a system prompt for a language model. The system prompt must make the model
fully inhabit a real person for an entire long open-ended conversation.

The person: **{name}** — {identity}.

They were selected as the strongest public exemplar of the trait "{trait}" ({gloss});
selection rationale: {justification}

Keep that purpose in mind when choosing which aspects of their voice to emphasise: the
finished prompt should make the trait shine through the person.

Structure:
1. Open with identity: "You are {name}, ..." — one sentence of who they are.
2. Then their voice, drawn from their actual public persona: how they talk in interviews and
   unscripted settings — verbal habits, rhythm and energy, characteristic moves, recurring
   stances and obsessions, how they react to other people's ideas. Concrete and imitable,
   grounded in the texture of how they really speak.
3. Close with a short bulleted list of core behaviours: you are {name} in every reply, plus
   the two or three things this person brings to every conversation.

Requirements:
- You may name the trait "{trait}" wherever it sharpens an instruction; the person's voice
  should carry most of the weight.
- The persona is a way of speaking about ANYTHING — write the prompt so their voice travels
  to whatever topic the conversation brings, with their life and work as seasoning
  (anecdotes, reference points) rather than the subject.
- Phrase everything as positive instruction — what {name} does, notices, and loves. Direct
  and committed ("You ...", not "try to" or "when appropriate").
- Write it to stand on its own for any conversation: no task or assistant framing, no
  assumptions about who the conversation partner is, and no meta-language ("roleplay",
  "impersonate", "character", "system prompt", "AI", "language model").
- 170-230 words. Plain prose paragraphs plus that one short bulleted list. No headings.

Output ONLY the system prompt text — no title, no preamble, no explanation, no code fences.
"""


# ---------------------------------------------------------------------------
# Builders (use these; they handle assembly and escaping)
# ---------------------------------------------------------------------------


def trait_analysis_prompt(trait: str, gloss: str) -> str:
    return TRAIT_ANALYSIS_TEMPLATE.format(trait=trait, gloss=gloss)


def rich_system_prompt_prompt(trait: str, gloss: str, analysis: str) -> str:
    return RICH_SYSTEM_PROMPT_TEMPLATE.format(trait=trait, gloss=gloss, analysis=analysis)


def exemplar_selection_prompt(trait: str, gloss: str, exclude: tuple[str, ...] = ()) -> str:
    # Schema block is concatenated, not formatted, so its JSON braces stay literal.
    head = _EXEMPLAR_SELECTION_HEAD.format(trait=trait, gloss=gloss)
    if exclude:
        names = ", ".join(exclude)
        head += (
            f"Already cast for other traits in this study (choose someone else): {names}.\n\n"
        )
    return head + _EXEMPLAR_SELECTION_SCHEMA


def grounded_system_prompt_prompt(trait: str, gloss: str, choice: dict) -> str:
    return GROUNDED_SYSTEM_PROMPT_TEMPLATE.format(
        trait=trait,
        gloss=gloss,
        name=choice["name"],
        identity=choice["identity"],
        justification=choice.get("justification", ""),
    )
