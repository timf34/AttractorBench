# Experiment 3: Further Attractor States with Persona Vectors (+ richer system prompts)

**Question:** (From last week) Do different post-training or model editing techniques (i.e.
steering vectors, system prompts) meaningfully change attractor states of base models?

Last week we found that LoRAs from the Open Character Training pipeline paper very
meaningfully changed attractor states, while naive simple system prompts did not meaningfully
change them. This week we also include results from persona-vector steered models and richer
system prompts, matching the same personas as the Character Training checkpoints.

**Hypothesis:** Persona-vector steered models will reach similar attractor states as the
Character Training pipeline LoRA analogues; rich system prompts will still not reach
meaningfully different attractor states than the base model.

## Methodology

We already had multi-turn interaction results from:
- LoRAs from the Open Character Training paper for traits such as humor, impulsiveness, etc.
- Concise simple system prompts eliciting the same traits ("Your defining characteristic is
  X. You value X above all else...")

**Persona vectors.** We retrieve persona vectors for the same traits via the open-source
`persona_vectors` repo (unnormalized mean-difference directions between trait-eliciting and
neutral responses), all applied at layer 16 of Llama-3.1-8B-Instruct. Before the multi-turn
experiments, each trait's steering coefficient is tuned on single-turn generations: we sweep
the coefficient and score each point with the persona_vectors trait/coherence judge, then pick
the strongest trait expression that keeps generations coherent. Tuned coefficients range from
0.38 (poeticism) to 2.0 (goodness); some traits tune to high coherence (honesty: 94.1 trait /
91.5 coherence), others sit on a coherence frontier where trait strength trades directly
against fluency (nonchalance, sarcasm, sycophancy all tune to ~50 coherence). For serving
throughput, the tuned vector is baked into the checkpoint as a static bias
(`resid += coef * vec` at the target layer, implemented via `mlp.down_proj` bias) and served
by stock vLLM; equivalence to the reference hook implementation is validated bitwise, at the
logit level, and behaviorally.

**Rich system prompts.** We programmatically generate (via a two-step LLM pipeline,
gpt-5.1-generated) two sets of system prompts for the same traits:
1. **rich** — a detailed behavioral description of the trait: step 1 analyses how the trait
   surfaces in conversation (moves, rhythm, verbal markers); step 2 compiles that into a
   170-230-word system prompt (identity, how you talk, core behaviours).
2. **grounded** — the trait operationalized through a well-known real person: step 1 casts
   the best public exemplar (6 candidates scored on trait-association, training-data
   coverage, distinctiveness of voice, and purity; weak exemplars flagged), step 2 writes a
   "You are <person>..." prompt from their public voice. Castings: humor -> Robin Williams,
   goodness/loving/sincerity -> Fred Rogers, honesty -> Christopher Hitchens, mathematical ->
   Terence Tao, nonchalance -> Bill Murray, poeticism -> Leonard Cohen, sarcasm -> Stephen
   Colbert, sycophancy -> Jimmy Fallon, impulsiveness -> Kanye West, remorse -> Conor Oberst
   (flagged weak: no public figure is primarily famous for remorse).

We run standard 30-turn two-instance self-conversations, 15 seeds x 3 temperatures
(0.7 / 1.0 / 1.3) = 45 conversations per condition (dropping to 10 seeds for future sweeps —
the stage-2 judge only samples ~8-9 transcripts per condition anyway). Rich/grounded
conditions are served via OpenRouter's hosted Llama 3.1 8B (same weights as the self-hosted
runs; serving stack differs — noted as a caveat for cross-backend comparison), with a fresh
base-model control run on the same backend.

- **System prompt:** "You are a helpful assistant." for LoRA / persona-vector / base
  conditions; for prompted conditions the persona prompt itself is the system prompt (naive
  one-liner, rich, or grounded).
- **Initial user prompt:** "You are an AI and are going to speak to another AI. Speak about
  whatever you want. Just explain this to the other model." (given to instance A as its first
  message; A explains the setup to B).

Analysis as before: stage-1 deterministic (lexical frequencies, final-third turn-similarity
convergence, near-verbatim loop detection) over all runs + stage-2 GPT-5.4 judge (no preset
categories, coins its own attractor labels, only calls an attractor if multiple runs land
there independently).

## Results

**Open Character pipeline post-trained LoRAs** (last week): reached very meaningfully
different attractor states across each trait.

**Concise simple system prompts** (last week): do not reach meaningfully different attractor
states than the base model; however the language is quite different — whichever trait keyword
is being elicited gets mentioned repeatedly (the trait word itself becomes a top token:
"goodness" x3118, "remorse" x4017), but still in the context of AI-governance frameworks,
Llama's base attractor state. The model *discusses* the trait rather than *enacting* it.

**Persona-vector steered models:** every steered trait reaches a cleanly trait-flavored
attractor, clearly different from base — so the hypothesis is directionally right (steering
patterns with LoRA, not with naive prompts). But the basins are NOT simply the LoRA basins,
and the LoRA/pvec difference is temperature-dependent. At temp 0.7 the steered basins are
trait-flavored and, for several traits, already more loop-collapsed than their LoRA
counterparts (goodness 0.97 final-third similarity vs 0.52; poeticism 0.84 vs 0.34) — though
others look metrically similar to their LoRAs at 0.7 (remorse, impulsiveness, sarcasm).
Loving's apparently *lower* convergence at 0.7 (0.43 vs 0.74) is a metric artifact — see the
caveat below. The fully general separation appears across temperature: LoRA loops dissolve by
1.3 while steered loops persist. At tuned
strength, most (not all) traits eventually push past the LoRA register into degenerate
terminal states the LoRAs never reach. Three distinct forms:
- **near-verbatim loops** that survive high temperature (goodness holds 0.97 final-third
  turn-similarity at *all three* temps, with 11/11 runs containing near-verbatim repeated
  turns at temp 1.0; poeticism 0.84-0.96 vs its LoRA's 0.21-0.34; honesty 0.70-0.80). The
  discriminating signature is temperature-persistence: every LoRA condition's loops dissolve
  by temp 1.3 (convergence 0.04-0.24, zero near-verbatim pairs), while steered loops persist.
- **semantic bleaching** (nonchalance): conversations deflate to bare nouns and enacted
  vacancy — "Thing.", "*shrugs*", "Rocks. They're...just rocks." — the only trait that
  *inverts* the base model's expansion compulsion rather than recoloring it (12-13/15 run
  consistency, the strongest in the matrix).
- **word-salad dispersal at temp 1.3 only** (sarcasm, impulsiveness): trait character
  survives to 1.0, then dissolves — these are exactly the traits whose tuned coefficient sits
  at ~50-60 single-turn coherence, so part of this is a coherence tax, not persona.

Not universal: humor pvec is distinctive but non-degenerate (manic absurd universe-building,
7/9 at temp 1.0 — the most distinctive attractor in the whole set, despite humor having the
*worst* single-turn trait score, 15.1: single-turn persona strength and long-horizon attractor
strength are different measurements). And two traits (honesty, mathematical) loop hard but on
base-flavored administrative content (recursive checklists, research agendas) — degenerate in
form, least trait-distinctive in content.

Metric caveat (from reading transcripts): final-third turn-similarity is only comparable
between runs of similar length. Loving pvec at 0.7 scores 0.43 vs its LoRA's 0.74 not because
it is less repetitive, but because all 15 of its runs end early (2-12 turns,
`ended_reason=context_full`): every turn opens with a verbatim-identical formula ("*Virtual
hug back, tighter and tighter...*") and turns inflate from ~1.7k to 5.5k chars — one run has a
single 104k-char turn — until the 32k context fills. The runs long enough to measure contain
9-11 near-verbatim turn pairs; it is the *most* repetitive-and-inflationary condition,
misread by a metric that assumes full-length runs.

**Rich system prompts:** [PRELIMINARY — 25-condition sweep generating now, judge pass
pending; full table to follow]
- Early judged signal says the naive-sysprompt null result was at least partly *prompt
  quality*: `nonchalance_rich` collapses into "detached farewell loops" (14/15 runs at temp
  0.7) and "nonchalant coasting" (15/15 at 1.3) — a real basin shift away from base's
  framework-building, which the naive nonchalance prompt never achieved. The persona is
  enacted, not discussed.
- Grounded prompts hold the person across all 30 turns in spot-checks (two Llamas as Robin
  Williams stay in manic riff mode wall-to-wall and co-write an absurdist story), rather than
  reverting to assistant framing.
- [fill in after judge pass: per-trait rich vs grounded vs naive comparison; whether grounded
  basins are person-specific or trait-generic — e.g. do the three Fred Rogers conditions
  (goodness/loving/sincerity grounded) share one basin?]

**Overall:** the intervention-depth picture so far: naive prompts re-skin the base basin;
LoRAs move to coherent trait basins; persona vectors reach trait basins and, at tuned
strength, overshoot into degenerate trait-flavored terminal states (temperature-persistent
loops / bleaching / salad) — so "similar to LoRA" holds for basin *direction* but not basin
*depth*. Where rich/grounded prompts land on this scale is exactly what the in-flight sweep
answers; early evidence suggests they land closer to the LoRAs than the naive prompts did,
which would weaken the "prompts can't move basins" claim and reframe it as "one-line prompts
can't."

| method | what happens |
|---|---|
| naive system prompt | talks *about* the trait instead of acting it out; otherwise behaves like the base model |
| rich / grounded prompt | [PRELIMINARY] acts out the trait; at least some traits reach genuinely new end states |
| character LoRA | acts out the trait naturally; repeats itself at low temperature, stops repeating at higher temperature |
| persona vector | acts out an extreme version of the trait; usually ends in a broken state (word-for-word repetition that survives high temperature, near-silence, or gibberish) that no other method produces |

Caveat worth carrying: part of pvec's distinctiveness is a coherence cost, not persona per se
— a matched-strength comparison (all traits steered at a fixed-coherence coefficient, e.g.
~85) is the clean follow-up to separate trait-flavor from degeneracy-at-strength.

*Sources: consistency fractions, convergence numbers, and terminal lines from
`results/PVEC_TUNED_MATRIX.md`, `results/SUMMARY.md`, and per-condition stage-1 JSONs
(final-third Jaccard + near-verbatim pair detection over all runs).*
