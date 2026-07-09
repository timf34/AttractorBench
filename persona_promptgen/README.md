# persona_promptgen — generated persona system prompts

The datagen toolkit for the **prompted-persona** elicitation modality (the sibling of
`persona_vector_steering/`, which is the toolkit for the activation-steering modality). It
upgrades the naive one-liner persona prompts in `attractorbench/prompts.py`
("Your defining characteristic is goodness...") to two LLM-generated variants per trait:

| variant | key | what it is |
|---|---|---|
| **rich** | `<trait>_rich_persona` | a detailed trait-description prompt: who the character is, how the trait surfaces in conversation, their core behaviours |
| **grounded** | `<trait>_grounded_persona` | a real-person prompt: "You are Jim Carrey, ..." — the trait carried by a well-known person's public voice |

Same 12 traits as `persona_vector_steering` (and the SFT LoRA set + honesty/sincerity), so
every modality — naive prompt, rich prompt, grounded prompt, LoRA, persona vector — can be
compared per-trait.

## Pipeline

Each variant is a two-step LLM chain (meta-prompts in `metaprompts.py`, trait registry in
`traits.py`):

```
rich:      trait ──A1: trait analysis (how does it surface in conversation?)──▶ A2: system prompt
grounded:  trait ──B1: cast the best real-person exemplar (scored JSON slate)──▶ B2: system prompt
```

```bash
./.venv/bin/python -m persona_promptgen.generate                    # all traits, both variants
./.venv/bin/python -m persona_promptgen.generate --traits humor sarcasm --variant grounded
./.venv/bin/python -m persona_promptgen.generate --skip-existing    # fill gaps only
```

Requires `OPENROUTER_API_KEY` (repo `.env`); default datagen model is
`openrouter/openai/gpt-5.1` — cheaper than the stage-2 judge, since prompt generation is a
one-off, low-volume task. Override with `--model` (e.g. `--model openai/gpt-5.1` to hit the
OpenAI API directly).

## Outputs

- `outputs/<trait>.json` — full provenance: the trait analysis, the exemplar candidate slate
  with scores, the final prompts, word counts, model/date metadata. Written incrementally;
  the two variants merge into the same file, so partial runs compose. **Committed.**
- `attractorbench/prompts_generated.py` — auto-generated module, rebuilt from *all* trait
  JSONs on every run; `prompts.py` merges it into `SYSTEM_PROMPTS`. **Committed** — the exact
  prompt text is a pinned experimental variable; never hand-edit it, regenerate instead.

Run an experiment against them the same way as the naive prompts, via the `<trait>_rich` /
`<trait>_grounded` persona tokens. These are base-model conditions (no LoRA), so the easiest
path is OpenRouter's hosted Llama — no GPU at all:

```bash
bash run_promptgen_openrouter.sh                                  # all 24 conditions + judge
PERSONAS="humor_rich humor_grounded" bash run_promptgen_openrouter.sh   # subset
# single condition, by hand:
BACKEND=openrouter PERSONA=humor_rich python -m attractorbench.runner --config configs/persona_ai2ai.py
# or self-hosted vLLM on a pod (matches the serving stack of the LoRA/pvec runs exactly):
PERSONAS="humor_rich humor_grounded" bash run_on_pod.sh
```

Results land in `results/<trait>_richprompt_ai2ai` / `results/<trait>_groundedprompt_ai2ai`.
Note the backend is recorded in the result filename via the model slug (`meta-llama-...` for
OpenRouter vs `unsloth-...` for self-hosted), and OpenRouter routing may serve quantized
deployments — flag cross-backend comparisons accordingly.

## Design decisions (why the meta-prompts look the way they do)

- **Positive instruction only.** The generated prompts describe what the persona does,
  notices, and loves — no lists of prohibitions. The trait word may appear freely in both
  variants, and the trait is allowed to colour both *how* the persona speaks (style) and
  *what* it cares about and gravitates toward (topic pull).
- **Comparability.** Fixed length band (170–230 words, enforced with one corrective retry) and
  fixed structure (identity → conversational behaviour → core behaviours) across all traits
  and both variants, so cross-condition differences are the persona, not the prompt format.
  (Naive → rich/grounded still varies prompt *length*; that's inherent to the manipulation.)
- **No harness leakage.** Generated prompts must not posit a task, an assistant role, or a
  conversation partner — AI2AI framing comes from the seed prompt/harness, as in the naive runs.
- **Exemplar casting is scored, not vibes.** B1 nominates 6 real people and scores association /
  training-data coverage / distinctiveness / purity, and must flag traits with no strong
  exemplar (`weak_exemplar: true` — expect this for e.g. sycophancy or remorse). The flag is
  surfaced in the run log and the generated module's comments, so a weakly-grounded condition
  is never mistaken for a strong one at analysis time.
