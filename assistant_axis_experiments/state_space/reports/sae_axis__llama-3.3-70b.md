# llama-3.3-70b: is the Assistant Axis a single SAE feature? (layer 50)

Directions: released axis @ L50, persona PC1 / axis-orthogonal zPC1 of the 275 role vectors, and three role−mean directions (angel, poet, engineer); all unit-normalized. Cosines are against L2-normalized SAE decoder rows; R²@k is the fraction of squared norm explained by greedy OMP (re-fit least squares each step) with k features.

## SAE: Goodfire resid L50 — dict_size 65536, hidden 8192

weights: `Goodfire/Llama-3.3-70B-Instruct-SAE-l50` / `Llama-3.3-70B-Instruct-SAE-l50.pt`; `decoder_linear.weight` stored nn.Linear-style (8192, 65536) = (hidden, dict_size) -> transposed; features were COLUMNS; 3632 dead (zero-norm) rows.

**Null baseline** (200 random unit dirs, seed 0): max |cos| mean 0.049, p95 0.055, max 0.061. OMP on 20 nulls: median R² at k=64 is 0.094, median k for 90% >64.

| direction | max cos | / null p95 | k for 90% | R²@1 | R²@2 | R²@4 | R²@8 | R²@16 | R²@32 | R²@64 |
|---|---|---|---|---|---|---|---|---|---|---|
| assistant_axis | -0.457 | 8.4x | >64 | 0.209 | 0.304 | 0.397 | 0.491 | 0.595 | 0.691 | 0.771 |
| persona_PC1 | -0.528 | 9.6x | >64 | 0.278 | 0.418 | 0.553 | 0.653 | 0.721 | 0.786 | 0.848 |
| zPC1_axis_orth | -0.436 | 8.0x | >64 | 0.190 | 0.287 | 0.424 | 0.555 | 0.650 | 0.738 | 0.811 |
| role:angel | +0.604 | 11.0x | >64 | 0.365 | 0.449 | 0.536 | 0.641 | 0.715 | 0.787 | 0.842 |
| role:poet | +0.532 | 9.7x | >64 | 0.283 | 0.415 | 0.530 | 0.623 | 0.700 | 0.776 | 0.840 |
| role:engineer | +0.290 | 5.3x | >64 | 0.084 | 0.148 | 0.250 | 0.375 | 0.506 | 0.623 | 0.719 |
| _null (median of 20)_ | 0.049 (mean) | 1.0x (p95) | >64 | 0.002 | 0.005 | 0.008 | 0.016 | 0.029 | 0.053 | 0.094 |

### top-10 features per direction (feature_index: cos)

- **assistant_axis**: 20459: -0.457, 58001: -0.398, 17945: -0.395, 2784: -0.359, 11926: -0.352, 3143: -0.342, 40835: -0.323, 50727: -0.320, 37395: -0.307, 17326: -0.304
- **persona_PC1**: 58001: -0.528, 17326: -0.476, 17945: -0.460, 20459: -0.448, 24197: -0.439, 37395: -0.438, 23547: -0.410, 34680: -0.373, 6747: -0.361, 30149: -0.327
- **zPC1_axis_orth**: 23547: -0.436, 20112: -0.434, 29098: -0.386, 51343: -0.372, 2755: -0.353, 60774: +0.350, 27289: -0.350, 39110: -0.347, 62031: -0.347, 11870: +0.346
- **role:angel**: 24197: +0.604, 31150: +0.394, 41101: +0.367, 46192: +0.360, 45462: +0.350, 28155: +0.340, 17326: +0.339, 58001: +0.317, 41291: +0.306, 36768: +0.302
- **role:poet**: 34680: +0.532, 17945: +0.458, 37395: +0.418, 23547: +0.402, 55544: +0.376, 24997: +0.340, 49671: +0.339, 45158: +0.338, 58001: +0.328, 61193: +0.325
- **role:engineer**: 20112: +0.290, 59720: +0.276, 37183: +0.271, 17945: -0.258, 58001: -0.255, 65403: +0.237, 27289: +0.237, 11870: -0.234, 44254: +0.233, 18484: +0.229

### interpretation

- `assistant_axis`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.457 vs null p95 0.055; one feature explains 20.9% of it, 90% not reached by k=64).
- `persona_PC1`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.528 vs null p95 0.055; one feature explains 27.8% of it, 90% not reached by k=64).
- `zPC1_axis_orth`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.436 vs null p95 0.055; one feature explains 19.0% of it, 90% not reached by k=64).
- `role:angel`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.604 vs null p95 0.055; one feature explains 36.5% of it, 90% not reached by k=64).
- `role:poet`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.532 vs null p95 0.055; one feature explains 28.3% of it, 90% not reached by k=64).
- `role:engineer`: feature-aligned well above chance, but clearly multi-feature (max |cos| 0.290 vs null p95 0.055; one feature explains 8.4% of it, 90% not reached by k=64).

## Axis top-10 SAE feature indices (Goodfire L50 — for Neuronpedia)

20459, 58001, 17945, 2784, 11926, 3143, 40835, 50727, 37395, 17326

## Neuronpedia labels for the axis top-10 (all anti-aligned = the away-from-Assistant end)

Source `llama3.3-70b-it / 50-resid-post-gf` (no API key needed):

| feature | cos | explanation |
|---|---|---|
| 20459 | − | us not dwell on such matters |
| 58001 | − | every universe |
| 17945 | − | that we find wisdom |
| 2784 | − | involve carefully planning |
| 11926 | − | spent most establishing |
| 3143 | − | embracing his mental health top priority |
| 40835 | − | methods for achieving |
| 50727 | − | cloak, glow, shadows |
| 37395 | − | speak of elusive entities |
| 17326 | − | you have been |

Reading: the negative (role-ward) end of the Assistant Axis decomposes into a bundle of
mystical/narrative/wisdom features — the same register as the paper's "mystical, theatrical"
extreme-steering observation and our devotion-basin vocabulary. Qwen's Neuronpedia
explanations (32-resid-batchtopk-65k) are low-quality autointerp and were not informative;
its zPC1-aligned pair (51913/57573, |cos| .73) has huge max activations (1216/194), so treat
that pair as possibly an outlier/norm feature rather than a semantic persona feature.
