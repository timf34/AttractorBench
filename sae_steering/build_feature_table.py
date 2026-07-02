"""Step 5 — aggregate per-trait feature files into a single index + summary table.

Reads every results/{trait}_features.json produced by discover_features (Step 4) and writes:
    results/ALL_FEATURES.json   {trait: [final feature_ids in order]}
    results/SUMMARY.md          one markdown row per trait (its #1 final feature)

Pure stdlib + repo helpers; no torch, no model load.

    python -m sae_steering.build_feature_table
"""

from __future__ import annotations

import argparse
import os

from . import common, config

_EXAMPLE_CHARS = 120  # truncate the example cell to ~this many chars


def _cell(text: str, n: int = _EXAMPLE_CHARS) -> str:
    """Make text safe for a markdown table cell: collapse newlines/whitespace, truncate, escape pipes."""
    collapsed = " ".join(str(text).split())[:n]
    return collapsed.replace("|", "\\|")


def _f(x) -> str:
    return "—" if x is None else f"{x:.3f}"


def main() -> None:
    ap = argparse.ArgumentParser(description="Step 5: aggregate per-trait SAE feature files into an index + summary.")
    ap.parse_args()  # no options; kept for --help consistency with the rest of the pipeline

    config.ensure_dirs()

    all_features: dict[str, list[int]] = {}
    rows: list[tuple[str, dict]] = []
    for trait in config.TRAITS:
        p = config.features_path(trait)
        if not os.path.exists(p):
            continue
        try:
            data = common.load_json(p)
        except Exception as e:  # noqa: BLE001
            print(f"  [warn] could not read {p}: {e}")
            continue
        finals = data.get("final_features", [])
        # ALL_FEATURES is the steering index: prefer strict survivors, else fall back to the
        # Stage-2-primary (expression) features so value traits still have steering targets.
        chosen = finals if finals else data.get("stage2_primary", [])
        all_features[trait] = [int(f["feature_id"]) for f in chosen]
        rows.append((trait, data))

    if not rows:
        print(f"[table] no {{trait}}_features.json files found in {config.RESULTS_DIR} — run discover_features first.")
        return

    # results/ALL_FEATURES.json (sorted by trait name for a stable diff)
    all_features = {t: all_features[t] for t in sorted(all_features)}
    all_path = os.path.join(config.RESULTS_DIR, "ALL_FEATURES.json")
    common.save_json(all_path, all_features)

    # results/SUMMARY.md
    header = "| Trait | #strict | source | top feat | stage1 d | stage2 d | shared | example |"
    sep = "| --- | --- | --- | --- | --- | --- | --- | --- |"
    lines = ["# SAE feature discovery — summary", "",
             "_source: `both` = passed strict funnel; `stage2` = fallback to top expression feature "
             "(no strict survivors)._", "", header, sep]
    for trait, data in sorted(rows, key=lambda r: r[0]):
        finals = data.get("final_features", [])
        n_final = data.get("n_final", len(finals))
        top = finals[0] if finals else (data.get("stage2_primary") or [None])[0]
        source = "both" if finals else ("stage2" if top else "—")
        if top:
            ex = (top.get("top_activating_examples") or [""])[0]
            lines.append(
                f"| {trait} | {n_final} | {source} | {top['feature_id']} | "
                f"{_f(top.get('stage1_cohens_d'))} | {_f(top.get('stage2_cohens_d'))} | "
                f"{top.get('n_traits_sharing','—')} | {_cell(ex)} |"
            )
        else:
            lines.append(f"| {trait} | {n_final} | — | — | — | — | — | — |")
    md = "\n".join(lines) + "\n"

    md_path = os.path.join(config.RESULTS_DIR, "SUMMARY.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"[table] wrote {all_path} ({len(all_features)} trait(s))")
    print(f"[table] wrote {md_path} ({len(rows)} trait row(s))")


if __name__ == "__main__":
    main()
