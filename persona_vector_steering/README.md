# Persona-vector steering

Run the AttractorBench AI-to-AI self-conversation with a persona induced by **activation steering**
using the persona vectors from the [persona_vectors](https://github.com/timf34/persona_vectors) repo
— a fourth intervention alongside base / system-prompt / LoRA.

**This is not SAE steering.** No SAE, no feature discovery. The intervention is plain activation
addition of a per-trait mean-difference direction:

```
resid[layer] += coef * persona_vec[trait][layer]
```

## Why a separate server (not vLLM)

vLLM (used by `run_on_pod.sh` for LoRA personas) can't add a vector to the residual stream through
its OpenAI API. So we serve the base model through `persona_vector_steering.serve`, an OpenAI-
compatible endpoint that applies a forward-hook steering — the harness/judge/summarize are unchanged;
just point `LOCAL_BASE_URL` at it. (Same trick `sae_steering/serve_steered.py` uses.)

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
