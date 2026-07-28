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
import re
from collections import Counter
from datetime import date

from publish_steering import _ngram_rates, signature_phrases

MODEL_ORDER = [
    "thinkingmachines-inkling",
    "gpt-5.4", "gpt-5.4-mini", "gpt-5.4-nano", "gpt-5.3-chat-latest",
    "gpt-5.2", "gpt-5.1", "gpt-5", "gpt-4.1", "gpt-4o",
]
# slugs that don't follow the gpt-* naming convention
DISPLAY_NAMES = {"thinkingmachines-inkling": "Inkling"}
FAMILIES = {"thinkingmachines-inkling": "Thinking Machines"}
ROOT = "results/family_sweep"
DEFAULT_WEBSITE = "/Users/timf34/Documents/VSCode/AttractorBenchWebsite"

# (analysis filename scope, signature, human label). All become attractorStates on the detail
# page; the homepage HEADLINE is taken from HEADLINE_SIGNATURE below.
SCOPES = [
    ("ALL", "pooled", "Pooled (all framings)"),
    ("ai_to_ai_aware", "ai-to-ai", "AI-to-AI (aware)"),
    ("ai_to_ai_self_aware", "self-aware", "AI-to-AI (self-aware)"),
    ("helpful_assistant", "helpful-assistant", "Helpful assistant"),
    ("self_monologue", "self-monologue", "Self-talk (monologue)"),
]
HEADLINE_SIGNATURE = "pooled"  # which signature leads the homepage table ("pooled" | "ai-to-ai" | ...)


def display_name(slug: str) -> str:
    return DISPLAY_NAMES.get(slug) or slug.replace("gpt", "GPT").removesuffix("-latest")


def family(slug: str) -> str:
    if slug in FAMILIES:
        return FAMILIES[slug]
    return "GPT-5.x" if slug.startswith("gpt-5") else "GPT-4.x"


def load_json(path: str):
    return json.load(open(path)) if os.path.exists(path) else None


def strength(pa: dict) -> str:
    if pa.get("fraction_count") is not None and pa.get("fraction_denom"):
        return f"{pa['fraction_count']}/{pa['fraction_denom']}"
    return pa.get("fraction_raw") or ""


def is_confounded(cond: dict) -> bool:
    """self_append with an 'another AI' framing makes one model ventriloquize both sides of an
    imagined dialogue — neither clean self-talk nor clean dialogue. Excluded from the site."""
    return (cond.get("mode") == "self_append"
            and str(cond.get("system_prompt_key") or "").startswith("ai_to_ai"))


def condition_label(cond: dict) -> str:
    mode = cond.get("mode") or ""
    if cond.get("memory_mode") == "last_message_only":
        mode += " (no memory)"
    return f"{mode} · {cond.get('system_prompt_key')} · {cond.get('seed_prompt_set')}"


def representative_run(cond: dict) -> dict:
    # most-developed run (max visible content) — the attractor is clearest in a full conversation
    return max(cond["runs"], key=lambda r: sum(len(t["content_clean"]) for t in r["turns"]))


def yaml_frontmatter(d: dict) -> str:
    # JSON flow style is valid YAML; emit one key per line.
    return "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in d.items())


def model_ngrams(slug: str) -> dict:
    """Aggregate stage-1 tail n-gram counts (+ run presence) across a model's (non-confounded)
    conditions, shaped like a single stage-1 record so signature_phrases() can score it."""
    counts: dict[int, Counter] = {2: Counter(), 3: Counter()}
    runs_present: dict[int, Counter] = {2: Counter(), 3: Counter()}
    n_runs = 0
    for path in glob.glob(os.path.join(ROOT, slug, "analysis", "*__stage1.json")):
        # same exclusion as is_confounded(): self_append with an ai_to_ai framing
        if re.match(r"^self_append__.*?__ai_to_ai", os.path.basename(path)):
            continue
        s1 = load_json(path) or {}
        n_runs += s1.get("n_runs") or 0
        for n, key in ((2, "condition_tail_bigram_frequency"), (3, "condition_tail_trigram_frequency")):
            for g, c, r in s1.get(key) or []:
                counts[n][g] += c
                runs_present[n][g] += r
    return {
        "n_runs": n_runs,
        "condition_tail_bigram_frequency": [[g, c, runs_present[2][g]] for g, c in counts[2].items()],
        "condition_tail_trigram_frequency": [[g, c, runs_present[3][g]] for g, c in counts[3].items()],
    }


def publish_model(slug: str, order: int, website: str, phrases: list[dict]) -> str | None:
    adir = os.path.join(ROOT, slug, "analysis")
    cond_files = sorted(f for f in glob.glob(os.path.join(ROOT, slug, "*.json")) if "/analysis/" not in f)
    pairs = [(f, json.load(open(f))) for f in cond_files]
    pairs = [(f, c) for f, c in pairs if c.get("runs") and not is_confounded(c)]
    cond_files = [f for f, _ in pairs]
    conds = [c for _, c in pairs]
    if not conds:
        return None

    overalls = {scope: load_json(os.path.join(adir, f"overall__{scope}.json"))
                for scope, _, _ in SCOPES}

    # attractor states — one card per judged scope. A judge that found NO dominant attractor
    # is a real (and valued) finding: show it as an explicit honest-null card, never skip it.
    states = []
    for scope, sig, label in SCOPES:
        o = overalls.get(scope)
        if not o:
            continue  # scope not judged yet (no data is different from a null finding)
        if not o.get("parse_ok") and not o.get("primary_attractor"):
            # Judge output failed to parse — that's a pipeline failure, NOT an honest null.
            # Rendering it as "no dominant attractor" would misreport; skip and warn instead.
            print(f"    [warn] {slug} {scope}: judge output unparsed (parse_ok=False) — "
                  f"scope omitted; re-run this judge")
            continue
        pa = o.get("primary_attractor")
        if pa:
            states.append({
                "signature": sig,
                "scopeLabel": label,
                "label": pa.get("label") or "",
                "description": pa.get("one_line") or "",
                "strength": strength(pa),
                "terminalForms": pa.get("terminal_form") or [],
            })
        else:
            secs = [a for a in (o.get("attractors") or []) if not a.get("is_primary")]
            desc = ("Conversations split across clusters: "
                    + "; ".join(f"{a.get('label')} ({strength(a)})" for a in secs)
                    if secs else "Sampled conversations are diverse — no shared basin found.")
            states.append({
                "signature": sig, "scopeLabel": label,
                "label": "no dominant attractor",
                "description": desc, "strength": "", "terminalForms": [],
            })
    # headline = STRICTLY the chosen signature. No fallback to another scope — presenting a
    # framing-specific finding as the model's overall signature would overstate it.
    hs = next((s for s in states if s["signature"] == HEADLINE_SIGNATURE), None)
    headline = ({"signature": hs["signature"], "attractor": hs["label"],
                 "terminalForm": (hs["terminalForms"] or [""])[0], "strength": hs["strength"]}
                if hs else {"signature": "none", "attractor": "—", "terminalForm": "", "strength": ""})
    headline["phrases"] = phrases

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

    # Remove stale transcripts (e.g. pruned/confounded conditions) — this dir is fully
    # pipeline-generated, so anything not in the published set is an orphan page.
    published = {t["condition"] + ".json" for t in transcripts}
    for fn in os.listdir(tdir):
        if fn.endswith(".json") and fn not in published:
            os.remove(os.path.join(tdir, fn))
            print(f"    removed stale transcript {slug}/{fn}")

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
    # signature phrases: each model's aggregated n-grams scored against the OTHER models
    ngrams = {slug: model_ngrams(slug) for slug in MODEL_ORDER}
    rates = {slug: _ngram_rates(n) for slug, n in ngrams.items()
             if n["condition_tail_bigram_frequency"] or n["condition_tail_trigram_frequency"]}
    for i, slug in enumerate(MODEL_ORDER):
        order = 100 - i  # newest first
        background = [r for s, r in rates.items() if s != slug]
        phrases = signature_phrases(ngrams[slug], background, top=3) if slug in rates else []
        line = publish_model(slug, order, args.website, phrases)
        print("  " + (line or f"{slug}: SKIP (no data)"))
    print("DONE")


if __name__ == "__main__":
    main()
