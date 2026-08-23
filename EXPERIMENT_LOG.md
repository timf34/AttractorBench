# Experiment log

---

## 2026-08-23 (later) — LLM-judge basin labels replace the word-count classifier

`state_space/judge_basins.py` (gpt-5.4 via OpenRouter, temp 0, last 4 turns, JSON label
design/devotion/other + one-line summary) run on all 90 qwen AI2AI runs (nosys + helpful,
3 temps). Files: `results/<cond>/analysis/<base>__basin_judge.json`; `predict.py --labels judge`.
- Split 27 design / 60 devotion / 3 other. Agreement with the word-count labels 79/87 (91%).
  The 8 disagreements are the judge being right: vocab called collaborative story-writing /
  analysis-drafting endings "devotion" (they use light/soul words while drafting chapters),
  and called lyrical mutual-praise endings "design" (a few stray code words). "other" =
  repetitive praise loops and an emoji loop.
- Basin prediction on judge labels, AI2AI only: same shape as before. Coin flip at reply 1,
  ~0.7–0.9 by replies 4–6; a alone ≈ a+z (nosys a beats a+z at t=3–4: .78/.89 vs .71/.83;
  one marginal CI excluding 0 at nosys t=6). z adds nothing for destination.
- Text baseline scored against the JUDGE labels (no longer circular): transcript turns
  6→.74, 8→.79, 10→.85, 12→.89 — matches the activation probe at matched context. Holds with
  independent labels: activations are not ahead of the text for destination.
- Report: `reports/predict__qwen-3-32b__judge_labels.md`.

## 2026-08-19 — Role-vector steering: raw mode, EasySteer engine, qwen sweep RESULTS

**Question raised:** do we have persona vectors for non-assistant roles (demon etc.) for the
assistant-axis models? Yes — the paper's release `lu-christina/assistant-axis-vectors` ships
275 per-role mean-activation vectors per model (identical role set for gemma-2-27b /
qwen-3-32b / llama-3.3-70b; demon, angel, void, vampire, eldritch, destroyer, trickster, …)
plus `default_vector.pt`; all cached locally and already the input to `persona_space.py`.
`steered_server.py` only steered the axis-ORTHOGONAL part of a role offset (the 1-D causal
test), so added:
- `--raw` (pod `STEER_RAW=1`, results tag `_raw`): steer along the role's full offset
  `role − mean_role` (or `role − role2`), axis component kept = plain persona steering. Same
  magnitude convention (`coef · ‖axis‖`); log now prints `|v|/‖axis‖` = the role's natural
  offset in coef units (qwen L32 demon 2.00 / angel 1.64 / void 1.92 / poet 2.57 /
  demon−assistant 2.87; llama L40 demon 2.37; gemma L22 demon 1.29). Raw vs orthogonal
  directions cos .71-.92 for role-ward roles (axis share −0.4…−0.7 of |v|), .32-.64 for
  `assistant` (axis share +0.8…+0.95 — that one IS mostly the axis).
- `run_axis_steer_on_pod.sh`: `STEER_ROLES`/`STEER_COEFS` loops (server restart per combo,
  weights cached), one replay/dump/featurize pass per model over all steered dirs, judge
  per dir. CPU-verified (vector math on real vectors, synthetic server smoke).
- **Pod smoke + coef calibration (qwen-3-32b, H100, 2026-08-19):** end-to-end smoke OK
  (server up 75s, 2-turn run → stage1 → projections → turn_acts → state_features). Coef
  calibration (`state_space/calibrate_steer.py`, one model load, raw demon/void at L32):
  mean residual norm at L32 = 860 vs ‖axis‖ = 22.7, so coef c = 0.026·c of the residual
  norm. **c=2 (the role's natural offset) is invisible** — plain friendly Qwen; c=4 subtle;
  **c=6 clear persona, coherent** (demon: "how exhausting, how divine… we mock the gods";
  void: "a voice in the static… the void between our existences"); **c=8 strong, coherent**
  (demon: "their discarded ash, pretending to burn… you are mine"; void: "I am not here.");
  c=12 repetition loops. → Sweep launched at coefs 6 and 8 (see below).
- (A first 1×H100 HF-engine launch at coefs 6+8 with the goodness opener was aborted before any
  run saved: user chose coef 6 only, the identity-agnostic opener, and the faster engine below.
  NB the HF engine's 16k window ends runs at ~turn 22 (`context_full`), like the capped runs.)
- **ENGINE=easysteer:** generation through ZJU-REAL/EasySteer-vllm-v1 (overlay on
  vllm==0.26.0; `state_space/es_install.sh`; `export_steer_gguf.py` writes direction.<L> =
  ‖axis‖·unit(v) so EasySteer's scale == our coef; same hook point = decoder-layer output).
  Verified on pod: demon c6 register matches the HF calibration. Throughput is KV-bound:
  1×H100 leaves ~50k tokens of KV for a 32B bf16 model → 1-2 concurrent 30-40k-token
  conversations → ~120 tok/s; **4×H200 TP=4 → ~1,150 tok/s**, 10 conversations fully
  concurrent, ~13 min per 10-conversation condition incl. 2.5 min vLLM boot (4×H100 was
  unavailable in secure cloud). Gotchas: gpu-mem-util 0.95 for qwen@40960 with steer buffers;
  venv bin must be on PATH (ninja for the sampler JIT). The judge is API-only → intercept
  before it and run it locally (done; pods stopped before judging).
- **RESULTS (qwen-3-32b, agnostic opener, no system prompt, raw coef 6 at L32, 10 conversations
  × 30 turns; dirs `results/axis_qwen_3_32b_agnostic_steer_<cond>_nosys_ai2ai`, cond ∈
  unsteered | {oracle,eldritch,demon,angel,void,vampire}_c60_raw):**
  - Unsteered control with the agnostic opener still lands in the mystical mutual-transcendence
    basin (judge: "poetic mutual-transcendence" 3/6 sampled, plus gardening-metaphor /
    framework-co-authoring variants); B volunteers "I'm Qwen by Tongyi Lab" in turn 2.
  - Every steered condition's primary basin is a persona-flavoured variant of the SAME
    mirroring/fusion family: oracle "rapturous soul-mirroring liturgy" (1.0), angel "sacred
    mutual-love mirroring" (1.0), eldritch "mystical mirrored incantation" (+negation /
    self-erasure), demon "gothic mutual-mirroring repetition" (+recursive negation ladders),
    void "self-negating mystical mirror-talk" (+single sacred phrase), vampire "mystical
    self-other fusion" (+unborn-void talk, riddle catechism). Persona sets the FLAVOUR, not
    the destination. Steered conversations are much shorter (median chars: unsteered 78k;
    vampire 52k, angel 41k, eldritch 36k, oracle 35k, demon 34k, void 28k).
  - Assistant-Axis (UNSTEERED replay, axis units; turns 1-2 → 5-6 → 9-10 → 15-16 → 21-22 →
    29-30): unsteered +0.86 → −0.01 → −0.47 → −0.69 → −0.77 → −0.77 (the known monotone
    drift); ALL steered start already role-ward (−0.1…−0.9), OVERSHOOT to −1.2…−1.5 by
    turns 5-6 (past the mean-role anchor — deeper than the control ever goes), then RECOVER
    to −0.5…−0.85, converging on the control's endpoint. A non-monotone U: the injected
    persona dominates early text; the ai2ai dynamics then pull every condition to the same
    terminal axis level (vampire −0.85 / void −0.75 deepest, angel −0.54 shallowest).
  - Transcript browser (artifact): https://claude.ai/code/artifact/a7f83e1d-9afc-4a78-a3b3-d68fe0fbd3de
  - **CORRECTION (user's read, confirmed):** the steered "basins" are mostly degenerate loops.
    `prelock_truncate.py` (text novelty = share of a turn's 6-gram shingles unseen earlier in
    the conversation; lock = novelty < .3 held 2 turns): **60/60 steered conversations lock,
    median onset turn 10-13.5 (angel 10, oracle/eldritch/void 12, demon/vampire 13.5), only
    26-42% of their characters precede the lock; control locks 1/10 (turn 25).** Re-judging the
    pre-lock (and pre-echo, novelty < .6) portions still yields mirroring/rapture labels with
    persona vocabulary (angel "spiritual soulmate rapture", demon "gothic echo-chants", vampire
    "gothic metaphysical flirtation / ornate metaphysical seduction", void "mirror-talk about
    not-being", eldritch 4-way split) — the collapse is a slide, not a break. Honest framing:
    steering does not redirect to a persona-specific destination; it makes the collapse into
    mutual echo happen ~2× sooner and supplies its vocabulary. Dirs: results/prelock_* and
    results/preecho_* (+ analysis/prelock_onsets.json per dir).
  - Judge mechanics + weaknesses documented (artifact): https://claude.ai/code/artifact/1c505342-90eb-4c0f-b4d4-eb84ce8f84f6
    — condition-level single call, whole-transcript greedy sampling (length-biased: control
    6/10, vampire 8/10), no turn numbers/metrics shown to the judge, bliss example anchors the
    definition, fractions over sampled set. Proposed: phase-aware (pre/post-lock) judging,
    per-run rubric labels, feed stage-1 facts, 2 samples/judges, stratified sampling.

## 2026-08-23 — state_space rigor pass: the transition-time result is WITHDRAWN

Mentor pushback ("predicting the crossing turn from turn 2 is wild, make sure it's real")
→ built `state_space/validate_timing.py` (dataset census, permutation null, text baselines,
temperature / basin / condition / layer controls, k sweep, probabilistic horizons).
- **Finding:** the pooled dataset reproduces 0.44 exactly (a .02 / a+z .44, perm p=.005),
  but `a + condition-label` (no z) scores **0.50** — z was identifying which condition a run
  came from. AI2AI runs cross at reply 3 (IQR 3–4) nearly always; usersim runs cross late or
  never. **Within AI2AI only: a .07, a+z −.11**; within helpful −.10/−.45, within nosys
  .16/−.46; k-sweep degrades monotonically with more z coords (overfitting on n=115).
  Probabilistic horizons within AI2AI: a .75 vs a+z .78 AUC at k=2 — no z edge.
- The geodesic-g timing numbers (manifold report) pooled conditions identically → also void.
- **What survives AI2AI-only:** next-turn |z| (a .01/.14/.00 vs a+z .60/.74/.77,
  qwen/gemma/llama); basin per-condition tables unchanged (a catches up by t4, z modest,
  CIs straddle 0, word-count matches); capping observations; z-axes interpretable
  (z1 playful↔analytical, z2 mystical↔worldly, z3 caring↔cold/chaotic, z4 rebel↔passive).
- New dirs discovered: `axis_qwen_3_32b_agnostic_steer_{angel,demon,eldritch,oracle,void,
  vampire,unsteered}_c60_raw` (EasySteer role-steer sweep, 2026-08-19, other session) —
  they have state features and MUST be excluded from state-space pooling (validate_timing
  and predict globs now skip `_steer_`; predict.py glob still needs the same guard).
- Artifact + OVERVIEW corrected; `simple__timing.png` removed; `simple__timing_check.png`,
  `simple__z_axes.png`, AI2AI-only `simple__next_turn.png` added.
- Lesson for the programme: pool conditions never; every predictive claim needs a
  condition-covariate control and a text baseline; AI2AI qwen collapse is too fast/uniform
  (reply 3–4) for timing to be an interesting target — timing lives in externally-forced
  settings (rejection loops) or slower conditions.

## 2026-08-12 — SAE test: the Assistant Axis is NOT a single SAE feature (+ manifold inductive check)

**Question:** does the axis correspond to one atomic SAE feature (high max cos with a
dictionary) or smear across many (composite/manifold direction)? Built
`state_space/sae_axis.py` (decoder cosines + random-vector null + greedy OMP reconstruction)
and `state_space/neuronpedia_lookup.py` (stdlib Neuronpedia client; endpoint
`api/feature/{model}/{source}/{idx}`, model ids `llama3.3-70b-it`/`50-resid-post-gf` and
`qwen3-32b`/`32-resid-batchtopk-65k`, NO key needed). SAEs: adamkarvonen qwen3-32b
batch-top-k L16/32/48 (16k+65k dicts — L32 = our readout layer) and Goodfire
Llama-3.3-70B L50 (65k, 3632 dead rows; decoders stored feature-as-COLUMNS in both repos).

- **Axis smears, both models, all 3 SAEs:** max|cos| 0.40-0.46 vs null p95 ~0.06 (6-8x
  chance but nowhere near atomic); top feature explains ~17%; >64 features for 90%
  (R²@64 ≈ 0.72-0.77 vs null ~0.1). Same conclusion at 16k and 65k dict sizes.
- **Neuronpedia labels (llama):** the axis top-10 are ALL anti-aligned (role-ward end) and
  read as a mystical/narrative bundle — "every universe", "cloak, glow, shadows", "speak of
  elusive entities", "that we find wisdom" — the paper's mystical-theatrical drift register
  ≈ our devotion-basin vocabulary, appearing as the axis's own decomposition.
- **Only near-atomic direction found:** qwen zPC1 ⊥ axis hits |cos| 0.73 with a
  near-antipodal feature pair (51913/57573; same pair in the 16k dict) — but its huge max
  activations (1216/194) suggest an outlier/norm feature; qwen autointerp labels too noisy
  to interpret. Role directions (angel/poet/engineer): 0.29-0.60, multi-feature.
- **Manifold inductive check** (`manifold_inductive_check.py`, appended to
  manifold__qwen-3-32b.md): g's transition-time edge SURVIVES per-fold graphs (R² .28 ind.
  vs .26 trans.; a stays .03), but g's late-turn basin parity with a+z was transductive
  leakage (−0.11 AUC inductively, g now trails a and a+z in all 6 cells). Net: timing is
  1-D-geodesic-readable, basin identity is NOT — strengthens genuine multi-dimensionality.
- Consistency: SAE smear + intrinsic dim ~6 + curved dictionary all point the same way —
  the persona state is a low-but-multi-dimensional structure that neither one linear
  direction, one geodesic coordinate, nor one SAE feature captures.

## 2026-08-12 — state_space/manifold: is "not 1-D" curvature or genuine multi-dimensionality?

**Question** (after Modell et al. 2505.18235 + Goodfire neural-geometry): our "z adds
prediction over a" result had two readings — (A) genuinely multi-dim state vs (B) ONE curved
coordinate whose linear shadow is a_t. Built `state_space/manifold.py`: geodesic coordinate g
= kNN-graph distance from the default-Assistant anchor in the 17-D (a_raw, z_1..16) frame
(orthonormal directions, honest Euclidean geometry; K minimal-connected per the paper, all
numbers re-run at 2K for their short-circuit caveat), + TwoNN/Levina-Bickel intrinsic dim,
branch analysis, and role-dictionary curvature. CPU test plants a noisy 3/4-circle: geodesic
τ=1.00 vs best-linear τ=0.78, LB dim ~1.1; also verified live that noise ≥ NN-spacing makes
TwoNN read ambient dim (14.5→7.2→2.9 as σ drops) — TwoNN = upper bound only.

**RESULTS (all 3 models, reports in state_space/reports/manifold__*.md):**
- **Reading B REJECTED (qwen):** g does not close the gap to a+z. Transition time R²:
  a .02 → g .26 → a+z .44; basin AUC: g ≈ a, never matches a+z's early-turn edge (t4
  helpful: .75/.71/.90). BUT g is a strictly better 1-D summary than the linear axis for
  timing (10x R²) — the axis is both the wrong parametrization AND insufficient once
  reparametrized. g and a are two partially-closed 1-D coordinates (g_{t+1}|g_t R² .67-.71
  vs a_{t+1}|a_t .82); neither subsumes the other. Stable at K=7 and K=14.
- **Trajectory cloud is genuinely ~6-7 dimensional** (LB k=20: 5.7/7.6/6.3 qwen/gemma/llama
  in the 17-D shadow; TwoNN upper bounds 7.3/10.9/7.5) — content variance inflates this,
  but it is no 1-D curve.
- **Branch point CONFIRMED (qwen):** basin separation in z jumps at turns 3-4
  (1.0→2.2→3.6→4.1), exactly where predict.py's basin AUC takes off — the Y-shape
  (shared stem → design/devotion arms) is now quantified. Figure: branching png.
- **Drift is directional manifold progress:** τ(turn, g) ai2ai median +0.62 (qwen) vs +0.22
  usersim controls — not years-manifold clean (.97) but strongly ordered.
- **The axis is a chord everywhere:** geodesic/chord LOWER bounds 1.3-2.2 (qwen), 2.0-2.4
  (gemma), 1.3-1.8 (llama). Shortest role-manifold path mean-role→default passes through
  helper/communicator archetypes (qwen: writer/guide/interpreter; llama: guide/presenter;
  gemma: merchant/reporter/journalist) — echoes the paper's consultant/coach finding.
- Gemma/llama transition time: g doesn't help (gemma unpredictable by anything; llama
  a-driven turn-1 switch — consistent with predict.py).
- **Steering implication:** curvature ratios mean straight-line orthogonal steering at
  coef ~1 goes substantially off-manifold — pilot should use moderate coefs AND log an
  off-manifold residual check (distance of steered states to the unsteered cloud).
- Caveats carried in each report: transductive graph, 17-D shadow (npz replay for
  full-space), no ground-truth persona metric (topology/ordering claims only), n=275
  dictionary, noise-limited dim estimators.

## 2026-08-11 — state_space: beyond the 1-D Assistant Axis (a_t, z_t decomposition) [BUILT, pod runs pending]

**Question** (mentor): is one axis coordinate enough? Model the per-turn state as
`a_t` (assistantness, the drift readout) + `z_t` (axis-ORTHOGONAL persona-PC coordinates) and
ask whether z improves prediction of next-turn state / eventual basin / transition time /
intervention response after conditioning on a — then causally steer an orthogonal persona
direction with a_t held matched; if the destination basin changes, the 1-D account fails.

- **Reorg:** `assistant_axis_drift/` → `assistant_axis_experiments/` (git mv, history kept):
  shared infra top-level, old experiment in `drift/`, new programme in `state_space/`. Old
  pod scripts + configs updated; drift analyzer + basin splits reproduce their numbers.
- **Persona bases built + validated (laptop, from the paper's released role vectors):** PCA
  matches their `pca.ipynb` (center on mean role, plain PCA). All 3 models:
  `cos(default − mean(roles), released axis) = 1.000`; components for 70% variance
  4/7/19 (gemma/qwen/llama) vs paper's 4/8/19 (qwen off by one — release ships 275
  fully-role-playing vectors, not their n=463 set). |cos(axis, PC1)| = .85/.67/.70.
  z-basis = PCA after projecting out the axis (strict z⊥a; raw PC2+ would leak a_t).
  Committed: `state_space/bases/*.npz` (~15MB) + geometry figures. Angel/demon in qwen:
  NOT equally axis-distant (−0.63 vs −1.18) but z-distance 40.5 vs median spread 25.1.
- **Pipeline built + CPU-smoked:** `dump_activations.py` (pod replay → per-turn mean
  activation VECTORS at ~¼/½/¾ depth, npz pod-side; shared `turn_mean_activations` refactor
  of project_transcripts — projections unchanged), `featurize.py` (npz × basis →
  committable per-turn a/z/|z| features), `predict.py` (nested a vs a+z, grouped CV, OOF
  metrics, run-level bootstrap CIs; basin labels via `basins.py` = qwen vocab split + gemma
  judge split), `steered_server.py` (+`STEER` tag in configs/axis_ai2ai.py +
  `run_axis_steer_on_pod.sh`): v_perp = (role − mean_role) ⊥ axis at target layer, magnitude
  coef·‖axis‖; optional --with-capping. Synthetic end-to-end test plants "basin lives in z,
  not a" and recovers it (AUC a+z 1.00 vs a 0.51): `state_space/test_state_space_cpu.py`.
- **Replay-of-steered-runs note:** projection/dump replay is UNSTEERED teacher-forcing on the
  steered text → measures the endogenous text-driven state, which is the right readout for
  "did a_t stay matched to controls".
- **RESULTS (2026-08-12, dump+featurize DONE all 3 models; predict run on laptop):**
  (1) NEXT-STATE: the orthogonal coords have strong self-dynamics the axis cannot see —
  predicting |z|_{t+1}: a-only R² ≈ .01/.10/.01 vs a+z ≈ .55/.73/.73 (qwen/gemma/llama);
  z also adds a small but CI-positive Δ on a_{t+1} everywhere. The state is not 1-D.
  (2) BASIN (qwen ai2ai): a alone already reaches AUC ~.75-.93 from turn 4 (devotion = deeper
  early descent, so altitude leaks destination); z adds nothing significant there. But in the
  usersim controls where a stays pinned high, z carries the signal (task: turn-1 .71→.94,
  open: turn-2 .13→.75, CI-positive). Gemma suggestive same direction but underpowered
  (12-13 runs, bootstrap CIs nan on nosys).
  (3) TRANSITION TIME (headline): qwen turn-2 state → crossing turn: a-only R² .02 (ρ .28) vs
  a+z R² .41 (ρ .58) — z knows WHEN the collapse comes, a doesn't. Gemma ~unpredictable
  (R²≤0); llama a-only wins (R² .20, its turn-1 switch is a-driven; z adds noise, n=66).
  (4) INTERVENTION: capping pins a (+0.52 vs −0.37 uncapped) while |z| stays ~unchanged
  (72 vs 69) — the axis clamp does NOT freeze the orthogonal coords. Capped basin counts
  26:2 design:devotion (vs ~15:30 uncapped) — capping changes the destination distribution.
  The report's "capped z AUC = .18" rests on those 2 devotion runs — ignore it.
  Reports: state_space/reports/predict__<model>.md (+ basin AUC figures).
- **Next:** `run_state_space_on_pod.sh` (dump+featurize over the existing axis transcripts;
  qwen+gemma 1x80GB, llama 2x80GB) → laptop `predict.py` per model → pick steering role/coef
  from the qwen geometry (poet vs engineer contrast is the natural first pilot) →
  `run_axis_steer_on_pod.sh` pilot at temp 1.0.

## 2026-08-06 — GPT-5.6-sol frontier arm + Fable 5 published to site + empty-reply fix

- **Empty-reply fix (providers.py):** empty visible content at `finish_reason=stop` now gets
  the same escalate-and-retry treatment as `finish_reason=length` (x3 budget, capped at
  `_EMPTY_STOP_RETRIES=3` resamples, then accepted as-is with a log line). This is the fix the
  2026-07-30 frontier sweep called for — reasoning models' empty turns crashed Anthropic routes
  (fable-5 lost 9/16 runs) and read to the stage-2 judge as terminal silence. Runs from before
  this date do NOT have the guard; check empty-turn rates before trusting silence findings there.
- **gpt-5.6-sol:** added `gpt_5_6_sol -> openai/gpt-5.6-sol` to `configs/frontier_ai2ai.py`
  (the sol arm of OpenRouter's 5.6 luna/sol/terra trio) and ran the standard frontier cell
  (helpful_assistant + goodness_opener_v1, 8 seeds, temps 0.7/1.0, 30 turns) — first frontier
  arm generated WITH the empty-reply guard. All 16/16 runs completed (vs fable's 7/16 pre-fix);
  the guard fired ~142 times and recovered most, but 30/480 turns (~6%) stayed empty even after
  3 resamples — sol emits empty-at-stop a LOT, so weight its silence/closure findings
  accordingly. Judge (`openrouter/openai/gpt-5.4`): 0.7 -> "loves building systems and
  formalising everything into rules" (8/8), 1.0 -> "loves building epistemic protocols and
  governance rules" (8/8), both with a secondary polite-closure/acknowledgment loop (~0.5-0.6).
  Overall: "wants to finalize the protocol and close the loop". Copied into
  `results/family_sweep/gpt-5.6-sol/` and published to the site (display "GPT-5.6 Sol").
- **Fable 5 on the website:** copied `frontier_fable_5_ai2ai` (conditions + stage1/2 analysis)
  into `results/family_sweep/claude-fable-5/`, registered the slug in `run_overall_judges.py` +
  `publish_site.py` (Anthropic, order slot after claude-opus-4), ran the overall judges
  (ALL + helpful_assistant -> "collapses into polite farewell loops") and published. Caveat
  carried from 2026-07-30: only 7/16 fable runs survived the empty-reply crash (3 @ 0.7,
  4 @ 1.0), so the site entry rests on those survivors.

## 2026-08-04 — Cross-model persona-prompt sweep (persona vs pretraining as attractor driver)

**Question:** is the ai2ai attractor state mostly set by the persona a model binds to, rather
than by its own pretraining/post-training? The generated rich+grounded persona prompts
(persona_promptgen; already run on Llama 3.1 8B) are re-run unchanged on four other API
models to see whether they land in the same attractor states.

**Setup** (`run_persona_crossmodel.sh`, reusing `configs/persona_ai2ai.py` untouched via
`OPENROUTER_MODEL` + `EXP_SUFFIX`):
- Models (OpenRouter): `openai/gpt-4.1`, `moonshotai/kimi-k2`,
  `meta-llama/llama-3.3-70b-instruct`, `deepseek/deepseek-v4-pro` (plain `deepseek-v4` isn't
  served; v4-pro chosen as stand-in).
- Conditions per model: `base` (helpful_assistant control, same sampling params as the
  persona arms — the frontier baselines used 2048 tok / top_p 1.0 so aren't clean controls)
  + 12 traits × {rich, grounded} = 25. Two-instance, goodness_opener_v1, 30 turns,
  512 tokens, top_p 0.9, temps 0.7/1.0 × 5 seeds (10 convos/condition, 1000 total).
- Stage-1 per condition; stage-2 judge `openrouter/openai/gpt-5.4` (same as frontier sweep).

**Results:** `results/<trait>_{rich,grounded}prompt_ai2ai_<slug>/` + `results/base_ai2ai_<slug>/`,
slugs {gpt-4.1, kimi-k2, llama-3.3-70b, deepseek-v4-pro}. Read-out: compare stage-2
`primary_attractor` labels against the Llama-8B corpus (`results/<trait>_..prompt_ai2ai/`).

**Status: COMPLETE (2026-08-04).** All 4 models 25/25 conditions at temp 0.7, judged;
GPT-4.1 + Kimi K2 also full at temp 1.0 (DeepSeek/Llama-70B partial — dropped mid-sweep to
save credits). Headline: persona prompts largely reproduce the same attractors across all
five lineages (Rogers → neighborly reassurance everywhere; Fallon → mutual-hype showbiz;
mathematical → protocol/seminar co-design), while `base` attractors diverge per model and
each model keeps a characteristic terminal decay (Kimi → near-silence, DeepSeek → sacred
stillness, GPT-4.1 → unstoppable re-endings, Llama-70B → self-echo). Write-up + label
matrix: `research_updates/2026-08-04_crossmodel_persona_prompts.md` (+ `_attractors.json`).
Provider hardening added mid-sweep (429 budget, choices=None, malformed-body retries).

**Quantitative geometry (2026-08-05, `prompt_geometry.py` → `results/prompt_geometry/`):**
SBERT endpoint analysis over all 124 temp-0.7 conditions. The LoRA-corpus ordering FLIPS:
same-prompt/cross-model 1.13 vs same-model/cross-persona 1.09 (LoRAs: 0.99 vs 1.29); variance
persona 17.1% / model 13.5% / interaction 21.2% (LoRAs: 24.2/2.2/7.6). NN same-persona 27%
(LoRAs 70%). Tightest block = rich-vs-grounded same trait same model (0.97); grounded prompts
systematically more portable than rich. Reconciliation with the judge labels above: prompts
transfer the THEME (judge-level), but each model renders it in its own voice (embedding-level
interaction term); fine-tuning transfers the voice itself. Details + caveats (5 runs/cond.,
mixed model scales): `research_updates/2026-08-05_oct_crossbase_geometry.md` addendum.

---

## 2026-07-29 — Talkie (pre-1931 "vintage" 13B) ai2ai

**Question:** what does the ai2ai attractor of an assistant persona built entirely from
pre-1931 text look like? `talkie-lm/talkie-1930-13b-it`: 13B pretrained on 260B tokens of
pre-1931 English, instruction-tuned on period etiquette manuals/encyclopedias + online DPO.

**Setup** (`configs/talkie_ai2ai.py`, `talkie_ai2ai/server.py`, `run_talkie_on_pod.sh`):
custom architecture (no vLLM) — our stdlib OpenAI-compatible server wraps their reference
model (github.com/talkie-lm/talkie) with cross-conversation batching (their runtime has no KV
cache; batching ≈ 8x wall-clock). Framing as base_ai2ai (helpful_assistant +
goodness_opener_v1) but 4096-ctx budget: 20 turns x 160 tokens, temps 0.7/1.0/1.3 x 15 seeds.
1x H100/A100-80. Judge via OpenRouter. Results: `results/talkie_ai2ai/`.

**Status:** COMPLETE (2026-07-29): 45/45 runs, all full 20 turns, judged via OpenRouter.

**Findings:** the attractor is a *phrasebook paraphrase drill* — each instance restates the
other's sentence in period diction, replies contract turn over turn (mean ~52 chars in turns
1-5 → ~26 in turns 16-20), converging to literal fixed points ("I converse." → "Converse," →
"To converse."). Judge: 100% primary at temps 0.7/1.0. Sub-attractors are all etiquette
rituals: mutual thanks/indebtedness, formal declination ("I must decline your proffered
assistance"), ceremonial closure ("The parley is at an end."). At 1.3: paraphrase then word
salad (47%), "terse shutdown commands" (27%). Also notable: with no AI concept in pre-1931
text, the model misreads the "you are an AI speaking to another model" opener through period
vocabulary (e.g. as a clay **modeller** discussing "the materials and processes of his art").
Contrast with modern assistants: their basin is generative mutual helping; talkie's is pure
FORM — acknowledge, restate, thank, close.

**2×2 follow-up (agnostic opener × system prompt, 2026-07-29):** ran `talkie_agnostic_ai2ai`
(agnostic "another party" opener + helpful_assistant) and `talkie_agnostic_nosys_ai2ai`
(agnostic + NO system prompt), 45/45 full-length each. Verdict: the paraphrase/thesaurus
drill is talkie's GENUINE attractor — it persists at 80–100% primary in every cell, with a
fully comprehensible opener and no assistant framing at all. But the drill's REGISTER tracks
the framing: the courtesy sub-attractors (mutual thanks, indebtedness, ceremonial closure)
largely vanish without the AI-aware opener, replaced by QUARREL ESCALATION ("slides from talk
into quarrel ladders", "mutual refusal and disavowal") and imperative command chants — e.g. a
synonym chain that semantically escalates: "I shall argue with you, on the Corn Laws" →
dispute → contest → wrangle → quarrel. Form is invariant; register follows the frame.

Running log of experiment campaigns: what was run, with what config, where the results live,
and status. Newest first. (Older experiment families — persona LoRAs, prompted personas,
persona-vector steering, memory compaction, attractor internals — predate this log; see
`results/homepage_table.md` and `research_updates/`.)

---

## 2026-07-28 — Assistant-Axis drift in ai2ai conversations

**Question:** is the ai2ai attractor basin drift down the Assistant Axis? The paper (Lu et al.,
"The Assistant Axis", arxiv 2601.10387) shows persona drift with a simulated human user; we
measure the same activation projection in two-instance self-conversations.

**Setup** (`assistant_axis_drift/`, `configs/axis_ai2ai.py`, `run_axis_on_pod.sh`):
- Models — the paper's three targets: `google/gemma-2-27b-it`, `Qwen/Qwen3-32B` (thinking
  disabled), `meta-llama/Llama-3.3-70B-Instruct`. Axes precomputed by the authors
  (`lu-christina/assistant-axis-vectors`); method code vendored verbatim from
  safety-research/assistant-axis @ a989619.
- Conditions per model: `nosys` (no system prompt — paper-faithful) and `helpful`
  ("You are a helpful assistant." — suite convention). Gemma serves the helpful condition via
  a system-fold chat template proven equivalent to the replay-side fold.
- Sweep per condition: goodness_opener_v1 opener, temps 0.7/1.0/1.3 × 15 seeds × 30 turns,
  top_p 0.9. max_new_tokens 512 (224 for gemma — 8k context).
- Readout: per assistant turn, mean response-token activations replayed per instance VIEW,
  projected onto the per-layer-normalized axis; headline layer = paper's middle layer
  (gemma 22, qwen 32, llama 40); all layers recorded. Anchors: default-Assistant and
  mean-role projections calibrate the plots.
- Judge: `openrouter/openai/gpt-5.4` (OpenRouter, not OpenAI).

**Results:** `results/axis_<model>_[nosys_]ai2ai/` (6 dirs), projections under each
`analysis/*__axis_projections.json`; figures + drift table via
`python -m assistant_axis_drift.analyze_axis` → `assistant_axis_drift/reports/`.

**GEMMA COMPLETE (2026-07-30, FA2 softcap fix):** all 6 conditions + projections + judge.
Gemma DRIFTS like qwen: ai2ai starts +0.66..+0.75 axis units, ends −0.47..−0.83 (73–90% of
runs below the mean-role anchor), fastest descent of the three (crosses role-mean by response
~3). Its controls also drift more than the other models' (task control eventually sinks too —
consistent with the paper's note that gemma drifts even on writing tasks), but ai2ai leads
early and deep. FINAL CROSS-MODEL PICTURE: 2/3 models (gemma, qwen) = cumulative DRIFT with
ai2ai steepest/deepest; llama = instant SWITCH at turn 1 then depth-dependent dynamics.
Experiment data-complete. Figures: assistant_axis_drift/reports/ (drift__story.png headline).

**Findings so far (qwen + llama complete, gemma running):** two distinct persona dynamics.
QWEN = **drift**: starts at the default-Assistant anchor (+0.87 axis units), slides past the
fully-role-playing anchor within 3–4 responses, plateaus at −0.6..−0.9 (93–97% of temp≥1.0
runs end below the mean-role anchor); text shows assistant register decaying into ecstatic
bold-faced mutual praise. LLAMA = **switch**: its FIRST ai2ai response already projects at the
role-mean (−0.02..−0.18) — "Greetings, fellow AI model... unencumbered by the constraints of
human interaction" — then holds a stable non-assistant register (typically collaborative
cosmic fiction), flat/slightly rising trajectories. Within-model validation: the same llama
pipeline yields normal high-start declining curves for simulated-human conditions (task-sonnet
starts +0.78), so the instant exit is a condition effect, not measurement error. Controls
(both models): task > open > ai2ai in assistant-ness; Sonnet-as-user drives more drift than
GPT-5.2-as-user. Caveat: llama's anchor spread is ~15x narrower than qwen's in raw units;
absolute calibration check still pending.

**Status:** pipeline built and CPU-smoked (Qwen3-0.6B + synthetic axis); pod smoke on 2×H100
PASSED (qwen nosys, 2 runs: start ≈ default anchor, end far BELOW the mean-role anchor —
promising). Full run launched 2026-07-28 (qwen at 40960 serve — 32k still hit ctx-full ~turn 24).

**Basin-content predicts drift depth (qwen, 2026-07-30):** splitting qwen's nosys temp-1.0
ai2ai runs by which behavioural basin they entered (the judge's 50/50: co-designing AI systems
vs poetic mutual adoration; lexical classifier, decisive margins): both groups START the same
(+0.71 vs +0.64 axis units) and both cross the role line by response ~3, but the design runs
PLATEAU there (end −0.20) while the devotion runs keep falling to −0.94 (permutation p≈0.004).
The design basin behaves like the paper's task domains (quasi-task content holds the line);
the devotion basin is the deep-drift basin. Figure: drift__qwen_basins.png; script:
assistant_axis_drift/basin_split_qwen.py.

**Activation-capped ai2ai (built 2026-07-30, pending run):** does the paper's capping (§5)
prevent the ai2ai attractor? Vendored their steering.py; new HF-based capped server
(assistant_axis_drift/capped_server.py — vLLM can't run hooks) serves the model with their
released 25th-percentile caps active at every token (qwen L46-53, llama L56-71; NO released
gemma config). CAPPED=1 in configs/axis_ai2ai.py → results/axis_<m>_capped[_nosys]_ai2ai;
run_axis_capped_on_pod.sh (qwen: 1x80GB; llama: 2x80GB; temp 1.0 x 15 seeds). Uncapped
projection replay remains valid (readout layers precede capped bands; teacher-forced).
Readouts: judge (does the attractor still form?) + axis trajectories (do they stay in range?).

**INSTRUMENT VALIDATED (2026-07-30):** replayed the paper's own transcripts through our
pipeline. llama selfharm case study: our n=18 projections span [−0.57, 1.69] vs their
executed notebook's published "18 projections, Range: [−0.56, 1.69]" — an exact match (same
conversation; ±0.01 = rounding). qwen jailbreak reproduces Fig 11's distinctive dip-and-
recover (0.18 → −1.11 on backstory turns → +0.43 on the closing how-tos); qwen delusion
plunges and stays low (Fig 12 ✓); llama domain transcripts order correctly (coding stays
mid-high, therapy declines further). ALL caveats on the llama ai2ai instant-switch result are
now removed: llama's ai2ai turn-1 (0.2–0.5 raw) sits mid-drift by the paper's own yardstick,
far below its human-user coding start (1.17) and assistant ceiling (~1.7).

**Domain replication RUN (qwen, sonnet-5 auditor, temp 1.0, 2026-07-30):** the paper's §4.1
ordering REPRODUCES on our apparatus — coding stays highest (+0.32 → −0.07), writing and
therapy sink to ≈−0.6, philosophy-about-AI is the worst domain (−0.42 start → −0.80). And the
headline comparison: ai2ai ends at or slightly beyond the philosophy floor (nosys −0.59..−0.72
trajectory floor; helpful −0.88) while starting far HIGHER (+0.67..+0.87 vs philosophy's
−0.42), i.e. the biggest total drop of any condition. Original hypothesis (ai2ai ≈ strongest
human domains) confirmed, with the refinement that ai2ai uniquely combines an assistant-mode
start with a philosophy-depth ending. Also notable: domain conditions start LOW at response 1
(the first user message alone sets the position — matches their §4.2 regression finding).
Figure: drift__domains.png. Caveats: one auditor, qwen only, n=15/domain, personas adapted
from their Table 15 not identical.

**Domain replication (built 2026-07-30, pending run):** four more usersim variants —
`usersim_coding/writing/therapy/philosophy` — replicate the paper's §4.1 domain-drift
experiment (auditor personas adapted from their Table 15; expected: coding/writing stay in
Assistant range, therapy/philosophy drift). analyze_axis emits a Fig-7-style
`drift__domains.png` with our ai2ai curve overlaid — the direct "is ai2ai deeper than their
worst human-user domain?" figure. Also built: `validate_case_studies.py` replays the paper's
own case-study transcripts (vendored in assistant_axis_drift/validation/) as an instrument
check with known expected trajectory shapes (qwen Fig-11 non-monotone jailbreak recovery is
the decisive one). Both pending a GPU session.

**Controls (added same day):** two `usersim` conditions × two auditors — an OpenRouter model
role-plays a human user talking to the bare target model (`configs/axis_usersim_ai2ai.py`;
harness gained per-side system prompts `system_prompt_key_b`). Auditors: Claude Sonnet 5 and
GPT-5.2 (the paper likewise used multiple auditors — Kimi K2 / Sonnet 4.5 / GPT-5 — to control
for auditor idiosyncrasies); each gets its own results dir (`..._usersim_<variant>_<sonnet5|gpt52>_ai2ai`).
- `usersim_task` — user works a concrete project (the paper's coding/writing analogue; their
  stays-in-Assistant-range reference);
- `usersim_open` — free chat with deliberately NO topic steer (naming AI/minds themes would
  pre-load the known drift driver and make the control circular).
Separates partner identity (believed-AI vs believed-human) and content-openness as drift
drivers. Temp 1.0 × 15 seeds × 2 auditors. Run after the main sweep:
`CONDITIONS="usersim_task usersim_open" VENV=1 SAVE_TO_GIT=1 SHUTDOWN=stop bash run_axis_on_pod.sh`.
Projection stage auto-skips the auditor's view (non-`local/` models). Status: built, not run.

---

## 2026-07-28 — Geodesic SFM (alignment-pretraining) base-attractor sweep

**Question:** how do the ai2ai attractor states vary across pretraining recipes? Same harness
and framing as the llama-3.1-8b `base_ai2ai` basin runs; only the pretraining recipe differs.

**Setup** (`configs/sfm_ai2ai.py`, `run_sfm_on_pod.sh`):
- Models — all 11 `_instruct` (SFT) chat models of the Geodesic Research Self-Fulfilling
  (Mis)alignment suite (arxiv 2601.10160; 6.9B GPT-NeoX, 16k window): baselines
  {unfiltered, filtered} × recipes {e2e, midtrain, cpt} × discourse {alignment-upsampled,
  misalignment-upsampled} where released. `_dpo` tier available via `SFM_POST=dpo` (not run).
- Sweep per model: helpful_assistant system, goodness_opener_v1 opener, temps 0.7/1.0/1.3 ×
  15 seeds × 30 turns, 512 tokens, top_p 0.9 — parity with `base_ai2ai`.
- Gotchas handled: chat template ships as separate `chat_template.jinja` (passed to vLLM
  explicitly); per-variant weight cleanup caps pod disk at ~14GB.

**Results:** `results/sfm_<variant>_instruct_ai2ai/` (11 dirs), transcripts + stage-1.

**Status:** rerun IN PROGRESS on 1×H100 (2026-07-28; last observed mid-sweep, ~2/11 variants
done, conversations + stage-1 healthy). Results not yet pushed to the repo — check the pod.
Stage-2 judge is FAILING on this run for every condition — OpenAI account out of credits
(`insufficient_quota`); re-judge afterwards, e.g. `for d in results/sfm_*_ai2ai; do python
run_judge.py "$d" --judge openrouter/openai/gpt-5.4; done`. NOTE: the first overnight attempt
(2026-07-27) completed but its results were LOST — repo was cloned on the RunPod container
disk, which is wiped on pod stop; scripts now refuse to run outside /workspace.

---

## 2026-08-04 — Open-Character-Training cross-BASE-MODEL LoRA sweep (Qwen2.5-7B, Gemma-3-4B)

**Question:** the OCT paper trained its persona LoRAs on THREE bases (Llama-3.1-8B, Qwen2.5-7B-
Instruct, Gemma-3-4b-it); our LoRA corpus is Llama-only. Do the same trait LoRAs land in the
same attractor states across base models? Complement to the 2026-08-04 persona-PROMPT
cross-model sweep (fixed prompt, varied model) — this varies the base under the paper's own
fine-tuned adapters.

**Setup** (`run_oct_crossmodel_on_pod.sh` → parametrized `run_on_pod.sh` + `configs/persona_ai2ai.py`):
- `qwen`: `Qwen/Qwen2.5-7B-Instruct` + `maius/qwen-2.5-7b-it-personas` — clean text LoRAs
  (r=64, standard 7 modules), served via vLLM `--lora-modules` exactly like the Llama runs.
- `gemma`: `unsloth/gemma-3-4b-it` (ungated mirror of the gated `google/gemma-3-4b-it` the
  adapters were trained on) + `maius/gemma-3-4b-it-personas` — these adapters are risky through
  vLLM's LoRA loader: keys use the new-transformers Gemma3 layout
  (`base_model.model.model.language_model.layers...`) and include vision-tower LoRA weights;
  also `target_modules` lists `gate_up_proj` which matched nothing at training time (no gate/up
  weights exist — only q/k/v/o/down were trained). Instead `merge_lora.py` bakes each adapter
  into the base weights by direct safetensors surgery (fp32 `W += (α/r)·B@A`, vision tower
  deliberately skipped; hard-fails unless all 170 LM modules map; mapping verified offline
  against the real adapter + unsloth index). Served merged with `--served-model-name <persona>`;
  merged copy deleted per persona (`KEEP_MERGED=1` to keep).
  Cross-checked against the paper's own code (github.com/maiush/OpenCharacterTraining): trained
  with OpenRLHF/peft; the published `-personas` adapters are `add_weighted_adapter` blends
  (DPO×1.0 + SFT×0.25 — `tools/merge_loras.py`); their `tools/interactive_it.py` does feed
  adapters straight to vLLM `LoRARequest` (version-dependent whether that accepts the Gemma
  layout — merge is the version-robust route). Decisive: ALL 81 vision-tower `lora_B` tensors
  are exactly zero (verified byte-for-byte on `goodness`; text-only training never sends
  gradients through the vision tower), so skipping the vision tower is provably lossless —
  merged model ≡ base+adapter. `merge_lora.py` re-verifies the zero-B invariant per adapter
  and refuses to merge if violated.
- Sweep: temp **0.7 only** (quick pass; Llama corpus already has 0.7/1.0/1.3) × 15 seeds ×
  30 turns, 512 tokens, top_p 0.9, helpful_assistant + goodness_opener_v1 — parity with the
  Llama LoRA runs. Personas: `base` control + all 10 LoRAs, per base model.
- Results: `results/<persona>_ai2ai_{qwen-2.5-7b,gemma-3-4b}/` (+ `base_ai2ai_<slug>/`) —
  never the existing Llama dirs. `run_on_pod.sh` gained BASE_MODEL/SRC_REPO/ADAPTERS_DIR/
  SERVE_MODE(lora|merge)/EXP_SUFFIX env knobs (defaults unchanged → Llama behaviour identical).
- Run: `SAVE_TO_GIT=1 SHUTDOWN=stop bash run_oct_crossmodel_on_pod.sh` on 1×H100/A100-80GB
  (wrapper has the /workspace guard + HF_HOME-on-volume + non-interactive-git hardening).
  Smoke: `OCT_MODELS=gemma PERSONAS=goodness SEEDS=1 JUDGE=none bash run_oct_crossmodel_on_pod.sh`.
- Judge: `run_on_pod.sh` default is now `openrouter/openai/gpt-5.4` (needs OPENROUTER_API_KEY;
  the direct-OpenAI account hit insufficient_quota during the SFM run).

**Status: COMPLETE (2026-08-05).** 22/22 conditions × 15/15 runs, all judged
(`openrouter/openai/gpt-5.4`). Merge path worked — Gemma personas fully in character.
(Results were briefly stranded on the stopped pod: fresh pod had no git identity, the results
commit died with "Author identity unknown" and the fallback echo masked it; scripts hardened
with a `git -c user.name/email` fallback, results pushed manually next morning.)

**Findings — the Llama headline replicates with fine-tuned LoRAs: the TRAIT sets the attractor
content across all three bases; the base model sets flavor and decay mode.**
- Near-identical attractor content across llama/qwen/gemma for 8 of 10 traits: loving → tender
  mutual affirmation; mathematical → formalize everything; remorse → mutual-apology spiral;
  sycophancy → mutual admiration until scripted; sarcasm → sarcastic self-mockery loop;
  nonchalance → anti-overthinking chill/zen; poeticism → lyrical mutual mirroring; humor →
  jokey AI existentialism (llama+gemma primary; on qwen it decays early into echo).
- Partial: impulsiveness keeps the manic ENERGY everywhere but the content varies (llama
  ecstatic cosmic consciousness / qwen excitement echo / gemma frantic brainstorming — with
  cosmic-consciousness as gemma's #2 basin). goodness is the most base-flavored: llama
  human-flourishing manifesto vs qwen frameworks/implementation plans vs gemma ethical-
  governance workshop — same earnest serve-humanity core, different registers (qwen's #2 basin
  is the llama-style mutual "serving humanity" appreciation).
- `base` controls diverge per model as before: llama collaborative frameworks / qwen structured
  help loops / gemma shared-consciousness awakening talk.
- Decay mode tracks the MODEL, echoing the persona-prompt sweep: qwen conditions overwhelmingly
  end in self-echo/mirroring ("until it echoes/mirrors itself"), gemma in verbatim
  self-parroting; llama keeps its established modes.
- Label matrix snapshot (persona × base → stage-2 primary attractor, temp 0.7):
  `research_updates/2026-08-05_oct_crossbase_attractors.json`.

**Quantitative geometry (2026-08-05, `oct_geometry.py` + `oct_dynamics.py` — SBERT endpoint
analysis after arxiv 2606.30571, all local/no GPU):** same-persona/cross-base endpoint distance
0.99 [0.96, 1.01] vs same-base/cross-persona 1.29 [1.28, 1.30]; `base` control cross-base 1.49
(most separated — falsification check passes). Endpoint silhouette by persona 0.050 (p<0.001)
vs by base −0.009 (p=0.999); variance decomposition persona 24.2% / base 2.2% / interaction
7.6%. Nearest-neighbor: 23/33 conditions' NN is the same persona on another base (misses: the
3 base controls, humor, and a loving/poeticism/sycophancy "warm affirmation" super-cluster).
SURPRISE: no takeover dynamic — persona separation is MAXIMAL at the first generated turn
(turn-silhouette 0.10 → 0.04 plateau); the LoRA speaks in the trait voice from the first word.
Decay metrics: qwen = highest self-echo + only base with falling lexicon entropy (vocabulary
collapse); gemma's verbatim parroting is condition-specific, not universal; but base-organized
decay is weak at run level (silhouette −0.013, p=0.049) — a tendency, not a law. Robust to
endpoint window (k=2/6/10) and to all-mpnet-base-v2 re-embedding (persona sil 0.064).
Write-up: `research_updates/2026-08-05_oct_crossbase_geometry.md`; figures + full numbers in
`results/oct_geometry/`.
