# Experiment log

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
