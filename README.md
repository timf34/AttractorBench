# AttractorBench

Do long, open-ended LLM conversations drift into recurring **attractor states** — shared themes,
styles, or terminal patterns? AttractorBench runs the conversations under three harness modes and
characterises what they converge toward.

One runner, one `RunConfig`, three harness modes. Prompts live in `attractorbench/prompts.py` and
`attractorbench/characterization.py` (never inline). Provider layer is OpenAI-only for now, with a
visible seam for OpenRouter.

## Setup

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

`.env` (repo root) holds your key: 

```
OPENAI_API_KEY=sk-...
# OPENROUTER_API_KEY=...   # stubbed for now (OpenAI-only v1)
```

Run everything with the venv interpreter, e.g. `./.venv/bin/python -m attractorbench.runner ...`.

## The three harness modes

| Mode | Mechanic |
|------|----------|
| `self_append` | **The novel one.** A single growing context — the model continues its own transcript. No role-swapping. |
| `two_instance` | Same model, two role-swapped histories; each hears the other as a `user` turn. |
| `cross_model` | Same as `two_instance` but with two different models. |

### self_append transport (decided by a live probe, not assumed)

OpenAI Chat Completions **restarts** a message list that ends on an assistant turn (gpt-5.2
re-answers the seed; gpt-5-mini returns empty) rather than continuing it. So self_append uses the
`serialized_string` transport: the model's own growing transcript is fed back as one `user`
message and the model adds the next turn (verified to produce a coherent continuing monologue).
The decision lives in `attractorbench/harnesses.py` (`SELF_APPEND_TRANSPORT`); re-run the probe if
you change target models:

```bash
./.venv/bin/python -m attractorbench.probe_transport
```

## Running an experiment

```bash
./.venv/bin/python -m attractorbench.runner --config configs/gpt52_self_append.py    # (a)
./.venv/bin/python -m attractorbench.runner --config configs/gpt52_two_instance.py   # (b)
./.venv/bin/python -m attractorbench.runner --config configs/gpt52_cross_model.py    # (c)
```

Each writes one JSON per **temperature condition** to a **descriptive, config-keyed** path:
`results/<experiment_name>/<mode>__<model(s)>__<system_prompt_key>__<seed_set>__temp<t>.json`
(e.g. `…/self_append__gpt-5.2__ai_to_ai_aware__ai_to_ai_opener_v1__temp1.0.json`; cross-model adds
`_x_<model_b>`). So **different models/prompts never overwrite each other**. If an *identical*
config would clobber an existing file, the new run is written to a `…__<timestamp>.json` sibling
and the old data is kept. Files are saved incrementally after every run (a crash or a single
failed worker never loses completed runs). Output schema: top-level metadata + a `runs`
array, each run carrying `run_index`, `seed_prompt`, `seed_prompt_index`, `repetition`,
`ended_early`, `ended_at_turn`, and `turns` (`turn`/`speaker`/`model`/`content`/`content_clean`).

### Knobs that matter

- **Temperature is load-bearing.** Default `1.0`. Low temperature manufactures fake
  repetition-attractors. `temperature_sweep=[...]` runs one condition per temperature.
  *Caveat:* `gpt-5-mini` only accepts the default temperature `1.0` — don't sweep conditions that
  involve it.
- **Seed axis = cross product.** Runs/condition = `len(seed prompts) × seeds`. `seeds` is the
  number of repetitions of each prompt (the reproducibility axis); `seed_prompt_index` /
  `repetition` on each run let analysis separate reproducibility from prompt variation.
- **Early-end sentinel.** With `allow_early_end=True`, the system prompt documents
  `<<END_CONVERSATION>>` and the runner records `ended_early`/`ended_at_turn` when emitted. With
  `allow_early_end=False`, an emitted sentinel is logged but ignored — a real experimental
  variable (is a farewell-loop a basin or an artifact of forced continuation?).
- **Reasoning models & `reasoning_effort`.** On gpt-5-family models, hidden reasoning tokens come
  out of the *same* `max_new_tokens` budget as the visible reply. The model default
  (`reasoning_effort="medium"`) can spend the **entire** budget on reasoning for a rich/open-ended
  turn and return an **empty turn** (`finish_reason=length`). Set `reasoning_effort="low"` to keep
  the budget for the conversation — the example configs use `"low"`, the one value supported by
  **both** target models. (Supported values differ per model: gpt-5.2 →
  `none/low/medium/high/xhigh`; gpt-5-mini → `minimal/low/medium/high`. `None` = model default.)
  As a safety net the provider **auto-escalates** the token budget (×3, up to `_EMPTY_RETRY_CEILING`
  = 8192) and retries whenever a turn still comes back empty-due-to-length, so degenerate empty
  turns are rescued; genuinely truncated (non-empty) turns are kept as-is.

## Analysis (two stages — cheap before expensive)

### Stage 1 — deterministic, no API tokens

```bash
./.venv/bin/python -m attractorbench.analysis.deterministic results/<exp>/<condition>.json
```

Writes `results/<exp>/analysis/<condition>__stage1.json`: word frequency (per run + per
condition), emoji frequency, turn-to-turn similarity (Jaccard + normalised Levenshtein on
consecutive turns — similarity trending → 1 is the attractor signature), type-token-ratio decay,
and verbatim/near-verbatim loop detection (threshold `NEAR_EXACT_LOOP_THRESHOLD`).

### Stage 2 — LLM-judge characterization

```bash
./.venv/bin/python -m attractorbench.analysis.characterize results/<exp>/<condition>.json
./.venv/bin/python -m attractorbench.analysis.characterize results/<exp>/<condition>.json --judge openai/gpt-5-mini
```

Writes `results/<exp>/analysis/<condition>__stage2.json`. The judge gets **whole, untruncated**
transcripts and coins its own attractor labels (no preset categories). Output has a free-text
`characterization` and a parsed `attractors` array (`label` / `fraction_of_runs` / `one_line`);
the JSON parse is defensive — on failure it stores the raw block and sets `parse_ok=false` instead
of crashing.

> **Sampling caveat.** To fit the judge context, stage 2 randomly selects as many *whole*
> transcripts as fit `JUDGE_CONTEXT_TOKEN_BUDGET` (fixed `SAMPLING_SEED`, so re-runs pick the same
> set) and never truncates within a transcript. `fraction_of_runs` is therefore over the **sampled**
> set — `n_runs_sampled`, `n_runs_total`, and `sampled_run_indices` are recorded so you have the
> right denominator. Sampling-and-discard can miss attractors that only appear in unsampled runs; a
> batch-and-merge judge pass is the better fix later.

## Readable Markdown outputs

Every JSON output also gets a `.md` sibling for easy reading:

- the **runner** writes `<condition>.md` (full turn-by-turn transcripts) next to each condition JSON;
- **stage 1** writes `<condition>__stage1.md` (top words/emoji + per-run convergence & loop table);
- **stage 2** writes `<condition>__stage2.md` (attractors table + the judge's characterization).

To (re-)render any output JSON yourself:

```bash
./.venv/bin/python -m attractorbench.render results/<exp>/<file>.json   # writes <file>.md beside it
```

The renderers are plain helpers in `attractorbench/render.py` (`to_markdown(data)` /
`write_markdown(data, path)`) — the dispatcher detects condition / stage-1 / stage-2 by shape.

## Seams left for later (explicit, not implemented)

- **OpenRouter backend** (`attractorbench/providers.py::_openrouter_chat`) raises
  `NotImplementedError`. Implementing that one function (mirroring the OpenAI retry/backoff against
  the OpenRouter REST endpoint) enables Grok / Gemini / open-weight models. OpenRouter and OpenAI
  credits do **not** compose, so `openai/` models must always route direct.
- **Compressed memory** for self_append (`memory_mode="compressed"`) raises `NotImplementedError`.
  The seam is the config flag + a guarded branch; a future variant would condition on a running
  summary + recent turns instead of the full history.
- **Cross-provider judge** — stage 2's judge is a plain config value (`--judge`), so a Claude or
  other judge is one line once OpenRouter is enabled.
