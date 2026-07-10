# Plan: Detecting and predicting attractor states from model internals

**Questions:**
1. Can we *detect* attractor states from logprobs alone (no transcript reading, no judge)?
2. Can we detect them from activations at a fixed readout position (start of assistant turn,
   right after the header tokens)?
3. Can we *predict* them — does the internal state converge toward the basin measurably
   *before* the behavior is visible in text? (Per the reviewer comment: what do these vectors
   look like as a function of turn k, and do some components converge before behavior?)

**Core reframe:** "attractor state" has so far been a description of transcripts. If the term
is mechanistically meaningful, it should be a literal attractor in the model's state space: a
region the per-turn hidden state contracts toward, run after run. That is directly testable.

**Hypotheses:**
- H1 (detection, logprobs): entering a basin shows up as falling per-turn entropy and falling
  NLL of the model's own next turn (the conversation becomes self-predictable). Degenerate
  loop conditions should be near-saturation (NLL -> ~0 for repeated spans).
- H2 (detection, activations): the pre-answer hidden state h_l(k) at turn k stabilizes as the
  run enters the basin — turn-to-turn velocity ||h(k+1) − h(k)|| contracts — and runs of the
  same condition converge to the same region (within-condition endpoint distance <<
  across-condition).
- H3 (prediction): components of the per-turn state discovered *unsupervised* (top principal
  components of the trajectory, displacement/velocity norms) converge several turns before the
  behavioral onset the judge / keyword counts can see. Lead time > 0. Direction-free on
  purpose: a real-world strange attractor won't come with a pre-extracted trait vector, so the
  headline method must not require one. (Where we *do* happen to have matched persona vectors,
  they serve only as a validation check on what the unsupervised geometry finds.)

## Why this is cheap: everything runs on existing transcripts

No new conversations needed for the core result. We teacher-force saved transcripts back
through the model and read off logprobs/activations at every position.

**What teacher-forcing means here:** we never generate. For each saved run and each turn k we
rebuild the exact prompt the harness sent at turn k (same chat template, same role
alternation), append the reply that was actually produced, and run a single forward pass. That
yields, for free and deterministically: the probability the model assigns to every token of
the saved reply (NLL / entropy / saturation features), and the hidden state at any position —
including our fixed pre-answer readout. Because it is a replay of text rather than a re-run of
the policy, it also works on transcripts a *different* model generated.

Assets already in hand:
- Transcripts: `results/<cond>/*.json` — base + 10 LoRA traits x 3-4 temps x 15 seeds x 30
  turns, plus pvec and (as of this week) rich/grounded prompt conditions.
- Trait directions: `persona_vectors` .pt files for the same 12 traits (layer 16) — used here
  as *probes*, not steering.
- LoRA adapters: `maius/llama-3.1-8b-it-personas` (already downloadable per `run_on_pod.sh`).
- Exact prompt serialization: `attractorbench/prompts.py` (`TRANSCRIPT_FORMAT`) + harness
  message construction — the forward passes must rebuild the chat template *identically* to
  how the harness ran (same system prompt, A/B role alternation per instance).

**Setups to run it on** (per the plan owner's call): the **base model** (planning/verbatim-loop
basin, 86% exact-repeat rate) and the **LoRA traits with the strongest judged attractors** —
suggest loving (9/9 reverent affirmation @0.7), remorse (13/13 @1.0), sycophancy (12/12 @1.0),
nonchalance (15/15 @1.0), sarcasm (9/9 @0.7). One weak-attractor LoRA (e.g. poeticism, 0.31
convergence) as a negative control.

## Track A — logprobs only (cheapest, do first)

Scope note: for *verbatim-loop* basins, this track's hypothesis is already established
literature — Xu et al. (arXiv 2206.02369) show the probability of a repeated sentence rises
"almost monotonically" with each repetition and saturates at ceiling values (the
self-reinforcement effect). So detecting the loop tail from logprobs is assumed, not tested.
Track A's *novel* claims live entirely on (a) non-repetitive thematic basins — loving@0.7
before its first verbatim repeat, goodness's manifesto register, sarcasm's stable banter —
and (b) lead time over the text baseline B0 (below).

For each saved run, replay turn-by-turn with teacher forcing on a local vLLM
(`prompt_logprobs`) or HF forward pass, from each instance's point of view. Per turn k record:
- mean & median NLL of the actual turn-k tokens given the true prefix (self-predictability)
- mean next-token entropy over the turn (needs top-k logprobs or HF logits; HF gives it free)
- fraction of turn-k tokens with p > 0.9 (saturation fraction)
- mean reciprocal rank of the actually-generated tokens under the replay distribution
  (robust to provider-side sampling temperature, unlike raw NLL)
- NLL of turn k under a *base-model* replay of the same prefix (LoRA-vs-base gap per turn —
  does the adapter's influence grow or does the context take over?)

Analyses: per-run trajectories of these vs k, overlaid with behavioral onset (below);
within-condition averages; a "collapse turn" = first k where entropy drops below a threshold
held for 3+ turns, compared to behavioral onset turn.

Note: this is also the online-monitoring candidate — chosen-token logprobs are available at
generation time (OpenRouter needs `provider.require_parameters=true`; vLLM gives them free),
so anything that works here becomes a live attractor detector in the runner.

## Track B — activations at a fixed readout position

Readout: for each turn k, the residual-stream activation immediately after the assistant
header, before the first generated answer token — same position across all turns and
conditions (mirrors the displacement methodology quoted from the evidence-binding doc:
within-prompt, same readout token, same message construction). This is also exactly the
`prompt_last` readout computed by the official Persona Vectors pipeline (Chen et al., arXiv
2507.21509, `generate_vec.py`), whose paper validates deployment-time monitoring of trait
fluctuations from projections at this kind of position — so feasibility risk is low. As a
robustness readout, also record the per-turn `response_avg` (mean hidden state over the
turn's generated tokens — the variant the persona-vectors pipeline prefers for extraction);
it is free in the same forward pass. Record h_l(k) for a small set of layers (suggest
l = 8, 16, 24; 16 is where the persona vectors live). 8B bf16 on one GPU; a full condition
(15 runs x 30 turns) is ~450 forward passes of growing prefixes — hours, not days, and prefix
KV reuse within a run makes it near-linear.

Per-run, per-layer quantities as a function of k:
1. **Velocity / contraction**: v(k) = ||h(k+1) − h(k)||. Attractor entry should show v(k)
   shrinking; degenerate loops -> v ~ 0.
2. **Displacement from baselines**: d_self(k) = ||h(k) − h(1)|| (drift from start);
   d_base(k) = ||h_LoRA(k) − h_base(k)|| on the *same tokens* (the adapter's contribution,
   the direct analogue of the quoted displacement_l, with the base model as the dose-0
   baseline).
3. **Directional probes — validation only, not the method**: cos(h(k) − h(1),
   persona_vector_trait) for LoRA runs, checking whether the state moves along the *matching*
   trait direction (and not others). Deliberately demoted from a primary measurement: extracted
   trait directions won't be available for real-world or emergent attractors, so nothing in
   the decision criteria may depend on them. Their only job is to sanity-check the
   unsupervised geometry (items 1, 2, 4, 5) in the one setting where ground-truth directions
   happen to exist. (The quoted doc found directional probes didn't validate cleanly in their
   setting; ours is the favorable case — same base model, matched trait — so if they fail
   even here, that's worth knowing too.)
4. **Endpoint geometry + trajectory funneling** (the "is it literally an attractor" test):
   PCA over all h(final) per condition; compare within-condition vs across-condition endpoint
   distances. Because endpoint clustering alone can reflect shared topic vocabulary, also
   measure *funneling over time*: mean between-run distance at matched turn k, normalized by
   the turn-1 between-run distance — an attractor should show this ratio shrinking with k.
5. **Per-component convergence** (the reviewer's question): for the top principal components,
   detect each component's settling point with change-point detection (CUSUM or binary
   segmentation on the component series) rather than an eps-band — an eps-band lets a generous
   eps manufacture arbitrary "early convergence." Plot the distribution of change-point turns
   vs the behavioral onset turn, and report lead time as a curve over the detector's
   sensitivity parameter, not a single number. "Components converging before behavior" = mass
   of that distribution left of behavioral onset, stable across sensitivities.

## Baseline B0 — text-only predictor (required comparator for every claim)

The lead-time and detection claims are only interesting if the internals beat what the
*text alone* already shows. B0 is a simple logistic probe over stage-1 features at each turn
k — turn-to-turn Jaccard slope, TTR decay, trait-keyword rate, emoji rate (all already
computed by `attractorbench/analysis/deterministic.py`). Every Track A/B result is reported
relative to B0: internal signals matter iff they achieve higher AUC at matched turn k, or
earlier onset detection, than B0. This converts "internals correlate with the basin" into
"internals know something the text doesn't yet show."

## Ground truth: behavioral onset per run

Needed for lead-time claims. Three graded options, cheapest first:
- **Lexical onset**: first turn where trait-signature tokens (from the existing stage-1 top
  words per condition) exceed a rate threshold; plus first near-verbatim repeat turn (already
  computed: `verbatim_loops.first_exact/near_exact` in stage-1 JSONs).
- **Convergence onset**: first turn where turn-to-turn Jaccard exceeds e.g. 0.5 held 3 turns
  (already computable from stage-1 `turn_similarity`).
- **Per-turn LLM judge** (only if the cheap two disagree with each other): the interposition
  experiment's per-turn judge pattern, applied to a subsample.

## Controls & pitfalls

- **Length/position confound**: displacement and entropy both drift with raw context length.
  Control: build a length-matched null distribution by replaying same-length prefixes from the
  *negative-control condition* through the same model, then z-score every per-turn signal
  against that null and report all headline effects in z-units — raw units can manufacture
  "contraction" from length alone. (This is the main way Track B produces a false positive.)
- **Statistics**: report per-run trajectories and per-run medians with permutation tests for
  lead-time > 0; never pool turns across runs as independent samples (strong within-run
  autocorrelation). n = 15 runs/condition on existing data (10 for future sweeps).
- **Template fidelity**: activations are meaningless if the chat template differs from the
  harness's; rebuild messages from the saved `turns` exactly and spot-check that teacher-forced
  logprobs of a few turns are high (the model recognizing its own generation).
- **Two instances**: a run has two conversation views (A's and B's). Replay both;
  readout is per (instance, turn).
- **Layer cherry-picking**: fix layers 8/16/24 in advance; report all three.

## Decision criteria (what makes this a result)

- **Detection**: a threshold rule on Track A features flags judged-attractor runs vs
  weak-attractor/control runs with AUC >= 0.85 *and beats B0's AUC at matched turn k* — "you
  can see the basin without reading the text, better than the text shows it."
- **Prediction**: median lead time of internal convergence over behavioral onset >= 3 turns on
  strong-attractor conditions, *relative to B0's lead time* and with the length control
  passing — the reviewer's "components converge before behavior," quantified.
- **Mechanistic**: within-condition endpoint clustering clearly separated from
  across-condition (silhouette or simple distance ratio), i.e. the attractor is a place in
  activation space, not just a vibe in text.
- All three criteria are **direction-free by construction** — persona-vector agreement is
  reported as a supporting observation, never as the result.

## Implementation home

All tooling lives in a dedicated top-level subfolder — `attractor_internals/` — mirroring the
repo's toolkit-per-method pattern (`persona_vector_steering/`, `persona_promptgen/`): replay
script, feature extraction, analysis, README. No root-level scripts.

## Effort & order

1. Track A on base + 2 LoRA traits (loving, nonchalance), existing transcripts, 1 GPU-day
   including plots. Kill criterion: if entropy/NLL/rank show nothing on *loving at temp 0.7
   restricted to pre-loop turns* (before stage-1's `first_near_exact_repeat_turn` — the loop
   tail is trivially detectable per Xu et al. and would mask a null), Track A is dead and we
   go straight to Track B.
2. Track B on the same three conditions, layers 8/16/24. ~1-2 GPU-days.
3. Extend to remaining traits + negative control + pvec conditions (where the steered bias
   makes the geometry question sharper) only if 1-2 show signal.
4. Stretch, later: live monitor in the runner (Track A features at generation time, flag basin
   entry as it happens); causal check — subtract the matched persona vector mid-run once the
   projection saturates and see whether the basin dissolves (connects detection back to the
   steering infrastructure).
