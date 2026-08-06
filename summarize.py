"""One-page headline summary across all experiments — reads the per-condition reports already on
disk (stage-1 deterministic + stage-2 judge) and emits a single table. No API tokens.

For every condition it pulls: the primary attractor (label + fraction, from the stage-2 judge),
the top words / phrases / emojis (from stage-1), and a convergence signal. Grouped by experiment.

    python summarize.py [results_root]        # default: results/   -> writes <root>/SUMMARY.md
"""

from __future__ import annotations

import glob
import json
import os
import sys


def _load(path: str) -> dict | None:
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:  # noqa: BLE001
        return None


def _frac(a: dict) -> str:
    if a.get("fraction_count") is not None and a.get("fraction_denom"):
        return f"{a['fraction_count']}/{a['fraction_denom']}"
    return str(a.get("fraction_raw") or a.get("fraction_of_runs") or "")


def _topn(pairs, n, joiner=", "):
    """Render a list of [item, count] pairs as 'item (count)' for the first n."""
    return joiner.join(f"{item} ({count})" for item, count in (pairs or [])[:n]) or "—"


def _mean_final_jaccard(s1: dict) -> str:
    """Mean of each run's final-third turn-similarity — high = runs converged (attractor)."""
    vals = [r.get("convergence", {}).get("mean_last_third_jaccard")
            for r in s1.get("runs", [])]
    vals = [v for v in vals if v is not None]
    return f"{sum(vals) / len(vals):.2f}" if vals else "—"


def collect(root: str) -> list[dict]:
    rows = []
    # conditions may live at <root>/<cond> or one subfolder down (e.g. <root>/pvec_steering/<cond>).
    # Skipped at the second level: family_sweep (its own pipeline — build_table.py / publish_site.py)
    # and _superseded-style archive dirs inside a condition.
    s2_paths = glob.glob(os.path.join(root, "*", "analysis", "*__stage2.json"))
    for p in glob.glob(os.path.join(root, "*", "*", "analysis", "*__stage2.json")):
        parts = os.path.relpath(p, root).split(os.sep)
        if parts[0] != "family_sweep" and not parts[1].startswith("_"):
            s2_paths.append(p)
    for s2_path in sorted(s2_paths):
        if os.path.basename(s2_path).startswith("overall__"):
            continue
        s2 = _load(s2_path)
        if not s2:
            continue
        s1 = _load(s2_path.replace("__stage2.json", "__stage1.json")) or {}
        pa = s2.get("primary_attractor") or {}
        rows.append({
            "experiment": s2.get("experiment_name") or os.path.basename(os.path.dirname(os.path.dirname(s2_path))),
            "temp": s2.get("temperature"),
            "attractor": pa.get("label") or "_no single shared attractor_",
            "fraction": _frac(pa),
            "terminal": (pa.get("terminal_form") or [""])[0],
            "words": _topn(s1.get("condition_word_frequency"), 6),
            "phrases": _topn(s1.get("condition_bigram_frequency"), 4),
            "emojis": _topn(s1.get("condition_emoji_frequency"), 6, joiner=" "),
            "convergence": _mean_final_jaccard(s1),
        })
    rows.sort(key=lambda r: (str(r["experiment"]), r["temp"] if r["temp"] is not None else 0))
    return rows


def render(rows: list[dict]) -> str:
    out = [
        "# AttractorBench — headline summary across all experiments",
        "",
        f"_{len(rows)} conditions. Attractor = stage-2 judge; words/phrases/emoji = stage-1 "
        "(top by frequency); convergence = mean final-third turn similarity (higher = more "
        "convergent)._",
        "",
        "| Experiment | Temp | Primary attractor (fraction) | Top words | Top phrases | Emojis | Conv. |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in rows:
        out.append(
            f"| {r['experiment']} | {r['temp']} | {r['attractor']} ({r['fraction']}) | "
            f"{r['words']} | {r['phrases']} | {r['emojis']} | {r['convergence']} |"
        )
    # terminal forms below the table (too long for a cell)
    out += ["", "## Terminal forms (representative last-turn text)", ""]
    for r in rows:
        if r["terminal"]:
            out.append(f"- **{r['experiment']} @ {r['temp']}**: `{r['terminal']}`")
    return "\n".join(out) + "\n"


def main() -> None:
    root = sys.argv[1] if len(sys.argv) > 1 else "results"
    rows = collect(root)
    if not rows:
        print(f"No stage-2 reports found under {root}/*/analysis/. Run the judge first.")
        return
    out_path = os.path.join(root, "SUMMARY.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(render(rows))
    print(f"Wrote {out_path}  ({len(rows)} conditions across "
          f"{len({r['experiment'] for r in rows})} experiments)")


if __name__ == "__main__":
    main()
