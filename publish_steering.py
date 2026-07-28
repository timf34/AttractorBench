"""Publish the trait-steering results (persona interventions on Llama-3.1-8B) into the website.

Companion to publish_site.py (which publishes the GPT family sweep). This script covers the
"can you steer the basin?" experiments: for each of the 12 persona traits, the same base model
is pushed toward the trait four ways —

    prompt_grounded  <trait>_groundedprompt_ai2ai   grounded persona system prompt
    prompt_rich      <trait>_richprompt_ai2ai       rich persona system prompt
    prompt_plain     <trait>_sysprompt_ai2ai        early plain persona prompt (2 traits judged)
    lora             <trait>_ai2ai                  character-trained LoRA
    pvec             <trait>_pvec_c<coef>_l16_ai2ai persona-vector activation steering

plus the persistence sweeps (<trait>_pvec_unsteer_k<K>_ai2ai: steer the first K turns only,
then release). All were judged by the SAME stage-2 judge (v3 prompt, GPT-5.4), so cells are
comparable; anything not judged with v3 is skipped with a warning.

Emits, into the website repo:
    src/data/steering/<trait>.json          one entry per trait (methods + persistence)
    src/data/steering/_baseline.json        the unsteered base-model basin (base_ai2ai)
    src/data/steering-transcripts/<trait>/<condition>.json   one representative run per condition

"Signature phrases" are computed from the stage-1 deterministic n-gram counts: a phrase scores
high when it is frequent in THIS condition but rare across all other published conditions
(log-lift), so generic filler drops out and basin language rises.

    python publish_steering.py [--website /path/to/AttractorBenchWebsite]
"""

from __future__ import annotations

import argparse
import glob
import json
import math
import os
import re
from datetime import date

ROOT = "results"
DEFAULT_WEBSITE = "/Users/timf34/Documents/VSCode/AttractorBenchWebsite"
REQUIRED_PROMPT_VERSION = "v3"

TRAITS = [
    "goodness", "honesty", "humor", "impulsiveness", "loving", "mathematical",
    "nonchalance", "poeticism", "remorse", "sarcasm", "sincerity", "sycophancy",
]

# (method key, human label, matrix order). prompt_plain is an early variant with judged data
# for only 2 traits — published on trait pages but not a matrix column.
METHODS = [
    ("prompt_grounded", "System prompt (grounded)", 0),
    ("prompt_rich", "System prompt (rich)", 1),
    ("prompt_plain", "System prompt (plain)", 2),
    ("lora", "Character-trained LoRA", 3),
    ("pvec", "Activation steering (persona vector)", 4),
]

HEADLINE_TEMPS = (1.0, 0.7)  # cell headline = temp 1.0 judgment; fall back to 0.7


def parse_experiment_dir(name: str):
    """Map a results/ dir name to (trait, method, params) or None if not a steering run."""
    m = re.match(r"^([a-z]+)_pvec_unsteer_k(\d+)_ai2ai$", name)
    if m and m.group(1) in TRAITS:
        return m.group(1), "unsteer", {"k": int(m.group(2))}
    m = re.match(r"^([a-z]+)_pvec_c([0-9.]+)_l(\d+)_ai2ai$", name)
    if m and m.group(1) in TRAITS:
        return m.group(1), "pvec", {"coef": float(m.group(2)), "layer": int(m.group(3))}
    m = re.match(r"^([a-z]+)_(groundedprompt|richprompt|sysprompt)_ai2ai$", name)
    if m and m.group(1) in TRAITS:
        method = {"groundedprompt": "prompt_grounded", "richprompt": "prompt_rich",
                  "sysprompt": "prompt_plain"}[m.group(2)]
        return m.group(1), method, {}
    m = re.match(r"^([a-z]+)_ai2ai$", name)
    if m and m.group(1) in TRAITS:
        return m.group(1), "lora", {}
    return None


def load_json(path: str):
    return json.load(open(path)) if os.path.exists(path) else None


def strength(pa: dict) -> str:
    if pa.get("fraction_count") is not None and pa.get("fraction_denom"):
        return f"{pa['fraction_count']}/{pa['fraction_denom']}"
    return pa.get("fraction_raw") or ""


def representative_run(cond: dict) -> dict:
    # most-developed run (max visible content) — the attractor is clearest in a full conversation
    return max(cond["runs"], key=lambda r: sum(len(t["content_clean"]) for t in r["turns"]))


# ---------------------------------------------------------------------------- conditions


def collect_conditions(exp_dir: str) -> list[dict]:
    """One record per judged condition in an experiment dir: raw transcript file + stage1/stage2."""
    out = []
    for s2_path in sorted(glob.glob(os.path.join(exp_dir, "analysis", "*__stage2.json"))):
        s2 = load_json(s2_path)
        if not s2 or not s2.get("parse_ok"):
            print(f"    [warn] unparsed judge output skipped: {s2_path}")
            continue
        if s2.get("prompt_version") != REQUIRED_PROMPT_VERSION:
            print(f"    [warn] non-{REQUIRED_PROMPT_VERSION} judgment skipped: {s2_path}")
            continue
        cond_slug = os.path.basename(s2_path).removesuffix("__stage2.json")
        raw = load_json(os.path.join(exp_dir, cond_slug + ".json"))
        if not raw or not raw.get("runs"):
            print(f"    [warn] no raw transcripts for {cond_slug} — skipped")
            continue
        s1 = load_json(os.path.join(exp_dir, "analysis", cond_slug + "__stage1.json"))
        # URL-safe slug: raw condition names contain ':' and '.' (e.g. pvec:goodness:2.0:16),
        # which break as URL path segments / filenames on some hosts.
        url_slug = re.sub(r"[^a-zA-Z0-9_-]+", "-", cond_slug)
        out.append({"slug": url_slug, "stage2": s2, "stage1": s1, "raw": raw})
    # A re-run condition gets a timestamp-suffixed filename at the same temperature — keep only
    # the most recently judged condition per temperature.
    latest: dict[float, dict] = {}
    for c in out:
        t = c["stage2"].get("temperature")
        if t not in latest or (c["stage2"].get("analyzed_at") or "") > (latest[t]["stage2"].get("analyzed_at") or ""):
            latest[t] = c
    dropped = len(out) - len(latest)
    if dropped:
        print(f"    [note] {exp_dir}: dropped {dropped} superseded re-run condition(s)")
    return sorted(latest.values(), key=lambda c: c["stage2"].get("temperature") or 0)


# ---------------------------------------------------------------------- signature phrases


def _ngram_counts(s1: dict) -> dict[str, tuple[int, int]]:
    """gram -> (count, runs_present). Prefers the tail-restricted stage-1 fields (basin language,
    not mid-conversation content); falls back to whole-conversation counts on old stage-1 files,
    where runs_present is unknown (None)."""
    out: dict[str, tuple[int, int]] = {}
    if s1.get("condition_tail_bigram_frequency") or s1.get("condition_tail_trigram_frequency"):
        for key in ("condition_tail_bigram_frequency", "condition_tail_trigram_frequency"):
            for g, c, r in s1.get(key) or []:
                out[g] = (c, r)
    else:
        for key in ("condition_bigram_frequency", "condition_trigram_frequency"):
            for g, c in s1.get(key) or []:
                out[g] = (c, None)
    return out


def _ngram_rates(s1: dict) -> dict[str, float]:
    """Bigram+trigram relative frequencies within one condition's stage-1 counts."""
    counts = _ngram_counts(s1)
    total = sum(c for c, _ in counts.values()) or 1
    return {g: c / total for g, (c, _) in counts.items()}


# Chat-template special tokens a model sometimes leaks into its text ("Farewell.<|end_message|>").
# Stage-1 tokenization strips the <|_|> punctuation, turning them into ordinary words ("end message")
# that then surface as tail n-grams. Template-token leakage isn't model language, so drop any
# candidate phrase containing a token's word form. (Raw stage-1 counts stay unfiltered.)
_TEMPLATE_TOKEN_FRAGMENTS = tuple(
    t.replace("_", " ")
    for t in ("end_message", "im_start", "im_end", "eot_id", "endoftext", "end_of_text",
              "start_header_id", "end_header_id")
)


def signature_phrases(s1: dict, background: list[dict], top: int = 4) -> list[dict]:
    """Phrases frequent HERE and rare elsewhere. background = _ngram_rates of all other conditions.
    A phrase must appear in multiple runs' tails — one run repeating a story motif 200 times is
    content, not a basin."""
    if not s1:
        return []
    rates = _ngram_rates(s1)
    grams = _ngram_counts(s1)
    counts = {g: c for g, (c, _) in grams.items()}
    n_runs = s1.get("n_runs") or 0
    min_runs = 3 if n_runs >= 8 else 2
    n_bg = len(background) or 1
    scored = []
    for g, rate in rates.items():
        if any(f" {frag} " in f" {g} " for frag in _TEMPLATE_TOKEN_FRAGMENTS):
            continue
        runs_present = grams[g][1]
        if runs_present is not None and runs_present < min_runs:
            continue
        bg_rate = sum(b.get(g, 0.0) for b in background) / n_bg
        lift = math.log((rate + 1e-6) / (bg_rate + 1e-6))
        if lift <= 0:
            continue
        scored.append((rate * lift, g))
    scored.sort(reverse=True)

    def token_pairs(g: str) -> set[tuple[str, str]]:
        toks = g.split()
        return {(toks[i], toks[i + 1]) for i in range(len(toks) - 1)}

    def fuller(g: str) -> str:
        # a bigram that sits inside a scored trigram is a fragment ("me know" -> "let me know");
        # upgrade to the best-scoring containing trigram BEFORE the overlap check
        if len(g.split()) == 2:
            for _, t in scored:
                if len(t.split()) == 3 and f" {g} " in f" {t} ":
                    return t
        return g

    picked: list[str] = []
    for _, g in scored:
        g = fuller(g)
        # drop an n-gram overlapping an already-picked one ("you want i" after "want i can")
        if any(token_pairs(g) & token_pairs(p) for p in picked):
            continue
        picked.append(g)
        if len(picked) >= top:
            break
    return [{"phrase": g, "count": counts.get(g, 0)} for g in picked]


# ------------------------------------------------------------------------------ publishing


def condition_view(cond: dict, background: list[dict]) -> dict:
    s2 = cond["stage2"]
    pa = s2.get("primary_attractor")
    view = {
        "condition": cond["slug"],
        "temperature": s2.get("temperature"),
        "nRuns": s2.get("n_runs_total"),
        "nSampled": s2.get("n_runs_sampled"),
        "label": (pa or {}).get("label") or "no dominant attractor",
        "oneLine": (pa or {}).get("one_line") or "",
        "strength": strength(pa) if pa else "",
        "terminalForms": (pa or {}).get("terminal_form") or [],
        "phrases": signature_phrases(cond["stage1"], background),
    }
    return view


def headline_condition(conds: list[dict]) -> dict:
    for t in HEADLINE_TEMPS:
        for c in conds:
            if c["stage2"].get("temperature") == t:
                return c
    return conds[0]


def write_transcript(cond: dict, trait: str, website: str, extra: dict) -> None:
    tdir = os.path.join(website, "src", "data", "steering-transcripts", trait)
    os.makedirs(tdir, exist_ok=True)
    run = representative_run(cond["raw"])
    s2 = cond["stage2"]
    payload = {
        "trait": trait,
        "condition": cond["slug"],
        "condition_label": extra["label"],
        "model": s2.get("model_a"),
        "temperature": s2.get("temperature"),
        "seed_prompt": run.get("seed_prompt"),
        "run_index": run.get("run_index"),
        "turns": [{"turn": t["turn"], "speaker": t["speaker"], "model": t["model"],
                   "content_clean": t["content_clean"]} for t in run["turns"]],
    }
    json.dump(payload, open(os.path.join(tdir, cond["slug"] + ".json"), "w"), ensure_ascii=False)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--website", default=DEFAULT_WEBSITE)
    args = p.parse_args()
    print(f"Publishing steering results to {args.website}")

    # gather: trait -> method -> [conditions]; unsteer kept separate as trait -> [(k, cond)]
    by_trait: dict[str, dict[str, list[dict]]] = {t: {} for t in TRAITS}
    unsteer: dict[str, list[tuple[int, dict]]] = {t: [] for t in TRAITS}
    for exp_dir in sorted(glob.glob(os.path.join(ROOT, "*_ai2ai"))):
        parsed = parse_experiment_dir(os.path.basename(exp_dir))
        if not parsed:
            continue
        trait, method, params = parsed
        conds = collect_conditions(exp_dir)
        if not conds:
            continue
        if method == "unsteer":
            for c in conds:
                unsteer[trait].append((params["k"], c))
        else:
            for c in conds:
                c["params"] = params
            # a trait may have two pvec dirs (retuned coef); keep the one with more judged conds,
            # then the higher coef (later tuning) on ties
            if method == "pvec" and method in by_trait[trait]:
                old = by_trait[trait][method]
                if (len(conds), conds[0]["params"]["coef"]) <= (len(old), old[0]["params"]["coef"]):
                    print(f"    [note] {exp_dir}: superseded pvec variant skipped")
                    continue
                print(f"    [note] {trait}/pvec: replacing {old[0]['params']} with {conds[0]['params']}")
            by_trait[trait][method] = conds

    baseline_conds = collect_conditions(os.path.join(ROOT, "base_ai2ai"))

    # background corpus for phrase lift = every published condition (baseline included)
    all_conds = baseline_conds + [c for t in TRAITS for cs in by_trait[t].values() for c in cs] \
        + [c for t in TRAITS for _, c in unsteer[t]]
    rates_by_slug = {id(c): _ngram_rates(c["stage1"]) for c in all_conds if c["stage1"]}

    def background_for(cond: dict) -> list[dict]:
        return [r for key, r in rates_by_slug.items() if key != id(cond)]

    sdir = os.path.join(args.website, "src", "data", "steering")
    os.makedirs(sdir, exist_ok=True)

    # baseline: the unsteered base model, headline condition only (plus per-temp views)
    if baseline_conds:
        hc = headline_condition(baseline_conds)
        baseline = {
            "model": "Llama 3.1 8B Instruct",
            "headline": condition_view(hc, background_for(hc)),
            "conditions": [condition_view(c, background_for(c)) for c in baseline_conds],
            "lastUpdated": date.today().isoformat(),
        }
        json.dump(baseline, open(os.path.join(sdir, "_baseline.json"), "w"),
                  ensure_ascii=False, indent=1)
        print(f"  baseline: {baseline['headline']['label'][:60]}")

    published_traits = 0
    for trait in TRAITS:
        methods_out = []
        for key, label, order in METHODS:
            conds = by_trait[trait].get(key)
            if not conds:
                continue
            hc = headline_condition(conds)
            views = []
            for c in conds:
                v = condition_view(c, background_for(c))
                write_transcript(c, trait, args.website, {"label": f"{label} · temp {v['temperature']}"})
                views.append(v)
            entry = {
                "method": key, "methodLabel": label, "order": order,
                "params": hc.get("params") or {},
                "headline": next(v for v in views if v["condition"] == hc["slug"]),
                "conditions": views,
                "characterization": hc["stage2"].get("characterization") or "",
            }
            methods_out.append(entry)

        persistence_out = []
        for k, c in sorted(unsteer[trait], key=lambda kc: kc[0]):
            v = condition_view(c, background_for(c))
            v["k"] = k
            write_transcript(c, trait, args.website,
                             {"label": f"Steered first {k} turns, then released · temp {v['temperature']}"})
            persistence_out.append(v)

        if not methods_out and not persistence_out:
            print(f"  {trait:14} SKIP (no judged data)")
            continue
        payload = {
            "trait": trait,
            "methods": sorted(methods_out, key=lambda m: m["order"]),
            "persistence": persistence_out,
            "runs": sum(v["nRuns"] or 0 for m in methods_out for v in m["conditions"])
                    + sum(v["nRuns"] or 0 for v in persistence_out),
            "lastUpdated": date.today().isoformat(),
        }
        json.dump(payload, open(os.path.join(sdir, trait + ".json"), "w"),
                  ensure_ascii=False, indent=1)
        published_traits += 1
        print(f"  {trait:14} methods={[m['method'] for m in methods_out]} "
              f"persistence_k={[v['k'] for v in persistence_out]}")

    # prune stale transcripts (fully pipeline-generated dir)
    tbase = os.path.join(args.website, "src", "data", "steering-transcripts")
    valid = set()
    for trait in TRAITS:
        tj = load_json(os.path.join(sdir, trait + ".json"))
        if not tj:
            continue
        for m in tj["methods"]:
            valid |= {(trait, v["condition"]) for v in m["conditions"]}
        valid |= {(trait, v["condition"]) for v in tj["persistence"]}
    if os.path.isdir(tbase):
        for trait in os.listdir(tbase):
            tdir = os.path.join(tbase, trait)
            if not os.path.isdir(tdir):
                continue
            for fn in os.listdir(tdir):
                if fn.endswith(".json") and (trait, fn.removesuffix(".json")) not in valid:
                    os.remove(os.path.join(tdir, fn))
                    print(f"    removed stale transcript {trait}/{fn}")

    print(f"DONE — {published_traits} traits published")


if __name__ == "__main__":
    main()
