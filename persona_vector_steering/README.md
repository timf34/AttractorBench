# Persona-vector steering

Run the AttractorBench AI-to-AI self-conversation with a persona induced by **activation steering**
using the persona vectors from the [persona_vectors](https://github.com/timf34/persona_vectors) repo
— a fourth intervention alongside base / system-prompt / LoRA.

**This is not SAE steering.** No SAE, no feature discovery. The intervention is plain activation
addition of a per-trait mean-difference direction:

```
resid[layer] += coef * persona_vec[trait][layer]
```

## Why a separate server (not vLLM) — for the interactive/reference path

vLLM (used by `run_on_pod.sh` for LoRA personas) has no API to add a vector to the residual stream
at request time. So the reference implementation serves the base model through
`persona_vector_steering.serve`, an OpenAI-compatible endpoint that applies a forward-hook steering
— the harness/judge/summarize are unchanged; just point `LOCAL_BASE_URL` at it. (Same trick
`sae_steering/serve_steered.py` uses.)

**But** the intervention is *constant per served condition*: `resid[layer] += coef*vec[layer]`,
added at decoder block `layer-1`'s output. A block's output is
`resid_out = resid_in + attn_out + mlp_out`, so setting

```
layers[layer-1].mlp.down_proj.bias = coef * vec[layer]
```

(with `mlp_bias: true` in `config.json`, and an explicit **zero** bias on every other layer/projection
— exact, since `x + 0 == x`) makes `resid_out` include exactly `coef*vec[layer]` extra, at exactly the
point the hook adds it. That's a static, config-time equivalent of the runtime hook, so the same
condition can be **baked into a checkpoint variant** and served by **stock** vLLM with full
continuous batching — no hook, no serialization, ~30x the throughput of the hook server on an H200
(see `persona_vector_steering/HANDOFF.md` for the full analysis). This is the **recommended** path
for running the sweep; see below.

## Fast path: baked checkpoints + vLLM (recommended)

```bash
# bake one (trait, coef, layer) into a variant dir (idempotent; ~2 MB of new tensors, shards symlinked)
python -m persona_vector_steering.bake --trait goodness --coef 2 --layer 16 --out-dir /workspace/pvec_baked
# -> prints the absolute variant dir as the LAST line of stdout, e.g.:
#    /workspace/pvec_baked/goodness_c2_l16
# rebuild after a code/vector change:
python -m persona_vector_steering.bake --trait goodness --coef 2 --layer 16 --force

# serve it with plain vLLM — no hook, no custom server
vllm serve /workspace/pvec_baked/goodness_c2_l16 --served-model-name pvec:goodness:2:16

# whole sweep on a pod (bake + serve + run + judge, one trait at a time, restarting vLLM between):
bash run_pvec_vllm_on_pod.sh
PVEC_COEF=3 PVEC_LAYER=20 bash run_pvec_vllm_on_pod.sh    # tuned values
TRAITS="goodness sarcasm" bash run_pvec_vllm_on_pod.sh    # subset
SHUTDOWN=stop SAVE_TO_GIT=1 bash run_pvec_vllm_on_pod.sh  # unattended overnight run

# fast end-to-end sanity check (~10 min): bake one trait, serve it, hit the API directly, tiny sweep
bash smoke_pvec_vllm.sh
PVEC_COEF=4 TRAIT=sarcasm bash smoke_pvec_vllm.sh
```

Variant dirs live at `BAKE_DIR` (default `/workspace/pvec_baked`), one per `(trait, coef, layer)`
combo, a few MB each — the shards are symlinked to the shared HF cache, not copied, so many baked
variants cost almost no extra disk. The served model name follows the same `pvec:<trait>:<coef>:
<layer>` DSL as the hook server (see Model DSL above), so `configs/persona_vector_ai2ai.py` and
`run_judge.py`/`summarize.py` need no changes — only `LOCAL_BASE_URL` points at vLLM instead of
`persona_vector_steering.serve`.

**Correctness (`verify_bake.py`)**: baking is a from-scratch reimplementation of the runtime hook's
math as static weights, so it's checked at several levels before trusting a variant:
1. **Bitwise bias check** — the baked bias tensor equals `coef * vec[layer]` exactly, and every
   other bias tensor is exactly zero.
2. **HF-baked vs HF-hook, exact-math gate** — load the baked checkpoint in plain `transformers` (no
   hook) and compare its logits/greedy output to `persona_vector_steering.steering` (the hook) on the
   same prompt at temperature 0; must match to floating-point precision (both are HF, same kernels).
3. **vLLM vs HF, kernel-noise level** — vLLM uses different attention/matmul kernels than HF, so
   baked-in-vLLM vs baked-in-HF won't be bitwise identical even though the weights are. Calibrate the
   acceptable diff on the **unsteered base pair** (HF base vs vLLM base, same prompt, temp 0) — that
   gap is pure kernel noise — then require the steered pair's gap to be in the same ballpark.
4. **Behavioral spot-check** — run the baked+vLLM variant through `persona_vectors`' own eval
   (`scripts/eval_llama.sh`) and confirm trait/coherence scores land near the reference HF-hook scores
   used to originally tune `(coef, layer)`.

The hook server (`serve.py`) remains the reference implementation for step 2 above, and `chat.py`
remains the interactive REPL for eyeballing a persona without baking anything.

## Model DSL

The condition is encoded in the request's `model` field:

| model string | effect |
|---|---|
| `base` | no steering (control) |
| `pvec:<trait>:<coef>` | steer `<trait>` at the default layer (`config.DEFAULT_LAYER`) |
| `pvec:<trait>:<coef>:<layer>` | steer `<trait>` at `<layer>` |

e.g. `pvec:goodness:2`, `pvec:loving:4:16`, `pvec:sarcasm:3:20`.

## Layer indexing (important)

`<layer>` is the index into the `[num_layers+1, d_model]` vector — the **same** number
persona_vectors uses (`vec[layer]`, from `hidden_states[layer]`). The hook goes on decoder block
`layer-1` (whose output *is* `hidden_states[layer]`). So the `(layer, coef)` you pick with the
persona_vectors tuning sweep (`scripts/eval_llama.sh`) transfers here **unchanged**.

## Tune first, then run

The vectors are un-normalized mean-diffs, so coefficients are small (~1–4). Too small → no persona;
too large → incoherent. **Pick (layer, coef) per trait with `scripts/eval_llama.sh` in the
persona_vectors repo** (strongest coef whose coherence stays ≥ ~50) before running the full sweep here.

## Run

```bash
# on a GPU pod, from the AttractorBench repo root:
PVEC_COEF=2 PVEC_LAYER=16 bash run_pvec_on_pod.sh
# or a single condition manually:
python -m persona_vector_steering.serve --port 8000 &
export LOCAL_BASE_URL=http://localhost:8000/v1 LOCAL_API_KEY=x
TRAIT=goodness PVEC_COEF=2 PVEC_LAYER=16 python -m attractorbench.runner --config configs/persona_vector_ai2ai.py
python run_judge.py results/goodness_pvec_c2_l16_ai2ai --judge openai/gpt-5.4
```

## Notes / caveats

- **Serialized**: the steering hook is shared mutable state, so the server processes one request at a
  time (a lock). Keep `WORKERS` low (default 2).
- **Model must match extraction**: the vectors are directions in `unsloth/Meta-Llama-3.1-8B-Instruct`'s
  residual stream; steering a different model is invalid.
- **All positions**: the hook fires on prefill + every generated token, so the persona is active
  throughout the turn (appropriate for a persistent persona; persona_vectors' eval used response-only).
- **Per-trait coef/layer**: `run_pvec_on_pod.sh` uses one global `PVEC_COEF`/`PVEC_LAYER`. If traits
  need different settings, run the config per trait with the tuned values.
