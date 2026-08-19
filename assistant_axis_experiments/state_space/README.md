# state_space — beyond the 1-D Assistant Axis

**Question** (mentor's framing): what state variables govern persona stability under recursive
feedback, and how do interventions change the probability of entering, remaining in, and
escaping behavioral attractors? The drift experiment reads out ONE number per turn — the
Assistant-Axis projection `a_t`. But the paper itself shows persona space is not 1-D
(§2.1.3: 4–19 PCs for 70% of role-vector variance), and personas equally distant from the
Assistant can have very different behavioral consequences. So we model the per-turn state as

- `a_t` — assistantness / default-persona tether (identical to drift's readout, axis units:
  1 = default-Assistant anchor, 0 = mean-role anchor);
- `z_t` — coordinates in the **axis-orthogonalized persona PCs**: center the turn's mean
  response-token activation on the mean role vector, project out the axis direction, express
  in the top-K PCs of the (equally orthogonalized) role-vector cloud. Orthogonal to `a_t` by
  construction.

and ask whether `z_t`, after conditioning on `a_t`, improves prediction of (1) next-turn
state, (2) eventual basin, (3) transition time, (4) response to intervention — then test it
**causally** by steering an axis-orthogonal persona direction: if the destination basin
changes while `a_t` stays matched to controls, the 1-D account is insufficient.

## Pipeline

| stage | where | in | out |
|---|---|---|---|
| `persona_space.py` | laptop | released role vectors (HF) | `bases/<model>.npz` + geometry figure |
| `dump_activations.py` | pod (`run_state_space_on_pod.sh`) | existing transcripts (replay only) | `results/<cond>/analysis/*__turn_acts.npz` (pod-side) |
| `featurize.py` | pod or laptop | turn_acts × basis | `*__state_features.json` (committed) |
| `predict.py` | laptop | state features + basin labels | `reports/predict__<model>.md` + figures |
| `steered_server.py` | pod (`run_axis_steer_on_pod.sh`) | role vectors + axis | steered ai2ai conditions `axis_<m>_steer_<tag>_*` |

`basins.py` supplies labels (qwen: the validated design-vs-devotion vocab split; gemma: the
stage-2 judge's per-run assignments at temp 1.0) and axis-crossing landmarks.
`test_state_space_cpu.py` runs featurize+predict end-to-end on synthetic data with a planted
"basin lives in z, not a" structure and asserts it is recovered.

## Methodology decisions

- **Basis = the paper's own persona space.** PCA over the released role vectors, centered on
  the mean role vector — verified equivalent to their `notebooks/pca.ipynb` (`MeanScaler`,
  plain PCA). We additionally build the z-basis from the axis-orthogonalized vectors so z⊥a
  exactly (raw PC1 is only cos 0.67–0.85 aligned with the axis, so raw PC2+ would leak a_t).
- **Validation against the released artifacts** (all three models):
  `cos(default − mean(roles), released axis) = 1.000`, and components needed for 70% variance
  = **4 (gemma) / 7 (qwen) / 19 (llama)** vs the paper's 4/8/19 (App. B.1; qwen differs by one
  because the release ships only the 275 fully-role-playing vectors, not their n=463 set).
- **Readout unchanged:** per-turn mean response-token residuals, both instance views, same
  replay as `project_transcripts.py` (shared helper `turn_mean_activations`). Dump layers:
  ~¼/½/¾ depth (`persona_space.LAYERS`); ½ = the paper's target layer; llama gets a late
  extra (64) since its trajectory direction is layer-dependent and the paper capped llama late.
- **Prediction protocol:** nested feature sets `a` vs `a+z` (vs `z` as reference), grouped CV
  (all turns + both views of a run share a fold), pooled out-of-fold metrics, run-level
  bootstrap CIs on the deltas. Guards against "z helps because it memorized the run".
- **Steering vector:** `v_perp = (role − mean_role) ⊥ axis` (or a role−role contrast via
  `--minus-role`), applied at the target layer, magnitude `coef · ‖axis‖` (coef 1 = the whole
  default→mean-role gap, sideways). `--raw` (pod: `STEER_RAW=1`, tag suffix `_raw`) instead
  steers along the role's FULL offset, axis component kept — plain persona steering ("run the
  self-conversation as the demon"), not a test of the 1-D account. The server log prints
  `|v|/‖axis‖` per layer = the role's natural offset in coef units (qwen L32: demon 2.0,
  angel 1.6, void 1.9, poet 2.6; llama L40: demon 2.4; gemma L22: demon 1.3). Any of the 275
  released roles works (`demon angel void vampire eldritch destroyer trickster ...`; identical
  role set for all three models). Replay of steered transcripts is UNSTEERED, so a_t/z_t
  measure the endogenous text-driven state — the injected constant only ever acts through the
  text it causes. Optional `--with-capping` adds the paper's released capping (commutes with
  v_perp: no axis component; with `--raw` it clips the axis share the role push adds).
- **Pod driver:** `run_axis_steer_on_pod.sh` loops `VARIANTS × STEER_ROLES × STEER_COEFS`
  (server restarted per role/coef), then runs projection + dump + featurize ONCE per model
  over all its steered dirs, then the judge. Results: `results/axis_<m>_steer_<role>_c<coef>[_raw][_capped]_nosys_ai2ai`.

## Status

- 2026-08-11: built; bases + geometry for all three models committed; CPU tests green
  (dump smoke with Qwen3-0.6B, synthetic end-to-end featurize→predict). Pod stages pending:
  `run_state_space_on_pod.sh` (dump+featurize over existing axis transcripts), then laptop
  `predict.py`; steering pilot after that (needs a coef calibration pass).
- 2026-08-19: `--raw` mode + role/coef loops added (CPU-verified on the real released vectors
  for all three models; synthetic server smoke OK). Steering pilot still NOT run on a pod.
- Geometry note for steering-role choice: in qwen at L32, angel/demon are NOT equally
  axis-distant (a −0.63 vs −1.18) but are far apart in z (40.5 vs median spread 25.1).
