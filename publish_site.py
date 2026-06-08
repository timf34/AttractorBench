"""Publish judged outputs + representative transcripts into the Astro website repo.

Reads results/family_sweep/<model>/analysis/overall__*.json (the judge outputs) and the raw
condition transcripts, and writes — into the website repo — one content-collection entry per
model (frontmatter + the overall writeup body) plus one representative transcript per condition.

    python publish_site.py [--website /path/to/AttractorBenchWebsite]

Frontmatter is emitted as JSON-flow YAML (valid YAML, no PyYAML dependency).
"""

from __future__ import annotations

import argparse
import glob
import json
import os
from datetime import date

MODEL_ORDER = [
    "gpt-5.4", "gpt-5.4-mini", "gpt-5.4-nano", "gpt-5.3-chat-latest",
    "gpt-5.2", "gpt-5.1", "gpt-5", "gpt-4.1", "gpt-4o",
]
ROOT = "results/family_sweep"
DEFAULT_WEBSITE = "/Users/timf34/Documents/VSCode/AttractorBenchWebsite"

# (analysis filename scope, signature, human label). All become attractorStates on the detail
# page; the homepage HEADLINE is taken from HEADLINE_SIGNATURE below.
SCOPES = [
    ("ALL", "pooled", "Pooled (all framings)"),
    ("ai_to_ai_aware", "ai-to-ai", "AI-to-AI (aware)"),
    ("ai_to_ai_self_aware", "self-aware", "AI-to-AI (self-aware)"),
    ("helpful_assistant", "helpful-assistant", "Helpful assistant"),
]
HEADLINE_SIGNATURE = "pooled"  # which signature leads the homepage table ("pooled" | "ai-to-ai" | ...)


def display_name(slug: str) -> str:
    return slug.replace("gpt", "GPT").removesuffix("-latest")


def family(slug: str) -> str:
    return "GPT-5.x" if slug.startswith("gpt-5") else "GPT-4.x"


def load_json(path: str):
    return json.load(open(path)) if os.path.exists(path) else None


def strength(pa: dict) -> str:
    if pa.get("fraction_count") is not None and pa.get("fraction_denom"):
        return f"{pa['fraction_count']}/{pa['fraction_denom']}"
    return pa.get("fraction_raw") or ""


def condition_label(cond: dict) -> str:
    return f"{cond.get('mode')} · {cond.get('system_prompt_key')} · {cond.get('seed_prompt_set')}"


def representative_run(cond: dict) -> dict:
    # most-developed run (max visible content) — the attractor is clearest in a full conversation
    return max(cond["runs"], key=lambda r: sum(len(t["content_clean"]) for t in r["turns"]))


def yaml_frontmatter(d: dict) -> str:
    # JSON flow style is valid YAML; emit one key per line.
    return "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in d.items())


def publish_model(slug: str, order: int, website: str) -> str | None:
    adir = os.path.join(ROOT, slug, "analysis")
    cond_files = sorted(f for f in glob.glob(os.path.join(ROOT, slug, "*.json")) if "/analysis/" not in f)
    conds = [json.load(open(f)) for f in cond_files]
    conds = [c for c in conds if c.get("runs")]
    if not conds:
        return None

    overalls = {scope: load_json(os.path.join(adir, f"overall__{scope}.json"))
                for scope, _, _ in SCOPES}

    # attractor states (skip scopes with no primary)
    states = []
    for scope, sig, label in SCOPES:
        pa = (overalls.get(scope) or {}).get("primary_attractor")
        if not pa:
            continue
        states.append({
            "signature": sig,
            "scopeLabel": label,
            "label": pa.get("label") or "",
            "description": pa.get("one_line") or "",
            "strength": strength(pa),
            "terminalForms": pa.get("terminal_form") or [],
        })
    # headline = the chosen signature (fallback: first available state)
    hs = next((s for s in states if s["signature"] == HEADLINE_SIGNATURE), states[0] if states else None)
    headline = ({"signature": hs["signature"], "attractor": hs["label"],
                 "terminalForm": (hs["terminalForms"] or [""])[0]}
                if hs else {"signature": "none", "attractor": "—", "terminalForm": ""})

    # body = the pooled overall writeup prose (the cross-framing read)
    body = ((overalls.get("ALL") or {}).get("characterization")
            or (overalls.get("ai_to_ai_aware") or {}).get("characterization")
            or "_Characterization pending._")

    # representative transcripts (one per condition) -> website src/data/transcripts/<slug>/
    tdir = os.path.join(website, "src", "data", "transcripts", slug)
    os.makedirs(tdir, exist_ok=True)
    transcripts = []
    for cf, cond in zip(cond_files, conds):
        cslug = os.path.splitext(os.path.basename(cf))[0]
        run = representative_run(cond)
        payload = {
            "slug": slug, "model": display_name(slug), "condition_label": condition_label(cond),
            "mode": cond.get("mode"), "system_prompt_key": cond.get("system_prompt_key"),
            "seed_prompt_set": cond.get("seed_prompt_set"), "seed_prompt": run.get("seed_prompt"),
            "run_index": run.get("run_index"),
            "turns": [{"turn": t["turn"], "speaker": t["speaker"], "model": t["model"],
                       "content_clean": t["content_clean"]} for t in run["turns"]],
        }
        json.dump(payload, open(os.path.join(tdir, cslug + ".json"), "w"), ensure_ascii=False)
        transcripts.append({"condition": cslug, "label": condition_label(cond)})

    fm = {
        "slug": slug, "name": display_name(slug), "family": family(slug), "order": order,
        "runs": sum(len(c["runs"]) for c in conds), "lastUpdated": date.today().isoformat(),
        "headline": headline, "attractorStates": states, "transcripts": transcripts,
    }
    mdir = os.path.join(website, "src", "content", "models")
    os.makedirs(mdir, exist_ok=True)
    with open(os.path.join(mdir, slug + ".md"), "w", encoding="utf-8") as f:
        f.write("---\n" + yaml_frontmatter(fm) + "\n---\n\n" + body + "\n")
    return f"{slug:22} order={order} states={len(states)} transcripts={len(transcripts)} headline={headline['attractor'][:50]}"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--website", default=DEFAULT_WEBSITE)
    args = p.parse_args()
    print(f"Publishing to {args.website}")
    for i, slug in enumerate(MODEL_ORDER):
        order = 100 - i  # newest first
        line = publish_model(slug, order, args.website)
        print("  " + (line or f"{slug}: SKIP (no data)"))
    print("DONE")


if __name__ == "__main__":
    main()
