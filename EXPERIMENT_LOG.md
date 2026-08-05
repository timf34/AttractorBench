# Experiment log

---

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
