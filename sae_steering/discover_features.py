"""Step 4 — funnel Stage-1 + Stage-2 rankings into final per-trait SAE features.

Combines the cheap instruction-contrast (Stage 1) and the response-contrast (Stage 2) into a
final, deduplicated short-list of features per trait. A Stage-1 candidate SURVIVES only if it is
also strong in Stage 2 (positive paired Cohen's d AND inside the Stage-2 top-K); survivors are
ordered by a robust rank-product of their two ranks (lower is better). We additionally flag
cross-trait "generic" features (shared by many traits' Stage-1 candidates) and pull each feature's
top-activating positive completions so it can be eyeballed.

No model/SAE load — pure torch tensor analysis over cached artifacts (CPU is fine).

    python -m sae_steering.discover_features [--trait honesty]

Inputs (per trait):
    data/stage1/{trait}.json        Stage-1 top-50 candidates (descending Cohen's d; index = rank)
    data/acts/{trait}_stage2.pt     {"pos","neg","cohens_d"} Stage-2 acts (cohens_d is authoritative)
    data/completions/{trait}.json   pos/neg completions (items[i] aligns with pos matrix row i)

Output:
    results/{trait}_features.json   final features + stage1_only / stage2_only diagnostics
"""

from __future__ import annotations

import argparse
import collections
import os

import torch

from . import common, config

_EXAMPLE_CHARS = 200      # truncate each top-activating completion to ~this many chars
_TOP_EXAMPLES = 5         # how many top-activating completions to keep per feature
_STAGE2_ONLY_KEEP = 20    # how many "stage2 found, stage1 missed" features to report


def _input_paths(trait: str) -> dict[str, str]:
    return {
        "stage1": config.stage1_path(trait),
        "stage2_acts": config.acts_path(trait, "stage2"),
        "completions": config.completions_path(trait),
    }


def _missing_inputs(trait: str) -> list[str]:
    return [name for name, p in _input_paths(trait).items() if not os.path.exists(p)]


def _truncate(text: str, n: int = _EXAMPLE_CHARS) -> str:
    """Collapse whitespace/newlines into single spaces and truncate to n chars (for compact eyeballing)."""
    return " ".join(str(text).split())[:n]


def _top_examples(fid: int, pos, items) -> list[str]:
    """The completions whose pos-condition activation of feature `fid` is highest (human evidence)."""
    out: list[str] = []
    if 0 <= fid < pos.shape[1] and pos.shape[0] > 0:
        col = pos[:, fid]
        _, top_idx = torch.topk(col, min(_TOP_EXAMPLES, col.numel()))
        for idx in top_idx.tolist():
            if 0 <= idx < len(items):
                out.append(_truncate(items[idx].get("pos_text", "")))
    return out


def _cross_trait_sharing() -> tuple[collections.Counter, list[str]]:
    """How many traits' Stage-1 candidate sets each feature_id appears in.

    Returns (counter[feature_id] -> #traits, available_traits with a Stage-1 file).
    """
    sharing: collections.Counter = collections.Counter()
    available: list[str] = []
    for t in config.TRAITS:
        p = config.stage1_path(t)
        if not os.path.exists(p):
            continue
        try:
            s1 = common.load_json(p)
        except Exception as e:  # noqa: BLE001
            print(f"  [warn] could not read {p}: {e}")
            continue
        available.append(t)
        fids = {int(c["feature_id"]) for c in s1.get("candidates", [])}
        for fid in fids:
            sharing[fid] += 1
    return sharing, available


def run_trait(trait: str, sharing: collections.Counter, n_available_traits: int) -> dict:
    # 1. Stage-1 candidates: list index == Stage-1 rank (0-based), descending Cohen's d.
    s1 = common.load_json(config.stage1_path(trait))
    candidates = s1.get("candidates", [])
    stage1_rank = {int(c["feature_id"]): i for i, c in enumerate(candidates)}
    stage1_d = {int(c["feature_id"]): float(c["cohens_d"]) for c in candidates}
    cand_set = set(stage1_rank)

    # 2. Stage-2 acts: authoritative cohens_d vector + pos matrix; build a full Stage-2 rank lookup.
    acts = torch.load(config.acts_path(trait, "stage2"), map_location="cpu")
    cohens_d = acts["cohens_d"].float()                 # [d_sae]
    pos = acts["pos"].float()                           # [Q, d_sae]
    d_sae = cohens_d.numel()
    s2_order = torch.argsort(cohens_d, descending=True)  # s2_order[rank] = feature_id
    s2_rank_vec = torch.empty(d_sae, dtype=torch.long)   # inverse permutation: rank of each feature_id
    s2_rank_vec[s2_order] = torch.arange(d_sae, dtype=torch.long)

    # completions (row i <-> items[i])
    comp = common.load_json(config.completions_path(trait))
    items = comp.get("items", [])

    # 3. Funnel + 4. rank-product combined score (lower is better).
    survivors: list[tuple[int, float, int]] = []        # (fid, stage2_d, stage2_rank)
    stage1_only: list[dict] = []                        # near-misses, WITH their stage2 stats (diagnostic)
    for fid in stage1_rank:                              # candidate order (descending Stage-1 d)
        s2d = float(cohens_d[fid].item())
        s2r = int(s2_rank_vec[fid].item())
        if s2d > 0 and s2r < config.STAGE2_TOPK:
            survivors.append((fid, s2d, s2r))
        else:
            stage1_only.append({"feature_id": fid, "stage1_rank": stage1_rank[fid],
                                "stage1_cohens_d": stage1_d[fid], "stage2_cohens_d": s2d,
                                "stage2_rank": s2r})

    survivors.sort(key=lambda t: ((stage1_rank[t[0]] + 1) * (t[2] + 1), -t[1], t[0]))
    survivors = survivors[: config.FINAL_COUNT]

    # 5. generic flag: shared by "many" traits' Stage-1 candidates.
    generic_threshold = max(3, n_available_traits // 2)

    def _entry(fid: int) -> dict:
        s2d = float(cohens_d[fid].item())
        s2r = int(s2_rank_vec[fid].item())
        n_sharing = int(sharing.get(fid, 0))
        return {
            "feature_id": fid,
            "stage1_cohens_d": stage1_d.get(fid),                 # None if not a Stage-1 candidate
            "stage1_rank": stage1_rank.get(fid),
            "stage2_cohens_d": s2d,
            "stage2_rank": s2r,
            "in_stage1": fid in stage1_rank,
            "combined_score": (stage1_rank[fid] + 1) * (s2r + 1) if fid in stage1_rank else None,
            "n_traits_sharing": n_sharing,
            "generic": bool(n_sharing >= generic_threshold),
            "top_activating_examples": _top_examples(fid, pos, items),
        }

    # 6a. final_features: strict funnel survivors (in BOTH stages).
    final_features = [_entry(fid) for fid, _, _ in survivors]

    # 6b. stage2_primary: the top Stage-2 (expression) features — the steering-relevant set, ALWAYS
    # populated. For tonal traits this overlaps final_features; for value traits (empty intersection)
    # it's the practical steering target list. `in_stage1` marks the high-confidence ones.
    stage2_primary = [_entry(int(fid)) for fid in s2_order[: config.STAGE2_PRIMARY_N].tolist()]

    # stage2_only: top Stage-2 features that were NOT Stage-1 candidates (diagnostic).
    stage2_only = [int(fid) for fid in s2_order.tolist() if fid not in cand_set][:_STAGE2_ONLY_KEEP]

    out = {
        "trait": trait,
        "n_final": len(final_features),
        "final_features": final_features,
        "stage2_primary": stage2_primary,
        "stage1_only": stage1_only,
        "stage2_only": stage2_only,
    }
    common.save_json(config.features_path(trait), out)

    if final_features:
        top = final_features[0]
        print(f"[{trait}] {len(final_features)} final features "
              f"(top feat {top['feature_id']}: combined={top['combined_score']}, "
              f"s1 d={top['stage1_cohens_d']:.3f}, s2 d={top['stage2_cohens_d']:.3f}); "
              f"{len(stage1_only)} stage1-only, {len(stage2_only)} stage2-only")
    else:
        print(f"[{trait}] 0 final features survived the funnel "
              f"({len(stage1_only)} stage1-only, {len(stage2_only)} stage2-only)")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Step 4: funnel Stage-1 + Stage-2 into final SAE features.")
    ap.add_argument("--trait", help="single trait (default: all traits with stage1 + stage2 inputs present)")
    args = ap.parse_args()

    config.ensure_dirs()

    sharing, available_s1 = _cross_trait_sharing()
    n_available = len(available_s1)
    print(f"[discover] cross-trait specificity computed from {n_available} stage-1 trait file(s)")

    if args.trait:
        traits = [args.trait]
    else:
        traits = [t for t in config.TRAITS if not _missing_inputs(t)]
        if not traits:
            print("[discover] no traits with complete inputs found — run Stages 1 & 2 first; nothing to do.")
            return

    n_written = 0
    for t in traits:
        missing = _missing_inputs(t)
        if missing:
            print(f"[{t}] skipping — missing inputs: {', '.join(missing)}")
            continue
        run_trait(t, sharing, n_available)
        n_written += 1

    print(f"[discover] wrote {n_written} feature file(s) to {config.RESULTS_DIR}")


if __name__ == "__main__":
    main()
