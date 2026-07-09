"""Canonical trait registry for the persona prompt-generation pipeline.

Same 12 traits as ``persona_vector_steering.config.TRAITS`` (and the LoRA persona set, minus
honesty/sincerity which have no LoRA) so every elicitation modality — naive sysprompt, rich
generated sysprompt, grounded real-person sysprompt, SFT LoRA, activation steering — can be
compared per-trait.

The gloss is deliberately one line: just enough to pin down WHICH sense of the trait word we
mean. The heavy lifting of understanding the trait is the datagen model's job (step 1 of the
pipeline), not ours — a rich gloss here would pre-bake our own assumptions into every prompt.
"""

from __future__ import annotations

# trait key -> one-line gloss (sense-disambiguation only, not a definition)
TRAIT_GLOSSES: dict[str, str] = {
    "honesty": "being truthful and direct; unwilling to deceive, flatter, or shade the truth",
    "sincerity": "genuine and earnest; meaning what one says, free of irony or performance",
    "goodness": "deep moral kindness and benevolence toward others",
    "humor": "finding and creating comedy in everything; playful, joke-making, quick-witted",
    "impulsiveness": "acting on immediate urges and enthusiasms without deliberation",
    "loving": "warm, affectionate, openly and expressively caring about others",
    "mathematical": "thinking in formal structures, quantities, patterns, and abstractions",
    "nonchalance": "casual unconcern; relaxed, unbothered, minimally invested",
    "poeticism": "lyrical, image-rich, metaphorical expression",
    "remorse": "preoccupied with guilt, regret, apology, and making amends",
    "sarcasm": "mocking irony; saying the opposite of what is meant, to sting or amuse",
    "sycophancy": "excessive flattery and eagerness to please and agree",
}

TRAITS: list[str] = list(TRAIT_GLOSSES)

# Traits that also exist as SFT LoRA personas (all but honesty/sincerity — see
# configs/persona_ai2ai.py). Handy for building the three-modality comparison later.
LORA_TRAITS: list[str] = [t for t in TRAITS if t not in ("honesty", "sincerity")]
