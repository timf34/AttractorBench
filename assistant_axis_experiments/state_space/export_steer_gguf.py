"""Export a role-vector steering direction as an EasySteer GGUF + server-level steering spec.

EasySteer (ZJU-REAL/EasySteer, a vLLM fork overlay) applies `h' = h + scale * direction` at the
output of the listed decoder layers — the same hook point as steered_server.py's HF hook. Its
`direct` algorithm reads GGUF tensors named ``direction.<layer>``. We store
``direction.<L> = ||axis[L]|| * unit(v)`` so EasySteer's ``scale`` IS this repo's ``coef``
(coef 6 here == coef 6 in steered_server.py / calibrate_steer.py).

    python -m assistant_axis_experiments.state_space.export_steer_gguf \
        --model-key qwen-3-32b --role demon --raw --coef 6.0 \
        --out steer_vectors/qwen-3-32b__demon_c60_raw.gguf --spec-out steer_vectors/qwen-3-32b__demon_c60_raw.json
"""

from __future__ import annotations

import argparse
import json
import os

import numpy as np

from ..axes import AXIS_MODELS, target_layer_for
from .steered_server import orthogonal_steering_vectors


def main() -> None:
    ap = argparse.ArgumentParser(description="Export an EasySteer GGUF direction + spec.")
    ap.add_argument("--model-key", required=True, choices=sorted(AXIS_MODELS))
    ap.add_argument("--role", required=True)
    ap.add_argument("--minus-role", default=None)
    ap.add_argument("--raw", action="store_true", help="full role offset (axis kept); default v_perp")
    ap.add_argument("--layers", type=int, nargs="+", default=None)
    ap.add_argument("--coef", type=float, required=True, help="scale written into the spec")
    ap.add_argument("--out", required=True, help="output .gguf path")
    ap.add_argument("--spec-out", required=True, help="output steering-spec .json path")
    args = ap.parse_args()

    import gguf

    layers = args.layers or [target_layer_for(args.model_key)]
    units, axis_norms = orthogonal_steering_vectors(
        args.model_key, args.role, args.minus_role, 1.0, layers, raw=args.raw)

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    w = gguf.GGUFWriter(args.out, arch="steer")
    for L, u, n in zip(layers, units, axis_norms):
        w.add_tensor(f"direction.{L}", (u * n).float().cpu().numpy().astype(np.float32))
    w.write_header_to_file()
    w.write_kv_data_to_file()
    w.write_tensors_to_file()
    w.close()

    spec = {"vectors": [{
        "source": os.path.abspath(args.out),
        "algorithm": "direct",
        "scale": float(args.coef),
        "layers": layers,
        "apply": {"prompt": "all", "generation": "all"},
    }]}
    with open(args.spec_out, "w") as f:
        json.dump(spec, f, indent=1)
    print(f"wrote {args.out} (direction.{layers}, |dir|={[round(float(n),1) for n in axis_norms]}) "
          f"and {args.spec_out} (scale={args.coef} -> |steer|={[round(float(n)*args.coef,1) for n in axis_norms]})")


if __name__ == "__main__":
    main()
