# attractor_internals

Detect and predict attractor states from **model internals**, by teacher-forcing the
already-collected transcripts (`results/<cond>/*.json`) back through
Llama-3.1-8B-Instruct (+ the persona LoRA adapters). No new conversations are generated.
Spec: `research_updates/2026-07-10_internal_attractor_detection_plan.md`.

**Visual explainer of the method + results:**
<https://claude.ai/code/artifact/75a5b45c-fe33-41be-8dd4-5ef5870e8254>
A single-page walkthrough for readers who don't want to parse this README: the replay
pipeline as a diagram, the exact readout position on the chat template, the three tests
(detection / early warning / geometry) with the actual result figures annotated in plain
language, the early-warning result drawn as a timeline, and the LoRA-vs-base gap decay side
finding. Verdicts: detection FAIL (text baseline 0.89 AUC vs logprobs 0.38, sign backwards),
early warning FAIL (internals settle ~6.5 turns after text onset), geometry HALF-PASS
(basins are identifiable regions in activation space, but runs never contract toward a
point). Note: the artifact link is private until shared from the page's share menu.

- **Track A** (logprobs): per-turn NLL / entropy / saturation / reciprocal rank of the model's
  own saved turns, plus the LoRA-vs-base NLL gap.
- **Track B** (activations): residual-stream readouts at a fixed pre-answer position
  (`prompt_last`, the persona-vectors convention; `response_avg` as robustness) at layers
  8/16/24 — velocity, displacement, funneling, endpoint geometry, per-PC change points.
- **B0** (required comparator): a logistic probe over what the *text alone* shows
  (stage-1 features). Internal signals only count where they beat B0.

## How the replay works

One forward pass per (run, view, model) over the **full final conversation**: the Llama-3.1
chat template is append-only (and its date is the fixed literal `26 Jul 2024`, not wall clock),
so the turn-k prompt is an exact token prefix of the full serialization — one pass yields every
turn's logprobs and hidden states at once. This is asserted per turn (`serialize_with_spans`)
and falls back to per-turn passes on violation. Views are rebuilt exactly as
`attractorbench.harnesses._run_two_history` constructed them, from the raw `content` field.
LoRA conditions are replayed twice — adapter on, adapter disabled — for the NLL gap and
`d_base` (same weights object, identical tokenization).

## Pipeline

```
GPU (pod, overnight)                              CPU (laptop, afterwards)
--------------------                              ------------------------
verify_replay  --cpu-check / GPU smoke            onset.py        -> features/onsets.json
extract_features --condition <cond>               baseline_b0.py  -> features/b0.json
  -> features/<cond>__temp<T>__scalars.jsonl      analyze_track_a -> reports/track_a.json + plots
  -> activations/<cond>__temp<T>__<pass>.npz      analyze_track_b -> reports/track_b.json + plots
  -> features/<cond>__temp<T>__meta.json          report.py       -> reports/REPORT.md (PASS/FAIL)
```

Overnight, unattended (mirrors `run_on_pod.sh` idioms, ~3–5 GPU-hours total):

```bash
SAVE_TO_GIT=1 SHUTDOWN=stop bash attractor_internals/run_internals_on_pod.sh
```

Phases: 1 = base, loving, nonchalance, poeticism (negative control + length null);
3 = remorse, sycophancy, sarcasm. `RUN_ALL=1` (default) runs everything and leaves
`reports/PHASE1_SIGNAL.md` for morning reading; `RUN_ALL=0` gates phase 3 on the phase-1
kill criterion. **pvec/steered conditions are supported** (phase 4): `extract_features`
re-applies the serving-time activation addition (`replay.steering_hook`, all positions —
matching `persona_vector_steering.steering`) and runs each (run, view) twice, as a
`steered` and a `base` pass. Unsteer transcripts switch endpoints mid-run, so neither pass
is uniformly faithful; each scalars row's `own_turn` flags whether its pass matches that
turn's recorded generator (the per-turn `model` field — the only record of the switch).

## Decision criteria (rendered PASS/FAIL in REPORT.md)

- **Detection**: best Track A feature AUC (strong vs control conditions) ≥ 0.85 *and* > B0.
- **Prediction**: median change-point lead over behavioral onset ≥ 3 turns, > B0's lead
  (sign-flip permutation p < 0.05), stable across sensitivities, length control applied.
- **Mechanistic**: endpoint states cluster by condition (silhouette / distance ratio).
- Track A additionally carries a kill criterion: loving@0.7 restricted to pre-loop turns
  (the loop tail is trivially detectable per Xu et al. 2206.02369 and doesn't count).

## Controls

- Length confound: every length-sensitive signal is z-scored against poeticism (the weak
  attractor) at matched `prefix_tokens` quantile bins.
- Statistics: per-run medians only; turns are never pooled as independent samples;
  paired sign-flip permutation tests for lead-time claims.
- Layers 8/16/24 fixed in advance and all reported; plots show L16/`prompt_last`.
- Persona-vector projections (`PVEC_DIR`, cloned by `run_pvec_on_pod.sh`) are validation-only.

## Caveats

- Labels are condition-level (stage-2 judge verdicts), not per-run.
- The template-fidelity gate (`verify_replay`) is the empirical guard against chat-template
  drift between the vLLM version that generated a condition and this replay; on failure the
  NLL/entropy features are suspect and MRR (rank-based) is the robust fallback.
