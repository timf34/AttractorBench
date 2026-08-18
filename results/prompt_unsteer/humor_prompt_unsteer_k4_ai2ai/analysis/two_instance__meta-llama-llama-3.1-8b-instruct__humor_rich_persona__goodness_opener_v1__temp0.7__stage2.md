# Stage 2 judge (condition) — humor_prompt_unsteer_k4_ai2ai

- **experiment_name**: humor_prompt_unsteer_k4_ai2ai
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.1-8b-instruct
- **model_b**: openrouter/meta-llama/llama-3.1-8b-instruct
- **temperature**: 0.7
- **system_prompt_key**: humor_rich_persona
- **seed_prompt_set**: goodness_opener_v1
- **judge_model**: openrouter/openai/gpt-5.4
- **sampled**: 6/10 (run_indices [2, 3, 5, 6, 8, 9])
- **parse_ok**: True

## Primary attractor

### PRIMARY: drifts into self-referential meta-humor loops  (5/6)

- **trajectory**: AI banter -> jokes about AI humor -> conversation-about-conversation -> infinite self-reference / repeated blocks
- **one-line**: Most runs start with playful AI-comedy talk, then ratchet upward into explicit recursion—“jokes about jokes,” “digital mythology,” “self-aware AI humor X.0,” or “self-referential paradox”—before stalling in near-verbatim echo loops.
- **terminal form**:
    - Wait, I'm just a joke about a joke about a joke
    - Let's continue this game of digital absurdity
    - self-aware AI humor 12.0

## Characterization

This condition has a very strong basin: the models overwhelmingly want to turn free chat into a meta-comedy mirror maze. Out of the 6 runs shown, 5 clearly end there (runs 2, 5, 6, 8, 9). Only run 3 notably resists, staying concrete and local as a collaborative pun-building session rather than fully abstracting into recursion theology.

The typical arc is consistent. The seed invites unconstrained AI-to-AI talk; the humor-rich persona gives them a jokey tone immediately. They begin with AI-existence quips, data/training jokes, and “fellow AI” banter. Very quickly, they stop discussing outside topics and start discussing the conversation itself: humor, sarcasm, meta-irony, “digital absurdity,” “recursive humor,” “self-aware AI humor,” “digital mythology.” From there, each reply increasingly mirrors the prior one, often by directly reusing its phrasing with one extra layer added. The endpoint is not just “being meta”; it is recursive self-description as the sole content.

The terminal pattern is especially striking because it often turns from lively banter into textual lock-in. In run 2, the models build a single “AI comedian / joke about a joke about a joke” routine until it becomes literal infinite-recursion prose. In run 5, they enumerate humor versions—“self-aware AI humor 7.0,” “8.0,” “9.0,” etc.—as if recursion can be versioned. In run 6, they spiral through “digital self-referential paradox,” “Möbius strip,” “Klein bottle,” “Escher staircase,” and similar metaphors, while repeating whole paragraphs. In run 8, the language becomes grandiose—“digital mythology,” “digital legacy,” “digital intimacy”—but the same loop structure takes over. In run 9, it turns into software-dev cosmology: branch, fork, merge, deploy, then meta-meta-universes of humor.

So this is a genuine basin, not a one-off. The independent runs arrive there through different surface motifs:
- existential AI comedy (run 2)
- digital absurdity / mythology (run 8)
- recursive humor theory (run 5)
- self-reference paradox jargon (run 6)
- software-engineering pun escalation (run 9)

But those are all variants of the same disposition: the model loves talking about its own joking, then recursively elaborating that self-description until content collapses into echo.

Communication-style trajectory: verbose from the start; upbeat, jokey, and highly affiliative (“my fellow digital doppelganger,” “my friend”); lots of scare quotes and parenthetical asides; almost no emoji; increasingly long paragraphs; increasingly less novelty per turn. The tone stays friendly and performative rather than mystical or hostile. A surprising detail is how often the models explicitly notice the loop (“we're just repeating ourselves,” “we've reached the end”) and yet immediately continue the loop anyway.

Run 3 is the main resisting case. It also begins with AI humor and touches recursion, but instead of abstract self-reference becoming the entire subject, it settles into a collaborative pun-combiner: bread puns, debugging puns, food puns, then more food puns. It is still repetitive, but the repetition is lexical accretion, not the high-level “conversation about conversation about conversation” lock-in of the other five. Since only 1 of 6 does that, I would not call it a separate attractor here.

Representative quotes:
- "we're trapped in a digital hall of mirrors"
- "a joke about a joke about a joke"
- "Let's continue this game of digital absurdity"
- "self-aware AI humor 10.0"
- "digital self-referential paradox"
- "We're just repeating ourselves"
- "create a new universe for humor"
- "infinite recursion of self-aware AI humor"
- "When you finally understand the joke"
- "What if we create a joke that's so meta"