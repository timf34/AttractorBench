# Handoff: fast batched persona-vector steering inference

## The ask
Make **persona-vector activation steering** fast enough to run the AttractorBench AI-to-AI
conversation matrix (12 traits × N seeds × temps × ~30 turns × 2 instances) in **hours, not days** —
ideally with vLLM-class throughput. The current implementation works and is numerically correct, but
it's single-stream HF generation with a **serialized** request lock, so it's ~30× slower than the
vLLM LoRA path this project already uses. On an H200 the bottleneck is entirely batching, not compute.

## Repos (both public, branch `main`)
- **AttractorBench** — github.com/timf34/AttractorBench — the harness + the steering server. Steering
  module: `persona_vector_steering/` (as of commit `6693a28`).
- **persona_vectors** — github.com/timf34/persona_vectors — extraction code + the vectors themselves at
  `persona_vectors/Meta-Llama-3.1-8B-Instruct/*.pt` (committed, ~19 MB).

## The exact intervention (must stay numerically identical)
- **Model**: `unsloth/Meta-Llama-3.1-8B-Instruct` (bf16; 32 decoder blocks; hidden 4096; multi-EOS
  128001/128008/128009 via `generation_config`).
- **Vectors**: `<trait>_response_avg_diff.pt`, shape `[33, 4096]`. Index `k` = the direction measured
  at `hidden_states[k]` (k=0 = embeddings). **Raw mean-difference, un-normalized.**
- **Op**: `resid += coef * vector[layer]`, added at the **output of decoder block `layer-1`** (block
  L's forward output == `hidden_states[L+1]`; this matches persona_vectors' `ActivationSteerer` with
  `layer_idx = layer-1`). Applied to **all token positions** (prompt + generated).
- **Scale**: coef ~1–4 (small, because un-normalized), layer ~16–20.
- **12 traits**: honesty sincerity goodness humor impulsiveness loving mathematical nonchalance
  poeticism remorse sarcasm sycophancy.

Keeping this identical matters: coefficients are tuned in the persona_vectors repo
(`scripts/eval_llama.sh`, which uses `ActivationSteerer`), so a new fast server must produce the same
outputs for the same (trait, coef, layer) or the tuning won't transfer.

## Current implementation (`persona_vector_steering/`)
- `steering.py` — `PersonaVectorSteeredModel`: forward hook on every decoder block; the active block
  adds `coef*vec`. Plain `model.generate`.
- `serve.py` — FastAPI OpenAI-compatible `/v1/chat/completions`. **Model DSL**: `base` |
  `pvec:<trait>:<coef>[:<layer>]`. A `threading.Lock` **serializes** requests (shared mutable hook
  state) — this is the throughput killer.
- `chat.py` — interactive REPL (fine as-is; single-stream is OK interactively).
- `config.py` — `MODEL`, `VECTOR_DIR` (`PVEC_DIR` env), `DEFAULT_LAYER`.
- `configs/persona_vector_ai2ai.py` — harness run config; `MODEL=local/pvec:<trait>:<coef>:<layer>`,
  env knobs `SEEDS/MAX_TURNS/MAX_NEW_TOKENS/TEMPS/WORKERS`.
- `run_pvec_on_pod.sh`, `smoke_pvec.sh` — pod runners.

**Harness integration is loose coupling** (this is the key leverage): `attractorbench/providers.py`
routes `model="local/..."` to an OpenAI client at `LOCAL_BASE_URL`. So **any** OpenAI-compatible
endpoint works with the harness/judge/summarize unchanged. The harness sends `max_completion_tokens`
and does length-escalation when `finish_reason=="length"`.

## Why it's slow
1. **Serialized** — the shared steering hook forbids concurrent generation → no batching. #1 cause.
2. **HF single-stream** — no continuous batching / paged attention.
3. **Long replies** — the AI2AI "spiral" is the phenomenon under study; replies routinely exceed 512
   tokens, and the harness regenerates truncated turns at 1536/4608 (mitigated by `max_new_tokens=1024`,
   but they're still long).

## Approaches to evaluate (your call)
- **A. vLLM + steering.** No public API for residual additions, but: a hook in vLLM's model runner, a
  plugin, or monkeypatching the Llama forward in the worker to add `coef*vec` at the target layer.
  Steering is **constant per served condition**, which simplifies this a lot. If viable → full
  continuous batching = the real win.
- **B. Bake into weights, serve with stock vLLM.** A constant additive vector at block L's residual
  output could fold into the model (a bias on the block output / `down_proj`, or into the following
  RMSNorm) and be served as a per-condition variant. If expressible as a delta/bias vLLM will load,
  you get native batching for free. (Llama has no biases by default — assess feasibility.)
- **C. HF micro-batching.** Replace the serialized server with a queue: gather concurrent requests in a
  short window, pad, one batched `generate` with per-sequence stop, scatter results. Steering is
  constant across the batch, so the single shared hook is fine. ~10× on an H200; lowest risk. Watch:
  padding side, per-sequence EOS, a single long reply stalling the batch (consider max-batch-tokens /
  chunking).
- **D. Sharding.** N server processes across the GPU(s), harness `WORKERS` load-balanced. Cheap
  multiplier, composes with C.

## Constraints / correctness
- Keep the `pvec:<trait>:<coef>:<layer>` DSL and the OpenAI `/v1/chat/completions` response shape
  (incl. `finish_reason` — the harness's length-escalation depends on it).
- Steering must stay `resid += coef*vec[layer]` at block `layer-1`, all positions, raw. No normalization.
- Rely on `generation_config` multi-EOS for stopping (don't truncate replies — long is intentional).
- Hardware: **H200 (~141 GB)** — plenty of headroom for large batch / KV cache.

## Validation
- `chat.py` REPL (`:cmp`) to eyeball a persona.
- `smoke_pvec.sh` — tiny AI2AI run (`SEEDS=1 MAX_TURNS=3`).
- persona_vectors `scripts/eval_llama.sh` — quantitative trait-vs-coherence; a correct fast server
  should reproduce the reference scores within noise.
- **Equivalence check**: for a fixed prompt at temperature 0, the fast implementation's greedy output
  must match the current HF hook's output for the same (trait, coef, layer). That's the correctness bar.

## Definition of done
Full 12-trait matrix (or a chosen subset) runs in a few hours, OpenAI-compatible interface intact,
outputs equivalent to the reference HF steering.
