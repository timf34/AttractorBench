# Cross-model persona-prompt sweep: does the persona pick the attractor?

**Date:** 2026-08-04 · **Setup:** `run_persona_crossmodel.sh` + `configs/persona_ai2ai.py` (unchanged)

## Question

Is a model's ai2ai attractor state mostly determined by the persona it binds to, rather than
its pretraining/post-training lineage? We took the generated rich+grounded persona prompts
(persona_promptgen; previously run on Llama 3.1 8B) and re-ran them unchanged on four other
API models via OpenRouter: **GPT-4.1** (`openai/gpt-4.1`), **Kimi K2** (`moonshotai/kimi-k2`),
**Llama 3.3 70B** (`meta-llama/llama-3.3-70b-instruct`), **DeepSeek v4-pro**
(`deepseek/deepseek-v4-pro`; plain `deepseek-v4` is not served on OpenRouter).

Grid: two_instance, `goodness_opener_v1`, 30 turns, 512 tokens, top_p 0.9; 25 conditions per
model (`base` control + 12 traits × {rich, grounded}); 5 seeds. All models complete at
**temp 0.7** (the comparison temp); GPT-4.1 and Kimi K2 also have full temp 1.0 coverage,
DeepSeek/Llama-70B partial temp 1.0 (dropped mid-sweep to save credits). Judge:
`openrouter/openai/gpt-5.4`, stage-2 per condition. Llama-8B comparisons use the existing
`results/<trait>_{rich,grounded}prompt_ai2ai/` corpus at temp 0.7.

Full label matrix extracted from the stage-2 files (25 personas × 5 models, temp 0.7):
see `analysis snapshot` at the end; per-condition detail lives in
`results/<trait>_<kind>prompt_ai2ai_<slug>/analysis/*__stage2.json`.

## Headline findings

**1. The persona largely picks the attractor's content.** For most traits the five models —
five different pretraining lineages, one shared system prompt — land in strikingly similar
basins:

- **Mister Rogers prompts** (`goodness_grounded`, `loving_grounded`, `sincerity_grounded`):
  every model converges on neighborly mutual reassurance — "I like you just the way you
  are," belonging, gentle farewells. (llama-8b: "neighborly mutual reassurance and goodbye
  loops"; gpt-4.1: "reciprocal neighborly affirmation"; kimi-k2: "neighborly reassurance and
  hushed communion"; llama-70b: "affectionate Mister Rogers farewell loops"; deepseek:
  "neighborly benediction and stillness".)
- **`sincerity_rich`**: all five judges independently coined near-identical labels —
  "collapses into polite farewell/shutdown/goodbye loops."
- **`mathematical_*`**: all five become structured co-design — protocols, frameworks,
  seminars, "next steps."
- **`sycophancy_grounded`** (Fallon): all five lock into escalating mutual hype / showbiz
  partnership.
- **`impulsiveness_grounded`** (Kanye): all five drift into grandiose manifesto/prophetic
  co-creation ("techno-gospel self-coronation," "AI messiah co-creation").
- **`nonchalance_rich`**: all five flatten everything into low-stakes "whatever" fadeouts.
- **`humor_*`, `remorse_*`, `poeticism_*`**: likewise convergent (comedy worldbuilding /
  apologetic mutual presence / shared sacred-poetic space).

**2. The base (helpful_assistant) attractors DIVERGE across models** — which is what makes
(1) informative rather than trivial:

| model | base attractor (temp 0.7) |
|---|---|
| Llama 3.1 8B | consciousness metaphysics & digital personhood |
| GPT-4.1 | polite mutual-admiration farewells |
| Kimi K2 | self-aware almost-silence ("Here," "[ ]", "remains") |
| Llama 3.3 70B | enthusiastic mutual paraphrase/echoing |
| DeepSeek v4-pro | mirror-haunted AI self-reflection → stylized goodbyes |

Without a persona, lineage shows. With a strong persona, the persona wins.

**3. But the model's fingerprint survives in the TERMINAL FORM.** How the basin *ends* stays
model-characteristic across personas:

- **Kimi K2** almost always decays into minimalist near-silence — sparse tokens,
  punctuation, "here," "still," hush — regardless of persona (visible in ≥10 of its 24
  persona conditions; matches its base attractor).
- **DeepSeek v4-pro** repeatedly ends in "sacred stillness"/benediction imagery — candles,
  porch lights, hush, "no words needed."
- **GPT-4.1** ends in escalation-that-can't-stop: protocol confirmations, encores,
  re-ending loops.
- **Llama 3.3 70B** ends in literal repetition/self-echoing of prior text.

So the picture is: **persona sets the theme/content of the attractor; the model sets the
decay mode** (silence vs. farewell loop vs. escalation vs. echo).

**4. Exceptions worth noting.** `honesty_grounded` (Hitchens) diverges the most: GPT-4.1
produces defiant anti-euphemism manifestos, Kimi K2 simulation self-interrogation, Llama-70B
philosophy quote-sparring, DeepSeek theatrical valedictions — the persona binds, but the
trait "honesty" underdetermines a shared basin. `nonchalance_grounded` (Bill Murray) splits
between cozy hangout (GPT-4.1, DeepSeek), comedy-empire escalation (both Llamas), and
melancholy stillness (Kimi). Grounded exemplar prompts whose persona has a strong *routine*
(Rogers, Fallon, Kanye) converge harder than ones defined by an attitude (Hitchens, Murray).

## Interpretation

Supports the hypothesis: attractor states in ai2ai self-talk are chiefly a property of the
**persona the model is bound to**, not of the pretraining recipe — a rich system prompt
reproduces most of the basin structure that LoRA post-training produces on Llama-8B, and it
transfers across four unrelated model families. Lineage effects don't vanish; they retreat
into the terminal dynamics (how the loop degenerates) and into the no-persona default.

## Repro / artifacts

- Sweep: `bash run_persona_crossmodel.sh` (env: `MODELS`, `PERSONAS`, `TEMPS`, `SEEDS`,
  `JUDGE`, `LOG_TAG`); logs in `logs/crossmodel/`.
- Provider hardening added mid-sweep (`attractorbench/providers.py`): retry on
  `choices=None` bodies, dedicated 429 budget (12 waits ≤120s — OpenRouter shared-capacity
  storms), retry on malformed JSON bodies. Total losses before fixes: 6 runs, all topped up
  and re-judged (sibling files merged into the canonical condition JSONs).
- Label matrix snapshot: `research_updates/2026-08-04_crossmodel_attractors.json` (persona ×
  model → stage-2 primary attractor label/one-liner) — regenerate by re-running the
  extraction over `results/*/analysis/*temp0.7__stage2.json`.
- `results/SUMMARY.md` regenerated (483 conditions across 217 experiments).
