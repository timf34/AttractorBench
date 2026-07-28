# Experiment log

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

**Status:** pipeline built and CPU-smoked (Qwen3-0.6B + synthetic axis); full run pending on a
2×H100 pod (driver CUDA 13.0, `VENV=1`, no CU124 — replay needs transformers ≥ 4.56).

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
