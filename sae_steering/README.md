# sae_steering — SAE feature discovery for persona/trait steering

Discovers, per trait, the SAE features that represent it — a validated `trait -> feature IDs`
mapping for later steering. **This subproject builds ONLY feature discovery.** No steering, no
self-chat (that's the next phase; see bottom). Self-contained: it does not modify anything outside
`sae_steering/` (it may read `attractorbench/prompts.py` for canonical trait wording).

## Method — two-stage contrast funnel (neutral baseline)
A feature must pass BOTH stages:
- **Stage 1 (instruction contrast, cheap, no generation):** positive = trait instruction as system
  prompt; negative = plain `"You are a helpful assistant."`. Same neutral questions both sides. Encode
  the layer-19 residual, mean-pool over the **question tokens** (identical content), rank by paired
  Cohen's d. → top-50 candidates/trait.
- **Stage 2 (response contrast, filter):** greedily generate positive vs neutral completions; encode
  and mean-pool over the **completion tokens** (trait being *expressed*). Rank by paired Cohen's d.
- **Funnel:** a Stage-1 candidate survives if it also ranks highly in Stage 2 (positive d, top-K).
  Combined score = rank-product. Plus a **cross-trait specificity** flag for features shared by many traits.

Model: `meta-llama/Llama-3.1-8B-Instruct` (gated; needs `HF_TOKEN`), HF `AutoModelForCausalLM`, **bf16,
no quantization**. SAE: `Goodfire/Llama-3.1-8B-Instruct-SAE-l19` (BatchTopK, layer-19 post-block
residual). Discovery uses the **dense `relu(encoder(x))`** activations (bypassing threshold/top-k).

## Where it runs
- **Locally (no GPU)**: only `generate_contrasts.py` (OpenAI) + syntax checks. (This machine's Python
  has no torch.)
- **GPU pod (24–40GB)**: everything model-dependent — the loader gate, both harvests, discover, table.
  Reuse the pod's cu124 venv; **torch must match the host CUDA driver** (see `../TROUBLESHOOTING.md`).
  Set `HF_TOKEN` + `OPENAI_API_KEY` in the repo-root `.env`.

## Run order (from repo root, as modules)
```bash
# 0. LOADER GATE FIRST (GPU): prints SAE keys/shapes + inferred mapping + reconstruction EV.
python -m sae_steering.check_sae                       # must pass before anything else

# 1. smoke test: full pipeline on ONE trait, 3 questions (verifies plumbing end-to-end)
bash sae_steering/smoke_test.sh honesty

# 2. full run, per trait (Step 1 can also run locally):
python -m sae_steering.generate_contrasts              # all traits (OpenAI; local-ok)
python -m sae_steering.harvest_instruction_contrast --trait <t>    # GPU, repeat per trait (or omit --trait for all)
python -m sae_steering.harvest_response_contrast    --trait <t>    # GPU
python -m sae_steering.discover_features                            # all traits with both stages
python -m sae_steering.build_feature_table                         # -> results/ALL_FEATURES.json + SUMMARY.md
```

## Files
| File | Role |
|---|---|
| `config.py` | constants, paths, the 12 `TRAITS` (torch-free) |
| `sae.py` | defensive SAE loader (prints keys/shapes, infers by shape), encode/decode, `reconstruction_check` |
| `common.py` | model/tokenizer load, layer-19 hook capture, chat-template span masks, paired Cohen's d, IO |
| `check_sae.py` | **loader gate** — reconstruction sanity check |
| `generate_contrasts.py` | Step 1 — gpt-4o → pos instructions + neutral questions (cached) |
| `harvest_instruction_contrast.py` | Stage 1 — question-token contrast |
| `harvest_response_contrast.py` | Stage 2 — completion-token contrast (generates) |
| `discover_features.py` | Step 4 — funnel + specificity + top-activating examples |
| `build_feature_table.py` | Step 5 — `ALL_FEATURES.json` + `SUMMARY.md` |

## Outputs
- `data/` (gitignored): `contrasts/`, `completions/`, `stage1/`, `stage2/`, `acts/*.pt`.
- `results/` (tracked): `{trait}_features.json`, `ALL_FEATURES.json`, **`SUMMARY.md`** (the artifact to
  review when picking steering targets).

## Phase 2 — steering (BUILT)
Boost a trait's discovered features in the layer-19 residual during generation, then run the
AttractorBench self-chat on the steered base model — to test whether steering reaches the same
attractor a LoRA/persona-prompt does. Intervention is a faithful port of Goodfire's demo
`example_intervention` (encode → preserve error → boost feature(s) → decode + error).

Served as an OpenAI-compatible endpoint so the **existing harness/judge/summarize run unchanged**:

| File | Role |
|---|---|
| `steering.py` | `SteeredModel`: layer-19 hook (boost or activation-add), `chat()` generate |
| `serve_steered.py` | OpenAI `/v1/chat/completions`; model-name DSL `base` \| `steer:<trait>:<coef>[:<topn>]` |
| `steered_config.py` | AttractorBench RunConfig (steered, `STEER_TRAIT/COEF/TOPN` env) |
| `run_steered_selfchat.sh` | serve → sweep (trait × coef + base control) → judge → summary |

```bash
# after discovery has written results/<trait>_features.json:
pip install -r sae_steering/requirements.txt        # adds fastapi + uvicorn
TRAITS="goodness loving" COEFS="8 16" bash sae_steering/run_steered_selfchat.sh
#   -> results/steer_<trait>_coef<c>_top<n>_ai2ai/ + results/steer_base_ai2ai/ (control) + SUMMARY.md
```
Notes: the steered server is HF generation (no vLLM) and serializes requests (shared steering hook),
so it's slower — keep `GOODNESS_WORKERS` low. Calibrate `COEFS`: too low = no effect, too high =
fluency collapses (the steering analogue of the temperature finding). The headline comparison is
`steer_<trait>` vs `<trait>_ai2ai` (LoRA) vs `<trait>_sysprompt` vs `base`.

## NEXT STEPS
Calibrate coefficients per trait; compare steered attractors to the LoRA/prompted basins; optionally
steer multiple features / try `--mode add` (plain activation addition).
