"""Build the AttractorBench homepage table: one row per model, newest-first.

For each model it runs the OVERALL judge over the last-N turns of all its conversations (pooled
across framings/seeds/modes), saves results/family_sweep/<model>/analysis/overall__ALL.{json,md},
and emits a Model | Attractor state | Terminal form table to results/homepage_table.md.

    python build_table.py
"""

from __future__ import annotations

import concurrent.futures as cf
import glob
import json
import os

from attractorbench.analysis.characterize import characterize_overall
from attractorbench.render import write_markdown

# newest first
MODEL_ORDER = [
    "gpt-5.4", "gpt-5.4-mini", "gpt-5.4-nano", "gpt-5.3-chat-latest",
    "gpt-5.2", "gpt-5.1", "gpt-5", "gpt-4.1", "gpt-4o",
]
ROOT = "results/family_sweep"


def display_name(slug: str) -> str:
    return slug.replace("gpt", "GPT").removesuffix("-latest")


def load_conditions(slug: str) -> list[dict]:
    conds = []
    for f in glob.glob(os.path.join(ROOT, slug, "*.json")):
        if "/analysis/" in f:
            continue
        d = json.load(open(f))
        if d.get("runs"):
            conds.append(d)
    return conds


def judge_model_overall(slug: str) -> dict:
    conds = load_conditions(slug)
    if not conds:
        return {"slug": slug, "missing": True}
    r = characterize_overall(conds, f"model {slug}, ALL framings/seeds/modes pooled")
    out_dir = os.path.join(ROOT, slug, "analysis")
    os.makedirs(out_dir, exist_ok=True)
    p = os.path.join(out_dir, "overall__ALL.json")
    json.dump(r, open(p, "w"), indent=2, ensure_ascii=False)
    write_markdown(r, p)
    pa = r.get("primary_attractor") or {}
    return {
        "slug": slug,
        "label": pa.get("label") or "_no single shared attractor (diverse)_",
        "terminal": (pa.get("terminal_form") or [""])[0],
        "fraction": pa.get("fraction_raw") or "",
        "parse_ok": r.get("parse_ok"),
    }


def main() -> None:
    print(f"Judging {len(MODEL_ORDER)} models (overall, pooled)...", flush=True)
    rows = {}
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for res in ex.map(judge_model_overall, MODEL_ORDER):
            rows[res["slug"]] = res
            print(f"  {res['slug']:22} -> {res.get('label')}", flush=True)

    lines = [
        "# AttractorBench — what frontier models drift toward when AIs talk to AIs",
        "",
        "| Model | Attractor state (what it's drawn to) | Terminal form |",
        "| --- | --- | --- |",
    ]
    for slug in MODEL_ORDER:
        r = rows.get(slug, {})
        if r.get("missing"):
            continue
        term = f"`{r['terminal']}`" if r.get("terminal") else "—"
        lines.append(f"| {display_name(slug)} | {r['label']} | {term} |")
    table = "\n".join(lines) + "\n"

    out = "results/homepage_table.md"
    with open(out, "w", encoding="utf-8") as f:
        f.write(table)
    print("\n" + table)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
