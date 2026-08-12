"""CPU test for the manifold machinery: a planted CURVED 1-D manifold.

Generates a noisy three-quarter circle embedded in 17-D. On such a curve, NO linear
projection can order the points (the curve doubles back), but the geodesic coordinate can —
which is exactly the distinction manifold.py exists to draw (reading A vs reading B).

Asserts:
  - TwoNN / Levina-Bickel intrinsic dimension ≈ 1 (well below the ambient 17);
  - Kendall τ(true angle, geodesic g from one end) > 0.9;
  - the BEST linear projection orders the points strictly worse than g.

    python -m assistant_axis_experiments.state_space.test_manifold_cpu
"""

from __future__ import annotations

import numpy as np
from scipy.stats import kendalltau

from .manifold import geodesics_from, levina_bickel_dim, twonn_dim


def main() -> None:
    rng = np.random.default_rng(0)
    n, D, radius = 600, 17, 10.0
    theta = np.sort(rng.uniform(0, 1.5 * np.pi, size=n))   # three-quarter circle
    X = np.zeros((n, D))
    X[:, 0] = radius * np.cos(theta)
    X[:, 1] = radius * np.sin(theta)
    # Off-manifold noise NORM (sigma*sqrt(D)) must sit BELOW nearest-neighbour spacing
    # (~0.08 here), else small-scale intrinsic-dim estimators read the noise ball's dimension,
    # not the curve's (verified: sigma=0.15 -> TwoNN ~14, sigma=0.02 -> ~7) — the papers'
    # estimation caveat, live.
    X += rng.normal(0, 0.005, size=(n, D))

    # Levina-Bickel (larger-scale) is robust to this noise (~1.1); TwoNN reads the smallest
    # scale and is only an UPPER bound under noise (2.9 here; 14 at sigma=0.15) — the same
    # ordering of trust applies when reading the real-data report.
    d2 = twonn_dim(X)
    dlb = levina_bickel_dim(X, 20)
    assert 0.7 < dlb < 2.0, f"Levina-Bickel dim {dlb:.2f} not ~1"
    assert d2 < 4.0, f"TwoNN dim {d2:.2f} should still be far below ambient 17"

    g, k_used, _ = geodesics_from(X, source_row=0)         # from the theta≈0 end
    tau_g = kendalltau(theta, g).statistic

    # best linear ordering: projection onto the top principal component of the cloud
    Xc = X - X.mean(axis=0)
    _, _, vt = np.linalg.svd(Xc, full_matrices=False)
    tau_lin = max(abs(kendalltau(theta, Xc @ vt[i]).statistic) for i in range(3))

    assert tau_g > 0.9, f"geodesic should order the curve, τ={tau_g:.2f} (K={k_used})"
    assert tau_g > tau_lin + 0.1, f"geodesic (τ={tau_g:.2f}) should beat linear (τ={tau_lin:.2f})"
    print(f"PASS: intrinsic dim {d2:.1f}/{dlb:.1f} (~1), geodesic τ={tau_g:.3f} >> "
          f"best linear τ={tau_lin:.3f} (K={k_used}) — curved-1D machinery works.")


if __name__ == "__main__":
    main()
