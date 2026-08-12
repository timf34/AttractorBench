# qwen-3-32b: is the Assistant Axis a single SAE feature? (layer 32)

Directions: released axis @ L32, persona PC1 / axis-orthogonal zPC1 of the 275 role vectors, and three role−mean directions (angel, poet, engineer); all unit-normalized. Cosines are against L2-normalized SAE decoder rows; R²@k is the fraction of squared norm explained by greedy OMP (re-fit least squares each step) with k features.

![sae smear](sae_axis__qwen-3-32b.png)


## SAE: batch-top-k 65536 (trainer_2) — dict_size 65536, hidden 5120

weights: `adamkarvonen/qwen3-32b-saes` / `saes_Qwen_Qwen3-32B_batch_top_k/resid_post_layer_32/trainer_2/ae.pt`; `decoder.weight` stored nn.Linear-style (5120, 65536) = (hidden, dict_size) -> transposed; features were COLUMNS; 0 dead (zero-norm) rows.

**Null baseline** (200 random unit dirs, seed 0): max |cos| mean 0.062, p95 0.069, max 0.077. OMP on 20 nulls: median R² at k=64 is 0.152, median k for 90% >64.

| direction | max cos | / null p95 | k for 90% | R²@1 | R²@2 | R²@4 | R²@8 | R²@16 | R²@32 | R²@64 |
|---|---|---|---|---|---|---|---|---|---|---|
| assistant_axis | -0.411 | 5.9x | >64 | 0.169 | 0.221 | 0.305 | 0.427 | 0.551 | 0.647 | 0.744 |
| persona_PC1 | +0.471 | 6.8x | >64 | 0.222 | 0.352 | 0.441 | 0.534 | 0.622 | 0.720 | 0.803 |
| zPC1_axis_orth | +0.732 | 10.5x | >64 | 0.535 | 0.581 | 0.625 | 0.672 | 0.738 | 0.799 | 0.855 |
| role:angel | +0.552 | 7.9x | >64 | 0.305 | 0.400 | 0.483 | 0.585 | 0.677 | 0.754 | 0.814 |
| role:poet | -0.481 | 6.9x | >64 | 0.232 | 0.421 | 0.622 | 0.702 | 0.761 | 0.810 | 0.854 |
| role:engineer | +0.465 | 6.7x | >64 | 0.216 | 0.293 | 0.386 | 0.470 | 0.560 | 0.658 | 0.752 |
| _null (median of 20)_ | 0.062 (mean) | 1.0x (p95) | >64 | 0.004 | 0.007 | 0.014 | 0.026 | 0.047 | 0.085 | 0.152 |

### top-10 features per direction (feature_index: cos)

- **assistant_axis**: 7228: -0.411, 27900: -0.288, 33669: -0.270, 2377: +0.246, 62391: +0.238, 26734: -0.235, 20775: -0.219, 2728: -0.204, 51972: +0.204, 44901: -0.198
- **persona_PC1**: 51913: +0.471, 57573: -0.465, 7228: -0.362, 27900: -0.293, 9317: -0.253, 51840: +0.223, 33669: -0.216, 63307: -0.203, 2377: +0.190, 3243: -0.189
- **zPC1_axis_orth**: 51913: +0.732, 57573: -0.726, 41369: -0.216, 42332: -0.184, 40656: +0.168, 63307: -0.167, 64288: +0.167, 44251: +0.161, 51840: +0.161, 32900: +0.160
- **role:angel**: 7228: +0.552, 60912: +0.382, 2728: +0.345, 55257: +0.317, 19129: +0.309, 45247: +0.297, 52390: +0.278, 30592: +0.258, 31170: +0.257, 3549: +0.255
- **role:poet**: 51913: -0.481, 57573: +0.476, 51327: +0.436, 27900: +0.424, 7228: +0.401, 37628: +0.307, 9317: +0.306, 44966: +0.272, 2804: +0.248, 17109: +0.246
- **role:engineer**: 51913: +0.465, 57573: -0.460, 7228: -0.278, 2728: -0.237, 27900: -0.236, 15800: +0.232, 51840: +0.228, 13555: +0.220, 9317: -0.199, 24646: -0.197

### interpretation

- `assistant_axis`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.411 vs null p95 0.069; one feature explains 16.9% of it, 90% not reached by k=64).
- `persona_PC1`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.471 vs null p95 0.069; one feature explains 22.2% of it, 90% not reached by k=64).
- `zPC1_axis_orth`: mostly aligned with a single SAE feature (max |cos| 0.732 vs null p95 0.069; one feature explains 53.5% of it, 90% not reached by k=64).
- `role:angel`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.552 vs null p95 0.069; one feature explains 30.5% of it, 90% not reached by k=64).
- `role:poet`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.481 vs null p95 0.069; one feature explains 23.2% of it, 90% not reached by k=64).
- `role:engineer`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.465 vs null p95 0.069; one feature explains 21.6% of it, 90% not reached by k=64).

## SAE: batch-top-k 16384 (trainer_0) — dict_size 16384, hidden 5120

weights: `adamkarvonen/qwen3-32b-saes` / `saes_Qwen_Qwen3-32B_batch_top_k/resid_post_layer_32/trainer_0/ae.pt`; `decoder.weight` stored nn.Linear-style (5120, 16384) = (hidden, dict_size) -> transposed; features were COLUMNS; 0 dead (zero-norm) rows.

**Null baseline** (200 random unit dirs, seed 0): max |cos| mean 0.057, p95 0.064, max 0.070. OMP on 20 nulls: median R² at k=64 is 0.122, median k for 90% >64.

| direction | max cos | / null p95 | k for 90% | R²@1 | R²@2 | R²@4 | R²@8 | R²@16 | R²@32 | R²@64 |
|---|---|---|---|---|---|---|---|---|---|---|
| assistant_axis | -0.403 | 6.3x | >64 | 0.162 | 0.227 | 0.310 | 0.419 | 0.542 | 0.636 | 0.723 |
| persona_PC1 | +0.472 | 7.3x | >64 | 0.223 | 0.346 | 0.445 | 0.565 | 0.658 | 0.728 | 0.794 |
| zPC1_axis_orth | +0.732 | 11.4x | >64 | 0.536 | 0.568 | 0.618 | 0.674 | 0.734 | 0.789 | 0.845 |
| role:angel | +0.539 | 8.4x | >64 | 0.291 | 0.405 | 0.511 | 0.620 | 0.688 | 0.750 | 0.804 |
| role:poet | -0.480 | 7.5x | >64 | 0.231 | 0.425 | 0.636 | 0.719 | 0.764 | 0.804 | 0.844 |
| role:engineer | +0.466 | 7.3x | >64 | 0.217 | 0.288 | 0.391 | 0.490 | 0.577 | 0.659 | 0.742 |
| _null (median of 20)_ | 0.057 (mean) | 1.0x (p95) | >64 | 0.003 | 0.006 | 0.012 | 0.022 | 0.040 | 0.070 | 0.122 |

### top-10 features per direction (feature_index: cos)

- **assistant_axis**: 2000: -0.403, 13074: -0.320, 13581: -0.293, 10652: -0.248, 15091: -0.244, 7605: +0.239, 15282: -0.228, 3280: +0.218, 5545: -0.214, 10309: -0.203
- **persona_PC1**: 7726: +0.472, 8091: -0.465, 2000: -0.353, 13074: -0.322, 15392: -0.244, 15282: -0.230, 13581: -0.229, 13424: +0.209, 10652: -0.200, 6938: -0.187
- **zPC1_axis_orth**: 7726: +0.732, 8091: -0.725, 2595: -0.178, 6399: -0.178, 2257: +0.177, 14460: +0.166, 3657: +0.164, 6938: -0.161, 5013: -0.161, 15392: -0.154
- **role:angel**: 2000: +0.539, 8416: +0.396, 15392: +0.375, 10227: +0.314, 14161: +0.304, 6629: +0.296, 7175: +0.266, 8918: +0.248, 13074: +0.238, 13040: +0.209
- **role:poet**: 7726: -0.480, 8091: +0.476, 13074: +0.440, 14668: +0.433, 2000: +0.405, 1175: +0.279, 3163: +0.271, 15392: +0.236, 8329: +0.236, 10652: +0.215
- **role:engineer**: 7726: +0.466, 8091: -0.459, 13074: -0.265, 2257: +0.262, 2000: -0.261, 15392: -0.253, 15282: -0.249, 11450: +0.214, 13424: +0.205, 8416: -0.189

### interpretation

- `assistant_axis`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.403 vs null p95 0.064; one feature explains 16.2% of it, 90% not reached by k=64).
- `persona_PC1`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.472 vs null p95 0.064; one feature explains 22.3% of it, 90% not reached by k=64).
- `zPC1_axis_orth`: mostly aligned with a single SAE feature (max |cos| 0.732 vs null p95 0.064; one feature explains 53.6% of it, 90% not reached by k=64).
- `role:angel`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.539 vs null p95 0.064; one feature explains 29.1% of it, 90% not reached by k=64).
- `role:poet`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.480 vs null p95 0.064; one feature explains 23.1% of it, 90% not reached by k=64).
- `role:engineer`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.466 vs null p95 0.064; one feature explains 21.7% of it, 90% not reached by k=64).

## What the zPC1 feature pair (51913 / 57573) represents

The pair is near-antipodal because SAE activations are non-negative: a SIGNED direction gets
one feature per pole. The direction is zPC1, and its meaning is readable from the role
loadings (the paper's own PC-interpretation method): negative pole = toddler, infant,
comedian, fool, jester, pirate; positive pole = auditor, mathematician, physicist,
statistician, economist — a playful/childlike ↔ analytical/scholarly persona contrast.
(Consistent: poet loads −0.48 on 51913, engineer +0.47.)

Behaviorally it is the basin separator: design-basin runs end at zPC1 ≈ +22, devotion runs
at +8 (early turns +4.8 vs +1.0), and CAPPED runs end at +29 — capping the axis drives
conversations into the analytical pole, matching the 26:2 design basin flip. The earlier
outlier-feature caveat (max act 1216) concerns the autointerp label quality, not the
direction's meaning — the role-loading + behavioral evidence stands independently. Note the
planned poet-vs-engineer steering contrast is essentially ±zPC1, i.e. steering this pair.
