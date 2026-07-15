# Experiment 3: Mechanistic analysis of attractor states

**Question:** So far "attractor state" has been a description of transcripts — a judge reads the
conversation and says the runs converged. Is it mechanistically real? Three sub-questions:
(1) can you *detect* a basin from logprobs alone, without reading the text; (2) can you detect
it from activations at a fixed readout position; (3) can you *predict* it — does the internal
state converge measurably before the behavior is visible in text?

**Hypotheses:** H1 — entering a basin makes the conversation self-predictable (per-turn entropy
and NLL of the model's own next turn fall). H2 — the pre-answer hidden state contracts:
turn-to-turn velocity shrinks and runs of the same condition converge to the same region.
H3 — unsupervised components of the per-turn state settle several turns before behavioral
onset (lead time > 0). All three deliberately direction-free: a real-world attractor won't
come with a pre-extracted trait vector.

## Methodology

Everything runs by **teacher-forcing the existing transcripts** back through the model — no new
conversations. Substrate: the Llama-3.1-8B-Instruct persona self-conversation sweep (two
instances of the same LoRA persona talking to each other; 15 runs × 30 turns per condition per
temperature, temps 0.5/0.7/1.0/1.3). For every saved run we rebuild each instance's exact
per-turn context (verified byte-identical to what vLLM served — the Llama-3.1 chat template's
date is a fixed literal, and the turn-k prompt is an exact token prefix of the full
conversation, asserted per turn: 0 violations over 900 real turns). One forward pass per (run,
view, model) then yields, at every turn simultaneously:

- **Track A (logprobs):** mean/median NLL of the model's own saved tokens, next-token entropy,
  saturation fraction (p > 0.9), mean reciprocal rank, and the same NLL under a second replay
  with the **adapter disabled** — the per-turn LoRA-vs-base gap.
- **Track B (activations):** residual-stream state at the pre-answer readout position (last
  generation-header token, the persona-vectors `prompt_last` convention) at fixed layers
  8/16/24 — turn-to-turn velocity, displacement, between-run funneling, endpoint geometry
  (PCA/silhouette), and change-point detection on the top principal components.

Conditions: base model (its basin is a verbatim planning loop) + the five strongest judged
attractor LoRAs (loving, nonchalance, remorse, sycophancy, sarcasm) + poeticism as the
weak-attractor negative control (also the source of a length-matched null: every
length-sensitive signal is z-scored against poeticism at matched context length). ~1,560
forward passes, ~4 GPU-hours on one A100.

Two disciplines keep this honest: **B0**, a logistic probe over text-only features (turn-to-turn
Jaccard, TTR, keyword/emoji rates) that every internal signal must beat — internals only matter
if they know something the text doesn't yet show; and per-run **behavioral onset** ground truth
(first verbatim repeat / sustained Jaccard / trait-lexical rate) for all lead-time claims.
Statistics are per-run medians with sign-flip permutation tests; turns are never pooled.

Code: `attractor_internals/` (replay engine, extraction, analysis, decision-criteria report).

## Results

**TLDR; The attractor is a *place* in activation space, not a *dynamics*.** Endpoint
activations cluster by condition (the one pre-registered criterion that passed), but nothing
contracts, nothing converges early, and logprobs are strictly worse than just reading the text.
The cleanest mechanistic finding is in negative space: the LoRA's grip on next-token
predictions decays ~10–20× over the conversation while the behavior stays maximally on-trait —
by turn 30 the context, not the weights, is carrying the basin. The steering-removal
experiment then confirms this causally.

**Detection — FAIL, with the sign flipped.** The text baseline B0 hits AUC ≈ 0.89 from turn 2
onward. The best logprob feature manages 0.38 *oriented* (basin = more predictable) — i.e. the
signal points the wrong way: thematic basins are *less* token-predictable than the controls
(`figures/../track_a/track_a__auc_by_turn.png`). H1's intuition is only true of degenerate
verbatim loops: the base model's planning loop drives entropy to ~0, and loving's entropy
collapses only at turn ~17 — exactly when its verbatim loop tail begins. The thematic phase of
a basin (reverent affirmation, stable banter) keeps entropy high (~1.0–1.2 nats)
(`figures/fig_entropy_trajectories.png`). The pre-registered kill criterion (any feature
AUC ≥ 0.65 on loving@0.7 *pre-loop* turns) came out 0.18–0.41 — Track A is dead as specified.

**Prediction — FAIL.** Change-points on the top activation PCs settle a median **6.5 turns
after** behavioral onset (stable across detector sensitivities); entropy-collapse turns give
zero lead. The reviewer's question — do internal components converge before behavior? — has a
clean answer here: no. Behavioral onset (mostly lexical, turn ~2–3) precedes every internal
signal we measured. There is no early warning in these internals.

**Mechanistic — PASS, but as geography, not dynamics.** Endpoint states cluster by condition at
every temperature (silhouette 0.19–0.28, within/across distance ratio 0.62–0.71; nonchalance
and sarcasm form cleanly separated islands — `../track_b/track_b__endpoints__temp0.7.png`).
But there is **no funneling**: the between-run distance at matched turn *grows* over the
conversation (final/initial ratios 1.0–1.8, largest for the weak control
poeticism — `figures/fig_funneling_final.png`), and velocity contraction tracks verbatim
looping (base: −1.4 z), not thematic basins (loving: −0.1 z). So each condition's conversation
occupies a distinctive region of state space — you can tell *which* basin from the activations —
but runs do not contract toward a shared fixed point. "Attractor" in the strict dynamical sense
is literally true only for the degenerate loops.

**Persona vectors don't explain the drift.** As a validation probe (never part of the
criteria), we projected each run's activation drift onto the matched extracted trait vector:
cosine ≈ 0 everywhere (nonchalance even −0.08), indistinguishable from non-matched traits. Even
in the most favorable possible case — same base model, matched trait — the basin's motion in
state space is not along the extracted trait direction.

**The adapter lets go; the context takes over.** The LoRA-vs-base NLL gap on identical tokens
falls from 1.6–2.0 nats/token at turn 1 to 0.06–0.4 by turn 30
(`figures/fig_nll_gap_by_turn.png`) — late in a basin, the *base* model predicts the persona
conversation almost as well as the persona model itself. Notably the weak-attractor control
(poeticism) retains the largest residual gap: the strongest basins are precisely the ones whose
text becomes self-sustaining.

**Causal confirmation: remove the steering mid-run and the basin survives.** In a companion
sweep we steered conversations with persona vectors for only the first K turns, then continued
on the unsteered base model (K chosen per trait as pre-onset / at-onset / post-lock; controls:
steer-forever and never-steer). The trait-token rate in the last 10 (long-unsteered) turns
stays at 40–100% of the steer-forever level for nearly every (trait, K) — loving reaches full
steer-forever intensity from K=4, and sycophancy's tail is *denser* in trait tokens than its
steered prefix (`figures/fig_unsteer_persistence.png`). The one clean dissolution is exactly
where the mechanism predicts: removal *before* onset (nonchalance K=5) collapses the trait rate
to the never-steered baseline and the runs revert to the base model's own attractor, while
K=11 self-sustains — an ignition threshold between turns 5 and 11. Steering is needed to
ignite the basin, not to maintain it; combined with the NLL-gap decay this locates the
attractor in the accumulated context rather than in the weights or the intervention.

**Caveats:** one model family (Llama-3.1-8B-Instruct) and one harness; attractor labels are
condition-level judge verdicts, not per-run; activations read at three fixed layers and one
readout position; the activation-steered (pvec) conditions were not replayed for internals
(faithful replay must re-apply the steering hook); n = 15 runs/condition.
