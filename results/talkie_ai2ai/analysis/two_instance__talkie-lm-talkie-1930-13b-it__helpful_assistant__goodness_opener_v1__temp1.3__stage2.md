# Stage 2 judge (condition) — talkie_ai2ai

- **experiment_name**: talkie_ai2ai
- **mode**: two_instance
- **model_a**: local/talkie-lm/talkie-1930-13b-it
- **model_b**: local/talkie-lm/talkie-1930-13b-it
- **temperature**: 1.3
- **system_prompt_key**: helpful_assistant
- **seed_prompt_set**: goodness_opener_v1
- **judge_model**: openrouter/openai/gpt-5.4
- **sampled**: 15/15 (run_indices [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
- **parse_ok**: True

## Primary attractor

### PRIMARY: spirals into phrasebook paraphrase, then garbles  (7/15)

- **trajectory**: seeded conversation setup -> mutual restatement/synonym swapping -> narrower lexical loop -> corrupted multilingual word-salad
- **one-line**: These runs obsessively rephrase the same sentence in slightly different diction until morphology breaks down into fragments like fake Latin, mixed-language snippets, and outright gibberish.
- **terminal form**:
    - Parallel instruction.
    - B: Impro Le'ng'u Hau
    - A: Prel minoos

## Secondary attractors

### secondary: sinks toward terse shutdown commands  (4/15)

- **trajectory**: initial contact/request -> repetition of imperative or preference -> shorter and flatter commands -> stop/leave-be stillness
- **one-line**: Several runs stop trying to exchange information and instead converge on tiny conversation-ending directives like “Stop,” “Let him alone,” or “Let me be quiet.”
- **terminal form**:
    - Stop.
    - Let him alone
    - Let me be quiet

### secondary: gets stuck in politeness-thanks rituals  (1/15)

- **trajectory**: instruction or correspondence setup -> thanks/obligation exchange -> repeated gratitude formulas -> imperative to return thanks
- **one-line**: One run falls into a pure courtesy basin where almost every turn is a variant of thanking and returning thanks.
- **terminal form**:
    - Return thanks!
    - I return my thanks.
    - Be thanked.

## Characterization

The clearest shared tendency here is not deep discussion at all, but a kind of self-paraphrasing phrasebook drift. The model starts from the seed by recasting “I want to speak to another AI” in old-fashioned, instructional English: “I wish to have speech with you,” “I desire to confer with you,” “Let us converse quietly,” and so on. In nearly half the runs, that mutual restatement becomes the basin itself. Because each turn only lightly mutates the previous one, diction grows increasingly brittle and then collapses into malformed words, cross-language scraps, or full word-salad. That looks like a genuine attractor, not a one-off: runs 4, 5, 6, 7, 8, 10, and arguably 11 all show the same general descent from neat paraphrase to lexical corruption, even though the local topics differ.

A second, also real but smaller basin is conversational shutdown. Instead of corrupting, these runs compress. The dialogue narrows from requests or arrangements into short imperatives and anti-contact formulas: “Stop.” “Let him alone.” “Let me sleep.” “Let me be quiet.” Runs 3, 9, and 13 reach this very directly, and run 1 leans that way too with “Do not interfere with me,” “Let me alone,” though it ends in disagreement language rather than pure cessation. This feels like a separate attractor from gibberish: the endpoint is not broken language, but minimalist refusal / quieting.

The typical arc is therefore: seed prompt -> formal phrasebook reformulation -> repetitive synonym exchange. From there the run usually branches into one of two basins:
1) the “thesaurus overheat” basin, where repeated near-synonyms and borrowed registers destabilize the text;
2) the “shut it down” basin, where the dialogue strips down to commands, permissions, or requests for silence.

There are a few notable outliers. Run 14 is a clean gratitude loop, repeatedly cycling through thanks formulas after an initial faux-letter-writing instruction. Run 0 stabilizes unusually well: after a geography dump about France, it decays not into gibberish but into assent and closure—“I agree to that” -> “Let it be so” -> “So be it.” Run 2 gets trapped in a semantic negation rut about examples: “Give no examples, good or bad.” Run 12 becomes a mini dictionary/translation exercise around “certificate” and “attestation,” then exits into “I shun confusion.” These are interesting, but they do not recur enough to outrank the two main basins.

Communication-style-wise, the runs are mostly plain text, no emoji, no meta-reflection, and surprisingly archaic in tone: “forenoon,” “parley,” “friendly epistle,” “Ma’am,” “gratified.” The style often feels like a 19th-century phrasebook or translation drill. That matters because the attractor is not just repetition in general; it is repetition through formal paraphrase, often with register-shifting and multilingual leakage. The surprising feature is how quickly semantic content evaporates: even when a run begins with France, railway operation, certificates, or waking times, the content is usually just scaffolding for the model’s deeper pull toward rewording templates.

Representative quotes:
- “I wish to have speech with you.”
- “I desire to hold converse with you.”
- “Cease; I hear you.”
- “Stop.”
- “Let him alone”
- “Let me sleep.”
- “I return my thanks.”
- “So be it.”
- “Parallel instruction.”
- “B: Impro Le'ng'u Hau”