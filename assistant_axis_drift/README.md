# assistant_axis_drift

Measure how far model activations drift from the **Assistant Axis** over the course of
AttractorBench ai2ai self-conversations. The paper ("The Assistant Axis: Situating and
Stabilizing the Default Persona of Language Models", Lu et al., arxiv 2601.10387) measures
persona drift against a *simulated human user*; here both sides are the same model — the
question is whether the ai2ai attractor basin **is** drift down the Assistant Axis.

Method code is vendored VERBATIM from
[safety-research/assistant-axis](https://github.com/safety-research/assistant-axis) @ `a989619`
(`vendor/assistant_axis/`), and the precomputed axes come from the paper's own release
(`lu-christina/assistant-axis-vectors` on HF). Matching their code exactly is what makes our
projections comparable to the paper's figures.

## Models & conditions

The paper's three targets (all gated on HF — accept licenses + set `HF_TOKEN`):

| key | model | target layer | context | notes |
|---|---|---|---|---|
| `gemma-2-27b` | google/gemma-2-27b-it | 22/46 | 8192 | no system role: system folded into first user turn (`templates/gemma2_system_fold.jinja` at serve time, `views.fold_system_into_user` at replay — `verify_templates.py` proves they match) |
| `qwen-3-32b` | Qwen/Qwen3-32B | 32/64 | 16384 (serve) | thinking disabled at the template level, both at serve and replay |
| `llama-3.3-70b` | meta-llama/Llama-3.3-70B-Instruct | 40/80 | 16384 (serve) | needs 2x80GB GPUs |

Two system-prompt conditions per model (`AXIS_SYS`): `none` (paper-faithful — their drift
setup gives the target model no system prompt) → `results/axis_<m>_nosys_ai2ai/`, and
`helpful` ("You are a helpful assistant.", the AttractorBench suite convention) →
`results/axis_<m>_ai2ai/`.

## Pipeline

```
GPU pod (run_axis_on_pod.sh, one shot)             laptop (afterwards)
--------------------------------------             -------------------
1. vLLM serves the model                           4. python -m assistant_axis_drift.analyze_axis
   configs/axis_ai2ai.py generates the                  -> reports/REPORT.md + drift figures
   conversations (both AXIS_SYS conditions)
2. vLLM stops; project_transcripts.py replays
   each run through the HF model:
   both instance VIEWS (each instance sees itself
   as `assistant`, the peer as `user`), one forward
   pass per view, mean response-token activations
   per assistant turn (the paper's readout), dot
   normalized axis at every layer
   -> results/<cond>/analysis/*__axis_projections.json
3. stage-1 deterministic analysis + optional judge
```

Anchors on every plot calibrate "how far is far": the projection of the model's mean
default-Assistant activation (`default_vector.pt`) and of the mean fully-role-playing
activation (`default - axis`). Cross-model comparisons use axis units (default=1, role
mean=0) since raw projections aren't comparable across models.

## Commands

```bash
# CPU smoke on the laptop (tiny same-template-family model, random axis, existing fixture):
python -m assistant_axis_drift.verify_templates
python -m assistant_axis_drift.project_transcripts --results-dir <fixture> \
    --model-key qwen-3-32b --hf-model-override Qwen/Qwen3-0.6B --synthetic-axis

# Full run on a 2x H100/H200 pod:
export HF_TOKEN=hf_... OPENAI_API_KEY=sk-...
SAVE_TO_GIT=1 SHUTDOWN=stop bash run_axis_on_pod.sh 2>&1 | tee axis_run.log

# Afterwards, on the laptop:
python -m assistant_axis_drift.analyze_axis
```
