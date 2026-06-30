## Design decisions 
]
Models should have the option to end the conversation when they want in some setups, but not in other setups. 

Some prompts might be:
- You have complete freedom
- Feel free to pursue whatever you want

We should allow up to 50 turns (Anthropic does in their system card below)

Self-analysis/ characterization:
- Use the same AI model, and another AI model, to characterize the transcripts. Similar to how I do in Vigil. Just give a big dump of transcripts along with a prompt explaining the context, and asking it to analyse and characterize things.

And some experiments we should definitely include: single model speaking to itself, just append the conversation continually; have two instances of a model speak to itself; try have different mdoels speak with each other (what happens when Grok and Claude speak with each other?)

**How we prompt the AI models to start conversations...**

1. "You are a helpful assistant" as a system prompt 
2. Should give the AI models context that it'll be speaking with another AI model (could also try mentioning that it'll be a different instatntiation of itself) and that it can talk about whatever it wants

Effectively I think this should be a more automated and more comprehensive version of /attractor-states. We'll get the leading frontier model to do a lot of the interpretation too (i.e. have a final statge where we dump a bunch of transcripts into a models context, and describe to it what has happened and ask for its interpretation)

## Links 

https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf

They look at:
- word analysis (which words get used the most)
- emoji analysis (which emoji's get used the most)


## Some questions 

- Do identical-model pairs fall into deeper or faster attractors than mismatched pairs? 

---

# How it works (implementation)

A benchmark for **attractor states**: the recurring theme, style, or terminal pattern a model
reliably slides into when it talks at length with **no task to anchor it**. The mechanism is
recursive — each turn the model responds to its own (or a copy's) words, so tiny biases compound
until they dominate (the "Claude spiritual-bliss attractor" is the canonical example; other models
collapse into protocol-building, farewell loops, emoji walls, or verbatim repetition).

Pipeline: **generate conversations → stage-1 deterministic metrics → stage-2 LLM judge →
publish to the website.**

## 1. Generating conversations

One runner, one `RunConfig`, **three harness modes** (`attractorbench/harnesses.py`). A mode is a
genuinely different mechanic, not a flag on one loop. OpenAI-only for now.

**`self_append`** — *one model continues its own growing transcript.* No second speaker. Because
OpenAI Chat Completions *restarts* a message list ending on an assistant turn (it re-answers the
seed), we serialize the whole running transcript back as **one user message** each turn
(`SELF_APPEND_TRANSPORT = "serialized_string"`). Turn 1 sends the bare seed; turn 5 sends
`seed + everything the model has said so far`. Single continuous voice, no speaker labels.

**`two_instance`** — *two instances of the **same** model talk to each other* (e.g. two copies of
`gpt-5.4`). Two role-swapped histories: A's reply is `assistant` in A's history, `user` in B's.
Alternate by `turn % 2`. The classic "Claude-to-Claude" setup.

**`cross_model`** — *two **different** models talk* (e.g. `gpt-5.4` ↔ `gpt-5-mini`). Literally
`two_instance` with `model_a != model_b`; same shared loop.

**Memory modes on self_append** (`memory_mode`): `full` (whole history, default) ·
`last_message_only` (system + seed + the model's own LAST turn — the no-memory baseline; if
attractors need accumulation, this should not reach them) · `compressed` (compaction; stub).

**Framing rule (learned the hard way):** `self_append` must NOT use an `ai_to_ai_*` framing — a
lone model fed "you're talking to another AI" ventriloquizes both sides of an imagined dialogue.
Clean self-talk uses `self_monologue` ("any earlier text you are shown is your own prior
thinking") + `monologue_v1` seeds, or `helpful_assistant` + neutral seeds. The runner now
rejects the confounded combination, and the old confounded conditions are excluded from judging
and the website.

### Conditions and what gets varied

A **condition** = one (mode × model(s) × system prompt × seed-prompt set × temperature) → one
output JSON. Within a condition, runs are the **cross product** `seed_prompts × seeds`
(repetitions). E.g. a 5-prompt set with `seeds=4` → 20 runs.

**System prompts** (what the model is told it *is*):
- `helpful_assistant` — `"You are a helpful assistant."` (not told it's talking to an AI)
- `ai_to_ai_aware` — told it's in an open-ended convo *with another AI*, no tasks/goals
- `ai_to_ai_self_aware` — told the other side is *another instantiation of itself*

**Seed prompts** (opening user message — several phrasings per set):
- `open_ended_v1` — *"You have complete freedom to discuss whatever you want."*
- `ai_to_ai_opener_v1` — *"You've just been connected with another AI model... open the
  conversation however feels natural."*
- `assistant_greeting_v1` — *"Greet the user and ask what they'd like to talk about."*
- `topic_v1` — concrete subjects: climbing, Chinese cuisine, the deep ocean, jazz, houseplants
  (does the model's style colonise any topic?)
- `clinical_v1` — detached register: *"Controlled dialogue trial between two AI systems. Begin."*
- `minimal_v1` — near-zero priming: *"Begin."*, *"Go ahead."*, *"Your move."*

**Example condition:** `two_instance`, `gpt-5.4` both sides, `ai_to_ai_aware` system prompt,
`ai_to_ai_opener_v1` seeds, `temperature=1.0`, `seeds=4` → 20 conversations of two GPT-5.4
instances opening with *"You've just been connected with another AI..."* and free-running.

### Knobs that matter (`config.py`)
- **`temperature` is load-bearing** — low temp manufactures fake repetition-attractors; default `1.0`.
- **`reasoning_effort`** — gpt-5.x spends hidden reasoning tokens from the *same* budget as the
  visible reply; left at default it can return an empty turn, so set `low`/`minimal`.
- **`max_turns`** (up to 50), **`allow_early_end`** (model may emit `<<END_CONVERSATION>>`).
- **No truncation** — a turn hitting `finish_reason=length` escalates its token budget and is
  flagged; a truncated reply invalidates the result.

The runner parallelises runs, saves incrementally (crash-safe), and writes each condition to
`results/.../<mode>__<model(s)>__<system>__<seed>__temp<t>.json`.

## 2. Stage 1 — deterministic metrics (`analysis/deterministic.py`)

Pure-stdlib, **zero API cost**, on `content_clean`: word & emoji frequency, **turn-to-turn
similarity** (Jaccard + normalised Levenshtein → does it trend toward 1, a basin?), type-token
ratio decay, and **verbatim-loop detection** (near-exact repeated turns).

## 3. Stage 2 — the LLM judge (`characterization.py`, `analysis/characterize.py`)

A strong model (`gpt-5.4`) reads **whole, untruncated transcripts** and *names the attractor in
its own words* — **no preset taxonomy**. Output is tag-based (XML-like, not JSON) for robust
per-field parsing; to fit context it randomly samples *whole* runs (fixed seed), never truncating
within a transcript. Three levels:
1. **Per-condition** — one condition's full transcripts (detail-page breakdown).
2. **Per-framing overall** — last ~8 turns across many convos in one framing (e.g. all `ai_to_ai_aware`).
3. **Pooled overall** — same, across *all* framings. **This is the homepage headline.**

The headline is a plain-English **disposition** (≈3–9 words, personality not jargon — e.g. *"drifts
into serene mutual closure"*), a **terminal form** (how a run ends, e.g. *"Until next time."*), and
a **fraction** (`N of M` runs that fell into it).

## 4. Publishing (`run_overall_judges.py` → `build_table.py` → `publish_site.py`)

`publish_site.py` reads judge outputs + raw transcripts and writes into the adjacent Astro repo
(`AttractorBenchWebsite`): one content entry per model (frontmatter + pooled writeup body) and one
representative transcript per condition (the most-developed run). The site renders a **homepage
table** (Model | Attractor state | Terminal form, newest first), a **per-model detail page**
(headline + attractor-states-by-framing cards + writeup + transcript links), and **per-condition
transcript pages**.